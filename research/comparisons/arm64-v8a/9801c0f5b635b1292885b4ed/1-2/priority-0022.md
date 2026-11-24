# v16.0.0 → v16.0.1 · 最優先の変更候補 (22)

[一覧の目次](README.md)

<a id="compare-91369077fbf635a96cbcdf99a15b3012"></a>

### [`005a7d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7d94.md) → [`005a7dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7dd4.md) FUN_005a7dd4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a7e38",
      "incomplete_value": false,
      "site": "005a7e3c",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7df8",
      "incomplete_value": false,
      "site": "005a7dfc",
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
            "const:600:8"
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
      "005a7e3c",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a7e3c",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7d94.md#insn-005a7ddc) · [`005a7dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7d94.md#insn-005a7dec) · [`005a7df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7d94.md#insn-005a7df8)
- 新版 [`005a7e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7dd4.md#insn-005a7e1c) · [`005a7e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7dd4.md#insn-005a7e2c) · [`005a7e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7dd4.md#insn-005a7e38)

~~~diff
- 005a7ddc ["INT_ADD", "register:40f0:8", ["const:5a7ddc:8", "const:4:8"]]
- 005a7ddc ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a7e1c ["INT_ADD", "register:40f0:8", ["const:5a7e1c:8", "const:4:8"]]
+ 005a7e1c ["CALL", null, ["callee:00c57eb0:8"]]
- 005a7ddc bytes 35bf1a94
+ 005a7e1c bytes 25c01a94
- 005a7dec ["INT_ADD", "register:40f0:8", ["const:5a7dec:8", "const:4:8"]]
- 005a7dec ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a7e2c ["INT_ADD", "register:40f0:8", ["const:5a7e2c:8", "const:4:8"]]
+ 005a7e2c ["CALL", null, ["callee:00c57eb0:8"]]
- 005a7dec bytes 31bf1a94
+ 005a7e2c bytes 21c01a94
- 005a7df8 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a7df8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a7df8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a7df8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a7e38 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a7e38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a7e38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a7e38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a7df8 bytes 29011891
+ 005a7e38 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-518be085f4fb9d72b68434d8022ed6d8"></a>

### [`005a7e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7e2c.md) → [`005a7e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7e6c.md) FUN_005a7e6c

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
      "definition_site": "005a7e70",
      "incomplete_value": false,
      "site": "005a7e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7e30",
      "incomplete_value": false,
      "site": "005a7e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a7e74",
      "DATA",
      [
        "storage",
        "00c6eae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a7e74",
      "DATA",
      [
        "storage",
        "00c6eee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7e2c.md#insn-005a7e30)
- 新版 [`005a7e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7e6c.md#insn-005a7e70)

~~~diff
- 005a7e30 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 005a7e30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7e30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7e30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7e70 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 005a7e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7e30 bytes 08a12b91
+ 005a7e70 bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-461c85c55fb0be8c39d30c4de9d255c8"></a>

### [`005a7e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7e3c.md) → [`005a7e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7e7c.md) FUN_005a7e7c

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
      "definition_site": "005a7e8c",
      "incomplete_value": false,
      "site": "005a7e94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7e4c",
      "incomplete_value": false,
      "site": "005a7e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a7e94",
      "DATA",
      [
        "storage",
        "00c6eae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a7e94",
      "DATA",
      [
        "storage",
        "00c6eee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7e3c.md#insn-005a7e4c) · [`005a7e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7e3c.md#insn-005a7e58)
- 新版 [`005a7e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7e7c.md#insn-005a7e8c) · [`005a7e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7e7c.md#insn-005a7e98)

~~~diff
- 005a7e4c ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 005a7e4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7e4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7e4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7e8c ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 005a7e8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7e8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7e8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7e4c bytes 08a12b91
+ 005a7e8c bytes 08a13b91
- 005a7e58 ["INT_ADD", "register:40f0:8", ["const:5a7e58:8", "const:4:8"]]
- 005a7e58 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005a7e98 ["INT_ADD", "register:40f0:8", ["const:5a7e98:8", "const:4:8"]]
+ 005a7e98 ["CALL", null, ["callee:00c57ea0:8"]]
- 005a7e58 bytes 12bf1a94
+ 005a7e98 bytes 02c01a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0bee201800b8f542395988b4bb7a651"></a>

### [`005a7e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7e74.md) → [`005a7eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7eb4.md) _INIT_53

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
      "definition_site": "005a7ef0",
      "incomplete_value": true,
      "site": "005a7f0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a7eb0",
      "incomplete_value": true,
      "site": "005a7ecc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a7f14",
      "incomplete_value": true,
      "site": "005a7f30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a7ed4",
      "incomplete_value": true,
      "site": "005a7ef0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a7f34",
      "incomplete_value": true,
      "site": "005a7f50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a7ef4",
      "incomplete_value": true,
      "site": "005a7f10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005a7ef0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005a7f14",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005a7f34",
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
      "005a7ef0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a7f14",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a7f34",
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

- 旧版 [`005a7eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7e74.md#insn-005a7eec) · [`005a7f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7e74.md#insn-005a7f0c) · [`005a80a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7e74.md#insn-005a80a8)
- 新版 [`005a7f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7eb4.md#insn-005a7f2c) · [`005a7f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7eb4.md#insn-005a7f4c) · [`005a80e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7eb4.md#insn-005a80e8)

~~~diff
- 005a7eec ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005a7eec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a7eec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a7eec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a7f2c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005a7f2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a7f2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a7f2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a7eec bytes 4a093691
+ 005a7f2c bytes 4a093791
- 005a7f0c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005a7f0c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a7f0c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a7f0c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a7f4c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005a7f4c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a7f4c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a7f4c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a7f0c bytes 4a553a91
+ 005a7f4c bytes 4a893d91
- 005a80a8 ["INT_ADD", "register:40f0:8", ["const:5a80a8:8", "const:4:8"]]
- 005a80a8 ["CALL", null, ["callee:00c57e30:8"]]
+ 005a80e8 ["INT_ADD", "register:40f0:8", ["const:5a80e8:8", "const:4:8"]]
+ 005a80e8 ["CALL", null, ["callee:00c57e30:8"]]
- 005a80a8 bytes 62be1a94
+ 005a80e8 bytes 52bf1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad24b8f800dec000e9ae062da262c862"></a>

### [`005a8204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8204.md) → [`005a8244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8244.md) FUN_005a8244

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.18% / 新版 96.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a8448",
      "incomplete_value": false,
      "site": "005a8454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8408",
      "incomplete_value": false,
      "site": "005a8414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "definition_site": "005a846c",
      "incomplete_value": false,
      "site": "005a8474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a842c",
      "incomplete_value": false,
      "site": "005a8434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:b38:8"
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
      "005a8274",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "005a8454",
      "DATA",
      [
        "storage",
        "00c6ec10",
        null,
        "undefined *"
      ]
    ],
    [
      "005a8474",
      "DATA",
      [
        "storage",
        "00c6eb38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a8274",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005a8454",
      "DATA",
      [
        "storage",
        "00c6f010",
        null,
        "undefined *"
      ]
    ],
    [
      "005a8474",
      "DATA",
      [
        "storage",
        "00c6ef38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a83f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8204.md#insn-005a83f4) · [`005a8228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8204.md#insn-005a8228) · [`005a8260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8204.md#insn-005a8260)
- 新版 [`005a8434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8244.md#insn-005a8434) · [`005a8268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8244.md#insn-005a8268) · [`005a82a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8244.md#insn-005a82a0)

~~~diff
- 005a83f4 ["INT_ADD", "register:40f0:8", ["const:5a83f4:8", "const:4:8"]]
- 005a83f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a8434 ["INT_ADD", "register:40f0:8", ["const:5a8434:8", "const:4:8"]]
+ 005a8434 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a83f4 bytes afbd1a94
+ 005a8434 bytes 9fbe1a94
- 005a8228 ["COPY", "tmp:0:8", ["const:165:8"]]
- 005a8228 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a8228 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a8228 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a8268 ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 005a8268 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a8268 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a8268 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a8228 bytes 4a950591
+ 005a8268 bytes 4a950691
- 005a8260 ["INT_ADD", "register:40f0:8", ["const:5a8260:8", "const:4:8"]]
- 005a8260 ["CALL", null, ["callee:0044108c:8"]]
+ 005a82a0 ["INT_ADD", "register:40f0:8", ["const:5a82a0:8", "const:4:8"]]
+ 005a82a0 ["CALL", null, ["callee:0044108c:8"]]
- 005a8260 bytes 7b63fa97
+ 005a82a0 bytes 7b63fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a4de432060dfe34634f130d09e025c2"></a>

### [`005a84f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a84f8.md) → [`005a8538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8538.md) FUN_005a8538

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009a5618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a5/009a5618.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)
- 新版 呼出元 1件 [`009a57b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a5/009a57b4.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)

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
      "definition_site": "005a855c",
      "incomplete_value": false,
      "site": "005a8560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a851c",
      "incomplete_value": false,
      "site": "005a8520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:b58:8"
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
      "005a8560",
      "DATA",
      [
        "storage",
        "00c6eb58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a8560",
      "DATA",
      [
        "storage",
        "00c6ef58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a84f8.md#insn-005a8514) · [`005a851c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a84f8.md#insn-005a851c)
- 新版 [`005a8554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8538.md#insn-005a8554) · [`005a855c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8538.md#insn-005a855c)

~~~diff
- 005a8514 ["INT_ADD", "register:40f0:8", ["const:5a8514:8", "const:4:8"]]
- 005a8514 ["CALL", null, ["callee:0059b908:8"]]
+ 005a8554 ["INT_ADD", "register:40f0:8", ["const:5a8554:8", "const:4:8"]]
+ 005a8554 ["CALL", null, ["callee:0059b908:8"]]
- 005a8514 bytes edccff97
+ 005a8554 bytes edccff97
- 005a851c ["COPY", "tmp:0:8", ["const:b58:8"]]
- 005a851c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a851c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a851c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a855c ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 005a855c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a855c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a855c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a851c bytes 08612d91
+ 005a855c bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e27117d03c4b0231c4f82293337d349e"></a>

### [`005a853c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a853c.md) → [`005a857c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a857c.md) FUN_005a857c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57dd0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c581d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a85ac",
      "incomplete_value": false,
      "site": "005a85b8",
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
            "const:fd1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a856c",
      "incomplete_value": false,
      "site": "005a8578",
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
            "const:f91:8"
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
      "definition_site": "005a85d8",
      "incomplete_value": false,
      "site": "005a85e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:79c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8598",
      "incomplete_value": false,
      "site": "005a85a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:75c:8"
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
      "005a85ac",
      "PARAM",
      [
        "storage",
        "002bff91",
        null,
        "string"
      ]
    ],
    [
      "005a85d8",
      "PARAM",
      [
        "storage",
        "002bc75c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a85ac",
      "PARAM",
      [
        "storage",
        "002bffd1",
        null,
        "string"
      ]
    ],
    [
      "005a85d8",
      "PARAM",
      [
        "storage",
        "002bc79c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a853c.md#insn-005a8578) · [`005a85a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a853c.md#insn-005a85a0) · [`005a8564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a853c.md#insn-005a8564)
- 新版 [`005a85b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a857c.md#insn-005a85b8) · [`005a85e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a857c.md#insn-005a85e0) · [`005a85a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a857c.md#insn-005a85a4)

~~~diff
- 005a8578 ["INT_ADD", "register:40f0:8", ["const:5a8578:8", "const:4:8"]]
- 005a8578 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a85b8 ["INT_ADD", "register:40f0:8", ["const:5a85b8:8", "const:4:8"]]
+ 005a85b8 ["CALL", null, ["callee:00c57f60:8"]]
- 005a8578 bytes 7abd1a94
+ 005a85b8 bytes 6abe1a94
- 005a85a0 ["INT_ADD", "register:40f0:8", ["const:5a85a0:8", "const:4:8"]]
- 005a85a0 ["CALL", null, ["callee:00c57f70:8"]]
+ 005a85e0 ["INT_ADD", "register:40f0:8", ["const:5a85e0:8", "const:4:8"]]
+ 005a85e0 ["CALL", null, ["callee:00c57f70:8"]]
- 005a85a0 bytes 74bd1a94
+ 005a85e0 bytes 64be1a94
- 005a8564 ["INT_ADD", "register:40f0:8", ["const:5a8564:8", "const:4:8"]]
- 005a8564 ["CALL", null, ["callee:00c581d0:8"]]
+ 005a85a4 ["INT_ADD", "register:40f0:8", ["const:5a85a4:8", "const:4:8"]]
+ 005a85a4 ["CALL", null, ["callee:00c581d0:8"]]
- 005a8564 bytes 1bbe1a94
+ 005a85a4 bytes 0bbf1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5acbb95594e6cfd0b90dd8f7c7354432"></a>

### [`005a8748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8748.md) → [`005a8788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8788.md) FUN_005a8788

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a87a4",
      "incomplete_value": false,
      "site": "005a87ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8764",
      "incomplete_value": false,
      "site": "005a876c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "definition_site": "005a87bc",
      "incomplete_value": false,
      "site": "005a87bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a877c",
      "incomplete_value": false,
      "site": "005a877c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "005a87ac",
      "DATA",
      [
        "storage",
        "00c6ec60",
        null,
        "undefined *"
      ]
    ],
    [
      "005a87bc",
      "DATA",
      [
        "storage",
        "00c6ebb0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a87ac",
      "DATA",
      [
        "storage",
        "00c6f060",
        null,
        "undefined *"
      ]
    ],
    [
      "005a87bc",
      "DATA",
      [
        "storage",
        "00c6efb0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a875c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8748.md#insn-005a875c) · [`005a8760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8748.md#insn-005a8760) · [`005a8764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8748.md#insn-005a8764)
- 新版 [`005a879c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8788.md#insn-005a879c) · [`005a87a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8788.md#insn-005a87a0) · [`005a87a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8788.md#insn-005a87a4)

~~~diff
- 005a875c ["INT_ADD", "register:40f0:8", ["const:5a875c:8", "const:4:8"]]
- 005a875c ["CALL", null, ["callee:00c57e90:8"]]
+ 005a879c ["INT_ADD", "register:40f0:8", ["const:5a879c:8", "const:4:8"]]
+ 005a879c ["CALL", null, ["callee:00c57e90:8"]]
- 005a875c bytes cdbc1a94
+ 005a879c bytes bdbd1a94
- 005a8760 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005a87a0 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005a8760 bytes 283600d0
+ 005a87a0 bytes 283600f0
- 005a8764 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 005a8764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a8764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a8764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a87a4 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 005a87a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a87a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a87a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a8764 bytes 08813191
+ 005a87a4 bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37a0e7b153d6334eede60c5467654c60"></a>

### [`005a8790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8790.md) → [`005a87d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a87d0.md) FUN_005a87d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a87ec",
      "incomplete_value": true,
      "site": "005a87f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005a87ac",
      "incomplete_value": true,
      "site": "005a87b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005a87e4",
      "READ",
      [
        "storage",
        "00c9af20",
        null,
        "pointer"
      ]
    ],
    [
      "005a87f0",
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
      "005a87e4",
      "READ",
      [
        "storage",
        "00c9b320",
        null,
        "pointer"
      ]
    ],
    [
      "005a87f0",
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

- 旧版 [`005a879c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8790.md#insn-005a879c) · [`005a87a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8790.md#insn-005a87a4) · [`005a87bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8790.md#insn-005a87bc)
- 新版 [`005a87dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a87d0.md#insn-005a87dc) · [`005a87e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a87d0.md#insn-005a87e4) · [`005a87fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a87d0.md#insn-005a87fc)

~~~diff
- 005a879c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005a87dc ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005a879c bytes 883700d0
+ 005a87dc bytes 883700f0
- 005a87a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
- 005a87a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a87e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:320:8"]]
+ 005a87e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a87a4 bytes 089147f9
+ 005a87e4 bytes 089141f9
- 005a87bc ["INT_ADD", "register:40f0:8", ["const:5a87bc:8", "const:4:8"]]
- 005a87bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a87fc ["INT_ADD", "register:40f0:8", ["const:5a87fc:8", "const:4:8"]]
+ 005a87fc ["CALL", null, ["callee:00c57eb0:8"]]
- 005a87bc bytes bdbc1a94
+ 005a87fc bytes adbd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a24d5a721ed940dd4412e3f277a9efb"></a>

### [`005a87e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a87e0.md) → [`005a8820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8820.md) FUN_005a8820

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
      "definition_site": "005a8828",
      "incomplete_value": false,
      "site": "005a882c",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a87e8",
      "incomplete_value": false,
      "site": "005a87ec",
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
            "const:600:8"
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
      "005a882c",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a882c",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a87e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a87e0.md#insn-005a87e8) · [`005a880c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a87e0.md#insn-005a880c)
- 新版 [`005a8828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8820.md#insn-005a8828) · [`005a884c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8820.md#insn-005a884c)

~~~diff
- 005a87e8 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a87e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a87e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a87e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a8828 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a8828 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a8828 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a8828 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a87e8 bytes 29011891
+ 005a8828 bytes 29012891
- 005a880c ["INT_ADD", "register:40f0:8", ["const:5a880c:8", "const:4:8"]]
- 005a880c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a884c ["INT_ADD", "register:40f0:8", ["const:5a884c:8", "const:4:8"]]
+ 005a884c ["CALL", null, ["callee:00c57eb0:8"]]
- 005a880c bytes a9bc1a94
+ 005a884c bytes 99bd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6ff2cdb20cc217c2c475d5a772c967c"></a>

### [`005a8860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8860.md) → [`005a88a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a88a0.md) FUN_005a88a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005a88a8",
      "incomplete_value": false,
      "site": "005a88ac",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8868",
      "incomplete_value": false,
      "site": "005a886c",
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
            "const:600:8"
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
      "005a88ac",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a88ac",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8860.md#insn-005a8868)
- 新版 [`005a88a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a88a0.md#insn-005a88a8)

~~~diff
- 005a8868 ["COPY", "tmp:0:8", ["const:600:8"]]
- 005a8868 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a8868 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a8868 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a88a8 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 005a88a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a88a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a88a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a8868 bytes 29011891
+ 005a88a8 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-319bca9fdcc446a0b2050db03ef5f9ec"></a>

### [`005a8884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8884.md) → [`005a88c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a88c4.md) FUN_005a88c4

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
      "definition_site": "005a88c8",
      "incomplete_value": false,
      "site": "005a88cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8888",
      "incomplete_value": false,
      "site": "005a888c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "005a88cc",
      "DATA",
      [
        "storage",
        "00c6ec60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a88cc",
      "DATA",
      [
        "storage",
        "00c6f060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8884.md#insn-005a8884) · [`005a8888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8884.md#insn-005a8888)
- 新版 [`005a88c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a88c4.md#insn-005a88c4) · [`005a88c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a88c4.md#insn-005a88c8)

~~~diff
- 005a8884 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005a88c4 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005a8884 bytes 283600d0
+ 005a88c4 bytes 283600f0
- 005a8888 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 005a8888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a8888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a8888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a88c8 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 005a88c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a88c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a88c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a8888 bytes 08813191
+ 005a88c8 bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d88bfd2d4ee48d17264f056c76a4cbe6"></a>

### [`005a88cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a88cc.md) → [`005a890c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a890c.md) _INIT_54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a896c",
      "incomplete_value": true,
      "site": "005a8988",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a892c",
      "incomplete_value": true,
      "site": "005a8948",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a898c",
      "incomplete_value": true,
      "site": "005a89a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a894c",
      "incomplete_value": true,
      "site": "005a8968",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a89ac",
      "incomplete_value": true,
      "site": "005a89c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a896c",
      "incomplete_value": true,
      "site": "005a8984",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005a8948",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005a896c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005a898c",
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
      "005a8948",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a896c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a898c",
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

- 旧版 [`005a8944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a88cc.md#insn-005a8944) · [`005a8964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a88cc.md#insn-005a8964) · [`005a8b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a88cc.md#insn-005a8b00)
- 新版 [`005a8984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a890c.md#insn-005a8984) · [`005a89a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a890c.md#insn-005a89a4) · [`005a8b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a890c.md#insn-005a8b40)

~~~diff
- 005a8944 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005a8944 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a8944 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a8944 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a8984 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005a8984 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a8984 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a8984 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a8944 bytes 4a093691
+ 005a8984 bytes 4a093791
- 005a8964 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005a8964 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a8964 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a8964 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a89a4 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005a89a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a89a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a89a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a8964 bytes 4a553a91
+ 005a89a4 bytes 4a893d91
- 005a8b00 ["INT_ADD", "register:40f0:8", ["const:5a8b00:8", "const:4:8"]]
- 005a8b00 ["CALL", null, ["callee:00c57e30:8"]]
+ 005a8b40 ["INT_ADD", "register:40f0:8", ["const:5a8b40:8", "const:4:8"]]
+ 005a8b40 ["CALL", null, ["callee:00c57e30:8"]]
- 005a8b00 bytes ccbb1a94
+ 005a8b40 bytes bcbc1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed90e0d092c7bb3de4ebfb728c6f35bf"></a>

### [`005a8c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8c5c.md) → [`005a8c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8c9c.md) FUN_005a8c9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005a8de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8de8.md) · 呼出先 2件 [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`005a9ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ce4.md)
- 新版 呼出元 1件 [`005a8e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8e28.md) · 呼出先 2件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`005a9d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a8ce8",
      "incomplete_value": false,
      "site": "005a8cf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8ca8",
      "incomplete_value": false,
      "site": "005a8cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a8cf0",
      "DATA",
      [
        "storage",
        "00c6ecb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a8cf0",
      "DATA",
      [
        "storage",
        "00c6f0b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8c5c.md#insn-005a8ca0) · [`005a8ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8c5c.md#insn-005a8ca4) · [`005a8ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8c5c.md#insn-005a8ca8)
- 新版 [`005a8ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8c9c.md#insn-005a8ce0) · [`005a8ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8c9c.md#insn-005a8ce4) · [`005a8ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8c9c.md#insn-005a8ce8)

~~~diff
- 005a8ca0 ["INT_ADD", "register:40f0:8", ["const:5a8ca0:8", "const:4:8"]]
- 005a8ca0 ["CALL", null, ["callee:0059b8dc:8"]]
+ 005a8ce0 ["INT_ADD", "register:40f0:8", ["const:5a8ce0:8", "const:4:8"]]
+ 005a8ce0 ["CALL", null, ["callee:0059b8dc:8"]]
- 005a8ca0 bytes ffcaff97
+ 005a8ce0 bytes ffcaff97
- 005a8ca4 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005a8ce4 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005a8ca4 bytes 283600d0
+ 005a8ce4 bytes 283600f0
- 005a8ca8 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 005a8ca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a8ca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a8ca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a8ce8 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 005a8ce8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a8ce8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a8ce8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a8ca8 bytes 08c13291
+ 005a8ce8 bytes 08c10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98cf55d1b2ec08ec334825cf460ec277"></a>

### [`005a8de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8de8.md) → [`005a8e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8e28.md) FUN_005a8e28

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005a8c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8c5c.md) [`005aa144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa144.md) [`009b2f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2f98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005a8c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8c9c.md) [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md) [`009b3134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3134.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.51% / 新版 95.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a8e84",
      "incomplete_value": true,
      "site": "005a8e84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8e44",
      "incomplete_value": true,
      "site": "005a8e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:165:8"
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
      "definition_site": "005a901c",
      "incomplete_value": true,
      "site": "005a901c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:81b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8fdc",
      "incomplete_value": true,
      "site": "005a8fdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:73f:8"
              ]
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
    "kind": "store_value",
    "new": {
      "definition_site": "005a9280",
      "incomplete_value": true,
      "site": "005a9280",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9240",
      "incomplete_value": true,
      "site": "005a9240",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2af:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 76,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a8e74",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "005a9008",
      "READ",
      [
        "storage",
        "002a673f",
        null,
        "string"
      ]
    ],
    [
      "005a908c",
      "READ",
      [
        "storage",
        "002a9d98",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a8e74",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005a9008",
      "READ",
      [
        "storage",
        "002a681b",
        null,
        "string"
      ]
    ],
    [
      "005a908c",
      "READ",
      [
        "storage",
        "002a9e65",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a92dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8de8.md#insn-005a92dc) · [`005a8e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8de8.md#insn-005a8e30) · [`005a8e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8de8.md#insn-005a8e50)
- 新版 [`005a931c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8e28.md#insn-005a931c) · [`005a8e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8e28.md#insn-005a8e70) · [`005a8e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8e28.md#insn-005a8e90)

~~~diff
- 005a92dc ["COPY", "tmp:0:8", ["const:435:8"]]
- 005a92dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a92dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a92dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a931c ["COPY", "tmp:0:8", ["const:475:8"]]
+ 005a931c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a931c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a931c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a92dc bytes 29d51091
+ 005a931c bytes 29d51191
- 005a8e30 ["COPY", "tmp:0:8", ["const:165:8"]]
- 005a8e30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a8e30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a8e30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a8e70 ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 005a8e70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a8e70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a8e70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a8e30 bytes 29950591
+ 005a8e70 bytes 29950691
- 005a8e50 ["INT_ADD", "register:40f0:8", ["const:5a8e50:8", "const:4:8"]]
- 005a8e50 ["CALL", null, ["callee:0044108c:8"]]
+ 005a8e90 ["INT_ADD", "register:40f0:8", ["const:5a8e90:8", "const:4:8"]]
+ 005a8e90 ["CALL", null, ["callee:0044108c:8"]]
- 005a8e50 bytes 7f60fa97
+ 005a8e90 bytes 7f60fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab750b480db8e9f6bb6809e800d5ee06"></a>

### [`005a9720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9720.md) → [`005a9760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9760.md) FUN_005a9760

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009b5220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5220.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)
- 新版 呼出元 1件 [`009b53bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b53bc.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a9784",
      "incomplete_value": true,
      "site": "005a978c",
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
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9744",
      "incomplete_value": true,
      "site": "005a974c",
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
            "const:cd0:8"
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
      "005a978c",
      "DATA",
      [
        "storage",
        "00c6ecd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a978c",
      "DATA",
      [
        "storage",
        "00c6f0d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a973c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9720.md#insn-005a973c) · [`005a9740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9720.md#insn-005a9740) · [`005a9744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9720.md#insn-005a9744)
- 新版 [`005a977c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9760.md#insn-005a977c) · [`005a9780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9760.md#insn-005a9780) · [`005a9784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9760.md#insn-005a9784)

~~~diff
- 005a973c ["INT_ADD", "register:40f0:8", ["const:5a973c:8", "const:4:8"]]
- 005a973c ["CALL", null, ["callee:0059b908:8"]]
+ 005a977c ["INT_ADD", "register:40f0:8", ["const:5a977c:8", "const:4:8"]]
+ 005a977c ["CALL", null, ["callee:0059b908:8"]]
- 005a973c bytes 63c8ff97
+ 005a977c bytes 63c8ff97
- 005a9740 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005a9780 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005a9740 bytes 283600b0
+ 005a9780 bytes 283600d0
- 005a9744 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 005a9744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a9744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a9744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a9784 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 005a9784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a9744 bytes 08413391
+ 005a9784 bytes 08410391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ca4e8424b24485acbffce58f49d0df2"></a>

### [`005a977c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a977c.md) → [`005a97bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a97bc.md) FUN_005a97bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a97f4",
      "incomplete_value": false,
      "site": "005a9800",
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
            "const:d86:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a97b4",
      "incomplete_value": false,
      "site": "005a97c0",
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
            "const:d46:8"
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
      "definition_site": "005a9820",
      "incomplete_value": false,
      "site": "005a9828",
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
            "const:722:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a97e0",
      "incomplete_value": false,
      "site": "005a97e8",
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
            "const:646:8"
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
      "005a97f4",
      "PARAM",
      [
        "storage",
        "002b0d46",
        null,
        "string"
      ]
    ],
    [
      "005a9820",
      "PARAM",
      [
        "storage",
        "002a5646",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a97f4",
      "PARAM",
      [
        "storage",
        "002b0d86",
        null,
        "string"
      ]
    ],
    [
      "005a9820",
      "PARAM",
      [
        "storage",
        "002a5722",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a97c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a977c.md#insn-005a97c0) · [`005a97e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a977c.md#insn-005a97e8) · [`005a97ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a977c.md#insn-005a97ac)
- 新版 [`005a9800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a97bc.md#insn-005a9800) · [`005a9828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a97bc.md#insn-005a9828) · [`005a97ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a97bc.md#insn-005a97ec)

~~~diff
- 005a97c0 ["INT_ADD", "register:40f0:8", ["const:5a97c0:8", "const:4:8"]]
- 005a97c0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a9800 ["INT_ADD", "register:40f0:8", ["const:5a9800:8", "const:4:8"]]
+ 005a9800 ["CALL", null, ["callee:00c57f60:8"]]
- 005a97c0 bytes e8b81a94
+ 005a9800 bytes d8b91a94
- 005a97e8 ["INT_ADD", "register:40f0:8", ["const:5a97e8:8", "const:4:8"]]
- 005a97e8 ["CALL", null, ["callee:00c57f70:8"]]
+ 005a9828 ["INT_ADD", "register:40f0:8", ["const:5a9828:8", "const:4:8"]]
+ 005a9828 ["CALL", null, ["callee:00c57f70:8"]]
- 005a97e8 bytes e2b81a94
+ 005a9828 bytes d2b91a94
- 005a97ac ["INT_ADD", "register:40f0:8", ["const:5a97ac:8", "const:4:8"]]
- 005a97ac ["CALL", null, ["callee:00c57f50:8"]]
+ 005a97ec ["INT_ADD", "register:40f0:8", ["const:5a97ec:8", "const:4:8"]]
+ 005a97ec ["CALL", null, ["callee:00c57f50:8"]]
- 005a97ac bytes e9b81a94
+ 005a97ec bytes d9b91a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71945d8695e51b6afa1722b6d53e1f3c"></a>

### [`005a992c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a992c.md) → [`005a996c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a996c.md) FUN_005a996c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`005970d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`00597110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597110.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a999c",
      "incomplete_value": false,
      "site": "005a99a4",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a995c",
      "incomplete_value": false,
      "site": "005a9964",
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
            "const:690:8"
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
      "definition_site": "005a99bc",
      "incomplete_value": false,
      "site": "005a99bc",
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
      "definition_site": "005a997c",
      "incomplete_value": false,
      "site": "005a997c",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a99f8",
      "incomplete_value": true,
      "site": "005a99f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:90e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a99b8",
      "incomplete_value": true,
      "site": "005a99b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8ce:8"
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
      "005a99a4",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ],
    [
      "005a99bc",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ],
    [
      "005a99d8",
      "READ",
      [
        "storage",
        "002b38ce",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a99a4",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "005a99bc",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "005a99d8",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a992c.md#insn-005a9978) · [`005a99f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a992c.md#insn-005a99f8) · [`005a9954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a992c.md#insn-005a9954)
- 新版 [`005a99b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a996c.md#insn-005a99b8) · [`005a9a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a996c.md#insn-005a9a38) · [`005a9994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a996c.md#insn-005a9994)

~~~diff
- 005a9978 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 005a9978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a9978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a9978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a99b8 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005a99b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a99b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a99b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a9978 bytes 08811b91
+ 005a99b8 bytes 08812b91
- 005a99f8 ["INT_ADD", "register:40f0:8", ["const:5a99f8:8", "const:4:8"]]
- 005a99f8 ["CALL", null, ["callee:0045982c:8"]]
+ 005a9a38 ["INT_ADD", "register:40f0:8", ["const:5a9a38:8", "const:4:8"]]
+ 005a9a38 ["CALL", null, ["callee:0045982c:8"]]
- 005a99f8 bytes 7dbffa97
+ 005a9a38 bytes 7dbffa97
- 005a9954 ["INT_ADD", "register:40f0:8", ["const:5a9954:8", "const:4:8"]]
- 005a9954 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a9994 ["INT_ADD", "register:40f0:8", ["const:5a9994:8", "const:4:8"]]
+ 005a9994 ["CALL", null, ["callee:00c57e90:8"]]
- 005a9954 bytes 4fb81a94
+ 005a9994 bytes 3fb91a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef20ed22e842ec90e1ca12d18ea90eb5"></a>

### [`005a9ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ad0.md) → [`005a9b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b10.md) FUN_005a9b10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a9b2c",
      "incomplete_value": false,
      "site": "005a9b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9aec",
      "incomplete_value": false,
      "site": "005a9af4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "definition_site": "005a9b44",
      "incomplete_value": false,
      "site": "005a9b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9b04",
      "incomplete_value": false,
      "site": "005a9b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "005a9b34",
      "DATA",
      [
        "storage",
        "00c6edd8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a9b44",
      "DATA",
      [
        "storage",
        "00c6ed28",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a9b34",
      "DATA",
      [
        "storage",
        "00c6f1d8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a9b44",
      "DATA",
      [
        "storage",
        "00c6f128",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ad0.md#insn-005a9ae4) · [`005a9ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ad0.md#insn-005a9ae8) · [`005a9aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ad0.md#insn-005a9aec)
- 新版 [`005a9b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b10.md#insn-005a9b24) · [`005a9b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b10.md#insn-005a9b28) · [`005a9b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b10.md#insn-005a9b2c)

~~~diff
- 005a9ae4 ["INT_ADD", "register:40f0:8", ["const:5a9ae4:8", "const:4:8"]]
- 005a9ae4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005a9b24 ["INT_ADD", "register:40f0:8", ["const:5a9b24:8", "const:4:8"]]
+ 005a9b24 ["CALL", null, ["callee:00c57e90:8"]]
- 005a9ae4 bytes ebb71a94
+ 005a9b24 bytes dbb81a94
- 005a9ae8 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005a9b28 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005a9ae8 bytes 283600b0
+ 005a9b28 bytes 283600d0
- 005a9aec ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 005a9aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a9aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a9aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a9b2c ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 005a9b2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9b2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9b2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a9aec bytes 08613791
+ 005a9b2c bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a2f5165272dcbe4fde721b3fa87ad3a"></a>

### [`005a9b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b18.md) → [`005a9b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b58.md) FUN_005a9b58

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
      "definition_site": "005a9b84",
      "incomplete_value": false,
      "site": "005a9b88",
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
      "definition_site": "005a9b44",
      "incomplete_value": false,
      "site": "005a9b48",
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
      "005a9b88",
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
      "005a9b88",
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

- 旧版 [`005a9b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b18.md#insn-005a9b34) · [`005a9b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b18.md#insn-005a9b3c) · [`005a9b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b18.md#insn-005a9b54)
- 新版 [`005a9b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b58.md#insn-005a9b74) · [`005a9b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b58.md#insn-005a9b7c) · [`005a9b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b58.md#insn-005a9b94)

~~~diff
- 005a9b34 ["INT_ADD", "register:40f0:8", ["const:5a9b34:8", "const:4:8"]]
- 005a9b34 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a9b74 ["INT_ADD", "register:40f0:8", ["const:5a9b74:8", "const:4:8"]]
+ 005a9b74 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a9b34 bytes dfb71a94
+ 005a9b74 bytes cfb81a94
- 005a9b3c ["COPY", "tmp:0:8", ["const:610:8"]]
- 005a9b3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a9b3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a9b3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a9b7c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005a9b7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9b7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9b7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a9b3c bytes 08411891
+ 005a9b7c bytes 08412891
- 005a9b54 ["INT_ADD", "register:40f0:8", ["const:5a9b54:8", "const:4:8"]]
- 005a9b54 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a9b94 ["INT_ADD", "register:40f0:8", ["const:5a9b94:8", "const:4:8"]]
+ 005a9b94 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a9b54 bytes d7b71a94
+ 005a9b94 bytes c7b81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ec709d82065ffededbb178298e8e509"></a>

### [`005a9b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b7c.md) → [`005a9bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9bbc.md) FUN_005a9bbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "005a9be8",
      "incomplete_value": true,
      "site": "005a9bec",
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
                "register:4040:8"
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
      "definition_site": "005a9ba8",
      "incomplete_value": true,
      "site": "005a9bac",
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
                "register:4040:8"
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
      "005a9bec",
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
      "005a9bec",
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

- 旧版 [`005a9b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b7c.md#insn-005a9b98) · [`005a9ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b7c.md#insn-005a9ba0) · [`005a9bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9b7c.md#insn-005a9bb8)
- 新版 [`005a9bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9bbc.md#insn-005a9bd8) · [`005a9be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9bbc.md#insn-005a9be0) · [`005a9bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9bbc.md#insn-005a9bf8)

~~~diff
- 005a9b98 ["INT_ADD", "register:40f0:8", ["const:5a9b98:8", "const:4:8"]]
- 005a9b98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a9bd8 ["INT_ADD", "register:40f0:8", ["const:5a9bd8:8", "const:4:8"]]
+ 005a9bd8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a9b98 bytes c6b71a94
+ 005a9bd8 bytes b6b81a94
- 005a9ba0 ["COPY", "tmp:0:8", ["const:610:8"]]
- 005a9ba0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a9ba0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a9ba0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a9be0 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005a9be0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9be0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9be0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a9ba0 bytes 08411891
+ 005a9be0 bytes 08412891
- 005a9bb8 ["INT_ADD", "register:40f0:8", ["const:5a9bb8:8", "const:4:8"]]
- 005a9bb8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a9bf8 ["INT_ADD", "register:40f0:8", ["const:5a9bf8:8", "const:4:8"]]
+ 005a9bf8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a9bb8 bytes beb71a94
+ 005a9bf8 bytes aeb81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1332c19f0e7cf2fc90565a24ccc3ee5a"></a>

### [`005a9bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9bdc.md) → [`005a9c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9c1c.md) FUN_005a9c1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`005a9cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9cc0.md) [`005aa214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa214.md) · 呼出先 2件 [`005aa144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa144.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`005a9d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d00.md) [`005aa254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa254.md) · 呼出先 2件 [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a9c9c",
      "incomplete_value": false,
      "site": "005a9ca0",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9c5c",
      "incomplete_value": false,
      "site": "005a9c60",
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
            "const:600:8"
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
      "005a9ca0",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a9ca0",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9bdc.md#insn-005a9c14) · [`005a9c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9bdc.md#insn-005a9c28) · [`005a9c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9bdc.md#insn-005a9c50)
- 新版 [`005a9c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9c1c.md#insn-005a9c54) · [`005a9c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9c1c.md#insn-005a9c68) · [`005a9c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9c1c.md#insn-005a9c90)

~~~diff
- 005a9c14 ["INT_ADD", "register:40f0:8", ["const:5a9c14:8", "const:4:8"]]
- 005a9c14 ["CALL", null, ["callee:005aa184:8"]]
+ 005a9c54 ["INT_ADD", "register:40f0:8", ["const:5a9c54:8", "const:4:8"]]
+ 005a9c54 ["CALL", null, ["callee:005aa184:8"]]
- 005a9c14 bytes 4c010094
+ 005a9c54 bytes 4c010094
- 005a9c28 ["INT_ADD", "register:40f0:8", ["const:5a9c28:8", "const:4:8"]]
- 005a9c28 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a9c68 ["INT_ADD", "register:40f0:8", ["const:5a9c68:8", "const:4:8"]]
+ 005a9c68 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a9c28 bytes a2b71a94
+ 005a9c68 bytes 92b81a94
- 005a9c50 ["INT_ADD", "register:40f0:8", ["const:5a9c50:8", "const:4:8"]]
- 005a9c50 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005a9c90 ["INT_ADD", "register:40f0:8", ["const:5a9c90:8", "const:4:8"]]
+ 005a9c90 ["CALL", null, ["callee:00c57eb0:8"]]
- 005a9c50 bytes 98b71a94
+ 005a9c90 bytes 88b81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-245a18d21ea58282a480a6b44aed1114"></a>

### [`005a9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ea4.md) → [`005a9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ee4.md) FUN_005a9ee4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a9ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ce4.md) [`009b5be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5be8.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`005a9d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md) [`009b5d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5d84.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005a9ef0",
      "incomplete_value": false,
      "site": "005a9ef4",
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
      "definition_site": "005a9eb0",
      "incomplete_value": false,
      "site": "005a9eb4",
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
      "005a9ef0",
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
      "005a9ef0",
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

- 旧版 [`005a9eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ea4.md#insn-005a9eb4) · [`005a9eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ea4.md#insn-005a9eb0)
- 新版 [`005a9ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ee4.md#insn-005a9ef4) · [`005a9ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ee4.md#insn-005a9ef0)

~~~diff
- 005a9eb4 ["INT_ADD", "register:40f0:8", ["const:5a9eb4:8", "const:4:8"]]
- 005a9eb4 ["CALL", null, ["callee:0043b778:8"]]
+ 005a9ef4 ["INT_ADD", "register:40f0:8", ["const:5a9ef4:8", "const:4:8"]]
+ 005a9ef4 ["CALL", null, ["callee:0043b778:8"]]
- 005a9eb4 bytes 2146fa97
+ 005a9ef4 bytes 2146fa97
- 005a9eb0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005a9eb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005a9eb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005a9eb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005a9ef0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005a9ef0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005a9ef0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005a9ef0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005a9eb0 bytes 00303c91
+ 005a9ef0 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f12ce1f9ef23feefa049a2beb986165a"></a>

### [`005aa130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md) → [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) FUN_005aa170

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 12件 [`005a9f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9f14.md) [`005aa5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa5f8.md) [`005ab760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab760.md) [`00747a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747a70.md) [`007481cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/007481cc.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 12件 [`005a9f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md) [`005aa638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa638.md) [`005ab7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab7a0.md) [`00747ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747ab0.md) [`0074820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/0074820c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005aa17c",
      "incomplete_value": false,
      "site": "005aa180",
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
      "definition_site": "005aa13c",
      "incomplete_value": false,
      "site": "005aa140",
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
      "005aa17c",
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
      "005aa17c",
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

- 旧版 [`005aa140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md#insn-005aa140) · [`005aa13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md#insn-005aa13c)
- 新版 [`005aa180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md#insn-005aa180) · [`005aa17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md#insn-005aa17c)

~~~diff
- 005aa140 ["INT_ADD", "register:40f0:8", ["const:5aa140:8", "const:4:8"]]
- 005aa140 ["CALL", null, ["callee:0043b778:8"]]
+ 005aa180 ["INT_ADD", "register:40f0:8", ["const:5aa180:8", "const:4:8"]]
+ 005aa180 ["CALL", null, ["callee:0043b778:8"]]
- 005aa140 bytes 7e45fa97
+ 005aa180 bytes 7e45fa97
- 005aa13c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005aa13c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005aa13c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005aa13c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005aa17c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005aa17c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005aa17c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005aa17c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005aa13c bytes 00303c91
+ 005aa17c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3773df57a5811feeb42ac0f0f61bb26"></a>

### [`005aa1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa1d4.md) → [`005aa214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa214.md) FUN_005aa214

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
      "definition_site": "005aa218",
      "incomplete_value": false,
      "site": "005aa21c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa1d8",
      "incomplete_value": false,
      "site": "005aa1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005aa21c",
      "DATA",
      [
        "storage",
        "00c6ed88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005aa21c",
      "DATA",
      [
        "storage",
        "00c6f188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa1d4.md#insn-005aa1d4) · [`005aa1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa1d4.md#insn-005aa1d8)
- 新版 [`005aa214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa214.md#insn-005aa214) · [`005aa218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa214.md#insn-005aa218)

~~~diff
- 005aa1d4 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005aa214 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005aa1d4 bytes 28360090
+ 005aa214 bytes 283600b0
- 005aa1d8 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 005aa1d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005aa1d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005aa1d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aa218 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 005aa218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005aa1d8 bytes 08213691
+ 005aa218 bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51bcc36088c6e89a3a48797a43481ea6"></a>

### [`005aa1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa1e4.md) → [`005aa224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa224.md) FUN_005aa224

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
      "definition_site": "005aa234",
      "incomplete_value": false,
      "site": "005aa23c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa1f4",
      "incomplete_value": false,
      "site": "005aa1fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005aa23c",
      "DATA",
      [
        "storage",
        "00c6ed88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005aa23c",
      "DATA",
      [
        "storage",
        "00c6f188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa1e4.md#insn-005aa1f0) · [`005aa1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa1e4.md#insn-005aa1f4) · [`005aa200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa1e4.md#insn-005aa200)
- 新版 [`005aa230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa224.md#insn-005aa230) · [`005aa234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa224.md#insn-005aa234) · [`005aa240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa224.md#insn-005aa240)

~~~diff
- 005aa1f0 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005aa230 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005aa1f0 bytes 28360090
+ 005aa230 bytes 283600b0
- 005aa1f4 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 005aa1f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005aa1f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005aa1f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aa234 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 005aa234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005aa1f4 bytes 08213691
+ 005aa234 bytes 08210691
- 005aa200 ["INT_ADD", "register:40f0:8", ["const:5aa200:8", "const:4:8"]]
- 005aa200 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005aa240 ["INT_ADD", "register:40f0:8", ["const:5aa240:8", "const:4:8"]]
+ 005aa240 ["CALL", null, ["callee:00c57ea0:8"]]
- 005aa200 bytes 28b61a94
+ 005aa240 bytes 18b71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af6d0dc6169ec3629dc77c714f5c43c1"></a>

### [`005aa220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa220.md) → [`005aa260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa260.md) FUN_005aa260

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
      "definition_site": "005aa264",
      "incomplete_value": false,
      "site": "005aa268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa224",
      "incomplete_value": false,
      "site": "005aa228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "005aa268",
      "DATA",
      [
        "storage",
        "00c6edd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005aa268",
      "DATA",
      [
        "storage",
        "00c6f1d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa220.md#insn-005aa220) · [`005aa224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa220.md#insn-005aa224)
- 新版 [`005aa260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa260.md#insn-005aa260) · [`005aa264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa260.md#insn-005aa264)

~~~diff
- 005aa220 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005aa260 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005aa220 bytes 28360090
+ 005aa260 bytes 283600b0
- 005aa224 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 005aa224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005aa224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005aa224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aa264 ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 005aa264 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa264 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa264 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005aa224 bytes 08613791
+ 005aa264 bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed4dd7a9255afbf9647d9f05b915f6b2"></a>

### [`005aa230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa230.md) → [`005aa270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa270.md) FUN_005aa270

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
      "definition_site": "005aa280",
      "incomplete_value": false,
      "site": "005aa288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa240",
      "incomplete_value": false,
      "site": "005aa248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "005aa288",
      "DATA",
      [
        "storage",
        "00c6edd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005aa288",
      "DATA",
      [
        "storage",
        "00c6f1d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa230.md#insn-005aa23c) · [`005aa240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa230.md#insn-005aa240) · [`005aa24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa230.md#insn-005aa24c)
- 新版 [`005aa27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa270.md#insn-005aa27c) · [`005aa280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa270.md#insn-005aa280) · [`005aa28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa270.md#insn-005aa28c)

~~~diff
- 005aa23c ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005aa27c ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005aa23c bytes 28360090
+ 005aa27c bytes 283600b0
- 005aa240 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 005aa240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005aa240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005aa240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aa280 ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 005aa280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005aa240 bytes 08613791
+ 005aa280 bytes 08610791
- 005aa24c ["INT_ADD", "register:40f0:8", ["const:5aa24c:8", "const:4:8"]]
- 005aa24c ["CALL", null, ["callee:00c57ea0:8"]]
+ 005aa28c ["INT_ADD", "register:40f0:8", ["const:5aa28c:8", "const:4:8"]]
+ 005aa28c ["CALL", null, ["callee:00c57ea0:8"]]
- 005aa24c bytes 15b61a94
+ 005aa28c bytes 05b71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9151834f89d1e48869aff34e911dbc1"></a>

### [`005aa268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa268.md) → [`005aa2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa2a8.md) _INIT_55

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
      "definition_site": "005aa2e4",
      "incomplete_value": true,
      "site": "005aa300",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005aa2a4",
      "incomplete_value": true,
      "site": "005aa2c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005aa308",
      "incomplete_value": true,
      "site": "005aa324",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005aa2c8",
      "incomplete_value": true,
      "site": "005aa2e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005aa328",
      "incomplete_value": true,
      "site": "005aa344",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005aa2e8",
      "incomplete_value": true,
      "site": "005aa304",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005aa2e4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005aa308",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005aa328",
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
      "005aa2e4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005aa308",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005aa328",
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

- 旧版 [`005aa2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa268.md#insn-005aa2e0) · [`005aa300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa268.md#insn-005aa300) · [`005aa3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa268.md#insn-005aa3c8)
- 新版 [`005aa320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa2a8.md#insn-005aa320) · [`005aa340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa2a8.md#insn-005aa340) · [`005aa408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa2a8.md#insn-005aa408)

~~~diff
- 005aa2e0 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005aa2e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005aa2e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005aa2e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005aa320 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005aa320 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005aa320 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005aa320 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005aa2e0 bytes 4a093691
+ 005aa320 bytes 4a093791
- 005aa300 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005aa300 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005aa300 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005aa300 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005aa340 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005aa340 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005aa340 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005aa340 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005aa300 bytes 4a553a91
+ 005aa340 bytes 4a893d91
- 005aa3c8 ["INT_ADD", "register:40f0:8", ["const:5aa3c8:8", "const:4:8"]]
- 005aa3c8 ["CALL", null, ["callee:0043b7f8:8"]]
+ 005aa408 ["INT_ADD", "register:40f0:8", ["const:5aa408:8", "const:4:8"]]
+ 005aa408 ["CALL", null, ["callee:0043b7f8:8"]]
- 005aa3c8 bytes fc44fa97
+ 005aa408 bytes fc44fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f02e88bcebb3581b27bc344f1af6f58"></a>

### [`005aa5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa5f8.md) → [`005aa638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa638.md) FUN_005aa638

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005aa76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa76c.md) · 呼出先 6件 [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`005aa130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005aa7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa7ac.md) · 呼出先 6件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.70% / 新版 95.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005aa66c",
      "incomplete_value": false,
      "site": "005aa670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa62c",
      "incomplete_value": false,
      "site": "005aa630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "definition_site": "005aa768",
      "incomplete_value": false,
      "site": "005aa76c",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa728",
      "incomplete_value": false,
      "site": "005aa72c",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005aa670",
      "DATA",
      [
        "storage",
        "00c6ee28",
        null,
        "pointer"
      ]
    ],
    [
      "005aa76c",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aa670",
      "DATA",
      [
        "storage",
        "00c6f228",
        null,
        "pointer"
      ]
    ],
    [
      "005aa76c",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa5f8.md#insn-005aa624) · [`005aa628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa5f8.md#insn-005aa628) · [`005aa62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa5f8.md#insn-005aa62c)
- 新版 [`005aa664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa638.md#insn-005aa664) · [`005aa668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa638.md#insn-005aa668) · [`005aa66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa638.md#insn-005aa66c)

~~~diff
- 005aa624 ["INT_ADD", "register:40f0:8", ["const:5aa624:8", "const:4:8"]]
- 005aa624 ["CALL", null, ["callee:0059b8dc:8"]]
+ 005aa664 ["INT_ADD", "register:40f0:8", ["const:5aa664:8", "const:4:8"]]
+ 005aa664 ["CALL", null, ["callee:0059b8dc:8"]]
- 005aa624 bytes 9ec4ff97
+ 005aa664 bytes 9ec4ff97
- 005aa628 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005aa668 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005aa628 bytes 28360090
+ 005aa668 bytes 283600b0
- 005aa62c ["COPY", "tmp:0:8", ["const:e28:8"]]
- 005aa62c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005aa62c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005aa62c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aa66c ["COPY", "tmp:0:8", ["const:228:8"]]
+ 005aa66c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa66c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa66c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005aa62c bytes 08a13891
+ 005aa66c bytes 08a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0e8f4dfefffd35506129b68e6ba81a4"></a>

### [`005aa76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa76c.md) → [`005aa7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa7ac.md) FUN_005aa7ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005aa5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa5f8.md) [`009b35fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b35fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005aa638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa638.md) [`009b3798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3798.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.76% / 新版 95.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005aa808",
      "incomplete_value": true,
      "site": "005aa808",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa7c8",
      "incomplete_value": true,
      "site": "005aa7c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:165:8"
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
      "definition_site": "005aa940",
      "incomplete_value": true,
      "site": "005aa940",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f2d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa900",
      "incomplete_value": true,
      "site": "005aa900",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e60:8"
              ]
            ]
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
      "definition_site": "005aaa74",
      "incomplete_value": true,
      "site": "005aaa74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aaa34",
      "incomplete_value": true,
      "site": "005aaa34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:92:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 49,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005aa7f8",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "005aa92c",
      "READ",
      [
        "storage",
        "0029fe60",
        null,
        "string"
      ]
    ],
    [
      "005aaa64",
      "READ",
      [
        "storage",
        "002b9092",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005aa7f8",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005aa92c",
      "READ",
      [
        "storage",
        "0029ff2d",
        null,
        "string"
      ]
    ],
    [
      "005aaa64",
      "READ",
      [
        "storage",
        "002b90d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa76c.md#insn-005aa8c0) · [`005aa940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa76c.md#insn-005aa940) · [`005aa7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa76c.md#insn-005aa7b4)
- 新版 [`005aa900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa7ac.md#insn-005aa900) · [`005aa980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa7ac.md#insn-005aa980) · [`005aa7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa7ac.md#insn-005aa7f4)

~~~diff
- 005aa8c0 ["INT_ADD", "register:40f0:8", ["const:5aa8c0:8", "const:4:8"]]
- 005aa8c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005aa900 ["INT_ADD", "register:40f0:8", ["const:5aa900:8", "const:4:8"]]
+ 005aa900 ["CALL", null, ["callee:00c57eb0:8"]]
- 005aa8c0 bytes 7cb41a94
+ 005aa900 bytes 6cb51a94
- 005aa940 ["INT_ADD", "register:40f0:8", ["const:5aa940:8", "const:4:8"]]
- 005aa940 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005aa980 ["INT_ADD", "register:40f0:8", ["const:5aa980:8", "const:4:8"]]
+ 005aa980 ["CALL", null, ["callee:00c57eb0:8"]]
- 005aa940 bytes 5cb41a94
+ 005aa980 bytes 4cb51a94
- 005aa7b4 ["COPY", "tmp:0:8", ["const:165:8"]]
- 005aa7b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005aa7b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005aa7b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005aa7f4 ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 005aa7f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005aa7f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005aa7f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005aa7b4 bytes 29950591
+ 005aa7f4 bytes 29950691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de106e448071be6668493c762f2bb4ed"></a>

### [`005aae48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aae48.md) → [`005aae88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aae88.md) FUN_005aae88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009b4764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4764.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)
- 新版 呼出元 1件 [`009b4900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4900.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)

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
      "definition_site": "005aaeac",
      "incomplete_value": false,
      "site": "005aaeb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aae6c",
      "incomplete_value": false,
      "site": "005aae74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "005aaeb4",
      "DATA",
      [
        "storage",
        "00c6ee48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005aaeb4",
      "DATA",
      [
        "storage",
        "00c6f248",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aae64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aae48.md#insn-005aae64) · [`005aae68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aae48.md#insn-005aae68) · [`005aae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aae48.md#insn-005aae6c)
- 新版 [`005aaea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aae88.md#insn-005aaea4) · [`005aaea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aae88.md#insn-005aaea8) · [`005aaeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aae88.md#insn-005aaeac)

~~~diff
- 005aae64 ["INT_ADD", "register:40f0:8", ["const:5aae64:8", "const:4:8"]]
- 005aae64 ["CALL", null, ["callee:0059b908:8"]]
+ 005aaea4 ["INT_ADD", "register:40f0:8", ["const:5aaea4:8", "const:4:8"]]
+ 005aaea4 ["CALL", null, ["callee:0059b908:8"]]
- 005aae64 bytes 99c2ff97
+ 005aaea4 bytes 99c2ff97
- 005aae68 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005aaea8 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005aae68 bytes 28360090
+ 005aaea8 bytes 283600b0
- 005aae6c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005aae6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005aae6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005aae6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aaeac ["COPY", "tmp:0:8", ["const:248:8"]]
+ 005aaeac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aaeac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aaeac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005aae6c bytes 08213991
+ 005aaeac bytes 08210991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a3d8cc7bae6320e053d58aa891212b1"></a>

### [`005aaea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aaea4.md) → [`005aaee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aaee4.md) FUN_005aaee4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.74% / 新版 96.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005aaf1c",
      "incomplete_value": false,
      "site": "005aaf28",
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
            "const:d86:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aaedc",
      "incomplete_value": false,
      "site": "005aaee8",
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
            "const:d46:8"
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
      "definition_site": "005aaf48",
      "incomplete_value": false,
      "site": "005aaf50",
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
            "const:722:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aaf08",
      "incomplete_value": false,
      "site": "005aaf10",
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
            "const:646:8"
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
      "definition_site": "005aafac",
      "incomplete_value": false,
      "site": "005aafb4",
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
            "const:d94:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aaf6c",
      "incomplete_value": false,
      "site": "005aaf74",
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
            "const:d54:8"
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
      "005aaf1c",
      "PARAM",
      [
        "storage",
        "002b0d46",
        null,
        "string"
      ]
    ],
    [
      "005aaf48",
      "PARAM",
      [
        "storage",
        "002a5646",
        null,
        "string"
      ]
    ],
    [
      "005aafac",
      "PARAM",
      [
        "storage",
        "002b0d54",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005aaf1c",
      "PARAM",
      [
        "storage",
        "002b0d86",
        null,
        "string"
      ]
    ],
    [
      "005aaf48",
      "PARAM",
      [
        "storage",
        "002a5722",
        null,
        "string"
      ]
    ],
    [
      "005aafac",
      "PARAM",
      [
        "storage",
        "002b0d94",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aaee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aaea4.md#insn-005aaee8) · [`005aaf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aaea4.md#insn-005aaf10) · [`005aaf74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aaea4.md#insn-005aaf74)
- 新版 [`005aaf28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aaee4.md#insn-005aaf28) · [`005aaf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aaee4.md#insn-005aaf50) · [`005aafb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aaee4.md#insn-005aafb4)

~~~diff
- 005aaee8 ["INT_ADD", "register:40f0:8", ["const:5aaee8:8", "const:4:8"]]
- 005aaee8 ["CALL", null, ["callee:00c57f60:8"]]
+ 005aaf28 ["INT_ADD", "register:40f0:8", ["const:5aaf28:8", "const:4:8"]]
+ 005aaf28 ["CALL", null, ["callee:00c57f60:8"]]
- 005aaee8 bytes 1eb31a94
+ 005aaf28 bytes 0eb41a94
- 005aaf10 ["INT_ADD", "register:40f0:8", ["const:5aaf10:8", "const:4:8"]]
- 005aaf10 ["CALL", null, ["callee:00c57f70:8"]]
+ 005aaf50 ["INT_ADD", "register:40f0:8", ["const:5aaf50:8", "const:4:8"]]
+ 005aaf50 ["CALL", null, ["callee:00c57f70:8"]]
- 005aaf10 bytes 18b31a94
+ 005aaf50 bytes 08b41a94
- 005aaf74 ["INT_ADD", "register:40f0:8", ["const:5aaf74:8", "const:4:8"]]
- 005aaf74 ["CALL", null, ["callee:00c57f70:8"]]
+ 005aafb4 ["INT_ADD", "register:40f0:8", ["const:5aafb4:8", "const:4:8"]]
+ 005aafb4 ["CALL", null, ["callee:00c57f70:8"]]
- 005aaf74 bytes ffb21a94
+ 005aafb4 bytes efb31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f143a9f8e861c20f66913f2785a0c02"></a>

### [`005ab0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab0ec.md) → [`005ab12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab12c.md) FUN_005ab12c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ab148",
      "incomplete_value": false,
      "site": "005ab150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab108",
      "incomplete_value": false,
      "site": "005ab110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "definition_site": "005ab160",
      "incomplete_value": false,
      "site": "005ab160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab120",
      "incomplete_value": false,
      "site": "005ab120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
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
      "005ab150",
      "DATA",
      [
        "storage",
        "00c6ef50",
        null,
        "undefined *"
      ]
    ],
    [
      "005ab160",
      "DATA",
      [
        "storage",
        "00c6eea0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005ab150",
      "DATA",
      [
        "storage",
        "00c6f350",
        null,
        "undefined *"
      ]
    ],
    [
      "005ab160",
      "DATA",
      [
        "storage",
        "00c6f2a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab0ec.md#insn-005ab100) · [`005ab104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab0ec.md#insn-005ab104) · [`005ab108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab0ec.md#insn-005ab108)
- 新版 [`005ab140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab12c.md#insn-005ab140) · [`005ab144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab12c.md#insn-005ab144) · [`005ab148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab12c.md#insn-005ab148)

~~~diff
- 005ab100 ["INT_ADD", "register:40f0:8", ["const:5ab100:8", "const:4:8"]]
- 005ab100 ["CALL", null, ["callee:00c57e90:8"]]
+ 005ab140 ["INT_ADD", "register:40f0:8", ["const:5ab140:8", "const:4:8"]]
+ 005ab140 ["CALL", null, ["callee:00c57e90:8"]]
- 005ab100 bytes 64b21a94
+ 005ab140 bytes 54b31a94
- 005ab104 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005ab144 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005ab104 bytes 083600f0
+ 005ab144 bytes 28360090
- 005ab108 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 005ab108 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab108 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab108 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab148 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 005ab148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab108 bytes 08413d91
+ 005ab148 bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-335ac92dfd9b43efa97b6d41f42ad22c"></a>

### [`005ab134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab134.md) → [`005ab174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab174.md) FUN_005ab174

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
      "definition_site": "005ab1a0",
      "incomplete_value": false,
      "site": "005ab1a4",
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
      "definition_site": "005ab160",
      "incomplete_value": false,
      "site": "005ab164",
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
      "005ab1a4",
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
      "005ab1a4",
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

- 旧版 [`005ab150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab134.md#insn-005ab150) · [`005ab158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab134.md#insn-005ab158) · [`005ab170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab134.md#insn-005ab170)
- 新版 [`005ab190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab174.md#insn-005ab190) · [`005ab198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab174.md#insn-005ab198) · [`005ab1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab174.md#insn-005ab1b0)

~~~diff
- 005ab150 ["INT_ADD", "register:40f0:8", ["const:5ab150:8", "const:4:8"]]
- 005ab150 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ab190 ["INT_ADD", "register:40f0:8", ["const:5ab190:8", "const:4:8"]]
+ 005ab190 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ab150 bytes 58b21a94
+ 005ab190 bytes 48b31a94
- 005ab158 ["COPY", "tmp:0:8", ["const:610:8"]]
- 005ab158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab198 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005ab198 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab198 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab198 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab158 bytes 08411891
+ 005ab198 bytes 08412891
- 005ab170 ["INT_ADD", "register:40f0:8", ["const:5ab170:8", "const:4:8"]]
- 005ab170 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ab1b0 ["INT_ADD", "register:40f0:8", ["const:5ab1b0:8", "const:4:8"]]
+ 005ab1b0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ab170 bytes 50b21a94
+ 005ab1b0 bytes 40b31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-133167bed4cc9a5521d46c7ddd2ca79c"></a>

### [`005ab198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab198.md) → [`005ab1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab1d8.md) FUN_005ab1d8

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
      "definition_site": "005ab204",
      "incomplete_value": false,
      "site": "005ab208",
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
      "definition_site": "005ab1c4",
      "incomplete_value": false,
      "site": "005ab1c8",
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
      "005ab208",
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
      "005ab208",
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

- 旧版 [`005ab1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab198.md#insn-005ab1b4) · [`005ab1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab198.md#insn-005ab1bc) · [`005ab1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab198.md#insn-005ab1d4)
- 新版 [`005ab1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab1d8.md#insn-005ab1f4) · [`005ab1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab1d8.md#insn-005ab1fc) · [`005ab214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab1d8.md#insn-005ab214)

~~~diff
- 005ab1b4 ["INT_ADD", "register:40f0:8", ["const:5ab1b4:8", "const:4:8"]]
- 005ab1b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ab1f4 ["INT_ADD", "register:40f0:8", ["const:5ab1f4:8", "const:4:8"]]
+ 005ab1f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ab1b4 bytes 3fb21a94
+ 005ab1f4 bytes 2fb31a94
- 005ab1bc ["COPY", "tmp:0:8", ["const:610:8"]]
- 005ab1bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab1bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab1bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab1fc ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005ab1fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab1fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab1fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab1bc bytes 08411891
+ 005ab1fc bytes 08412891
- 005ab1d4 ["INT_ADD", "register:40f0:8", ["const:5ab1d4:8", "const:4:8"]]
- 005ab1d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ab214 ["INT_ADD", "register:40f0:8", ["const:5ab214:8", "const:4:8"]]
+ 005ab214 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ab1d4 bytes 37b21a94
+ 005ab214 bytes 27b31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-943d2fe7e1b00cf8e0b3d11b496202a7"></a>

### [`005ab1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab1f8.md) → [`005ab238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab238.md) FUN_005ab238

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005ab280",
      "incomplete_value": false,
      "site": "005ab284",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab240",
      "incomplete_value": false,
      "site": "005ab244",
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
            "const:600:8"
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
      "005ab284",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ab284",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab1f8.md#insn-005ab214) · [`005ab224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab1f8.md#insn-005ab224) · [`005ab234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab1f8.md#insn-005ab234)
- 新版 [`005ab254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab238.md#insn-005ab254) · [`005ab264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab238.md#insn-005ab264) · [`005ab274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab238.md#insn-005ab274)

~~~diff
- 005ab214 ["INT_ADD", "register:40f0:8", ["const:5ab214:8", "const:4:8"]]
- 005ab214 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ab254 ["INT_ADD", "register:40f0:8", ["const:5ab254:8", "const:4:8"]]
+ 005ab254 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ab214 bytes 27b21a94
+ 005ab254 bytes 17b31a94
- 005ab224 ["INT_ADD", "register:40f0:8", ["const:5ab224:8", "const:4:8"]]
- 005ab224 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ab264 ["INT_ADD", "register:40f0:8", ["const:5ab264:8", "const:4:8"]]
+ 005ab264 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ab224 bytes 23b21a94
+ 005ab264 bytes 13b31a94
- 005ab234 ["INT_ADD", "register:40f0:8", ["const:5ab234:8", "const:4:8"]]
- 005ab234 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ab274 ["INT_ADD", "register:40f0:8", ["const:5ab274:8", "const:4:8"]]
+ 005ab274 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ab234 bytes 1fb21a94
+ 005ab274 bytes 0fb31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-716952b8255ae4ddf2585ac093d9ac7b"></a>

### [`005ab268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab268.md) → [`005ab2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab2a8.md) FUN_005ab2a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ab2f0",
      "incomplete_value": false,
      "site": "005ab2f4",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab2b0",
      "incomplete_value": false,
      "site": "005ab2b4",
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
            "const:600:8"
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
      "005ab2f4",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ab2f4",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab268.md#insn-005ab284) · [`005ab294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab268.md#insn-005ab294) · [`005ab2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab268.md#insn-005ab2a4)
- 新版 [`005ab2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab2a8.md#insn-005ab2c4) · [`005ab2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab2a8.md#insn-005ab2d4) · [`005ab2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab2a8.md#insn-005ab2e4)

~~~diff
- 005ab284 ["INT_ADD", "register:40f0:8", ["const:5ab284:8", "const:4:8"]]
- 005ab284 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ab2c4 ["INT_ADD", "register:40f0:8", ["const:5ab2c4:8", "const:4:8"]]
+ 005ab2c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ab284 bytes 0bb21a94
+ 005ab2c4 bytes fbb21a94
- 005ab294 ["INT_ADD", "register:40f0:8", ["const:5ab294:8", "const:4:8"]]
- 005ab294 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ab2d4 ["INT_ADD", "register:40f0:8", ["const:5ab2d4:8", "const:4:8"]]
+ 005ab2d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ab294 bytes 07b21a94
+ 005ab2d4 bytes f7b21a94
- 005ab2a4 ["INT_ADD", "register:40f0:8", ["const:5ab2a4:8", "const:4:8"]]
- 005ab2a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ab2e4 ["INT_ADD", "register:40f0:8", ["const:5ab2e4:8", "const:4:8"]]
+ 005ab2e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ab2a4 bytes 03b21a94
+ 005ab2e4 bytes f3b21a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3674689b454644b34a1437a0b0fdaff"></a>

### [`005ab2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab2d4.md) → [`005ab314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab314.md) FUN_005ab314

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
      "definition_site": "005ab318",
      "incomplete_value": false,
      "site": "005ab31c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab2d8",
      "incomplete_value": false,
      "site": "005ab2dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "005ab31c",
      "DATA",
      [
        "storage",
        "00c6ef00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ab31c",
      "DATA",
      [
        "storage",
        "00c6f300",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab2d4.md#insn-005ab2d4) · [`005ab2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab2d4.md#insn-005ab2d8)
- 新版 [`005ab314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab314.md#insn-005ab314) · [`005ab318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab314.md#insn-005ab318)

~~~diff
- 005ab2d4 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005ab314 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005ab2d4 bytes 083600f0
+ 005ab314 bytes 28360090
- 005ab2d8 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 005ab2d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab2d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab2d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab318 ["COPY", "tmp:0:8", ["const:300:8"]]
+ 005ab318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab2d8 bytes 08013c91
+ 005ab318 bytes 08010c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df0ffce04f4e9a0d072ee37a9a9ae8b3"></a>

### [`005ab2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab2e4.md) → [`005ab324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab324.md) FUN_005ab324

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
      "definition_site": "005ab334",
      "incomplete_value": false,
      "site": "005ab33c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab2f4",
      "incomplete_value": false,
      "site": "005ab2fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "005ab33c",
      "DATA",
      [
        "storage",
        "00c6ef00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ab33c",
      "DATA",
      [
        "storage",
        "00c6f300",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab2e4.md#insn-005ab2f0) · [`005ab2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab2e4.md#insn-005ab2f4) · [`005ab300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab2e4.md#insn-005ab300)
- 新版 [`005ab330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab324.md#insn-005ab330) · [`005ab334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab324.md#insn-005ab334) · [`005ab340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab324.md#insn-005ab340)

~~~diff
- 005ab2f0 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005ab330 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005ab2f0 bytes 083600f0
+ 005ab330 bytes 28360090
- 005ab2f4 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 005ab2f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab2f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab2f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab334 ["COPY", "tmp:0:8", ["const:300:8"]]
+ 005ab334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab2f4 bytes 08013c91
+ 005ab334 bytes 08010c91
- 005ab300 ["INT_ADD", "register:40f0:8", ["const:5ab300:8", "const:4:8"]]
- 005ab300 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005ab340 ["INT_ADD", "register:40f0:8", ["const:5ab340:8", "const:4:8"]]
+ 005ab340 ["CALL", null, ["callee:00c57ea0:8"]]
- 005ab300 bytes e8b11a94
+ 005ab340 bytes d8b21a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7154e21f3ba066055231e797fb598973"></a>

### [`005ab314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab314.md) → [`005ab354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab354.md) FUN_005ab354

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005ab39c",
      "incomplete_value": false,
      "site": "005ab3a0",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab35c",
      "incomplete_value": false,
      "site": "005ab360",
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
            "const:600:8"
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
      "005ab3a0",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ab3a0",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab314.md#insn-005ab330) · [`005ab340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab314.md#insn-005ab340) · [`005ab350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab314.md#insn-005ab350)
- 新版 [`005ab370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab354.md#insn-005ab370) · [`005ab380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab354.md#insn-005ab380) · [`005ab390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab354.md#insn-005ab390)

~~~diff
- 005ab330 ["INT_ADD", "register:40f0:8", ["const:5ab330:8", "const:4:8"]]
- 005ab330 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ab370 ["INT_ADD", "register:40f0:8", ["const:5ab370:8", "const:4:8"]]
+ 005ab370 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ab330 bytes e0b11a94
+ 005ab370 bytes d0b21a94
- 005ab340 ["INT_ADD", "register:40f0:8", ["const:5ab340:8", "const:4:8"]]
- 005ab340 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ab380 ["INT_ADD", "register:40f0:8", ["const:5ab380:8", "const:4:8"]]
+ 005ab380 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ab340 bytes dcb11a94
+ 005ab380 bytes ccb21a94
- 005ab350 ["INT_ADD", "register:40f0:8", ["const:5ab350:8", "const:4:8"]]
- 005ab350 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ab390 ["INT_ADD", "register:40f0:8", ["const:5ab390:8", "const:4:8"]]
+ 005ab390 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ab350 bytes d8b11a94
+ 005ab390 bytes c8b21a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2ea7f37fd88ba2cea7cd10c539c1c76"></a>

### [`005ab388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab388.md) → [`005ab3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab3c8.md) FUN_005ab3c8

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
      "definition_site": "005ab3cc",
      "incomplete_value": false,
      "site": "005ab3d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab38c",
      "incomplete_value": false,
      "site": "005ab390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005ab3d0",
      "DATA",
      [
        "storage",
        "00c6ef50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ab3d0",
      "DATA",
      [
        "storage",
        "00c6f350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab388.md#insn-005ab388) · [`005ab38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab388.md#insn-005ab38c)
- 新版 [`005ab3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab3c8.md#insn-005ab3c8) · [`005ab3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab3c8.md#insn-005ab3cc)

~~~diff
- 005ab388 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005ab3c8 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005ab388 bytes 083600f0
+ 005ab3c8 bytes 28360090
- 005ab38c ["COPY", "tmp:0:8", ["const:f50:8"]]
- 005ab38c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab38c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab38c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab3cc ["COPY", "tmp:0:8", ["const:350:8"]]
+ 005ab3cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab3cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab3cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab38c bytes 08413d91
+ 005ab3cc bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e17ef3f9e68e7c1836204fdc46fb341"></a>

### [`005ab398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab398.md) → [`005ab3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab3d8.md) FUN_005ab3d8

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
      "definition_site": "005ab3e8",
      "incomplete_value": false,
      "site": "005ab3f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab3a8",
      "incomplete_value": false,
      "site": "005ab3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005ab3f0",
      "DATA",
      [
        "storage",
        "00c6ef50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ab3f0",
      "DATA",
      [
        "storage",
        "00c6f350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab398.md#insn-005ab3a4) · [`005ab3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab398.md#insn-005ab3a8) · [`005ab3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab398.md#insn-005ab3b4)
- 新版 [`005ab3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab3d8.md#insn-005ab3e4) · [`005ab3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab3d8.md#insn-005ab3e8) · [`005ab3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab3d8.md#insn-005ab3f4)

~~~diff
- 005ab3a4 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005ab3e4 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005ab3a4 bytes 083600f0
+ 005ab3e4 bytes 28360090
- 005ab3a8 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 005ab3a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab3a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab3a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab3e8 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 005ab3e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab3e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab3e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab3a8 bytes 08413d91
+ 005ab3e8 bytes 08410d91
- 005ab3b4 ["INT_ADD", "register:40f0:8", ["const:5ab3b4:8", "const:4:8"]]
- 005ab3b4 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005ab3f4 ["INT_ADD", "register:40f0:8", ["const:5ab3f4:8", "const:4:8"]]
+ 005ab3f4 ["CALL", null, ["callee:00c57ea0:8"]]
- 005ab3b4 bytes bbb11a94
+ 005ab3f4 bytes abb21a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7c625529f43eeb9b36f63b8eb166db4"></a>

### [`005ab3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab3d0.md) → [`005ab410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab410.md) _INIT_56

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
      "definition_site": "005ab44c",
      "incomplete_value": true,
      "site": "005ab468",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ab40c",
      "incomplete_value": true,
      "site": "005ab428",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ab470",
      "incomplete_value": true,
      "site": "005ab48c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ab430",
      "incomplete_value": true,
      "site": "005ab44c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ab490",
      "incomplete_value": true,
      "site": "005ab4ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ab450",
      "incomplete_value": true,
      "site": "005ab46c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005ab44c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005ab470",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005ab490",
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
      "005ab44c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005ab470",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005ab490",
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

- 旧版 [`005ab448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab3d0.md#insn-005ab448) · [`005ab468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab3d0.md#insn-005ab468) · [`005ab530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab3d0.md#insn-005ab530)
- 新版 [`005ab488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab410.md#insn-005ab488) · [`005ab4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab410.md#insn-005ab4a8) · [`005ab570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab410.md#insn-005ab570)

~~~diff
- 005ab448 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005ab448 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005ab448 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005ab448 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005ab488 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005ab488 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005ab488 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005ab488 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005ab448 bytes 4a093691
+ 005ab488 bytes 4a093791
- 005ab468 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005ab468 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005ab468 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005ab468 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005ab4a8 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005ab4a8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005ab4a8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005ab4a8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005ab468 bytes 4a553a91
+ 005ab4a8 bytes 4a893d91
- 005ab530 ["INT_ADD", "register:40f0:8", ["const:5ab530:8", "const:4:8"]]
- 005ab530 ["CALL", null, ["callee:0043b7f8:8"]]
+ 005ab570 ["INT_ADD", "register:40f0:8", ["const:5ab570:8", "const:4:8"]]
+ 005ab570 ["CALL", null, ["callee:0043b7f8:8"]]
- 005ab530 bytes a240fa97
+ 005ab570 bytes a240fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53bf10250bc0b6b0727c352826930c49"></a>

### [`005ab760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab760.md) → [`005ab7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab7a0.md) FUN_005ab7a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005ab8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab8d4.md) · 呼出先 6件 [`0059b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b89c.md) [`005aa130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005ab914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab914.md) · 呼出先 6件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.70% / 新版 95.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ab7d4",
      "incomplete_value": false,
      "site": "005ab7d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab794",
      "incomplete_value": false,
      "site": "005ab798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
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
      "definition_site": "005ab8d0",
      "incomplete_value": false,
      "site": "005ab8d4",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab890",
      "incomplete_value": false,
      "site": "005ab894",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005ab7d8",
      "DATA",
      [
        "storage",
        "00c6efa0",
        null,
        "pointer"
      ]
    ],
    [
      "005ab8d4",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ab7d8",
      "DATA",
      [
        "storage",
        "00c6f3a0",
        null,
        "pointer"
      ]
    ],
    [
      "005ab8d4",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab760.md#insn-005ab78c) · [`005ab790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab760.md#insn-005ab790) · [`005ab794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab760.md#insn-005ab794)
- 新版 [`005ab7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab7a0.md#insn-005ab7cc) · [`005ab7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab7a0.md#insn-005ab7d0) · [`005ab7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab7a0.md#insn-005ab7d4)

~~~diff
- 005ab78c ["INT_ADD", "register:40f0:8", ["const:5ab78c:8", "const:4:8"]]
- 005ab78c ["CALL", null, ["callee:0059b8dc:8"]]
+ 005ab7cc ["INT_ADD", "register:40f0:8", ["const:5ab7cc:8", "const:4:8"]]
+ 005ab7cc ["CALL", null, ["callee:0059b8dc:8"]]
- 005ab78c bytes 44c0ff97
+ 005ab7cc bytes 44c0ff97
- 005ab790 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005ab7d0 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005ab790 bytes 083600f0
+ 005ab7d0 bytes 28360090
- 005ab794 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 005ab794 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab794 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab794 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab7d4 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 005ab7d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab7d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab7d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab794 bytes 08813e91
+ 005ab7d4 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cde41887f996a0d7774da9e4dcdecc2"></a>

### [`005ab8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab8d4.md) → [`005ab914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab914.md) FUN_005ab914

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005ab760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab760.md) [`009b35fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b35fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005ab7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab7a0.md) [`009b3798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3798.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.76% / 新版 95.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ab970",
      "incomplete_value": true,
      "site": "005ab970",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab930",
      "incomplete_value": true,
      "site": "005ab930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:165:8"
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
      "definition_site": "005abaa8",
      "incomplete_value": true,
      "site": "005abaa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f2d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aba68",
      "incomplete_value": true,
      "site": "005aba68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e60:8"
              ]
            ]
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
      "definition_site": "005abbdc",
      "incomplete_value": true,
      "site": "005abbdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005abb9c",
      "incomplete_value": true,
      "site": "005abb9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:92:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 49,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005ab960",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "005aba94",
      "READ",
      [
        "storage",
        "0029fe60",
        null,
        "string"
      ]
    ],
    [
      "005abbcc",
      "READ",
      [
        "storage",
        "002b9092",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005ab960",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005aba94",
      "READ",
      [
        "storage",
        "0029ff2d",
        null,
        "string"
      ]
    ],
    [
      "005abbcc",
      "READ",
      [
        "storage",
        "002b90d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aba28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab8d4.md#insn-005aba28) · [`005abaa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab8d4.md#insn-005abaa8) · [`005ab91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab8d4.md#insn-005ab91c)
- 新版 [`005aba68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab914.md#insn-005aba68) · [`005abae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab914.md#insn-005abae8) · [`005ab95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab914.md#insn-005ab95c)

~~~diff
- 005aba28 ["INT_ADD", "register:40f0:8", ["const:5aba28:8", "const:4:8"]]
- 005aba28 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005aba68 ["INT_ADD", "register:40f0:8", ["const:5aba68:8", "const:4:8"]]
+ 005aba68 ["CALL", null, ["callee:00c57eb0:8"]]
- 005aba28 bytes 22b01a94
+ 005aba68 bytes 12b11a94
- 005abaa8 ["INT_ADD", "register:40f0:8", ["const:5abaa8:8", "const:4:8"]]
- 005abaa8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005abae8 ["INT_ADD", "register:40f0:8", ["const:5abae8:8", "const:4:8"]]
+ 005abae8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005abaa8 bytes 02b01a94
+ 005abae8 bytes f2b01a94
- 005ab91c ["COPY", "tmp:0:8", ["const:165:8"]]
- 005ab91c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ab91c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ab91c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ab95c ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 005ab95c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ab95c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ab95c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ab91c bytes 29950591
+ 005ab95c bytes 29950691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c71c380700c33a41167f8459a5aa8a2"></a>

### [`005abfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005abfb0.md) → [`005abff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005abff0.md) FUN_005abff0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009b3fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b3fc8.md) · 呼出先 1件 [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md)
- 新版 呼出元 1件 [`009b4164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4164.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)

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
      "definition_site": "005ac018",
      "incomplete_value": false,
      "site": "005ac020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005abfd8",
      "incomplete_value": false,
      "site": "005abfe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
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
      "005ac020",
      "DATA",
      [
        "storage",
        "00c6efc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ac020",
      "DATA",
      [
        "storage",
        "00c6f3c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005abfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005abfb0.md#insn-005abfd0) · [`005abfd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005abfb0.md#insn-005abfd4) · [`005abfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005abfb0.md#insn-005abfd8)
- 新版 [`005ac010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005abff0.md#insn-005ac010) · [`005ac014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005abff0.md#insn-005ac014) · [`005ac018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005abff0.md#insn-005ac018)

~~~diff
- 005abfd0 ["INT_ADD", "register:40f0:8", ["const:5abfd0:8", "const:4:8"]]
- 005abfd0 ["CALL", null, ["callee:0059b908:8"]]
+ 005ac010 ["INT_ADD", "register:40f0:8", ["const:5ac010:8", "const:4:8"]]
+ 005ac010 ["CALL", null, ["callee:0059b908:8"]]
- 005abfd0 bytes 3ebeff97
+ 005ac010 bytes 3ebeff97
- 005abfd4 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005ac014 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005abfd4 bytes 083600f0
+ 005ac014 bytes 083600f0
- 005abfd8 ["COPY", "tmp:0:8", ["const:fc0:8"]]
- 005abfd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005abfd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005abfd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac018 ["COPY", "tmp:0:8", ["const:3c0:8"]]
+ 005ac018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005abfd8 bytes 08013f91
+ 005ac018 bytes 08010f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb6b257baf72e6cf19ad5340abed3388"></a>

### [`005ac014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac014.md) → [`005ac054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac054.md) FUN_005ac054

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.74% / 新版 96.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005ac0b8",
      "incomplete_value": false,
      "site": "005ac0c0",
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
            "const:722:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac078",
      "incomplete_value": false,
      "site": "005ac080",
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
            "const:646:8"
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
      "definition_site": "005ac11c",
      "incomplete_value": false,
      "site": "005ac124",
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
            "const:d94:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac0dc",
      "incomplete_value": false,
      "site": "005ac0e4",
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
            "const:d54:8"
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
      "005ac08c",
      "PARAM",
      [
        "storage",
        "002b0d46",
        null,
        "string"
      ]
    ],
    [
      "005ac0b8",
      "PARAM",
      [
        "storage",
        "002a5646",
        null,
        "string"
      ]
    ],
    [
      "005ac11c",
      "PARAM",
      [
        "storage",
        "002b0d54",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005ac08c",
      "PARAM",
      [
        "storage",
        "002b0d86",
        null,
        "string"
      ]
    ],
    [
      "005ac0b8",
      "PARAM",
      [
        "storage",
        "002a5722",
        null,
        "string"
      ]
    ],
    [
      "005ac11c",
      "PARAM",
      [
        "storage",
        "002b0d94",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac014.md#insn-005ac080) · [`005ac0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac014.md#insn-005ac0e4) · [`005ac124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac014.md#insn-005ac124)
- 新版 [`005ac0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac054.md#insn-005ac0c0) · [`005ac124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac054.md#insn-005ac124) · [`005ac164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac054.md#insn-005ac164)

~~~diff
- 005ac080 ["INT_ADD", "register:40f0:8", ["const:5ac080:8", "const:4:8"]]
- 005ac080 ["CALL", null, ["callee:00c57f70:8"]]
+ 005ac0c0 ["INT_ADD", "register:40f0:8", ["const:5ac0c0:8", "const:4:8"]]
+ 005ac0c0 ["CALL", null, ["callee:00c57f70:8"]]
- 005ac080 bytes bcae1a94
+ 005ac0c0 bytes acaf1a94
- 005ac0e4 ["INT_ADD", "register:40f0:8", ["const:5ac0e4:8", "const:4:8"]]
- 005ac0e4 ["CALL", null, ["callee:00c57f70:8"]]
+ 005ac124 ["INT_ADD", "register:40f0:8", ["const:5ac124:8", "const:4:8"]]
+ 005ac124 ["CALL", null, ["callee:00c57f70:8"]]
- 005ac0e4 bytes a3ae1a94
+ 005ac124 bytes 93af1a94
- 005ac124 ["INT_ADD", "register:40f0:8", ["const:5ac124:8", "const:4:8"]]
- 005ac124 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ac164 ["INT_ADD", "register:40f0:8", ["const:5ac164:8", "const:4:8"]]
+ 005ac164 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ac124 bytes 63ae1a94
+ 005ac164 bytes 53af1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66f6f71688a51c92f4e5dbbc65eb2b9d"></a>

### [`005ac35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac35c.md) → [`005ac39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac39c.md) FUN_005ac39c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ac3b8",
      "incomplete_value": false,
      "site": "005ac3c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac378",
      "incomplete_value": false,
      "site": "005ac380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:c8:8"
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
      "definition_site": "005ac3d0",
      "incomplete_value": false,
      "site": "005ac3d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac390",
      "incomplete_value": false,
      "site": "005ac390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "005ac3c0",
      "DATA",
      [
        "storage",
        "00c6f0c8",
        null,
        "undefined *"
      ]
    ],
    [
      "005ac3d0",
      "DATA",
      [
        "storage",
        "00c6f018",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005ac3c0",
      "DATA",
      [
        "storage",
        "00c6f4c8",
        null,
        "undefined *"
      ]
    ],
    [
      "005ac3d0",
      "DATA",
      [
        "storage",
        "00c6f418",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac35c.md#insn-005ac370) · [`005ac378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac35c.md#insn-005ac378) · [`005ac384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac35c.md#insn-005ac384)
- 新版 [`005ac3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac39c.md#insn-005ac3b0) · [`005ac3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac39c.md#insn-005ac3b8)

~~~diff
- 005ac370 ["INT_ADD", "register:40f0:8", ["const:5ac370:8", "const:4:8"]]
- 005ac370 ["CALL", null, ["callee:00c57e90:8"]]
+ 005ac3b0 ["INT_ADD", "register:40f0:8", ["const:5ac3b0:8", "const:4:8"]]
+ 005ac3b0 ["CALL", null, ["callee:00c57e90:8"]]
- 005ac370 bytes c8ad1a94
+ 005ac3b0 bytes b8ae1a94
- 005ac378 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 005ac378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac3b8 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 005ac3b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac3b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac3b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac378 bytes 08210391
+ 005ac3b8 bytes 08211391
- 005ac384 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005ac384 bytes 083600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bb39fc1b7949a1b5cbb3f374eed3c0a"></a>

### [`005ac3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac3a4.md) → [`005ac3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac3e4.md) FUN_005ac3e4

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
      "definition_site": "005ac410",
      "incomplete_value": false,
      "site": "005ac414",
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
      "definition_site": "005ac3d0",
      "incomplete_value": false,
      "site": "005ac3d4",
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
      "005ac414",
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
      "005ac414",
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

- 旧版 [`005ac3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac3a4.md#insn-005ac3c0) · [`005ac3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac3a4.md#insn-005ac3c8) · [`005ac3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac3a4.md#insn-005ac3e0)
- 新版 [`005ac400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac3e4.md#insn-005ac400) · [`005ac408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac3e4.md#insn-005ac408) · [`005ac420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac3e4.md#insn-005ac420)

~~~diff
- 005ac3c0 ["INT_ADD", "register:40f0:8", ["const:5ac3c0:8", "const:4:8"]]
- 005ac3c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ac400 ["INT_ADD", "register:40f0:8", ["const:5ac400:8", "const:4:8"]]
+ 005ac400 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ac3c0 bytes bcad1a94
+ 005ac400 bytes acae1a94
- 005ac3c8 ["COPY", "tmp:0:8", ["const:610:8"]]
- 005ac3c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac3c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac3c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac408 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 005ac408 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac408 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac3c8 bytes 08411891
+ 005ac408 bytes 08412891
- 005ac3e0 ["INT_ADD", "register:40f0:8", ["const:5ac3e0:8", "const:4:8"]]
- 005ac3e0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ac420 ["INT_ADD", "register:40f0:8", ["const:5ac420:8", "const:4:8"]]
+ 005ac420 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ac3e0 bytes b4ad1a94
+ 005ac420 bytes a4ae1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f88a259cafaae886e44ad3f768fcfec"></a>

### [`005ac468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac468.md) → [`005ac4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac4a8.md) FUN_005ac4a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005ac4f0",
      "incomplete_value": false,
      "site": "005ac4f4",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac4b0",
      "incomplete_value": false,
      "site": "005ac4b4",
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
            "const:600:8"
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
      "005ac4f4",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac4f4",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac468.md#insn-005ac484) · [`005ac494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac468.md#insn-005ac494) · [`005ac4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac468.md#insn-005ac4a4)
- 新版 [`005ac4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac4a8.md#insn-005ac4c4) · [`005ac4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac4a8.md#insn-005ac4d4) · [`005ac4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac4a8.md#insn-005ac4e4)

~~~diff
- 005ac484 ["INT_ADD", "register:40f0:8", ["const:5ac484:8", "const:4:8"]]
- 005ac484 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ac4c4 ["INT_ADD", "register:40f0:8", ["const:5ac4c4:8", "const:4:8"]]
+ 005ac4c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ac484 bytes 8bad1a94
+ 005ac4c4 bytes 7bae1a94
- 005ac494 ["INT_ADD", "register:40f0:8", ["const:5ac494:8", "const:4:8"]]
- 005ac494 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ac4d4 ["INT_ADD", "register:40f0:8", ["const:5ac4d4:8", "const:4:8"]]
+ 005ac4d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ac494 bytes 87ad1a94
+ 005ac4d4 bytes 77ae1a94
- 005ac4a4 ["INT_ADD", "register:40f0:8", ["const:5ac4a4:8", "const:4:8"]]
- 005ac4a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ac4e4 ["INT_ADD", "register:40f0:8", ["const:5ac4e4:8", "const:4:8"]]
+ 005ac4e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ac4a4 bytes 83ad1a94
+ 005ac4e4 bytes 73ae1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-743cfadf6d922434943050ff472e7360"></a>

### [`005ac4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac4d8.md) → [`005ac518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac518.md) FUN_005ac518

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ac560",
      "incomplete_value": false,
      "site": "005ac564",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac520",
      "incomplete_value": false,
      "site": "005ac524",
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
            "const:600:8"
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
      "005ac564",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac564",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac4d8.md#insn-005ac4f4) · [`005ac504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac4d8.md#insn-005ac504) · [`005ac514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac4d8.md#insn-005ac514)
- 新版 [`005ac534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac518.md#insn-005ac534) · [`005ac544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac518.md#insn-005ac544) · [`005ac554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac518.md#insn-005ac554)

~~~diff
- 005ac4f4 ["INT_ADD", "register:40f0:8", ["const:5ac4f4:8", "const:4:8"]]
- 005ac4f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ac534 ["INT_ADD", "register:40f0:8", ["const:5ac534:8", "const:4:8"]]
+ 005ac534 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ac4f4 bytes 6fad1a94
+ 005ac534 bytes 5fae1a94
- 005ac504 ["INT_ADD", "register:40f0:8", ["const:5ac504:8", "const:4:8"]]
- 005ac504 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ac544 ["INT_ADD", "register:40f0:8", ["const:5ac544:8", "const:4:8"]]
+ 005ac544 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ac504 bytes 6bad1a94
+ 005ac544 bytes 5bae1a94
- 005ac514 ["INT_ADD", "register:40f0:8", ["const:5ac514:8", "const:4:8"]]
- 005ac514 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ac554 ["INT_ADD", "register:40f0:8", ["const:5ac554:8", "const:4:8"]]
+ 005ac554 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ac514 bytes 67ad1a94
+ 005ac554 bytes 57ae1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e738ab6b8622959be9c9b7c59fa60325"></a>

### [`005ac544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac544.md) → [`005ac584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac584.md) FUN_005ac584

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
      "definition_site": "005ac588",
      "incomplete_value": false,
      "site": "005ac58c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac548",
      "incomplete_value": false,
      "site": "005ac54c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "005ac58c",
      "DATA",
      [
        "storage",
        "00c6f078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ac58c",
      "DATA",
      [
        "storage",
        "00c6f478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac544.md#insn-005ac548)
- 新版 [`005ac588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac584.md#insn-005ac588)

~~~diff
- 005ac548 ["COPY", "tmp:0:8", ["const:78:8"]]
- 005ac548 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac548 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac548 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac588 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 005ac588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac548 bytes 08e10191
+ 005ac588 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8ca12bc9ee8d99e61f3e83383e56246"></a>

### [`005ac554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac554.md) → [`005ac594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac594.md) FUN_005ac594

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
      "definition_site": "005ac5a4",
      "incomplete_value": false,
      "site": "005ac5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac564",
      "incomplete_value": false,
      "site": "005ac56c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "005ac5ac",
      "DATA",
      [
        "storage",
        "00c6f078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ac5ac",
      "DATA",
      [
        "storage",
        "00c6f478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac554.md#insn-005ac564) · [`005ac570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac554.md#insn-005ac570)
- 新版 [`005ac5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac594.md#insn-005ac5a4) · [`005ac5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac594.md#insn-005ac5b0)

~~~diff
- 005ac564 ["COPY", "tmp:0:8", ["const:78:8"]]
- 005ac564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac5a4 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 005ac5a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac5a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac5a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac564 bytes 08e10191
+ 005ac5a4 bytes 08e11191
- 005ac570 ["INT_ADD", "register:40f0:8", ["const:5ac570:8", "const:4:8"]]
- 005ac570 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005ac5b0 ["INT_ADD", "register:40f0:8", ["const:5ac5b0:8", "const:4:8"]]
+ 005ac5b0 ["CALL", null, ["callee:00c57ea0:8"]]
- 005ac570 bytes 4cad1a94
+ 005ac5b0 bytes 3cae1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fadfa502f89eefb2ffdcf63f5f182057"></a>

### [`005ac584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac584.md) → [`005ac5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac5c4.md) FUN_005ac5c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005ac60c",
      "incomplete_value": false,
      "site": "005ac610",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac5cc",
      "incomplete_value": false,
      "site": "005ac5d0",
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
            "const:600:8"
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
      "005ac610",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac610",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac584.md#insn-005ac5a0) · [`005ac5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac584.md#insn-005ac5b0) · [`005ac5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac584.md#insn-005ac5c0)
- 新版 [`005ac5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac5c4.md#insn-005ac5e0) · [`005ac5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac5c4.md#insn-005ac5f0) · [`005ac600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac5c4.md#insn-005ac600)

~~~diff
- 005ac5a0 ["INT_ADD", "register:40f0:8", ["const:5ac5a0:8", "const:4:8"]]
- 005ac5a0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ac5e0 ["INT_ADD", "register:40f0:8", ["const:5ac5e0:8", "const:4:8"]]
+ 005ac5e0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ac5a0 bytes 44ad1a94
+ 005ac5e0 bytes 34ae1a94
- 005ac5b0 ["INT_ADD", "register:40f0:8", ["const:5ac5b0:8", "const:4:8"]]
- 005ac5b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ac5f0 ["INT_ADD", "register:40f0:8", ["const:5ac5f0:8", "const:4:8"]]
+ 005ac5f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ac5b0 bytes 40ad1a94
+ 005ac5f0 bytes 30ae1a94
- 005ac5c0 ["INT_ADD", "register:40f0:8", ["const:5ac5c0:8", "const:4:8"]]
- 005ac5c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ac600 ["INT_ADD", "register:40f0:8", ["const:5ac600:8", "const:4:8"]]
+ 005ac600 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ac5c0 bytes 3cad1a94
+ 005ac600 bytes 2cae1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57db6a6d028e78c89dbf6cbfec11f624"></a>

### [`005ac5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac5f8.md) → [`005ac638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac638.md) FUN_005ac638

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
      "definition_site": "005ac63c",
      "incomplete_value": false,
      "site": "005ac640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac5fc",
      "incomplete_value": false,
      "site": "005ac600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
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
      "005ac640",
      "DATA",
      [
        "storage",
        "00c6f0c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ac640",
      "DATA",
      [
        "storage",
        "00c6f4c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac5f8.md#insn-005ac5fc)
- 新版 [`005ac63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac638.md#insn-005ac63c)

~~~diff
- 005ac5fc ["COPY", "tmp:0:8", ["const:c8:8"]]
- 005ac5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac63c ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 005ac63c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac63c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac63c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac5fc bytes 08210391
+ 005ac63c bytes 08211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6609783752f99a53d3aeb33e22fca76c"></a>

### [`005ac608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac608.md) → [`005ac648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac648.md) FUN_005ac648

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
      "definition_site": "005ac658",
      "incomplete_value": false,
      "site": "005ac660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac618",
      "incomplete_value": false,
      "site": "005ac620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
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
      "005ac660",
      "DATA",
      [
        "storage",
        "00c6f0c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ac660",
      "DATA",
      [
        "storage",
        "00c6f4c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac608.md#insn-005ac618) · [`005ac624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac608.md#insn-005ac624)
- 新版 [`005ac658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac648.md#insn-005ac658) · [`005ac664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac648.md#insn-005ac664)

~~~diff
- 005ac618 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 005ac618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac658 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 005ac658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac618 bytes 08210391
+ 005ac658 bytes 08211391
- 005ac624 ["INT_ADD", "register:40f0:8", ["const:5ac624:8", "const:4:8"]]
- 005ac624 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005ac664 ["INT_ADD", "register:40f0:8", ["const:5ac664:8", "const:4:8"]]
+ 005ac664 ["CALL", null, ["callee:00c57ea0:8"]]
- 005ac624 bytes 1fad1a94
+ 005ac664 bytes 0fae1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44e16db4408fb88c2cbbd219e6cf510e"></a>

### [`005ac640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac640.md) → [`005ac680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac680.md) _INIT_57

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
      "definition_site": "005ac6bc",
      "incomplete_value": true,
      "site": "005ac6d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ac67c",
      "incomplete_value": true,
      "site": "005ac698",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ac700",
      "incomplete_value": true,
      "site": "005ac71c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ac6c0",
      "incomplete_value": true,
      "site": "005ac6dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005ac8a0",
      "incomplete_value": false,
      "site": "005ac8b4",
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
      "definition_site": "005ac860",
      "incomplete_value": false,
      "site": "005ac874",
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
      "005ac6bc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005ac6e0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005ac700",
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
      "005ac6bc",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005ac6e0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005ac700",
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

- 旧版 [`005ac6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac640.md#insn-005ac6d8) · [`005ac874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac640.md#insn-005ac874) · [`005ac66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac640.md#insn-005ac66c)
- 新版 [`005ac718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac680.md#insn-005ac718) · [`005ac8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac680.md#insn-005ac8b4) · [`005ac6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac680.md#insn-005ac6ac)

~~~diff
- 005ac6d8 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005ac6d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005ac6d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005ac6d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005ac718 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005ac718 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005ac718 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005ac718 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005ac6d8 bytes 4a553a91
+ 005ac718 bytes 4a893d91
- 005ac874 ["INT_ADD", "register:40f0:8", ["const:5ac874:8", "const:4:8"]]
- 005ac874 ["CALL", null, ["callee:00c57e30:8"]]
+ 005ac8b4 ["INT_ADD", "register:40f0:8", ["const:5ac8b4:8", "const:4:8"]]
+ 005ac8b4 ["CALL", null, ["callee:00c57e30:8"]]
- 005ac874 bytes 6fac1a94
+ 005ac8b4 bytes 5fad1a94
- 005ac66c ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 005ac66c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005ac66c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005ac66c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005ac6ac ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 005ac6ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005ac6ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005ac6ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005ac66c bytes 73820f91
+ 005ac6ac bytes 73821f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d8f17c5e37fdf18e85752f516a4b8a1"></a>

### [`005ac9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac9d0.md) → [`005aca10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca10.md) FUN_005aca10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b8a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8a24.md) · 呼出先 1件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md)
- 新版 呼出元 1件 [`005b8a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8a64.md) · 呼出先 1件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md)

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
      "definition_site": "005aca28",
      "incomplete_value": false,
      "site": "005aca30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac9e8",
      "incomplete_value": false,
      "site": "005ac9f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:118:8"
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
      "005aca30",
      "DATA",
      [
        "storage",
        "00c6f118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005aca30",
      "DATA",
      [
        "storage",
        "00c6f518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac9d0.md#insn-005ac9e0) · [`005ac9e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac9d0.md#insn-005ac9e8)
- 新版 [`005aca20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca10.md#insn-005aca20) · [`005aca28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca10.md#insn-005aca28)

~~~diff
- 005ac9e0 ["INT_ADD", "register:40f0:8", ["const:5ac9e0:8", "const:4:8"]]
- 005ac9e0 ["CALL", null, ["callee:00597ed0:8"]]
+ 005aca20 ["INT_ADD", "register:40f0:8", ["const:5aca20:8", "const:4:8"]]
+ 005aca20 ["CALL", null, ["callee:00597ed0:8"]]
- 005ac9e0 bytes 2cadff97
+ 005aca20 bytes 2cadff97
- 005ac9e8 ["COPY", "tmp:0:8", ["const:118:8"]]
- 005ac9e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac9e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac9e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aca28 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 005aca28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aca28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aca28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac9e8 bytes 08610491
+ 005aca28 bytes 08611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1471145278bd4f5921aa26ce8642da41"></a>

### [`005aca04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005aca04.md) → [`005aca44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md) FUN_005aca44

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00597ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597ebc.md) [`0059a458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a458.md) [`005ace40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ace40.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00597efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md) [`0059a498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a498.md) [`005ace80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ace80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005acc50",
      "incomplete_value": false,
      "site": "005acc58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005acc10",
      "incomplete_value": false,
      "site": "005acc18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "005acc58",
      "DATA",
      [
        "storage",
        "00c6f160",
        null,
        "undefined *"
      ]
    ],
    [
      "005acce0",
      "READ",
      [
        "storage",
        "00c6f188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005acc58",
      "DATA",
      [
        "storage",
        "00c6f560",
        null,
        "undefined *"
      ]
    ],
    [
      "005acce0",
      "READ",
      [
        "storage",
        "00c6f588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aca30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005aca04.md#insn-005aca30) · [`005aca50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005aca04.md#insn-005aca50) · [`005aca64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005aca04.md#insn-005aca64)
- 新版 [`005aca70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md#insn-005aca70) · [`005aca90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md#insn-005aca90) · [`005acaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md#insn-005acaa4)

~~~diff
- 005aca30 ["INT_ADD", "register:40f0:8", ["const:5aca30:8", "const:4:8"]]
- 005aca30 ["CALL", null, ["callee:00597efc:8"]]
+ 005aca70 ["INT_ADD", "register:40f0:8", ["const:5aca70:8", "const:4:8"]]
+ 005aca70 ["CALL", null, ["callee:00597efc:8"]]
- 005aca30 bytes 23adff97
+ 005aca70 bytes 23adff97
- 005aca50 ["INT_ADD", "register:40f0:8", ["const:5aca50:8", "const:4:8"]]
- 005aca50 ["CALL", null, ["callee:00c53d00:8"]]
+ 005aca90 ["INT_ADD", "register:40f0:8", ["const:5aca90:8", "const:4:8"]]
+ 005aca90 ["CALL", null, ["callee:00c53d00:8"]]
- 005aca50 bytes a49b1a94
+ 005aca90 bytes 9c9c1a94
- 005aca64 ["COPY", "register:0:8", ["register:4040:8"]]
- 005aca64 ["INT_ADD", "register:40f0:8", ["const:5aca64:8", "const:4:8"]]
- 005aca64 ["CALLIND", null, ["register:0:8"]]
+ 005acaa4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005acaa4 ["INT_ADD", "register:40f0:8", ["const:5acaa4:8", "const:4:8"]]
+ 005acaa4 ["CALLIND", null, ["register:0:8"]]
- 005aca64 bytes 00013fd6
+ 005acaa4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-826b655bf17d1a076339de182da30e08"></a>

### [`005ace80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ace80.md) → [`005acec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005acec0.md) FUN_005acec0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00597ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597ebc.md) [`005ae844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae844.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00597efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md) [`005ae884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae884.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ad084",
      "incomplete_value": false,
      "site": "005ad08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad044",
      "incomplete_value": false,
      "site": "005ad04c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "005ad08c",
      "DATA",
      [
        "storage",
        "00c6f1e0",
        null,
        "undefined *"
      ]
    ],
    [
      "005ad10c",
      "READ",
      [
        "storage",
        "00c6f208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad08c",
      "DATA",
      [
        "storage",
        "00c6f5e0",
        null,
        "undefined *"
      ]
    ],
    [
      "005ad10c",
      "READ",
      [
        "storage",
        "00c6f608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aceb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ace80.md#insn-005aceb0) · [`005aced0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ace80.md#insn-005aced0) · [`005acee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ace80.md#insn-005acee4)
- 新版 [`005acef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005acec0.md#insn-005acef0) · [`005acf10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005acec0.md#insn-005acf10) · [`005acf24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005acec0.md#insn-005acf24)

~~~diff
- 005aceb0 ["INT_ADD", "register:40f0:8", ["const:5aceb0:8", "const:4:8"]]
- 005aceb0 ["CALL", null, ["callee:00597efc:8"]]
+ 005acef0 ["INT_ADD", "register:40f0:8", ["const:5acef0:8", "const:4:8"]]
+ 005acef0 ["CALL", null, ["callee:00597efc:8"]]
- 005aceb0 bytes 03acff97
+ 005acef0 bytes 03acff97
- 005aced0 ["INT_ADD", "register:40f0:8", ["const:5aced0:8", "const:4:8"]]
- 005aced0 ["CALL", null, ["callee:00c53d00:8"]]
+ 005acf10 ["INT_ADD", "register:40f0:8", ["const:5acf10:8", "const:4:8"]]
+ 005acf10 ["CALL", null, ["callee:00c53d00:8"]]
- 005aced0 bytes 849a1a94
+ 005acf10 bytes 7c9b1a94
- 005acee4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005acee4 ["INT_ADD", "register:40f0:8", ["const:5acee4:8", "const:4:8"]]
- 005acee4 ["CALLIND", null, ["register:0:8"]]
+ 005acf24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005acf24 ["INT_ADD", "register:40f0:8", ["const:5acf24:8", "const:4:8"]]
+ 005acf24 ["CALLIND", null, ["register:0:8"]]
- 005acee4 bytes 00013fd6
+ 005acf24 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b4f8e0b5543591e243734705cf95d92"></a>

### [`005ad444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad444.md) → [`005ad484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad484.md) FUN_005ad484

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00599e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599e14.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00599e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e54.md)

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
      "definition_site": "005ad49c",
      "incomplete_value": false,
      "site": "005ad4a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad45c",
      "incomplete_value": false,
      "site": "005ad468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:118:8"
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
      "005ad4a8",
      "DATA",
      [
        "storage",
        "00c6f118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad4a8",
      "DATA",
      [
        "storage",
        "00c6f518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ad45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad444.md#insn-005ad45c) · [`005ad48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad444.md#insn-005ad48c) · [`005ad4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad444.md#insn-005ad4bc)
- 新版 [`005ad49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad484.md#insn-005ad49c) · [`005ad4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad484.md#insn-005ad4cc) · [`005ad4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad484.md#insn-005ad4fc)

~~~diff
- 005ad45c ["COPY", "tmp:0:8", ["const:118:8"]]
- 005ad45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ad45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ad45c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ad49c ["COPY", "tmp:0:8", ["const:518:8"]]
+ 005ad49c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ad49c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ad49c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ad45c bytes 08610491
+ 005ad49c bytes 08611491
- 005ad48c ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad48c ["INT_ADD", "register:40f0:8", ["const:5ad48c:8", "const:4:8"]]
- 005ad48c ["CALLIND", null, ["register:0:8"]]
+ 005ad4cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad4cc ["INT_ADD", "register:40f0:8", ["const:5ad4cc:8", "const:4:8"]]
+ 005ad4cc ["CALLIND", null, ["register:0:8"]]
- 005ad48c bytes 00013fd6
+ 005ad4cc bytes 00013fd6
- 005ad4bc ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad4bc ["INT_ADD", "register:40f0:8", ["const:5ad4bc:8", "const:4:8"]]
- 005ad4bc ["CALLIND", null, ["register:0:8"]]
+ 005ad4fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad4fc ["INT_ADD", "register:40f0:8", ["const:5ad4fc:8", "const:4:8"]]
+ 005ad4fc ["CALLIND", null, ["register:0:8"]]
- 005ad4bc bytes 00013fd6
+ 005ad4fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ac92c928bdb2513566d48007a3f6555"></a>

### [`005ad4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad4d0.md) → [`005ad510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad510.md) FUN_005ad510

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00599e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599e14.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00599e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e54.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ad528",
      "incomplete_value": false,
      "site": "005ad534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad4e8",
      "incomplete_value": false,
      "site": "005ad4f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:118:8"
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
      "005ad534",
      "DATA",
      [
        "storage",
        "00c6f118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad534",
      "DATA",
      [
        "storage",
        "00c6f518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ad4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad4d0.md#insn-005ad4e8) · [`005ad518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad4d0.md#insn-005ad518) · [`005ad548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad4d0.md#insn-005ad548)
- 新版 [`005ad528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad510.md#insn-005ad528) · [`005ad558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad510.md#insn-005ad558) · [`005ad588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad510.md#insn-005ad588)

~~~diff
- 005ad4e8 ["COPY", "tmp:0:8", ["const:118:8"]]
- 005ad4e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ad4e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ad4e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ad528 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 005ad528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ad528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ad528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ad4e8 bytes 08610491
+ 005ad528 bytes 08611491
- 005ad518 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad518 ["INT_ADD", "register:40f0:8", ["const:5ad518:8", "const:4:8"]]
- 005ad518 ["CALLIND", null, ["register:0:8"]]
+ 005ad558 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad558 ["INT_ADD", "register:40f0:8", ["const:5ad558:8", "const:4:8"]]
+ 005ad558 ["CALLIND", null, ["register:0:8"]]
- 005ad518 bytes 00013fd6
+ 005ad558 bytes 00013fd6
- 005ad548 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad548 ["INT_ADD", "register:40f0:8", ["const:5ad548:8", "const:4:8"]]
- 005ad548 ["CALLIND", null, ["register:0:8"]]
+ 005ad588 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad588 ["INT_ADD", "register:40f0:8", ["const:5ad588:8", "const:4:8"]]
+ 005ad588 ["CALLIND", null, ["register:0:8"]]
- 005ad548 bytes 00013fd6
+ 005ad588 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ac8bc0011de1148af2d617b7974ef74"></a>

### [`005ad564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad564.md) → [`005ad5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5a4.md) FUN_005ad5a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005ad5bc",
      "incomplete_value": false,
      "site": "005ad5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad57c",
      "incomplete_value": false,
      "site": "005ad580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "005ad5c0",
      "DATA",
      [
        "storage",
        "00c6f160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad5c0",
      "DATA",
      [
        "storage",
        "00c6f560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ad57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad564.md#insn-005ad57c) · [`005ad58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad564.md#insn-005ad58c)
- 新版 [`005ad5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5a4.md#insn-005ad5bc) · [`005ad5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5a4.md#insn-005ad5cc)

~~~diff
- 005ad57c ["COPY", "tmp:0:8", ["const:160:8"]]
- 005ad57c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ad57c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ad57c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ad5bc ["COPY", "tmp:0:8", ["const:560:8"]]
+ 005ad5bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad5bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad5bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ad57c bytes 29810591
+ 005ad5bc bytes 29811591
- 005ad58c ["INT_ADD", "register:40f0:8", ["const:5ad58c:8", "const:4:8"]]
- 005ad58c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ad5cc ["INT_ADD", "register:40f0:8", ["const:5ad5cc:8", "const:4:8"]]
+ 005ad5cc ["CALL", null, ["callee:00c57eb0:8"]]
- 005ad58c bytes 49a91a94
+ 005ad5cc bytes 39aa1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ce69af71912197a36d66489b60b1120"></a>

### [`005ad5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad5b0.md) → [`005ad5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5f0.md) FUN_005ad5f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005ad608",
      "incomplete_value": false,
      "site": "005ad60c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad5c8",
      "incomplete_value": false,
      "site": "005ad5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "005ad60c",
      "DATA",
      [
        "storage",
        "00c6f160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad60c",
      "DATA",
      [
        "storage",
        "00c6f560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ad5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad5b0.md#insn-005ad5c8) · [`005ad5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad5b0.md#insn-005ad5d8) · [`005ad5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad5b0.md#insn-005ad5e4)
- 新版 [`005ad608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5f0.md#insn-005ad608) · [`005ad618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5f0.md#insn-005ad618) · [`005ad624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5f0.md#insn-005ad624)

~~~diff
- 005ad5c8 ["COPY", "tmp:0:8", ["const:160:8"]]
- 005ad5c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ad5c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ad5c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ad608 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 005ad608 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad608 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad608 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ad5c8 bytes 29810591
+ 005ad608 bytes 29811591
- 005ad5d8 ["INT_ADD", "register:40f0:8", ["const:5ad5d8:8", "const:4:8"]]
- 005ad5d8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ad618 ["INT_ADD", "register:40f0:8", ["const:5ad618:8", "const:4:8"]]
+ 005ad618 ["CALL", null, ["callee:00c57eb0:8"]]
- 005ad5d8 bytes 36a91a94
+ 005ad618 bytes 26aa1a94
- 005ad5e4 ["INT_ADD", "register:40f0:8", ["const:5ad5e4:8", "const:4:8"]]
- 005ad5e4 ["CALL", null, ["callee:00c57e80:8"]]
+ 005ad624 ["INT_ADD", "register:40f0:8", ["const:5ad624:8", "const:4:8"]]
+ 005ad624 ["CALL", null, ["callee:00c57e80:8"]]
- 005ad5e4 bytes 27a91a94
+ 005ad624 bytes 17aa1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f53130db4e305954af3b99649bca6b45"></a>

### [`005ad5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad5f8.md) → [`005ad638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad638.md) FUN_005ad638

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005ad660",
      "incomplete_value": false,
      "site": "005ad660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad620",
      "incomplete_value": false,
      "site": "005ad620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "005ad660",
      "DATA",
      [
        "storage",
        "00c6f160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad660",
      "DATA",
      [
        "storage",
        "00c6f560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ad660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad5f8.md#insn-005ad660) · [`005ad60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad5f8.md#insn-005ad60c) · [`005ad61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad5f8.md#insn-005ad61c)
- 新版 [`005ad6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad638.md#insn-005ad6a0) · [`005ad64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad638.md#insn-005ad64c) · [`005ad65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad638.md#insn-005ad65c)

~~~diff
- 005ad660 ["INT_ADD", "register:40f0:8", ["const:5ad660:8", "const:4:8"]]
- 005ad660 ["CALL", null, ["callee:0043bb20:8"]]
+ 005ad6a0 ["INT_ADD", "register:40f0:8", ["const:5ad6a0:8", "const:4:8"]]
+ 005ad6a0 ["CALL", null, ["callee:0043bb20:8"]]
- 005ad660 bytes 2039fa97
+ 005ad6a0 bytes 2039fa97
- 005ad60c ["INT_ADD", "register:40f0:8", ["const:5ad60c:8", "const:4:8"]]
- 005ad60c ["CALL", null, ["callee:00c57e90:8"]]
+ 005ad64c ["INT_ADD", "register:40f0:8", ["const:5ad64c:8", "const:4:8"]]
+ 005ad64c ["CALL", null, ["callee:00c57e90:8"]]
- 005ad60c bytes 21a91a94
+ 005ad64c bytes 11aa1a94
- 005ad61c ["COPY", "tmp:0:8", ["const:160:8"]]
- 005ad61c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ad61c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ad61c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ad65c ["COPY", "tmp:0:8", ["const:560:8"]]
+ 005ad65c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad65c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad65c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ad61c bytes 29810591
+ 005ad65c bytes 29811591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec05d5292ef5781efc46af8028b1f472"></a>

### [`005ad698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad698.md) → [`005ad6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad6d8.md) FUN_005ad6d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "005ad6f8",
      "incomplete_value": false,
      "site": "005ad6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad6b8",
      "incomplete_value": false,
      "site": "005ad6b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "005ad6f8",
      "DATA",
      [
        "storage",
        "00c6f160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad6f8",
      "DATA",
      [
        "storage",
        "00c6f560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ad6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad698.md#insn-005ad6f8) · [`005ad6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad698.md#insn-005ad6b4) · [`005ad6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad698.md#insn-005ad6cc)
- 新版 [`005ad738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad6d8.md#insn-005ad738) · [`005ad6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad6d8.md#insn-005ad6f4) · [`005ad70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad6d8.md#insn-005ad70c)

~~~diff
- 005ad6f8 ["INT_ADD", "register:40f0:8", ["const:5ad6f8:8", "const:4:8"]]
- 005ad6f8 ["CALL", null, ["callee:0043bb20:8"]]
+ 005ad738 ["INT_ADD", "register:40f0:8", ["const:5ad738:8", "const:4:8"]]
+ 005ad738 ["CALL", null, ["callee:0043bb20:8"]]
- 005ad6f8 bytes fa38fa97
+ 005ad738 bytes fa38fa97
- 005ad6b4 ["COPY", "tmp:0:8", ["const:160:8"]]
- 005ad6b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ad6b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ad6b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ad6f4 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 005ad6f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad6f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad6f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ad6b4 bytes 29810591
+ 005ad6f4 bytes 29811591
- 005ad6cc ["INT_ADD", "register:40f0:8", ["const:5ad6cc:8", "const:4:8"]]
- 005ad6cc ["CALL", null, ["callee:00c53cd0:8"]]
+ 005ad70c ["INT_ADD", "register:40f0:8", ["const:5ad70c:8", "const:4:8"]]
+ 005ad70c ["CALL", null, ["callee:00c53cd0:8"]]
- 005ad6cc bytes 79981a94
+ 005ad70c bytes 71991a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a64180bce7e4c5a36818f4fe234c5ef1"></a>

### [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) → [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) FUN_005ad7e0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 27件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`00450140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md) [`00450710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`00450180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md) [`00450750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.53% / 新版 96.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ad8e4",
      "incomplete_value": true,
      "site": "005ad8e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:90e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad8a4",
      "incomplete_value": true,
      "site": "005ad8a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8ce:8"
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
      "definition_site": "005add90",
      "incomplete_value": true,
      "site": "005add90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:756:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005add50",
      "incomplete_value": true,
      "site": "005add50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:716:8"
              ]
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
    "kind": "store_value",
    "new": {
      "definition_site": "005add84",
      "incomplete_value": true,
      "site": "005add94",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005add44",
      "incomplete_value": true,
      "site": "005add54",
      "value": [
        "LOAD",
        "8",
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
      "005ad8d0",
      "READ",
      [
        "storage",
        "002b38ce",
        null,
        "string"
      ]
    ],
    [
      "005ad998",
      "READ",
      [
        "storage",
        "002b1953",
        null,
        "string"
      ]
    ],
    [
      "005adce0",
      "PARAM",
      [
        "storage",
        "002a8a0c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005ad8d0",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ],
    [
      "005ad998",
      "READ",
      [
        "storage",
        "002b1993",
        null,
        "string"
      ]
    ],
    [
      "005adce0",
      "PARAM",
      [
        "storage",
        "002a8ad9",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005adca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md#insn-005adca8) · [`005add14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md#insn-005add14) · [`005add6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md#insn-005add6c)
- 新版 [`005adce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md#insn-005adce8) · [`005add54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md#insn-005add54) · [`005addac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md#insn-005addac)

~~~diff
- 005adca8 ["INT_ADD", "register:40f0:8", ["const:5adca8:8", "const:4:8"]]
- 005adca8 ["CALL", null, ["callee:00c57f70:8"]]
+ 005adce8 ["INT_ADD", "register:40f0:8", ["const:5adce8:8", "const:4:8"]]
+ 005adce8 ["CALL", null, ["callee:00c57f70:8"]]
- 005adca8 bytes b2a71a94
+ 005adce8 bytes a2a81a94
- 005add14 ["INT_ADD", "register:40f0:8", ["const:5add14:8", "const:4:8"]]
- 005add14 ["CALL", null, ["callee:00c53d00:8"]]
+ 005add54 ["INT_ADD", "register:40f0:8", ["const:5add54:8", "const:4:8"]]
+ 005add54 ["CALL", null, ["callee:00c53d00:8"]]
- 005add14 bytes f3961a94
+ 005add54 bytes eb971a94
- 005add6c ["COPY", "register:0:8", ["register:4048:8"]]
- 005add6c ["INT_ADD", "register:40f0:8", ["const:5add6c:8", "const:4:8"]]
- 005add6c ["CALLIND", null, ["register:0:8"]]
+ 005addac ["COPY", "register:0:8", ["register:4048:8"]]
+ 005addac ["INT_ADD", "register:40f0:8", ["const:5addac:8", "const:4:8"]]
+ 005addac ["CALLIND", null, ["register:0:8"]]
- 005add6c bytes 20013fd6
+ 005addac bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2540a4ee7daaf3875a13fe179d7a0c9a"></a>

### [`005ae5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae5c4.md) → [`005ae604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae604.md) FUN_005ae604

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005ae61c",
      "incomplete_value": false,
      "site": "005ae620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ae5dc",
      "incomplete_value": false,
      "site": "005ae5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "005ae620",
      "DATA",
      [
        "storage",
        "00c6f1e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ae620",
      "DATA",
      [
        "storage",
        "00c6f5e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ae620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae5c4.md#insn-005ae620) · [`005ae5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae5c4.md#insn-005ae5dc) · [`005ae5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae5c4.md#insn-005ae5ec)
- 新版 [`005ae660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae604.md#insn-005ae660) · [`005ae61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae604.md#insn-005ae61c) · [`005ae62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae604.md#insn-005ae62c)

~~~diff
- 005ae620 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ae620 ["INT_ADD", "register:40f0:8", ["const:5ae620:8", "const:4:8"]]
- 005ae620 ["CALLIND", null, ["register:0:8"]]
+ 005ae660 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ae660 ["INT_ADD", "register:40f0:8", ["const:5ae660:8", "const:4:8"]]
+ 005ae660 ["CALLIND", null, ["register:0:8"]]
- 005ae620 bytes 00013fd6
+ 005ae660 bytes 00013fd6
- 005ae5dc ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 005ae5dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ae5dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ae5dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ae61c ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 005ae61c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ae61c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ae61c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ae5dc bytes 29810791
+ 005ae61c bytes 29811791
- 005ae5ec ["INT_ADD", "register:40f0:8", ["const:5ae5ec:8", "const:4:8"]]
- 005ae5ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ae62c ["INT_ADD", "register:40f0:8", ["const:5ae62c:8", "const:4:8"]]
+ 005ae62c ["CALL", null, ["callee:00c57eb0:8"]]
- 005ae5ec bytes 31a51a94
+ 005ae62c bytes 21a61a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ca80f5393fdd4586452ef4660379144"></a>

### [`005ae634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae634.md) → [`005ae674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae674.md) FUN_005ae674

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ae68c",
      "incomplete_value": false,
      "site": "005ae690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ae64c",
      "incomplete_value": false,
      "site": "005ae650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "005ae690",
      "DATA",
      [
        "storage",
        "00c6f1e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ae690",
      "DATA",
      [
        "storage",
        "00c6f5e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ae64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae634.md#insn-005ae64c) · [`005ae65c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae634.md#insn-005ae65c) · [`005ae670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae634.md#insn-005ae670)
- 新版 [`005ae68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae674.md#insn-005ae68c) · [`005ae69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae674.md#insn-005ae69c) · [`005ae6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae674.md#insn-005ae6b0)

~~~diff
- 005ae64c ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 005ae64c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ae64c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ae64c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ae68c ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 005ae68c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ae68c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ae68c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ae64c bytes 29810791
+ 005ae68c bytes 29811791
- 005ae65c ["INT_ADD", "register:40f0:8", ["const:5ae65c:8", "const:4:8"]]
- 005ae65c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005ae69c ["INT_ADD", "register:40f0:8", ["const:5ae69c:8", "const:4:8"]]
+ 005ae69c ["CALL", null, ["callee:00c57eb0:8"]]
- 005ae65c bytes 15a51a94
+ 005ae69c bytes 05a61a94
- 005ae670 ["INT_ADD", "register:40f0:8", ["const:5ae670:8", "const:4:8"]]
- 005ae670 ["CALL", null, ["callee:00c53d00:8"]]
+ 005ae6b0 ["INT_ADD", "register:40f0:8", ["const:5ae6b0:8", "const:4:8"]]
+ 005ae6b0 ["CALL", null, ["callee:00c53d00:8"]]
- 005ae670 bytes 9c941a94
+ 005ae6b0 bytes 94951a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9672abd8eb8bbecdadaa5a3b735d09e4"></a>

### [`005ae6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae6a0.md) → [`005ae6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae6e0.md) FUN_005ae6e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ae700",
      "incomplete_value": false,
      "site": "005ae708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ae6c0",
      "incomplete_value": false,
      "site": "005ae6c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "005ae708",
      "DATA",
      [
        "storage",
        "00c6f1e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ae708",
      "DATA",
      [
        "storage",
        "00c6f5e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ae6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae6a0.md#insn-005ae6b8) · [`005ae6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae6a0.md#insn-005ae6c0) · [`005ae6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae6a0.md#insn-005ae6c4)
- 新版 [`005ae6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae6e0.md#insn-005ae6f8) · [`005ae700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae6e0.md#insn-005ae700)

~~~diff
- 005ae6b8 ["INT_ADD", "register:40f0:8", ["const:5ae6b8:8", "const:4:8"]]
- 005ae6b8 ["CALL", null, ["callee:00c57e90:8"]]
+ 005ae6f8 ["INT_ADD", "register:40f0:8", ["const:5ae6f8:8", "const:4:8"]]
+ 005ae6f8 ["CALL", null, ["callee:00c57e90:8"]]
- 005ae6b8 bytes f6a41a94
+ 005ae6f8 bytes e6a51a94
- 005ae6c0 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 005ae6c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ae6c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ae6c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ae700 ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 005ae700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ae700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ae700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ae6c0 bytes 08810791
+ 005ae700 bytes 08811791
- 005ae6c4 ["COPY", "register:4098:8", ["register:4000:8"]]
- 005ae6c4 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47c052f7836782135ceb1f9c9013b8cf"></a>

### [`005ae748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae748.md) → [`005ae788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae788.md) FUN_005ae788

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ae79c",
      "incomplete_value": false,
      "site": "005ae7a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ae75c",
      "incomplete_value": false,
      "site": "005ae764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "005ae7a4",
      "DATA",
      [
        "storage",
        "00c6f1e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ae7a4",
      "DATA",
      [
        "storage",
        "00c6f5e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ae75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae748.md#insn-005ae75c) · [`005ae78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae748.md#insn-005ae78c) · [`005ae7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae748.md#insn-005ae7b8)
- 新版 [`005ae79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae788.md#insn-005ae79c) · [`005ae7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae788.md#insn-005ae7cc) · [`005ae7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae788.md#insn-005ae7f8)

~~~diff
- 005ae75c ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 005ae75c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ae75c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ae75c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ae79c ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 005ae79c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ae79c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ae79c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ae75c bytes 08810791
+ 005ae79c bytes 08811791
- 005ae78c ["INT_ADD", "register:40f0:8", ["const:5ae78c:8", "const:4:8"]]
- 005ae78c ["CALL", null, ["callee:00c53cd0:8"]]
+ 005ae7cc ["INT_ADD", "register:40f0:8", ["const:5ae7cc:8", "const:4:8"]]
+ 005ae7cc ["CALL", null, ["callee:00c53cd0:8"]]
- 005ae78c bytes 49941a94
+ 005ae7cc bytes 41951a94
- 005ae7b8 ["INT_ADD", "register:40f0:8", ["const:5ae7b8:8", "const:4:8"]]
- 005ae7b8 ["CALL", null, ["callee:0043bb20:8"]]
+ 005ae7f8 ["INT_ADD", "register:40f0:8", ["const:5ae7f8:8", "const:4:8"]]
+ 005ae7f8 ["CALL", null, ["callee:0043bb20:8"]]
- 005ae7b8 bytes ca34fa97
+ 005ae7f8 bytes ca34fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f27464a84286d6e966b2a4b37b83fd8"></a>

### [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) → [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) FUN_005ae8e4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00450140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md) [`00450710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0045b5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b5d0.md)
- 新版 呼出元 0件  · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00450180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md) [`00450750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0045b610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b610.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.58% / 新版 96.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005aea98",
      "incomplete_value": true,
      "site": "005aea98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:993:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aea58",
      "incomplete_value": true,
      "site": "005aea58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:953:8"
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
      "definition_site": "005aee98",
      "incomplete_value": true,
      "site": "005aee98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:756:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aee58",
      "incomplete_value": true,
      "site": "005aee58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:716:8"
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
      "definition_site": "005aee8c",
      "incomplete_value": true,
      "site": "005aee9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005aee4c",
      "incomplete_value": true,
      "site": "005aee5c",
      "value": [
        "LOAD",
        "8",
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
      "005ae9b0",
      "READ",
      [
        "storage",
        "002b38ce",
        null,
        "string"
      ]
    ],
    [
      "005aea80",
      "READ",
      [
        "storage",
        "002b1953",
        null,
        "string"
      ]
    ],
    [
      "005aede8",
      "PARAM",
      [
        "storage",
        "002a8a0c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005ae9b0",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ],
    [
      "005aea80",
      "READ",
      [
        "storage",
        "002b1993",
        null,
        "string"
      ]
    ],
    [
      "005aede8",
      "PARAM",
      [
        "storage",
        "002a8ad9",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aedb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md#insn-005aedb0) · [`005aee1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md#insn-005aee1c) · [`005aee74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md#insn-005aee74)
- 新版 [`005aedf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md#insn-005aedf0) · [`005aee5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md#insn-005aee5c) · [`005aeeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md#insn-005aeeb4)

~~~diff
- 005aedb0 ["INT_ADD", "register:40f0:8", ["const:5aedb0:8", "const:4:8"]]
- 005aedb0 ["CALL", null, ["callee:00c57f70:8"]]
+ 005aedf0 ["INT_ADD", "register:40f0:8", ["const:5aedf0:8", "const:4:8"]]
+ 005aedf0 ["CALL", null, ["callee:00c57f70:8"]]
- 005aedb0 bytes 70a31a94
+ 005aedf0 bytes 60a41a94
- 005aee1c ["INT_ADD", "register:40f0:8", ["const:5aee1c:8", "const:4:8"]]
- 005aee1c ["CALL", null, ["callee:00c53d00:8"]]
+ 005aee5c ["INT_ADD", "register:40f0:8", ["const:5aee5c:8", "const:4:8"]]
+ 005aee5c ["CALL", null, ["callee:00c53d00:8"]]
- 005aee1c bytes b1921a94
+ 005aee5c bytes a9931a94
- 005aee74 ["COPY", "register:0:8", ["register:4048:8"]]
- 005aee74 ["INT_ADD", "register:40f0:8", ["const:5aee74:8", "const:4:8"]]
- 005aee74 ["CALLIND", null, ["register:0:8"]]
+ 005aeeb4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005aeeb4 ["INT_ADD", "register:40f0:8", ["const:5aeeb4:8", "const:4:8"]]
+ 005aeeb4 ["CALLIND", null, ["register:0:8"]]
- 005aee74 bytes 20013fd6
+ 005aeeb4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b68a3429659b31d98a0b0342d7a2c291"></a>

### [`005af8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af8a8.md) → [`005af8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af8e8.md) _INIT_58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005af9a4",
      "incomplete_value": true,
      "site": "005af9c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005af964",
      "incomplete_value": true,
      "site": "005af980",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "store_value",
    "new": {
      "definition_site": "005af9c4",
      "incomplete_value": true,
      "site": "005af9e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005af984",
      "incomplete_value": true,
      "site": "005af9a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005af924",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005af948",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005af968",
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
      "005af924",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005af948",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005af968",
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

- 旧版 [`005af940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af8a8.md#insn-005af940) · [`005af8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af8a8.md#insn-005af8d4) · [`005af8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005af8a8.md#insn-005af8e0)
- 新版 [`005af980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af8e8.md#insn-005af980) · [`005af914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af8e8.md#insn-005af914) · [`005af920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af8e8.md#insn-005af920)

~~~diff
- 005af940 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005af940 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005af940 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005af940 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005af980 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005af980 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005af980 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005af980 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005af940 bytes 4a553a91
+ 005af980 bytes 4a893d91
- 005af8d4 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 005af8d4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005af8d4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005af8d4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005af914 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 005af914 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005af914 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005af914 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005af8d4 bytes 73e20f91
+ 005af914 bytes 73e21f91
- 005af8e0 ["COPY", "tmp:0:8", ["const:ee6:8"]]
- 005af8e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005af8e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005af8e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005af920 ["COPY", "tmp:0:8", ["const:f26:8"]]
+ 005af920 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005af920 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005af920 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005af8e0 bytes 29993b91
+ 005af920 bytes 29993c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef23e9c30d167f4bc1029cb3702bebfe"></a>

### [`005b080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b080c.md) → [`005b084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b084c.md) _INIT_59

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b0888",
      "incomplete_value": true,
      "site": "005b08a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b0848",
      "incomplete_value": true,
      "site": "005b0864",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b08ec",
      "incomplete_value": true,
      "site": "005b0904",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b08ac",
      "incomplete_value": true,
      "site": "005b08c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005b0888",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005b08ac",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005b08cc",
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
      "005b0888",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005b08ac",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005b08cc",
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

- 旧版 [`005b0884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b080c.md#insn-005b0884) · [`005b08a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b080c.md#insn-005b08a4) · [`005b0838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b080c.md#insn-005b0838)
- 新版 [`005b08c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b084c.md#insn-005b08c4) · [`005b08e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b084c.md#insn-005b08e4) · [`005b0878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b084c.md#insn-005b0878)

~~~diff
- 005b0884 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005b0884 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b0884 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b0884 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b08c4 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005b08c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b08c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b08c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b0884 bytes 4a093691
+ 005b08c4 bytes 4a093791
- 005b08a4 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005b08a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b08a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b08a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b08e4 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005b08e4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b08e4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b08e4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b08a4 bytes 4a553a91
+ 005b08e4 bytes 4a893d91
- 005b0838 ["COPY", "tmp:0:8", ["const:410:8"]]
- 005b0838 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005b0838 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005b0838 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005b0878 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 005b0878 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005b0878 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005b0878 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005b0838 bytes 73421091
+ 005b0878 bytes 73422091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2297fd376d05e52beecfac5f841be6e7"></a>

### [`005b0c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0c08.md) → [`005b0c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0c48.md) FUN_005b0c48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005b0b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0b9c.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`005b0bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0bdc.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005b0c7c",
      "incomplete_value": false,
      "site": "005b0c88",
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
            "const:e14:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0c3c",
      "incomplete_value": false,
      "site": "005b0c48",
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
            "const:dd4:8"
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
      "definition_site": "005b0ca8",
      "incomplete_value": false,
      "site": "005b0cb0",
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
            "const:25c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0c68",
      "incomplete_value": false,
      "site": "005b0c70",
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
            "const:18f:8"
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
      "definition_site": "005b0d18",
      "incomplete_value": false,
      "site": "005b0d20",
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
            "const:1f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0cd8",
      "incomplete_value": false,
      "site": "005b0ce0",
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
            "const:126:8"
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
      "005b0c7c",
      "PARAM",
      [
        "storage",
        "002b1dd4",
        null,
        "string"
      ]
    ],
    [
      "005b0ca8",
      "PARAM",
      [
        "storage",
        "002a018f",
        null,
        "string"
      ]
    ],
    [
      "005b0d18",
      "PARAM",
      [
        "storage",
        "0029f126",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005b0c7c",
      "PARAM",
      [
        "storage",
        "002b1e14",
        null,
        "string"
      ]
    ],
    [
      "005b0ca8",
      "PARAM",
      [
        "storage",
        "002a025c",
        null,
        "string"
      ]
    ],
    [
      "005b0d18",
      "PARAM",
      [
        "storage",
        "0029f1f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0c08.md#insn-005b0c48) · [`005b0c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0c08.md#insn-005b0c70) · [`005b0ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0c08.md#insn-005b0ce0)
- 新版 [`005b0c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0c48.md#insn-005b0c88) · [`005b0cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0c48.md#insn-005b0cb0) · [`005b0d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0c48.md#insn-005b0d20)

~~~diff
- 005b0c48 ["INT_ADD", "register:40f0:8", ["const:5b0c48:8", "const:4:8"]]
- 005b0c48 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b0c88 ["INT_ADD", "register:40f0:8", ["const:5b0c88:8", "const:4:8"]]
+ 005b0c88 ["CALL", null, ["callee:00c57f60:8"]]
- 005b0c48 bytes c69b1a94
+ 005b0c88 bytes b69c1a94
- 005b0c70 ["INT_ADD", "register:40f0:8", ["const:5b0c70:8", "const:4:8"]]
- 005b0c70 ["CALL", null, ["callee:00c57f70:8"]]
+ 005b0cb0 ["INT_ADD", "register:40f0:8", ["const:5b0cb0:8", "const:4:8"]]
+ 005b0cb0 ["CALL", null, ["callee:00c57f70:8"]]
- 005b0c70 bytes c09b1a94
+ 005b0cb0 bytes b09c1a94
- 005b0ce0 ["INT_ADD", "register:40f0:8", ["const:5b0ce0:8", "const:4:8"]]
- 005b0ce0 ["CALL", null, ["callee:00c57f70:8"]]
+ 005b0d20 ["INT_ADD", "register:40f0:8", ["const:5b0d20:8", "const:4:8"]]
+ 005b0d20 ["CALL", null, ["callee:00c57f70:8"]]
- 005b0ce0 bytes a49b1a94
+ 005b0d20 bytes 949c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf0c54154e81b86658d2201290829494"></a>

### [`005b0f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0f68.md) → [`005b0fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0fa8.md) _INIT_60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b0fe4",
      "incomplete_value": true,
      "site": "005b1000",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b0fa4",
      "incomplete_value": true,
      "site": "005b0fc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b1028",
      "incomplete_value": true,
      "site": "005b1044",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b0fe8",
      "incomplete_value": true,
      "site": "005b1004",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b1048",
      "incomplete_value": true,
      "site": "005b1060",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b1008",
      "incomplete_value": true,
      "site": "005b1020",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005b0fe4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005b1008",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005b1028",
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
      "005b0fe4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005b1008",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005b1028",
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

- 旧版 [`005b0fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0f68.md#insn-005b0fe0) · [`005b1000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0f68.md#insn-005b1000) · [`005b119c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0f68.md#insn-005b119c)
- 新版 [`005b1020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0fa8.md#insn-005b1020) · [`005b1040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0fa8.md#insn-005b1040) · [`005b11dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0fa8.md#insn-005b11dc)

~~~diff
- 005b0fe0 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005b0fe0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b0fe0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b0fe0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b1020 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005b1020 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b1020 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b1020 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b0fe0 bytes 4a093691
+ 005b1020 bytes 4a093791
- 005b1000 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005b1000 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b1000 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b1000 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b1040 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005b1040 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b1040 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b1040 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b1000 bytes 4a553a91
+ 005b1040 bytes 4a893d91
- 005b119c ["INT_ADD", "register:40f0:8", ["const:5b119c:8", "const:4:8"]]
- 005b119c ["CALL", null, ["callee:00c57e30:8"]]
+ 005b11dc ["INT_ADD", "register:40f0:8", ["const:5b11dc:8", "const:4:8"]]
+ 005b11dc ["CALL", null, ["callee:00c57e30:8"]]
- 005b119c bytes 259a1a94
+ 005b11dc bytes 159b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19d65a802d9de46a641deac911cc6a9e"></a>

### [`005b14d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b14d4.md) → [`005b1514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1514.md) FUN_005b1514

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`005b14a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b14a4.md) [`005b2ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ac8.md) · 呼出先 8件 [`005b530c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b530c.md) [`005b5310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5310.md) [`005b5390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5390.md) [`005b5394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5394.md) [`00b364ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b364ac.md)
- 新版 呼出元 2件 [`005b14e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b14e4.md) [`005b2b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md) · 呼出先 8件 [`005b534c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b534c.md) [`005b5350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5350.md) [`005b53d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b53d0.md) [`005b53d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b53d4.md) [`00b368d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b368d4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b1544",
      "incomplete_value": false,
      "site": "005b1544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1504",
      "incomplete_value": false,
      "site": "005b1504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "definition_site": "005b1588",
      "incomplete_value": false,
      "site": "005b1588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1548",
      "incomplete_value": false,
      "site": "005b1548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:340:8"
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
      "005b1544",
      "DATA",
      [
        "storage",
        "00c6f2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1578",
      "READ",
      [
        "storage",
        "00c6f2d0",
        null,
        "pointer"
      ]
    ],
    [
      "005b1578",
      "READ",
      [
        "storage",
        "00c6f2d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b1544",
      "DATA",
      [
        "storage",
        "00c6f6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1578",
      "READ",
      [
        "storage",
        "00c6f6d0",
        null,
        "pointer"
      ]
    ],
    [
      "005b1578",
      "READ",
      [
        "storage",
        "00c6f6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b1544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b14d4.md#insn-005b1544) · [`005b1588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b14d4.md#insn-005b1588) · [`005b1500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b14d4.md#insn-005b1500)
- 新版 [`005b1584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1514.md#insn-005b1584) · [`005b15c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1514.md#insn-005b15c8) · [`005b1540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1514.md#insn-005b1540)

~~~diff
- 005b1544 ["COPY", "tmp:0:8", ["const:340:8"]]
- 005b1544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b1544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b1544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b1584 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 005b1584 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1584 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1584 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b1544 bytes 08010d91
+ 005b1584 bytes 08011d91
- 005b1588 ["INT_ADD", "register:40f0:8", ["const:5b1588:8", "const:4:8"]]
- 005b1588 ["CALL", null, ["callee:00b368d4:8"]]
+ 005b15c8 ["INT_ADD", "register:40f0:8", ["const:5b15c8:8", "const:4:8"]]
+ 005b15c8 ["CALL", null, ["callee:00b368d4:8"]]
- 005b1588 bytes c9131694
+ 005b15c8 bytes c3141694
- 005b1500 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 005b1500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b1500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b1500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b1540 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 005b1540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b1500 bytes 08c10a91
+ 005b1540 bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4a439df1ced4b1e57fb23980d00288d"></a>

### [`005b1610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1610.md) → [`005b1650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1650.md) FUN_005b1650

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005b14a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b14a4.md) [`005b2ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ac8.md) · 呼出先 11件 [`005b5694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5694.md) [`005b5698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5698.md) [`005b5718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5718.md) [`005b571c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b571c.md) [`00879d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879d40.md)
- 新版 呼出元 2件 [`005b14e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b14e4.md) [`005b2b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md) · 呼出先 11件 [`005b56d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b56d4.md) [`005b56d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b56d8.md) [`005b5758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5758.md) [`005b575c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b575c.md) [`00879d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b16a8",
      "incomplete_value": false,
      "site": "005b16a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1668",
      "incomplete_value": false,
      "site": "005b1668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
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
      "definition_site": "005b16ec",
      "incomplete_value": true,
      "site": "005b16ec",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b16ac",
      "incomplete_value": true,
      "site": "005b16ac",
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
            "const:560:8"
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
      "005b1670",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "005b16a8",
      "DATA",
      [
        "storage",
        "00c6f4e0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b16dc",
      "READ",
      [
        "storage",
        "00c6f500",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b1670",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "005b16a8",
      "DATA",
      [
        "storage",
        "00c6f8e0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b16dc",
      "READ",
      [
        "storage",
        "00c6f900",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b16a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1610.md#insn-005b16a8) · [`005b1630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1610.md#insn-005b1630) · [`005b1640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1610.md#insn-005b1640)
- 新版 [`005b16e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1650.md#insn-005b16e8) · [`005b1670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1650.md#insn-005b1670) · [`005b1680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1650.md#insn-005b1680)

~~~diff
- 005b16a8 ["COPY", "tmp:0:8", ["const:560:8"]]
- 005b16a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b16a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b16a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b16e8 ["COPY", "tmp:0:8", ["const:960:8"]]
+ 005b16e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b16e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b16e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b16a8 bytes 08811591
+ 005b16e8 bytes 08812591
- 005b1630 ["COPY", "tmp:0:8", ["const:30e:8"]]
- 005b1630 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005b1630 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005b1630 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005b1670 ["COPY", "tmp:0:8", ["const:3ea:8"]]
+ 005b1670 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005b1670 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005b1670 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005b1630 bytes 21380c91
+ 005b1670 bytes 21a80f91
- 005b1640 ["INT_ADD", "register:40f0:8", ["const:5b1640:8", "const:4:8"]]
- 005b1640 ["CALL", null, ["callee:00c58190:8"]]
+ 005b1680 ["INT_ADD", "register:40f0:8", ["const:5b1680:8", "const:4:8"]]
+ 005b1680 ["CALL", null, ["callee:00c58190:8"]]
- 005b1640 bytes d4991a94
+ 005b1680 bytes c49a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1013c603b816582a01e67759fd4bc6ec"></a>

### [`005b1778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1778.md) → [`005b17b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md) FUN_005b17b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b5314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5314.md) · 呼出先 6件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00493650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493650.md) [`005b1890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1890.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005b5354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5354.md) · 呼出先 6件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00493690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493690.md) [`005b18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b1810",
      "incomplete_value": true,
      "site": "005b1810",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2fa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b17d0",
      "incomplete_value": true,
      "site": "005b17d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ba:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b17e8",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b17a8",
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
      "005b17e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "005b17fc",
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
      "005b17e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "005b17fc",
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

- 旧版 [`005b17a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1778.md#insn-005b17a8) · [`005b17e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1778.md#insn-005b17e8) · [`005b17b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1778.md#insn-005b17b4)
- 新版 [`005b17e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md#insn-005b17e8) · [`005b1828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md#insn-005b1828) · [`005b17f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md#insn-005b17f4)

~~~diff
- 005b17a8 ["INT_ADD", "register:40f0:8", ["const:5b17a8:8", "const:4:8"]]
- 005b17a8 ["CALL", null, ["ram:48ccb8:8"]]
+ 005b17e8 ["INT_ADD", "register:40f0:8", ["const:5b17e8:8", "const:4:8"]]
+ 005b17e8 ["CALL", null, ["ram:48ccf8:8"]]
- 005b17a8 bytes 446dfb97
+ 005b17e8 bytes 446dfb97
- 005b17e8 ["INT_ADD", "register:40f0:8", ["const:5b17e8:8", "const:4:8"]]
- 005b17e8 ["CALL", null, ["callee:00493690:8"]]
+ 005b1828 ["INT_ADD", "register:40f0:8", ["const:5b1828:8", "const:4:8"]]
+ 005b1828 ["CALL", null, ["callee:00493690:8"]]
- 005b17e8 bytes 9a87fb97
+ 005b1828 bytes 9a87fb97
- 005b17b4 ["COPY", "tmp:0:8", ["const:2ba:8"]]
- 005b17b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b17b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b17b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b17f4 ["COPY", "tmp:0:8", ["const:2fa:8"]]
+ 005b17f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b17f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b17f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b17b4 bytes 29e90a91
+ 005b17f4 bytes 29e90b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cadee7dd221a617afc623e6e8b3d76e"></a>

### [`005b1890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1890.md) → [`005b18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md) FUN_005b18d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b1778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1778.md) · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005b5524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5524.md) [`005b55dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b55dc.md) [`005b55e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b55e0.md) [`00879d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879d48.md)
- 新版 呼出元 1件 [`005b17b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md) · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005b5564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5564.md) [`005b561c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b561c.md) [`005b5620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5620.md) [`00879d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.52% / 新版 96.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b1994",
      "incomplete_value": false,
      "site": "005b1994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1954",
      "incomplete_value": false,
      "site": "005b1954",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
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
      "definition_site": "005b19c8",
      "incomplete_value": false,
      "site": "005b19c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1988",
      "incomplete_value": false,
      "site": "005b1988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:460:8"
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
      "005b1994",
      "DATA",
      [
        "storage",
        "00c6f3d0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b19c8",
      "DATA",
      [
        "storage",
        "00c6f460",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1a14",
      "READ",
      [
        "storage",
        "00c6f480",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b1994",
      "DATA",
      [
        "storage",
        "00c6f7d0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b19c8",
      "DATA",
      [
        "storage",
        "00c6f860",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1a14",
      "READ",
      [
        "storage",
        "00c6f880",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b18f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1890.md#insn-005b18f4) · [`005b1930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1890.md#insn-005b1930) · [`005b193c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1890.md#insn-005b193c)
- 新版 [`005b1934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md#insn-005b1934) · [`005b1970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md#insn-005b1970) · [`005b197c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md#insn-005b197c)

~~~diff
- 005b18f4 ["INT_ADD", "register:40f0:8", ["const:5b18f4:8", "const:4:8"]]
- 005b18f4 ["CALL", null, ["callee:0043bb20:8"]]
+ 005b1934 ["INT_ADD", "register:40f0:8", ["const:5b1934:8", "const:4:8"]]
+ 005b1934 ["CALL", null, ["callee:0043bb20:8"]]
- 005b18f4 bytes 7b28fa97
+ 005b1934 bytes 7b28fa97
- 005b1930 ["INT_ADD", "register:40f0:8", ["const:5b1930:8", "const:4:8"]]
- 005b1930 ["CALL", null, ["callee:0043bb20:8"]]
+ 005b1970 ["INT_ADD", "register:40f0:8", ["const:5b1970:8", "const:4:8"]]
+ 005b1970 ["CALL", null, ["callee:0043bb20:8"]]
- 005b1930 bytes 6c28fa97
+ 005b1970 bytes 6c28fa97
- 005b193c ["INT_ADD", "register:40f0:8", ["const:5b193c:8", "const:4:8"]]
- 005b193c ["CALL", null, ["callee:00c57e90:8"]]
+ 005b197c ["INT_ADD", "register:40f0:8", ["const:5b197c:8", "const:4:8"]]
+ 005b197c ["CALL", null, ["callee:00c57e90:8"]]
- 005b193c bytes 55981a94
+ 005b197c bytes 45991a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-531bf46133d8b90430e8d5f54d3d00db"></a>

### [`005b1b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1b44.md) → [`005b1b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md) FUN_005b1b84

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b569c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b569c.md) · 呼出先 7件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00493650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493650.md) [`005b1c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1c90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005b56dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b56dc.md) · 呼出先 7件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00493690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493690.md) [`005b1cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1cd0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.44% / 新版 93.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b1bdc",
      "incomplete_value": true,
      "site": "005b1bdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2fa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1b9c",
      "incomplete_value": true,
      "site": "005b1b9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ba:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b1bb4",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b1b74",
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
      "005b1bb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "005b1bc8",
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
      "005b1bb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "005b1bc8",
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

- 旧版 [`005b1b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1b44.md#insn-005b1b74) · [`005b1bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1b44.md#insn-005b1bb4) · [`005b1b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1b44.md#insn-005b1b80)
- 新版 [`005b1bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md#insn-005b1bb4) · [`005b1bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md#insn-005b1bf4) · [`005b1bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md#insn-005b1bc0)

~~~diff
- 005b1b74 ["INT_ADD", "register:40f0:8", ["const:5b1b74:8", "const:4:8"]]
- 005b1b74 ["CALL", null, ["ram:48ccb8:8"]]
+ 005b1bb4 ["INT_ADD", "register:40f0:8", ["const:5b1bb4:8", "const:4:8"]]
+ 005b1bb4 ["CALL", null, ["ram:48ccf8:8"]]
- 005b1b74 bytes 516cfb97
+ 005b1bb4 bytes 516cfb97
- 005b1bb4 ["INT_ADD", "register:40f0:8", ["const:5b1bb4:8", "const:4:8"]]
- 005b1bb4 ["CALL", null, ["callee:00493690:8"]]
+ 005b1bf4 ["INT_ADD", "register:40f0:8", ["const:5b1bf4:8", "const:4:8"]]
+ 005b1bf4 ["CALL", null, ["callee:00493690:8"]]
- 005b1bb4 bytes a786fb97
+ 005b1bf4 bytes a786fb97
- 005b1b80 ["COPY", "tmp:0:8", ["const:2ba:8"]]
- 005b1b80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b1b80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b1b80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b1bc0 ["COPY", "tmp:0:8", ["const:2fa:8"]]
+ 005b1bc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b1bc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b1bc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b1b80 bytes 29e90a91
+ 005b1bc0 bytes 29e90b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ad8cbfe300a10c88276bc61d5c12ede"></a>

### [`005b1c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1c90.md) → [`005b1cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1cd0.md) FUN_005b1cd0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`005b1b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1b44.md) [`005b5558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5558.md) · 呼出先 6件 [`005b1de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1de4.md) [`005b57cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b57cc.md) [`005b57d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b57d0.md) [`005b5a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5a98.md) [`005b5a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5a9c.md)
- 新版 呼出元 2件 [`005b1b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md) [`005b5598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5598.md) · 呼出先 6件 [`005b1e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1e24.md) [`005b580c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b580c.md) [`005b5810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5810.md) [`005b5ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ad8.md) [`005b5adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5adc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b1cfc",
      "incomplete_value": false,
      "site": "005b1cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1cbc",
      "incomplete_value": false,
      "site": "005b1cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "definition_site": "005b1d14",
      "incomplete_value": false,
      "site": "005b1d14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1cd4",
      "incomplete_value": false,
      "site": "005b1cd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "005b1cfc",
      "DATA",
      [
        "storage",
        "00c6f5e0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1d14",
      "DATA",
      [
        "storage",
        "00c6f6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1d4c",
      "READ",
      [
        "storage",
        "00c6f6d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b1cfc",
      "DATA",
      [
        "storage",
        "00c6f9e0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1d14",
      "DATA",
      [
        "storage",
        "00c6fab0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1d4c",
      "READ",
      [
        "storage",
        "00c6fad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b1cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1c90.md#insn-005b1cb8) · [`005b1cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1c90.md#insn-005b1cd0) · [`005b1ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1c90.md#insn-005b1ce4)
- 新版 [`005b1cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1cd0.md#insn-005b1cf8) · [`005b1d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1cd0.md#insn-005b1d10) · [`005b1d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1cd0.md#insn-005b1d24)

~~~diff
- 005b1cb8 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 005b1cb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b1cb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b1cb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b1cf8 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 005b1cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b1cb8 bytes 08811791
+ 005b1cf8 bytes 08812791
- 005b1cd0 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 005b1cd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b1cd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b1cd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b1d10 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 005b1d10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1d10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1d10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b1cd0 bytes 08c11a91
+ 005b1d10 bytes 08c12a91
- 005b1ce4 ["INT_ADD", "register:40f0:8", ["const:5b1ce4:8", "const:4:8"]]
- 005b1ce4 ["CALL", null, ["callee:005b1e24:8"]]
+ 005b1d24 ["INT_ADD", "register:40f0:8", ["const:5b1d24:8", "const:4:8"]]
+ 005b1d24 ["CALL", null, ["callee:005b1e24:8"]]
- 005b1ce4 bytes 40000094
+ 005b1d24 bytes 40000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-159d92ddbf177d3f8b60febe5c266799"></a>

### [`005b20ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b20ec.md) → [`005b212c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b212c.md) FUN_005b212c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`005b22b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b22b0.md) [`005b5398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5398.md) [`005b55e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b55e4.md) [`005b5720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5720.md) [`005b5c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c0c.md) · 呼出先 7件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`005b0b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0b9c.md) [`005b51d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51d4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 7件 [`005b22f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22f0.md) [`005b53d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b53d8.md) [`005b5624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5624.md) [`005b5760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5760.md) [`005b5c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5c4c.md) · 呼出先 7件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005b0bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0bdc.md) [`005b5214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5214.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b21ac",
      "incomplete_value": false,
      "site": "005b21c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b216c",
      "incomplete_value": false,
      "site": "005b2180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
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
      "005b21c0",
      "DATA",
      [
        "storage",
        "00c6f260",
        null,
        "pointer"
      ]
    ],
    [
      "005b2210",
      "READ",
      [
        "storage",
        "00c6f270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b21c0",
      "DATA",
      [
        "storage",
        "00c6f660",
        null,
        "pointer"
      ]
    ],
    [
      "005b2210",
      "READ",
      [
        "storage",
        "00c6f670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b21c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b20ec.md#insn-005b21c0) · [`005b2160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b20ec.md#insn-005b2160) · [`005b216c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b20ec.md#insn-005b216c)
- 新版 [`005b2200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b212c.md#insn-005b2200) · [`005b21a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b212c.md#insn-005b21a0) · [`005b21ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b212c.md#insn-005b21ac)

~~~diff
- 005b21c0 ["INT_ADD", "register:40f0:8", ["const:5b21c0:8", "const:4:8"]]
- 005b21c0 ["CALL", null, ["callee:00c53d00:8"]]
+ 005b2200 ["INT_ADD", "register:40f0:8", ["const:5b2200:8", "const:4:8"]]
+ 005b2200 ["CALL", null, ["callee:00c53d00:8"]]
- 005b21c0 bytes c8851a94
+ 005b2200 bytes c0861a94
- 005b2160 ["INT_ADD", "register:40f0:8", ["const:5b2160:8", "const:4:8"]]
- 005b2160 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b21a0 ["INT_ADD", "register:40f0:8", ["const:5b21a0:8", "const:4:8"]]
+ 005b21a0 ["CALL", null, ["callee:00c57e90:8"]]
- 005b2160 bytes 4c961a94
+ 005b21a0 bytes 3c971a94
- 005b216c ["COPY", "tmp:0:8", ["const:260:8"]]
- 005b216c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b216c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b216c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b21ac ["COPY", "tmp:0:8", ["const:660:8"]]
+ 005b21ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b21ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b21ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b216c bytes 08810991
+ 005b21ac bytes 08811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-702b97542f2ed254197d8f48959efa26"></a>

### [`005b22b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b22b0.md) → [`005b22f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22f0.md) FUN_005b22f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`005b5aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5aa0.md) [`005b5dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5dc8.md) [`005b6390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6390.md) [`005b6720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6720.md) [`005b6840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6840.md) · 呼出先 6件 [`005b20ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b20ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 6件 [`005b5ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ae0.md) [`005b5e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5e08.md) [`005b63d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b63d0.md) [`005b6760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6760.md) [`005b6880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6880.md) · 呼出先 6件 [`005b212c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b212c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.70% / 新版 95.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005b2340",
      "incomplete_value": false,
      "site": "005b2348",
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
            "const:72e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b2300",
      "incomplete_value": false,
      "site": "005b2308",
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
            "const:652:8"
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
      "definition_site": "005b2358",
      "incomplete_value": false,
      "site": "005b2360",
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
            "const:26d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b2318",
      "incomplete_value": false,
      "site": "005b2320",
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
            "const:1a0:8"
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
      "definition_site": "005b238c",
      "incomplete_value": false,
      "site": "005b2398",
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
            "const:d9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b234c",
      "incomplete_value": false,
      "site": "005b2358",
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
            "const:ccf:8"
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
      "005b2340",
      "PARAM",
      [
        "storage",
        "002a5652",
        null,
        null
      ]
    ],
    [
      "005b2358",
      "PARAM",
      [
        "storage",
        "002a01a0",
        null,
        null
      ]
    ],
    [
      "005b238c",
      "PARAM",
      [
        "storage",
        "002a8ccf",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005b2340",
      "PARAM",
      [
        "storage",
        "002a572e",
        null,
        null
      ]
    ],
    [
      "005b2358",
      "PARAM",
      [
        "storage",
        "002a026d",
        null,
        null
      ]
    ],
    [
      "005b238c",
      "PARAM",
      [
        "storage",
        "002a8d9c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b2308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b22b0.md#insn-005b2308) · [`005b2318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b22b0.md#insn-005b2318) · [`005b2320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b22b0.md#insn-005b2320)
- 新版 [`005b2348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22f0.md#insn-005b2348) · [`005b2358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22f0.md#insn-005b2358) · [`005b2360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22f0.md#insn-005b2360)

~~~diff
- 005b2308 ["INT_ADD", "register:40f0:8", ["const:5b2308:8", "const:4:8"]]
- 005b2308 ["CALL", null, ["callee:00c58190:8"]]
+ 005b2348 ["INT_ADD", "register:40f0:8", ["const:5b2348:8", "const:4:8"]]
+ 005b2348 ["CALL", null, ["callee:00c58190:8"]]
- 005b2308 bytes a2961a94
+ 005b2348 bytes 92971a94
- 005b2318 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 005b2318 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005b2318 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005b2318 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005b2358 ["COPY", "tmp:0:8", ["const:26d:8"]]
+ 005b2358 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005b2358 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005b2358 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005b2318 bytes 21800691
+ 005b2358 bytes 21b40991
- 005b2320 ["INT_ADD", "register:40f0:8", ["const:5b2320:8", "const:4:8"]]
- 005b2320 ["CALL", null, ["callee:00c58190:8"]]
+ 005b2360 ["INT_ADD", "register:40f0:8", ["const:5b2360:8", "const:4:8"]]
+ 005b2360 ["CALL", null, ["callee:00c58190:8"]]
- 005b2320 bytes 9c961a94
+ 005b2360 bytes 8c971a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57f255d82859cd6401da98567f4806de"></a>

### [`005b2474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2474.md) → [`005b24b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b24b4.md) FUN_005b24b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005b246c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b246c.md) [`005b3e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3e8c.md) · 呼出先 6件 [`005b5b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b64.md) [`005b5b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b68.md) [`005b5c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c04.md) [`005b5c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c08.md) [`0087a5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a5a4.md)
- 新版 呼出元 2件 [`005b24ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b24ac.md) [`005b3ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3ecc.md) · 呼出先 6件 [`005b5ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ba4.md) [`005b5ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ba8.md) [`005b5c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5c44.md) [`005b5c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5c48.md) [`0087a5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a5e4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b24e0",
      "incomplete_value": false,
      "site": "005b24e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b24a0",
      "incomplete_value": false,
      "site": "005b24a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:740:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b2510",
      "value": [
        "leaf",
        "ram:87a5e4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b24d0",
      "value": [
        "leaf",
        "ram:87a5a4:8"
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
      "005b24e0",
      "DATA",
      [
        "storage",
        "00c6f740",
        null,
        "undefined *"
      ]
    ],
    [
      "005b24f4",
      "DATA",
      [
        "storage",
        "00c6f7c0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b2510",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0087a5a4"
      ]
    ]
  ],
  "added": [
    [
      "005b24e0",
      "DATA",
      [
        "storage",
        "00c6fb40",
        null,
        "undefined *"
      ]
    ],
    [
      "005b24f4",
      "DATA",
      [
        "storage",
        "00c6fbc0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b2510",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0087a5e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b24d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2474.md#insn-005b24d0) · [`005b248c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2474.md#insn-005b248c) · [`005b24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2474.md#insn-005b24b0)
- 新版 [`005b2510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b24b4.md#insn-005b2510) · [`005b24cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b24b4.md#insn-005b24cc) · [`005b24f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b24b4.md#insn-005b24f0)

~~~diff
- 005b24d0 ["INT_ADD", "register:40f0:8", ["const:5b24d0:8", "const:4:8"]]
- 005b24d0 ["CALL", null, ["ram:87a5a4:8"]]
+ 005b2510 ["INT_ADD", "register:40f0:8", ["const:5b2510:8", "const:4:8"]]
+ 005b2510 ["CALL", null, ["ram:87a5e4:8"]]
- 005b24d0 bytes 35200b94
+ 005b2510 bytes 35200b94
- 005b248c ["COPY", "tmp:0:8", ["const:740:8"]]
- 005b248c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b248c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b248c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b24cc ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 005b24cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b24cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b24cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b248c bytes 29011d91
+ 005b24cc bytes 29012d91
- 005b24b0 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 005b24b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b24b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b24b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b24f0 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 005b24f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b24f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b24f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b24b0 bytes 08011f91
+ 005b24f0 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc0486546248426c6fc77bbd96c31bbc"></a>

### [`005b25d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b25d0.md) → [`005b2610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2610.md) FUN_005b2610

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b5b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b6c.md) · 呼出先 6件 [`005b271c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b271c.md) [`005b5c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c98.md) [`005b5c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5c9c.md) [`005b5dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5dc0.md) [`005b5dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5dc4.md)
- 新版 呼出元 1件 [`005b5bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5bac.md) · 呼出先 6件 [`005b275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md) [`005b5cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5cd8.md) [`005b5cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5cdc.md) [`005b5e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5e00.md) [`005b5e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5e04.md)

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
      "definition_site": "005b2638",
      "incomplete_value": false,
      "site": "005b2638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b25f8",
      "incomplete_value": false,
      "site": "005b25f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "definition_site": "005b264c",
      "incomplete_value": false,
      "site": "005b264c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b260c",
      "incomplete_value": false,
      "site": "005b260c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "005b2638",
      "DATA",
      [
        "storage",
        "00c6f840",
        null,
        "undefined *"
      ]
    ],
    [
      "005b264c",
      "DATA",
      [
        "storage",
        "00c6f8c0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b2684",
      "READ",
      [
        "storage",
        "00c6f8e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b2638",
      "DATA",
      [
        "storage",
        "00c6fc40",
        null,
        "undefined *"
      ]
    ],
    [
      "005b264c",
      "DATA",
      [
        "storage",
        "00c6fcc0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b2684",
      "READ",
      [
        "storage",
        "00c6fce0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b25f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b25d0.md#insn-005b25f4) · [`005b2608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b25d0.md#insn-005b2608) · [`005b261c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b25d0.md#insn-005b261c)
- 新版 [`005b2634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2610.md#insn-005b2634) · [`005b2648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2610.md#insn-005b2648) · [`005b265c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2610.md#insn-005b265c)

~~~diff
- 005b25f4 ["COPY", "tmp:0:8", ["const:840:8"]]
- 005b25f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b25f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b25f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b2634 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 005b2634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b25f4 bytes 08012191
+ 005b2634 bytes 08013191
- 005b2608 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 005b2608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b2608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b2608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b2648 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 005b2648 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2648 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2648 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b2608 bytes 08012391
+ 005b2648 bytes 08013391
- 005b261c ["INT_ADD", "register:40f0:8", ["const:5b261c:8", "const:4:8"]]
- 005b261c ["CALL", null, ["callee:005b275c:8"]]
+ 005b265c ["INT_ADD", "register:40f0:8", ["const:5b265c:8", "const:4:8"]]
+ 005b265c ["CALL", null, ["callee:005b275c:8"]]
- 005b261c bytes 40000094
+ 005b265c bytes 40000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03d4017012b448cc70f9cdf7ba613995"></a>

### [`005b271c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b271c.md) → [`005b275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md) FUN_005b275c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b25d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b25d0.md) · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`0059f4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059f/0059f4c0.md) [`005b809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b809c.md)
- 新版 呼出元 1件 [`005b2610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2610.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059f500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f500.md) [`005b80dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b80dc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.71% / 新版 97.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b28a8",
      "incomplete_value": false,
      "site": "005b28a8",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b2868",
      "incomplete_value": false,
      "site": "005b2868",
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
            "const:3a0:8"
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
      "005b281c",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ],
    [
      "005b28a8",
      "DATA",
      [
        "storage",
        "00c703a0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b291c",
      "READ",
      [
        "storage",
        "00c703c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b281c",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "005b28a8",
      "DATA",
      [
        "storage",
        "00c707a0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b291c",
      "READ",
      [
        "storage",
        "00c707c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b2750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b271c.md#insn-005b2750) · [`005b277c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b271c.md#insn-005b277c) · [`005b2788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b271c.md#insn-005b2788)
- 新版 [`005b2790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md#insn-005b2790) · [`005b27bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md#insn-005b27bc) · [`005b27c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md#insn-005b27c8)

~~~diff
- 005b2750 ["INT_ADD", "register:40f0:8", ["const:5b2750:8", "const:4:8"]]
- 005b2750 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b2790 ["INT_ADD", "register:40f0:8", ["const:5b2790:8", "const:4:8"]]
+ 005b2790 ["CALL", null, ["callee:00c57e90:8"]]
- 005b2750 bytes d0941a94
+ 005b2790 bytes c0951a94
- 005b277c ["INT_ADD", "register:40f0:8", ["const:5b277c:8", "const:4:8"]]
- 005b277c ["CALL", null, ["callee:0043bb20:8"]]
+ 005b27bc ["INT_ADD", "register:40f0:8", ["const:5b27bc:8", "const:4:8"]]
+ 005b27bc ["CALL", null, ["callee:0043bb20:8"]]
- 005b277c bytes d924fa97
+ 005b27bc bytes d924fa97
- 005b2788 ["INT_ADD", "register:40f0:8", ["const:5b2788:8", "const:4:8"]]
- 005b2788 ["CALL", null, ["callee:0059f500:8"]]
+ 005b27c8 ["INT_ADD", "register:40f0:8", ["const:5b27c8:8", "const:4:8"]]
+ 005b27c8 ["CALL", null, ["callee:0059f500:8"]]
- 005b2788 bytes 4eb3ff97
+ 005b27c8 bytes 4eb3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2552193b9cf2c9640adad1c1717c3de"></a>

### [`005b2ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ac8.md) → [`005b2b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md) FUN_005b2b08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · 呼出先 9件 [`005b14d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b14d4.md) [`005b1610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1610.md) [`005b2c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2c50.md) [`005b2ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ea8.md) [`005b5e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e60.md)
- 新版 呼出元 1件 [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) · 呼出先 9件 [`005b1514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1514.md) [`005b1650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1650.md) [`005b2c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2c90.md) [`005b2ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2ee8.md) [`005b5ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ea0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b2b44",
      "incomplete_value": false,
      "site": "005b2b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:d40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b2b04",
      "incomplete_value": false,
      "site": "005b2b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "definition_site": "005b2b94",
      "incomplete_value": true,
      "site": "005b2b94",
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
      "definition_site": "005b2b54",
      "incomplete_value": true,
      "site": "005b2b54",
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
      "005b2b44",
      "DATA",
      [
        "storage",
        "00c6f940",
        null,
        "undefined *"
      ]
    ],
    [
      "005b2b80",
      "READ",
      [
        "storage",
        "00c6f960",
        null,
        "pointer"
      ]
    ],
    [
      "005b2b80",
      "READ",
      [
        "storage",
        "00c6f968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b2b44",
      "DATA",
      [
        "storage",
        "00c6fd40",
        null,
        "undefined *"
      ]
    ],
    [
      "005b2b80",
      "READ",
      [
        "storage",
        "00c6fd60",
        null,
        "pointer"
      ]
    ],
    [
      "005b2b80",
      "READ",
      [
        "storage",
        "00c6fd68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b2b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ac8.md#insn-005b2b44) · [`005b2b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ac8.md#insn-005b2b00) · [`005b2b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b2/005b2ac8.md#insn-005b2b18)
- 新版 [`005b2b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md#insn-005b2b84) · [`005b2b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md#insn-005b2b40) · [`005b2b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md#insn-005b2b58)

~~~diff
- 005b2b44 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b2b44 ["INT_ADD", "register:40f0:8", ["const:5b2b44:8", "const:4:8"]]
- 005b2b44 ["CALLIND", null, ["register:0:8"]]
+ 005b2b84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b2b84 ["INT_ADD", "register:40f0:8", ["const:5b2b84:8", "const:4:8"]]
+ 005b2b84 ["CALLIND", null, ["register:0:8"]]
- 005b2b44 bytes 00013fd6
+ 005b2b84 bytes 00013fd6
- 005b2b00 ["COPY", "tmp:0:8", ["const:940:8"]]
- 005b2b00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b2b00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b2b00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b2b40 ["COPY", "tmp:0:8", ["const:d40:8"]]
+ 005b2b40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2b40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2b40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b2b00 bytes 08012591
+ 005b2b40 bytes 08013591
- 005b2b18 ["INT_ADD", "register:40f0:8", ["const:5b2b18:8", "const:4:8"]]
- 005b2b18 ["CALL", null, ["callee:005b2c90:8"]]
+ 005b2b58 ["INT_ADD", "register:40f0:8", ["const:5b2b58:8", "const:4:8"]]
+ 005b2b58 ["CALL", null, ["callee:005b2c90:8"]]
- 005b2b18 bytes 4e000094
+ 005b2b58 bytes 4e000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59f789318434bbd3b745c26e67d2425d"></a>

### [`005b3100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3100.md) → [`005b3140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3140.md) FUN_005b3140

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b5e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5e68.md) · 呼出先 9件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`005b0b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b0b9c.md) [`005b3308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3308.md) [`005b51d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51d4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`005b5ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ea8.md) · 呼出先 9件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005b0bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0bdc.md) [`005b3348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3348.md) [`005b5214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5214.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.74% / 新版 90.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b3200",
      "incomplete_value": true,
      "site": "005b3208",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b31c0",
      "incomplete_value": true,
      "site": "005b31c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b31fc",
      "incomplete_value": true,
      "site": "005b320c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b31bc",
      "incomplete_value": true,
      "site": "005b31cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:944:8"
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
      "definition_site": "005b31fc",
      "incomplete_value": true,
      "site": "005b320c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "005b31bc",
      "incomplete_value": true,
      "site": "005b31cc",
      "value": [
        "LOAD",
        "16",
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
      "005b31fc",
      "READ",
      [
        "storage",
        "002a7944",
        null,
        null
      ]
    ],
    [
      "005b31fc",
      "READ",
      [
        "storage",
        "002a7954",
        null,
        null
      ]
    ],
    [
      "005b3200",
      "READ",
      [
        "storage",
        "002c3160",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005b31fc",
      "READ",
      [
        "storage",
        "002a7a20",
        null,
        null
      ]
    ],
    [
      "005b31fc",
      "READ",
      [
        "storage",
        "002a7a30",
        null,
        null
      ]
    ],
    [
      "005b3200",
      "READ",
      [
        "storage",
        "002c31a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b31c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3100.md#insn-005b31c0) · [`005b3240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3100.md#insn-005b3240) · [`005b31ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3100.md#insn-005b31ac)
- 新版 [`005b3200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3140.md#insn-005b3200) · [`005b3280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3140.md#insn-005b3280) · [`005b31ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3140.md#insn-005b31ec)

~~~diff
- 005b31c0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:160:8"]]
- 005b31c0 ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
- 005b31c0 ["COPY", "register:5050:8", ["const:0:8"]]
- 005b31c0 ["COPY", "register:5058:8", ["const:0:8"]]
+ 005b3200 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1a0:8"]]
+ 005b3200 ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
+ 005b3200 ["COPY", "register:5050:8", ["const:0:8"]]
+ 005b3200 ["COPY", "register:5058:8", ["const:0:8"]]
- 005b31c0 bytes 2259c03d
+ 005b3200 bytes 2269c03d
- 005b3240 ["INT_ADD", "register:40f0:8", ["const:5b3240:8", "const:4:8"]]
- 005b3240 ["CALL", null, ["callee:00c53d00:8"]]
+ 005b3280 ["INT_ADD", "register:40f0:8", ["const:5b3280:8", "const:4:8"]]
+ 005b3280 ["CALL", null, ["callee:00c53d00:8"]]
- 005b3240 bytes a8811a94
+ 005b3280 bytes a0821a94
- 005b31ac ["INT_ADD", "register:40f0:8", ["const:5b31ac:8", "const:4:8"]]
- 005b31ac ["CALL", null, ["callee:00c57e90:8"]]
+ 005b31ec ["INT_ADD", "register:40f0:8", ["const:5b31ec:8", "const:4:8"]]
+ 005b31ec ["CALL", null, ["callee:00c57e90:8"]]
- 005b31ac bytes 39921a94
+ 005b31ec bytes 29931a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-856c5c81d421bef541885bba9914ce1f"></a>

### [`005b3308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3308.md) → [`005b3348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3348.md) FUN_005b3348

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005b3100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3100.md) [`005b3304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3304.md) [`005b5fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5fbc.md) · 呼出先 6件 [`005b611c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b611c.md) [`005b6120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6120.md) [`005b61ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b61ac.md) [`005b61b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b61b0.md) [`0087ac18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087ac18.md)
- 新版 呼出元 3件 [`005b3140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3140.md) [`005b3344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3344.md) [`005b5ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ffc.md) · 呼出先 6件 [`005b615c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b615c.md) [`005b6160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6160.md) [`005b61ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b61ec.md) [`005b61f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b61f0.md) [`0087ac58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087ac58.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b3374",
      "incomplete_value": false,
      "site": "005b3374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3334",
      "incomplete_value": false,
      "site": "005b3334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      "definition_site": "005b3388",
      "incomplete_value": false,
      "site": "005b3388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3348",
      "incomplete_value": false,
      "site": "005b3348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "site": "005b33a4",
      "value": [
        "leaf",
        "ram:87ac58:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b3364",
      "value": [
        "leaf",
        "ram:87ac18:8"
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
      "005b3374",
      "DATA",
      [
        "storage",
        "00c6fa60",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3388",
      "DATA",
      [
        "storage",
        "00c6fae0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b33a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0087ac18"
      ]
    ]
  ],
  "added": [
    [
      "005b3374",
      "DATA",
      [
        "storage",
        "00c6fe60",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3388",
      "DATA",
      [
        "storage",
        "00c6fee0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b33a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0087ac58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b3364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3308.md#insn-005b3364) · [`005b3330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3308.md#insn-005b3330) · [`005b3344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3308.md#insn-005b3344)
- 新版 [`005b33a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3348.md#insn-005b33a4) · [`005b3370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3348.md#insn-005b3370) · [`005b3384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3348.md#insn-005b3384)

~~~diff
- 005b3364 ["INT_ADD", "register:40f0:8", ["const:5b3364:8", "const:4:8"]]
- 005b3364 ["CALL", null, ["ram:87ac18:8"]]
+ 005b33a4 ["INT_ADD", "register:40f0:8", ["const:5b33a4:8", "const:4:8"]]
+ 005b33a4 ["CALL", null, ["ram:87ac58:8"]]
- 005b3364 bytes 2d1e0b94
+ 005b33a4 bytes 2d1e0b94
- 005b3330 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 005b3330 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b3330 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b3330 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b3370 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 005b3370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b3330 bytes 08812991
+ 005b3370 bytes 08813991
- 005b3344 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 005b3344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b3344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b3344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b3384 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 005b3384 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3384 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3384 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b3344 bytes 08812b91
+ 005b3384 bytes 08813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da64424cdccd98fd22f028ddbd69ea7a"></a>

### [`005b3464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3464.md) → [`005b34a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b34a4.md) FUN_005b34a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b6124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6124.md) · 呼出先 6件 [`005b35b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b35b8.md) [`005b6260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6260.md) [`005b6264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6264.md) [`005b6388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6388.md) [`005b638c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b638c.md)
- 新版 呼出元 1件 [`005b6164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6164.md) · 呼出先 6件 [`005b35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md) [`005b62a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b62a0.md) [`005b62a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b62a4.md) [`005b63c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b63c8.md) [`005b63cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b63cc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b34cc",
      "incomplete_value": false,
      "site": "005b34cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b348c",
      "incomplete_value": false,
      "site": "005b348c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:b60:8"
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
      "definition_site": "005b34e4",
      "incomplete_value": false,
      "site": "005b34e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b34a4",
      "incomplete_value": false,
      "site": "005b34a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:be0:8"
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
      "005b34cc",
      "DATA",
      [
        "storage",
        "00c6fb60",
        null,
        "undefined *"
      ]
    ],
    [
      "005b34e4",
      "DATA",
      [
        "storage",
        "00c6fbe0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3520",
      "READ",
      [
        "storage",
        "00c6fc00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b34cc",
      "DATA",
      [
        "storage",
        "00c6ff60",
        null,
        "undefined *"
      ]
    ],
    [
      "005b34e4",
      "DATA",
      [
        "storage",
        "00c6ffe0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3520",
      "READ",
      [
        "storage",
        "00c70000",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b34e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3464.md#insn-005b34e4) · [`005b3488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3464.md#insn-005b3488) · [`005b349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3464.md#insn-005b349c)
- 新版 [`005b3524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b34a4.md#insn-005b3524) · [`005b34c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b34a4.md#insn-005b34c8) · [`005b34dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b34a4.md#insn-005b34dc)

~~~diff
- 005b34e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b34e4 ["INT_ADD", "register:40f0:8", ["const:5b34e4:8", "const:4:8"]]
- 005b34e4 ["CALLIND", null, ["register:0:8"]]
+ 005b3524 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b3524 ["INT_ADD", "register:40f0:8", ["const:5b3524:8", "const:4:8"]]
+ 005b3524 ["CALLIND", null, ["register:0:8"]]
- 005b34e4 bytes 00013fd6
+ 005b3524 bytes 00013fd6
- 005b3488 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 005b3488 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b3488 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b3488 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b34c8 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 005b34c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b34c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b34c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b3488 bytes 08812d91
+ 005b34c8 bytes 08813d91
- 005b349c ["COPY", "tmp:0:8", ["const:be0:8"]]
- 005b349c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b349c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b349c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b34dc ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 005b34dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b34dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b34dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b349c bytes 08812f91
+ 005b34dc bytes 08813f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9bed1fb304910e3e18af66719350a2e"></a>

### [`005b35b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b35b8.md) → [`005b35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md) FUN_005b35f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b3464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3464.md) · 呼出先 13件 [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`0059d314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059d/0059d314.md) [`005b7cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7cb8.md) [`005b8004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8004.md)
- 新版 呼出元 1件 [`005b34a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b34a4.md) · 呼出先 13件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059d354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d354.md) [`005b7cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7cf8.md) [`005b8044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8044.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.60% / 新版 97.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b3734",
      "incomplete_value": false,
      "site": "005b3738",
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
      "definition_site": "005b36f4",
      "incomplete_value": false,
      "site": "005b36f8",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b37c8",
      "incomplete_value": false,
      "site": "005b37c8",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3788",
      "incomplete_value": false,
      "site": "005b3788",
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
            "const:320:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b3738",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ],
    [
      "005b37c8",
      "DATA",
      [
        "storage",
        "00c70320",
        null,
        "undefined *"
      ]
    ],
    [
      "005b383c",
      "READ",
      [
        "storage",
        "00c70348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b3738",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "005b37c8",
      "DATA",
      [
        "storage",
        "00c70720",
        null,
        "undefined *"
      ]
    ],
    [
      "005b383c",
      "READ",
      [
        "storage",
        "00c70748",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b36b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b35b8.md#insn-005b36b8) · [`005b3668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b35b8.md#insn-005b3668) · [`005b36a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b35b8.md#insn-005b36a4)
- 新版 [`005b36f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md#insn-005b36f8) · [`005b36a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md#insn-005b36a8) · [`005b36e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md#insn-005b36e4)

~~~diff
- 005b36b8 ["INT_ADD", "register:40f0:8", ["const:5b36b8:8", "const:4:8"]]
- 005b36b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b36f8 ["INT_ADD", "register:40f0:8", ["const:5b36f8:8", "const:4:8"]]
+ 005b36f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b36b8 bytes fe901a94
+ 005b36f8 bytes ee911a94
- 005b3668 ["INT_ADD", "register:40f0:8", ["const:5b3668:8", "const:4:8"]]
- 005b3668 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b36a8 ["INT_ADD", "register:40f0:8", ["const:5b36a8:8", "const:4:8"]]
+ 005b36a8 ["CALL", null, ["callee:00c57e90:8"]]
- 005b3668 bytes 0a911a94
+ 005b36a8 bytes fa911a94
- 005b36a4 ["INT_ADD", "register:40f0:8", ["const:5b36a4:8", "const:4:8"]]
- 005b36a4 ["CALL", null, ["callee:0059d354:8"]]
+ 005b36e4 ["INT_ADD", "register:40f0:8", ["const:5b36e4:8", "const:4:8"]]
+ 005b36e4 ["CALL", null, ["callee:0059d354:8"]]
- 005b36a4 bytes 1ca7ff97
+ 005b36e4 bytes 1ca7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-393e9b207be1f1e9c8344b7f94fdb235"></a>

### [`005b39e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b39e8.md) → [`005b3a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3a28.md) FUN_005b3a28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · 呼出先 6件 [`005b3b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3b34.md) [`005b6420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6420.md) [`005b6424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6424.md) [`005b6718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6718.md) [`005b671c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b671c.md)
- 新版 呼出元 1件 [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) · 呼出先 6件 [`005b3b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md) [`005b6460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6460.md) [`005b6464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6464.md) [`005b6758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6758.md) [`005b675c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b675c.md)

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
      "definition_site": "005b3a50",
      "incomplete_value": false,
      "site": "005b3a50",
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
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3a10",
      "incomplete_value": false,
      "site": "005b3a10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "definition_site": "005b3a64",
      "incomplete_value": true,
      "site": "005b3a64",
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
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3a24",
      "incomplete_value": true,
      "site": "005b3a24",
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
            "const:d40:8"
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
      "005b3a50",
      "DATA",
      [
        "storage",
        "00c6fc60",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3a64",
      "DATA",
      [
        "storage",
        "00c6fd40",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3a9c",
      "READ",
      [
        "storage",
        "00c6fd60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b3a50",
      "DATA",
      [
        "storage",
        "00c70060",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3a64",
      "DATA",
      [
        "storage",
        "00c70140",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3a9c",
      "READ",
      [
        "storage",
        "00c70160",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b3a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b39e8.md#insn-005b3a08) · [`005b3a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b39e8.md#insn-005b3a0c) · [`005b3a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b39e8.md#insn-005b3a1c)
- 新版 [`005b3a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3a28.md#insn-005b3a48) · [`005b3a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3a28.md#insn-005b3a4c) · [`005b3a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3a28.md#insn-005b3a5c)

~~~diff
- 005b3a08 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b3a48 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b3a08 bytes e8350090
+ 005b3a48 bytes e83500b0
- 005b3a0c ["COPY", "tmp:0:8", ["const:c60:8"]]
- 005b3a0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b3a0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b3a0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b3a4c ["COPY", "tmp:0:8", ["const:60:8"]]
+ 005b3a4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3a4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3a4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b3a0c bytes 08813191
+ 005b3a4c bytes 08810191
- 005b3a1c ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b3a5c ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b3a1c bytes e8350090
+ 005b3a5c bytes e83500b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93863c22c46bede71775b64e9fdb8926"></a>

### [`005b3b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3b34.md) → [`005b3b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md) FUN_005b3b74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b39e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b39e8.md) · 呼出先 13件 [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md) [`005b7144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7144.md) [`005b74e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b74e0.md)
- 新版 呼出元 1件 [`005b3a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3a28.md) · 呼出先 13件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md) [`005b7184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7184.md) [`005b7520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7520.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.25% / 新版 96.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b3c44",
      "incomplete_value": false,
      "site": "005b3c44",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3c04",
      "incomplete_value": false,
      "site": "005b3c04",
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
            "const:210:8"
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
      "definition_site": "005b3da0",
      "incomplete_value": false,
      "site": "005b3da4",
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
      "definition_site": "005b3d60",
      "incomplete_value": false,
      "site": "005b3d64",
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
      "005b3bcc",
      "DATA",
      [
        "storage",
        "00c6d9e8",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3c44",
      "DATA",
      [
        "storage",
        "00c70210",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3cb8",
      "READ",
      [
        "storage",
        "00c70238",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b3bcc",
      "DATA",
      [
        "storage",
        "00c6dde8",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3c44",
      "DATA",
      [
        "storage",
        "00c70610",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3cb8",
      "READ",
      [
        "storage",
        "00c70638",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b3b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3b34.md#insn-005b3b60) · [`005b3b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3b34.md#insn-005b3b78) · [`005b3b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3b34.md#insn-005b3b80)
- 新版 [`005b3ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md#insn-005b3ba0) · [`005b3bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md#insn-005b3bb8) · [`005b3bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md#insn-005b3bc0)

~~~diff
- 005b3b60 ["INT_ADD", "register:40f0:8", ["const:5b3b60:8", "const:4:8"]]
- 005b3b60 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b3ba0 ["INT_ADD", "register:40f0:8", ["const:5b3ba0:8", "const:4:8"]]
+ 005b3ba0 ["CALL", null, ["callee:00c57e90:8"]]
- 005b3b60 bytes cc8f1a94
+ 005b3ba0 bytes bc901a94
- 005b3b78 ["INT_ADD", "register:40f0:8", ["const:5b3b78:8", "const:4:8"]]
- 005b3b78 ["CALL", null, ["callee:0059b908:8"]]
+ 005b3bb8 ["INT_ADD", "register:40f0:8", ["const:5b3bb8:8", "const:4:8"]]
+ 005b3bb8 ["CALL", null, ["callee:0059b908:8"]]
- 005b3b78 bytes 549fff97
+ 005b3bb8 bytes 549fff97
- 005b3b80 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 005b3b80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b3b80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b3b80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b3bc0 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 005b3bc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3bc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3bc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b3b80 bytes 08612791
+ 005b3bc0 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e462b289c4ab09e6a0a878e0db40bfb9"></a>

### [`005b3e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3e94.md) → [`005b3ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3ed4.md) FUN_005b3ed4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b5b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5b6c.md) · 呼出先 6件 [`005b3fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3fe0.md) [`005b67b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b67b0.md) [`005b67b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b67b4.md) [`005b6838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6838.md) [`005b683c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b683c.md)
- 新版 呼出元 1件 [`005b5bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5bac.md) · 呼出先 6件 [`005b4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md) [`005b67f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b67f0.md) [`005b67f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b67f4.md) [`005b6878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6878.md) [`005b687c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b687c.md)

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
      "definition_site": "005b3efc",
      "incomplete_value": false,
      "site": "005b3efc",
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
    "old": {
      "definition_site": "005b3ebc",
      "incomplete_value": false,
      "site": "005b3ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
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
      "definition_site": "005b3f10",
      "incomplete_value": false,
      "site": "005b3f10",
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
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3ed0",
      "incomplete_value": false,
      "site": "005b3ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "005b3efc",
      "DATA",
      [
        "storage",
        "00c6fdc0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3f10",
      "DATA",
      [
        "storage",
        "00c6fe50",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3f48",
      "READ",
      [
        "storage",
        "00c6fe70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b3efc",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3f10",
      "DATA",
      [
        "storage",
        "00c70250",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3f48",
      "READ",
      [
        "storage",
        "00c70270",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b3eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3e94.md#insn-005b3eb4) · [`005b3eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3e94.md#insn-005b3eb8) · [`005b3ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3e94.md#insn-005b3ec8)
- 新版 [`005b3ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3ed4.md#insn-005b3ef4) · [`005b3ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3ed4.md#insn-005b3ef8) · [`005b3f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3ed4.md#insn-005b3f08)

~~~diff
- 005b3eb4 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b3ef4 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b3eb4 bytes e8350090
+ 005b3ef4 bytes e83500b0
- 005b3eb8 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 005b3eb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b3eb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b3eb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b3ef8 ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 005b3ef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3ef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3ef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b3eb8 bytes 08013791
+ 005b3ef8 bytes 08010791
- 005b3ec8 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b3f08 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b3ec8 bytes e8350090
+ 005b3f08 bytes e83500b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf35ec53ed97fe747954d4a14855c27e"></a>

### [`005b3fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3fe0.md) → [`005b4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md) FUN_005b4020

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b3e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3e94.md) · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`0059eb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059e/0059eb20.md) [`005b8480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8480.md)
- 新版 呼出元 1件 [`005b3ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3ed4.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059eb60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059eb60.md) [`005b84c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b84c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b40dc",
      "incomplete_value": false,
      "site": "005b40e0",
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
      "definition_site": "005b409c",
      "incomplete_value": false,
      "site": "005b40a0",
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b416c",
      "incomplete_value": true,
      "site": "005b416c",
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
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b412c",
      "incomplete_value": true,
      "site": "005b412c",
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
            "const:420:8"
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
      "005b40e0",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ],
    [
      "005b416c",
      "DATA",
      [
        "storage",
        "00c70420",
        null,
        "undefined *"
      ]
    ],
    [
      "005b41e0",
      "READ",
      [
        "storage",
        "00c70448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b40e0",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "005b416c",
      "DATA",
      [
        "storage",
        "00c70820",
        null,
        "undefined *"
      ]
    ],
    [
      "005b41e0",
      "READ",
      [
        "storage",
        "00c70848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3fe0.md#insn-005b4060) · [`005b4014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3fe0.md#insn-005b4014) · [`005b4040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3fe0.md#insn-005b4040)
- 新版 [`005b40a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md#insn-005b40a0) · [`005b4054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md#insn-005b4054) · [`005b4080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md#insn-005b4080)

~~~diff
- 005b4060 ["INT_ADD", "register:40f0:8", ["const:5b4060:8", "const:4:8"]]
- 005b4060 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b40a0 ["INT_ADD", "register:40f0:8", ["const:5b40a0:8", "const:4:8"]]
+ 005b40a0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b4060 bytes 948e1a94
+ 005b40a0 bytes 848f1a94
- 005b4014 ["INT_ADD", "register:40f0:8", ["const:5b4014:8", "const:4:8"]]
- 005b4014 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b4054 ["INT_ADD", "register:40f0:8", ["const:5b4054:8", "const:4:8"]]
+ 005b4054 ["CALL", null, ["callee:00c57e90:8"]]
- 005b4014 bytes 9f8e1a94
+ 005b4054 bytes 8f8f1a94
- 005b4040 ["INT_ADD", "register:40f0:8", ["const:5b4040:8", "const:4:8"]]
- 005b4040 ["CALL", null, ["callee:0043bb20:8"]]
+ 005b4080 ["INT_ADD", "register:40f0:8", ["const:5b4080:8", "const:4:8"]]
+ 005b4080 ["CALL", null, ["callee:0043bb20:8"]]
- 005b4040 bytes a81efa97
+ 005b4080 bytes a81efa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84c89636114d4f4c193b777a1e93a74a"></a>

### [`005b438c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b438c.md) → [`005b43cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b43cc.md) FUN_005b43cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b67b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b67b8.md) · 呼出先 8件 [`005b4550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4550.md) [`005b68d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b68d0.md) [`005b68d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b68d4.md) [`005b6af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6af0.md) [`005b6af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6af4.md)
- 新版 呼出元 1件 [`005b67f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b67f8.md) · 呼出先 8件 [`005b4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md) [`005b6910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6910.md) [`005b6914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6914.md) [`005b6b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6b30.md) [`005b6b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6b34.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b43f4",
      "incomplete_value": false,
      "site": "005b43f4",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b43b4",
      "incomplete_value": false,
      "site": "005b43b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "005b4408",
      "incomplete_value": false,
      "site": "005b4408",
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
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b43c8",
      "incomplete_value": false,
      "site": "005b43c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:f60:8"
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
      "definition_site": "005b441c",
      "incomplete_value": false,
      "site": "005b441c",
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
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b43dc",
      "incomplete_value": false,
      "site": "005b43dc",
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
            "const:40:8"
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
      "005b43f4",
      "DATA",
      [
        "storage",
        "00c6fed0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4408",
      "DATA",
      [
        "storage",
        "00c6ff60",
        null,
        "undefined *"
      ]
    ],
    [
      "005b441c",
      "DATA",
      [
        "storage",
        "00c70040",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b43f4",
      "DATA",
      [
        "storage",
        "00c702d0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4408",
      "DATA",
      [
        "storage",
        "00c70360",
        null,
        "undefined *"
      ]
    ],
    [
      "005b441c",
      "DATA",
      [
        "storage",
        "00c70440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b441c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b438c.md#insn-005b441c) · [`005b43ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b438c.md#insn-005b43ac) · [`005b43b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b438c.md#insn-005b43b0)
- 新版 [`005b445c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b43cc.md#insn-005b445c) · [`005b43ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b43cc.md#insn-005b43ec) · [`005b43f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b43cc.md#insn-005b43f0)

~~~diff
- 005b441c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b441c ["INT_ADD", "register:40f0:8", ["const:5b441c:8", "const:4:8"]]
- 005b441c ["CALLIND", null, ["register:0:8"]]
+ 005b445c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b445c ["INT_ADD", "register:40f0:8", ["const:5b445c:8", "const:4:8"]]
+ 005b445c ["CALLIND", null, ["register:0:8"]]
- 005b441c bytes 00013fd6
+ 005b445c bytes 00013fd6
- 005b43ac ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b43ec ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b43ac bytes c83500f0
+ 005b43ec bytes e8350090
- 005b43b0 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 005b43b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b43b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b43b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b43f0 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 005b43f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b43f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b43f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b43b0 bytes 08413b91
+ 005b43f0 bytes 08410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-203eca39be07bad9f978b7ffdfdc49ea"></a>

### [`005b4550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4550.md) → [`005b4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md) FUN_005b4590

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b438c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b438c.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`005a0628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a0/005a0628.md) [`005ad2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad2ac.md) [`005ad378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad378.md)
- 新版 呼出元 1件 [`005b43cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b43cc.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`005a0668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0668.md) [`005ad2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad2ec.md) [`005ad3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad3b8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.21% / 新版 97.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4650",
      "incomplete_value": false,
      "site": "005b4654",
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
      "definition_site": "005b4610",
      "incomplete_value": false,
      "site": "005b4614",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b46e0",
      "incomplete_value": false,
      "site": "005b46e0",
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
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b46a0",
      "incomplete_value": false,
      "site": "005b46a0",
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
            "const:4f0:8"
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
      "005b4654",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ],
    [
      "005b46e0",
      "DATA",
      [
        "storage",
        "00c704f0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4754",
      "READ",
      [
        "storage",
        "00c70518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4654",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "005b46e0",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4754",
      "READ",
      [
        "storage",
        "00c70918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b45d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4550.md#insn-005b45d4) · [`005b4588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4550.md#insn-005b4588) · [`005b45b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4550.md#insn-005b45b4)
- 新版 [`005b4614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md#insn-005b4614) · [`005b45c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md#insn-005b45c8) · [`005b45f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md#insn-005b45f4)

~~~diff
- 005b45d4 ["INT_ADD", "register:40f0:8", ["const:5b45d4:8", "const:4:8"]]
- 005b45d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005b4614 ["INT_ADD", "register:40f0:8", ["const:5b4614:8", "const:4:8"]]
+ 005b4614 ["CALL", null, ["callee:00c57eb0:8"]]
- 005b45d4 bytes 378d1a94
+ 005b4614 bytes 278e1a94
- 005b4588 ["INT_ADD", "register:40f0:8", ["const:5b4588:8", "const:4:8"]]
- 005b4588 ["CALL", null, ["callee:00c57e90:8"]]
+ 005b45c8 ["INT_ADD", "register:40f0:8", ["const:5b45c8:8", "const:4:8"]]
+ 005b45c8 ["CALL", null, ["callee:00c57e90:8"]]
- 005b4588 bytes 428d1a94
+ 005b45c8 bytes 328e1a94
- 005b45b4 ["INT_ADD", "register:40f0:8", ["const:5b45b4:8", "const:4:8"]]
- 005b45b4 ["CALL", null, ["callee:0043bb20:8"]]
+ 005b45f4 ["INT_ADD", "register:40f0:8", ["const:5b45f4:8", "const:4:8"]]
+ 005b45f4 ["CALL", null, ["callee:0043bb20:8"]]
- 005b45b4 bytes 4b1dfa97
+ 005b45f4 bytes 4b1dfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80d81d64aad6596ab942df3746dbf340"></a>

### [`005b490c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b490c.md) → [`005b494c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b494c.md) FUN_005b494c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`008a7264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7264.md) · 呼出先 6件 [`005b4a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b4a58.md) [`005b6fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6fd0.md) [`005b6fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b6/005b6fd4.md) [`005b70fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b70fc.md) [`005b7100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7100.md)
- 新版 呼出元 1件 [`008a72a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a72a8.md) · 呼出先 6件 [`005b4a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4a98.md) [`005b7010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7010.md) [`005b7014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7014.md) [`005b713c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b713c.md) [`005b7140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7140.md)

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
      "definition_site": "005b4974",
      "incomplete_value": false,
      "site": "005b4974",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4934",
      "incomplete_value": false,
      "site": "005b4934",
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
            "const:c0:8"
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
      "definition_site": "005b4988",
      "incomplete_value": false,
      "site": "005b4988",
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
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4948",
      "incomplete_value": false,
      "site": "005b4948",
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
            "const:140:8"
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
      "005b4974",
      "DATA",
      [
        "storage",
        "00c700c0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4988",
      "DATA",
      [
        "storage",
        "00c70140",
        null,
        "undefined *"
      ]
    ],
    [
      "005b49c0",
      "READ",
      [
        "storage",
        "00c70160",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b4974",
      "DATA",
      [
        "storage",
        "00c704c0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4988",
      "DATA",
      [
        "storage",
        "00c70540",
        null,
        "undefined *"
      ]
    ],
    [
      "005b49c0",
      "READ",
      [
        "storage",
        "00c70560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b490c.md#insn-005b4930) · [`005b4944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b490c.md#insn-005b4944) · [`005b4958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b4/005b490c.md#insn-005b4958)
- 新版 [`005b4970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b494c.md#insn-005b4970) · [`005b4984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b494c.md#insn-005b4984) · [`005b4998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b494c.md#insn-005b4998)

~~~diff
- 005b4930 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 005b4930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4970 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 005b4970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4930 bytes 08010391
+ 005b4970 bytes 08011391
- 005b4944 ["COPY", "tmp:0:8", ["const:140:8"]]
- 005b4944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4984 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 005b4984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4944 bytes 08010591
+ 005b4984 bytes 08011591
- 005b4958 ["INT_ADD", "register:40f0:8", ["const:5b4958:8", "const:4:8"]]
- 005b4958 ["CALL", null, ["callee:005b4a98:8"]]
+ 005b4998 ["INT_ADD", "register:40f0:8", ["const:5b4998:8", "const:4:8"]]
+ 005b4998 ["CALL", null, ["callee:005b4a98:8"]]
- 005b4958 bytes 40000094
+ 005b4998 bytes 40000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

