# v16.0.0 → v16.0.1 · 最優先の変更候補 (12)

[一覧の目次](README.md)

<a id="compare-631deed3d253ceef494094fcc5f4c290"></a>

### [`005166c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005166c8.md) → [`00516708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516708.md) FUN_00516708

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

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
      "definition_site": "00516740",
      "incomplete_value": true,
      "site": "00516740",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00516700",
      "incomplete_value": true,
      "site": "00516700",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00516730",
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
      "00516730",
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

- 旧版 [`005166e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005166c8.md#insn-005166e4) · [`0051670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005166c8.md#insn-0051670c) · [`0051671c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005166c8.md#insn-0051671c)
- 新版 `00516724`（命令位置の公開資料なし） · `0051674c`（命令位置の公開資料なし） · `0051675c`（命令位置の公開資料なし）

~~~diff
- 005166e4 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 005166e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005166e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005166e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516724 ["COPY", "tmp:0:8", ["const:f6d:8"]]
+ 00516724 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516724 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516724 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005166e4 bytes 29813a91
+ 00516724 bytes 29b53d91
- 0051670c ["INT_ADD", "register:40f0:8", ["const:51670c:8", "const:4:8"]]
- 0051670c ["CALL", null, ["callee:00c58690:8"]]
+ 0051674c ["INT_ADD", "register:40f0:8", ["const:51674c:8", "const:4:8"]]
+ 0051674c ["CALL", null, ["callee:00c58690:8"]]
- 0051670c bytes e1061d94
+ 0051674c bytes d1071d94
- 0051671c ["INT_ADD", "register:40f0:8", ["const:51671c:8", "const:4:8"]]
- 0051671c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051675c ["INT_ADD", "register:40f0:8", ["const:51675c:8", "const:4:8"]]
+ 0051675c ["CALL", null, ["callee:00c57eb0:8"]]
- 0051671c bytes e5041d94
+ 0051675c bytes d5051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2cdfde7e976fc64b99c2244085f725d"></a>

### [`00516770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516770.md) → [`005167b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/005167b0.md) FUN_005167b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

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
      "definition_site": "005167e8",
      "incomplete_value": true,
      "site": "005167e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005167a8",
      "incomplete_value": true,
      "site": "005167a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "005167d8",
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
      "005167d8",
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

- 旧版 [`0051678c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516770.md#insn-0051678c) · [`005167b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516770.md#insn-005167b4) · [`005167c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516770.md#insn-005167c4)
- 新版 `005167cc`（命令位置の公開資料なし） · `005167f4`（命令位置の公開資料なし） · `00516804`（命令位置の公開資料なし）

~~~diff
- 0051678c ["COPY", "tmp:0:8", ["const:6ad:8"]]
- 0051678c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051678c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051678c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005167cc ["COPY", "tmp:0:8", ["const:789:8"]]
+ 005167cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005167cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005167cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051678c bytes 29b51a91
+ 005167cc bytes 29251e91
- 005167b4 ["INT_ADD", "register:40f0:8", ["const:5167b4:8", "const:4:8"]]
- 005167b4 ["CALL", null, ["callee:00c58690:8"]]
+ 005167f4 ["INT_ADD", "register:40f0:8", ["const:5167f4:8", "const:4:8"]]
+ 005167f4 ["CALL", null, ["callee:00c58690:8"]]
- 005167b4 bytes b7061d94
+ 005167f4 bytes a7071d94
- 005167c4 ["INT_ADD", "register:40f0:8", ["const:5167c4:8", "const:4:8"]]
- 005167c4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00516804 ["INT_ADD", "register:40f0:8", ["const:516804:8", "const:4:8"]]
+ 00516804 ["CALL", null, ["callee:00c57eb0:8"]]
- 005167c4 bytes bb041d94
+ 00516804 bytes ab051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-016b3d18c23c32dbf3ed711e7d2e8571"></a>

### [`00516818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516818.md) → [`00516858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516858.md) FUN_00516858

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

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
      "definition_site": "00516890",
      "incomplete_value": true,
      "site": "00516890",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00516850",
      "incomplete_value": true,
      "site": "00516850",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00516880",
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
      "00516880",
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

- 旧版 [`00516834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516818.md#insn-00516834) · [`0051685c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516818.md#insn-0051685c) · [`0051686c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516818.md#insn-0051686c)
- 新版 `00516874`（命令位置の公開資料なし） · `0051689c`（命令位置の公開資料なし） · `005168ac`（命令位置の公開資料なし）

~~~diff
- 00516834 ["COPY", "tmp:0:8", ["const:49d:8"]]
- 00516834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00516834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00516834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516874 ["COPY", "tmp:0:8", ["const:4dd:8"]]
+ 00516874 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516874 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516874 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00516834 bytes 29751291
+ 00516874 bytes 29751391
- 0051685c ["INT_ADD", "register:40f0:8", ["const:51685c:8", "const:4:8"]]
- 0051685c ["CALL", null, ["callee:00c58690:8"]]
+ 0051689c ["INT_ADD", "register:40f0:8", ["const:51689c:8", "const:4:8"]]
+ 0051689c ["CALL", null, ["callee:00c58690:8"]]
- 0051685c bytes 8d061d94
+ 0051689c bytes 7d071d94
- 0051686c ["INT_ADD", "register:40f0:8", ["const:51686c:8", "const:4:8"]]
- 0051686c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005168ac ["INT_ADD", "register:40f0:8", ["const:5168ac:8", "const:4:8"]]
+ 005168ac ["CALL", null, ["callee:00c57eb0:8"]]
- 0051686c bytes 91041d94
+ 005168ac bytes 81051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25d87d45760cd5b726d3161d7094161c"></a>

### [`005168c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005168c0.md) → [`00516900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516900.md) FUN_00516900

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

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
      "definition_site": "00516938",
      "incomplete_value": true,
      "site": "00516938",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005168f8",
      "incomplete_value": true,
      "site": "005168f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00516928",
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
      "00516928",
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

- 旧版 [`005168dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005168c0.md#insn-005168dc) · [`00516904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005168c0.md#insn-00516904) · [`00516914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005168c0.md#insn-00516914)
- 新版 `0051691c`（命令位置の公開資料なし） · `00516944`（命令位置の公開資料なし） · `00516954`（命令位置の公開資料なし）

~~~diff
- 005168dc ["COPY", "tmp:0:8", ["const:701:8"]]
- 005168dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005168dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005168dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051691c ["COPY", "tmp:0:8", ["const:741:8"]]
+ 0051691c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051691c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051691c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005168dc bytes 29051c91
+ 0051691c bytes 29051d91
- 00516904 ["INT_ADD", "register:40f0:8", ["const:516904:8", "const:4:8"]]
- 00516904 ["CALL", null, ["callee:00c58690:8"]]
+ 00516944 ["INT_ADD", "register:40f0:8", ["const:516944:8", "const:4:8"]]
+ 00516944 ["CALL", null, ["callee:00c58690:8"]]
- 00516904 bytes 63061d94
+ 00516944 bytes 53071d94
- 00516914 ["INT_ADD", "register:40f0:8", ["const:516914:8", "const:4:8"]]
- 00516914 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00516954 ["INT_ADD", "register:40f0:8", ["const:516954:8", "const:4:8"]]
+ 00516954 ["CALL", null, ["callee:00c57eb0:8"]]
- 00516914 bytes 67041d94
+ 00516954 bytes 57051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bda9e7cc40a21c374a99d4b297448641"></a>

### [`00516968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516968.md) → [`005169a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/005169a8.md) FUN_005169a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

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
      "definition_site": "005169e0",
      "incomplete_value": true,
      "site": "005169e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005169a0",
      "incomplete_value": true,
      "site": "005169a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "005169d0",
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
      "005169d0",
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

- 旧版 [`00516984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516968.md#insn-00516984) · [`005169ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516968.md#insn-005169ac) · [`005169bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516968.md#insn-005169bc)
- 新版 `005169c4`（命令位置の公開資料なし） · `005169ec`（命令位置の公開資料なし） · `005169fc`（命令位置の公開資料なし）

~~~diff
- 00516984 ["COPY", "tmp:0:8", ["const:3d7:8"]]
- 00516984 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00516984 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00516984 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005169c4 ["COPY", "tmp:0:8", ["const:417:8"]]
+ 005169c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005169c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005169c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00516984 bytes 295d0f91
+ 005169c4 bytes 295d1091
- 005169ac ["INT_ADD", "register:40f0:8", ["const:5169ac:8", "const:4:8"]]
- 005169ac ["CALL", null, ["callee:00c58690:8"]]
+ 005169ec ["INT_ADD", "register:40f0:8", ["const:5169ec:8", "const:4:8"]]
+ 005169ec ["CALL", null, ["callee:00c58690:8"]]
- 005169ac bytes 39061d94
+ 005169ec bytes 29071d94
- 005169bc ["INT_ADD", "register:40f0:8", ["const:5169bc:8", "const:4:8"]]
- 005169bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 005169fc ["INT_ADD", "register:40f0:8", ["const:5169fc:8", "const:4:8"]]
+ 005169fc ["CALL", null, ["callee:00c57eb0:8"]]
- 005169bc bytes 3d041d94
+ 005169fc bytes 2d051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99f790f2c7d5fe246a3882230fd19b9b"></a>

### [`00516a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516a10.md) → [`00516a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516a50.md) FUN_00516a50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

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
      "definition_site": "00516a78",
      "incomplete_value": true,
      "site": "00516a88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00516a38",
      "incomplete_value": true,
      "site": "00516a48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00516a78",
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
      "00516a78",
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

- 旧版 [`00516a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516a10.md#insn-00516a2c) · [`00516a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516a10.md#insn-00516a54) · [`00516a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516a10.md#insn-00516a64)
- 新版 `00516a6c`（命令位置の公開資料なし） · `00516a94`（命令位置の公開資料なし） · `00516aa4`（命令位置の公開資料なし）

~~~diff
- 00516a2c ["COPY", "tmp:0:8", ["const:a57:8"]]
- 00516a2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00516a2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00516a2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516a6c ["COPY", "tmp:0:8", ["const:a97:8"]]
+ 00516a6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516a6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516a6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00516a2c bytes 295d2991
+ 00516a6c bytes 295d2a91
- 00516a54 ["INT_ADD", "register:40f0:8", ["const:516a54:8", "const:4:8"]]
- 00516a54 ["CALL", null, ["callee:00c58690:8"]]
+ 00516a94 ["INT_ADD", "register:40f0:8", ["const:516a94:8", "const:4:8"]]
+ 00516a94 ["CALL", null, ["callee:00c58690:8"]]
- 00516a54 bytes 0f061d94
+ 00516a94 bytes ff061d94
- 00516a64 ["INT_ADD", "register:40f0:8", ["const:516a64:8", "const:4:8"]]
- 00516a64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00516aa4 ["INT_ADD", "register:40f0:8", ["const:516aa4:8", "const:4:8"]]
+ 00516aa4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00516a64 bytes 13041d94
+ 00516aa4 bytes 03051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2d8c8cc2506d475ae3b1a07981edcd6"></a>

### [`00516ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516ab8.md) → [`00516af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516af8.md) FUN_00516af8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 5件 [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 5件 [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516b40",
      "incomplete_value": true,
      "site": "00516b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00516b00",
      "incomplete_value": true,
      "site": "00516b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00516b40",
      "incomplete_value": true,
      "site": "00516b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00516b00",
      "incomplete_value": true,
      "site": "00516b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00516b20",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "00516b2c",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "00516b40",
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
      "00516b20",
      "READ",
      [
        "storage",
        "00c9b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "00516b2c",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00516b40",
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

- 旧版 [`00516ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516ab8.md#insn-00516ad0) · [`00516ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516ab8.md#insn-00516ae0) · [`00516ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516ab8.md#insn-00516ae8)
- 新版 `00516b10`（命令位置の公開資料なし） · `00516b20`（命令位置の公開資料なし）

~~~diff
- 00516ad0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00516b10 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00516ad0 bytes 283c0090
+ 00516b10 bytes 283c00b0
- 00516ae0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
- 00516ae0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00516b20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
+ 00516b20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00516ae0 bytes 08f146f9
+ 00516b20 bytes 08f140f9
- 00516ae8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00516ae8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27cb4fb5f77735c0f8966834fc830f32"></a>

### [`00516dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516dac.md) → [`00516dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516dec.md) _ZNK5Botan10Extensions20get_extension_objectERKNS_3OIDE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c596c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596c0.md) · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 1件 [`00c59ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ac0.md) · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.37% / 新版 94.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00516ee4",
      "incomplete_value": false,
      "site": "00516f04",
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
            "const:d32:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516ea4",
      "incomplete_value": false,
      "site": "00516ec4",
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
            "const:c65:8"
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
      "definition_site": "00516eec",
      "incomplete_value": false,
      "site": "00516f04",
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
      "definition_site": "00516eac",
      "incomplete_value": false,
      "site": "00516ec4",
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
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00516ef4",
      "incomplete_value": false,
      "site": "00516f04",
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
            "const:2b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516eb4",
      "incomplete_value": false,
      "site": "00516ec4",
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
            "const:277:8"
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
      "00516ee4",
      "PARAM",
      [
        "storage",
        "002a9c65",
        null,
        "string"
      ]
    ],
    [
      "00516eec",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "00516ef4",
      "PARAM",
      [
        "storage",
        "002c1277",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00516ee4",
      "PARAM",
      [
        "storage",
        "002a9d32",
        null,
        "string"
      ]
    ],
    [
      "00516eec",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "00516ef4",
      "PARAM",
      [
        "storage",
        "002c12b7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00516ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516dac.md#insn-00516ec4) · [`00516ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516dac.md#insn-00516ea4) · [`00516eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516dac.md#insn-00516eac)
- 新版 `00516f04`（命令位置の公開資料なし） · `00516ee4`（命令位置の公開資料なし） · `00516eec`（命令位置の公開資料なし）

~~~diff
- 00516ec4 ["INT_ADD", "register:40f0:8", ["const:516ec4:8", "const:4:8"]]
- 00516ec4 ["CALL", null, ["callee:00c58650:8"]]
+ 00516f04 ["INT_ADD", "register:40f0:8", ["const:516f04:8", "const:4:8"]]
+ 00516f04 ["CALL", null, ["callee:00c58650:8"]]
- 00516ec4 bytes e3041d94
+ 00516f04 bytes d3051d94
- 00516ea4 ["COPY", "tmp:0:8", ["const:c65:8"]]
- 00516ea4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00516ea4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00516ea4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00516ee4 ["COPY", "tmp:0:8", ["const:d32:8"]]
+ 00516ee4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00516ee4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00516ee4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00516ea4 bytes 00943191
+ 00516ee4 bytes 00c83491
- 00516eac ["COPY", "tmp:0:8", ["const:30e:8"]]
- 00516eac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00516eac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00516eac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00516eec ["COPY", "tmp:0:8", ["const:3ea:8"]]
+ 00516eec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00516eec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00516eec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00516eac bytes 21380c91
+ 00516eec bytes 21a80f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ace1aa12d09f6a8a12d72b4876e17a6"></a>

### [`00516ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516ec8.md) → [`00516f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516f08.md) _ZNK5Botan10Extensions10extensionsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a00.md) · 呼出先 3件 [`0054c0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c0ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 1件 [`00c59e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e00.md) · 呼出先 3件 [`0054c0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c0ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.06% / 新版 95.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517024",
      "incomplete_value": false,
      "site": "00517044",
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
            "const:d32:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516fe4",
      "incomplete_value": false,
      "site": "00517004",
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
            "const:c65:8"
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
      "definition_site": "0051702c",
      "incomplete_value": false,
      "site": "00517044",
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
      "definition_site": "00516fec",
      "incomplete_value": false,
      "site": "00517004",
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
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517034",
      "incomplete_value": false,
      "site": "00517044",
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
            "const:2b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516ff4",
      "incomplete_value": false,
      "site": "00517004",
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
            "const:277:8"
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
      "00517024",
      "PARAM",
      [
        "storage",
        "002a9c65",
        null,
        "string"
      ]
    ],
    [
      "0051702c",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "00517034",
      "PARAM",
      [
        "storage",
        "002c1277",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00517024",
      "PARAM",
      [
        "storage",
        "002a9d32",
        null,
        "string"
      ]
    ],
    [
      "0051702c",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "00517034",
      "PARAM",
      [
        "storage",
        "002c12b7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516ec8.md#insn-00517004) · [`00516f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516ec8.md#insn-00516f44) · [`00516f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516ec8.md#insn-00516f7c)
- 新版 `00517044`（命令位置の公開資料なし） · `00516f84`（命令位置の公開資料なし） · `00516fbc`（命令位置の公開資料なし）

~~~diff
- 00517004 ["INT_ADD", "register:40f0:8", ["const:517004:8", "const:4:8"]]
- 00517004 ["CALL", null, ["callee:00c58650:8"]]
+ 00517044 ["INT_ADD", "register:40f0:8", ["const:517044:8", "const:4:8"]]
+ 00517044 ["CALL", null, ["callee:00c58650:8"]]
- 00517004 bytes 93041d94
+ 00517044 bytes 83051d94
- 00516f44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00516f44 ["INT_ADD", "register:40f0:8", ["const:516f44:8", "const:4:8"]]
- 00516f44 ["CALLIND", null, ["register:0:8"]]
+ 00516f84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00516f84 ["INT_ADD", "register:40f0:8", ["const:516f84:8", "const:4:8"]]
+ 00516f84 ["CALLIND", null, ["register:0:8"]]
- 00516f44 bytes 00013fd6
+ 00516f84 bytes 00013fd6
- 00516f7c ["INT_ADD", "register:40f0:8", ["const:516f7c:8", "const:4:8"]]
- 00516f7c ["CALL", null, ["callee:0054c0ec:8"]]
+ 00516fbc ["INT_ADD", "register:40f0:8", ["const:516fbc:8", "const:4:8"]]
+ 00516fbc ["CALL", null, ["callee:0054c0ec:8"]]
- 00516f7c bytes 4cd40094
+ 00516fbc bytes 4cd40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73c20509e44b9834302c28eb92faa4ef"></a>

### [`00517250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517250.md) → [`00517290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517290.md) _ZNK5Botan10Extensions11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0051209c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051209c.md) · 呼出先 9件 [`00517448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517448.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005120dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005120dc.md) · 呼出先 9件 [`00517488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517488.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517430",
      "incomplete_value": false,
      "site": "00517450",
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
            "const:d32:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005173f0",
      "incomplete_value": false,
      "site": "00517410",
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
            "const:c65:8"
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
      "definition_site": "00517438",
      "incomplete_value": false,
      "site": "00517450",
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
      "definition_site": "005173f8",
      "incomplete_value": false,
      "site": "00517410",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517440",
      "incomplete_value": false,
      "site": "00517450",
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
            "const:2b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517400",
      "incomplete_value": false,
      "site": "00517410",
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
            "const:277:8"
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
      "00517430",
      "PARAM",
      [
        "storage",
        "002a9c65",
        null,
        "string"
      ]
    ],
    [
      "00517438",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "00517440",
      "PARAM",
      [
        "storage",
        "002c1277",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00517430",
      "PARAM",
      [
        "storage",
        "002a9d32",
        null,
        "string"
      ]
    ],
    [
      "00517438",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "00517440",
      "PARAM",
      [
        "storage",
        "002c12b7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517250.md#insn-00517410) · [`005172a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517250.md#insn-005172a0) · [`005172b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517250.md#insn-005172b4)
- 新版 `00517450`（命令位置の公開資料なし） · `005172e0`（命令位置の公開資料なし） · `005172f4`（命令位置の公開資料なし）

~~~diff
- 00517410 ["INT_ADD", "register:40f0:8", ["const:517410:8", "const:4:8"]]
- 00517410 ["CALL", null, ["callee:00c58650:8"]]
+ 00517450 ["INT_ADD", "register:40f0:8", ["const:517450:8", "const:4:8"]]
+ 00517450 ["CALL", null, ["callee:00c58650:8"]]
- 00517410 bytes 90031d94
+ 00517450 bytes 80041d94
- 005172a0 ["INT_ADD", "register:40f0:8", ["const:5172a0:8", "const:4:8"]]
- 005172a0 ["CALL", null, ["callee:00517488:8"]]
+ 005172e0 ["INT_ADD", "register:40f0:8", ["const:5172e0:8", "const:4:8"]]
+ 005172e0 ["CALL", null, ["callee:00517488:8"]]
- 005172a0 bytes 6a000094
+ 005172e0 bytes 6a000094
- 005172b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005172b4 ["INT_ADD", "register:40f0:8", ["const:5172b4:8", "const:4:8"]]
- 005172b4 ["CALLIND", null, ["register:0:8"]]
+ 005172f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005172f4 ["INT_ADD", "register:40f0:8", ["const:5172f4:8", "const:4:8"]]
+ 005172f4 ["CALLIND", null, ["register:0:8"]]
- 005172b4 bytes 00013fd6
+ 005172f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f55507e91eef0c7c80938f3d540a74ec"></a>

### [`00517448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517448.md) → [`00517488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517488.md) FUN_00517488

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00517250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517250.md) [`0053c3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c3cc.md) [`0054a284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a284.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 3件 [`00517290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517290.md) [`0053c40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c40c.md) [`0054a2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a2c4.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005174c4",
      "incomplete_value": true,
      "site": "005174c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00517484",
      "incomplete_value": true,
      "site": "00517488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005174b4",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "005174c8",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005174b4",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "005174c8",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517448.md#insn-00517474) · [`0051749c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517448.md#insn-0051749c) · [`005174b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517448.md#insn-005174b4)
- 新版 `005174b4`（命令位置の公開資料なし） · `005174dc`（命令位置の公開資料なし） · `005174f4`（命令位置の公開資料なし）

~~~diff
- 00517474 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
- 00517474 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005174b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
+ 005174b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00517474 bytes 08a144f9
+ 005174b4 bytes 08a146f9
- 0051749c ["INT_ADD", "register:40f0:8", ["const:51749c:8", "const:4:8"]]
- 0051749c ["CALL", null, ["callee:00c57e90:8"]]
+ 005174dc ["INT_ADD", "register:40f0:8", ["const:5174dc:8", "const:4:8"]]
+ 005174dc ["CALL", null, ["callee:00c57e90:8"]]
- 0051749c bytes 7d011d94
+ 005174dc bytes 6d021d94
- 005174b4 ["INT_ADD", "register:40f0:8", ["const:5174b4:8", "const:4:8"]]
- 005174b4 ["CALL", null, ["callee:00c58000:8"]]
+ 005174f4 ["INT_ADD", "register:40f0:8", ["const:5174f4:8", "const:4:8"]]
+ 005174f4 ["CALL", null, ["callee:00c58000:8"]]
- 005174b4 bytes d3011d94
+ 005174f4 bytes c3021d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f66c582865e1e4c2ad81ed910130816"></a>

### [`00517610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517610.md) → [`00517650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517650.md) _ZN5Botan10Extensions11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0050372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md) [`00513270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md) · 呼出先 21件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00517bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517bf4.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`0054b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md)
- 新版 呼出元 2件 [`0050376c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/0050376c.md) [`005132b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/005132b0.md) · 呼出先 21件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00517c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517c34.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`0054b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005177c0",
      "incomplete_value": true,
      "site": "005177c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517780",
      "incomplete_value": true,
      "site": "00517780",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051795c",
      "incomplete_value": true,
      "site": "0051795c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051791c",
      "incomplete_value": true,
      "site": "0051791c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005176d8",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "005177b0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00517808",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005176d8",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "005177b0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00517808",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517610.md#insn-00517740) · [`00517780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517610.md#insn-00517780) · [`0051791c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517610.md#insn-0051791c)
- 新版 `00517780`（命令位置の公開資料なし） · `005177c0`（命令位置の公開資料なし） · `0051795c`（命令位置の公開資料なし）

~~~diff
- 00517740 ["INT_ADD", "register:40f0:8", ["const:517740:8", "const:4:8"]]
- 00517740 ["CALL", null, ["callee:00c588a0:8"]]
+ 00517780 ["INT_ADD", "register:40f0:8", ["const:517780:8", "const:4:8"]]
+ 00517780 ["CALL", null, ["callee:00c588a0:8"]]
- 00517740 bytes 58031d94
+ 00517780 bytes 48041d94
- 00517780 ["COPY", "register:0:8", ["register:4048:8"]]
- 00517780 ["INT_ADD", "register:40f0:8", ["const:517780:8", "const:4:8"]]
- 00517780 ["CALLIND", null, ["register:0:8"]]
+ 005177c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005177c0 ["INT_ADD", "register:40f0:8", ["const:5177c0:8", "const:4:8"]]
+ 005177c0 ["CALLIND", null, ["register:0:8"]]
- 00517780 bytes 20013fd6
+ 005177c0 bytes 20013fd6
- 0051791c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051791c ["INT_ADD", "register:40f0:8", ["const:51791c:8", "const:4:8"]]
- 0051791c ["CALLIND", null, ["register:0:8"]]
+ 0051795c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051795c ["INT_ADD", "register:40f0:8", ["const:51795c:8", "const:4:8"]]
+ 0051795c ["CALLIND", null, ["register:0:8"]]
- 0051791c bytes 20013fd6
+ 0051795c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acaba10507b3a7db9c3f69647f82b425"></a>

### [`00517bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517bf4.md) → [`00517c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517c34.md) FUN_00517c34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00517610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517610.md) · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00517650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517650.md) · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00517c84",
      "incomplete_value": true,
      "site": "00517c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00517c44",
      "incomplete_value": true,
      "site": "00517c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00517c70",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "00517c84",
      "DATA",
      [
        "storage",
        "00c6a038",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00517c70",
      "READ",
      [
        "storage",
        "00c9b120",
        null,
        "pointer"
      ]
    ],
    [
      "00517c84",
      "DATA",
      [
        "storage",
        "00c6a438",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517bf4.md#insn-00517c20) · [`00517c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517bf4.md#insn-00517c28) · [`00517c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517bf4.md#insn-00517c30)
- 新版 `00517c60`（命令位置の公開資料なし） · `00517c68`（命令位置の公開資料なし） · `00517c70`（命令位置の公開資料なし）

~~~diff
- 00517c20 ["INT_ADD", "register:40f0:8", ["const:517c20:8", "const:4:8"]]
- 00517c20 ["CALL", null, ["callee:00c57e90:8"]]
+ 00517c60 ["INT_ADD", "register:40f0:8", ["const:517c60:8", "const:4:8"]]
+ 00517c60 ["CALL", null, ["callee:00c57e90:8"]]
- 00517c20 bytes 9cff1c94
+ 00517c60 bytes 8c001d94
- 00517c28 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00517c68 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00517c28 bytes 083c00f0
+ 00517c68 bytes 283c0090
- 00517c30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
- 00517c30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00517c70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:120:8"]]
+ 00517c70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00517c30 bytes 089146f9
+ 00517c70 bytes 089140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0b25292407f50de766ffe50cd3e83f7"></a>

### [`00517ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517ce8.md) → [`00517d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517d28.md) _ZNK5Botan10Extensions11contents_toERNS_10Data_StoreES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a20.md) · 呼出先 6件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 1件 [`00c59e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e20.md) · 呼出先 6件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517ea8",
      "incomplete_value": false,
      "site": "00517ec8",
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
            "const:d32:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517e68",
      "incomplete_value": false,
      "site": "00517e88",
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
            "const:c65:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517eb0",
      "incomplete_value": false,
      "site": "00517ec8",
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
      "definition_site": "00517e70",
      "incomplete_value": false,
      "site": "00517e88",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517eb8",
      "incomplete_value": false,
      "site": "00517ec8",
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
            "const:2b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517e78",
      "incomplete_value": false,
      "site": "00517e88",
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
            "const:277:8"
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
      "00517db4",
      "PARAM",
      [
        "storage",
        "002b613e",
        null,
        "string"
      ]
    ],
    [
      "00517ea8",
      "PARAM",
      [
        "storage",
        "002a9c65",
        null,
        "string"
      ]
    ],
    [
      "00517eb0",
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
      "00517db4",
      "PARAM",
      [
        "storage",
        "002b617e",
        null,
        "string"
      ]
    ],
    [
      "00517ea8",
      "PARAM",
      [
        "storage",
        "002a9d32",
        null,
        "string"
      ]
    ],
    [
      "00517eb0",
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

- 旧版 [`00517e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517ce8.md#insn-00517e88) · [`00517d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517ce8.md#insn-00517d28) · [`00517d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517ce8.md#insn-00517d54)
- 新版 `00517ec8`（命令位置の公開資料なし） · `00517d68`（命令位置の公開資料なし） · `00517d94`（命令位置の公開資料なし）

~~~diff
- 00517e88 ["INT_ADD", "register:40f0:8", ["const:517e88:8", "const:4:8"]]
- 00517e88 ["CALL", null, ["callee:00c58650:8"]]
+ 00517ec8 ["INT_ADD", "register:40f0:8", ["const:517ec8:8", "const:4:8"]]
+ 00517ec8 ["CALL", null, ["callee:00c58650:8"]]
- 00517e88 bytes f2001d94
+ 00517ec8 bytes e2011d94
- 00517d28 ["COPY", "tmp:0:8", ["const:13e:8"]]
- 00517d28 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00517d28 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00517d28 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00517d68 ["COPY", "tmp:0:8", ["const:17e:8"]]
+ 00517d68 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00517d68 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00517d68 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00517d28 bytes b5fa0491
+ 00517d68 bytes b5fa0591
- 00517d54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00517d54 ["INT_ADD", "register:40f0:8", ["const:517d54:8", "const:4:8"]]
- 00517d54 ["CALLIND", null, ["register:0:8"]]
+ 00517d94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00517d94 ["INT_ADD", "register:40f0:8", ["const:517d94:8", "const:4:8"]]
+ 00517d94 ["CALLIND", null, ["register:0:8"]]
- 00517d54 bytes 00013fd6
+ 00517d94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efb13317b5087df98b3c55febe0a91fc"></a>

### [`00518160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518160.md) → [`005181a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/005181a0.md) _ZN5Botan14Cert_Extension17Basic_Constraints12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 8件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md) [`00c58310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58310.md) [`00c58480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58480.md)
- 新版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 8件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md) [`00c58710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58710.md) [`00c58880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58880.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00518200",
      "incomplete_value": false,
      "site": "00518210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ce000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005181c0",
      "incomplete_value": false,
      "site": "005181d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ce000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 5
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00518254",
      "incomplete_value": true,
      "site": "00518254",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "00518214",
      "incomplete_value": true,
      "site": "00518214",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "00518298",
      "incomplete_value": true,
      "site": "00518298",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "00518258",
      "incomplete_value": true,
      "site": "00518258",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "00518200",
      "PARAM",
      [
        "storage",
        "002ce480",
        null,
        null
      ]
    ],
    [
      "00518244",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00518288",
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
      "00518200",
      "PARAM",
      [
        "storage",
        "002ce4c0",
        null,
        null
      ]
    ],
    [
      "00518244",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00518288",
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

- 旧版 [`005181d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518160.md#insn-005181d0) · [`005181d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518160.md#insn-005181d4) · [`00518214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518160.md#insn-00518214)
- 新版 `00518210`（命令位置の公開資料なし） · `00518214`（命令位置の公開資料なし） · `00518254`（命令位置の公開資料なし）

~~~diff
- 005181d0 ["INT_ADD", "register:40f0:8", ["const:5181d0:8", "const:4:8"]]
- 005181d0 ["CALL", null, ["callee:00c59460:8"]]
+ 00518210 ["INT_ADD", "register:40f0:8", ["const:518210:8", "const:4:8"]]
+ 00518210 ["CALL", null, ["callee:00c59460:8"]]
- 005181d0 bytes a4031d94
+ 00518210 bytes 94041d94
- 005181d4 ["INT_ADD", "register:40f0:8", ["const:5181d4:8", "const:4:8"]]
- 005181d4 ["CALL", null, ["callee:00c58710:8"]]
+ 00518214 ["INT_ADD", "register:40f0:8", ["const:518214:8", "const:4:8"]]
+ 00518214 ["CALL", null, ["callee:00c58710:8"]]
- 005181d4 bytes 4f001d94
+ 00518214 bytes 3f011d94
- 00518214 ["COPY", "register:0:8", ["register:4048:8"]]
- 00518214 ["INT_ADD", "register:40f0:8", ["const:518214:8", "const:4:8"]]
- 00518214 ["CALLIND", null, ["register:0:8"]]
+ 00518254 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00518254 ["INT_ADD", "register:40f0:8", ["const:518254:8", "const:4:8"]]
+ 00518254 ["CALLIND", null, ["register:0:8"]]
- 00518214 bytes 20013fd6
+ 00518254 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ec8a7ea20d0a84fd58baf84434e9563"></a>

### [`005182d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/005182d4.md) → [`00518314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518314.md) _ZNK5Botan14Cert_Extension17Basic_Constraints11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58390.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58790.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 79.49% / 新版 79.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00518350",
      "incomplete_value": true,
      "site": "00518364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518310",
      "incomplete_value": true,
      "site": "00518324",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:42a:8"
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
      "definition_site": "00518354",
      "incomplete_value": true,
      "site": "00518368",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00518314",
      "incomplete_value": true,
      "site": "00518328",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00518358",
      "incomplete_value": true,
      "site": "0051836c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00518318",
      "incomplete_value": true,
      "site": "0051832c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00518350",
      "READ",
      [
        "storage",
        "002bb42a",
        null,
        "string"
      ]
    ],
    [
      "00518354",
      "READ",
      [
        "storage",
        "002bb437",
        null,
        "string"
      ]
    ],
    [
      "00518358",
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
      "00518350",
      "READ",
      [
        "storage",
        "002bb46a",
        null,
        "string"
      ]
    ],
    [
      "00518354",
      "READ",
      [
        "storage",
        "002bb477",
        null,
        "string"
      ]
    ],
    [
      "00518358",
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

- 旧版 [`0051835c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/005182d4.md#insn-0051835c) · [`0051836c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/005182d4.md#insn-0051836c) · [`005183e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/005182d4.md#insn-005183e0)
- 新版 `0051839c`（命令位置の公開資料なし） · `005183ac`（命令位置の公開資料なし） · `00518420`（命令位置の公開資料なし）

~~~diff
- 0051835c ["INT_ADD", "register:40f0:8", ["const:51835c:8", "const:4:8"]]
- 0051835c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051839c ["INT_ADD", "register:40f0:8", ["const:51839c:8", "const:4:8"]]
+ 0051839c ["CALL", null, ["callee:00c57eb0:8"]]
- 0051835c bytes d5fd1c94
+ 0051839c bytes c5fe1c94
- 0051836c ["INT_ADD", "register:40f0:8", ["const:51836c:8", "const:4:8"]]
- 0051836c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005183ac ["INT_ADD", "register:40f0:8", ["const:5183ac:8", "const:4:8"]]
+ 005183ac ["CALL", null, ["callee:00c57eb0:8"]]
- 0051836c bytes d1fd1c94
+ 005183ac bytes c1fe1c94
- 005183e0 ["INT_ADD", "register:40f0:8", ["const:5183e0:8", "const:4:8"]]
- 005183e0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00518420 ["INT_ADD", "register:40f0:8", ["const:518420:8", "const:4:8"]]
+ 00518420 ["CALL", null, ["callee:00c57eb0:8"]]
- 005183e0 bytes b4fd1c94
+ 00518420 bytes a4fe1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0ee63e1b3fa4b3949ca5aeaa8642006"></a>

### [`00518458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518458.md) → [`00518498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518498.md) _ZNK5Botan14Cert_Extension9Key_Usage12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

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
      "definition_site": "00518760",
      "incomplete_value": false,
      "site": "00518768",
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
            "const:cca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518720",
      "incomplete_value": false,
      "site": "00518728",
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
            "const:c8a:8"
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
      "definition_site": "00518798",
      "incomplete_value": true,
      "site": "005187a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518758",
      "incomplete_value": true,
      "site": "00518764",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:998:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00518794",
      "incomplete_value": false,
      "site": "005187a4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "00518754",
      "incomplete_value": false,
      "site": "00518764",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 15,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00518760",
      "PARAM",
      [
        "storage",
        "002b0c8a",
        null,
        "string"
      ]
    ],
    [
      "00518794",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00518798",
      "READ",
      [
        "storage",
        "00c9a998",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00518760",
      "PARAM",
      [
        "storage",
        "002b0cca",
        null,
        "string"
      ]
    ],
    [
      "00518794",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00518798",
      "READ",
      [
        "storage",
        "00c9ad98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00518728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518458.md#insn-00518728) · [`00518764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518458.md#insn-00518764) · [`005184bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518458.md#insn-005184bc)
- 新版 `00518768`（命令位置の公開資料なし） · `005187a4`（命令位置の公開資料なし） · `005184fc`（命令位置の公開資料なし）

~~~diff
- 00518728 ["INT_ADD", "register:40f0:8", ["const:518728:8", "const:4:8"]]
- 00518728 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00518768 ["INT_ADD", "register:40f0:8", ["const:518768:8", "const:4:8"]]
+ 00518768 ["CALL", null, ["callee:0043ddd8:8"]]
- 00518728 bytes 9c95fc97
+ 00518768 bytes 9c95fc97
- 00518764 ["INT_ADD", "register:40f0:8", ["const:518764:8", "const:4:8"]]
- 00518764 ["CALL", null, ["callee:00c57f10:8"]]
+ 005187a4 ["INT_ADD", "register:40f0:8", ["const:5187a4:8", "const:4:8"]]
+ 005187a4 ["CALL", null, ["callee:00c57f10:8"]]
- 00518764 bytes ebfc1c94
+ 005187a4 bytes dbfd1c94
- 005184bc ["INT_ADD", "register:40f0:8", ["const:5184bc:8", "const:4:8"]]
- 005184bc ["CALL", null, ["callee:00c57e90:8"]]
+ 005184fc ["INT_ADD", "register:40f0:8", ["const:5184fc:8", "const:4:8"]]
+ 005184fc ["CALL", null, ["callee:00c57e90:8"]]
- 005184bc bytes 75fd1c94
+ 005184fc bytes 65fe1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e53b6bcadc4599bc4b32a83c345641f1"></a>

### [`0051882c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/0051882c.md) → [`0051886c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/0051886c.md) _ZN5Botan14Cert_Extension9Key_Usage12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 11件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 11件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.14% / 新版 91.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00518b24",
      "incomplete_value": true,
      "site": "00518b24",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "00518ae4",
      "incomplete_value": true,
      "site": "00518ae4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00518b68",
      "incomplete_value": true,
      "site": "00518b68",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "00518b28",
      "incomplete_value": true,
      "site": "00518b28",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00518ba8",
      "incomplete_value": false,
      "site": "00518bb0",
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
            "const:956:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518b68",
      "incomplete_value": false,
      "site": "00518b70",
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
            "const:916:8"
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
      "00518958",
      "READ",
      [
        "storage",
        "002c2270",
        null,
        null
      ]
    ],
    [
      "00518960",
      "READ",
      [
        "storage",
        "002c2420",
        null,
        null
      ]
    ],
    [
      "00518968",
      "READ",
      [
        "storage",
        "002c2800",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00518958",
      "READ",
      [
        "storage",
        "002c22b0",
        null,
        null
      ]
    ],
    [
      "00518960",
      "READ",
      [
        "storage",
        "002c2460",
        null,
        null
      ]
    ],
    [
      "00518968",
      "READ",
      [
        "storage",
        "002c2840",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00518ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/0051882c.md#insn-00518ae4) · [`00518b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/0051882c.md#insn-00518b28) · [`00518b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/0051882c.md#insn-00518b30)
- 新版 `00518b24`（命令位置の公開資料なし） · `00518b68`（命令位置の公開資料なし） · `00518b70`（命令位置の公開資料なし）

~~~diff
- 00518ae4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00518ae4 ["INT_ADD", "register:40f0:8", ["const:518ae4:8", "const:4:8"]]
- 00518ae4 ["CALLIND", null, ["register:0:8"]]
+ 00518b24 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00518b24 ["INT_ADD", "register:40f0:8", ["const:518b24:8", "const:4:8"]]
+ 00518b24 ["CALLIND", null, ["register:0:8"]]
- 00518ae4 bytes 20013fd6
+ 00518b24 bytes 20013fd6
- 00518b28 ["COPY", "register:0:8", ["register:4048:8"]]
- 00518b28 ["INT_ADD", "register:40f0:8", ["const:518b28:8", "const:4:8"]]
- 00518b28 ["CALLIND", null, ["register:0:8"]]
+ 00518b68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00518b68 ["INT_ADD", "register:40f0:8", ["const:518b68:8", "const:4:8"]]
+ 00518b68 ["CALLIND", null, ["register:0:8"]]
- 00518b28 bytes 20013fd6
+ 00518b68 bytes 20013fd6
- 00518b30 ["INT_ADD", "register:40f0:8", ["const:518b30:8", "const:4:8"]]
- 00518b30 ["CALL", null, ["callee:00c58660:8"]]
+ 00518b70 ["INT_ADD", "register:40f0:8", ["const:518b70:8", "const:4:8"]]
+ 00518b70 ["CALL", null, ["callee:00c58660:8"]]
- 00518b30 bytes ccfd1c94
+ 00518b70 bytes bcfe1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e2ed5c47880f84effff399114af1a26"></a>

### [`00518ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518ce0.md) → [`00518d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518d20.md) _ZNK5Botan14Cert_Extension9Key_Usage11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58390.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58790.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00518d58",
      "incomplete_value": true,
      "site": "00518d58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00518d18",
      "incomplete_value": true,
      "site": "00518d18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00518d50",
      "incomplete_value": true,
      "site": "00518d5c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00518d10",
      "incomplete_value": true,
      "site": "00518d1c",
      "value": [
        "LOAD",
        "8",
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
      "00518d40",
      "READ",
      [
        "storage",
        "002a9a8d",
        null,
        "string"
      ]
    ],
    [
      "00518d50",
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
      "00518d40",
      "READ",
      [
        "storage",
        "002a9b5a",
        null,
        "string"
      ]
    ],
    [
      "00518d50",
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

- 旧版 [`00518d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518ce0.md#insn-00518d5c) · [`00518cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518ce0.md#insn-00518cf8) · [`00518d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518ce0.md#insn-00518d2c)
- 新版 `00518d9c`（命令位置の公開資料なし） · `00518d38`（命令位置の公開資料なし） · `00518d6c`（命令位置の公開資料なし）

~~~diff
- 00518d5c ["INT_ADD", "register:40f0:8", ["const:518d5c:8", "const:4:8"]]
- 00518d5c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00518d9c ["INT_ADD", "register:40f0:8", ["const:518d9c:8", "const:4:8"]]
+ 00518d9c ["CALL", null, ["callee:00c57eb0:8"]]
- 00518d5c bytes 55fb1c94
+ 00518d9c bytes 45fc1c94
- 00518cf8 ["COPY", "tmp:0:8", ["const:a8d:8"]]
- 00518cf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00518cf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00518cf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00518d38 ["COPY", "tmp:0:8", ["const:b5a:8"]]
+ 00518d38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00518d38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00518d38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00518cf8 bytes 29352a91
+ 00518d38 bytes 29692d91
- 00518d2c ["INT_ADD", "register:40f0:8", ["const:518d2c:8", "const:4:8"]]
- 00518d2c ["CALL", null, ["callee:00c58790:8"]]
+ 00518d6c ["INT_ADD", "register:40f0:8", ["const:518d6c:8", "const:4:8"]]
+ 00518d6c ["CALL", null, ["callee:00c58790:8"]]
- 00518d2c bytes 99fd1c94
+ 00518d6c bytes 89fe1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3549914a2c1665239b5c8528ffa396f"></a>

### [`00518fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518fb0.md) → [`00518ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518ff0.md) _ZNK5Botan14Cert_Extension14Subject_Key_ID11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c596f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59af0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 80.49% / 新版 80.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051902c",
      "incomplete_value": true,
      "site": "0051903c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518fec",
      "incomplete_value": true,
      "site": "00518ffc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9f5:8"
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
      "definition_site": "00519030",
      "incomplete_value": true,
      "site": "00519040",
      "value": [
        "LOAD",
        "16",
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
                "const:b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518ff0",
      "incomplete_value": true,
      "site": "00519000",
      "value": [
        "LOAD",
        "16",
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
                "const:b:8"
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
      "definition_site": "00519034",
      "incomplete_value": true,
      "site": "00519044",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:680:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518ff4",
      "incomplete_value": true,
      "site": "00519004",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:640:8"
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
      "0051902c",
      "READ",
      [
        "storage",
        "002b29f5",
        null,
        "string"
      ]
    ],
    [
      "00519030",
      "READ",
      [
        "storage",
        "002b2a00",
        null,
        "string"
      ]
    ],
    [
      "00519034",
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
      "0051902c",
      "READ",
      [
        "storage",
        "002b2a35",
        null,
        "string"
      ]
    ],
    [
      "00519030",
      "READ",
      [
        "storage",
        "002b2a40",
        null,
        "string"
      ]
    ],
    [
      "00519034",
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

- 旧版 [`00518fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518fb0.md#insn-00518fdc) · [`00518fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518fb0.md#insn-00518fe4) · [`00518fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00518/00518fb0.md#insn-00518fe8)
- 新版 `0051901c`（命令位置の公開資料なし） · `00519024`（命令位置の公開資料なし）

~~~diff
- 00518fdc ["INT_ADD", "register:40f0:8", ["const:518fdc:8", "const:4:8"]]
- 00518fdc ["CALL", null, ["callee:00c57e90:8"]]
+ 0051901c ["INT_ADD", "register:40f0:8", ["const:51901c:8", "const:4:8"]]
+ 0051901c ["CALL", null, ["callee:00c57e90:8"]]
- 00518fdc bytes adfa1c94
+ 0051901c bytes 9dfb1c94
- 00518fe4 ["COPY", "tmp:0:8", ["const:9f5:8"]]
- 00518fe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00518fe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00518fe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00519024 ["COPY", "tmp:0:8", ["const:a35:8"]]
+ 00519024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00519024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00519024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00518fe4 bytes 08d52791
+ 00519024 bytes 08d52891
- 00518fe8 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 00518fe8 bytes 49edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb9e9990ca4f8180f3305cad35c0837d"></a>

### [`00519080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519080.md) → [`005190c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/005190c0.md) _ZN5Botan14Cert_Extension14Subject_Key_IDC2ERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEERKNS2_12basic_stringIcNS2_11char_traitsIcEENS4_IcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59940.md) · 呼出先 7件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c59d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d40.md) · 呼出先 7件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.46% / 新版 97.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00519100",
      "incomplete_value": true,
      "site": "00519108",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005190c0",
      "incomplete_value": true,
      "site": "005190c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005190fc",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "00519108",
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
      "005190fc",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ],
    [
      "00519108",
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

- 旧版 [`00519108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519080.md#insn-00519108) · [`005190a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519080.md#insn-005190a4) · [`005190bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519080.md#insn-005190bc)
- 新版 `00519148`（命令位置の公開資料なし） · `005190e4`（命令位置の公開資料なし） · `005190fc`（命令位置の公開資料なし）

~~~diff
- 00519108 ["COPY", "register:0:8", ["register:4040:8"]]
- 00519108 ["INT_ADD", "register:40f0:8", ["const:519108:8", "const:4:8"]]
- 00519108 ["CALLIND", null, ["register:0:8"]]
+ 00519148 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00519148 ["INT_ADD", "register:40f0:8", ["const:519148:8", "const:4:8"]]
+ 00519148 ["CALLIND", null, ["register:0:8"]]
- 00519108 bytes 00013fd6
+ 00519148 bytes 00013fd6
- 005190a4 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 005190e4 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 005190a4 bytes 093c00b0
+ 005190e4 bytes 093c00d0
- 005190bc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:db0:8"]]
- 005190bc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005190fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1b0:8"]]
+ 005190fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005190bc bytes 29d946f9
+ 005190fc bytes 29d940f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed2c2a5ed7d3b742cef7f9c30ee33708"></a>

### [`005193e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/005193e0.md) → [`00519420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519420.md) _ZN5Botan14Cert_Extension16Authority_Key_ID12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0050ac78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ac78.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md) [`00c58480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58480.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0050acb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050acb8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md) [`00c58880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58880.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005194b4",
      "incomplete_value": true,
      "site": "005194b4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00519474",
      "incomplete_value": true,
      "site": "00519474",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005194f8",
      "incomplete_value": true,
      "site": "005194f8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005194b8",
      "incomplete_value": true,
      "site": "005194b8",
      "value": [
        "LOAD",
        "8",
        [
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
      "005194a4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "005194e8",
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
      "005194a4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "005194e8",
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

- 旧版 [`00519434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/005193e0.md#insn-00519434) · [`00519474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/005193e0.md#insn-00519474) · [`005194b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/005193e0.md#insn-005194b8)
- 新版 `00519474`（命令位置の公開資料なし） · `005194b4`（命令位置の公開資料なし） · `005194f8`（命令位置の公開資料なし）

~~~diff
- 00519434 ["INT_ADD", "register:40f0:8", ["const:519434:8", "const:4:8"]]
- 00519434 ["CALL", null, ["callee:0050acb8:8"]]
+ 00519474 ["INT_ADD", "register:40f0:8", ["const:519474:8", "const:4:8"]]
+ 00519474 ["CALL", null, ["callee:0050acb8:8"]]
- 00519434 bytes 11c6ff97
+ 00519474 bytes 11c6ff97
- 00519474 ["COPY", "register:0:8", ["register:4048:8"]]
- 00519474 ["INT_ADD", "register:40f0:8", ["const:519474:8", "const:4:8"]]
- 00519474 ["CALLIND", null, ["register:0:8"]]
+ 005194b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005194b4 ["INT_ADD", "register:40f0:8", ["const:5194b4:8", "const:4:8"]]
+ 005194b4 ["CALLIND", null, ["register:0:8"]]
- 00519474 bytes 20013fd6
+ 005194b4 bytes 20013fd6
- 005194b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005194b8 ["INT_ADD", "register:40f0:8", ["const:5194b8:8", "const:4:8"]]
- 005194b8 ["CALLIND", null, ["register:0:8"]]
+ 005194f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005194f8 ["INT_ADD", "register:40f0:8", ["const:5194f8:8", "const:4:8"]]
+ 005194f8 ["CALLIND", null, ["register:0:8"]]
- 005194b8 bytes 20013fd6
+ 005194f8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca6cb1bd6e4f1dfd0e66adf96471c2d6"></a>

### [`00519528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519528.md) → [`00519568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519568.md) _ZNK5Botan14Cert_Extension16Authority_Key_ID11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c596f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59af0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005195b0",
      "incomplete_value": true,
      "site": "005195c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00519570",
      "incomplete_value": true,
      "site": "00519580",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4a7:8"
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
      "definition_site": "005195b4",
      "incomplete_value": true,
      "site": "005195c4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00519574",
      "incomplete_value": true,
      "site": "00519584",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005195b8",
      "incomplete_value": true,
      "site": "005195c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00519578",
      "incomplete_value": true,
      "site": "00519588",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005195b0",
      "READ",
      [
        "storage",
        "002bc4a7",
        null,
        "string"
      ]
    ],
    [
      "005195b4",
      "READ",
      [
        "storage",
        "002bc4b4",
        null,
        "string"
      ]
    ],
    [
      "005195b8",
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
      "005195b0",
      "READ",
      [
        "storage",
        "002bc4e7",
        null,
        "string"
      ]
    ],
    [
      "005195b4",
      "READ",
      [
        "storage",
        "002bc4f4",
        null,
        "string"
      ]
    ],
    [
      "005195b8",
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

- 旧版 [`00519560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519528.md#insn-00519560) · [`00519568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519528.md#insn-00519568) · [`0051956c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519528.md#insn-0051956c)
- 新版 `005195a0`（命令位置の公開資料なし） · `005195a8`（命令位置の公開資料なし）

~~~diff
- 00519560 ["INT_ADD", "register:40f0:8", ["const:519560:8", "const:4:8"]]
- 00519560 ["CALL", null, ["callee:00c57e90:8"]]
+ 005195a0 ["INT_ADD", "register:40f0:8", ["const:5195a0:8", "const:4:8"]]
+ 005195a0 ["CALL", null, ["callee:00c57e90:8"]]
- 00519560 bytes 4cf91c94
+ 005195a0 bytes 3cfa1c94
- 00519568 ["COPY", "tmp:0:8", ["const:4a7:8"]]
- 00519568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00519568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00519568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005195a8 ["COPY", "tmp:0:8", ["const:4e7:8"]]
+ 005195a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005195a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005195a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00519568 bytes 089d1291
+ 005195a8 bytes 089d1391
- 0051956c ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 0051956c bytes 49edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a50c6bf31d0b2d65a6acd8036c69bf55"></a>

### [`0051a008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a008.md) → [`0051a048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a048.md) _ZNK5Botan14Cert_Extension18Extended_Key_Usage11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58400.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58800.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051a08c",
      "incomplete_value": true,
      "site": "0051a0a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1f9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a04c",
      "incomplete_value": true,
      "site": "0051a064",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1b9:8"
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
      "definition_site": "0051a088",
      "incomplete_value": true,
      "site": "0051a0a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0051a048",
      "incomplete_value": true,
      "site": "0051a064",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0051a088",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ],
    [
      "0051a08c",
      "READ",
      [
        "storage",
        "002ba1b9",
        null,
        "string"
      ]
    ],
    [
      "0051a090",
      "READ",
      [
        "storage",
        "002ba1c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051a088",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ],
    [
      "0051a08c",
      "READ",
      [
        "storage",
        "002ba1f9",
        null,
        "string"
      ]
    ],
    [
      "0051a090",
      "READ",
      [
        "storage",
        "002ba208",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051a044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a008.md#insn-0051a044) · [`0051a048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a008.md#insn-0051a048) · [`0051a088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a008.md#insn-0051a088)
- 新版 `0051a084`（命令位置の公開資料なし） · `0051a088`（命令位置の公開資料なし） · `0051a0c8`（命令位置の公開資料なし）

~~~diff
- 0051a044 ["COPY", "tmp:0:8", ["const:1b9:8"]]
- 0051a044 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051a044 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051a044 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051a084 ["COPY", "tmp:0:8", ["const:1f9:8"]]
+ 0051a084 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051a084 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051a084 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051a044 bytes 29e50691
+ 0051a084 bytes 29e50791
- 0051a048 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:410:8"]]
- 0051a048 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0051a048 ["COPY", "register:5030:8", ["const:0:8"]]
- 0051a048 ["COPY", "register:5038:8", ["const:0:8"]]
+ 0051a088 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
+ 0051a088 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0051a088 ["COPY", "register:5030:8", ["const:0:8"]]
+ 0051a088 ["COPY", "register:5038:8", ["const:0:8"]]
- 0051a048 bytes 0105c13d
+ 0051a088 bytes 0115c13d
- 0051a088 ["INT_ADD", "register:40f0:8", ["const:51a088:8", "const:4:8"]]
- 0051a088 ["CALL", null, ["callee:00c57e90:8"]]
+ 0051a0c8 ["INT_ADD", "register:40f0:8", ["const:51a0c8:8", "const:4:8"]]
+ 0051a0c8 ["CALL", null, ["callee:00c57e90:8"]]
- 0051a088 bytes 82f61c94
+ 0051a0c8 bytes 72f71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c856f69ad7189f2abf9e5221bd3afb8e"></a>

### [`0051a158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a158.md) → [`0051a198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a198.md) _ZNK5Botan14Cert_Extension16Name_Constraints12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051a1d8",
      "incomplete_value": true,
      "site": "0051a1ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:65c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a198",
      "incomplete_value": true,
      "site": "0051a1ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:580:8"
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
      "definition_site": "0051a1dc",
      "incomplete_value": true,
      "site": "0051a1f0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0051a19c",
      "incomplete_value": true,
      "site": "0051a1b0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051a1e0",
      "incomplete_value": true,
      "site": "0051a1f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:790:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a1a0",
      "incomplete_value": true,
      "site": "0051a1b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:750:8"
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
      "0051a1d8",
      "READ",
      [
        "storage",
        "002a5580",
        null,
        "string"
      ]
    ],
    [
      "0051a1dc",
      "READ",
      [
        "storage",
        "002a5589",
        null,
        "string"
      ]
    ],
    [
      "0051a1e0",
      "READ",
      [
        "storage",
        "002c2750",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051a1d8",
      "READ",
      [
        "storage",
        "002a565c",
        null,
        "string"
      ]
    ],
    [
      "0051a1dc",
      "READ",
      [
        "storage",
        "002a5665",
        null,
        "string"
      ]
    ],
    [
      "0051a1e0",
      "READ",
      [
        "storage",
        "002c2790",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051a1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a158.md#insn-0051a1f0) · [`0051a17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a158.md#insn-0051a17c) · [`0051a188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a158.md#insn-0051a188)
- 新版 `0051a230`（命令位置の公開資料なし） · `0051a1bc`（命令位置の公開資料なし） · `0051a1c8`（命令位置の公開資料なし）

~~~diff
- 0051a1f0 ["INT_ADD", "register:40f0:8", ["const:51a1f0:8", "const:4:8"]]
- 0051a1f0 ["CALL", null, ["callee:00c57f10:8"]]
+ 0051a230 ["INT_ADD", "register:40f0:8", ["const:51a230:8", "const:4:8"]]
+ 0051a230 ["CALL", null, ["callee:00c57f10:8"]]
- 0051a1f0 bytes 48f61c94
+ 0051a230 bytes 38f71c94
- 0051a17c ["INT_ADD", "register:40f0:8", ["const:51a17c:8", "const:4:8"]]
- 0051a17c ["CALL", null, ["callee:00c57ef0:8"]]
+ 0051a1bc ["INT_ADD", "register:40f0:8", ["const:51a1bc:8", "const:4:8"]]
+ 0051a1bc ["CALL", null, ["callee:00c57ef0:8"]]
- 0051a17c bytes 5df61c94
+ 0051a1bc bytes 4df71c94
- 0051a188 ["INT_ADD", "register:40f0:8", ["const:51a188:8", "const:4:8"]]
- 0051a188 ["CALL", null, ["callee:00c57e90:8"]]
+ 0051a1c8 ["INT_ADD", "register:40f0:8", ["const:51a1c8:8", "const:4:8"]]
+ 0051a1c8 ["CALL", null, ["callee:00c57e90:8"]]
- 0051a188 bytes 42f61c94
+ 0051a1c8 bytes 32f71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67f83b92acc8a628ebad74ff40a5bbd3"></a>

### [`0051a240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a240.md) → [`0051a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a280.md) _ZN5Botan14Cert_Extension16Name_Constraints12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 18件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0051a994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a994.md) [`0051ab5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ab5c.md) [`0051ac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ac84.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)
- 新版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 18件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0051a9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a9d4.md) [`0051ab9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ab9c.md) [`0051acc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051acc4.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.51% / 新版 94.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 4件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051a3d8",
      "incomplete_value": true,
      "site": "0051a3d8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051a398",
      "incomplete_value": true,
      "site": "0051a398",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051a404",
      "incomplete_value": true,
      "site": "0051a404",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051a3c4",
      "incomplete_value": true,
      "site": "0051a3c4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051a448",
      "incomplete_value": true,
      "site": "0051a448",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051a408",
      "incomplete_value": true,
      "site": "0051a408",
      "value": [
        "LOAD",
        "8",
        [
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
      "0051a3c8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0051a3f4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0051a438",
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
      "0051a3c8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051a3f4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051a438",
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

- 旧版 [`0051a398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a240.md#insn-0051a398) · [`0051a3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a240.md#insn-0051a3c4) · [`0051a408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a240.md#insn-0051a408)
- 新版 `0051a3d8`（命令位置の公開資料なし） · `0051a404`（命令位置の公開資料なし） · `0051a448`（命令位置の公開資料なし）

~~~diff
- 0051a398 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051a398 ["INT_ADD", "register:40f0:8", ["const:51a398:8", "const:4:8"]]
- 0051a398 ["CALLIND", null, ["register:0:8"]]
+ 0051a3d8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051a3d8 ["INT_ADD", "register:40f0:8", ["const:51a3d8:8", "const:4:8"]]
+ 0051a3d8 ["CALLIND", null, ["register:0:8"]]
- 0051a398 bytes 20013fd6
+ 0051a3d8 bytes 20013fd6
- 0051a3c4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051a3c4 ["INT_ADD", "register:40f0:8", ["const:51a3c4:8", "const:4:8"]]
- 0051a3c4 ["CALLIND", null, ["register:0:8"]]
+ 0051a404 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051a404 ["INT_ADD", "register:40f0:8", ["const:51a404:8", "const:4:8"]]
+ 0051a404 ["CALLIND", null, ["register:0:8"]]
- 0051a3c4 bytes 20013fd6
+ 0051a404 bytes 20013fd6
- 0051a408 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051a408 ["INT_ADD", "register:40f0:8", ["const:51a408:8", "const:4:8"]]
- 0051a408 ["CALLIND", null, ["register:0:8"]]
+ 0051a448 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051a448 ["INT_ADD", "register:40f0:8", ["const:51a448:8", "const:4:8"]]
+ 0051a448 ["CALLIND", null, ["register:0:8"]]
- 0051a408 bytes 20013fd6
+ 0051a448 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33918c9f4fe621accb210ec3423272b7"></a>

### [`0051adec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051adec.md) → [`0051ae2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ae2c.md) _ZNK5Botan14Cert_Extension16Name_Constraints11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`005093b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005093b8.md) [`00548218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548218.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`005093f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005093f8.md) [`00548258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548258.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.50% / 新版 91.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051ae80",
      "incomplete_value": true,
      "site": "0051ae84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:780:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051ae40",
      "incomplete_value": true,
      "site": "0051ae44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0051af4c",
      "incomplete_value": true,
      "site": "0051af50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0051af0c",
      "incomplete_value": true,
      "site": "0051af10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051b010",
      "incomplete_value": true,
      "site": "0051b018",
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
      "definition_site": "0051afd0",
      "incomplete_value": true,
      "site": "0051afd8",
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
      "0051ae80",
      "READ",
      [
        "storage",
        "002c2740",
        null,
        null
      ]
    ],
    [
      "0051aebc",
      "READ",
      [
        "storage",
        "002a8c01",
        null,
        "string"
      ]
    ],
    [
      "0051aebc",
      "READ",
      [
        "storage",
        "002a8c11",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051ae80",
      "READ",
      [
        "storage",
        "002c2780",
        null,
        null
      ]
    ],
    [
      "0051aebc",
      "READ",
      [
        "storage",
        "002a8cce",
        null,
        "string"
      ]
    ],
    [
      "0051aebc",
      "READ",
      [
        "storage",
        "002a8cde",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051adec.md#insn-0051aed0) · [`0051ae24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051adec.md#insn-0051ae24) · [`0051ae3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051adec.md#insn-0051ae3c)
- 新版 `0051af10`（命令位置の公開資料なし） · `0051ae64`（命令位置の公開資料なし） · `0051ae7c`（命令位置の公開資料なし）

~~~diff
- 0051aed0 ["INT_ADD", "register:40f0:8", ["const:51aed0:8", "const:4:8"]]
- 0051aed0 ["CALL", null, ["callee:00c58430:8"]]
+ 0051af10 ["INT_ADD", "register:40f0:8", ["const:51af10:8", "const:4:8"]]
+ 0051af10 ["CALL", null, ["callee:00c58430:8"]]
- 0051aed0 bytes 58f41c94
+ 0051af10 bytes 48f51c94
- 0051ae24 ["INT_ADD", "register:40f0:8", ["const:51ae24:8", "const:4:8"]]
- 0051ae24 ["CALL", null, ["callee:004518b0:8"]]
+ 0051ae64 ["INT_ADD", "register:40f0:8", ["const:51ae64:8", "const:4:8"]]
+ 0051ae64 ["CALL", null, ["callee:004518b0:8"]]
- 0051ae24 bytes 93dafc97
+ 0051ae64 bytes 93dafc97
- 0051ae3c ["COPY", "tmp:0:8", ["const:c01:8"]]
- 0051ae3c ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 0051ae3c ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 0051ae3c ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 0051ae7c ["COPY", "tmp:0:8", ["const:cce:8"]]
+ 0051ae7c ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 0051ae7c ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 0051ae7c ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 0051ae3c bytes 39073091
+ 0051ae7c bytes 393b3391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbf9b511420b70fa3a4711eee3e43817"></a>

### [`0051b0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b0dc.md) → [`0051b11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b11c.md) _ZN5Botan14Cert_Extension16Name_Constraints8validateERKNS_16X509_CertificateES4_RKNSt6__ndk16vectorINS5_10shared_ptrIS3_EENS5_9allocatorIS8_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054087c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054087c.md) [`0054cb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cb5c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005408bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408bc.md) [`0054cb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cb9c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.95% / 新版 97.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051b304",
      "incomplete_value": true,
      "site": "0051b304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0051b2c4",
      "incomplete_value": true,
      "site": "0051b2c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051b304",
      "incomplete_value": true,
      "site": "0051b304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0051b2c4",
      "incomplete_value": true,
      "site": "0051b2c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051b38c",
      "incomplete_value": true,
      "site": "0051b38c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0051b34c",
      "incomplete_value": true,
      "site": "0051b34c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "0051b194",
      "READ",
      [
        "storage",
        "002a53b3",
        null,
        "string"
      ]
    ],
    [
      "0051b198",
      "READ",
      [
        "storage",
        "002a53c1",
        null,
        "string"
      ]
    ],
    [
      "0051b290",
      "READ",
      [
        "storage",
        "002a53b3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051b194",
      "READ",
      [
        "storage",
        "002a548f",
        null,
        "string"
      ]
    ],
    [
      "0051b198",
      "READ",
      [
        "storage",
        "002a549d",
        null,
        "string"
      ]
    ],
    [
      "0051b290",
      "READ",
      [
        "storage",
        "002a548f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051b140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b0dc.md#insn-0051b140) · [`0051b14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b0dc.md#insn-0051b14c) · [`0051b178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b0dc.md#insn-0051b178)
- 新版 `0051b180`（命令位置の公開資料なし） · `0051b18c`（命令位置の公開資料なし） · `0051b1b8`（命令位置の公開資料なし）

~~~diff
- 0051b140 ["INT_ADD", "register:40f0:8", ["const:51b140:8", "const:4:8"]]
- 0051b140 ["CALL", null, ["callee:00c599f0:8"]]
+ 0051b180 ["INT_ADD", "register:40f0:8", ["const:51b180:8", "const:4:8"]]
+ 0051b180 ["CALL", null, ["callee:00c599f0:8"]]
- 0051b140 bytes 2cf91c94
+ 0051b180 bytes 1cfa1c94
- 0051b14c ["COPY", "tmp:0:8", ["const:3b3:8"]]
- 0051b14c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 0051b14c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 0051b14c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 0051b18c ["COPY", "tmp:0:8", ["const:48f:8"]]
+ 0051b18c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 0051b18c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 0051b18c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 0051b14c bytes 94ce0e91
+ 0051b18c bytes 943e1291
- 0051b178 ["INT_ADD", "register:40f0:8", ["const:51b178:8", "const:4:8"]]
- 0051b178 ["CALL", null, ["callee:00c59e50:8"]]
+ 0051b1b8 ["INT_ADD", "register:40f0:8", ["const:51b1b8:8", "const:4:8"]]
+ 0051b1b8 ["CALL", null, ["callee:00c59e50:8"]]
- 0051b178 bytes 36fa1c94
+ 0051b1b8 bytes 26fb1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be08b1a11c19cf29b6b17220d23d3d99"></a>

### [`0051baa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051baa8.md) → [`0051bae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051bae8.md) _ZNK5Botan14Cert_Extension20Certificate_Policies12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`0054cbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cbe0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`0054cc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cc20.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.17% / 新版 97.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051bb54",
      "incomplete_value": true,
      "site": "0051bb5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0051bb14",
      "incomplete_value": true,
      "site": "0051bb1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "0051bb78",
      "incomplete_value": true,
      "site": "0051bb78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0051bb38",
      "incomplete_value": true,
      "site": "0051bb38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051bcac",
      "incomplete_value": true,
      "site": "0051bcac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0051bc6c",
      "incomplete_value": true,
      "site": "0051bc6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0051bb38",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "0051bb5c",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051bb68",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051bb38",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "0051bb5c",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051bb68",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051baf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051baa8.md#insn-0051baf8) · [`0051be44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051baa8.md#insn-0051be44) · [`0051be84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051baa8.md#insn-0051be84)
- 新版 `0051bb38`（命令位置の公開資料なし） · `0051be84`（命令位置の公開資料なし） · `0051bec4`（命令位置の公開資料なし）

~~~diff
- 0051baf8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:940:8"]]
- 0051baf8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051bb38 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
+ 0051bb38 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0051baf8 bytes 29a144f9
+ 0051bb38 bytes 29a146f9
- 0051be44 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051be44 ["INT_ADD", "register:40f0:8", ["const:51be44:8", "const:4:8"]]
- 0051be44 ["CALLIND", null, ["register:0:8"]]
+ 0051be84 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051be84 ["INT_ADD", "register:40f0:8", ["const:51be84:8", "const:4:8"]]
+ 0051be84 ["CALLIND", null, ["register:0:8"]]
- 0051be44 bytes 20013fd6
+ 0051be84 bytes 20013fd6
- 0051be84 ["INT_ADD", "register:40f0:8", ["const:51be84:8", "const:4:8"]]
- 0051be84 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051bec4 ["INT_ADD", "register:40f0:8", ["const:51bec4:8", "const:4:8"]]
+ 0051bec4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0051be84 bytes 0bef1c94
+ 0051bec4 bytes fbef1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59df8fd90a04ea74eba23a231298d4d2"></a>

### [`0051c028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c028.md) → [`0051c068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c068.md) _ZN5Botan14Cert_Extension20Certificate_Policies12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0053d9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d9cc.md) [`0054b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0053da0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053da0c.md) [`0054b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051c0f0",
      "incomplete_value": true,
      "site": "0051c0f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0051c0b0",
      "incomplete_value": true,
      "site": "0051c0b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051c384",
      "incomplete_value": true,
      "site": "0051c384",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
      "definition_site": "0051c344",
      "incomplete_value": true,
      "site": "0051c344",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051c3c8",
      "incomplete_value": true,
      "site": "0051c3c8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
      "definition_site": "0051c388",
      "incomplete_value": true,
      "site": "0051c388",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
    "ordinal": 19,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051c0d0",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "0051c0f0",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051c11c",
      "DATA",
      [
        "storage",
        "00c6a088",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051c0d0",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "0051c0f0",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051c11c",
      "DATA",
      [
        "storage",
        "00c6a488",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051c0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c028.md#insn-0051c0f0) · [`0051c304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c028.md#insn-0051c304) · [`0051c344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c028.md#insn-0051c344)
- 新版 `0051c130`（命令位置の公開資料なし） · `0051c344`（命令位置の公開資料なし） · `0051c384`（命令位置の公開資料なし）

~~~diff
- 0051c0f0 ["INT_ADD", "register:40f0:8", ["const:51c0f0:8", "const:4:8"]]
- 0051c0f0 ["CALL", null, ["callee:00c58690:8"]]
+ 0051c130 ["INT_ADD", "register:40f0:8", ["const:51c130:8", "const:4:8"]]
+ 0051c130 ["CALL", null, ["callee:00c58690:8"]]
- 0051c0f0 bytes 68f01c94
+ 0051c130 bytes 58f11c94
- 0051c304 ["INT_ADD", "register:40f0:8", ["const:51c304:8", "const:4:8"]]
- 0051c304 ["CALL", null, ["callee:00c58710:8"]]
+ 0051c344 ["INT_ADD", "register:40f0:8", ["const:51c344:8", "const:4:8"]]
+ 0051c344 ["CALL", null, ["callee:00c58710:8"]]
- 0051c304 bytes 03f01c94
+ 0051c344 bytes f3f01c94
- 0051c344 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051c344 ["INT_ADD", "register:40f0:8", ["const:51c344:8", "const:4:8"]]
- 0051c344 ["CALLIND", null, ["register:0:8"]]
+ 0051c384 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051c384 ["INT_ADD", "register:40f0:8", ["const:51c384:8", "const:4:8"]]
+ 0051c384 ["CALLIND", null, ["register:0:8"]]
- 0051c344 bytes 20013fd6
+ 0051c384 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afe07c11ffa0b3630f65d0c9f7d2c395"></a>

### [`0051c67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c67c.md) → [`0051c6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c6bc.md) _ZNK5Botan14Cert_Extension20Certificate_Policies11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58400.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58800.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.04% / 新版 91.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051c6fc",
      "incomplete_value": true,
      "site": "0051c710",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7e7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051c6bc",
      "incomplete_value": true,
      "site": "0051c6d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7a7:8"
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
      "definition_site": "0051c6f8",
      "incomplete_value": true,
      "site": "0051c710",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051c6b8",
      "incomplete_value": true,
      "site": "0051c6d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a50:8"
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
      "definition_site": "0051c714",
      "incomplete_value": true,
      "site": "0051c718",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051c6d4",
      "incomplete_value": true,
      "site": "0051c6d8",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
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
      "0051c6f8",
      "READ",
      [
        "storage",
        "002c2a50",
        null,
        null
      ]
    ],
    [
      "0051c6fc",
      "READ",
      [
        "storage",
        "002ae7a7",
        null,
        "string"
      ]
    ],
    [
      "0051c714",
      "READ",
      [
        "storage",
        "002ae7b1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051c6f8",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ],
    [
      "0051c6fc",
      "READ",
      [
        "storage",
        "002ae7e7",
        null,
        "string"
      ]
    ],
    [
      "0051c714",
      "READ",
      [
        "storage",
        "002ae7f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051c6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c67c.md#insn-0051c6b4) · [`0051c6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c67c.md#insn-0051c6b8) · [`0051c6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c67c.md#insn-0051c6fc)
- 新版 `0051c6f4`（命令位置の公開資料なし） · `0051c6f8`（命令位置の公開資料なし） · `0051c73c`（命令位置の公開資料なし）

~~~diff
- 0051c6b4 ["COPY", "tmp:0:8", ["const:7a7:8"]]
- 0051c6b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051c6b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051c6b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051c6f4 ["COPY", "tmp:0:8", ["const:7e7:8"]]
+ 0051c6f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051c6f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051c6f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051c6b4 bytes 299d1e91
+ 0051c6f4 bytes 299d1f91
- 0051c6b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
- 0051c6b8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0051c6b8 ["COPY", "register:5030:8", ["const:0:8"]]
- 0051c6b8 ["COPY", "register:5038:8", ["const:0:8"]]
+ 0051c6f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
+ 0051c6f8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0051c6f8 ["COPY", "register:5030:8", ["const:0:8"]]
+ 0051c6f8 ["COPY", "register:5038:8", ["const:0:8"]]
- 0051c6b8 bytes 0195c23d
+ 0051c6f8 bytes 01a5c23d
- 0051c6fc ["INT_ADD", "register:40f0:8", ["const:51c6fc:8", "const:4:8"]]
- 0051c6fc ["CALL", null, ["callee:00c57e90:8"]]
+ 0051c73c ["INT_ADD", "register:40f0:8", ["const:51c73c:8", "const:4:8"]]
+ 0051c73c ["CALL", null, ["callee:00c57e90:8"]]
- 0051c6fc bytes e5ec1c94
+ 0051c73c bytes d5ed1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42e8d45667204f749af004c0f0140e2a"></a>

### [`0051ca70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051ca70.md) → [`0051cab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051cab0.md) _ZNK5Botan14Cert_Extension28Authority_Information_Access12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 0件  · 呼出先 11件 [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

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
      "definition_site": "0051cb30",
      "incomplete_value": true,
      "site": "0051cb30",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:f5c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051caf0",
      "incomplete_value": true,
      "site": "0051caf0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:f1c:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0051cc24",
      "incomplete_value": true,
      "site": "0051cc24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0051cbe4",
      "incomplete_value": true,
      "site": "0051cbe4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0051cb20",
      "READ",
      [
        "storage",
        "002b5f1c",
        null,
        "string"
      ]
    ],
    [
      "0051cc14",
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
      "0051cb20",
      "READ",
      [
        "storage",
        "002b5f5c",
        null,
        "string"
      ]
    ],
    [
      "0051cc14",
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

- 旧版 [`0051cbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051ca70.md#insn-0051cbe4) · [`0051caa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051ca70.md#insn-0051caa4) · [`0051cac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051ca70.md#insn-0051cac0)
- 新版 `0051cc24`（命令位置の公開資料なし） · `0051cae4`（命令位置の公開資料なし） · `0051cb00`（命令位置の公開資料なし）

~~~diff
- 0051cbe4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051cbe4 ["INT_ADD", "register:40f0:8", ["const:51cbe4:8", "const:4:8"]]
- 0051cbe4 ["CALLIND", null, ["register:0:8"]]
+ 0051cc24 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051cc24 ["INT_ADD", "register:40f0:8", ["const:51cc24:8", "const:4:8"]]
+ 0051cc24 ["CALLIND", null, ["register:0:8"]]
- 0051cbe4 bytes 20013fd6
+ 0051cc24 bytes 20013fd6
- 0051caa4 ["INT_ADD", "register:40f0:8", ["const:51caa4:8", "const:4:8"]]
- 0051caa4 ["CALL", null, ["callee:00c59960:8"]]
+ 0051cae4 ["INT_ADD", "register:40f0:8", ["const:51cae4:8", "const:4:8"]]
+ 0051cae4 ["CALL", null, ["callee:00c59960:8"]]
- 0051caa4 bytes aff21c94
+ 0051cae4 bytes 9ff31c94
- 0051cac0 ["INT_ADD", "register:40f0:8", ["const:51cac0:8", "const:4:8"]]
- 0051cac0 ["CALL", null, ["callee:00c586b0:8"]]
+ 0051cb00 ["INT_ADD", "register:40f0:8", ["const:51cb00:8", "const:4:8"]]
+ 0051cb00 ["CALL", null, ["callee:00c586b0:8"]]
- 0051cac0 bytes fced1c94
+ 0051cb00 bytes ecee1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b6a9842f0d4ee47e83129b6562f534f"></a>

### [`0051cc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051cc9c.md) → [`0051ccdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051ccdc.md) _ZN5Botan14Cert_Extension28Authority_Information_Access12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.90% / 新版 95.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051cd8c",
      "incomplete_value": true,
      "site": "0051cda8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:780:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051cd4c",
      "incomplete_value": true,
      "site": "0051cd68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:740:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0051cd68",
      "incomplete_value": true,
      "site": "0051cd68",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051cd28",
      "incomplete_value": true,
      "site": "0051cd28",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051d008",
      "incomplete_value": true,
      "site": "0051d008",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051cfc8",
      "incomplete_value": true,
      "site": "0051cfc8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051cd58",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0051cd8c",
      "READ",
      [
        "storage",
        "002c2740",
        null,
        null
      ]
    ],
    [
      "0051ce18",
      "READ",
      [
        "storage",
        "002b5f1c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051cd58",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051cd8c",
      "READ",
      [
        "storage",
        "002c2780",
        null,
        null
      ]
    ],
    [
      "0051ce18",
      "READ",
      [
        "storage",
        "002b5f5c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051cce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051cc9c.md#insn-0051cce8) · [`0051cd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051cc9c.md#insn-0051cd28) · [`0051cfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051cc9c.md#insn-0051cfc8)
- 新版 `0051cd28`（命令位置の公開資料なし） · `0051cd68`（命令位置の公開資料なし） · `0051d008`（命令位置の公開資料なし）

~~~diff
- 0051cce8 ["INT_ADD", "register:40f0:8", ["const:51cce8:8", "const:4:8"]]
- 0051cce8 ["CALL", null, ["callee:00c58700:8"]]
+ 0051cd28 ["INT_ADD", "register:40f0:8", ["const:51cd28:8", "const:4:8"]]
+ 0051cd28 ["CALL", null, ["callee:00c58700:8"]]
- 0051cce8 bytes 86ed1c94
+ 0051cd28 bytes 76ee1c94
- 0051cd28 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051cd28 ["INT_ADD", "register:40f0:8", ["const:51cd28:8", "const:4:8"]]
- 0051cd28 ["CALLIND", null, ["register:0:8"]]
+ 0051cd68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051cd68 ["INT_ADD", "register:40f0:8", ["const:51cd68:8", "const:4:8"]]
+ 0051cd68 ["CALLIND", null, ["register:0:8"]]
- 0051cd28 bytes 20013fd6
+ 0051cd68 bytes 20013fd6
- 0051cfc8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051cfc8 ["INT_ADD", "register:40f0:8", ["const:51cfc8:8", "const:4:8"]]
- 0051cfc8 ["CALLIND", null, ["register:0:8"]]
+ 0051d008 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051d008 ["INT_ADD", "register:40f0:8", ["const:51d008:8", "const:4:8"]]
+ 0051d008 ["CALLIND", null, ["register:0:8"]]
- 0051cfc8 bytes 20013fd6
+ 0051d008 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdb597b737fd3b83983d4d63830eb5b1"></a>

### [`0051d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d4c8.md) → [`0051d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d508.md) _ZNK5Botan14Cert_Extension28Authority_Information_Access11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.14% / 新版 85.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051d568",
      "incomplete_value": true,
      "site": "0051d568",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d528",
      "incomplete_value": true,
      "site": "0051d528",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:160:8"
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
      "definition_site": "0051d56c",
      "incomplete_value": true,
      "site": "0051d56c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0051d52c",
      "incomplete_value": true,
      "site": "0051d52c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0051d5a4",
      "incomplete_value": true,
      "site": "0051d5ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:adc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d564",
      "incomplete_value": true,
      "site": "0051d56c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a9c:8"
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
      "0051d558",
      "READ",
      [
        "storage",
        "002c1160",
        null,
        "string"
      ]
    ],
    [
      "0051d55c",
      "READ",
      [
        "storage",
        "002c1166",
        null,
        "string"
      ]
    ],
    [
      "0051d5a4",
      "READ",
      [
        "storage",
        "002b1a9c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051d558",
      "READ",
      [
        "storage",
        "002c11a0",
        null,
        "string"
      ]
    ],
    [
      "0051d55c",
      "READ",
      [
        "storage",
        "002c11a6",
        null,
        "string"
      ]
    ],
    [
      "0051d5a4",
      "READ",
      [
        "storage",
        "002b1adc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d4c8.md#insn-0051d568) · [`0051d5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d4c8.md#insn-0051d5b0) · [`0051d510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d4c8.md#insn-0051d510)
- 新版 `0051d5a8`（命令位置の公開資料なし） · `0051d5f0`（命令位置の公開資料なし） · `0051d550`（命令位置の公開資料なし）

~~~diff
- 0051d568 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:740:8"]]
- 0051d568 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0051d568 ["COPY", "register:5030:8", ["const:0:8"]]
- 0051d568 ["COPY", "register:5038:8", ["const:0:8"]]
+ 0051d5a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:780:8"]]
+ 0051d5a8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0051d5a8 ["COPY", "register:5030:8", ["const:0:8"]]
+ 0051d5a8 ["COPY", "register:5038:8", ["const:0:8"]]
- 0051d568 bytes 01d1c13d
+ 0051d5a8 bytes 01e1c13d
- 0051d5b0 ["INT_ADD", "register:40f0:8", ["const:51d5b0:8", "const:4:8"]]
- 0051d5b0 ["CALL", null, ["callee:004ff1a0:8"]]
+ 0051d5f0 ["INT_ADD", "register:40f0:8", ["const:51d5f0:8", "const:4:8"]]
+ 0051d5f0 ["CALL", null, ["callee:004ff1a0:8"]]
- 0051d5b0 bytes ec86ff97
+ 0051d5f0 bytes ec86ff97
- 0051d510 ["COPY", "tmp:0:8", ["const:160:8"]]
- 0051d510 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051d510 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051d510 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051d550 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 0051d550 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051d550 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051d550 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051d510 bytes 29810591
+ 0051d550 bytes 29810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e28ab27a7e5d117a5fe16d1015e21c7b"></a>

### [`0051d620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d620.md) → [`0051d660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d660.md) _ZNK5Botan14Cert_Extension10CRL_Number14get_crl_numberEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c599b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599b0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c59db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59db0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

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
      "definition_site": "0051d6c4",
      "incomplete_value": false,
      "site": "0051d6cc",
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
            "const:a8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d684",
      "incomplete_value": false,
      "site": "0051d68c",
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
            "const:a4c:8"
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
      "definition_site": "0051d700",
      "incomplete_value": true,
      "site": "0051d70c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d6c0",
      "incomplete_value": true,
      "site": "0051d6cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:948:8"
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
      "definition_site": "0051d6fc",
      "incomplete_value": false,
      "site": "0051d70c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "0051d6bc",
      "incomplete_value": false,
      "site": "0051d6cc",
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
      "0051d6c4",
      "PARAM",
      [
        "storage",
        "002afa4c",
        null,
        "string"
      ]
    ],
    [
      "0051d6fc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "0051d700",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051d6c4",
      "PARAM",
      [
        "storage",
        "002afa8c",
        null,
        "string"
      ]
    ],
    [
      "0051d6fc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0051d700",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051d68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d620.md#insn-0051d68c) · [`0051d6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d620.md#insn-0051d6cc) · [`0051d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d620.md#insn-0051d678)
- 新版 `0051d6cc`（命令位置の公開資料なし） · `0051d70c`（命令位置の公開資料なし） · `0051d6b8`（命令位置の公開資料なし）

~~~diff
- 0051d68c ["INT_ADD", "register:40f0:8", ["const:51d68c:8", "const:4:8"]]
- 0051d68c ["CALL", null, ["callee:0043ddd8:8"]]
+ 0051d6cc ["INT_ADD", "register:40f0:8", ["const:51d6cc:8", "const:4:8"]]
+ 0051d6cc ["CALL", null, ["callee:0043ddd8:8"]]
- 0051d68c bytes c381fc97
+ 0051d6cc bytes c381fc97
- 0051d6cc ["INT_ADD", "register:40f0:8", ["const:51d6cc:8", "const:4:8"]]
- 0051d6cc ["CALL", null, ["callee:00c57f10:8"]]
+ 0051d70c ["INT_ADD", "register:40f0:8", ["const:51d70c:8", "const:4:8"]]
+ 0051d70c ["CALL", null, ["callee:00c57f10:8"]]
- 0051d6cc bytes 11e91c94
+ 0051d70c bytes 01ea1c94
- 0051d678 ["INT_ADD", "register:40f0:8", ["const:51d678:8", "const:4:8"]]
- 0051d678 ["CALL", null, ["callee:00c57ef0:8"]]
+ 0051d6b8 ["INT_ADD", "register:40f0:8", ["const:51d6b8:8", "const:4:8"]]
+ 0051d6b8 ["CALL", null, ["callee:00c57ef0:8"]]
- 0051d678 bytes 1ee91c94
+ 0051d6b8 bytes 0eea1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97ce8493378aeb6ceca48eaeb19379f1"></a>

### [`0051d720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d720.md) → [`0051d760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d760.md) _ZNK5Botan14Cert_Extension10CRL_Number4copyEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051d7a8",
      "incomplete_value": true,
      "site": "0051d7b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0051d768",
      "incomplete_value": true,
      "site": "0051d770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0051d7ec",
      "incomplete_value": false,
      "site": "0051d7f4",
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
            "const:24d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d7ac",
      "incomplete_value": false,
      "site": "0051d7b4",
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
            "const:20d:8"
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
      "definition_site": "0051d828",
      "incomplete_value": true,
      "site": "0051d834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d7e8",
      "incomplete_value": true,
      "site": "0051d7f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:948:8"
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
      "0051d79c",
      "READ",
      [
        "storage",
        "00c9ada0",
        null,
        "pointer"
      ]
    ],
    [
      "0051d7b0",
      "DATA",
      [
        "storage",
        "00c688c0",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "0051d7ec",
      "PARAM",
      [
        "storage",
        "002b820d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051d79c",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "0051d7b0",
      "DATA",
      [
        "storage",
        "00c68cc0",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "0051d7ec",
      "PARAM",
      [
        "storage",
        "002b824d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051d7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d720.md#insn-0051d7b4) · [`0051d7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d720.md#insn-0051d7f4) · [`0051d750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d720.md#insn-0051d750)
- 新版 `0051d7f4`（命令位置の公開資料なし） · `0051d834`（命令位置の公開資料なし） · `0051d790`（命令位置の公開資料なし）

~~~diff
- 0051d7b4 ["INT_ADD", "register:40f0:8", ["const:51d7b4:8", "const:4:8"]]
- 0051d7b4 ["CALL", null, ["callee:0043ddd8:8"]]
+ 0051d7f4 ["INT_ADD", "register:40f0:8", ["const:51d7f4:8", "const:4:8"]]
+ 0051d7f4 ["CALL", null, ["callee:0043ddd8:8"]]
- 0051d7b4 bytes 7981fc97
+ 0051d7f4 bytes 7981fc97
- 0051d7f4 ["INT_ADD", "register:40f0:8", ["const:51d7f4:8", "const:4:8"]]
- 0051d7f4 ["CALL", null, ["callee:00c57f10:8"]]
+ 0051d834 ["INT_ADD", "register:40f0:8", ["const:51d834:8", "const:4:8"]]
+ 0051d834 ["CALL", null, ["callee:00c57f10:8"]]
- 0051d7f4 bytes c7e81c94
+ 0051d834 bytes b7e91c94
- 0051d750 ["INT_ADD", "register:40f0:8", ["const:51d750:8", "const:4:8"]]
- 0051d750 ["CALL", null, ["callee:00c57e90:8"]]
+ 0051d790 ["INT_ADD", "register:40f0:8", ["const:51d790:8", "const:4:8"]]
+ 0051d790 ["CALL", null, ["callee:00c57e90:8"]]
- 0051d750 bytes d0e81c94
+ 0051d790 bytes c0e91c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63ec67215e0b1f019e7a69f6a8ba290f"></a>

### [`0051d848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d848.md) → [`0051d888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d888.md) _ZNK5Botan14Cert_Extension10CRL_Number12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051d900",
      "incomplete_value": true,
      "site": "0051d900",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051d8c0",
      "incomplete_value": true,
      "site": "0051d8c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051d978",
      "incomplete_value": true,
      "site": "0051d978",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051d938",
      "incomplete_value": true,
      "site": "0051d938",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "0051d8f0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0051d968",
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
      "0051d8f0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051d968",
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

- 旧版 [`0051d8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d848.md#insn-0051d8c0) · [`0051d900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d848.md#insn-0051d900) · [`0051d938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051d848.md#insn-0051d938)
- 新版 `0051d900`（命令位置の公開資料なし） · `0051d940`（命令位置の公開資料なし） · `0051d978`（命令位置の公開資料なし）

~~~diff
- 0051d8c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051d8c0 ["INT_ADD", "register:40f0:8", ["const:51d8c0:8", "const:4:8"]]
- 0051d8c0 ["CALLIND", null, ["register:0:8"]]
+ 0051d900 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051d900 ["INT_ADD", "register:40f0:8", ["const:51d900:8", "const:4:8"]]
+ 0051d900 ["CALLIND", null, ["register:0:8"]]
- 0051d8c0 bytes 20013fd6
+ 0051d900 bytes 20013fd6
- 0051d900 ["INT_ADD", "register:40f0:8", ["const:51d900:8", "const:4:8"]]
- 0051d900 ["CALL", null, ["callee:00535b80:8"]]
+ 0051d940 ["INT_ADD", "register:40f0:8", ["const:51d940:8", "const:4:8"]]
+ 0051d940 ["CALL", null, ["callee:00535b80:8"]]
- 0051d900 bytes 90600094
+ 0051d940 bytes 90600094
- 0051d938 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051d938 ["INT_ADD", "register:40f0:8", ["const:51d938:8", "const:4:8"]]
- 0051d938 ["CALLIND", null, ["register:0:8"]]
+ 0051d978 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051d978 ["INT_ADD", "register:40f0:8", ["const:51d978:8", "const:4:8"]]
+ 0051d978 ["CALLIND", null, ["register:0:8"]]
- 0051d938 bytes 20013fd6
+ 0051d978 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-767f67f3ce719cd084dbf6e56177d4b8"></a>

### [`0051da8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051da8c.md) → [`0051dacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dacc.md) _ZNK5Botan14Cert_Extension10CRL_Number11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58390.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58790.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051daec",
      "incomplete_value": true,
      "site": "0051db08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0051daac",
      "incomplete_value": true,
      "site": "0051dac8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0051daec",
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
      "0051daec",
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

- 旧版 [`0051daa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051da8c.md#insn-0051daa4) · [`0051dad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051da8c.md#insn-0051dad0) · [`0051dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051da8c.md#insn-0051dae0)
- 新版 `0051dae4`（命令位置の公開資料なし） · `0051db10`（命令位置の公開資料なし） · `0051db20`（命令位置の公開資料なし）

~~~diff
- 0051daa4 ["COPY", "tmp:0:8", ["const:3bc:8"]]
- 0051daa4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051daa4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051daa4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051dae4 ["COPY", "tmp:0:8", ["const:3fc:8"]]
+ 0051dae4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051dae4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051dae4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051daa4 bytes 29f10e91
+ 0051dae4 bytes 29f10f91
- 0051dad0 ["INT_ADD", "register:40f0:8", ["const:51dad0:8", "const:4:8"]]
- 0051dad0 ["CALL", null, ["callee:00c58790:8"]]
+ 0051db10 ["INT_ADD", "register:40f0:8", ["const:51db10:8", "const:4:8"]]
+ 0051db10 ["CALL", null, ["callee:00c58790:8"]]
- 0051dad0 bytes 30ea1c94
+ 0051db10 bytes 20eb1c94
- 0051dae0 ["INT_ADD", "register:40f0:8", ["const:51dae0:8", "const:4:8"]]
- 0051dae0 ["CALL", null, ["callee:004ff1a0:8"]]
+ 0051db20 ["INT_ADD", "register:40f0:8", ["const:51db20:8", "const:4:8"]]
+ 0051db20 ["CALL", null, ["callee:004ff1a0:8"]]
- 0051dae0 bytes a085ff97
+ 0051db20 bytes a085ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd6ef86a9db56f15d73dd2ea3e0452f4"></a>

### [`0051db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051db64.md) → [`0051dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dba4.md) _ZNK5Botan14Cert_Extension14CRL_ReasonCode12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051dc1c",
      "incomplete_value": true,
      "site": "0051dc1c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051dbdc",
      "incomplete_value": true,
      "site": "0051dbdc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051dc94",
      "incomplete_value": true,
      "site": "0051dc94",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051dc54",
      "incomplete_value": true,
      "site": "0051dc54",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "0051dc0c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0051dc84",
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
      "0051dc0c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051dc84",
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

- 旧版 [`0051dbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051db64.md#insn-0051dbdc) · [`0051dc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051db64.md#insn-0051dc1c) · [`0051dc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051db64.md#insn-0051dc54)
- 新版 `0051dc1c`（命令位置の公開資料なし） · `0051dc5c`（命令位置の公開資料なし） · `0051dc94`（命令位置の公開資料なし）

~~~diff
- 0051dbdc ["COPY", "register:0:8", ["register:4048:8"]]
- 0051dbdc ["INT_ADD", "register:40f0:8", ["const:51dbdc:8", "const:4:8"]]
- 0051dbdc ["CALLIND", null, ["register:0:8"]]
+ 0051dc1c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051dc1c ["INT_ADD", "register:40f0:8", ["const:51dc1c:8", "const:4:8"]]
+ 0051dc1c ["CALLIND", null, ["register:0:8"]]
- 0051dbdc bytes 20013fd6
+ 0051dc1c bytes 20013fd6
- 0051dc1c ["INT_ADD", "register:40f0:8", ["const:51dc1c:8", "const:4:8"]]
- 0051dc1c ["CALL", null, ["callee:00535b80:8"]]
+ 0051dc5c ["INT_ADD", "register:40f0:8", ["const:51dc5c:8", "const:4:8"]]
+ 0051dc5c ["CALL", null, ["callee:00535b80:8"]]
- 0051dc1c bytes c95f0094
+ 0051dc5c bytes c95f0094
- 0051dc54 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051dc54 ["INT_ADD", "register:40f0:8", ["const:51dc54:8", "const:4:8"]]
- 0051dc54 ["CALLIND", null, ["register:0:8"]]
+ 0051dc94 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051dc94 ["INT_ADD", "register:40f0:8", ["const:51dc94:8", "const:4:8"]]
+ 0051dc94 ["CALLIND", null, ["register:0:8"]]
- 0051dc54 bytes 20013fd6
+ 0051dc94 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-476e34cddd8abfb71b59aad4ae4b8a73"></a>

### [`0051ddac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051ddac.md) → [`0051ddec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051ddec.md) _ZNK5Botan14Cert_Extension14CRL_ReasonCode11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58390.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58790.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051de0c",
      "incomplete_value": true,
      "site": "0051de34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:267:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051ddcc",
      "incomplete_value": true,
      "site": "0051ddf4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:227:8"
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
      "0051de0c",
      "READ",
      [
        "storage",
        "002b8227",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051de0c",
      "READ",
      [
        "storage",
        "002b8267",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051ddc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051ddac.md#insn-0051ddc4) · [`0051ddfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051ddac.md#insn-0051ddfc) · [`0051de0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051ddac.md#insn-0051de0c)
- 新版 `0051de04`（命令位置の公開資料なし） · `0051de3c`（命令位置の公開資料なし） · `0051de4c`（命令位置の公開資料なし）

~~~diff
- 0051ddc4 ["COPY", "tmp:0:8", ["const:227:8"]]
- 0051ddc4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0051ddc4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0051ddc4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0051de04 ["COPY", "tmp:0:8", ["const:267:8"]]
+ 0051de04 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0051de04 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0051de04 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0051ddc4 bytes 4a9d0891
+ 0051de04 bytes 4a9d0991
- 0051ddfc ["INT_ADD", "register:40f0:8", ["const:51ddfc:8", "const:4:8"]]
- 0051ddfc ["CALL", null, ["callee:00c58790:8"]]
+ 0051de3c ["INT_ADD", "register:40f0:8", ["const:51de3c:8", "const:4:8"]]
+ 0051de3c ["CALL", null, ["callee:00c58790:8"]]
- 0051ddfc bytes 65e91c94
+ 0051de3c bytes 55ea1c94
- 0051de0c ["INT_ADD", "register:40f0:8", ["const:51de0c:8", "const:4:8"]]
- 0051de0c ["CALL", null, ["callee:004ff1a0:8"]]
+ 0051de4c ["INT_ADD", "register:40f0:8", ["const:51de4c:8", "const:4:8"]]
+ 0051de4c ["CALL", null, ["callee:004ff1a0:8"]]
- 0051de0c bytes d584ff97
+ 0051de4c bytes d584ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c964d667a613f077ddcc6a15fa853b9"></a>

### [`0051de90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051de90.md) → [`0051ded0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051ded0.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.58% / 新版 81.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051df14",
      "incomplete_value": true,
      "site": "0051df20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:780:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051ded4",
      "incomplete_value": true,
      "site": "0051dee0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0051df10",
      "incomplete_value": true,
      "site": "0051df24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:54b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051ded0",
      "incomplete_value": true,
      "site": "0051dee4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:50b:8"
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
      "definition_site": "0051df10",
      "incomplete_value": true,
      "site": "0051df24",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0051ded0",
      "incomplete_value": true,
      "site": "0051dee4",
      "value": [
        "LOAD",
        "16",
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
      "0051df10",
      "READ",
      [
        "storage",
        "002ab50b",
        null,
        "string"
      ]
    ],
    [
      "0051df10",
      "READ",
      [
        "storage",
        "002ab51b",
        null,
        "string"
      ]
    ],
    [
      "0051df14",
      "READ",
      [
        "storage",
        "002c2740",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051df10",
      "READ",
      [
        "storage",
        "002ab54b",
        null,
        "string"
      ]
    ],
    [
      "0051df10",
      "READ",
      [
        "storage",
        "002ab55b",
        null,
        "string"
      ]
    ],
    [
      "0051df14",
      "READ",
      [
        "storage",
        "002c2780",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051de90.md#insn-0051df20) · [`0051deb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051de90.md#insn-0051deb4) · [`0051dec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051de90.md#insn-0051dec0)
- 新版 `0051df60`（命令位置の公開資料なし） · `0051def4`（命令位置の公開資料なし） · `0051df00`（命令位置の公開資料なし）

~~~diff
- 0051df20 ["INT_ADD", "register:40f0:8", ["const:51df20:8", "const:4:8"]]
- 0051df20 ["CALL", null, ["callee:00c57f10:8"]]
+ 0051df60 ["INT_ADD", "register:40f0:8", ["const:51df60:8", "const:4:8"]]
+ 0051df60 ["CALL", null, ["callee:00c57f10:8"]]
- 0051df20 bytes fce61c94
+ 0051df60 bytes ece71c94
- 0051deb4 ["INT_ADD", "register:40f0:8", ["const:51deb4:8", "const:4:8"]]
- 0051deb4 ["CALL", null, ["callee:00c57ef0:8"]]
+ 0051def4 ["INT_ADD", "register:40f0:8", ["const:51def4:8", "const:4:8"]]
+ 0051def4 ["CALL", null, ["callee:00c57ef0:8"]]
- 0051deb4 bytes 0fe71c94
+ 0051def4 bytes ffe71c94
- 0051dec0 ["INT_ADD", "register:40f0:8", ["const:51dec0:8", "const:4:8"]]
- 0051dec0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0051df00 ["INT_ADD", "register:40f0:8", ["const:51df00:8", "const:4:8"]]
+ 0051df00 ["CALL", null, ["callee:00c57e90:8"]]
- 0051dec0 bytes f4e61c94
+ 0051df00 bytes e4e71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8715c14ab2df4951173bd1898bd4a7f"></a>

### [`0051df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051df70.md) → [`0051dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dfb0.md) _ZN5Botan14Cert_Extension23CRL_Distribution_Points12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051e27c",
      "incomplete_value": true,
      "site": "0051e284",
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
      "definition_site": "0051e23c",
      "incomplete_value": true,
      "site": "0051e244",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0051e28c",
      "incomplete_value": true,
      "site": "0051e28c",
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
                "const:20:8"
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
      "definition_site": "0051e24c",
      "incomplete_value": true,
      "site": "0051e24c",
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
                "const:20:8"
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
    "ordinal": 27,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051e28c",
      "incomplete_value": true,
      "site": "0051e28c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0051e24c",
      "incomplete_value": true,
      "site": "0051e24c",
      "value": [
        "LOAD",
        "8",
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
      "0051e02c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0051e0f0",
      "PARAM",
      [
        "storage",
        "002bd72e",
        null,
        null
      ]
    ],
    [
      "0051e11c",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051e02c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051e0f0",
      "PARAM",
      [
        "storage",
        "002bd76e",
        null,
        null
      ]
    ],
    [
      "0051e11c",
      "PARAM",
      [
        "storage",
        "002a0fc7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051dfbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051df70.md#insn-0051dfbc) · [`0051dffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051df70.md#insn-0051dffc) · [`0051dfa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051df70.md#insn-0051dfa4)
- 新版 `0051dffc`（命令位置の公開資料なし） · `0051e03c`（命令位置の公開資料なし） · `0051dfe4`（命令位置の公開資料なし）

~~~diff
- 0051dfbc ["INT_ADD", "register:40f0:8", ["const:51dfbc:8", "const:4:8"]]
- 0051dfbc ["CALL", null, ["callee:00c58a20:8"]]
+ 0051dffc ["INT_ADD", "register:40f0:8", ["const:51dffc:8", "const:4:8"]]
+ 0051dffc ["CALL", null, ["callee:00c58a20:8"]]
- 0051dfbc bytes 99e91c94
+ 0051dffc bytes 89ea1c94
- 0051dffc ["COPY", "register:0:8", ["register:4048:8"]]
- 0051dffc ["INT_ADD", "register:40f0:8", ["const:51dffc:8", "const:4:8"]]
- 0051dffc ["CALLIND", null, ["register:0:8"]]
+ 0051e03c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051e03c ["INT_ADD", "register:40f0:8", ["const:51e03c:8", "const:4:8"]]
+ 0051e03c ["CALLIND", null, ["register:0:8"]]
- 0051dffc bytes 20013fd6
+ 0051e03c bytes 20013fd6
- 0051dfa4 ["INT_ADD", "register:40f0:8", ["const:51dfa4:8", "const:4:8"]]
- 0051dfa4 ["CALL", null, ["callee:00c58880:8"]]
+ 0051dfe4 ["INT_ADD", "register:40f0:8", ["const:51dfe4:8", "const:4:8"]]
+ 0051dfe4 ["CALL", null, ["callee:00c58880:8"]]
- 0051dfa4 bytes 37e91c94
+ 0051dfe4 bytes 27ea1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33bb8c7bc619240a7b24b418e0654a30"></a>

### [`0051e358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e358.md) → [`0051e398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e398.md) _ZN5Botan11BER_Decoder11decode_listINS_14Cert_Extension23CRL_Distribution_Points18Distribution_PointEEERS0_RNSt6__ndk16vectorIT_NS6_9allocat

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a60.md) · 呼出先 11件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053aa64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053aa64.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0053ca48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053ca48.md) [`0053d52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d52c.md)
- 新版 呼出元 1件 [`00c59e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e60.md) · 呼出先 11件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053aaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053aaa4.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`0053ca88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053ca88.md) [`0053d56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d56c.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

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
      "definition_site": "0051e3fc",
      "incomplete_value": true,
      "site": "0051e404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0051e3bc",
      "incomplete_value": true,
      "site": "0051e3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051e5b4",
      "incomplete_value": true,
      "site": "0051e5b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0051e574",
      "incomplete_value": true,
      "site": "0051e574",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051e3ec",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "0051e3f0",
      "READ",
      [
        "storage",
        "00c9acc8",
        null,
        "pointer"
      ]
    ],
    [
      "0051e404",
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
      "0051e3ec",
      "READ",
      [
        "storage",
        "00c9b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "0051e3f0",
      "READ",
      [
        "storage",
        "00c9b0c8",
        null,
        "pointer"
      ]
    ],
    [
      "0051e404",
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

- 旧版 [`0051e534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e358.md#insn-0051e534) · [`0051e574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e358.md#insn-0051e574) · [`0051e39c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e358.md#insn-0051e39c)
- 新版 `0051e574`（命令位置の公開資料なし） · `0051e5b4`（命令位置の公開資料なし） · `0051e3dc`（命令位置の公開資料なし）

~~~diff
- 0051e534 ["INT_ADD", "register:40f0:8", ["const:51e534:8", "const:4:8"]]
- 0051e534 ["CALL", null, ["callee:00c58710:8"]]
+ 0051e574 ["INT_ADD", "register:40f0:8", ["const:51e574:8", "const:4:8"]]
+ 0051e574 ["CALL", null, ["callee:00c58710:8"]]
- 0051e534 bytes 77e71c94
+ 0051e574 bytes 67e81c94
- 0051e574 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051e574 ["INT_ADD", "register:40f0:8", ["const:51e574:8", "const:4:8"]]
- 0051e574 ["CALLIND", null, ["register:0:8"]]
+ 0051e5b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051e5b4 ["INT_ADD", "register:40f0:8", ["const:51e5b4:8", "const:4:8"]]
+ 0051e5b4 ["CALLIND", null, ["register:0:8"]]
- 0051e574 bytes 20013fd6
+ 0051e5b4 bytes 20013fd6
- 0051e39c ["INT_ADD", "register:40f0:8", ["const:51e39c:8", "const:4:8"]]
- 0051e39c ["CALL", null, ["callee:00c58700:8"]]
+ 0051e3dc ["INT_ADD", "register:40f0:8", ["const:51e3dc:8", "const:4:8"]]
+ 0051e3dc ["CALL", null, ["callee:00c58700:8"]]
- 0051e39c bytes d9e71c94
+ 0051e3dc bytes c9e81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4e3694ce22b03a2bf77efb533996472"></a>

### [`0051e634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e634.md) → [`0051e674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e674.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051e6b4",
      "incomplete_value": true,
      "site": "0051e6c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3f2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e674",
      "incomplete_value": true,
      "site": "0051e688",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3b2:8"
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
      "0051e6b4",
      "READ",
      [
        "storage",
        "002ba3b2",
        null,
        "string"
      ]
    ],
    [
      "0051e6b8",
      "READ",
      [
        "storage",
        "002ba3bf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051e6b4",
      "READ",
      [
        "storage",
        "002ba3f2",
        null,
        "string"
      ]
    ],
    [
      "0051e6b8",
      "READ",
      [
        "storage",
        "002ba3ff",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051e66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e634.md#insn-0051e66c) · [`0051e6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e634.md#insn-0051e6bc) · [`0051e6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e634.md#insn-0051e6cc)
- 新版 `0051e6ac`（命令位置の公開資料なし） · `0051e6fc`（命令位置の公開資料なし） · `0051e70c`（命令位置の公開資料なし）

~~~diff
- 0051e66c ["COPY", "tmp:0:8", ["const:3b2:8"]]
- 0051e66c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0051e66c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0051e66c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0051e6ac ["COPY", "tmp:0:8", ["const:3f2:8"]]
+ 0051e6ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0051e6ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0051e6ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0051e66c bytes 08c90e91
+ 0051e6ac bytes 08c90f91
- 0051e6bc ["INT_ADD", "register:40f0:8", ["const:51e6bc:8", "const:4:8"]]
- 0051e6bc ["CALL", null, ["callee:004ff1a0:8"]]
+ 0051e6fc ["INT_ADD", "register:40f0:8", ["const:51e6fc:8", "const:4:8"]]
+ 0051e6fc ["CALL", null, ["callee:004ff1a0:8"]]
- 0051e6bc bytes a982ff97
+ 0051e6fc bytes a982ff97
- 0051e6cc ["INT_ADD", "register:40f0:8", ["const:51e6cc:8", "const:4:8"]]
- 0051e6cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051e70c ["INT_ADD", "register:40f0:8", ["const:51e70c:8", "const:4:8"]]
+ 0051e70c ["CALL", null, ["callee:00c57eb0:8"]]
- 0051e6cc bytes f9e41c94
+ 0051e70c bytes e9e51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d49fd545aaebb30c843ed42be45df117"></a>

### [`0051e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e730.md) → [`0051e770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e770.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points18Distribution_Point11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.58% / 新版 81.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051e7b4",
      "incomplete_value": true,
      "site": "0051e7c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:780:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e774",
      "incomplete_value": true,
      "site": "0051e780",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0051e7b0",
      "incomplete_value": true,
      "site": "0051e7c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:54b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e770",
      "incomplete_value": true,
      "site": "0051e784",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:50b:8"
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
      "definition_site": "0051e7b0",
      "incomplete_value": true,
      "site": "0051e7c4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0051e770",
      "incomplete_value": true,
      "site": "0051e784",
      "value": [
        "LOAD",
        "16",
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
      "0051e7b0",
      "READ",
      [
        "storage",
        "002ab50b",
        null,
        "string"
      ]
    ],
    [
      "0051e7b0",
      "READ",
      [
        "storage",
        "002ab51b",
        null,
        "string"
      ]
    ],
    [
      "0051e7b4",
      "READ",
      [
        "storage",
        "002c2740",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051e7b0",
      "READ",
      [
        "storage",
        "002ab54b",
        null,
        "string"
      ]
    ],
    [
      "0051e7b0",
      "READ",
      [
        "storage",
        "002ab55b",
        null,
        "string"
      ]
    ],
    [
      "0051e7b4",
      "READ",
      [
        "storage",
        "002c2780",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051e7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e730.md#insn-0051e7c0) · [`0051e754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e730.md#insn-0051e754) · [`0051e760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e730.md#insn-0051e760)
- 新版 `0051e800`（命令位置の公開資料なし） · `0051e794`（命令位置の公開資料なし） · `0051e7a0`（命令位置の公開資料なし）

~~~diff
- 0051e7c0 ["INT_ADD", "register:40f0:8", ["const:51e7c0:8", "const:4:8"]]
- 0051e7c0 ["CALL", null, ["callee:00c57f10:8"]]
+ 0051e800 ["INT_ADD", "register:40f0:8", ["const:51e800:8", "const:4:8"]]
+ 0051e800 ["CALL", null, ["callee:00c57f10:8"]]
- 0051e7c0 bytes d4e41c94
+ 0051e800 bytes c4e51c94
- 0051e754 ["INT_ADD", "register:40f0:8", ["const:51e754:8", "const:4:8"]]
- 0051e754 ["CALL", null, ["callee:00c57ef0:8"]]
+ 0051e794 ["INT_ADD", "register:40f0:8", ["const:51e794:8", "const:4:8"]]
+ 0051e794 ["CALL", null, ["callee:00c57ef0:8"]]
- 0051e754 bytes e7e41c94
+ 0051e794 bytes d7e51c94
- 0051e760 ["INT_ADD", "register:40f0:8", ["const:51e760:8", "const:4:8"]]
- 0051e760 ["CALL", null, ["callee:00c57e90:8"]]
+ 0051e7a0 ["INT_ADD", "register:40f0:8", ["const:51e7a0:8", "const:4:8"]]
+ 0051e7a0 ["CALL", null, ["callee:00c57e90:8"]]
- 0051e760 bytes cce41c94
+ 0051e7a0 bytes bce51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9191861015f194289fe16101919b350"></a>

### [`0051e810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e810.md) → [`0051e850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e850.md) _ZN5Botan14Cert_Extension23CRL_Distribution_Points18Distribution_Point11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

変更の種類 call_target, constant, operands_and_dependencies

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
      "definition_site": "0051e96c",
      "incomplete_value": true,
      "site": "0051e96c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051e92c",
      "incomplete_value": true,
      "site": "0051e92c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051e9b0",
      "incomplete_value": true,
      "site": "0051e9b0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051e970",
      "incomplete_value": true,
      "site": "0051e970",
      "value": [
        "LOAD",
        "8",
        [
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
      "0051e95c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0051e9a0",
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
      "0051e95c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051e9a0",
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

- 旧版 [`0051e8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e810.md#insn-0051e8ec) · [`0051e92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e810.md#insn-0051e92c) · [`0051e970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e810.md#insn-0051e970)
- 新版 `0051e92c`（命令位置の公開資料なし） · `0051e96c`（命令位置の公開資料なし） · `0051e9b0`（命令位置の公開資料なし）

~~~diff
- 0051e8ec ["INT_ADD", "register:40f0:8", ["const:51e8ec:8", "const:4:8"]]
- 0051e8ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051e92c ["INT_ADD", "register:40f0:8", ["const:51e92c:8", "const:4:8"]]
+ 0051e92c ["CALL", null, ["callee:00c57eb0:8"]]
- 0051e8ec bytes 71e41c94
+ 0051e92c bytes 61e51c94
- 0051e92c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051e92c ["INT_ADD", "register:40f0:8", ["const:51e92c:8", "const:4:8"]]
- 0051e92c ["CALLIND", null, ["register:0:8"]]
+ 0051e96c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051e96c ["INT_ADD", "register:40f0:8", ["const:51e96c:8", "const:4:8"]]
+ 0051e96c ["CALLIND", null, ["register:0:8"]]
- 0051e92c bytes 20013fd6
+ 0051e96c bytes 20013fd6
- 0051e970 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051e970 ["INT_ADD", "register:40f0:8", ["const:51e970:8", "const:4:8"]]
- 0051e970 ["CALLIND", null, ["register:0:8"]]
+ 0051e9b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051e9b0 ["INT_ADD", "register:40f0:8", ["const:51e9b0:8", "const:4:8"]]
+ 0051e9b0 ["CALLIND", null, ["register:0:8"]]
- 0051e970 bytes 20013fd6
+ 0051e9b0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c742686a6ec5ad4331352868b3ef1414"></a>

### [`0051ebcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051ebcc.md) → [`0051ec0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051ec0c.md) FUN_0051ec0c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051ec50",
      "incomplete_value": true,
      "site": "0051ec60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0051ec10",
      "incomplete_value": true,
      "site": "0051ec20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051ec4c",
      "incomplete_value": true,
      "site": "0051ec64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c0c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051ec0c",
      "incomplete_value": true,
      "site": "0051ec24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bcc:8"
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
      "definition_site": "0051ec4c",
      "incomplete_value": true,
      "site": "0051ec64",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0051ec0c",
      "incomplete_value": true,
      "site": "0051ec24",
      "value": [
        "LOAD",
        "16",
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
      "0051ec4c",
      "READ",
      [
        "storage",
        "002b2bcc",
        null,
        "string"
      ]
    ],
    [
      "0051ec4c",
      "READ",
      [
        "storage",
        "002b2bdc",
        null,
        "string"
      ]
    ],
    [
      "0051ec50",
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
      "0051ec4c",
      "READ",
      [
        "storage",
        "002b2c0c",
        null,
        "string"
      ]
    ],
    [
      "0051ec4c",
      "READ",
      [
        "storage",
        "002b2c1c",
        null,
        "string"
      ]
    ],
    [
      "0051ec50",
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

- 旧版 [`0051ec64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051ebcc.md#insn-0051ec64) · [`0051ebf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051ebcc.md#insn-0051ebf0) · [`0051ebfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051ebcc.md#insn-0051ebfc)
- 新版 `0051eca4`（命令位置の公開資料なし） · `0051ec30`（命令位置の公開資料なし） · `0051ec3c`（命令位置の公開資料なし）

~~~diff
- 0051ec64 ["INT_ADD", "register:40f0:8", ["const:51ec64:8", "const:4:8"]]
- 0051ec64 ["CALL", null, ["callee:00c57f10:8"]]
+ 0051eca4 ["INT_ADD", "register:40f0:8", ["const:51eca4:8", "const:4:8"]]
+ 0051eca4 ["CALL", null, ["callee:00c57f10:8"]]
- 0051ec64 bytes abe31c94
+ 0051eca4 bytes 9be41c94
- 0051ebf0 ["INT_ADD", "register:40f0:8", ["const:51ebf0:8", "const:4:8"]]
- 0051ebf0 ["CALL", null, ["callee:00c57ef0:8"]]
+ 0051ec30 ["INT_ADD", "register:40f0:8", ["const:51ec30:8", "const:4:8"]]
+ 0051ec30 ["CALL", null, ["callee:00c57ef0:8"]]
- 0051ebf0 bytes c0e31c94
+ 0051ec30 bytes b0e41c94
- 0051ebfc ["INT_ADD", "register:40f0:8", ["const:51ebfc:8", "const:4:8"]]
- 0051ebfc ["CALL", null, ["callee:00c57e90:8"]]
+ 0051ec3c ["INT_ADD", "register:40f0:8", ["const:51ec3c:8", "const:4:8"]]
+ 0051ec3c ["CALL", null, ["callee:00c57e90:8"]]
- 0051ebfc bytes a5e31c94
+ 0051ec3c bytes 95e41c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69fa9cdc381f59b406257c36438278d5"></a>

### [`0051ed8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051ed8c.md) → [`0051edcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051edcc.md) FUN_0051edcc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`004ff160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff160.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051eee8",
      "incomplete_value": true,
      "site": "0051eefc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051eea8",
      "incomplete_value": true,
      "site": "0051eebc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:260:8"
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
      "definition_site": "0051eee4",
      "incomplete_value": true,
      "site": "0051ef00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ca8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051eea4",
      "incomplete_value": true,
      "site": "0051eec0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c68:8"
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
      "definition_site": "0051eee4",
      "incomplete_value": true,
      "site": "0051ef00",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0051eea4",
      "incomplete_value": true,
      "site": "0051eec0",
      "value": [
        "LOAD",
        "16",
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
      "0051ee68",
      "PARAM",
      [
        "storage",
        "002bd72e",
        null,
        null
      ]
    ],
    [
      "0051ee94",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        null
      ]
    ],
    [
      "0051eee4",
      "READ",
      [
        "storage",
        "002bec68",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051ee68",
      "PARAM",
      [
        "storage",
        "002bd76e",
        null,
        null
      ]
    ],
    [
      "0051ee94",
      "PARAM",
      [
        "storage",
        "002a0fc7",
        null,
        null
      ]
    ],
    [
      "0051eee4",
      "READ",
      [
        "storage",
        "002beca8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051eee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051ed8c.md#insn-0051eee0) · [`0051ef00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051ed8c.md#insn-0051ef00) · [`0051edc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051ed8c.md#insn-0051edc4)
- 新版 `0051ef20`（命令位置の公開資料なし） · `0051ef40`（命令位置の公開資料なし） · `0051ee04`（命令位置の公開資料なし）

~~~diff
- 0051eee0 ["INT_ADD", "register:40f0:8", ["const:51eee0:8", "const:4:8"]]
- 0051eee0 ["CALL", null, ["callee:004ff1a0:8"]]
+ 0051ef20 ["INT_ADD", "register:40f0:8", ["const:51ef20:8", "const:4:8"]]
+ 0051ef20 ["CALL", null, ["callee:004ff1a0:8"]]
- 0051eee0 bytes a080ff97
+ 0051ef20 bytes a080ff97
- 0051ef00 ["INT_ADD", "register:40f0:8", ["const:51ef00:8", "const:4:8"]]
- 0051ef00 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051ef40 ["INT_ADD", "register:40f0:8", ["const:51ef40:8", "const:4:8"]]
+ 0051ef40 ["CALL", null, ["callee:00c57eb0:8"]]
- 0051ef00 bytes ece21c94
+ 0051ef40 bytes dce31c94
- 0051edc4 ["INT_ADD", "register:40f0:8", ["const:51edc4:8", "const:4:8"]]
- 0051edc4 ["CALL", null, ["callee:00c59970:8"]]
+ 0051ee04 ["INT_ADD", "register:40f0:8", ["const:51ee04:8", "const:4:8"]]
+ 0051ee04 ["CALL", null, ["callee:00c59970:8"]]
- 0051edc4 bytes ebe91c94
+ 0051ee04 bytes dbea1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da670d9937745c4c364cbdab71d8ca59"></a>

### [`0051f1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f1b4.md) → [`0051f1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f1f4.md) _ZN5Botan11X509_Object11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`004a5940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md) [`00c58310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58310.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004a5980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md) [`00c58710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58710.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051f2c4",
      "incomplete_value": true,
      "site": "0051f2c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051f284",
      "incomplete_value": true,
      "site": "0051f284",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051f308",
      "incomplete_value": true,
      "site": "0051f308",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051f2c8",
      "incomplete_value": true,
      "site": "0051f2c8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051f2b4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0051f2f8",
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
      "0051f2b4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051f2f8",
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

- 旧版 [`0051f244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f1b4.md#insn-0051f244) · [`0051f284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f1b4.md#insn-0051f284) · [`0051f2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f1b4.md#insn-0051f2c8)
- 新版 `0051f284`（命令位置の公開資料なし） · `0051f2c4`（命令位置の公開資料なし） · `0051f308`（命令位置の公開資料なし）

~~~diff
- 0051f244 ["INT_ADD", "register:40f0:8", ["const:51f244:8", "const:4:8"]]
- 0051f244 ["CALL", null, ["callee:00c58710:8"]]
+ 0051f284 ["INT_ADD", "register:40f0:8", ["const:51f284:8", "const:4:8"]]
+ 0051f284 ["CALL", null, ["callee:00c58710:8"]]
- 0051f244 bytes 33e41c94
+ 0051f284 bytes 23e51c94
- 0051f284 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051f284 ["INT_ADD", "register:40f0:8", ["const:51f284:8", "const:4:8"]]
- 0051f284 ["CALLIND", null, ["register:0:8"]]
+ 0051f2c4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051f2c4 ["INT_ADD", "register:40f0:8", ["const:51f2c4:8", "const:4:8"]]
+ 0051f2c4 ["CALLIND", null, ["register:0:8"]]
- 0051f284 bytes 20013fd6
+ 0051f2c4 bytes 20013fd6
- 0051f2c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051f2c8 ["INT_ADD", "register:40f0:8", ["const:51f2c8:8", "const:4:8"]]
- 0051f2c8 ["CALLIND", null, ["register:0:8"]]
+ 0051f308 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051f308 ["INT_ADD", "register:40f0:8", ["const:51f308:8", "const:4:8"]]
+ 0051f308 ["CALLIND", null, ["register:0:8"]]
- 0051f2c8 bytes 20013fd6
+ 0051f308 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-578c99b1271afd314b5a755a00ff33d8"></a>

### [`0051f544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f544.md) → [`0051f584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f584.md) _ZNK5Botan11X509_Object23hash_used_for_signatureEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a90.md) · 呼出先 16件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0051f9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f9d0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md) [`00547b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b30.md)
- 新版 呼出元 1件 [`00c59e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e90.md) · 呼出先 16件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0051fa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051fa10.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md) [`00547b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0051f5c0",
      "incomplete_value": false,
      "site": "0051f5c8",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051f580",
      "incomplete_value": false,
      "site": "0051f588",
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
            "const:2b0:8"
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
      "definition_site": "0051f824",
      "incomplete_value": false,
      "site": "0051f830",
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
            "const:c34:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051f7e4",
      "incomplete_value": false,
      "site": "0051f7f0",
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
            "const:bf4:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0051f878",
      "incomplete_value": true,
      "site": "0051f884",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051f838",
      "incomplete_value": true,
      "site": "0051f844",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f8:8"
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
      "0051f5c8",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0051f60c",
      "READ",
      [
        "storage",
        "00c6a2d0",
        null,
        "pointer"
      ]
    ],
    [
      "0051f60c",
      "READ",
      [
        "storage",
        "00c6a2d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0051f5c8",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0051f60c",
      "READ",
      [
        "storage",
        "00c6a6d0",
        null,
        "pointer"
      ]
    ],
    [
      "0051f60c",
      "READ",
      [
        "storage",
        "00c6a6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051f7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f544.md#insn-0051f7b0) · [`0051f7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f544.md#insn-0051f7f0) · [`0051f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f544.md#insn-0051f844)
- 新版 `0051f7f0`（命令位置の公開資料なし） · `0051f830`（命令位置の公開資料なし） · `0051f884`（命令位置の公開資料なし）

~~~diff
- 0051f7b0 ["INT_ADD", "register:40f0:8", ["const:51f7b0:8", "const:4:8"]]
- 0051f7b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0051f7f0 ["INT_ADD", "register:40f0:8", ["const:51f7f0:8", "const:4:8"]]
+ 0051f7f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0051f7b0 bytes c0e01c94
+ 0051f7f0 bytes b0e11c94
- 0051f7f0 ["INT_ADD", "register:40f0:8", ["const:51f7f0:8", "const:4:8"]]
- 0051f7f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0051f830 ["INT_ADD", "register:40f0:8", ["const:51f830:8", "const:4:8"]]
+ 0051f830 ["CALL", null, ["callee:00c57f60:8"]]
- 0051f7f0 bytes dce01c94
+ 0051f830 bytes cce11c94
- 0051f844 ["INT_ADD", "register:40f0:8", ["const:51f844:8", "const:4:8"]]
- 0051f844 ["CALL", null, ["callee:00c57f10:8"]]
+ 0051f884 ["INT_ADD", "register:40f0:8", ["const:51f884:8", "const:4:8"]]
+ 0051f884 ["CALL", null, ["callee:00c57f10:8"]]
- 0051f844 bytes b3e01c94
+ 0051f884 bytes a3e11c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a49b27b17438daff24f68e9166280d6b"></a>

### [`0051f9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f9d0.md) → [`0051fa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051fa10.md) FUN_0051fa10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0051f544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f544.md) [`00520010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520010.md) · 呼出先 15件 [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0051f584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f584.md) [`00520050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520050.md) · 呼出先 15件 [`004a577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a577c.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.01% / 新版 96.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051fa50",
      "incomplete_value": true,
      "site": "0051fa50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0051fa10",
      "incomplete_value": true,
      "site": "0051fa10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0051fcf8",
      "incomplete_value": true,
      "site": "0051fcf8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051fcb8",
      "incomplete_value": true,
      "site": "0051fcb8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051fd7c",
      "incomplete_value": true,
      "site": "0051fd7c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051fd3c",
      "incomplete_value": true,
      "site": "0051fd3c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051fa38",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "0051fa50",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051fa7c",
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
      "0051fa38",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0051fa50",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051fa7c",
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

- 旧版 [`0051fa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f9d0.md#insn-0051fa50) · [`0051fcb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f9d0.md#insn-0051fcb8) · [`0051fd3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f9d0.md#insn-0051fd3c)
- 新版 `0051fa90`（命令位置の公開資料なし） · `0051fcf8`（命令位置の公開資料なし） · `0051fd7c`（命令位置の公開資料なし）

~~~diff
- 0051fa50 ["INT_ADD", "register:40f0:8", ["const:51fa50:8", "const:4:8"]]
- 0051fa50 ["CALL", null, ["callee:00c58690:8"]]
+ 0051fa90 ["INT_ADD", "register:40f0:8", ["const:51fa90:8", "const:4:8"]]
+ 0051fa90 ["CALL", null, ["callee:00c58690:8"]]
- 0051fa50 bytes 10e21c94
+ 0051fa90 bytes 00e31c94
- 0051fcb8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051fcb8 ["INT_ADD", "register:40f0:8", ["const:51fcb8:8", "const:4:8"]]
- 0051fcb8 ["CALLIND", null, ["register:0:8"]]
+ 0051fcf8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051fcf8 ["INT_ADD", "register:40f0:8", ["const:51fcf8:8", "const:4:8"]]
+ 0051fcf8 ["CALLIND", null, ["register:0:8"]]
- 0051fcb8 bytes 20013fd6
+ 0051fcf8 bytes 20013fd6
- 0051fd3c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051fd3c ["INT_ADD", "register:40f0:8", ["const:51fd3c:8", "const:4:8"]]
- 0051fd3c ["CALLIND", null, ["register:0:8"]]
+ 0051fd7c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051fd7c ["INT_ADD", "register:40f0:8", ["const:51fd7c:8", "const:4:8"]]
+ 0051fd7c ["CALLIND", null, ["register:0:8"]]
- 0051fd3c bytes 20013fd6
+ 0051fd7c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b4831245d5e6fa470956a7e071f4dc9"></a>

### [`00520010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520010.md) → [`00520050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520050.md) _ZNK5Botan11X509_Object16verify_signatureERKNS_10Public_KeyE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c598b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598b0.md) · 呼出先 19件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004a6bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6bdc.md) [`004acbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acbe4.md) [`0051f9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051f/0051f9d0.md) [`00547ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547ad4.md)
- 新版 呼出元 1件 [`00c59cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cb0.md) · 呼出先 19件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004a6c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6c1c.md) [`004acc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acc24.md) [`0051fa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051fa10.md) [`00547b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b14.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00520098",
      "incomplete_value": false,
      "site": "00520098",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00520058",
      "incomplete_value": false,
      "site": "00520058",
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
            "const:2b0:8"
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
      "definition_site": "0052042c",
      "incomplete_value": false,
      "site": "00520434",
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
            "const:b9f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005203ec",
      "incomplete_value": false,
      "site": "005203f4",
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
            "const:ad2:8"
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
      "definition_site": "00520440",
      "incomplete_value": false,
      "site": "00520448",
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
            "const:2e9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00520400",
      "incomplete_value": false,
      "site": "00520408",
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
            "const:2a9:8"
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
      "00520098",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005200dc",
      "READ",
      [
        "storage",
        "00c6a2d0",
        null,
        "pointer"
      ]
    ],
    [
      "005200dc",
      "READ",
      [
        "storage",
        "00c6a2d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00520098",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005200dc",
      "READ",
      [
        "storage",
        "00c6a6d0",
        null,
        "pointer"
      ]
    ],
    [
      "005200dc",
      "READ",
      [
        "storage",
        "00c6a6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005203f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520010.md#insn-005203f4) · [`00520408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520010.md#insn-00520408) · [`005204c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520010.md#insn-005204c4)
- 新版 `00520434`（命令位置の公開資料なし） · `00520448`（命令位置の公開資料なし） · `00520504`（命令位置の公開資料なし）

~~~diff
- 005203f4 ["INT_ADD", "register:40f0:8", ["const:5203f4:8", "const:4:8"]]
- 005203f4 ["CALL", null, ["callee:004acc24:8"]]
+ 00520434 ["INT_ADD", "register:40f0:8", ["const:520434:8", "const:4:8"]]
+ 00520434 ["CALL", null, ["callee:004acc24:8"]]
- 005203f4 bytes fc31fe97
+ 00520434 bytes fc31fe97
- 00520408 ["INT_ADD", "register:40f0:8", ["const:520408:8", "const:4:8"]]
- 00520408 ["CALL", null, ["callee:004acc24:8"]]
+ 00520448 ["INT_ADD", "register:40f0:8", ["const:520448:8", "const:4:8"]]
+ 00520448 ["CALL", null, ["callee:004acc24:8"]]
- 00520408 bytes f731fe97
+ 00520448 bytes f731fe97
- 005204c4 ["INT_ADD", "register:40f0:8", ["const:5204c4:8", "const:4:8"]]
- 005204c4 ["CALL", null, ["callee:00c580b0:8"]]
+ 00520504 ["INT_ADD", "register:40f0:8", ["const:520504:8", "const:4:8"]]
+ 00520504 ["CALL", null, ["callee:00c580b0:8"]]
- 005204c4 bytes fbdd1c94
+ 00520504 bytes ebde1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0abffeb3bf439e2edd440d8d88a3c37"></a>

### [`005209a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/005209a4.md) → [`005209e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/005209e4.md) _ZNK5Botan16X509_Certificate9PEM_labelEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00520a08",
      "incomplete_value": true,
      "site": "00520a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:408:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005209c8",
      "incomplete_value": true,
      "site": "005209c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c8:8"
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
      "005209f8",
      "READ",
      [
        "storage",
        "002ba3c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005209f8",
      "READ",
      [
        "storage",
        "002ba408",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005209ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/005209a4.md#insn-005209ac)
- 新版 `005209ec`（命令位置の公開資料なし）

~~~diff
- 005209ac ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 005209ac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005209ac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005209ac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005209ec ["COPY", "tmp:0:8", ["const:408:8"]]
+ 005209ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005209ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005209ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005209ac bytes 4a210f91
+ 005209ec bytes 4a211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-373e5ad73c7f0fd21fbdaf3ea9227dd7"></a>

### [`005209d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/005209d0.md) → [`00520a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520a10.md) _ZNK5Botan16X509_Certificate20alternate_PEM_labelsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "00520a34",
      "incomplete_value": true,
      "site": "00520a44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d67:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005209f4",
      "incomplete_value": true,
      "site": "00520a04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d27:8"
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
      "00520a34",
      "READ",
      [
        "storage",
        "002b1d27",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00520a34",
      "READ",
      [
        "storage",
        "002b1d67",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005209e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/005209d0.md#insn-005209e8) · [`00520a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/005209d0.md#insn-00520a14) · [`00520a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/005209d0.md#insn-00520a24)
- 新版 `00520a28`（命令位置の公開資料なし） · `00520a54`（命令位置の公開資料なし） · `00520a64`（命令位置の公開資料なし）

~~~diff
- 005209e8 ["COPY", "tmp:0:8", ["const:d27:8"]]
- 005209e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005209e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005209e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00520a28 ["COPY", "tmp:0:8", ["const:d67:8"]]
+ 00520a28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00520a28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00520a28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005209e8 bytes 299d3491
+ 00520a28 bytes 299d3591
- 00520a14 ["INT_ADD", "register:40f0:8", ["const:520a14:8", "const:4:8"]]
- 00520a14 ["CALL", null, ["callee:00473540:8"]]
+ 00520a54 ["INT_ADD", "register:40f0:8", ["const:520a54:8", "const:4:8"]]
+ 00520a54 ["CALL", null, ["callee:00473540:8"]]
- 00520a14 bytes bb4afd97
+ 00520a54 bytes bb4afd97
- 00520a24 ["INT_ADD", "register:40f0:8", ["const:520a24:8", "const:4:8"]]
- 00520a24 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00520a64 ["INT_ADD", "register:40f0:8", ["const:520a64:8", "const:4:8"]]
+ 00520a64 ["CALL", null, ["callee:00c57eb0:8"]]
- 00520a24 bytes 23dc1c94
+ 00520a64 bytes 13dd1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4b2f2453fbf7ad993d5831df2d74b1e"></a>

### [`00520a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520a78.md) → [`00520ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520ab8.md) _ZN5Botan16X509_CertificateC1ERNS_10DataSourceE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md) [`00c59880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59880.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) [`00c59c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520af8",
      "incomplete_value": true,
      "site": "00520af8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00520ab8",
      "incomplete_value": true,
      "site": "00520ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00520af8",
      "incomplete_value": true,
      "site": "00520af8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00520ab8",
      "incomplete_value": true,
      "site": "00520ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00520b38",
      "incomplete_value": true,
      "site": "00520b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00520af8",
      "incomplete_value": true,
      "site": "00520b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00520ad8",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00520ae0",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00520af8",
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
      "00520ad8",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00520ae0",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00520af8",
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

- 旧版 [`00520a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520a78.md#insn-00520a90) · [`00520a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520a78.md#insn-00520a98) · [`00520aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520a78.md#insn-00520aa0)
- 新版 `00520ad0`（命令位置の公開資料なし） · `00520ad8`（命令位置の公開資料なし） · `00520ae0`（命令位置の公開資料なし）

~~~diff
- 00520a90 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00520ad0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00520a90 bytes c83b00d0
+ 00520ad0 bytes c83b00f0
- 00520a98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 00520a98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00520ad8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 00520ad8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00520a98 bytes 08ad46f9
+ 00520ad8 bytes 08ad40f9
- 00520aa0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:938:8"]]
- 00520aa0 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00520ae0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
+ 00520ae0 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00520aa0 bytes 4a9d44f9
+ 00520ae0 bytes 4a9d46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2e6ea4e795b575cb544f86e0a171bb3"></a>

### [`00520bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520bcc.md) → [`00520c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520c0c.md) _ZN5Botan16X509_CertificateC1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c597c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c597c0.md) · 呼出先 7件 [`00540388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540388.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`00c59bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59bc0.md) · 呼出先 7件 [`005403c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520c4c",
      "incomplete_value": true,
      "site": "00520c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00520c0c",
      "incomplete_value": true,
      "site": "00520c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00520c4c",
      "incomplete_value": true,
      "site": "00520c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00520c0c",
      "incomplete_value": true,
      "site": "00520c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00520c94",
      "incomplete_value": true,
      "site": "00520ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00520c54",
      "incomplete_value": true,
      "site": "00520c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00520c2c",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00520c34",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00520c4c",
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
      "00520c2c",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00520c34",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00520c4c",
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

- 旧版 [`00520cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520bcc.md#insn-00520cb8) · [`00520be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520bcc.md#insn-00520be4) · [`00520bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520bcc.md#insn-00520bec)
- 新版 `00520cf8`（命令位置の公開資料なし） · `00520c24`（命令位置の公開資料なし） · `00520c2c`（命令位置の公開資料なし）

~~~diff
- 00520cb8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00520cb8 ["INT_ADD", "register:40f0:8", ["const:520cb8:8", "const:4:8"]]
- 00520cb8 ["CALLIND", null, ["register:0:8"]]
+ 00520cf8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00520cf8 ["INT_ADD", "register:40f0:8", ["const:520cf8:8", "const:4:8"]]
+ 00520cf8 ["CALLIND", null, ["register:0:8"]]
- 00520cb8 bytes 20013fd6
+ 00520cf8 bytes 20013fd6
- 00520be4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00520c24 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00520be4 bytes c83b00d0
+ 00520c24 bytes c83b00f0
- 00520bec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 00520bec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00520c2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 00520c2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00520bec bytes 08ad46f9
+ 00520c2c bytes 08ad40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-620142a47eb6389fe7e7c92b5bb750aa"></a>

### [`00520d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520d44.md) → [`00520d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520d84.md) _ZN5Botan16X509_CertificateC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59660.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md) [`00c59260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) [`00c59270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md)
- 新版 呼出元 1件 [`00c59a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a60.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) [`00c59660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59660.md) [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520dc4",
      "incomplete_value": true,
      "site": "00520dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00520d84",
      "incomplete_value": true,
      "site": "00520d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00520dc4",
      "incomplete_value": true,
      "site": "00520dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00520d84",
      "incomplete_value": true,
      "site": "00520d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00520e04",
      "incomplete_value": true,
      "site": "00520e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00520dc4",
      "incomplete_value": true,
      "site": "00520dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00520da4",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00520dac",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00520dc4",
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
      "00520da4",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00520dac",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00520dc4",
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

- 旧版 [`00520d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520d44.md#insn-00520d5c) · [`00520d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520d44.md#insn-00520d64) · [`00520d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520d44.md#insn-00520d6c)
- 新版 `00520d9c`（命令位置の公開資料なし） · `00520da4`（命令位置の公開資料なし） · `00520dac`（命令位置の公開資料なし）

~~~diff
- 00520d5c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00520d9c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00520d5c bytes c83b00d0
+ 00520d9c bytes c83b00f0
- 00520d64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 00520d64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00520da4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 00520da4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00520d64 bytes 08ad46f9
+ 00520da4 bytes 08ad40f9
- 00520d6c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:938:8"]]
- 00520d6c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00520dac ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
+ 00520dac ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00520d6c bytes 4a9d44f9
+ 00520dac bytes 4a9d46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36ef50293ac7075798b22e2f8723077e"></a>

### [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) → [`00520eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520eb0.md) _ZN5Botan16X509_Certificate12force_decodeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 68件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md)
- 新版 呼出元 0件  · 呼出先 68件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004a577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a577c.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `call_target` 8件, `store_value` 14件

アドレスに依存する影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00521154",
      "incomplete_value": true,
      "site": "00521158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00521114",
      "incomplete_value": true,
      "site": "00521118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00521220",
      "incomplete_value": false,
      "site": "00521220",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005211e0",
      "incomplete_value": false,
      "site": "005211e0",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00521668",
      "incomplete_value": true,
      "site": "00521668",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00521628",
      "incomplete_value": true,
      "site": "00521628",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00521028",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0052114c",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00521158",
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
      "00521028",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052114c",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00521158",
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

- 旧版 [`00520fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md#insn-00520fb8) · [`00520ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md#insn-00520ff8) · [`0052117c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md#insn-0052117c)
- 新版 `00520ff8`（命令位置の公開資料なし） · `00521038`（命令位置の公開資料なし） · `005211bc`（命令位置の公開資料なし）

~~~diff
- 00520fb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00520fb8 ["INT_ADD", "register:40f0:8", ["const:520fb8:8", "const:4:8"]]
- 00520fb8 ["CALLIND", null, ["register:0:8"]]
+ 00520ff8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00520ff8 ["INT_ADD", "register:40f0:8", ["const:520ff8:8", "const:4:8"]]
+ 00520ff8 ["CALLIND", null, ["register:0:8"]]
- 00520fb8 bytes 00013fd6
+ 00520ff8 bytes 00013fd6
- 00520ff8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00520ff8 ["INT_ADD", "register:40f0:8", ["const:520ff8:8", "const:4:8"]]
- 00520ff8 ["CALLIND", null, ["register:0:8"]]
+ 00521038 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00521038 ["INT_ADD", "register:40f0:8", ["const:521038:8", "const:4:8"]]
+ 00521038 ["CALLIND", null, ["register:0:8"]]
- 00520ff8 bytes 20013fd6
+ 00521038 bytes 20013fd6
- 0052117c ["COPY", "register:0:8", ["register:4040:8"]]
- 0052117c ["INT_ADD", "register:40f0:8", ["const:52117c:8", "const:4:8"]]
- 0052117c ["CALLIND", null, ["register:0:8"]]
+ 005211bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005211bc ["INT_ADD", "register:40f0:8", ["const:5211bc:8", "const:4:8"]]
+ 005211bc ["CALLIND", null, ["register:0:8"]]
- 0052117c bytes 00013fd6
+ 005211bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8bc7f472a804d5cefaceee425855af6"></a>

### [`00522824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522824.md) → [`00522864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522864.md) _ZNK5Botan16X509_Certificate4dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "definition_site": "005228c4",
      "incomplete_value": false,
      "site": "005228cc",
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
            "const:cef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00522884",
      "incomplete_value": false,
      "site": "0052288c",
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
            "const:caf:8"
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
      "definition_site": "00522900",
      "incomplete_value": true,
      "site": "0052290c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005228c0",
      "incomplete_value": true,
      "site": "005228cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:948:8"
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
      "definition_site": "005228fc",
      "incomplete_value": false,
      "site": "0052290c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "005228bc",
      "incomplete_value": false,
      "site": "005228cc",
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
      "005228c4",
      "PARAM",
      [
        "storage",
        "002b0caf",
        null,
        "string"
      ]
    ],
    [
      "005228fc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00522900",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005228c4",
      "PARAM",
      [
        "storage",
        "002b0cef",
        null,
        "string"
      ]
    ],
    [
      "005228fc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00522900",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052288c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522824.md#insn-0052288c) · [`005228cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522824.md#insn-005228cc) · [`00522878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522824.md#insn-00522878)
- 新版 `005228cc`（命令位置の公開資料なし） · `0052290c`（命令位置の公開資料なし） · `005228b8`（命令位置の公開資料なし）

~~~diff
- 0052288c ["INT_ADD", "register:40f0:8", ["const:52288c:8", "const:4:8"]]
- 0052288c ["CALL", null, ["callee:0043ddd8:8"]]
+ 005228cc ["INT_ADD", "register:40f0:8", ["const:5228cc:8", "const:4:8"]]
+ 005228cc ["CALL", null, ["callee:0043ddd8:8"]]
- 0052288c bytes 436dfc97
+ 005228cc bytes 436dfc97
- 005228cc ["INT_ADD", "register:40f0:8", ["const:5228cc:8", "const:4:8"]]
- 005228cc ["CALL", null, ["callee:00c57f10:8"]]
+ 0052290c ["INT_ADD", "register:40f0:8", ["const:52290c:8", "const:4:8"]]
+ 0052290c ["CALL", null, ["callee:00c57f10:8"]]
- 005228cc bytes 91d41c94
+ 0052290c bytes 81d51c94
- 00522878 ["INT_ADD", "register:40f0:8", ["const:522878:8", "const:4:8"]]
- 00522878 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005228b8 ["INT_ADD", "register:40f0:8", ["const:5228b8:8", "const:4:8"]]
+ 005228b8 ["CALL", null, ["callee:00c57ef0:8"]]
- 00522878 bytes 9ed41c94
+ 005228b8 bytes 8ed51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7028ba26bdd9ed643195cc011d4212de"></a>

### [`00522b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522b20.md) → [`00522b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522b60.md) _ZNK5Botan16X509_Certificate13allowed_usageENS_10Usage_TypeE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59aa0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md) [`00c59840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59840.md)
- 新版 呼出元 1件 [`00c59ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ea0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md) [`00c59c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c40.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.30% / 新版 90.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00522bec",
      "incomplete_value": true,
      "site": "00522bf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cba:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00522bac",
      "incomplete_value": true,
      "site": "00522bb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c7a:8"
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
      "definition_site": "00522c94",
      "incomplete_value": true,
      "site": "00522c94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c45:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00522c54",
      "incomplete_value": true,
      "site": "00522c54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c05:8"
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
      "definition_site": "00522c88",
      "incomplete_value": true,
      "site": "00522c98",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00522c48",
      "incomplete_value": true,
      "site": "00522c58",
      "value": [
        "LOAD",
        "8",
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
      "00522bec",
      "READ",
      [
        "storage",
        "002b4c7a",
        null,
        "string"
      ]
    ],
    [
      "00522c84",
      "READ",
      [
        "storage",
        "002bec05",
        null,
        "string"
      ]
    ],
    [
      "00522c88",
      "READ",
      [
        "storage",
        "002bec0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00522bec",
      "READ",
      [
        "storage",
        "002b4cba",
        null,
        "string"
      ]
    ],
    [
      "00522c84",
      "READ",
      [
        "storage",
        "002bec45",
        null,
        "string"
      ]
    ],
    [
      "00522c88",
      "READ",
      [
        "storage",
        "002bec4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00522b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522b20.md#insn-00522b64) · [`00522b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522b20.md#insn-00522b74) · [`00522b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522b20.md#insn-00522b84)
- 新版 `00522ba4`（命令位置の公開資料なし） · `00522bb4`（命令位置の公開資料なし） · `00522bc4`（命令位置の公開資料なし）

~~~diff
- 00522b64 ["INT_ADD", "register:40f0:8", ["const:522b64:8", "const:4:8"]]
- 00522b64 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522ba4 ["INT_ADD", "register:40f0:8", ["const:522ba4:8", "const:4:8"]]
+ 00522ba4 ["CALL", null, ["callee:00c599f0:8"]]
- 00522b64 bytes a3da1c94
+ 00522ba4 bytes 93db1c94
- 00522b74 ["INT_ADD", "register:40f0:8", ["const:522b74:8", "const:4:8"]]
- 00522b74 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522bb4 ["INT_ADD", "register:40f0:8", ["const:522bb4:8", "const:4:8"]]
+ 00522bb4 ["CALL", null, ["callee:00c599f0:8"]]
- 00522b74 bytes 9fda1c94
+ 00522bb4 bytes 8fdb1c94
- 00522b84 ["INT_ADD", "register:40f0:8", ["const:522b84:8", "const:4:8"]]
- 00522b84 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522bc4 ["INT_ADD", "register:40f0:8", ["const:522bc4:8", "const:4:8"]]
+ 00522bc4 ["CALL", null, ["callee:00c599f0:8"]]
- 00522b84 bytes 9bda1c94
+ 00522bc4 bytes 8bdb1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f69eb97bbd63c3fba3bef61256bcb3fb"></a>

### [`0052308c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/0052308c.md) → [`005230cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/005230cc.md) _ZNK5Botan16X509_Certificate12subject_infoERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ab0.md) · 呼出先 16件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`00548058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00c59eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59eb0.md) · 呼出先 16件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`00548098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00523400",
      "incomplete_value": false,
      "site": "00523408",
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
            "const:56c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005233c0",
      "incomplete_value": false,
      "site": "005233c8",
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
            "const:52c:8"
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
      "definition_site": "0052343c",
      "incomplete_value": false,
      "site": "00523444",
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
            "const:ea5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005233fc",
      "incomplete_value": false,
      "site": "00523404",
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
            "const:e65:8"
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
      "definition_site": "00523478",
      "incomplete_value": false,
      "site": "00523480",
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
            "const:209:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00523438",
      "incomplete_value": false,
      "site": "00523440",
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
            "const:13c:8"
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
      "00523400",
      "PARAM",
      [
        "storage",
        "002ab52c",
        null,
        "string"
      ]
    ],
    [
      "0052343c",
      "PARAM",
      [
        "storage",
        "002b4e65",
        null,
        "string"
      ]
    ],
    [
      "00523478",
      "PARAM",
      [
        "storage",
        "002a113c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00523400",
      "PARAM",
      [
        "storage",
        "002ab56c",
        null,
        "string"
      ]
    ],
    [
      "0052343c",
      "PARAM",
      [
        "storage",
        "002b4ea5",
        null,
        "string"
      ]
    ],
    [
      "00523478",
      "PARAM",
      [
        "storage",
        "002a1209",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005233c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/0052308c.md#insn-005233c8) · [`00523404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/0052308c.md#insn-00523404) · [`00523440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/0052308c.md#insn-00523440)
- 新版 `00523408`（命令位置の公開資料なし） · `00523444`（命令位置の公開資料なし） · `00523480`（命令位置の公開資料なし）

~~~diff
- 005233c8 ["INT_ADD", "register:40f0:8", ["const:5233c8:8", "const:4:8"]]
- 005233c8 ["CALL", null, ["callee:00441e94:8"]]
+ 00523408 ["INT_ADD", "register:40f0:8", ["const:523408:8", "const:4:8"]]
+ 00523408 ["CALL", null, ["callee:00441e94:8"]]
- 005233c8 bytes a37afc97
+ 00523408 bytes a37afc97
- 00523404 ["INT_ADD", "register:40f0:8", ["const:523404:8", "const:4:8"]]
- 00523404 ["CALL", null, ["callee:00441e94:8"]]
+ 00523444 ["INT_ADD", "register:40f0:8", ["const:523444:8", "const:4:8"]]
+ 00523444 ["CALL", null, ["callee:00441e94:8"]]
- 00523404 bytes 947afc97
+ 00523444 bytes 947afc97
- 00523440 ["INT_ADD", "register:40f0:8", ["const:523440:8", "const:4:8"]]
- 00523440 ["CALL", null, ["callee:00441e94:8"]]
+ 00523480 ["INT_ADD", "register:40f0:8", ["const:523480:8", "const:4:8"]]
+ 00523480 ["CALL", null, ["callee:00441e94:8"]]
- 00523440 bytes 857afc97
+ 00523480 bytes 857afc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-849e2c3702e920f9f870a77559e35695"></a>

### [`005249a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005249a0.md) → [`005249e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/005249e0.md) _ZNK5Botan16X509_Certificate9to_stringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 27件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0053ee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ee30.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0053ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ee70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.84% / 新版 92.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 47件, `store_destination` 2件, `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00524a24",
      "incomplete_value": true,
      "site": "00524a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "005249e4",
      "incomplete_value": true,
      "site": "005249f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00524a30",
      "incomplete_value": true,
      "site": "00524a3c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005249f0",
      "incomplete_value": true,
      "site": "005249fc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00524a44",
      "incomplete_value": true,
      "site": "00524a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:e0:8"
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
      "definition_site": "00524a04",
      "incomplete_value": true,
      "site": "00524a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:e0:8"
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
      "00524a0c",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "00524a1c",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00524a30",
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
      "00524a0c",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00524a1c",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00524a30",
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

- 旧版 [`00524a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005249a0.md#insn-00524a3c) · [`00524a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005249a0.md#insn-00524a74) · [`00524a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005249a0.md#insn-00524a9c)
- 新版 `00524a7c`（命令位置の公開資料なし） · `00524ab4`（命令位置の公開資料なし） · `00524adc`（命令位置の公開資料なし）

~~~diff
- 00524a3c ["INT_ADD", "register:40f0:8", ["const:524a3c:8", "const:4:8"]]
- 00524a3c ["CALL", null, ["callee:00c581f0:8"]]
+ 00524a7c ["INT_ADD", "register:40f0:8", ["const:524a7c:8", "const:4:8"]]
+ 00524a7c ["CALL", null, ["callee:00c581f0:8"]]
- 00524a3c bytes edcc1c94
+ 00524a7c bytes ddcd1c94
- 00524a74 ["INT_ADD", "register:40f0:8", ["const:524a74:8", "const:4:8"]]
- 00524a74 ["CALL", null, ["callee:004594d0:8"]]
+ 00524ab4 ["INT_ADD", "register:40f0:8", ["const:524ab4:8", "const:4:8"]]
+ 00524ab4 ["CALL", null, ["callee:004594d0:8"]]
- 00524a74 bytes 87d2fc97
+ 00524ab4 bytes 87d2fc97
- 00524a9c ["INT_ADD", "register:40f0:8", ["const:524a9c:8", "const:4:8"]]
- 00524a9c ["CALL", null, ["callee:004594d0:8"]]
+ 00524adc ["INT_ADD", "register:40f0:8", ["const:524adc:8", "const:4:8"]]
+ 00524adc ["CALL", null, ["callee:004594d0:8"]]
- 00524a9c bytes 7dd2fc97
+ 00524adc bytes 7dd2fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b93bb8be6c5b828cf73cf5db62bd1752"></a>

### [`005262a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/005262a0.md) → [`005262e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005262e0.md) _ZN5Botan17X509_Cert_Options17add_ex_constraintERKNS_3OIDE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0054b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0054b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00526320",
      "incomplete_value": true,
      "site": "00526324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005262e0",
      "incomplete_value": true,
      "site": "005262e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00526314",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "00526324",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00526314",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00526324",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005262d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/005262a0.md#insn-005262d4) · [`005262f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/005262a0.md#insn-005262f8) · [`00526310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/005262a0.md#insn-00526310)
- 新版 `00526314`（命令位置の公開資料なし） · `00526338`（命令位置の公開資料なし） · `00526350`（命令位置の公開資料なし）

~~~diff
- 005262d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
- 005262d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00526314 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
+ 00526314 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005262d4 bytes 08a144f9
+ 00526314 bytes 08a146f9
- 005262f8 ["INT_ADD", "register:40f0:8", ["const:5262f8:8", "const:4:8"]]
- 005262f8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00526338 ["INT_ADD", "register:40f0:8", ["const:526338:8", "const:4:8"]]
+ 00526338 ["CALL", null, ["callee:00c57e90:8"]]
- 005262f8 bytes e6c51c94
+ 00526338 bytes d6c61c94
- 00526310 ["INT_ADD", "register:40f0:8", ["const:526310:8", "const:4:8"]]
- 00526310 ["CALL", null, ["callee:00c58000:8"]]
+ 00526350 ["INT_ADD", "register:40f0:8", ["const:526350:8", "const:4:8"]]
+ 00526350 ["CALL", null, ["callee:00c58000:8"]]
- 00526310 bytes 3cc61c94
+ 00526350 bytes 2cc71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cbde5da1527cd35b3a0addfe28dee78"></a>

### [`00526370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526370.md) → [`005263b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005263b0.md) _ZN5Botan17X509_Cert_Options17add_ex_constraintERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0054d804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d804.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0054d844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d844.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00526400",
      "incomplete_value": true,
      "site": "00526408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005263c0",
      "incomplete_value": true,
      "site": "005263c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005263f8",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "00526408",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005263f8",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00526408",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00526398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526370.md#insn-00526398) · [`005263b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526370.md#insn-005263b8) · [`005263e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526370.md#insn-005263e4)
- 新版 `005263d8`（命令位置の公開資料なし） · `005263f8`（命令位置の公開資料なし） · `00526424`（命令位置の公開資料なし）

~~~diff
- 00526398 ["INT_ADD", "register:40f0:8", ["const:526398:8", "const:4:8"]]
- 00526398 ["CALL", null, ["callee:00c58680:8"]]
+ 005263d8 ["INT_ADD", "register:40f0:8", ["const:5263d8:8", "const:4:8"]]
+ 005263d8 ["CALL", null, ["callee:00c58680:8"]]
- 00526398 bytes bac71c94
+ 005263d8 bytes aac81c94
- 005263b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:940:8"]]
- 005263b8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005263f8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
+ 005263f8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005263b8 bytes 29a144f9
+ 005263f8 bytes 29a146f9
- 005263e4 ["INT_ADD", "register:40f0:8", ["const:5263e4:8", "const:4:8"]]
- 005263e4 ["CALL", null, ["callee:0054d844:8"]]
+ 00526424 ["INT_ADD", "register:40f0:8", ["const:526424:8", "const:4:8"]]
+ 00526424 ["CALL", null, ["callee:0054d844:8"]]
- 005263e4 bytes 089d0094
+ 00526424 bytes 089d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58a4ee2a52d72a99af2ab8b592f01acd"></a>

### [`0052646c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/0052646c.md) → [`005264ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005264ac.md) _ZN5Botan17X509_Cert_OptionsC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md) [`00547b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md) [`00547b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b70.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00526528",
      "incomplete_value": true,
      "site": "00526528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005264e8",
      "incomplete_value": true,
      "site": "005264e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00526530",
      "incomplete_value": true,
      "site": "00526530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005264f0",
      "incomplete_value": true,
      "site": "005264f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00526558",
      "incomplete_value": true,
      "site": "00526558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00526518",
      "incomplete_value": true,
      "site": "00526518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00526514",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ],
    [
      "00526528",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00526530",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00526514",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "00526528",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00526530",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052653c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/0052646c.md#insn-0052653c) · [`00526748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/0052646c.md#insn-00526748) · [`00526784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/0052646c.md#insn-00526784)
- 新版 `0052657c`（命令位置の公開資料なし） · `00526788`（命令位置の公開資料なし） · `005267c4`（命令位置の公開資料なし）

~~~diff
- 0052653c ["INT_ADD", "register:40f0:8", ["const:52653c:8", "const:4:8"]]
- 0052653c ["CALL", null, ["callee:00c58190:8"]]
+ 0052657c ["INT_ADD", "register:40f0:8", ["const:52657c:8", "const:4:8"]]
+ 0052657c ["CALL", null, ["callee:00c58190:8"]]
- 0052653c bytes 15c61c94
+ 0052657c bytes 05c71c94
- 00526748 ["INT_ADD", "register:40f0:8", ["const:526748:8", "const:4:8"]]
- 00526748 ["CALL", null, ["callee:00c580b0:8"]]
+ 00526788 ["INT_ADD", "register:40f0:8", ["const:526788:8", "const:4:8"]]
+ 00526788 ["CALL", null, ["callee:00c580b0:8"]]
- 00526748 bytes 5ac51c94
+ 00526788 bytes 4ac61c94
- 00526784 ["INT_ADD", "register:40f0:8", ["const:526784:8", "const:4:8"]]
- 00526784 ["CALL", null, ["callee:00c57f10:8"]]
+ 005267c4 ["INT_ADD", "register:40f0:8", ["const:5267c4:8", "const:4:8"]]
+ 005267c4 ["CALL", null, ["callee:00c57f10:8"]]
- 00526784 bytes e3c41c94
+ 005267c4 bytes d3c51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a9335302f268d059386ba72d5d8d20f"></a>

### [`00526990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526990.md) → [`005269d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005269d0.md) _ZN5Botan4PKIX11check_chainERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEENS1_6chrono10time_pointINSC_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ae0.md) · 呼出先 29件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`005111e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md) [`00527d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527d7c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)
- 新版 呼出元 1件 [`00c59ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ee0.md) · 呼出先 29件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00511224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511224.md) [`00527dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527dbc.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.42% / 新版 99.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00526f68",
      "incomplete_value": true,
      "site": "00526f6c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4050:8"
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
      "definition_site": "00526f28",
      "incomplete_value": true,
      "site": "00526f2c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4050:8"
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
    "ordinal": 58,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00527bfc",
      "incomplete_value": false,
      "site": "00527c04",
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
            "const:f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00527bbc",
      "incomplete_value": false,
      "site": "00527bc4",
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
            "const:fcf:8"
          ]
        ]
      ]
    },
    "ordinal": 86,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00527c38",
      "incomplete_value": true,
      "site": "00527c44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00527bf8",
      "incomplete_value": true,
      "site": "00527c04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 88,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00526ec4",
      "READ",
      [
        "storage",
        "00ca4fa8",
        null,
        "undefined8"
      ]
    ],
    [
      "0052706c",
      "READ",
      [
        "storage",
        "00ca4fa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00527bfc",
      "PARAM",
      [
        "storage",
        "002b8fcf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00526ec4",
      "READ",
      [
        "storage",
        "00ca53a8",
        null,
        "undefined8"
      ]
    ],
    [
      "0052706c",
      "READ",
      [
        "storage",
        "00ca53a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00527bfc",
      "PARAM",
      [
        "storage",
        "002b900f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00527bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526990.md#insn-00527bc4) · [`00527c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526990.md#insn-00527c04) · [`005269ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526990.md#insn-005269ec)
- 新版 `00527c04`（命令位置の公開資料なし） · `00527c44`（命令位置の公開資料なし） · `00526a2c`（命令位置の公開資料なし）

~~~diff
- 00527bc4 ["INT_ADD", "register:40f0:8", ["const:527bc4:8", "const:4:8"]]
- 00527bc4 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00527c04 ["INT_ADD", "register:40f0:8", ["const:527c04:8", "const:4:8"]]
+ 00527c04 ["CALL", null, ["callee:0043ddd8:8"]]
- 00527bc4 bytes 7558fc97
+ 00527c04 bytes 7558fc97
- 00527c04 ["INT_ADD", "register:40f0:8", ["const:527c04:8", "const:4:8"]]
- 00527c04 ["CALL", null, ["callee:00c57f10:8"]]
+ 00527c44 ["INT_ADD", "register:40f0:8", ["const:527c44:8", "const:4:8"]]
+ 00527c44 ["CALL", null, ["callee:00c57f10:8"]]
- 00527c04 bytes c3bf1c94
+ 00527c44 bytes b3c01c94
- 005269ec ["INT_ADD", "register:40f0:8", ["const:5269ec:8", "const:4:8"]]
- 005269ec ["CALL", null, ["callee:00c59a70:8"]]
+ 00526a2c ["INT_ADD", "register:40f0:8", ["const:526a2c:8", "const:4:8"]]
+ 00526a2c ["CALL", null, ["callee:00c59a70:8"]]
- 005269ec bytes 21cb1c94
+ 00526a2c bytes 11cc1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16c8d6d5c0bf5a6686268350945d3296"></a>

### [`00527de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) → [`00527e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527e28.md) _ZN5Botan4PKIX10check_ocspERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_4OCSP8Respons

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59af0.md) · 呼出先 21件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`005015b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/005015b0.md) [`00527d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527d7c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)
- 新版 呼出元 1件 [`00c59ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ef0.md) · 呼出先 21件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`005015f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005015f0.md) [`00527dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527dbc.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.36% / 新版 99.36%

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
      "definition_site": "00528294",
      "incomplete_value": false,
      "site": "0052829c",
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
            "const:97d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00528254",
      "incomplete_value": false,
      "site": "0052825c",
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
            "const:93d:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005282d0",
      "incomplete_value": true,
      "site": "005282dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00528290",
      "incomplete_value": true,
      "site": "0052829c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005282cc",
      "incomplete_value": false,
      "site": "005282dc",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "0052828c",
      "incomplete_value": false,
      "site": "0052829c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 22,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00528294",
      "PARAM",
      [
        "storage",
        "002ae93d",
        null,
        "string"
      ]
    ],
    [
      "005282cc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "005282d0",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00528294",
      "PARAM",
      [
        "storage",
        "002ae97d",
        null,
        "string"
      ]
    ],
    [
      "005282cc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "005282d0",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052825c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md#insn-0052825c) · [`0052829c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md#insn-0052829c) · [`00527e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md#insn-00527e6c)
- 新版 `0052829c`（命令位置の公開資料なし） · `005282dc`（命令位置の公開資料なし） · `00527eac`（命令位置の公開資料なし）

~~~diff
- 0052825c ["INT_ADD", "register:40f0:8", ["const:52825c:8", "const:4:8"]]
- 0052825c ["CALL", null, ["callee:0043ddd8:8"]]
+ 0052829c ["INT_ADD", "register:40f0:8", ["const:52829c:8", "const:4:8"]]
+ 0052829c ["CALL", null, ["callee:0043ddd8:8"]]
- 0052825c bytes cf56fc97
+ 0052829c bytes cf56fc97
- 0052829c ["INT_ADD", "register:40f0:8", ["const:52829c:8", "const:4:8"]]
- 0052829c ["CALL", null, ["callee:00c57f10:8"]]
+ 005282dc ["INT_ADD", "register:40f0:8", ["const:5282dc:8", "const:4:8"]]
+ 005282dc ["CALL", null, ["callee:00c57f10:8"]]
- 0052829c bytes 1dbe1c94
+ 005282dc bytes 0dbf1c94
- 00527e6c ["INT_ADD", "register:40f0:8", ["const:527e6c:8", "const:4:8"]]
- 00527e6c ["CALL", null, ["callee:00c57e90:8"]]
+ 00527eac ["INT_ADD", "register:40f0:8", ["const:527eac:8", "const:4:8"]]
+ 00527eac ["CALL", null, ["callee:00c57e90:8"]]
- 00527e6c bytes 09bf1c94
+ 00527eac bytes f9bf1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69c7437c80afa88715211b13b3e7d617"></a>

### [`00528364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528364.md) → [`005283a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00528/005283a4.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b00.md) · 呼出先 29件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md)
- 新版 呼出元 1件 [`00c59f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f00.md) · 呼出先 29件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`0053f810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f810.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.72% / 新版 99.72%

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
      "definition_site": "00528dfc",
      "incomplete_value": false,
      "site": "00528e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:277:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00528dbc",
      "incomplete_value": false,
      "site": "00528dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:1aa:8"
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00528e38",
      "incomplete_value": true,
      "site": "00528e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00528df8",
      "incomplete_value": true,
      "site": "00528e04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00528e34",
      "incomplete_value": false,
      "site": "00528e44",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "00528df4",
      "incomplete_value": false,
      "site": "00528e04",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 58,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00528dfc",
      "PARAM",
      [
        "storage",
        "002a41aa",
        null,
        "string"
      ]
    ],
    [
      "00528e34",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00528e38",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00528dfc",
      "PARAM",
      [
        "storage",
        "002a4277",
        null,
        "string"
      ]
    ],
    [
      "00528e34",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00528e38",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00528dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528364.md#insn-00528dc4) · [`00528e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528364.md#insn-00528e04) · [`005283e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528364.md#insn-005283e8)
- 新版 `00528e04`（命令位置の公開資料なし） · `00528e44`（命令位置の公開資料なし） · `00528428`（命令位置の公開資料なし）

~~~diff
- 00528dc4 ["INT_ADD", "register:40f0:8", ["const:528dc4:8", "const:4:8"]]
- 00528dc4 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00528e04 ["INT_ADD", "register:40f0:8", ["const:528e04:8", "const:4:8"]]
+ 00528e04 ["CALL", null, ["callee:0043ddd8:8"]]
- 00528dc4 bytes f553fc97
+ 00528e04 bytes f553fc97
- 00528e04 ["INT_ADD", "register:40f0:8", ["const:528e04:8", "const:4:8"]]
- 00528e04 ["CALL", null, ["callee:00c57f10:8"]]
+ 00528e44 ["INT_ADD", "register:40f0:8", ["const:528e44:8", "const:4:8"]]
+ 00528e44 ["CALL", null, ["callee:00c57f10:8"]]
- 00528e04 bytes 43bb1c94
+ 00528e44 bytes 33bc1c94
- 005283e8 ["INT_ADD", "register:40f0:8", ["const:5283e8:8", "const:4:8"]]
- 005283e8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00528428 ["INT_ADD", "register:40f0:8", ["const:528428:8", "const:4:8"]]
+ 00528428 ["CALL", null, ["callee:00c57e90:8"]]
- 005283e8 bytes aabd1c94
+ 00528428 bytes 9abe1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b699ace0f5d0fa093bd2cd374ccbe1fa"></a>

### [`00528f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528f40.md) → [`00528f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00528/00528f80.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_IPNS_17Certificate_StoreE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b10.md) · 呼出先 16件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00548cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548cdc.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`00c59f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f10.md) · 呼出先 16件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00548d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548d1c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.44% / 新版 96.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005291c8",
      "incomplete_value": false,
      "site": "005291e8",
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
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00529188",
      "incomplete_value": false,
      "site": "005291a8",
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
            "const:68c:8"
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
      "definition_site": "005291d0",
      "incomplete_value": false,
      "site": "005291e8",
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
      "definition_site": "00529190",
      "incomplete_value": false,
      "site": "005291a8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005291d8",
      "incomplete_value": false,
      "site": "005291e8",
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
            "const:18b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00529198",
      "incomplete_value": false,
      "site": "005291a8",
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
            "const:14b:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005291c8",
      "PARAM",
      [
        "storage",
        "002a668c",
        null,
        "string"
      ]
    ],
    [
      "005291d0",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "005291d8",
      "PARAM",
      [
        "storage",
        "002b614b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005291c8",
      "PARAM",
      [
        "storage",
        "002a6768",
        null,
        "string"
      ]
    ],
    [
      "005291d0",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "005291d8",
      "PARAM",
      [
        "storage",
        "002b618b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005291a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528f40.md#insn-005291a8) · [`005291c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528f40.md#insn-005291c4) · [`00529200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528f40.md#insn-00529200)
- 新版 `005291e8`（命令位置の公開資料なし） · `00529204`（命令位置の公開資料なし） · `00529240`（命令位置の公開資料なし）

~~~diff
- 005291a8 ["INT_ADD", "register:40f0:8", ["const:5291a8:8", "const:4:8"]]
- 005291a8 ["CALL", null, ["callee:00c58650:8"]]
+ 005291e8 ["INT_ADD", "register:40f0:8", ["const:5291e8:8", "const:4:8"]]
+ 005291e8 ["CALL", null, ["callee:00c58650:8"]]
- 005291a8 bytes 2abc1c94
+ 005291e8 bytes 1abd1c94
- 005291c4 ["INT_ADD", "register:40f0:8", ["const:5291c4:8", "const:4:8"]]
- 005291c4 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00529204 ["INT_ADD", "register:40f0:8", ["const:529204:8", "const:4:8"]]
+ 00529204 ["CALL", null, ["callee:0043ddd8:8"]]
- 005291c4 bytes f552fc97
+ 00529204 bytes f552fc97
- 00529200 ["INT_ADD", "register:40f0:8", ["const:529200:8", "const:4:8"]]
- 00529200 ["CALL", null, ["callee:00c57f10:8"]]
+ 00529240 ["INT_ADD", "register:40f0:8", ["const:529240:8", "const:4:8"]]
+ 00529240 ["CALL", null, ["callee:00c57f10:8"]]
- 00529200 bytes 44ba1c94
+ 00529240 bytes 34bb1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d1b7c62efa1ee00438f9f58ca80e95d"></a>

### [`005292f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/005292f4.md) → [`00529334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529334.md) _ZN5Botan4PKIX22build_certificate_pathERNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_IPNS_17Certi

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 20件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`005027b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00540890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540890.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`005027f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027f8.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`005408d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.43% / 新版 99.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052959c",
      "incomplete_value": true,
      "site": "0052959c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052955c",
      "incomplete_value": true,
      "site": "0052955c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "00529590",
      "READ",
      [
        "storage",
        "00c9acf8",
        null,
        "pointer"
      ]
    ],
    [
      "0052959c",
      "DATA",
      [
        "storage",
        "00c67398",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00529590",
      "READ",
      [
        "storage",
        "00c9b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "0052959c",
      "DATA",
      [
        "storage",
        "00c67798",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00529338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/005292f4.md#insn-00529338) · [`00529384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/005292f4.md#insn-00529384) · [`00529398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/005292f4.md#insn-00529398)
- 新版 `00529378`（命令位置の公開資料なし） · `005293c4`（命令位置の公開資料なし） · `005293d8`（命令位置の公開資料なし）

~~~diff
- 00529338 ["INT_ADD", "register:40f0:8", ["const:529338:8", "const:4:8"]]
- 00529338 ["CALL", null, ["callee:00c599f0:8"]]
+ 00529378 ["INT_ADD", "register:40f0:8", ["const:529378:8", "const:4:8"]]
+ 00529378 ["CALL", null, ["callee:00c599f0:8"]]
- 00529338 bytes aec01c94
+ 00529378 bytes 9ec11c94
- 00529384 ["INT_ADD", "register:40f0:8", ["const:529384:8", "const:4:8"]]
- 00529384 ["CALL", null, ["callee:00c53cd0:8"]]
+ 005293c4 ["INT_ADD", "register:40f0:8", ["const:5293c4:8", "const:4:8"]]
+ 005293c4 ["CALL", null, ["callee:00c53cd0:8"]]
- 00529384 bytes 4ba91c94
+ 005293c4 bytes 43aa1c94
- 00529398 ["INT_ADD", "register:40f0:8", ["const:529398:8", "const:4:8"]]
- 00529398 ["CALL", null, ["callee:00548598:8"]]
+ 005293d8 ["INT_ADD", "register:40f0:8", ["const:5293d8:8", "const:4:8"]]
+ 005293d8 ["CALL", null, ["callee:00548598:8"]]
- 00529398 bytes 707c0094
+ 005293d8 bytes 707c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-145111179292a88675b2e80dc01b2d1a"></a>

### [`0052b0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b0e8.md) → [`0052b128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b128.md) _ZN5Botan4PKIX23merge_revocation_statusERNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b20.md) · 呼出先 8件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c59f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f20.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.29% / 新版 99.29%

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
      "definition_site": "0052b538",
      "incomplete_value": false,
      "site": "0052b540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:297:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052b4f8",
      "incomplete_value": false,
      "site": "0052b500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:1ca:8"
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
      "definition_site": "0052b574",
      "incomplete_value": true,
      "site": "0052b580",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0052b534",
      "incomplete_value": true,
      "site": "0052b540",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
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
      "definition_site": "0052b570",
      "incomplete_value": false,
      "site": "0052b580",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "0052b530",
      "incomplete_value": false,
      "site": "0052b540",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0052b538",
      "PARAM",
      [
        "storage",
        "002a41ca",
        null,
        "string"
      ]
    ],
    [
      "0052b570",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "0052b574",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052b538",
      "PARAM",
      [
        "storage",
        "002a4297",
        null,
        "string"
      ]
    ],
    [
      "0052b570",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0052b574",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052b500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b0e8.md#insn-0052b500) · [`0052b540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b0e8.md#insn-0052b540) · [`0052b190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b0e8.md#insn-0052b190)
- 新版 `0052b540`（命令位置の公開資料なし） · `0052b580`（命令位置の公開資料なし） · `0052b1d0`（命令位置の公開資料なし）

~~~diff
- 0052b500 ["INT_ADD", "register:40f0:8", ["const:52b500:8", "const:4:8"]]
- 0052b500 ["CALL", null, ["callee:0043ddd8:8"]]
+ 0052b540 ["INT_ADD", "register:40f0:8", ["const:52b540:8", "const:4:8"]]
+ 0052b540 ["CALL", null, ["callee:0043ddd8:8"]]
- 0052b500 bytes 264afc97
+ 0052b540 bytes 264afc97
- 0052b540 ["INT_ADD", "register:40f0:8", ["const:52b540:8", "const:4:8"]]
- 0052b540 ["CALL", null, ["callee:00c57f10:8"]]
+ 0052b580 ["INT_ADD", "register:40f0:8", ["const:52b580:8", "const:4:8"]]
+ 0052b580 ["CALL", null, ["callee:00c57f10:8"]]
- 0052b540 bytes 74b11c94
+ 0052b580 bytes 64b21c94
- 0052b190 ["INT_ADD", "register:40f0:8", ["const:52b190:8", "const:4:8"]]
- 0052b190 ["CALL", null, ["callee:0043bba4:8"]]
+ 0052b1d0 ["INT_ADD", "register:40f0:8", ["const:52b1d0:8", "const:4:8"]]
+ 0052b1d0 ["CALL", null, ["callee:0043bba4:8"]]
- 0052b190 bytes 7542fc97
+ 0052b1d0 bytes 7542fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0366646ca26b18311f9b23d31a08f607"></a>

### [`0052b594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b594.md) → [`0052b5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b5d4.md) _ZN5Botan4PKIX14overall_statusERKNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS9_EEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b30.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c59f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f30.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

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
      "definition_site": "0052b69c",
      "incomplete_value": false,
      "site": "0052b6a4",
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
    "old": {
      "definition_site": "0052b65c",
      "incomplete_value": false,
      "site": "0052b664",
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
            "const:c4d:8"
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
      "definition_site": "0052b6d8",
      "incomplete_value": true,
      "site": "0052b6e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0052b698",
      "incomplete_value": true,
      "site": "0052b6a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
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
      "definition_site": "0052b6d4",
      "incomplete_value": false,
      "site": "0052b6e4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "0052b694",
      "incomplete_value": false,
      "site": "0052b6a4",
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
      "0052b69c",
      "PARAM",
      [
        "storage",
        "002b2c4d",
        null,
        "string"
      ]
    ],
    [
      "0052b6d4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "0052b6d8",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052b69c",
      "PARAM",
      [
        "storage",
        "002b2c8d",
        null,
        "string"
      ]
    ],
    [
      "0052b6d4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0052b6d8",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052b664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b594.md#insn-0052b664) · [`0052b6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b594.md#insn-0052b6a4) · [`0052b650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b594.md#insn-0052b650)
- 新版 `0052b6a4`（命令位置の公開資料なし） · `0052b6e4`（命令位置の公開資料なし） · `0052b690`（命令位置の公開資料なし）

~~~diff
- 0052b664 ["INT_ADD", "register:40f0:8", ["const:52b664:8", "const:4:8"]]
- 0052b664 ["CALL", null, ["callee:0043ddd8:8"]]
+ 0052b6a4 ["INT_ADD", "register:40f0:8", ["const:52b6a4:8", "const:4:8"]]
+ 0052b6a4 ["CALL", null, ["callee:0043ddd8:8"]]
- 0052b664 bytes cd49fc97
+ 0052b6a4 bytes cd49fc97
- 0052b6a4 ["INT_ADD", "register:40f0:8", ["const:52b6a4:8", "const:4:8"]]
- 0052b6a4 ["CALL", null, ["callee:00c57f10:8"]]
+ 0052b6e4 ["INT_ADD", "register:40f0:8", ["const:52b6e4:8", "const:4:8"]]
+ 0052b6e4 ["CALL", null, ["callee:00c57f10:8"]]
- 0052b6a4 bytes 1bb11c94
+ 0052b6e4 bytes 0bb21c94
- 0052b650 ["INT_ADD", "register:40f0:8", ["const:52b650:8", "const:4:8"]]
- 0052b650 ["CALL", null, ["callee:00c57ef0:8"]]
+ 0052b690 ["INT_ADD", "register:40f0:8", ["const:52b690:8", "const:4:8"]]
+ 0052b690 ["CALL", null, ["callee:00c57ef0:8"]]
- 0052b650 bytes 28b11c94
+ 0052b690 bytes 18b21c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec40d3395163dc980e5675ede432ddfe"></a>

### [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) → [`0052b738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md) _ZN5Botan18x509_path_validateERKNSt6__ndk16vectorINS_16X509_CertificateENS0_9allocatorIS2_EEEERKNS_28Path_Validation_RestrictionsERKNS1_IPNS

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b40.md) · 呼出先 28件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) [`0052c204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c204.md) [`0052c314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c314.md)
- 新版 呼出元 1件 [`00c59f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f40.md) · 呼出先 28件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00529db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529db8.md) [`0052c244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md) [`0052c354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.03% / 新版 99.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052b7b0",
      "incomplete_value": true,
      "site": "0052b7b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052b770",
      "incomplete_value": true,
      "site": "0052b774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "0052b7d4",
      "incomplete_value": true,
      "site": "0052b7d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052b794",
      "incomplete_value": true,
      "site": "0052b798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052b920",
      "value": [
        "leaf",
        "ram:529db8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052b8e0",
      "value": [
        "leaf",
        "ram:529d78:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0052b7a8",
      "READ",
      [
        "storage",
        "00c9acd8",
        null,
        "pointer"
      ]
    ],
    [
      "0052b7b4",
      "DATA",
      [
        "storage",
        "00c6a340",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "0052b7d0",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052b7a8",
      "READ",
      [
        "storage",
        "00c9b0d8",
        null,
        "pointer"
      ]
    ],
    [
      "0052b7b4",
      "DATA",
      [
        "storage",
        "00c6a740",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "0052b7d0",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052b758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md#insn-0052b758) · [`0052b8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md#insn-0052b8e0) · [`0052c064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md#insn-0052c064)
- 新版 `0052b798`（命令位置の公開資料なし） · `0052b920`（命令位置の公開資料なし） · `0052c0a4`（命令位置の公開資料なし）

~~~diff
- 0052b758 ["INT_ADD", "register:40f0:8", ["const:52b758:8", "const:4:8"]]
- 0052b758 ["CALL", null, ["callee:00c57e90:8"]]
+ 0052b798 ["INT_ADD", "register:40f0:8", ["const:52b798:8", "const:4:8"]]
+ 0052b798 ["CALL", null, ["callee:00c57e90:8"]]
- 0052b758 bytes ceb01c94
+ 0052b798 bytes beb11c94
- 0052b8e0 ["INT_ADD", "register:40f0:8", ["const:52b8e0:8", "const:4:8"]]
- 0052b8e0 ["CALL", null, ["ram:529d78:8"]]
+ 0052b920 ["INT_ADD", "register:40f0:8", ["const:52b920:8", "const:4:8"]]
+ 0052b920 ["CALL", null, ["ram:529db8:8"]]
- 0052b8e0 bytes 26f9ff97
+ 0052b920 bytes 26f9ff97
- 0052c064 ["INT_ADD", "register:40f0:8", ["const:52c064:8", "const:4:8"]]
- 0052c064 ["CALL", null, ["callee:0043ddd8:8"]]
+ 0052c0a4 ["INT_ADD", "register:40f0:8", ["const:52c0a4:8", "const:4:8"]]
+ 0052c0a4 ["CALL", null, ["callee:0043ddd8:8"]]
- 0052c064 bytes 4d47fc97
+ 0052c0a4 bytes 4d47fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-359a00cafe21b3404920347963de7c65"></a>

### [`0052d0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d0d4.md) → [`0052d114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d114.md) _ZNK5Botan22Path_Validation_Result10trust_rootEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052d184",
      "incomplete_value": false,
      "site": "0052d18c",
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
            "const:e36:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052d144",
      "incomplete_value": false,
      "site": "0052d14c",
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
            "const:df6:8"
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
      "definition_site": "0052d1c0",
      "incomplete_value": true,
      "site": "0052d1cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052d180",
      "incomplete_value": true,
      "site": "0052d18c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052d1bc",
      "incomplete_value": false,
      "site": "0052d1cc",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "0052d17c",
      "incomplete_value": false,
      "site": "0052d18c",
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
      "0052d184",
      "PARAM",
      [
        "storage",
        "002bedf6",
        null,
        "string"
      ]
    ],
    [
      "0052d1bc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "0052d1c0",
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
      "0052d184",
      "PARAM",
      [
        "storage",
        "002bee36",
        null,
        "string"
      ]
    ],
    [
      "0052d1bc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0052d1c0",
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

- 旧版 [`0052d14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d0d4.md#insn-0052d14c) · [`0052d18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d0d4.md#insn-0052d18c) · [`0052d1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d0d4.md#insn-0052d1b0)
- 新版 `0052d18c`（命令位置の公開資料なし） · `0052d1cc`（命令位置の公開資料なし） · `0052d1f0`（命令位置の公開資料なし）

~~~diff
- 0052d14c ["INT_ADD", "register:40f0:8", ["const:52d14c:8", "const:4:8"]]
- 0052d14c ["CALL", null, ["callee:0043ddd8:8"]]
+ 0052d18c ["INT_ADD", "register:40f0:8", ["const:52d18c:8", "const:4:8"]]
+ 0052d18c ["CALL", null, ["callee:0043ddd8:8"]]
- 0052d14c bytes 1343fc97
+ 0052d18c bytes 1343fc97
- 0052d18c ["INT_ADD", "register:40f0:8", ["const:52d18c:8", "const:4:8"]]
- 0052d18c ["CALL", null, ["callee:00c57f10:8"]]
+ 0052d1cc ["INT_ADD", "register:40f0:8", ["const:52d1cc:8", "const:4:8"]]
+ 0052d1cc ["CALL", null, ["callee:00c57f10:8"]]
- 0052d18c bytes 61aa1c94
+ 0052d1cc bytes 51ab1c94
- 0052d1b0 ["INT_ADD", "register:40f0:8", ["const:52d1b0:8", "const:4:8"]]
- 0052d1b0 ["CALL", null, ["callee:0043ddd8:8"]]
+ 0052d1f0 ["INT_ADD", "register:40f0:8", ["const:52d1f0:8", "const:4:8"]]
+ 0052d1f0 ["CALL", null, ["callee:0043ddd8:8"]]
- 0052d1b0 bytes fa42fc97
+ 0052d1f0 bytes fa42fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39307f9a987a5a907f8469af59741811"></a>

### [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) → [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) _ZN5Botan4X50923create_self_signed_certERKNS_17X509_Cert_OptionsERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9al

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 27件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`004c0a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0a38.md) [`00500ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500ecc.md) [`00505294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505294.md) [`00510020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`004c0a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0a78.md) [`00500f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500f0c.md) [`005052d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/005052d4.md) [`00510060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.96% / 新版 94.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052d564",
      "incomplete_value": true,
      "site": "0052d564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052d524",
      "incomplete_value": true,
      "site": "0052d524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0052d5b0",
      "incomplete_value": true,
      "site": "0052d5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052d570",
      "incomplete_value": true,
      "site": "0052d570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052d718",
      "incomplete_value": true,
      "site": "0052d720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052d6d8",
      "incomplete_value": true,
      "site": "0052d6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "0052d54c",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "0052d564",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0052d59c",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052d54c",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0052d564",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0052d59c",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052d5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md#insn-0052d5d4) · [`0052d608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md#insn-0052d608) · [`0052d648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md#insn-0052d648)
- 新版 `0052d614`（命令位置の公開資料なし） · `0052d648`（命令位置の公開資料なし） · `0052d688`（命令位置の公開資料なし）

~~~diff
- 0052d5d4 ["INT_ADD", "register:40f0:8", ["const:52d5d4:8", "const:4:8"]]
- 0052d5d4 ["CALL", null, ["callee:0052dc0c:8"]]
+ 0052d614 ["INT_ADD", "register:40f0:8", ["const:52d614:8", "const:4:8"]]
+ 0052d614 ["CALL", null, ["callee:0052dc0c:8"]]
- 0052d5d4 bytes 7e010094
+ 0052d614 bytes 7e010094
- 0052d608 ["INT_ADD", "register:40f0:8", ["const:52d608:8", "const:4:8"]]
- 0052d608 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0052d648 ["INT_ADD", "register:40f0:8", ["const:52d648:8", "const:4:8"]]
+ 0052d648 ["CALL", null, ["callee:00c57eb0:8"]]
- 0052d608 bytes 2aa91c94
+ 0052d648 bytes 1aaa1c94
- 0052d648 ["INT_ADD", "register:40f0:8", ["const:52d648:8", "const:4:8"]]
- 0052d648 ["CALL", null, ["ram:52dddc:8"]]
+ 0052d688 ["INT_ADD", "register:40f0:8", ["const:52d688:8", "const:4:8"]]
+ 0052d688 ["CALL", null, ["ram:52de1c:8"]]
- 0052d648 bytes e5010094
+ 0052d688 bytes e5010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11efa11211ab5bdda7b9b608beafaaf7"></a>

### [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) → [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) _ZN5Botan4X50915create_cert_reqERKNS_17X509_Cert_OptionsERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9allocatorI

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 42件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`004c0a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0a38.md) [`00500ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500ecc.md) [`00505294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505294.md)
- 新版 呼出元 0件  · 呼出先 42件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`004c0a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0a78.md) [`00500f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500f0c.md) [`005052d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/005052d4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.58% / 新版 93.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 6件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e388",
      "incomplete_value": true,
      "site": "0052e388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052e348",
      "incomplete_value": true,
      "site": "0052e348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e3d4",
      "incomplete_value": true,
      "site": "0052e3d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052e394",
      "incomplete_value": true,
      "site": "0052e394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e538",
      "incomplete_value": true,
      "site": "0052e540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052e4f8",
      "incomplete_value": true,
      "site": "0052e500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "0052e370",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "0052e388",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0052e3c0",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052e370",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0052e388",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0052e3c0",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052e3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md#insn-0052e3f8) · [`0052e42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md#insn-0052e42c) · [`0052e46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md#insn-0052e46c)
- 新版 `0052e438`（命令位置の公開資料なし） · `0052e46c`（命令位置の公開資料なし） · `0052e4ac`（命令位置の公開資料なし）

~~~diff
- 0052e3f8 ["INT_ADD", "register:40f0:8", ["const:52e3f8:8", "const:4:8"]]
- 0052e3f8 ["CALL", null, ["callee:0052dc0c:8"]]
+ 0052e438 ["INT_ADD", "register:40f0:8", ["const:52e438:8", "const:4:8"]]
+ 0052e438 ["CALL", null, ["callee:0052dc0c:8"]]
- 0052e3f8 bytes f5fdff97
+ 0052e438 bytes f5fdff97
- 0052e42c ["INT_ADD", "register:40f0:8", ["const:52e42c:8", "const:4:8"]]
- 0052e42c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0052e46c ["INT_ADD", "register:40f0:8", ["const:52e46c:8", "const:4:8"]]
+ 0052e46c ["CALL", null, ["callee:00c57eb0:8"]]
- 0052e42c bytes a1a51c94
+ 0052e46c bytes 91a61c94
- 0052e46c ["INT_ADD", "register:40f0:8", ["const:52e46c:8", "const:4:8"]]
- 0052e46c ["CALL", null, ["ram:52dddc:8"]]
+ 0052e4ac ["INT_ADD", "register:40f0:8", ["const:52e4ac:8", "const:4:8"]]
+ 0052e4ac ["CALL", null, ["ram:52de1c:8"]]
- 0052e46c bytes 5cfeff97
+ 0052e4ac bytes 5cfeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c15055bb0f21c1b5ddb46441a037e69"></a>

### [`0052ef80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052ef80.md) → [`0052efc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052efc0.md) FUN_0052efc0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f074.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`0052f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f0b4.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052eff8",
      "incomplete_value": true,
      "site": "0052eff8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052efb8",
      "incomplete_value": true,
      "site": "0052efb8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f024",
      "incomplete_value": true,
      "site": "0052f024",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052efe4",
      "incomplete_value": true,
      "site": "0052efe4",
      "value": [
        "LOAD",
        "8",
        [
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f050",
      "incomplete_value": true,
      "site": "0052f050",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f010",
      "incomplete_value": true,
      "site": "0052f010",
      "value": [
        "LOAD",
        "8",
        [
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
      "0052efe8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0052f014",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0052f040",
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
      "0052efe8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052f014",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052f040",
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

- 旧版 [`0052efb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052ef80.md#insn-0052efb8) · [`0052efe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052ef80.md#insn-0052efe4) · [`0052f010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052ef80.md#insn-0052f010)
- 新版 `0052eff8`（命令位置の公開資料なし） · `0052f024`（命令位置の公開資料なし） · `0052f050`（命令位置の公開資料なし）

~~~diff
- 0052efb8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052efb8 ["INT_ADD", "register:40f0:8", ["const:52efb8:8", "const:4:8"]]
- 0052efb8 ["CALLIND", null, ["register:0:8"]]
+ 0052eff8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052eff8 ["INT_ADD", "register:40f0:8", ["const:52eff8:8", "const:4:8"]]
+ 0052eff8 ["CALLIND", null, ["register:0:8"]]
- 0052efb8 bytes 20013fd6
+ 0052eff8 bytes 20013fd6
- 0052efe4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052efe4 ["INT_ADD", "register:40f0:8", ["const:52efe4:8", "const:4:8"]]
- 0052efe4 ["CALLIND", null, ["register:0:8"]]
+ 0052f024 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f024 ["INT_ADD", "register:40f0:8", ["const:52f024:8", "const:4:8"]]
+ 0052f024 ["CALLIND", null, ["register:0:8"]]
- 0052efe4 bytes 20013fd6
+ 0052f024 bytes 20013fd6
- 0052f010 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f010 ["INT_ADD", "register:40f0:8", ["const:52f010:8", "const:4:8"]]
- 0052f010 ["CALLIND", null, ["register:0:8"]]
+ 0052f050 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f050 ["INT_ADD", "register:40f0:8", ["const:52f050:8", "const:4:8"]]
+ 0052f050 ["CALLIND", null, ["register:0:8"]]
- 0052f010 bytes 20013fd6
+ 0052f050 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-554e3d79a0ca2ecab0a2080e5e045f5a"></a>

### [`0052f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f228.md) → [`0052f268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f268.md) FUN_0052f268

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
      "definition_site": "0052f284",
      "incomplete_value": true,
      "site": "0052f288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052f244",
      "incomplete_value": true,
      "site": "0052f248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "0052f280",
      "READ",
      [
        "storage",
        "00c9aa10",
        null,
        "pointer"
      ]
    ],
    [
      "0052f288",
      "DATA",
      [
        "storage",
        "00c676d0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0052f280",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0052f288",
      "DATA",
      [
        "storage",
        "00c67ad0",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f228.md#insn-0052f234) · [`0052f240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f228.md#insn-0052f240)
- 新版 `0052f274`（命令位置の公開資料なし） · `0052f280`（命令位置の公開資料なし）

~~~diff
- 0052f234 ["INT_ADD", "register:40f0:8", ["const:52f234:8", "const:4:8"]]
- 0052f234 ["CALL", null, ["callee:00c57e90:8"]]
+ 0052f274 ["INT_ADD", "register:40f0:8", ["const:52f274:8", "const:4:8"]]
+ 0052f274 ["CALL", null, ["callee:00c57e90:8"]]
- 0052f234 bytes 17a21c94
+ 0052f274 bytes 07a31c94
- 0052f240 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a10:8"]]
- 0052f240 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f280 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 0052f280 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f240 bytes 080945f9
+ 0052f280 bytes 080947f9
~~~


<a id="compare-cbbc530338d952860bf780e180443494"></a>

### [`0052f26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f26c.md) → [`0052f2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f2ac.md) FUN_0052f2ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052f360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f360.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`0052f3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f3a0.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f2e4",
      "incomplete_value": true,
      "site": "0052f2e4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f2a4",
      "incomplete_value": true,
      "site": "0052f2a4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f310",
      "incomplete_value": true,
      "site": "0052f310",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f2d0",
      "incomplete_value": true,
      "site": "0052f2d0",
      "value": [
        "LOAD",
        "8",
        [
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f33c",
      "incomplete_value": true,
      "site": "0052f33c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f2fc",
      "incomplete_value": true,
      "site": "0052f2fc",
      "value": [
        "LOAD",
        "8",
        [
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
      "0052f2d4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0052f300",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0052f32c",
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
      "0052f2d4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052f300",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052f32c",
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

- 旧版 [`0052f2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f26c.md#insn-0052f2a4) · [`0052f2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f26c.md#insn-0052f2d0) · [`0052f2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f26c.md#insn-0052f2fc)
- 新版 `0052f2e4`（命令位置の公開資料なし） · `0052f310`（命令位置の公開資料なし） · `0052f33c`（命令位置の公開資料なし）

~~~diff
- 0052f2a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f2a4 ["INT_ADD", "register:40f0:8", ["const:52f2a4:8", "const:4:8"]]
- 0052f2a4 ["CALLIND", null, ["register:0:8"]]
+ 0052f2e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f2e4 ["INT_ADD", "register:40f0:8", ["const:52f2e4:8", "const:4:8"]]
+ 0052f2e4 ["CALLIND", null, ["register:0:8"]]
- 0052f2a4 bytes 20013fd6
+ 0052f2e4 bytes 20013fd6
- 0052f2d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f2d0 ["INT_ADD", "register:40f0:8", ["const:52f2d0:8", "const:4:8"]]
- 0052f2d0 ["CALLIND", null, ["register:0:8"]]
+ 0052f310 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f310 ["INT_ADD", "register:40f0:8", ["const:52f310:8", "const:4:8"]]
+ 0052f310 ["CALLIND", null, ["register:0:8"]]
- 0052f2d0 bytes 20013fd6
+ 0052f310 bytes 20013fd6
- 0052f2fc ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f2fc ["INT_ADD", "register:40f0:8", ["const:52f2fc:8", "const:4:8"]]
- 0052f2fc ["CALLIND", null, ["register:0:8"]]
+ 0052f33c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f33c ["INT_ADD", "register:40f0:8", ["const:52f33c:8", "const:4:8"]]
+ 0052f33c ["CALLIND", null, ["register:0:8"]]
- 0052f2fc bytes 20013fd6
+ 0052f33c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c3f0deeba7a22a72b1ff89d79a7df1a"></a>

### [`0052f514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f514.md) → [`0052f554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f554.md) FUN_0052f554

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
      "definition_site": "0052f570",
      "incomplete_value": true,
      "site": "0052f574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052f530",
      "incomplete_value": true,
      "site": "0052f534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "0052f56c",
      "READ",
      [
        "storage",
        "00c9aa18",
        null,
        "pointer"
      ]
    ],
    [
      "0052f574",
      "DATA",
      [
        "storage",
        "00c677a8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0052f56c",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0052f574",
      "DATA",
      [
        "storage",
        "00c67ba8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f514.md#insn-0052f520) · [`0052f52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f514.md#insn-0052f52c)
- 新版 `0052f560`（命令位置の公開資料なし） · `0052f56c`（命令位置の公開資料なし）

~~~diff
- 0052f520 ["INT_ADD", "register:40f0:8", ["const:52f520:8", "const:4:8"]]
- 0052f520 ["CALL", null, ["callee:00c57e90:8"]]
+ 0052f560 ["INT_ADD", "register:40f0:8", ["const:52f560:8", "const:4:8"]]
+ 0052f560 ["CALL", null, ["callee:00c57e90:8"]]
- 0052f520 bytes 5ca11c94
+ 0052f560 bytes 4ca21c94
- 0052f52c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a18:8"]]
- 0052f52c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f56c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e18:8"]]
+ 0052f56c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f52c bytes 080d45f9
+ 0052f56c bytes 080d47f9
~~~


<a id="compare-9035c2fc884dff6360fca4d550859959"></a>

### [`0052f558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f558.md) → [`0052f598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f598.md) FUN_0052f598

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052f64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f64c.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`0052f68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f68c.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f5d0",
      "incomplete_value": true,
      "site": "0052f5d0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f590",
      "incomplete_value": true,
      "site": "0052f590",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f5fc",
      "incomplete_value": true,
      "site": "0052f5fc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f5bc",
      "incomplete_value": true,
      "site": "0052f5bc",
      "value": [
        "LOAD",
        "8",
        [
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f628",
      "incomplete_value": true,
      "site": "0052f628",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f5e8",
      "incomplete_value": true,
      "site": "0052f5e8",
      "value": [
        "LOAD",
        "8",
        [
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
      "0052f5c0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0052f5ec",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0052f618",
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
      "0052f5c0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052f5ec",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052f618",
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

- 旧版 [`0052f590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f558.md#insn-0052f590) · [`0052f5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f558.md#insn-0052f5bc) · [`0052f5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f558.md#insn-0052f5e8)
- 新版 `0052f5d0`（命令位置の公開資料なし） · `0052f5fc`（命令位置の公開資料なし） · `0052f628`（命令位置の公開資料なし）

~~~diff
- 0052f590 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f590 ["INT_ADD", "register:40f0:8", ["const:52f590:8", "const:4:8"]]
- 0052f590 ["CALLIND", null, ["register:0:8"]]
+ 0052f5d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f5d0 ["INT_ADD", "register:40f0:8", ["const:52f5d0:8", "const:4:8"]]
+ 0052f5d0 ["CALLIND", null, ["register:0:8"]]
- 0052f590 bytes 20013fd6
+ 0052f5d0 bytes 20013fd6
- 0052f5bc ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f5bc ["INT_ADD", "register:40f0:8", ["const:52f5bc:8", "const:4:8"]]
- 0052f5bc ["CALLIND", null, ["register:0:8"]]
+ 0052f5fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f5fc ["INT_ADD", "register:40f0:8", ["const:52f5fc:8", "const:4:8"]]
+ 0052f5fc ["CALLIND", null, ["register:0:8"]]
- 0052f5bc bytes 20013fd6
+ 0052f5fc bytes 20013fd6
- 0052f5e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f5e8 ["INT_ADD", "register:40f0:8", ["const:52f5e8:8", "const:4:8"]]
- 0052f5e8 ["CALLIND", null, ["register:0:8"]]
+ 0052f628 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f628 ["INT_ADD", "register:40f0:8", ["const:52f628:8", "const:4:8"]]
+ 0052f628 ["CALLIND", null, ["register:0:8"]]
- 0052f5e8 bytes 20013fd6
+ 0052f628 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3da3b41073c01eaad47d6fec73d02eee"></a>

### [`0052f800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f800.md) → [`0052f840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f840.md) FUN_0052f840

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
      "definition_site": "0052f85c",
      "incomplete_value": true,
      "site": "0052f860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052f81c",
      "incomplete_value": true,
      "site": "0052f820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "0052f858",
      "READ",
      [
        "storage",
        "00c9aa20",
        null,
        "pointer"
      ]
    ],
    [
      "0052f860",
      "DATA",
      [
        "storage",
        "00c67858",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0052f858",
      "READ",
      [
        "storage",
        "00c9ae20",
        null,
        "pointer"
      ]
    ],
    [
      "0052f860",
      "DATA",
      [
        "storage",
        "00c67c58",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f800.md#insn-0052f80c) · [`0052f818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f800.md#insn-0052f818)
- 新版 `0052f84c`（命令位置の公開資料なし） · `0052f858`（命令位置の公開資料なし）

~~~diff
- 0052f80c ["INT_ADD", "register:40f0:8", ["const:52f80c:8", "const:4:8"]]
- 0052f80c ["CALL", null, ["callee:00c57e90:8"]]
+ 0052f84c ["INT_ADD", "register:40f0:8", ["const:52f84c:8", "const:4:8"]]
+ 0052f84c ["CALL", null, ["callee:00c57e90:8"]]
- 0052f80c bytes a1a01c94
+ 0052f84c bytes 91a11c94
- 0052f818 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a20:8"]]
- 0052f818 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f858 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e20:8"]]
+ 0052f858 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f818 bytes 081145f9
+ 0052f858 bytes 081147f9
~~~


<a id="compare-2a6ed4d740bc250716f5649b5bfe8657"></a>

### [`0052f85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f85c.md) → [`0052f89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f89c.md) FUN_0052f89c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f8d0",
      "incomplete_value": true,
      "site": "0052f8d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052f890",
      "incomplete_value": true,
      "site": "0052f890",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0052f8c0",
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
      "0052f8c0",
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

- 旧版 [`0052f890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f85c.md#insn-0052f890) · [`0052f880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f85c.md#insn-0052f880) · [`0052f898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f85c.md#insn-0052f898)
- 新版 `0052f8d0`（命令位置の公開資料なし） · `0052f8c0`（命令位置の公開資料なし） · `0052f8d8`（命令位置の公開資料なし）

~~~diff
- 0052f890 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f890 ["INT_ADD", "register:40f0:8", ["const:52f890:8", "const:4:8"]]
- 0052f890 ["CALLIND", null, ["register:0:8"]]
+ 0052f8d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f8d0 ["INT_ADD", "register:40f0:8", ["const:52f8d0:8", "const:4:8"]]
+ 0052f8d0 ["CALLIND", null, ["register:0:8"]]
- 0052f890 bytes 20013fd6
+ 0052f8d0 bytes 20013fd6
- 0052f880 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:338:8"]]
- 0052f880 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f8c0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:738:8"]]
+ 0052f8c0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f880 bytes 299d41f9
+ 0052f8c0 bytes 299d43f9
- 0052f898 ["INT_ADD", "register:40f0:8", ["const:52f898:8", "const:4:8"]]
- 0052f898 ["CALL", null, ["callee:00c58660:8"]]
+ 0052f8d8 ["INT_ADD", "register:40f0:8", ["const:52f8d8:8", "const:4:8"]]
+ 0052f8d8 ["CALL", null, ["callee:00c58660:8"]]
- 0052f898 bytes 72a21c94
+ 0052f8d8 bytes 62a31c94
~~~


<a id="compare-e61b547acdec4e9af096b68d0783df63"></a>

### [`0052f8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f8e0.md) → [`0052f920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f920.md) FUN_0052f920

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

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
      "definition_site": "0052f93c",
      "incomplete_value": true,
      "site": "0052f940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052f8fc",
      "incomplete_value": true,
      "site": "0052f900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052f964",
      "incomplete_value": true,
      "site": "0052f964",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052f924",
      "incomplete_value": true,
      "site": "0052f924",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0052f934",
      "READ",
      [
        "storage",
        "00c9aa30",
        null,
        "pointer"
      ]
    ],
    [
      "0052f940",
      "DATA",
      [
        "storage",
        "00c66020",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052f954",
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
      "0052f934",
      "READ",
      [
        "storage",
        "00c9ae30",
        null,
        "pointer"
      ]
    ],
    [
      "0052f940",
      "DATA",
      [
        "storage",
        "00c66420",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052f954",
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

- 旧版 [`0052f924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f8e0.md#insn-0052f924) · [`0052f8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f8e0.md#insn-0052f8f4) · [`0052f914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f8e0.md#insn-0052f914)
- 新版 `0052f964`（命令位置の公開資料なし） · `0052f934`（命令位置の公開資料なし） · `0052f954`（命令位置の公開資料なし）

~~~diff
- 0052f924 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f924 ["INT_ADD", "register:40f0:8", ["const:52f924:8", "const:4:8"]]
- 0052f924 ["CALLIND", null, ["register:0:8"]]
+ 0052f964 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f964 ["INT_ADD", "register:40f0:8", ["const:52f964:8", "const:4:8"]]
+ 0052f964 ["CALLIND", null, ["register:0:8"]]
- 0052f924 bytes 20013fd6
+ 0052f964 bytes 20013fd6
- 0052f8f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a30:8"]]
- 0052f8f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f934 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e30:8"]]
+ 0052f934 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f8f4 bytes 081945f9
+ 0052f934 bytes 081947f9
- 0052f914 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:338:8"]]
- 0052f914 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f954 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:738:8"]]
+ 0052f954 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f914 bytes 299d41f9
+ 0052f954 bytes 299d43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2bd29d6246c03054fcb1a3fce9eaeb8"></a>

### [`0052f974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f974.md) → [`0052f9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f9b4.md) FUN_0052f9b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

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
      "definition_site": "0052f9d0",
      "incomplete_value": true,
      "site": "0052f9d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052f990",
      "incomplete_value": true,
      "site": "0052f994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052f9f8",
      "incomplete_value": true,
      "site": "0052f9f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052f9b8",
      "incomplete_value": true,
      "site": "0052f9b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0052f9c8",
      "READ",
      [
        "storage",
        "00c9aa30",
        null,
        "pointer"
      ]
    ],
    [
      "0052f9d4",
      "DATA",
      [
        "storage",
        "00c66020",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052f9e8",
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
      "0052f9c8",
      "READ",
      [
        "storage",
        "00c9ae30",
        null,
        "pointer"
      ]
    ],
    [
      "0052f9d4",
      "DATA",
      [
        "storage",
        "00c66420",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052f9e8",
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

- 旧版 [`0052f9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f974.md#insn-0052f9b8) · [`0052f988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f974.md#insn-0052f988) · [`0052f9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f974.md#insn-0052f9a8)
- 新版 `0052f9f8`（命令位置の公開資料なし） · `0052f9c8`（命令位置の公開資料なし） · `0052f9e8`（命令位置の公開資料なし）

~~~diff
- 0052f9b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f9b8 ["INT_ADD", "register:40f0:8", ["const:52f9b8:8", "const:4:8"]]
- 0052f9b8 ["CALLIND", null, ["register:0:8"]]
+ 0052f9f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f9f8 ["INT_ADD", "register:40f0:8", ["const:52f9f8:8", "const:4:8"]]
+ 0052f9f8 ["CALLIND", null, ["register:0:8"]]
- 0052f9b8 bytes 20013fd6
+ 0052f9f8 bytes 20013fd6
- 0052f988 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a30:8"]]
- 0052f988 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f9c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e30:8"]]
+ 0052f9c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f988 bytes 081945f9
+ 0052f9c8 bytes 081947f9
- 0052f9a8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:338:8"]]
- 0052f9a8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f9e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:738:8"]]
+ 0052f9e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f9a8 bytes 299d41f9
+ 0052f9e8 bytes 299d43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad92d1356c456f704d363538315d07ca"></a>

### [`0052fa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fa0c.md) → [`0052fa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fa4c.md) FUN_0052fa4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

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
      "definition_site": "0052fa68",
      "incomplete_value": true,
      "site": "0052fa6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fa28",
      "incomplete_value": true,
      "site": "0052fa2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fa90",
      "incomplete_value": true,
      "site": "0052fa90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052fa50",
      "incomplete_value": true,
      "site": "0052fa50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0052fa60",
      "READ",
      [
        "storage",
        "00c9aa30",
        null,
        "pointer"
      ]
    ],
    [
      "0052fa6c",
      "DATA",
      [
        "storage",
        "00c66020",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fa80",
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
      "0052fa60",
      "READ",
      [
        "storage",
        "00c9ae30",
        null,
        "pointer"
      ]
    ],
    [
      "0052fa6c",
      "DATA",
      [
        "storage",
        "00c66420",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fa80",
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

- 旧版 [`0052fa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fa0c.md#insn-0052fa50) · [`0052fa20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fa0c.md#insn-0052fa20) · [`0052fa40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fa0c.md#insn-0052fa40)
- 新版 `0052fa90`（命令位置の公開資料なし） · `0052fa60`（命令位置の公開資料なし） · `0052fa80`（命令位置の公開資料なし）

~~~diff
- 0052fa50 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fa50 ["INT_ADD", "register:40f0:8", ["const:52fa50:8", "const:4:8"]]
- 0052fa50 ["CALLIND", null, ["register:0:8"]]
+ 0052fa90 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fa90 ["INT_ADD", "register:40f0:8", ["const:52fa90:8", "const:4:8"]]
+ 0052fa90 ["CALLIND", null, ["register:0:8"]]
- 0052fa50 bytes 20013fd6
+ 0052fa90 bytes 20013fd6
- 0052fa20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a30:8"]]
- 0052fa20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052fa60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e30:8"]]
+ 0052fa60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052fa20 bytes 081945f9
+ 0052fa60 bytes 081947f9
- 0052fa40 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:338:8"]]
- 0052fa40 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052fa80 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:738:8"]]
+ 0052fa80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0052fa40 bytes 299d41f9
+ 0052fa80 bytes 299d43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b0bb00dba8776669cb63b1290972f32"></a>

### [`0052faa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052faa0.md) → [`0052fae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fae0.md) FUN_0052fae0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fb04",
      "incomplete_value": true,
      "site": "0052fb08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fac4",
      "incomplete_value": true,
      "site": "0052fac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fb40",
      "incomplete_value": true,
      "site": "0052fb44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fb00",
      "incomplete_value": true,
      "site": "0052fb04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fb28",
      "incomplete_value": true,
      "site": "0052fb28",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052fae8",
      "incomplete_value": true,
      "site": "0052fae8",
      "value": [
        "LOAD",
        "8",
        [
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
      "0052fafc",
      "READ",
      [
        "storage",
        "00c9ab98",
        null,
        "pointer"
      ]
    ],
    [
      "0052fb08",
      "DATA",
      [
        "storage",
        "00c67b20",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fb18",
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
      "0052fafc",
      "READ",
      [
        "storage",
        "00c9af98",
        null,
        "pointer"
      ]
    ],
    [
      "0052fb08",
      "DATA",
      [
        "storage",
        "00c67f20",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fb18",
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

- 旧版 [`0052fae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052faa0.md#insn-0052fae8) · [`0052fb24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052faa0.md#insn-0052fb24) · [`0052fb44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052faa0.md#insn-0052fb44)
- 新版 `0052fb28`（命令位置の公開資料なし） · `0052fb64`（命令位置の公開資料なし） · `0052fb84`（命令位置の公開資料なし）

~~~diff
- 0052fae8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fae8 ["INT_ADD", "register:40f0:8", ["const:52fae8:8", "const:4:8"]]
- 0052fae8 ["CALLIND", null, ["register:0:8"]]
+ 0052fb28 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fb28 ["INT_ADD", "register:40f0:8", ["const:52fb28:8", "const:4:8"]]
+ 0052fb28 ["CALLIND", null, ["register:0:8"]]
- 0052fae8 bytes 20013fd6
+ 0052fb28 bytes 20013fd6
- 0052fb24 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fb24 ["INT_ADD", "register:40f0:8", ["const:52fb24:8", "const:4:8"]]
- 0052fb24 ["CALLIND", null, ["register:0:8"]]
+ 0052fb64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fb64 ["INT_ADD", "register:40f0:8", ["const:52fb64:8", "const:4:8"]]
+ 0052fb64 ["CALLIND", null, ["register:0:8"]]
- 0052fb24 bytes 20013fd6
+ 0052fb64 bytes 20013fd6
- 0052fb44 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052fb44 ["INT_ADD", "register:40f0:8", ["const:52fb44:8", "const:4:8"]]
- 0052fb44 ["CALLIND", null, ["register:0:8"]]
+ 0052fb84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052fb84 ["INT_ADD", "register:40f0:8", ["const:52fb84:8", "const:4:8"]]
+ 0052fb84 ["CALLIND", null, ["register:0:8"]]
- 0052fb44 bytes 00013fd6
+ 0052fb84 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27790bd9a48b7804dab223941c94b388"></a>

### [`0052fb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fb7c.md) → [`0052fbbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fbbc.md) FUN_0052fbbc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.27% / 新版 87.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fbe0",
      "incomplete_value": true,
      "site": "0052fbe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fba0",
      "incomplete_value": true,
      "site": "0052fba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fc1c",
      "incomplete_value": true,
      "site": "0052fc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fbdc",
      "incomplete_value": true,
      "site": "0052fbe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fc04",
      "incomplete_value": true,
      "site": "0052fc04",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052fbc4",
      "incomplete_value": true,
      "site": "0052fbc4",
      "value": [
        "LOAD",
        "8",
        [
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
      "0052fbd8",
      "READ",
      [
        "storage",
        "00c9ab98",
        null,
        "pointer"
      ]
    ],
    [
      "0052fbe4",
      "DATA",
      [
        "storage",
        "00c67b20",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fbf4",
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
      "0052fbd8",
      "READ",
      [
        "storage",
        "00c9af98",
        null,
        "pointer"
      ]
    ],
    [
      "0052fbe4",
      "DATA",
      [
        "storage",
        "00c67f20",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fbf4",
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

- 旧版 [`0052fbc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fb7c.md#insn-0052fbc4) · [`0052fc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fb7c.md#insn-0052fc00) · [`0052fc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fb7c.md#insn-0052fc20)
- 新版 `0052fc04`（命令位置の公開資料なし） · `0052fc40`（命令位置の公開資料なし） · `0052fc60`（命令位置の公開資料なし）

~~~diff
- 0052fbc4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fbc4 ["INT_ADD", "register:40f0:8", ["const:52fbc4:8", "const:4:8"]]
- 0052fbc4 ["CALLIND", null, ["register:0:8"]]
+ 0052fc04 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fc04 ["INT_ADD", "register:40f0:8", ["const:52fc04:8", "const:4:8"]]
+ 0052fc04 ["CALLIND", null, ["register:0:8"]]
- 0052fbc4 bytes 20013fd6
+ 0052fc04 bytes 20013fd6
- 0052fc00 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fc00 ["INT_ADD", "register:40f0:8", ["const:52fc00:8", "const:4:8"]]
- 0052fc00 ["CALLIND", null, ["register:0:8"]]
+ 0052fc40 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fc40 ["INT_ADD", "register:40f0:8", ["const:52fc40:8", "const:4:8"]]
+ 0052fc40 ["CALLIND", null, ["register:0:8"]]
- 0052fc00 bytes 20013fd6
+ 0052fc40 bytes 20013fd6
- 0052fc20 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052fc20 ["INT_ADD", "register:40f0:8", ["const:52fc20:8", "const:4:8"]]
- 0052fc20 ["CALLIND", null, ["register:0:8"]]
+ 0052fc60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052fc60 ["INT_ADD", "register:40f0:8", ["const:52fc60:8", "const:4:8"]]
+ 0052fc60 ["CALLIND", null, ["register:0:8"]]
- 0052fc20 bytes 00013fd6
+ 0052fc60 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19adeeb74c391a195958f719347463b8"></a>

### [`0052fc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fc60.md) → [`0052fca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fca0.md) FUN_0052fca0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fcc4",
      "incomplete_value": true,
      "site": "0052fcc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fc84",
      "incomplete_value": true,
      "site": "0052fc88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fd00",
      "incomplete_value": true,
      "site": "0052fd04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fcc0",
      "incomplete_value": true,
      "site": "0052fcc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fce8",
      "incomplete_value": true,
      "site": "0052fce8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052fca8",
      "incomplete_value": true,
      "site": "0052fca8",
      "value": [
        "LOAD",
        "8",
        [
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
      "0052fcbc",
      "READ",
      [
        "storage",
        "00c9ab98",
        null,
        "pointer"
      ]
    ],
    [
      "0052fcc8",
      "DATA",
      [
        "storage",
        "00c67b20",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fcd8",
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
      "0052fcbc",
      "READ",
      [
        "storage",
        "00c9af98",
        null,
        "pointer"
      ]
    ],
    [
      "0052fcc8",
      "DATA",
      [
        "storage",
        "00c67f20",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fcd8",
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

- 旧版 [`0052fca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fc60.md#insn-0052fca8) · [`0052fce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fc60.md#insn-0052fce4) · [`0052fd04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fc60.md#insn-0052fd04)
- 新版 `0052fce8`（命令位置の公開資料なし） · `0052fd24`（命令位置の公開資料なし） · `0052fd44`（命令位置の公開資料なし）

~~~diff
- 0052fca8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fca8 ["INT_ADD", "register:40f0:8", ["const:52fca8:8", "const:4:8"]]
- 0052fca8 ["CALLIND", null, ["register:0:8"]]
+ 0052fce8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fce8 ["INT_ADD", "register:40f0:8", ["const:52fce8:8", "const:4:8"]]
+ 0052fce8 ["CALLIND", null, ["register:0:8"]]
- 0052fca8 bytes 20013fd6
+ 0052fce8 bytes 20013fd6
- 0052fce4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fce4 ["INT_ADD", "register:40f0:8", ["const:52fce4:8", "const:4:8"]]
- 0052fce4 ["CALLIND", null, ["register:0:8"]]
+ 0052fd24 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fd24 ["INT_ADD", "register:40f0:8", ["const:52fd24:8", "const:4:8"]]
+ 0052fd24 ["CALLIND", null, ["register:0:8"]]
- 0052fce4 bytes 20013fd6
+ 0052fd24 bytes 20013fd6
- 0052fd04 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052fd04 ["INT_ADD", "register:40f0:8", ["const:52fd04:8", "const:4:8"]]
- 0052fd04 ["CALLIND", null, ["register:0:8"]]
+ 0052fd44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052fd44 ["INT_ADD", "register:40f0:8", ["const:52fd44:8", "const:4:8"]]
+ 0052fd44 ["CALLIND", null, ["register:0:8"]]
- 0052fd04 bytes 00013fd6
+ 0052fd44 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-953c38a3bc2f2c2c03b388321ccd863e"></a>

### [`0052fe34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fe34.md) → [`0052fe74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fe74.md) FUN_0052fe74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fe94",
      "incomplete_value": true,
      "site": "0052fe98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052fe54",
      "incomplete_value": true,
      "site": "0052fe58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0052fe88",
      "READ",
      [
        "storage",
        "00c9aa48",
        null,
        "pointer"
      ]
    ],
    [
      "0052fe98",
      "DATA",
      [
        "storage",
        "00c660d8",
        null,
        "undefined1[160]"
      ]
    ]
  ],
  "added": [
    [
      "0052fe88",
      "READ",
      [
        "storage",
        "00c9ae48",
        null,
        "pointer"
      ]
    ],
    [
      "0052fe98",
      "DATA",
      [
        "storage",
        "00c664d8",
        null,
        "undefined1[160]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052fe48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fe34.md#insn-0052fe48) · [`0052fe68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fe34.md#insn-0052fe68) · [`0052fe80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fe34.md#insn-0052fe80)
- 新版 `0052fe88`（命令位置の公開資料なし） · `0052fea8`（命令位置の公開資料なし） · `0052fec0`（命令位置の公開資料なし）

~~~diff
- 0052fe48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a48:8"]]
- 0052fe48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052fe88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e48:8"]]
+ 0052fe88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052fe48 bytes 082545f9
+ 0052fe88 bytes 082547f9
- 0052fe68 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052fe68 ["INT_ADD", "register:40f0:8", ["const:52fe68:8", "const:4:8"]]
- 0052fe68 ["CALLIND", null, ["register:0:8"]]
+ 0052fea8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052fea8 ["INT_ADD", "register:40f0:8", ["const:52fea8:8", "const:4:8"]]
+ 0052fea8 ["CALLIND", null, ["register:0:8"]]
- 0052fe68 bytes 00013fd6
+ 0052fea8 bytes 00013fd6
- 0052fe80 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052fe80 ["INT_ADD", "register:40f0:8", ["const:52fe80:8", "const:4:8"]]
- 0052fe80 ["CALLIND", null, ["register:0:8"]]
+ 0052fec0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052fec0 ["INT_ADD", "register:40f0:8", ["const:52fec0:8", "const:4:8"]]
+ 0052fec0 ["CALLIND", null, ["register:0:8"]]
- 0052fe80 bytes 00013fd6
+ 0052fec0 bytes 00013fd6
~~~


<a id="compare-c0dcde026200f74519aeda332d9c67e5"></a>

### [`0052fe94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fe94.md) → [`0052fed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fed4.md) FUN_0052fed4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fef4",
      "incomplete_value": true,
      "site": "0052fef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052feb4",
      "incomplete_value": true,
      "site": "0052feb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0052fee8",
      "READ",
      [
        "storage",
        "00c9aa48",
        null,
        "pointer"
      ]
    ],
    [
      "0052fef8",
      "DATA",
      [
        "storage",
        "00c660d8",
        null,
        "undefined1[160]"
      ]
    ]
  ],
  "added": [
    [
      "0052fee8",
      "READ",
      [
        "storage",
        "00c9ae48",
        null,
        "pointer"
      ]
    ],
    [
      "0052fef8",
      "DATA",
      [
        "storage",
        "00c664d8",
        null,
        "undefined1[160]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052fea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fe94.md#insn-0052fea8) · [`0052fec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fe94.md#insn-0052fec8)
- 新版 `0052fee8`（命令位置の公開資料なし） · `0052ff08`（命令位置の公開資料なし）

~~~diff
- 0052fea8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a48:8"]]
- 0052fea8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052fee8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e48:8"]]
+ 0052fee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052fea8 bytes 082545f9
+ 0052fee8 bytes 082547f9
- 0052fec8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052fec8 ["INT_ADD", "register:40f0:8", ["const:52fec8:8", "const:4:8"]]
- 0052fec8 ["CALLIND", null, ["register:0:8"]]
+ 0052ff08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052ff08 ["INT_ADD", "register:40f0:8", ["const:52ff08:8", "const:4:8"]]
+ 0052ff08 ["CALLIND", null, ["register:0:8"]]
- 0052fec8 bytes 00013fd6
+ 0052ff08 bytes 00013fd6
~~~


<a id="compare-f68cbf94049fce5f04000da968b4dbcf"></a>

### [`0052fef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fef8.md) → [`0052ff38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052ff38.md) FUN_0052ff38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052ff58",
      "incomplete_value": true,
      "site": "0052ff5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052ff18",
      "incomplete_value": true,
      "site": "0052ff1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0052ff4c",
      "READ",
      [
        "storage",
        "00c9aa48",
        null,
        "pointer"
      ]
    ],
    [
      "0052ff5c",
      "DATA",
      [
        "storage",
        "00c660d8",
        null,
        "undefined1[160]"
      ]
    ]
  ],
  "added": [
    [
      "0052ff4c",
      "READ",
      [
        "storage",
        "00c9ae48",
        null,
        "pointer"
      ]
    ],
    [
      "0052ff5c",
      "DATA",
      [
        "storage",
        "00c664d8",
        null,
        "undefined1[160]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052ff0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fef8.md#insn-0052ff0c) · [`0052ff2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fef8.md#insn-0052ff2c) · [`0052ff44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fef8.md#insn-0052ff44)
- 新版 `0052ff4c`（命令位置の公開資料なし） · `0052ff6c`（命令位置の公開資料なし） · `0052ff84`（命令位置の公開資料なし）

~~~diff
- 0052ff0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a48:8"]]
- 0052ff0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052ff4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e48:8"]]
+ 0052ff4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052ff0c bytes 082545f9
+ 0052ff4c bytes 082547f9
- 0052ff2c ["COPY", "register:0:8", ["register:4040:8"]]
- 0052ff2c ["INT_ADD", "register:40f0:8", ["const:52ff2c:8", "const:4:8"]]
- 0052ff2c ["CALLIND", null, ["register:0:8"]]
+ 0052ff6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052ff6c ["INT_ADD", "register:40f0:8", ["const:52ff6c:8", "const:4:8"]]
+ 0052ff6c ["CALLIND", null, ["register:0:8"]]
- 0052ff2c bytes 00013fd6
+ 0052ff6c bytes 00013fd6
- 0052ff44 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052ff44 ["INT_ADD", "register:40f0:8", ["const:52ff44:8", "const:4:8"]]
- 0052ff44 ["CALLIND", null, ["register:0:8"]]
+ 0052ff84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052ff84 ["INT_ADD", "register:40f0:8", ["const:52ff84:8", "const:4:8"]]
+ 0052ff84 ["CALLIND", null, ["register:0:8"]]
- 0052ff44 bytes 00013fd6
+ 0052ff84 bytes 00013fd6
~~~


<a id="compare-d9b0451d958efac0ca9e22c5c13b7a9d"></a>

### [`005302a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005302a8.md) → [`005302e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005302e8.md) FUN_005302e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0053037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053037c.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`005303bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005303bc.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530364",
      "incomplete_value": true,
      "site": "00530368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00530324",
      "incomplete_value": true,
      "site": "00530328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00530320",
      "incomplete_value": true,
      "site": "00530320",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005302e0",
      "incomplete_value": true,
      "site": "005302e0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0053034c",
      "incomplete_value": true,
      "site": "0053034c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0053030c",
      "incomplete_value": true,
      "site": "0053030c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00530310",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0053033c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0053035c",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00530310",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0053033c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0053035c",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005302e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005302a8.md#insn-005302e0) · [`005302e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005302a8.md#insn-005302e8) · [`0053030c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005302a8.md#insn-0053030c)
- 新版 `00530320`（命令位置の公開資料なし） · `00530328`（命令位置の公開資料なし） · `0053034c`（命令位置の公開資料なし）

~~~diff
- 005302e0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005302e0 ["INT_ADD", "register:40f0:8", ["const:5302e0:8", "const:4:8"]]
- 005302e0 ["CALLIND", null, ["register:0:8"]]
+ 00530320 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530320 ["INT_ADD", "register:40f0:8", ["const:530320:8", "const:4:8"]]
+ 00530320 ["CALLIND", null, ["register:0:8"]]
- 005302e0 bytes 20013fd6
+ 00530320 bytes 20013fd6
- 005302e8 ["INT_ADD", "register:40f0:8", ["const:5302e8:8", "const:4:8"]]
- 005302e8 ["CALL", null, ["callee:00c58660:8"]]
+ 00530328 ["INT_ADD", "register:40f0:8", ["const:530328:8", "const:4:8"]]
+ 00530328 ["CALL", null, ["callee:00c58660:8"]]
- 005302e8 bytes de9f1c94
+ 00530328 bytes cea01c94
- 0053030c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053030c ["INT_ADD", "register:40f0:8", ["const:53030c:8", "const:4:8"]]
- 0053030c ["CALLIND", null, ["register:0:8"]]
+ 0053034c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053034c ["INT_ADD", "register:40f0:8", ["const:53034c:8", "const:4:8"]]
+ 0053034c ["CALLIND", null, ["register:0:8"]]
- 0053030c bytes 20013fd6
+ 0053034c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27971fda38ba5f771d7b30bdde1fb20d"></a>

### [`00530438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530438.md) → [`00530478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530478.md) FUN_00530478

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005304bc",
      "incomplete_value": true,
      "site": "005304bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0053047c",
      "incomplete_value": true,
      "site": "0053047c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005304b4",
      "READ",
      [
        "storage",
        "00c9abc8",
        null,
        "pointer"
      ]
    ],
    [
      "005304bc",
      "DATA",
      [
        "storage",
        "00c68130",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "005304b4",
      "READ",
      [
        "storage",
        "00c9afc8",
        null,
        "pointer"
      ]
    ],
    [
      "005304bc",
      "DATA",
      [
        "storage",
        "00c68530",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053044c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530438.md#insn-0053044c) · [`00530464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530438.md#insn-00530464) · [`00530474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530438.md#insn-00530474)
- 新版 `0053048c`（命令位置の公開資料なし） · `005304a4`（命令位置の公開資料なし） · `005304b4`（命令位置の公開資料なし）

~~~diff
- 0053044c ["INT_ADD", "register:40f0:8", ["const:53044c:8", "const:4:8"]]
- 0053044c ["CALL", null, ["callee:00c57e90:8"]]
+ 0053048c ["INT_ADD", "register:40f0:8", ["const:53048c:8", "const:4:8"]]
+ 0053048c ["CALL", null, ["callee:00c57e90:8"]]
- 0053044c bytes 919d1c94
+ 0053048c bytes 819e1c94
- 00530464 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530464 ["INT_ADD", "register:40f0:8", ["const:530464:8", "const:4:8"]]
- 00530464 ["CALLIND", null, ["register:0:8"]]
+ 005304a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005304a4 ["INT_ADD", "register:40f0:8", ["const:5304a4:8", "const:4:8"]]
+ 005304a4 ["CALLIND", null, ["register:0:8"]]
- 00530464 bytes 20013fd6
+ 005304a4 bytes 20013fd6
- 00530474 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc8:8"]]
- 00530474 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005304b4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fc8:8"]]
+ 005304b4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00530474 bytes 29e545f9
+ 005304b4 bytes 29e547f9
~~~


<a id="compare-847cdaa3da0deec80561bdfc2271a650"></a>

### [`005304a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005304a0.md) → [`005304e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005304e0.md) FUN_005304e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00530518",
      "incomplete_value": false,
      "site": "00530524",
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
            "const:c7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005304d8",
      "incomplete_value": false,
      "site": "005304e4",
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
            "const:bad:8"
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
      "definition_site": "00530544",
      "incomplete_value": false,
      "site": "0053054c",
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
      "definition_site": "00530504",
      "incomplete_value": false,
      "site": "0053050c",
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
      "00530518",
      "PARAM",
      [
        "storage",
        "002a8bad",
        null,
        "string"
      ]
    ],
    [
      "00530544",
      "PARAM",
      [
        "storage",
        "002ab265",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00530518",
      "PARAM",
      [
        "storage",
        "002a8c7a",
        null,
        "string"
      ]
    ],
    [
      "00530544",
      "PARAM",
      [
        "storage",
        "002ab332",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005304e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005304a0.md#insn-005304e4) · [`0053050c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005304a0.md#insn-0053050c) · [`005304d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005304a0.md#insn-005304d0)
- 新版 `00530524`（命令位置の公開資料なし） · `0053054c`（命令位置の公開資料なし） · `00530510`（命令位置の公開資料なし）

~~~diff
- 005304e4 ["INT_ADD", "register:40f0:8", ["const:5304e4:8", "const:4:8"]]
- 005304e4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00530524 ["INT_ADD", "register:40f0:8", ["const:530524:8", "const:4:8"]]
+ 00530524 ["CALL", null, ["callee:00c57f60:8"]]
- 005304e4 bytes 9f9d1c94
+ 00530524 bytes 8f9e1c94
- 0053050c ["INT_ADD", "register:40f0:8", ["const:53050c:8", "const:4:8"]]
- 0053050c ["CALL", null, ["callee:00c57f70:8"]]
+ 0053054c ["INT_ADD", "register:40f0:8", ["const:53054c:8", "const:4:8"]]
+ 0053054c ["CALL", null, ["callee:00c57f70:8"]]
- 0053050c bytes 999d1c94
+ 0053054c bytes 899e1c94
- 005304d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005304d0 ["INT_ADD", "register:40f0:8", ["const:5304d0:8", "const:4:8"]]
- 005304d0 ["CALLIND", null, ["register:0:8"]]
+ 00530510 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530510 ["INT_ADD", "register:40f0:8", ["const:530510:8", "const:4:8"]]
+ 00530510 ["CALLIND", null, ["register:0:8"]]
- 005304d0 bytes 20013fd6
+ 00530510 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d7a4f92e9468a80eea3a05be8eb66cf"></a>

### [`00530624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530624.md) → [`00530664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530664.md) FUN_00530664

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

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
      "definition_site": "00530688",
      "incomplete_value": true,
      "site": "0053068c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00530648",
      "incomplete_value": true,
      "site": "0053064c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "005306ac",
      "incomplete_value": true,
      "site": "005306ac",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0053066c",
      "incomplete_value": true,
      "site": "0053066c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005306d8",
      "incomplete_value": true,
      "site": "005306d8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530698",
      "incomplete_value": true,
      "site": "00530698",
      "value": [
        "LOAD",
        "8",
        [
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
      "00530680",
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ],
    [
      "0053068c",
      "DATA",
      [
        "storage",
        "00c66ca8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "0053069c",
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
      "00530680",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "0053068c",
      "DATA",
      [
        "storage",
        "00c670a8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "0053069c",
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

- 旧版 [`0053066c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530624.md#insn-0053066c) · [`00530698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530624.md#insn-00530698) · [`00530640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530624.md#insn-00530640)
- 新版 `005306ac`（命令位置の公開資料なし） · `005306d8`（命令位置の公開資料なし） · `00530680`（命令位置の公開資料なし）

~~~diff
- 0053066c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053066c ["INT_ADD", "register:40f0:8", ["const:53066c:8", "const:4:8"]]
- 0053066c ["CALLIND", null, ["register:0:8"]]
+ 005306ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 005306ac ["INT_ADD", "register:40f0:8", ["const:5306ac:8", "const:4:8"]]
+ 005306ac ["CALLIND", null, ["register:0:8"]]
- 0053066c bytes 20013fd6
+ 005306ac bytes 20013fd6
- 00530698 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530698 ["INT_ADD", "register:40f0:8", ["const:530698:8", "const:4:8"]]
- 00530698 ["CALLIND", null, ["register:0:8"]]
+ 005306d8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005306d8 ["INT_ADD", "register:40f0:8", ["const:5306d8:8", "const:4:8"]]
+ 005306d8 ["CALLIND", null, ["register:0:8"]]
- 00530698 bytes 20013fd6
+ 005306d8 bytes 20013fd6
- 00530640 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd8:8"]]
- 00530640 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530680 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd8:8"]]
+ 00530680 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00530640 bytes 08ed45f9
+ 00530680 bytes 08ed47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1aff9996779ce81d3d81e9639be4d94"></a>

### [`005306c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005306c8.md) → [`00530708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530708.md) FUN_00530708

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053072c",
      "incomplete_value": true,
      "site": "00530730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "005306ec",
      "incomplete_value": true,
      "site": "005306f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00530750",
      "incomplete_value": true,
      "site": "00530750",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530710",
      "incomplete_value": true,
      "site": "00530710",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0053077c",
      "incomplete_value": true,
      "site": "0053077c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0053073c",
      "incomplete_value": true,
      "site": "0053073c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00530724",
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ],
    [
      "00530730",
      "DATA",
      [
        "storage",
        "00c66ca8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00530740",
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
      "00530724",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "00530730",
      "DATA",
      [
        "storage",
        "00c670a8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00530740",
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

- 旧版 [`00530710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005306c8.md#insn-00530710) · [`0053073c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005306c8.md#insn-0053073c) · [`005306e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005306c8.md#insn-005306e4)
- 新版 `00530750`（命令位置の公開資料なし） · `0053077c`（命令位置の公開資料なし） · `00530724`（命令位置の公開資料なし）

~~~diff
- 00530710 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530710 ["INT_ADD", "register:40f0:8", ["const:530710:8", "const:4:8"]]
- 00530710 ["CALLIND", null, ["register:0:8"]]
+ 00530750 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530750 ["INT_ADD", "register:40f0:8", ["const:530750:8", "const:4:8"]]
+ 00530750 ["CALLIND", null, ["register:0:8"]]
- 00530710 bytes 20013fd6
+ 00530750 bytes 20013fd6
- 0053073c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053073c ["INT_ADD", "register:40f0:8", ["const:53073c:8", "const:4:8"]]
- 0053073c ["CALLIND", null, ["register:0:8"]]
+ 0053077c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053077c ["INT_ADD", "register:40f0:8", ["const:53077c:8", "const:4:8"]]
+ 0053077c ["CALLIND", null, ["register:0:8"]]
- 0053073c bytes 20013fd6
+ 0053077c bytes 20013fd6
- 005306e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd8:8"]]
- 005306e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530724 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd8:8"]]
+ 00530724 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005306e4 bytes 08ed45f9
+ 00530724 bytes 08ed47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-566ed98aa4958a7666f9fd35d93f40ec"></a>

### [`0053078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md) → [`005307cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005307cc.md) FUN_005307cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`004c7be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7be4.md) [`004c7c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7c20.md) [`00530878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530878.md) [`00530904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530904.md) [`0053090c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053090c.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 6件 [`004c7c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7c24.md) [`004c7c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7c60.md) [`005308b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005308b8.md) [`00530944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530944.md) [`0053094c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/0053094c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.98% / 新版 92.98%

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
      "definition_site": "00530804",
      "incomplete_value": true,
      "site": "00530808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005307c4",
      "incomplete_value": true,
      "site": "005307c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00530838",
      "incomplete_value": true,
      "site": "00530838",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "005307f8",
      "incomplete_value": true,
      "site": "005307f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0053088c",
      "incomplete_value": true,
      "site": "0053088c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0053084c",
      "incomplete_value": true,
      "site": "0053084c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "005307f8",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "00530808",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00530828",
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
      "005307f8",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "00530808",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00530828",
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

- 旧版 [`005307b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md#insn-005307b8) · [`005307f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md#insn-005307f8) · [`0053084c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md#insn-0053084c)
- 新版 `005307f8`（命令位置の公開資料なし） · `00530838`（命令位置の公開資料なし） · `0053088c`（命令位置の公開資料なし）

~~~diff
- 005307b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 005307b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005307f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 005307f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005307b8 bytes 083945f9
+ 005307f8 bytes 083947f9
- 005307f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005307f8 ["INT_ADD", "register:40f0:8", ["const:5307f8:8", "const:4:8"]]
- 005307f8 ["CALLIND", null, ["register:0:8"]]
+ 00530838 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530838 ["INT_ADD", "register:40f0:8", ["const:530838:8", "const:4:8"]]
+ 00530838 ["CALLIND", null, ["register:0:8"]]
- 005307f8 bytes 20013fd6
+ 00530838 bytes 20013fd6
- 0053084c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053084c ["INT_ADD", "register:40f0:8", ["const:53084c:8", "const:4:8"]]
- 0053084c ["CALLIND", null, ["register:0:8"]]
+ 0053088c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053088c ["INT_ADD", "register:40f0:8", ["const:53088c:8", "const:4:8"]]
+ 0053088c ["CALLIND", null, ["register:0:8"]]
- 0053084c bytes 20013fd6
+ 0053088c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8b2783cb91feb17bc777d992f9848a6"></a>

### [`00530934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530934.md) → [`00530974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530974.md) FUN_00530974

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00530a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a08.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00530a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530a48.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005309f0",
      "incomplete_value": true,
      "site": "005309f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005309b0",
      "incomplete_value": true,
      "site": "005309b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005309ac",
      "incomplete_value": true,
      "site": "005309ac",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0053096c",
      "incomplete_value": true,
      "site": "0053096c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005309d8",
      "incomplete_value": true,
      "site": "005309d8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530998",
      "incomplete_value": true,
      "site": "00530998",
      "value": [
        "LOAD",
        "8",
        [
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
      "0053099c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "005309c8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "005309e8",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053099c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "005309c8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "005309e8",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053096c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530934.md#insn-0053096c) · [`00530974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530934.md#insn-00530974) · [`00530998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530934.md#insn-00530998)
- 新版 `005309ac`（命令位置の公開資料なし） · `005309b4`（命令位置の公開資料なし） · `005309d8`（命令位置の公開資料なし）

~~~diff
- 0053096c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053096c ["INT_ADD", "register:40f0:8", ["const:53096c:8", "const:4:8"]]
- 0053096c ["CALLIND", null, ["register:0:8"]]
+ 005309ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 005309ac ["INT_ADD", "register:40f0:8", ["const:5309ac:8", "const:4:8"]]
+ 005309ac ["CALLIND", null, ["register:0:8"]]
- 0053096c bytes 20013fd6
+ 005309ac bytes 20013fd6
- 00530974 ["INT_ADD", "register:40f0:8", ["const:530974:8", "const:4:8"]]
- 00530974 ["CALL", null, ["callee:00c58660:8"]]
+ 005309b4 ["INT_ADD", "register:40f0:8", ["const:5309b4:8", "const:4:8"]]
+ 005309b4 ["CALL", null, ["callee:00c58660:8"]]
- 00530974 bytes 3b9e1c94
+ 005309b4 bytes 2b9f1c94
- 00530998 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530998 ["INT_ADD", "register:40f0:8", ["const:530998:8", "const:4:8"]]
- 00530998 ["CALLIND", null, ["register:0:8"]]
+ 005309d8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005309d8 ["INT_ADD", "register:40f0:8", ["const:5309d8:8", "const:4:8"]]
+ 005309d8 ["CALLIND", null, ["register:0:8"]]
- 00530998 bytes 20013fd6
+ 005309d8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9db714f03ad011b29ce72a5371592a2"></a>

### [`00530a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a94.md) → [`00530ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530ad4.md) FUN_00530ad4

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
      "definition_site": "00530b24",
      "incomplete_value": true,
      "site": "00530b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00530ae4",
      "incomplete_value": true,
      "site": "00530ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00530b0c",
      "incomplete_value": true,
      "site": "00530b0c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530acc",
      "incomplete_value": true,
      "site": "00530acc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530b48",
      "incomplete_value": true,
      "site": "00530b48",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530b08",
      "incomplete_value": true,
      "site": "00530b08",
      "value": [
        "LOAD",
        "8",
        [
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
      "00530afc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00530b1c",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "00530b28",
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
      "00530afc",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00530b1c",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "00530b28",
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

- 旧版 [`00530acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a94.md#insn-00530acc) · [`00530b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a94.md#insn-00530b08) · [`00530abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a94.md#insn-00530abc)
- 新版 `00530b0c`（命令位置の公開資料なし） · `00530b48`（命令位置の公開資料なし） · `00530afc`（命令位置の公開資料なし）

~~~diff
- 00530acc ["COPY", "register:0:8", ["register:4048:8"]]
- 00530acc ["INT_ADD", "register:40f0:8", ["const:530acc:8", "const:4:8"]]
- 00530acc ["CALLIND", null, ["register:0:8"]]
+ 00530b0c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530b0c ["INT_ADD", "register:40f0:8", ["const:530b0c:8", "const:4:8"]]
+ 00530b0c ["CALLIND", null, ["register:0:8"]]
- 00530acc bytes 20013fd6
+ 00530b0c bytes 20013fd6
- 00530b08 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530b08 ["INT_ADD", "register:40f0:8", ["const:530b08:8", "const:4:8"]]
- 00530b08 ["CALLIND", null, ["register:0:8"]]
+ 00530b48 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530b48 ["INT_ADD", "register:40f0:8", ["const:530b48:8", "const:4:8"]]
+ 00530b48 ["CALLIND", null, ["register:0:8"]]
- 00530b08 bytes 20013fd6
+ 00530b48 bytes 20013fd6
- 00530abc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00530abc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530afc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
+ 00530afc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00530abc bytes a99e41f9
+ 00530afc bytes a99e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

