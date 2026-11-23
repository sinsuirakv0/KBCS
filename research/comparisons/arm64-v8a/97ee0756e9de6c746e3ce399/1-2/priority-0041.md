# v15.7.3 → v15.7.4 · 最優先の変更候補 (41)

[一覧の目次](README.md)

<a id="compare-c0029521af11fbb0c9c7fe64c06dd828"></a>

### [`008499bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/008499bc.md) → [`008499bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/008499bc.md) FUN_008499bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084859c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/0084859c.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`0084859c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/0084859c.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "008499ec",
      "incomplete_value": false,
      "site": "008499ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008499ec",
      "incomplete_value": false,
      "site": "008499ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:300:8"
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
      "008499ec",
      "DATA",
      [
        "storage",
        "00c02300",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008499ec",
      "DATA",
      [
        "storage",
        "00c02350",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008499e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/008499bc.md#insn-008499e4)
- 新版 `008499e4`（命令位置の公開資料なし）

~~~diff
- 008499e4 ["COPY", "tmp:0:8", ["const:300:8"]]
- 008499e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008499e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008499e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008499e4 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 008499e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008499e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008499e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008499e4 bytes 08010c91
+ 008499e4 bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf416aa4e02e055a6293b0d17b53c96b"></a>

### [`00849ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849ac4.md) → [`00849ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849ac4.md) FUN_00849ac4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

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
      "definition_site": "00849aec",
      "incomplete_value": false,
      "site": "00849aec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00849aec",
      "incomplete_value": false,
      "site": "00849aec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:300:8"
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
      "00849aec",
      "DATA",
      [
        "storage",
        "00c02300",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00849aec",
      "DATA",
      [
        "storage",
        "00c02350",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00849ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849ac4.md#insn-00849ae4) · [`00849ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849ac4.md#insn-00849ae8)
- 新版 `00849ae4`（命令位置の公開資料なし） · `00849ae8`（命令位置の公開資料なし）

~~~diff
- 00849ae4 ["COPY", "tmp:0:8", ["const:300:8"]]
- 00849ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00849ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00849ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00849ae4 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 00849ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00849ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00849ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00849ae4 bytes 08010c91
+ 00849ae4 bytes 08410d91
- 00849ae8 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 00849ae8 bytes f40301aa
+ 00849ae8 ["COPY", "register:40a0:8", ["register:4008:8"]]
+ 00849ae8 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2410079e2865f1ea582eff975f4fad1b"></a>

### [`00849cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849cd4.md) → [`00849cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849cd4.md) FUN_00849cd4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00849d48",
      "incomplete_value": true,
      "site": "00849d60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:43:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00849d48",
      "incomplete_value": true,
      "site": "00849d60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d0:8"
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
      "definition_site": "00849d48",
      "incomplete_value": true,
      "site": "00849d60",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00849d48",
      "incomplete_value": true,
      "site": "00849d60",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00849d64",
      "incomplete_value": true,
      "site": "00849d70",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00849d64",
      "incomplete_value": true,
      "site": "00849d70",
      "value": [
        "LOAD",
        "16",
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
      "00849d48",
      "READ",
      [
        "storage",
        "002970d0",
        null,
        null
      ]
    ],
    [
      "00849d48",
      "READ",
      [
        "storage",
        "002970e0",
        null,
        null
      ]
    ],
    [
      "00849d64",
      "READ",
      [
        "storage",
        "002970f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00849d48",
      "READ",
      [
        "storage",
        "00297043",
        null,
        null
      ]
    ],
    [
      "00849d48",
      "READ",
      [
        "storage",
        "00297053",
        null,
        null
      ]
    ],
    [
      "00849d64",
      "READ",
      [
        "storage",
        "00297063",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00849d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849cd4.md#insn-00849d40) · [`00849d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849cd4.md#insn-00849d44)
- 新版 `00849d40`（命令位置の公開資料なし） · `00849d44`（命令位置の公開資料なし）

~~~diff
- 00849d40 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 00849d40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00849d40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00849d40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00849d40 ["COPY", "tmp:0:8", ["const:43:8"]]
+ 00849d40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00849d40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00849d40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00849d40 bytes 29410391
+ 00849d40 bytes 290d0191
- 00849d44 ["COPY", "register:4050:8", ["const:2b0000:8"]]
- 00849d44 bytes 2ad3fff0
+ 00849d44 ["COPY", "register:4050:8", ["const:2b0000:8"]]
+ 00849d44 bytes 2ad3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abc9f79e663dc6abeaa893926b6e62a0"></a>

### [`00849e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849e98.md) → [`00849e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849e98.md) _INIT_156

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 77.29% / 新版 77.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 10件, `store_value` 8件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00849ed4",
      "incomplete_value": true,
      "site": "00849ef0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00849ed4",
      "incomplete_value": true,
      "site": "00849ef0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dd:8"
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
      "definition_site": "00849ef8",
      "incomplete_value": true,
      "site": "00849f14",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00849ef8",
      "incomplete_value": true,
      "site": "00849f14",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f0:8"
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
      "definition_site": "00849f18",
      "incomplete_value": true,
      "site": "00849f34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00849f18",
      "incomplete_value": true,
      "site": "00849f34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
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
      "00849ed4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00849ef8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00849f18",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00849ed4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00849ef8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00849f18",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084a0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849e98.md#insn-0084a0d0) · [`0084a10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00849/00849e98.md#insn-0084a10c)
- 新版 `0084a0d0`（命令位置の公開資料なし）

~~~diff
- 0084a0d0 ["INT_ADD", "register:40f0:8", ["const:84a0d0:8", "const:4:8"]]
- 0084a0d0 ["CALL", null, ["callee:00bdafe0:8"]]
- 0084a0d0 bytes b0430e94
+ 0084a0d0 ["INT_ADD", "register:40f0:8", ["const:84a0d0:8", "const:4:8"]]
+ 0084a0d0 ["CALL", null, ["callee:00bdafe0:8"]]
+ 0084a0d0 bytes c4430e94
- 0084a10c ["INT_ADD", "register:40f0:8", ["const:84a10c:8", "const:4:8"]]
- 0084a10c ["CALL", null, ["callee:00bdafe0:8"]]
- 0084a10c bytes a1430e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceb68d1a3a303246439c425c5bf17768"></a>

### [`0084a534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084a/0084a534.md) → [`0084a534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a534.md) FUN_0084a534

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0082f3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082f/0082f3d0.md) · 呼出先 6件 [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddab0.md)
- 新版 呼出元 1件 [`0082f3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082f/0082f3d0.md) · 呼出先 6件 [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb00.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "0084a570",
      "incomplete_value": false,
      "site": "0084a578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084a570",
      "incomplete_value": false,
      "site": "0084a578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:390:8"
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
      "0084a578",
      "DATA",
      [
        "storage",
        "00c02390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084a578",
      "DATA",
      [
        "storage",
        "00c023e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084a570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084a/0084a534.md#insn-0084a570) · [`0084a574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084a/0084a534.md#insn-0084a574)
- 新版 `0084a570`（命令位置の公開資料なし） · `0084a574`（命令位置の公開資料なし）

~~~diff
- 0084a570 ["COPY", "tmp:0:8", ["const:390:8"]]
- 0084a570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084a570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084a570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084a570 ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 0084a570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084a570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084a570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084a570 bytes 08410e91
+ 0084a570 bytes 08810f91
- 0084a574 ["COPY", "register:4000:8", ["register:4098:8"]]
- 0084a574 bytes e00313aa
+ 0084a574 ["COPY", "register:4000:8", ["register:4098:8"]]
+ 0084a574 bytes e00313aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3891023ecd5ec43404cd2d1af04584f6"></a>

### [`0084a588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084a/0084a588.md) → [`0084a588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a588.md) _INIT_157

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084a5c4",
      "incomplete_value": true,
      "site": "0084a5e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084a5c4",
      "incomplete_value": true,
      "site": "0084a5e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dd:8"
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
      "definition_site": "0084a5e8",
      "incomplete_value": true,
      "site": "0084a604",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084a5e8",
      "incomplete_value": true,
      "site": "0084a604",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f0:8"
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
      "definition_site": "0084a608",
      "incomplete_value": true,
      "site": "0084a624",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084a608",
      "incomplete_value": true,
      "site": "0084a624",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
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
      "0084a5c4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0084a5e8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0084a608",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0084a5c4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0084a5e8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0084a608",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084a5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084a/0084a588.md#insn-0084a5b4) · [`0084a5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084a/0084a588.md#insn-0084a5bc)
- 新版 `0084a5b4`（命令位置の公開資料なし） · `0084a5bc`（命令位置の公開資料なし）

~~~diff
- 0084a5b4 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 0084a5b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0084a5b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0084a5b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0084a5b4 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0084a5b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0084a5b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0084a5b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0084a5b4 bytes 73a20f91
+ 0084a5b4 bytes 73a21091
- 0084a5bc ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0084a5bc bytes e9d2ffb0
+ 0084a5bc ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0084a5bc bytes e9d2ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0b9c22a2efbbf5b92e3b536f6df2311"></a>

### [`0084ad38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084a/0084ad38.md) → [`0084ad38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084ad38.md) _INIT_158

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0084ac4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084a/0084ac4c.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0084ac4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084ac4c.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md)

変更の種類 call, call_argument_candidate, call_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 53.63% / 新版 53.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 35件, `store_destination` 48件, `store_value` 24件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084ad80",
      "incomplete_value": true,
      "site": "0084ad9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084ad80",
      "incomplete_value": true,
      "site": "0084ad9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dd:8"
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
      "definition_site": "0084ada4",
      "incomplete_value": true,
      "site": "0084adc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084ada4",
      "incomplete_value": true,
      "site": "0084adc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f0:8"
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
      "definition_site": "0084adc4",
      "incomplete_value": true,
      "site": "0084ade0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084adc4",
      "incomplete_value": true,
      "site": "0084ade0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
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
      "0084ad80",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0084ada4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0084adc4",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0084ad80",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0084ada4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0084adc4",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084b078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084a/0084ad38.md#insn-0084b078) · [`0084ad70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084a/0084ad38.md#insn-0084ad70)
- 新版 `0084b078`（命令位置の公開資料なし） · `0084ad70`（命令位置の公開資料なし）

~~~diff
- 0084b078 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0084b078 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0084b078 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:19:8"]]
- 0084b078 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0084b078 bytes 1f640039
+ 0084b078 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0084b078 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0084b078 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:19:8"]]
+ 0084b078 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0084b078 bytes 1f640039
- 0084ad70 ["COPY", "tmp:0:8", ["const:400:8"]]
- 0084ad70 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 0084ad70 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 0084ad70 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 0084ad70 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 0084ad70 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 0084ad70 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 0084ad70 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 0084ad70 bytes 94021091
+ 0084ad70 bytes 94021191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f6e4eb5a18e9a206bec8e9d74f88ecd"></a>

### [`0084b738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084b/0084b738.md) → [`0084b738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b738.md) FUN_0084b738

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0084b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084b/0084b734.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0084bd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084b/0084bd74.md) [`0084c060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c060.md)
- 新版 呼出元 1件 [`0084b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b734.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0084bd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bd74.md) [`0084c060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c060.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "0084b8d8",
      "incomplete_value": false,
      "site": "0084b8e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084b8d8",
      "incomplete_value": false,
      "site": "0084b8e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "0084b7c0",
      "READ",
      [
        "storage",
        "0109e4f8",
        null,
        "undefined1"
      ]
    ],
    [
      "0084b7c0",
      "READ",
      [
        "storage",
        "0109e510",
        null,
        "undefined1"
      ]
    ],
    [
      "0084b7c8",
      "READ",
      [
        "storage",
        "0109e4f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0084b7c0",
      "READ",
      [
        "storage",
        "0109e538",
        null,
        "undefined1"
      ]
    ],
    [
      "0084b7c0",
      "READ",
      [
        "storage",
        "0109e550",
        null,
        "undefined1"
      ]
    ],
    [
      "0084b7c8",
      "READ",
      [
        "storage",
        "0109e538",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084b7b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084b/0084b738.md#insn-0084b7b8) · [`0084b8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084b/0084b738.md#insn-0084b8d8) · [`0084b8dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084b/0084b738.md#insn-0084b8dc)
- 新版 `0084b7b8`（命令位置の公開資料なし） · `0084b8d8`（命令位置の公開資料なし）

~~~diff
- 0084b7b8 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 0084b7b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084b7b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084b7b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084b7b8 ["COPY", "tmp:0:8", ["const:538:8"]]
+ 0084b7b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084b7b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084b7b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084b7b8 bytes 08e11391
+ 0084b7b8 bytes 08e11491
- 0084b8d8 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 0084b8d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084b8d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084b8d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084b8d8 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0084b8d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084b8d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084b8d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084b8d8 bytes 08610f91
+ 0084b8d8 bytes 08a11091
- 0084b8dc ["COPY", "register:40b0:8", ["register:4000:8"]]
- 0084b8dc bytes f60300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-014ce9384e38f2f20498bbf7803271e4"></a>

### [`0084c020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c020.md) → [`0084c020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c020.md) FUN_0084c020

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0084c024",
      "incomplete_value": false,
      "site": "0084c028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084c024",
      "incomplete_value": false,
      "site": "0084c028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "0084c028",
      "DATA",
      [
        "storage",
        "00c023d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0084c028",
      "DATA",
      [
        "storage",
        "00c02428",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084c024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c020.md#insn-0084c024)
- 新版 `0084c024`（命令位置の公開資料なし）

~~~diff
- 0084c024 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 0084c024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084c024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084c024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084c024 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0084c024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084c024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084c024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084c024 bytes 08610f91
+ 0084c024 bytes 08a11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae226cd7c3ff5dbde8403dcd2959ca73"></a>

### [`0084c030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c030.md) → [`0084c030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c030.md) FUN_0084c030

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0084c040",
      "incomplete_value": false,
      "site": "0084c048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084c040",
      "incomplete_value": false,
      "site": "0084c048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "0084c048",
      "DATA",
      [
        "storage",
        "00c023d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0084c048",
      "DATA",
      [
        "storage",
        "00c02428",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084c040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c030.md#insn-0084c040)
- 新版 `0084c040`（命令位置の公開資料なし）

~~~diff
- 0084c040 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 0084c040 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084c040 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084c040 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084c040 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0084c040 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084c040 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084c040 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084c040 bytes 08610f91
+ 0084c040 bytes 08a11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0934e4d8a17ecb10b6c8e2f785dfab96"></a>

### [`0084c134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c134.md) → [`0084c134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c134.md) FUN_0084c134

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084c174",
      "incomplete_value": true,
      "site": "0084c188",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d8d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084c174",
      "incomplete_value": true,
      "site": "0084c188",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cf3:8"
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
      "definition_site": "0084c18c",
      "incomplete_value": true,
      "site": "0084c18c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0084c18c",
      "incomplete_value": true,
      "site": "0084c18c",
      "value": [
        "LOAD",
        "8",
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
      "0084c174",
      "READ",
      [
        "storage",
        "002a6cf3",
        null,
        "string"
      ]
    ],
    [
      "0084c17c",
      "READ",
      [
        "storage",
        "002a6d01",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0084c174",
      "READ",
      [
        "storage",
        "002a6d8d",
        null,
        "string"
      ]
    ],
    [
      "0084c17c",
      "READ",
      [
        "storage",
        "002a6d9b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084c170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c134.md#insn-0084c170)
- 新版 `0084c170`（命令位置の公開資料なし）

~~~diff
- 0084c170 ["COPY", "tmp:0:8", ["const:cf3:8"]]
- 0084c170 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084c170 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084c170 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084c170 ["COPY", "tmp:0:8", ["const:d8d:8"]]
+ 0084c170 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084c170 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084c170 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084c170 bytes 29cd3391
+ 0084c170 bytes 29353691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84947ac4df8afb08339d048c18a11fd9"></a>

### [`0084c290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c290.md) → [`0084c290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c290.md) FUN_0084c290

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084c2d4",
      "incomplete_value": true,
      "site": "0084c2e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084c2d4",
      "incomplete_value": true,
      "site": "0084c2e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
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
      "0084c2d4",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0084c2d4",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084c2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c290.md#insn-0084c2cc)
- 新版 `0084c2cc`（命令位置の公開資料なし）

~~~diff
- 0084c2cc ["COPY", "tmp:0:8", ["const:de3:8"]]
- 0084c2cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084c2cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084c2cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084c2cc ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 0084c2cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084c2cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084c2cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084c2cc bytes 298d3791
+ 0084c2cc bytes 29593591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24aac139845317f9e711f292aa8d03f6"></a>

### [`0084c390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c390.md) → [`0084c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) FUN_0084c390

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 55件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`0041cc4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cc4c.md)
- 新版 呼出元 0件  · 呼出先 55件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`0041cc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cc4c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.43% / 新版 95.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 13件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0084c458",
      "incomplete_value": false,
      "site": "0084c458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084c458",
      "incomplete_value": false,
      "site": "0084c458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "definition_site": "0084c4b0",
      "incomplete_value": true,
      "site": "0084c4b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084c4b0",
      "incomplete_value": true,
      "site": "0084c4b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb9:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0084c670",
      "incomplete_value": false,
      "site": "0084c670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084c670",
      "incomplete_value": false,
      "site": "0084c670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "0084c458",
      "DATA",
      [
        "storage",
        "00c02770",
        null,
        "undefined *"
      ]
    ],
    [
      "0084c4a0",
      "READ",
      [
        "storage",
        "002a9bb9",
        null,
        "string"
      ]
    ],
    [
      "0084c670",
      "DATA",
      [
        "storage",
        "00c026f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084c458",
      "DATA",
      [
        "storage",
        "00c027c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0084c4a0",
      "READ",
      [
        "storage",
        "002a9bc8",
        null,
        "string"
      ]
    ],
    [
      "0084c670",
      "DATA",
      [
        "storage",
        "00c02740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084c424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c390.md#insn-0084c424) · [`0084c44c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c390.md#insn-0084c44c) · [`0084c498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c390.md#insn-0084c498)
- 新版 `0084c424`（命令位置の公開資料なし） · `0084c44c`（命令位置の公開資料なし） · `0084c498`（命令位置の公開資料なし）

~~~diff
- 0084c424 ["COPY", "register:4040:8", ["const:4cad:8"]]
+ 0084c424 ["COPY", "register:4040:8", ["const:4cb1:8"]]
- 0084c424 bytes a8958952
+ 0084c424 bytes 28968952
- 0084c44c ["COPY", "tmp:0:8", ["const:770:8"]]
- 0084c44c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084c44c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084c44c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084c44c ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 0084c44c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084c44c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084c44c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084c44c bytes 08c11d91
+ 0084c44c bytes 08011f91
- 0084c498 ["COPY", "tmp:0:8", ["const:bb9:8"]]
- 0084c498 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084c498 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084c498 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084c498 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 0084c498 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084c498 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084c498 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084c498 bytes 29e52e91
+ 0084c498 bytes 29212f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe373b75cbcb58617d3f7fc6f055b58e"></a>

### [`0084d1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d1b4.md) → [`0084d1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d1b4.md) FUN_0084d1b4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084c390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c390.md) · 呼出先 9件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046fd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fd28.md) [`004709fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/004709fc.md)
- 新版 呼出元 1件 [`0084c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) · 呼出先 9件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046fd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fd28.md) [`004709fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/004709fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0084d274",
      "incomplete_value": false,
      "site": "0084d274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084d274",
      "incomplete_value": false,
      "site": "0084d274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "0084d274",
      "DATA",
      [
        "storage",
        "00c024f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0084d2ec",
      "READ",
      [
        "storage",
        "00c02518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084d274",
      "DATA",
      [
        "storage",
        "00c02540",
        null,
        "undefined *"
      ]
    ],
    [
      "0084d2ec",
      "READ",
      [
        "storage",
        "00c02568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084d26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d1b4.md#insn-0084d26c)
- 新版 `0084d26c`（命令位置の公開資料なし）

~~~diff
- 0084d26c ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 0084d26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084d26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084d26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084d26c ["COPY", "tmp:0:8", ["const:540:8"]]
+ 0084d26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084d26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084d26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084d26c bytes 08c11391
+ 0084d26c bytes 08011591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af2660daffb5f58400563cd5f151d1dd"></a>

### [`0084d3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d3e8.md) → [`0084d3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d3e8.md) FUN_0084d3e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0084d404",
      "incomplete_value": true,
      "site": "0084d408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0084d404",
      "incomplete_value": true,
      "site": "0084d408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0084d3fc",
      "READ",
      [
        "storage",
        "00c1ae58",
        null,
        "pointer"
      ]
    ],
    [
      "0084d408",
      "DATA",
      [
        "storage",
        "00be8588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084d3fc",
      "READ",
      [
        "storage",
        "00c1aea8",
        null,
        "pointer"
      ]
    ],
    [
      "0084d408",
      "DATA",
      [
        "storage",
        "00be85d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084d3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d3e8.md#insn-0084d3fc)
- 新版 `0084d3fc`（命令位置の公開資料なし）

~~~diff
- 0084d3fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e58:8"]]
- 0084d3fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0084d3fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
+ 0084d3fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0084d3fc bytes 082d47f9
+ 0084d3fc bytes 085547f9
~~~


<a id="compare-61868b9fb14dc0ce985bcfba2b987d8d"></a>

### [`0084d464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d464.md) → [`0084d464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d464.md) FUN_0084d464

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041cc4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cc4c.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`0045a0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a0c0.md) [`0045a0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a0e0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041cc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cc4c.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`0045a0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a0c0.md) [`0045a0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a0e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084d5b4",
      "incomplete_value": true,
      "site": "0084d5c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084d5b4",
      "incomplete_value": true,
      "site": "0084d5c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
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
      "definition_site": "0084d5f8",
      "incomplete_value": true,
      "site": "0084d60c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084d5f8",
      "incomplete_value": true,
      "site": "0084d60c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
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
      "0084d5b4",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ],
    [
      "0084d5f8",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0084d5b4",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ],
    [
      "0084d5f8",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084d5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d464.md#insn-0084d5ac) · [`0084d5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d464.md#insn-0084d5f0)
- 新版 `0084d5ac`（命令位置の公開資料なし） · `0084d5f0`（命令位置の公開資料なし）

~~~diff
- 0084d5ac ["COPY", "tmp:0:8", ["const:de3:8"]]
- 0084d5ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084d5ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084d5ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084d5ac ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 0084d5ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084d5ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084d5ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084d5ac bytes 298d3791
+ 0084d5ac bytes 29593591
- 0084d5f0 ["COPY", "tmp:0:8", ["const:de3:8"]]
- 0084d5f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084d5f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084d5f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084d5f0 ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 0084d5f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084d5f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084d5f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084d5f0 bytes 298d3791
+ 0084d5f0 bytes 29593591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a731f049a541d6fea08189eedb3edec7"></a>

### [`0084d6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d6d0.md) → [`0084d6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d6d0.md) FUN_0084d6d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 13件 [`00841924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841924.md) [`00851444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851444.md) [`008517f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008517f0.md) [`00852390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852390.md) [`0085274c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/0085274c.md) · 呼出先 15件 [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`0042f000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f000.md) [`0042f610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f610.md) [`00574810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574810.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md)
- 新版 呼出元 13件 [`00841924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841924.md) [`00851444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851444.md) [`008517f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008517f0.md) [`00852390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852390.md) [`0085274c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085274c.md) · 呼出先 15件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`0042f000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f000.md) [`0042f610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md) [`00574810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574810.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.47% / 新版 98.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0084d830",
      "incomplete_value": false,
      "site": "0084d838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084d830",
      "incomplete_value": false,
      "site": "0084d838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "definition_site": "0084d994",
      "incomplete_value": false,
      "site": "0084d99c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084d994",
      "incomplete_value": false,
      "site": "0084d99c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "0084d838",
      "DATA",
      [
        "storage",
        "00c02870",
        null,
        "undefined *"
      ]
    ],
    [
      "0084d8d8",
      "READ",
      [
        "storage",
        "00c02898",
        null,
        "undefined *"
      ]
    ],
    [
      "0084d99c",
      "DATA",
      [
        "storage",
        "00c02a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084d838",
      "DATA",
      [
        "storage",
        "00c028c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0084d8d8",
      "READ",
      [
        "storage",
        "00c028e8",
        null,
        "undefined *"
      ]
    ],
    [
      "0084d99c",
      "DATA",
      [
        "storage",
        "00c02a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084d830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d6d0.md#insn-0084d830) · [`0084d994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d6d0.md#insn-0084d994)
- 新版 `0084d830`（命令位置の公開資料なし） · `0084d994`（命令位置の公開資料なし）

~~~diff
- 0084d830 ["COPY", "tmp:0:8", ["const:870:8"]]
- 0084d830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084d830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084d830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084d830 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 0084d830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084d830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084d830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084d830 bytes 08c12191
+ 0084d830 bytes 08012391
- 0084d994 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0084d994 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084d994 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084d994 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084d994 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0084d994 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084d994 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084d994 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084d994 bytes 08012891
+ 0084d994 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97447295ab7f7fc48176b4ae1ee58d5f"></a>

### [`0084dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084dd1c.md) → [`0084dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md) FUN_0084dd1c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 16件 [`004508a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/004508a4.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`00841a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841a9c.md) [`0084e0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e0c0.md) [`00850afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850afc.md) · 呼出先 14件 [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md) [`0073e07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e07c.md)
- 新版 呼出元 16件 [`004508a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00841a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841a9c.md) [`0084e0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e0c0.md) [`00850afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850afc.md) · 呼出先 14件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md) [`0073e07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e07c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.76% / 新版 98.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0084de60",
      "incomplete_value": false,
      "site": "0084de60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084de60",
      "incomplete_value": false,
      "site": "0084de60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b00:8"
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
      "0084de60",
      "DATA",
      [
        "storage",
        "00c02b00",
        null,
        "undefined *"
      ]
    ],
    [
      "0084defc",
      "READ",
      [
        "storage",
        "00c02b28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084de60",
      "DATA",
      [
        "storage",
        "00c02b50",
        null,
        "undefined *"
      ]
    ],
    [
      "0084defc",
      "READ",
      [
        "storage",
        "00c02b78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084de58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084dd1c.md#insn-0084de58)
- 新版 `0084de58`（命令位置の公開資料なし）

~~~diff
- 0084de58 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 0084de58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084de58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084de58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084de58 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 0084de58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084de58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084de58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084de58 bytes 08012c91
+ 0084de58 bytes 08412d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cd32ae48441577f5b224f7c10003644"></a>

### [`0084e0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e0c0.md) → [`0084e0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e0c0.md) FUN_0084e0c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008629ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00862/008629ec.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0053d984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d984.md) [`0084dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084dd1c.md) [`008531c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/008531c8.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0053d984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d984.md) [`0084dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md) [`008531c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/008531c8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.79% / 新版 97.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0084e190",
      "incomplete_value": false,
      "site": "0084e190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084e190",
      "incomplete_value": false,
      "site": "0084e190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c00:8"
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
      "0084e190",
      "DATA",
      [
        "storage",
        "00c02c00",
        null,
        "undefined *"
      ]
    ],
    [
      "0084e210",
      "READ",
      [
        "storage",
        "00c02c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084e190",
      "DATA",
      [
        "storage",
        "00c02c50",
        null,
        "undefined *"
      ]
    ],
    [
      "0084e210",
      "READ",
      [
        "storage",
        "00c02c78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084e188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e0c0.md#insn-0084e188) · [`0084e18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e0c0.md#insn-0084e18c)
- 新版 `0084e188`（命令位置の公開資料なし） · `0084e18c`（命令位置の公開資料なし）

~~~diff
- 0084e188 ["COPY", "tmp:0:8", ["const:c00:8"]]
- 0084e188 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084e188 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084e188 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084e188 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 0084e188 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084e188 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084e188 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084e188 bytes 29013091
+ 0084e188 bytes 29413191
- 0084e18c ["COPY", "register:40b8:8", ["register:4000:8"]]
- 0084e18c bytes f70300aa
+ 0084e18c ["COPY", "register:40b8:8", ["register:4000:8"]]
+ 0084e18c bytes f70300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ea341a4f25de54366f05432a8064e56"></a>

### [`0084e3d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e3d8.md) → [`0084e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e3d8.md) FUN_0084e3d8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00461338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00461/00461338.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00461338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/00461338.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084e424",
      "incomplete_value": true,
      "site": "0084e424",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084e424",
      "incomplete_value": true,
      "site": "0084e424",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb9:8"
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
      "definition_site": "0084e460",
      "incomplete_value": true,
      "site": "0084e478",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d69:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084e460",
      "incomplete_value": true,
      "site": "0084e478",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:df6:8"
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
      "0084e414",
      "READ",
      [
        "storage",
        "002a9bb9",
        null,
        "string"
      ]
    ],
    [
      "0084e460",
      "READ",
      [
        "storage",
        "00292df6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0084e414",
      "READ",
      [
        "storage",
        "002a9bc8",
        null,
        "string"
      ]
    ],
    [
      "0084e460",
      "READ",
      [
        "storage",
        "00292d69",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084e40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e3d8.md#insn-0084e40c) · [`0084e458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e3d8.md#insn-0084e458)
- 新版 `0084e40c`（命令位置の公開資料なし） · `0084e458`（命令位置の公開資料なし）

~~~diff
- 0084e40c ["COPY", "tmp:0:8", ["const:bb9:8"]]
- 0084e40c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084e40c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084e40c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084e40c ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 0084e40c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084e40c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084e40c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084e40c bytes 29e52e91
+ 0084e40c bytes 29212f91
- 0084e458 ["COPY", "tmp:0:8", ["const:df6:8"]]
- 0084e458 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084e458 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084e458 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084e458 ["COPY", "tmp:0:8", ["const:d69:8"]]
+ 0084e458 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084e458 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084e458 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084e458 bytes 29d93791
+ 0084e458 bytes 29a53591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c15abecad2e42078ce67371879ef176"></a>

### [`0084e5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e5ac.md) → [`0084e5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e5ac.md) FUN_0084e5ac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00461338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00461/00461338.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00461338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/00461338.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084e5f8",
      "incomplete_value": true,
      "site": "0084e5f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084e5f8",
      "incomplete_value": true,
      "site": "0084e5f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb9:8"
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
      "definition_site": "0084e634",
      "incomplete_value": true,
      "site": "0084e64c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d69:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084e634",
      "incomplete_value": true,
      "site": "0084e64c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:df6:8"
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
      "0084e5e8",
      "READ",
      [
        "storage",
        "002a9bb9",
        null,
        "string"
      ]
    ],
    [
      "0084e634",
      "READ",
      [
        "storage",
        "00292df6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0084e5e8",
      "READ",
      [
        "storage",
        "002a9bc8",
        null,
        "string"
      ]
    ],
    [
      "0084e634",
      "READ",
      [
        "storage",
        "00292d69",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084e5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e5ac.md#insn-0084e5e0) · [`0084e62c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e5ac.md#insn-0084e62c)
- 新版 `0084e5e0`（命令位置の公開資料なし） · `0084e62c`（命令位置の公開資料なし）

~~~diff
- 0084e5e0 ["COPY", "tmp:0:8", ["const:bb9:8"]]
- 0084e5e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084e5e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084e5e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084e5e0 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 0084e5e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084e5e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084e5e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084e5e0 bytes 29e52e91
+ 0084e5e0 bytes 29212f91
- 0084e62c ["COPY", "tmp:0:8", ["const:df6:8"]]
- 0084e62c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084e62c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084e62c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084e62c ["COPY", "tmp:0:8", ["const:d69:8"]]
+ 0084e62c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084e62c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084e62c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084e62c bytes 29d93791
+ 0084e62c bytes 29a53591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd49f88dce03a52505d569a4feaa2f5d"></a>

### [`0084e780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e780.md) → [`0084e780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e780.md) FUN_0084e780

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`00431534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431534.md) [`0043344c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/0043344c.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`00431534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md) [`0043344c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/0043344c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084e7ec",
      "incomplete_value": true,
      "site": "0084e7ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084e7ec",
      "incomplete_value": true,
      "site": "0084e7ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f95:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0084e994",
      "incomplete_value": false,
      "site": "0084e994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084e994",
      "incomplete_value": false,
      "site": "0084e994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "definition_site": "0084ea64",
      "incomplete_value": false,
      "site": "0084ea68",
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
                "const:be8000:8"
              ],
              [
                "leaf",
                "const:570:8"
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
      "definition_site": "0084ea64",
      "incomplete_value": false,
      "site": "0084ea68",
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
                "const:be8000:8"
              ],
              [
                "leaf",
                "const:520:8"
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
      "0084e7dc",
      "READ",
      [
        "storage",
        "00291f95",
        null,
        "string"
      ]
    ],
    [
      "0084e994",
      "DATA",
      [
        "storage",
        "00c02d10",
        null,
        "undefined *"
      ]
    ],
    [
      "0084e9dc",
      "READ",
      [
        "storage",
        "00c02d30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0084e7dc",
      "READ",
      [
        "storage",
        "00291f08",
        null,
        "string"
      ]
    ],
    [
      "0084e994",
      "DATA",
      [
        "storage",
        "00c02d60",
        null,
        "undefined *"
      ]
    ],
    [
      "0084e9dc",
      "READ",
      [
        "storage",
        "00c02d80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084e7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e780.md#insn-0084e7d4) · [`0084e98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e780.md#insn-0084e98c) · [`0084ea5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e780.md#insn-0084ea5c)
- 新版 `0084e7d4`（命令位置の公開資料なし） · `0084e98c`（命令位置の公開資料なし） · `0084ea5c`（命令位置の公開資料なし）

~~~diff
- 0084e7d4 ["COPY", "tmp:0:8", ["const:f95:8"]]
- 0084e7d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084e7d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084e7d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084e7d4 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 0084e7d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084e7d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084e7d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084e7d4 bytes 29553e91
+ 0084e7d4 bytes 29213c91
- 0084e98c ["COPY", "tmp:0:8", ["const:d10:8"]]
- 0084e98c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084e98c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084e98c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084e98c ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 0084e98c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084e98c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084e98c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084e98c bytes 08413491
+ 0084e98c bytes 08813591
- 0084ea5c ["COPY", "tmp:0:8", ["const:520:8"]]
- 0084ea5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084ea5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084ea5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084ea5c ["COPY", "tmp:0:8", ["const:570:8"]]
+ 0084ea5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084ea5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084ea5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084ea5c bytes 08811491
+ 0084ea5c bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8548e72ae3ec6cdd08145b1ca3d3bf22"></a>

### [`0084eca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084eca4.md) → [`0084eca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084eca4.md) FUN_0084eca4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084ece0",
      "incomplete_value": true,
      "site": "0084ecf4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084ece0",
      "incomplete_value": true,
      "site": "0084ecf4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
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
      "0084ece0",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0084ece0",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084ecd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084eca4.md#insn-0084ecd8)
- 新版 `0084ecd8`（命令位置の公開資料なし）

~~~diff
- 0084ecd8 ["COPY", "tmp:0:8", ["const:de3:8"]]
- 0084ecd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084ecd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084ecd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084ecd8 ["COPY", "tmp:0:8", ["const:d56:8"]]
+ 0084ecd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084ecd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084ecd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084ecd8 bytes 298d3791
+ 0084ecd8 bytes 29593591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf4b5ef85193809cf4e0f569e9ac3dfb"></a>

### [`0084eda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084eda4.md) → [`0084eda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084eda4.md) FUN_0084eda4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00574fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fe4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00845f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00845/00845f8c.md) [`00855df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855df0.md) [`009bd60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd60c.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00574fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fe4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00845f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845f8c.md) [`00855df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855df0.md) [`009bd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd618.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.12% / 新版 96.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084eed0",
      "incomplete_value": true,
      "site": "0084eed0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:983:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084eed0",
      "incomplete_value": true,
      "site": "0084eed0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084eec4",
      "incomplete_value": true,
      "site": "0084eed4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0084eec4",
      "incomplete_value": true,
      "site": "0084eed4",
      "value": [
        "LOAD",
        "8",
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
      "0084eec0",
      "READ",
      [
        "storage",
        "002a08f8",
        null,
        "string"
      ]
    ],
    [
      "0084eec4",
      "READ",
      [
        "storage",
        "002a08ff",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0084eec0",
      "READ",
      [
        "storage",
        "002a0983",
        null,
        "string"
      ]
    ],
    [
      "0084eec4",
      "READ",
      [
        "storage",
        "002a098a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084eeb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084eda4.md#insn-0084eeb8)
- 新版 `0084eeb8`（命令位置の公開資料なし）

~~~diff
- 0084eeb8 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 0084eeb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084eeb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084eeb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084eeb8 ["COPY", "tmp:0:8", ["const:983:8"]]
+ 0084eeb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084eeb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084eeb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084eeb8 bytes 29e12391
+ 0084eeb8 bytes 290d2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34eceb3cd5ebd60000a23955d5f5fd67"></a>

### [`0084f468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f468.md) → [`0084f468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f468.md) FUN_0084f468

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0084f474",
      "incomplete_value": false,
      "site": "0084f480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f474",
      "incomplete_value": false,
      "site": "0084f480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "0084f480",
      "DATA",
      [
        "storage",
        "00c024f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084f480",
      "DATA",
      [
        "storage",
        "00c02540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f468.md#insn-0084f474)
- 新版 `0084f474`（命令位置の公開資料なし）

~~~diff
- 0084f474 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 0084f474 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0084f474 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0084f474 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0084f474 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 0084f474 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0084f474 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0084f474 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0084f474 bytes 4ac11391
+ 0084f474 bytes 4a011591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c3e05063a6e6ba2e2b886dd4ffbbba8"></a>

### [`0084f4ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f4ac.md) → [`0084f4ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f4ac.md) FUN_0084f4ac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0084f4c4",
      "incomplete_value": false,
      "site": "0084f4d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f4c4",
      "incomplete_value": false,
      "site": "0084f4d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "0084f4d0",
      "DATA",
      [
        "storage",
        "00c024f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084f4d0",
      "DATA",
      [
        "storage",
        "00c02540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f4ac.md#insn-0084f4c4)
- 新版 `0084f4c4`（命令位置の公開資料なし）

~~~diff
- 0084f4c4 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 0084f4c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084f4c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084f4c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084f4c4 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 0084f4c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f4c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f4c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084f4c4 bytes 08c11391
+ 0084f4c4 bytes 08011591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a7786ff9e49aab6438fc91be622c207"></a>

### [`0084f508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f508.md) → [`0084f508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f508.md) FUN_0084f508

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0084f534",
      "incomplete_value": false,
      "site": "0084f534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f534",
      "incomplete_value": false,
      "site": "0084f534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "0084f534",
      "DATA",
      [
        "storage",
        "00c024f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084f534",
      "DATA",
      [
        "storage",
        "00c02540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f508.md#insn-0084f52c)
- 新版 `0084f52c`（命令位置の公開資料なし）

~~~diff
- 0084f52c ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 0084f52c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084f52c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084f52c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084f52c ["COPY", "tmp:0:8", ["const:540:8"]]
+ 0084f52c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f52c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f52c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084f52c bytes 08c11391
+ 0084f52c bytes 08011591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acde9d881f6e021bfacb695ca0e480d3"></a>

### [`0084f590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f590.md) → [`0084f590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f590.md) FUN_0084f590

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0084f5ac",
      "incomplete_value": false,
      "site": "0084f5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f5ac",
      "incomplete_value": false,
      "site": "0084f5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "0084f5ac",
      "DATA",
      [
        "storage",
        "00c024f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084f5ac",
      "DATA",
      [
        "storage",
        "00c02540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f590.md#insn-0084f5a8)
- 新版 `0084f5a8`（命令位置の公開資料なし）

~~~diff
- 0084f5a8 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 0084f5a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084f5a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084f5a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084f5a8 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 0084f5a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084f5a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084f5a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084f5a8 bytes 29c11391
+ 0084f5a8 bytes 29011591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba747af6e7fcb535a4fb2ab1a0799b8e"></a>

### [`0084f6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f6d0.md) → [`0084f6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f6d0.md) FUN_0084f6d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0084f6e4",
      "incomplete_value": false,
      "site": "0084f6e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f6e4",
      "incomplete_value": false,
      "site": "0084f6e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "0084f6e8",
      "DATA",
      [
        "storage",
        "00c02570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084f6e8",
      "DATA",
      [
        "storage",
        "00c025c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f6d0.md#insn-0084f6e4)
- 新版 `0084f6e4`（命令位置の公開資料なし）

~~~diff
- 0084f6e4 ["COPY", "tmp:0:8", ["const:570:8"]]
- 0084f6e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084f6e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084f6e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084f6e4 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 0084f6e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f6e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f6e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084f6e4 bytes 08c11591
+ 0084f6e4 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-151e107c7ed80d65b8629755e5dda1c6"></a>

### [`0084f6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f6f4.md) → [`0084f6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f6f4.md) FUN_0084f6f4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0084f6f8",
      "incomplete_value": false,
      "site": "0084f6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f6f8",
      "incomplete_value": false,
      "site": "0084f6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "0084f6fc",
      "DATA",
      [
        "storage",
        "00c02570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084f6fc",
      "DATA",
      [
        "storage",
        "00c025c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f6f4.md#insn-0084f6f8)
- 新版 `0084f6f8`（命令位置の公開資料なし）

~~~diff
- 0084f6f8 ["COPY", "tmp:0:8", ["const:570:8"]]
- 0084f6f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084f6f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084f6f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084f6f8 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 0084f6f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f6f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f6f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084f6f8 bytes 08c11591
+ 0084f6f8 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54010470143ab63c7eec1142a4130eb8"></a>

### [`0084f70c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f70c.md) → [`0084f70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f70c.md) FUN_0084f70c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00470050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470050.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00470050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470050.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084f744",
      "incomplete_value": true,
      "site": "0084f754",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c9c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f744",
      "incomplete_value": true,
      "site": "0084f754",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c11:8"
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
      "definition_site": "0084f744",
      "incomplete_value": true,
      "site": "0084f754",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0084f744",
      "incomplete_value": true,
      "site": "0084f754",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0084f758",
      "incomplete_value": true,
      "site": "0084f760",
      "value": [
        "LOAD",
        "16",
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
                "const:1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f758",
      "incomplete_value": true,
      "site": "0084f760",
      "value": [
        "LOAD",
        "16",
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
                "const:1f:8"
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
      "0084f744",
      "READ",
      [
        "storage",
        "002a5c11",
        null,
        "string"
      ]
    ],
    [
      "0084f744",
      "READ",
      [
        "storage",
        "002a5c21",
        null,
        "string"
      ]
    ],
    [
      "0084f758",
      "READ",
      [
        "storage",
        "002a5c30",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0084f744",
      "READ",
      [
        "storage",
        "002a5c9c",
        null,
        "string"
      ]
    ],
    [
      "0084f744",
      "READ",
      [
        "storage",
        "002a5cac",
        null,
        "string"
      ]
    ],
    [
      "0084f758",
      "READ",
      [
        "storage",
        "002a5cbb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f70c.md#insn-0084f73c) · [`0084f740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f70c.md#insn-0084f740)
- 新版 `0084f73c`（命令位置の公開資料なし） · `0084f740`（命令位置の公開資料なし）

~~~diff
- 0084f73c ["COPY", "tmp:0:8", ["const:c11:8"]]
- 0084f73c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084f73c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084f73c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084f73c ["COPY", "tmp:0:8", ["const:c9c:8"]]
+ 0084f73c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f73c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f73c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084f73c bytes 08453091
+ 0084f73c bytes 08713291
- 0084f740 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0084f740 bytes 09d3ffb0
+ 0084f740 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0084f740 bytes 09d3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5849c1e560424ccd39fcc70f4a69a6f"></a>

### [`0084f98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f98c.md) → [`0084f98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f98c.md) FUN_0084f98c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0084f9a0",
      "incomplete_value": false,
      "site": "0084f9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f9a0",
      "incomplete_value": false,
      "site": "0084f9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "0084f9a4",
      "DATA",
      [
        "storage",
        "00c025f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084f9a4",
      "DATA",
      [
        "storage",
        "00c02640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f98c.md#insn-0084f9a0)
- 新版 `0084f9a0`（命令位置の公開資料なし）

~~~diff
- 0084f9a0 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 0084f9a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084f9a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084f9a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084f9a0 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 0084f9a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f9a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f9a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084f9a0 bytes 08c11791
+ 0084f9a0 bytes 08011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2874b553e9155c020479b6dbe09e3886"></a>

### [`0084f9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f9b0.md) → [`0084f9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f9b0.md) FUN_0084f9b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0084f9b4",
      "incomplete_value": false,
      "site": "0084f9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f9b4",
      "incomplete_value": false,
      "site": "0084f9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "0084f9b8",
      "DATA",
      [
        "storage",
        "00c025f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084f9b8",
      "DATA",
      [
        "storage",
        "00c02640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f9b0.md#insn-0084f9b4)
- 新版 `0084f9b4`（命令位置の公開資料なし）

~~~diff
- 0084f9b4 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 0084f9b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084f9b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084f9b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084f9b4 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 0084f9b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f9b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f9b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084f9b4 bytes 08c11791
+ 0084f9b4 bytes 08011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04a05bfd1ab3b94bcbed0d3b351c9c97"></a>

### [`0084f9c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f9c8.md) → [`0084f9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f9c8.md) FUN_0084f9c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00470050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470050.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00470050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470050.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084fa00",
      "incomplete_value": true,
      "site": "0084fa10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:856:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084fa00",
      "incomplete_value": true,
      "site": "0084fa10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7bc:8"
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
      "definition_site": "0084fa00",
      "incomplete_value": true,
      "site": "0084fa10",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0084fa00",
      "incomplete_value": true,
      "site": "0084fa10",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0084fa14",
      "incomplete_value": true,
      "site": "0084fa1c",
      "value": [
        "LOAD",
        "16",
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
                "const:1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084fa14",
      "incomplete_value": true,
      "site": "0084fa1c",
      "value": [
        "LOAD",
        "16",
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
                "const:1f:8"
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
      "0084fa00",
      "READ",
      [
        "storage",
        "002a87bc",
        null,
        "string"
      ]
    ],
    [
      "0084fa00",
      "READ",
      [
        "storage",
        "002a87cc",
        null,
        "string"
      ]
    ],
    [
      "0084fa14",
      "READ",
      [
        "storage",
        "002a87db",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0084fa00",
      "READ",
      [
        "storage",
        "002a8856",
        null,
        "string"
      ]
    ],
    [
      "0084fa00",
      "READ",
      [
        "storage",
        "002a8866",
        null,
        "string"
      ]
    ],
    [
      "0084fa14",
      "READ",
      [
        "storage",
        "002a8875",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f9c8.md#insn-0084f9f8) · [`0084f9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f9c8.md#insn-0084f9fc)
- 新版 `0084f9f8`（命令位置の公開資料なし） · `0084f9fc`（命令位置の公開資料なし）

~~~diff
- 0084f9f8 ["COPY", "tmp:0:8", ["const:7bc:8"]]
- 0084f9f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084f9f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084f9f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084f9f8 ["COPY", "tmp:0:8", ["const:856:8"]]
+ 0084f9f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f9f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084f9f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084f9f8 bytes 08f11e91
+ 0084f9f8 bytes 08592191
- 0084f9fc ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0084f9fc bytes 09d3ffb0
+ 0084f9fc ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0084f9fc bytes 09d3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-261d2829a49f2a88a01f7a81b44face8"></a>

### [`0084fc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084fc44.md) → [`0084fc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fc44.md) FUN_0084fc44

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0084fc4c",
      "incomplete_value": false,
      "site": "0084fc50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084fc4c",
      "incomplete_value": false,
      "site": "0084fc50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "0084fc50",
      "DATA",
      [
        "storage",
        "00c02670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084fc50",
      "DATA",
      [
        "storage",
        "00c026c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084fc4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084fc44.md#insn-0084fc4c)
- 新版 `0084fc4c`（命令位置の公開資料なし）

~~~diff
- 0084fc4c ["COPY", "tmp:0:8", ["const:670:8"]]
- 0084fc4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084fc4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084fc4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084fc4c ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 0084fc4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084fc4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084fc4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084fc4c bytes 29c11991
+ 0084fc4c bytes 29011b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-948a2ad05e7854dcd9b770b9b3c4c281"></a>

### [`0084fc64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084fc64.md) → [`0084fc64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fc64.md) FUN_0084fc64

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0084fc6c",
      "incomplete_value": false,
      "site": "0084fc70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084fc6c",
      "incomplete_value": false,
      "site": "0084fc70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "0084fc70",
      "DATA",
      [
        "storage",
        "00c02670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084fc70",
      "DATA",
      [
        "storage",
        "00c026c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084fc6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084fc64.md#insn-0084fc6c)
- 新版 `0084fc6c`（命令位置の公開資料なし）

~~~diff
- 0084fc6c ["COPY", "tmp:0:8", ["const:670:8"]]
- 0084fc6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084fc6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084fc6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084fc6c ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 0084fc6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084fc6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084fc6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084fc6c bytes 29c11991
+ 0084fc6c bytes 29011b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3a1cf5f96906e14a6c0e55612e46bed"></a>

### [`0084fca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084fca4.md) → [`0084fca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fca4.md) FUN_0084fca4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0084fcd0",
      "incomplete_value": false,
      "site": "0084fcd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084fcd0",
      "incomplete_value": false,
      "site": "0084fcd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "0084fcd0",
      "DATA",
      [
        "storage",
        "00c02670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084fcd0",
      "DATA",
      [
        "storage",
        "00c026c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084fcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084fca4.md#insn-0084fcc8)
- 新版 `0084fcc8`（命令位置の公開資料なし）

~~~diff
- 0084fcc8 ["COPY", "tmp:0:8", ["const:670:8"]]
- 0084fcc8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0084fcc8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0084fcc8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0084fcc8 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 0084fcc8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0084fcc8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0084fcc8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0084fcc8 bytes 4ac11991
+ 0084fcc8 bytes 4a011b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d87628829e4aaf6cff6b7ed74edda30a"></a>

### [`0084fd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084fd18.md) → [`0084fd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fd18.md) FUN_0084fd18

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084fd20",
      "incomplete_value": true,
      "site": "0084fd20",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084fd20",
      "incomplete_value": true,
      "site": "0084fd20",
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
            "const:670:8"
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
      "0084fd20",
      "DATA",
      [
        "storage",
        "00c02670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084fd20",
      "DATA",
      [
        "storage",
        "00c026c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084fd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084fd18.md#insn-0084fd1c)
- 新版 `0084fd1c`（命令位置の公開資料なし）

~~~diff
- 0084fd1c ["COPY", "tmp:0:8", ["const:670:8"]]
- 0084fd1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084fd1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084fd1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084fd1c ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 0084fd1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084fd1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084fd1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084fd1c bytes 08c11991
+ 0084fd1c bytes 08011b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c9b318306ad4b95cdb209c851bd0d8d"></a>

### [`0084fe70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084fe70.md) → [`0084fe70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fe70.md) FUN_0084fe70

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0084fe84",
      "incomplete_value": false,
      "site": "0084fe88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084fe84",
      "incomplete_value": false,
      "site": "0084fe88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "0084fe88",
      "DATA",
      [
        "storage",
        "00c026f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084fe88",
      "DATA",
      [
        "storage",
        "00c02740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084fe84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084fe70.md#insn-0084fe84)
- 新版 `0084fe84`（命令位置の公開資料なし）

~~~diff
- 0084fe84 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 0084fe84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084fe84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084fe84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084fe84 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0084fe84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084fe84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084fe84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084fe84 bytes 08c11b91
+ 0084fe84 bytes 08011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54c312c5ce482890778578a9bf7ffeaa"></a>

### [`0084fe94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084fe94.md) → [`0084fe94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fe94.md) FUN_0084fe94

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0084fe98",
      "incomplete_value": true,
      "site": "0084fe9c",
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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084fe98",
      "incomplete_value": true,
      "site": "0084fe9c",
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
            "const:6f0:8"
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
      "0084fe9c",
      "DATA",
      [
        "storage",
        "00c026f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084fe9c",
      "DATA",
      [
        "storage",
        "00c02740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084fe98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084fe94.md#insn-0084fe98)
- 新版 `0084fe98`（命令位置の公開資料なし）

~~~diff
- 0084fe98 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 0084fe98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084fe98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084fe98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084fe98 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0084fe98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084fe98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084fe98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084fe98 bytes 08c11b91
+ 0084fe98 bytes 08011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4427d3f01307d38e28f9e6111cec574a"></a>

### [`00850128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850128.md) → [`00850128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850128.md) FUN_00850128

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00850148",
      "incomplete_value": false,
      "site": "0085014c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850148",
      "incomplete_value": false,
      "site": "0085014c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "0085014c",
      "DATA",
      [
        "storage",
        "00c02770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085014c",
      "DATA",
      [
        "storage",
        "00c027c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00850148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850128.md#insn-00850148)
- 新版 `00850148`（命令位置の公開資料なし）

~~~diff
- 00850148 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00850148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00850148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00850148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00850148 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 00850148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00850148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00850148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00850148 bytes 08c11d91
+ 00850148 bytes 08011f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-109b94f6b2aab3fd030a9d9e6f3debf3"></a>

### [`00850160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850160.md) → [`00850160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850160.md) FUN_00850160

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00850168",
      "incomplete_value": false,
      "site": "0085016c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850168",
      "incomplete_value": false,
      "site": "0085016c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "0085016c",
      "DATA",
      [
        "storage",
        "00c02770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085016c",
      "DATA",
      [
        "storage",
        "00c027c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00850168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850160.md#insn-00850168)
- 新版 `00850168`（命令位置の公開資料なし）

~~~diff
- 00850168 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00850168 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00850168 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00850168 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00850168 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 00850168 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00850168 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00850168 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00850168 bytes 29c11d91
+ 00850168 bytes 29011f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2204cc32a8709aaa23637f7493b25d88"></a>

### [`00850180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850180.md) → [`00850180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850180.md) FUN_00850180

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00470404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470404.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00470404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470404.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008501e0",
      "incomplete_value": true,
      "site": "008501e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:efe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008501e0",
      "incomplete_value": true,
      "site": "008501e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f8b:8"
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
      "definition_site": "008501e8",
      "incomplete_value": true,
      "site": "008501e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b64:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008501e8",
      "incomplete_value": true,
      "site": "008501e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ad9:8"
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
      "definition_site": "00850318",
      "incomplete_value": true,
      "site": "00850318",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:fd7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850318",
      "incomplete_value": true,
      "site": "00850318",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:64:8"
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
      "008501d4",
      "READ",
      [
        "storage",
        "00291f8b",
        null,
        "string"
      ]
    ],
    [
      "008501d8",
      "READ",
      [
        "storage",
        "0029fad9",
        null,
        "string"
      ]
    ],
    [
      "00850308",
      "READ",
      [
        "storage",
        "00297064",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008501d4",
      "READ",
      [
        "storage",
        "00291efe",
        null,
        "string"
      ]
    ],
    [
      "008501d8",
      "READ",
      [
        "storage",
        "0029fb64",
        null,
        "string"
      ]
    ],
    [
      "00850308",
      "READ",
      [
        "storage",
        "00296fd7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008501bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850180.md#insn-008501bc) · [`008501d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850180.md#insn-008501d0) · [`00850294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850180.md#insn-00850294)
- 新版 `008501bc`（命令位置の公開資料なし） · `008501d0`（命令位置の公開資料なし） · `00850294`（命令位置の公開資料なし）

~~~diff
- 008501bc ["COPY", "tmp:0:8", ["const:ad9:8"]]
- 008501bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008501bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008501bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008501bc ["COPY", "tmp:0:8", ["const:b64:8"]]
+ 008501bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008501bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008501bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008501bc bytes 29652b91
+ 008501bc bytes 29912d91
- 008501d0 ["COPY", "tmp:0:8", ["const:f8b:8"]]
- 008501d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008501d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008501d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008501d0 ["COPY", "tmp:0:8", ["const:efe:8"]]
+ 008501d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008501d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008501d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008501d0 bytes 082d3e91
+ 008501d0 bytes 08f93b91
- 00850294 ["COPY", "register:4010:8", ["const:4caf:8"]]
+ 00850294 ["COPY", "register:4010:8", ["const:4cb0:8"]]
- 00850294 bytes e2958952
+ 00850294 bytes 02968952
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed469ab8a9b9cb691a455074d0d98fce"></a>

### [`00850640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850640.md) → [`00850640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850640.md) FUN_00850640

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00850654",
      "incomplete_value": false,
      "site": "00850658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850654",
      "incomplete_value": false,
      "site": "00850658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "00850658",
      "DATA",
      [
        "storage",
        "00c027e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00850658",
      "DATA",
      [
        "storage",
        "00c02830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00850654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850640.md#insn-00850654)
- 新版 `00850654`（命令位置の公開資料なし）

~~~diff
- 00850654 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 00850654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00850654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00850654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00850654 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 00850654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00850654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00850654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00850654 bytes 08811f91
+ 00850654 bytes 08c12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa181694bc80cb9d9c084f1c81c147b3"></a>

### [`00850664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850664.md) → [`00850664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850664.md) FUN_00850664

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00850668",
      "incomplete_value": false,
      "site": "0085066c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850668",
      "incomplete_value": false,
      "site": "0085066c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "0085066c",
      "DATA",
      [
        "storage",
        "00c027e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085066c",
      "DATA",
      [
        "storage",
        "00c02830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00850668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850664.md#insn-00850668)
- 新版 `00850668`（命令位置の公開資料なし）

~~~diff
- 00850668 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 00850668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00850668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00850668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00850668 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 00850668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00850668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00850668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00850668 bytes 08811f91
+ 00850668 bytes 08c12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb4b3c2faddbecf8313e6063d81b371c"></a>

### [`0085067c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/0085067c.md) → [`0085067c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085067c.md) FUN_0085067c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ad88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046ad88.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ad88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046ad88.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008506c0",
      "incomplete_value": true,
      "site": "008506c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:f2f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008506c0",
      "incomplete_value": true,
      "site": "008506c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:f31:8"
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
      "008506ac",
      "READ",
      [
        "storage",
        "00299f31",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008506ac",
      "READ",
      [
        "storage",
        "00299f2f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008506a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/0085067c.md#insn-008506a4)
- 新版 `008506a4`（命令位置の公開資料なし）

~~~diff
- 008506a4 ["COPY", "tmp:0:8", ["const:f31:8"]]
- 008506a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008506a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008506a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008506a4 ["COPY", "tmp:0:8", ["const:f2f:8"]]
+ 008506a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008506a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008506a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008506a4 bytes 29c53c91
+ 008506a4 bytes 29bd3c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-351eda8a04b575e25f680c15e0f0cddc"></a>

### [`0085078c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/0085078c.md) → [`0085078c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085078c.md) FUN_0085078c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "008507a4",
      "incomplete_value": false,
      "site": "008507b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008507a4",
      "incomplete_value": false,
      "site": "008507b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "008507b0",
      "DATA",
      [
        "storage",
        "00c02870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008507b0",
      "DATA",
      [
        "storage",
        "00c028c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008507a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/0085078c.md#insn-008507a4)
- 新版 `008507a4`（命令位置の公開資料なし）

~~~diff
- 008507a4 ["COPY", "tmp:0:8", ["const:870:8"]]
- 008507a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008507a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008507a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008507a4 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 008507a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008507a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008507a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008507a4 bytes 08c12191
+ 008507a4 bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef1dc4401bffbac1796ecfb67722b571"></a>

### [`0085081c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/0085081c.md) → [`0085081c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085081c.md) FUN_0085081c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00850834",
      "incomplete_value": false,
      "site": "00850840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850834",
      "incomplete_value": false,
      "site": "00850840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00850840",
      "DATA",
      [
        "storage",
        "00c02870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00850840",
      "DATA",
      [
        "storage",
        "00c028c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00850834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/0085081c.md#insn-00850834)
- 新版 `00850834`（命令位置の公開資料なし）

~~~diff
- 00850834 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00850834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00850834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00850834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00850834 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00850834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00850834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00850834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00850834 bytes 08c12191
+ 00850834 bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39fd6003f788ecaf3489dea071ae039d"></a>

### [`008508a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/008508a8.md) → [`008508a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/008508a8.md) FUN_008508a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "008508d0",
      "incomplete_value": false,
      "site": "008508d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008508d0",
      "incomplete_value": false,
      "site": "008508d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "008508d4",
      "DATA",
      [
        "storage",
        "00c02870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008508d4",
      "DATA",
      [
        "storage",
        "00c028c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008508d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/008508a8.md#insn-008508d0)
- 新版 `008508d0`（命令位置の公開資料なし）

~~~diff
- 008508d0 ["COPY", "tmp:0:8", ["const:870:8"]]
- 008508d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008508d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008508d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008508d0 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 008508d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008508d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008508d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008508d0 bytes 29c12191
+ 008508d0 bytes 29012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-337d07b022862119fd20b9d05d2e2402"></a>

### [`00850958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850958.md) → [`00850958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850958.md) FUN_00850958

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "00850974",
      "incomplete_value": false,
      "site": "00850980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850974",
      "incomplete_value": false,
      "site": "00850980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00850980",
      "DATA",
      [
        "storage",
        "00c02870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00850980",
      "DATA",
      [
        "storage",
        "00c028c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00850974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850958.md#insn-00850974)
- 新版 `00850974`（命令位置の公開資料なし）

~~~diff
- 00850974 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00850974 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00850974 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00850974 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00850974 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00850974 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00850974 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00850974 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00850974 bytes 29c12191
+ 00850974 bytes 29012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3f9a8f52088173455da020c272db895"></a>

### [`00850afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850afc.md) → [`00850afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850afc.md) FUN_00850afc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0073e4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e4a4.md) [`0073e89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e89c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0084dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084dd1c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0073e4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e4a4.md) [`0073e89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e89c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0084dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.33% / 新版 98.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00850cf8",
      "incomplete_value": false,
      "site": "00850d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850cf8",
      "incomplete_value": false,
      "site": "00850d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "definition_site": "00850da4",
      "incomplete_value": false,
      "site": "00850dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850da4",
      "incomplete_value": false,
      "site": "00850dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "00850d00",
      "DATA",
      [
        "storage",
        "00c02970",
        null,
        "undefined *"
      ]
    ],
    [
      "00850dac",
      "DATA",
      [
        "storage",
        "00c028f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00850e4c",
      "READ",
      [
        "storage",
        "00c02918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00850d00",
      "DATA",
      [
        "storage",
        "00c029c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00850dac",
      "DATA",
      [
        "storage",
        "00c02940",
        null,
        "undefined *"
      ]
    ],
    [
      "00850e4c",
      "READ",
      [
        "storage",
        "00c02968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00850cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850afc.md#insn-00850cf8) · [`00850da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850afc.md#insn-00850da4)
- 新版 `00850cf8`（命令位置の公開資料なし） · `00850da4`（命令位置の公開資料なし）

~~~diff
- 00850cf8 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00850cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00850cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00850cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00850cf8 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00850cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00850cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00850cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00850cf8 bytes 08c12591
+ 00850cf8 bytes 08012791
- 00850da4 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00850da4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00850da4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00850da4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00850da4 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00850da4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00850da4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00850da4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00850da4 bytes 08c12391
+ 00850da4 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0707317d8be94d6612de6fa5f812842e"></a>

### [`008510d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008510d4.md) → [`008510d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008510d4.md) FUN_008510d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "008510ec",
      "incomplete_value": false,
      "site": "008510f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008510ec",
      "incomplete_value": false,
      "site": "008510f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "008510f8",
      "DATA",
      [
        "storage",
        "00c028f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008510f8",
      "DATA",
      [
        "storage",
        "00c02940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008510ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008510d4.md#insn-008510ec)
- 新版 `008510ec`（命令位置の公開資料なし）

~~~diff
- 008510ec ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 008510ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008510ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008510ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008510ec ["COPY", "tmp:0:8", ["const:940:8"]]
+ 008510ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008510ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008510ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008510ec bytes 08c12391
+ 008510ec bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5ce35b6d378dace8c401e235836a410"></a>

### [`00851164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851164.md) → [`00851164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851164.md) FUN_00851164

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0085117c",
      "incomplete_value": false,
      "site": "00851188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085117c",
      "incomplete_value": false,
      "site": "00851188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "00851188",
      "DATA",
      [
        "storage",
        "00c028f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00851188",
      "DATA",
      [
        "storage",
        "00c02940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085117c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851164.md#insn-0085117c)
- 新版 `0085117c`（命令位置の公開資料なし）

~~~diff
- 0085117c ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 0085117c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085117c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085117c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085117c ["COPY", "tmp:0:8", ["const:940:8"]]
+ 0085117c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085117c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085117c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085117c bytes 08c12391
+ 0085117c bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8129245d7d87051914c681a55087c3d4"></a>

### [`008511f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008511f0.md) → [`008511f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008511f0.md) FUN_008511f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00851218",
      "incomplete_value": false,
      "site": "0085121c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851218",
      "incomplete_value": false,
      "site": "0085121c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "0085121c",
      "DATA",
      [
        "storage",
        "00c028f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085121c",
      "DATA",
      [
        "storage",
        "00c02940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008511f0.md#insn-00851218)
- 新版 `00851218`（命令位置の公開資料なし）

~~~diff
- 00851218 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00851218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00851218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00851218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00851218 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00851218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00851218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00851218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00851218 bytes 29c12391
+ 00851218 bytes 29012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-432e2d9a98cbf94d7f332418d3f7a2da"></a>

### [`008512a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008512a0.md) → [`008512a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008512a0.md) FUN_008512a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "008512bc",
      "incomplete_value": false,
      "site": "008512c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008512bc",
      "incomplete_value": false,
      "site": "008512c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
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
      "008512c8",
      "DATA",
      [
        "storage",
        "00c028f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008512c8",
      "DATA",
      [
        "storage",
        "00c02940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008512bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008512a0.md#insn-008512bc)
- 新版 `008512bc`（命令位置の公開資料なし）

~~~diff
- 008512bc ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 008512bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008512bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008512bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008512bc ["COPY", "tmp:0:8", ["const:940:8"]]
+ 008512bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008512bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008512bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008512bc bytes 29c12391
+ 008512bc bytes 29012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2377887a6693e242e33f8dfc4b53386a"></a>

### [`00851510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851510.md) → [`00851510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851510.md) FUN_00851510

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00851528",
      "incomplete_value": false,
      "site": "00851534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851528",
      "incomplete_value": false,
      "site": "00851534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "00851534",
      "DATA",
      [
        "storage",
        "00c02970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00851534",
      "DATA",
      [
        "storage",
        "00c029c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851510.md#insn-00851528)
- 新版 `00851528`（命令位置の公開資料なし）

~~~diff
- 00851528 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00851528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00851528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00851528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00851528 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00851528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00851528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00851528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00851528 bytes 08c12591
+ 00851528 bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4588133ae7ec73b24eb7f2fd9814937c"></a>

### [`0085159c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/0085159c.md) → [`0085159c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/0085159c.md) FUN_0085159c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "008515c4",
      "incomplete_value": false,
      "site": "008515c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008515c4",
      "incomplete_value": false,
      "site": "008515c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "008515c8",
      "DATA",
      [
        "storage",
        "00c02970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008515c8",
      "DATA",
      [
        "storage",
        "00c029c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008515c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/0085159c.md#insn-008515c4)
- 新版 `008515c4`（命令位置の公開資料なし）

~~~diff
- 008515c4 ["COPY", "tmp:0:8", ["const:970:8"]]
- 008515c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008515c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008515c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008515c4 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 008515c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008515c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008515c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008515c4 bytes 29c12591
+ 008515c4 bytes 29012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e4472ccc55e5aac42903368e423ba90"></a>

### [`0085164c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/0085164c.md) → [`0085164c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/0085164c.md) FUN_0085164c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "00851668",
      "incomplete_value": false,
      "site": "00851674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851668",
      "incomplete_value": false,
      "site": "00851674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "00851674",
      "DATA",
      [
        "storage",
        "00c02970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00851674",
      "DATA",
      [
        "storage",
        "00c029c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/0085164c.md#insn-00851668)
- 新版 `00851668`（命令位置の公開資料なし）

~~~diff
- 00851668 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00851668 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00851668 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00851668 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00851668 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00851668 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00851668 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00851668 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00851668 bytes 29c12591
+ 00851668 bytes 29012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a91adfb5194fb4270e57a5759ca6b77"></a>

### [`0085182c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/0085182c.md) → [`0085182c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/0085182c.md) FUN_0085182c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00851844",
      "incomplete_value": false,
      "site": "00851850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851844",
      "incomplete_value": false,
      "site": "00851850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "00851850",
      "DATA",
      [
        "storage",
        "00c02a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00851850",
      "DATA",
      [
        "storage",
        "00c02a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/0085182c.md#insn-00851844)
- 新版 `00851844`（命令位置の公開資料なし）

~~~diff
- 00851844 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00851844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00851844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00851844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00851844 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00851844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00851844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00851844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00851844 bytes 08012891
+ 00851844 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e6c6c14ca567dc9a7b871044cd2e050"></a>

### [`008518bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008518bc.md) → [`008518bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008518bc.md) FUN_008518bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "008518d4",
      "incomplete_value": false,
      "site": "008518e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008518d4",
      "incomplete_value": false,
      "site": "008518e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "008518e0",
      "DATA",
      [
        "storage",
        "00c02a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008518e0",
      "DATA",
      [
        "storage",
        "00c02a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008518d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008518bc.md#insn-008518d4)
- 新版 `008518d4`（命令位置の公開資料なし）

~~~diff
- 008518d4 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 008518d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008518d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008518d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008518d4 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 008518d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008518d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008518d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008518d4 bytes 08012891
+ 008518d4 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0eac0ab68ae1d6ea9bbde25a161d613e"></a>

### [`00851948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851948.md) → [`00851948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851948.md) FUN_00851948

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00851970",
      "incomplete_value": false,
      "site": "00851974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851970",
      "incomplete_value": false,
      "site": "00851974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "00851974",
      "DATA",
      [
        "storage",
        "00c02a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00851974",
      "DATA",
      [
        "storage",
        "00c02a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851948.md#insn-00851970)
- 新版 `00851970`（命令位置の公開資料なし）

~~~diff
- 00851970 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00851970 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00851970 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00851970 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00851970 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00851970 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00851970 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00851970 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00851970 bytes 29012891
+ 00851970 bytes 29412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73114f58f6f3254474be7837a4932c53"></a>

### [`008519f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008519f8.md) → [`008519f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008519f8.md) FUN_008519f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "00851a14",
      "incomplete_value": false,
      "site": "00851a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851a14",
      "incomplete_value": false,
      "site": "00851a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "00851a20",
      "DATA",
      [
        "storage",
        "00c02a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00851a20",
      "DATA",
      [
        "storage",
        "00c02a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008519f8.md#insn-00851a14)
- 新版 `00851a14`（命令位置の公開資料なし）

~~~diff
- 00851a14 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00851a14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00851a14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00851a14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00851a14 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00851a14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00851a14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00851a14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00851a14 bytes 29012891
+ 00851a14 bytes 29412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fef4e8dc314cfac80eb06a31222807b"></a>

### [`00851b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851b9c.md) → [`00851b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851b9c.md) FUN_00851b9c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0073de68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073de68.md) [`0073e4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e4a4.md) [`0073e89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e89c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0073de68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073de68.md) [`0073e4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e4a4.md) [`0073e89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e89c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.04% / 新版 99.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00851db0",
      "incomplete_value": false,
      "site": "00851db8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851db0",
      "incomplete_value": false,
      "site": "00851db8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00851db8",
      "DATA",
      [
        "storage",
        "00c02a70",
        null,
        "undefined *"
      ]
    ],
    [
      "00851e58",
      "READ",
      [
        "storage",
        "00c02a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00851db8",
      "DATA",
      [
        "storage",
        "00c02ac0",
        null,
        "undefined *"
      ]
    ],
    [
      "00851e58",
      "READ",
      [
        "storage",
        "00c02ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851b9c.md#insn-00851db0)
- 新版 `00851db0`（命令位置の公開資料なし）

~~~diff
- 00851db0 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 00851db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00851db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00851db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00851db0 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 00851db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00851db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00851db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00851db0 bytes 08c12991
+ 00851db0 bytes 08012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dfd2d278462cfcd00a3c1869ed96c9e"></a>

### [`00852020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852020.md) → [`00852020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852020.md) FUN_00852020

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00852038",
      "incomplete_value": false,
      "site": "00852044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852038",
      "incomplete_value": false,
      "site": "00852044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "00852044",
      "DATA",
      [
        "storage",
        "00c02a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852044",
      "DATA",
      [
        "storage",
        "00c02ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852020.md#insn-00852038)
- 新版 `00852038`（命令位置の公開資料なし）

~~~diff
- 00852038 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 00852038 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00852038 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00852038 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00852038 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 00852038 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00852038 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00852038 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00852038 bytes 08c12991
+ 00852038 bytes 08012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61f65d11c991bd0f89458b8c79865e00"></a>

### [`008520b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008520b0.md) → [`008520b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008520b0.md) FUN_008520b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "008520c8",
      "incomplete_value": false,
      "site": "008520d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008520c8",
      "incomplete_value": false,
      "site": "008520d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008520d4",
      "DATA",
      [
        "storage",
        "00c02a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008520d4",
      "DATA",
      [
        "storage",
        "00c02ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008520c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008520b0.md#insn-008520c8)
- 新版 `008520c8`（命令位置の公開資料なし）

~~~diff
- 008520c8 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 008520c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008520c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008520c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008520c8 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 008520c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008520c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008520c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008520c8 bytes 08c12991
+ 008520c8 bytes 08012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14f3b9d74eeeedeef345f7b363328b89"></a>

### [`0085213c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/0085213c.md) → [`0085213c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085213c.md) FUN_0085213c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00852164",
      "incomplete_value": false,
      "site": "00852168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852164",
      "incomplete_value": false,
      "site": "00852168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00852168",
      "DATA",
      [
        "storage",
        "00c02a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852168",
      "DATA",
      [
        "storage",
        "00c02ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/0085213c.md#insn-00852164)
- 新版 `00852164`（命令位置の公開資料なし）

~~~diff
- 00852164 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 00852164 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00852164 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00852164 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00852164 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 00852164 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00852164 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00852164 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00852164 bytes 29c12991
+ 00852164 bytes 29012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4807573531cf5be007fdd25d8520c977"></a>

### [`008521ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008521ec.md) → [`008521ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008521ec.md) FUN_008521ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "00852208",
      "incomplete_value": false,
      "site": "00852214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852208",
      "incomplete_value": false,
      "site": "00852214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "00852214",
      "DATA",
      [
        "storage",
        "00c02a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852214",
      "DATA",
      [
        "storage",
        "00c02ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008521ec.md#insn-00852208)
- 新版 `00852208`（命令位置の公開資料なし）

~~~diff
- 00852208 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 00852208 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00852208 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00852208 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00852208 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 00852208 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00852208 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00852208 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00852208 bytes 29c12991
+ 00852208 bytes 29012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebde6a24cdcef523614fa511e0c630d1"></a>

### [`008523cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008523cc.md) → [`008523cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008523cc.md) FUN_008523cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "008523e8",
      "incomplete_value": false,
      "site": "008523f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008523e8",
      "incomplete_value": false,
      "site": "008523f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b00:8"
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
      "008523f0",
      "DATA",
      [
        "storage",
        "00c02b00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008523f0",
      "DATA",
      [
        "storage",
        "00c02b50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008523e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008523cc.md#insn-008523e8)
- 新版 `008523e8`（命令位置の公開資料なし）

~~~diff
- 008523e8 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 008523e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008523e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008523e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008523e8 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 008523e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008523e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008523e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008523e8 bytes 08012c91
+ 008523e8 bytes 08412d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69dfc88242c5dbf0ee27724891b9ad0c"></a>

### [`00852468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852468.md) → [`00852468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852468.md) FUN_00852468

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00852484",
      "incomplete_value": false,
      "site": "0085248c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852484",
      "incomplete_value": false,
      "site": "0085248c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b00:8"
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
      "0085248c",
      "DATA",
      [
        "storage",
        "00c02b00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085248c",
      "DATA",
      [
        "storage",
        "00c02b50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852468.md#insn-00852484)
- 新版 `00852484`（命令位置の公開資料なし）

~~~diff
- 00852484 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 00852484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00852484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00852484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00852484 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 00852484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00852484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00852484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00852484 bytes 08012c91
+ 00852484 bytes 08412d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-611ffbd73dcf7279846babd9603e897e"></a>

### [`008524fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008524fc.md) → [`008524fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008524fc.md) FUN_008524fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00852528",
      "incomplete_value": false,
      "site": "00852528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852528",
      "incomplete_value": false,
      "site": "00852528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b00:8"
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
      "00852528",
      "DATA",
      [
        "storage",
        "00c02b00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852528",
      "DATA",
      [
        "storage",
        "00c02b50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008524fc.md#insn-00852520)
- 新版 `00852520`（命令位置の公開資料なし）

~~~diff
- 00852520 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 00852520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00852520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00852520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00852520 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 00852520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00852520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00852520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00852520 bytes 08012c91
+ 00852520 bytes 08412d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-719bce7ec2e1046bc66e2408503f951e"></a>

### [`008525a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008525a4.md) → [`008525a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008525a4.md) FUN_008525a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "008525c4",
      "incomplete_value": false,
      "site": "008525c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008525c4",
      "incomplete_value": false,
      "site": "008525c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b00:8"
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
      "008525c4",
      "DATA",
      [
        "storage",
        "00c02b00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008525c4",
      "DATA",
      [
        "storage",
        "00c02b50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008525c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008525a4.md#insn-008525c0)
- 新版 `008525c0`（命令位置の公開資料なし）

~~~diff
- 008525c0 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 008525c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008525c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008525c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008525c0 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 008525c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008525c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008525c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008525c0 bytes 08012c91
+ 008525c0 bytes 08412d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d17fc78a7434647c3962e0efb9068b58"></a>

### [`0085274c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/0085274c.md) → [`0085274c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085274c.md) FUN_0085274c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0073e6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e6dc.md) [`0073eb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073eb44.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0084d6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d6d0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0073e6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e6dc.md) [`0073eb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073eb44.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0084d6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d6d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.86% / 新版 98.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008528e0",
      "incomplete_value": false,
      "site": "008528e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008528e0",
      "incomplete_value": false,
      "site": "008528e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "008528e8",
      "DATA",
      [
        "storage",
        "00c02b70",
        null,
        "undefined *"
      ]
    ],
    [
      "00852988",
      "READ",
      [
        "storage",
        "00c02b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008528e8",
      "DATA",
      [
        "storage",
        "00c02bc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00852988",
      "READ",
      [
        "storage",
        "00c02be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008528e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/0085274c.md#insn-008528e0)
- 新版 `008528e0`（命令位置の公開資料なし）

~~~diff
- 008528e0 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 008528e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008528e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008528e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008528e0 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 008528e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008528e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008528e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008528e0 bytes 08c12d91
+ 008528e0 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6a80583708966abcb0a7d0b39e3cc4a"></a>

### [`00852c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852c58.md) → [`00852c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852c58.md) FUN_00852c58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00852c80",
      "incomplete_value": false,
      "site": "00852c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852c80",
      "incomplete_value": false,
      "site": "00852c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "00852c84",
      "DATA",
      [
        "storage",
        "00c02b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852c84",
      "DATA",
      [
        "storage",
        "00c02bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852c58.md#insn-00852c80)
- 新版 `00852c80`（命令位置の公開資料なし）

~~~diff
- 00852c80 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 00852c80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00852c80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00852c80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00852c80 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00852c80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00852c80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00852c80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00852c80 bytes 29c12d91
+ 00852c80 bytes 29012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d321560f98b250963e4f6481841c937"></a>

### [`00852ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852ee8.md) → [`00852ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852ee8.md) FUN_00852ee8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00852f00",
      "incomplete_value": false,
      "site": "00852f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852f00",
      "incomplete_value": false,
      "site": "00852f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c00:8"
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
      "00852f0c",
      "DATA",
      [
        "storage",
        "00c02c00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852f0c",
      "DATA",
      [
        "storage",
        "00c02c50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852ee8.md#insn-00852f00)
- 新版 `00852f00`（命令位置の公開資料なし）

~~~diff
- 00852f00 ["COPY", "tmp:0:8", ["const:c00:8"]]
- 00852f00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00852f00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00852f00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00852f00 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00852f00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00852f00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00852f00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00852f00 bytes 08013091
+ 00852f00 bytes 08413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a7136d8eae2a107f527be729fc10a02"></a>

### [`00852f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852f58.md) → [`00852f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852f58.md) FUN_00852f58

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00852f70",
      "incomplete_value": false,
      "site": "00852f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852f70",
      "incomplete_value": false,
      "site": "00852f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c00:8"
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
      "00852f7c",
      "DATA",
      [
        "storage",
        "00c02c00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852f7c",
      "DATA",
      [
        "storage",
        "00c02c50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852f58.md#insn-00852f70)
- 新版 `00852f70`（命令位置の公開資料なし）

~~~diff
- 00852f70 ["COPY", "tmp:0:8", ["const:c00:8"]]
- 00852f70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00852f70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00852f70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00852f70 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00852f70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00852f70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00852f70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00852f70 bytes 08013091
+ 00852f70 bytes 08413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7946ecbf4c48cdf06612ee3bac9acc07"></a>

### [`0085309c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085309c.md) → [`0085309c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/0085309c.md) FUN_0085309c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008530b8",
      "incomplete_value": false,
      "site": "008530b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008530b8",
      "incomplete_value": false,
      "site": "008530b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c00:8"
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
      "008530b8",
      "DATA",
      [
        "storage",
        "00c02c00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008530b8",
      "DATA",
      [
        "storage",
        "00c02c50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008530b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085309c.md#insn-008530b0) · [`008530b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085309c.md#insn-008530b4)
- 新版 `008530b0`（命令位置の公開資料なし） · `008530b4`（命令位置の公開資料なし）

~~~diff
- 008530b0 ["COPY", "tmp:0:8", ["const:c00:8"]]
- 008530b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008530b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008530b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008530b0 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 008530b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008530b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008530b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008530b0 bytes 08013091
+ 008530b0 bytes 08413191
- 008530b4 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 008530b4 bytes f40301aa
+ 008530b4 ["COPY", "register:40a0:8", ["register:4008:8"]]
+ 008530b4 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38e28368a9af640aeebd57645c08ce29"></a>

### [`00853228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853228.md) → [`00853228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853228.md) FUN_00853228

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`00432904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432904.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`00432904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432904.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0073ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073ab94.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085330c",
      "incomplete_value": false,
      "site": "0085330c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085330c",
      "incomplete_value": false,
      "site": "0085330c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
      "0085330c",
      "DATA",
      [
        "storage",
        "00c02c70",
        null,
        "undefined *"
      ]
    ],
    [
      "00853388",
      "READ",
      [
        "storage",
        "00c02c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085330c",
      "DATA",
      [
        "storage",
        "00c02cc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00853388",
      "READ",
      [
        "storage",
        "00c02ce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853228.md#insn-00853304)
- 新版 `00853304`（命令位置の公開資料なし）

~~~diff
- 00853304 ["COPY", "tmp:0:8", ["const:c70:8"]]
- 00853304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00853304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00853304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00853304 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 00853304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00853304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00853304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00853304 bytes 08c13191
+ 00853304 bytes 08013391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e313f50281932ad3719aafafb81919b"></a>

### [`008534fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/008534fc.md) → [`008534fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/008534fc.md) FUN_008534fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00853508",
      "incomplete_value": false,
      "site": "00853514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853508",
      "incomplete_value": false,
      "site": "00853514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
      "00853514",
      "DATA",
      [
        "storage",
        "00c02c70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853514",
      "DATA",
      [
        "storage",
        "00c02cc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/008534fc.md#insn-00853508)
- 新版 `00853508`（命令位置の公開資料なし）

~~~diff
- 00853508 ["COPY", "tmp:0:8", ["const:c70:8"]]
- 00853508 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00853508 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00853508 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00853508 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 00853508 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00853508 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00853508 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00853508 bytes 4ac13191
+ 00853508 bytes 4a013391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98256bd49cba69fa61b1f0e161ae75df"></a>

### [`00853540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853540.md) → [`00853540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853540.md) FUN_00853540

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00853558",
      "incomplete_value": false,
      "site": "00853564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853558",
      "incomplete_value": false,
      "site": "00853564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
      "00853564",
      "DATA",
      [
        "storage",
        "00c02c70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853564",
      "DATA",
      [
        "storage",
        "00c02cc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853540.md#insn-00853558)
- 新版 `00853558`（命令位置の公開資料なし）

~~~diff
- 00853558 ["COPY", "tmp:0:8", ["const:c70:8"]]
- 00853558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00853558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00853558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00853558 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 00853558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00853558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00853558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00853558 bytes 08c13191
+ 00853558 bytes 08013391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4165bdae2d81c74f29613756502ceee1"></a>

### [`0085359c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085359c.md) → [`0085359c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/0085359c.md) FUN_0085359c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "008535c8",
      "incomplete_value": false,
      "site": "008535c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008535c8",
      "incomplete_value": false,
      "site": "008535c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
      "008535c8",
      "DATA",
      [
        "storage",
        "00c02c70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008535c8",
      "DATA",
      [
        "storage",
        "00c02cc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008535c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085359c.md#insn-008535c0)
- 新版 `008535c0`（命令位置の公開資料なし）

~~~diff
- 008535c0 ["COPY", "tmp:0:8", ["const:c70:8"]]
- 008535c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008535c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008535c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008535c0 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 008535c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008535c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008535c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008535c0 bytes 08c13191
+ 008535c0 bytes 08013391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfa1bd0ec9270ce57f811cf617468942"></a>

### [`00853624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853624.md) → [`00853624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853624.md) FUN_00853624

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00853640",
      "incomplete_value": false,
      "site": "00853640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853640",
      "incomplete_value": false,
      "site": "00853640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
      "00853640",
      "DATA",
      [
        "storage",
        "00c02c70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853640",
      "DATA",
      [
        "storage",
        "00c02cc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085363c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853624.md#insn-0085363c)
- 新版 `0085363c`（命令位置の公開資料なし）

~~~diff
- 0085363c ["COPY", "tmp:0:8", ["const:c70:8"]]
- 0085363c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085363c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085363c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085363c ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 0085363c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085363c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085363c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085363c bytes 29c13191
+ 0085363c bytes 29013391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f8b39021b269104a478e9736be5909d"></a>

### [`008538e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/008538e0.md) → [`008538e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/008538e0.md) FUN_008538e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "008538f4",
      "incomplete_value": false,
      "site": "008538f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008538f4",
      "incomplete_value": false,
      "site": "008538f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "008538f8",
      "DATA",
      [
        "storage",
        "00c02d10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008538f8",
      "DATA",
      [
        "storage",
        "00c02d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008538f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/008538e0.md#insn-008538f4)
- 新版 `008538f4`（命令位置の公開資料なし）

~~~diff
- 008538f4 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 008538f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008538f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008538f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008538f4 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 008538f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008538f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008538f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008538f4 bytes 08413491
+ 008538f4 bytes 08813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9957258c780ff40ca09f2ded6f449e5"></a>

### [`0085393c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085393c.md) → [`0085393c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/0085393c.md) FUN_0085393c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00853954",
      "incomplete_value": false,
      "site": "00853958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853954",
      "incomplete_value": false,
      "site": "00853958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "00853958",
      "DATA",
      [
        "storage",
        "00c02d10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853958",
      "DATA",
      [
        "storage",
        "00c02d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085393c.md#insn-00853954)
- 新版 `00853954`（命令位置の公開資料なし）

~~~diff
- 00853954 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 00853954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00853954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00853954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00853954 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00853954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00853954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00853954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00853954 bytes 08413491
+ 00853954 bytes 08813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f17793b6f7257b8ad3099e4bf49bf0f"></a>

### [`00853998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853998.md) → [`00853998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853998.md) FUN_00853998

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "008539bc",
      "incomplete_value": false,
      "site": "008539c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008539bc",
      "incomplete_value": false,
      "site": "008539c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "008539c0",
      "DATA",
      [
        "storage",
        "00c02d10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008539c0",
      "DATA",
      [
        "storage",
        "00c02d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008539bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853998.md#insn-008539bc)
- 新版 `008539bc`（命令位置の公開資料なし）

~~~diff
- 008539bc ["COPY", "tmp:0:8", ["const:d10:8"]]
- 008539bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008539bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008539bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008539bc ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 008539bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008539bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008539bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008539bc bytes 29413491
+ 008539bc bytes 29813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4da605170ddf0426f6012c536c2e87e3"></a>

### [`008539f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/008539f0.md) → [`008539f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/008539f0.md) FUN_008539f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "008539f8",
      "incomplete_value": false,
      "site": "008539fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008539f8",
      "incomplete_value": false,
      "site": "008539fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "008539fc",
      "DATA",
      [
        "storage",
        "00c02d10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008539fc",
      "DATA",
      [
        "storage",
        "00c02d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008539f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/008539f0.md#insn-008539f8)
- 新版 `008539f8`（命令位置の公開資料なし）

~~~diff
- 008539f8 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 008539f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008539f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008539f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008539f8 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 008539f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008539f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008539f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008539f8 bytes 29413491
+ 008539f8 bytes 29813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65c4bb29593a5457cff40d15732f0cff"></a>

### [`00853acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853acc.md) → [`00853acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853acc.md) FUN_00853acc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`00433930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/00433930.md) [`004418c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004418c4.md) [`00853f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853f38.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`00433930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/00433930.md) [`004418c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004418c4.md) [`00853f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853f38.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00853c5c",
      "incomplete_value": false,
      "site": "00853c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853c5c",
      "incomplete_value": false,
      "site": "00853c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
      "00853c5c",
      "DATA",
      [
        "storage",
        "00c02d80",
        null,
        "undefined *"
      ]
    ],
    [
      "00853cb0",
      "READ",
      [
        "storage",
        "00c02da8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853c5c",
      "DATA",
      [
        "storage",
        "00c02dd0",
        null,
        "undefined *"
      ]
    ],
    [
      "00853cb0",
      "READ",
      [
        "storage",
        "00c02df8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853acc.md#insn-00853c50)
- 新版 `00853c50`（命令位置の公開資料なし）

~~~diff
- 00853c50 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 00853c50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00853c50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00853c50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00853c50 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00853c50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00853c50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00853c50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00853c50 bytes 08013691
+ 00853c50 bytes 08413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07af194d610aaaca7940ef5470b4af9f"></a>

### [`00853e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853e08.md) → [`00853e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853e08.md) FUN_00853e08

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00853e10",
      "incomplete_value": false,
      "site": "00853e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853e10",
      "incomplete_value": false,
      "site": "00853e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
      "00853e14",
      "DATA",
      [
        "storage",
        "00c02d80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853e14",
      "DATA",
      [
        "storage",
        "00c02dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853e08.md#insn-00853e10)
- 新版 `00853e10`（命令位置の公開資料なし）

~~~diff
- 00853e10 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 00853e10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00853e10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00853e10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00853e10 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00853e10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00853e10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00853e10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00853e10 bytes 29013691
+ 00853e10 bytes 29413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fae4f72d5bd5515d5324e199393e763c"></a>

### [`00853e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853e28.md) → [`00853e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853e28.md) FUN_00853e28

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00853e30",
      "incomplete_value": true,
      "site": "00853e34",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853e30",
      "incomplete_value": true,
      "site": "00853e34",
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
            "const:d80:8"
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
      "00853e34",
      "DATA",
      [
        "storage",
        "00c02d80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853e34",
      "DATA",
      [
        "storage",
        "00c02dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853e28.md#insn-00853e30)
- 新版 `00853e30`（命令位置の公開資料なし）

~~~diff
- 00853e30 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 00853e30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00853e30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00853e30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00853e30 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00853e30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00853e30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00853e30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00853e30 bytes 29013691
+ 00853e30 bytes 29413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e191b194e44f1943e042b8ebe8a7f5b7"></a>

### [`00853e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853e68.md) → [`00853e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853e68.md) FUN_00853e68

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00853e98",
      "incomplete_value": false,
      "site": "00853e98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853e98",
      "incomplete_value": false,
      "site": "00853e98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
      "00853e98",
      "DATA",
      [
        "storage",
        "00c02d80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853e98",
      "DATA",
      [
        "storage",
        "00c02dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853e68.md#insn-00853e8c)
- 新版 `00853e8c`（命令位置の公開資料なし）

~~~diff
- 00853e8c ["COPY", "tmp:0:8", ["const:d80:8"]]
- 00853e8c ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00853e8c ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00853e8c ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00853e8c ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00853e8c ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00853e8c ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00853e8c ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00853e8c bytes 6b013691
+ 00853e8c bytes 6b413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb99c710ee84a2745261f260676d5bf0"></a>

### [`00853ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853ee4.md) → [`00853ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853ee4.md) FUN_00853ee4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

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
      "definition_site": "00853ef0",
      "incomplete_value": false,
      "site": "00853ef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853ef0",
      "incomplete_value": false,
      "site": "00853ef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
      "00853ef0",
      "DATA",
      [
        "storage",
        "00c02d80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853ef0",
      "DATA",
      [
        "storage",
        "00c02dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853ee4.md#insn-00853eec)
- 新版 `00853eec`（命令位置の公開資料なし）

~~~diff
- 00853eec ["COPY", "tmp:0:8", ["const:d80:8"]]
- 00853eec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00853eec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00853eec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00853eec ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00853eec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00853eec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00853eec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00853eec bytes 29013691
+ 00853eec bytes 29413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37cffa2d264fa77fd11e822f391220d3"></a>

### [`00854110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854110.md) → [`00854110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854110.md) _INIT_159

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085414c",
      "incomplete_value": true,
      "site": "00854168",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085414c",
      "incomplete_value": true,
      "site": "00854168",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:2dd:8"
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
      "definition_site": "00854170",
      "incomplete_value": true,
      "site": "0085418c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00854170",
      "incomplete_value": true,
      "site": "0085418c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f0:8"
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
      "definition_site": "008541b0",
      "incomplete_value": true,
      "site": "008541c8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:293000:8"
              ],
              [
                "leaf",
                "const:6ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008541b0",
      "incomplete_value": true,
      "site": "008541c8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:293000:8"
              ],
              [
                "leaf",
                "const:73b:8"
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
      "0085414c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00854170",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00854190",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0085414c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00854170",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00854190",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085413c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854110.md#insn-0085413c) · [`00854144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854110.md#insn-00854144)
- 新版 `0085413c`（命令位置の公開資料なし） · `00854144`（命令位置の公開資料なし）

~~~diff
- 0085413c ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 0085413c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0085413c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0085413c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0085413c ["COPY", "tmp:0:8", ["const:610:8"]]
+ 0085413c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0085413c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0085413c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0085413c bytes 73421791
+ 0085413c bytes 73421891
- 00854144 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00854144 bytes 89d2fff0
+ 00854144 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00854144 bytes 89d2fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39c5f44ca013428c4faed39d1e7eb5bb"></a>

### [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) → [`008544a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008544a0.md) FUN_008544a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 10件 [`008577f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008577f8.md) [`00857d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857d90.md) [`00857eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857eb4.md) [`00857fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857fd8.md) [`008580fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580fc.md) · 呼出先 12件 [`00855e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e58.md) [`00855e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e5c.md) [`00855ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855ea4.md) [`00856058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856058.md) [`0085605c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/0085605c.md)
- 新版 呼出元 10件 [`008577f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/008577f8.md) [`00857d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857d90.md) [`00857eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857eb4.md) [`00857fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00857/00857fd8.md) [`008580fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/008580fc.md) · 呼出先 12件 [`00855e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855e58.md) [`00855e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855e5c.md) [`00855ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855ea4.md) [`00856058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856058.md) [`0085605c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/0085605c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008544d4",
      "incomplete_value": false,
      "site": "008544d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008544d4",
      "incomplete_value": false,
      "site": "008544d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e10:8"
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
      "008544d8",
      "DATA",
      [
        "storage",
        "00c02e10",
        null,
        "pointer"
      ]
    ],
    [
      "00854510",
      "DATA",
      [
        "storage",
        "00c02fc8",
        null,
        "undefined *"
      ]
    ],
    [
      "00854544",
      "READ",
      [
        "storage",
        "00c02fe8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008544d8",
      "DATA",
      [
        "storage",
        "00c02e60",
        null,
        "pointer"
      ]
    ],
    [
      "00854510",
      "DATA",
      [
        "storage",
        "00c03018",
        null,
        "undefined *"
      ]
    ],
    [
      "00854544",
      "READ",
      [
        "storage",
        "00c03038",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008544d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md#insn-008544d4) · [`008544dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md#insn-008544dc) · [`008544e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md#insn-008544e0)
- 新版 `008544d4`（命令位置の公開資料なし） · `008544dc`（命令位置の公開資料なし） · `008544e0`（命令位置の公開資料なし）

~~~diff
- 008544d4 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 008544d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008544d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008544d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008544d4 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 008544d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008544d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008544d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008544d4 bytes 08413891
+ 008544d4 bytes 08813991
- 008544dc ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 008544dc ["COPY", "register:4040:8", ["const:c03000:8"]]
- 008544dc bytes 681d00d0
+ 008544dc bytes 681d00f0
- 008544e0 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 008544e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008544e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008544e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008544e0 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 008544e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008544e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008544e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008544e0 bytes 08213f91
+ 008544e0 bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc2be21141ea54617e1ea730f794f136"></a>

### [`008546a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008546a8.md) → [`008546a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/008546a8.md) FUN_008546a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a26b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26b24.md) [`00a26cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26cbc.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a26b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26b68.md) [`00a26d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26d00.md)

変更の種類 call, call_target, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

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
      "site": "008546c4",
      "value": [
        "leaf",
        "ram:a26d00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008546c4",
      "value": [
        "leaf",
        "ram:a26cbc:8"
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
      "008546c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a26cbc"
      ]
    ]
  ],
  "added": [
    [
      "008546c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a26d00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008546c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008546a8.md#insn-008546c4)
- 新版 `008546c4`（命令位置の公開資料なし）

~~~diff
- 008546c4 ["INT_ADD", "register:40f0:8", ["const:8546c4:8", "const:4:8"]]
- 008546c4 ["CALL", null, ["ram:a26cbc:8"]]
+ 008546c4 ["INT_ADD", "register:40f0:8", ["const:8546c4:8", "const:4:8"]]
+ 008546c4 ["CALL", null, ["ram:a26d00:8"]]
- 008546c4 bytes 7e490794
+ 008546c4 bytes 8f490794
~~~


<a id="compare-ed7d777ba531dbd34eb5096b914f6e18"></a>

### [`00854718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854718.md) → [`00854718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854718.md) FUN_00854718

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0081f58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f58c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) · 呼出先 0件 

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
      "definition_site": "0085472c",
      "incomplete_value": false,
      "site": "00854730",
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
            "const:bd3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085472c",
      "incomplete_value": false,
      "site": "00854730",
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
            "const:bc4:8"
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
      "00854730",
      "DATA",
      [
        "storage",
        "002a9bc4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00854730",
      "DATA",
      [
        "storage",
        "002a9bd3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085472c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854718.md#insn-0085472c)
- 新版 `0085472c`（命令位置の公開資料なし）

~~~diff
- 0085472c ["COPY", "tmp:0:8", ["const:bc4:8"]]
- 0085472c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085472c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085472c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085472c ["COPY", "tmp:0:8", ["const:bd3:8"]]
+ 0085472c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085472c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085472c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085472c bytes 08112f91
+ 0085472c bytes 084d2f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8e226543a61499f20acb93826f0751b"></a>

### [`00854808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854808.md) → [`00854808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854808.md) FUN_00854808

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00a3cca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cca4.md) · 呼出先 4件 [`00856bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bc4.md) [`00856bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bc8.md) [`00ad7598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7598.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00a3cce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cce8.md) · 呼出先 4件 [`00856bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856bc4.md) [`00856bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00856/00856bc8.md) [`00ad75dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad75dc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "0085483c",
      "incomplete_value": false,
      "site": "0085483c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085483c",
      "incomplete_value": false,
      "site": "0085483c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "0085483c",
      "DATA",
      [
        "storage",
        "00c031e8",
        null,
        "undefined *"
      ]
    ],
    [
      "0085487c",
      "READ",
      [
        "storage",
        "00c03208",
        null,
        "pointer"
      ]
    ],
    [
      "0085487c",
      "READ",
      [
        "storage",
        "00c03210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085483c",
      "DATA",
      [
        "storage",
        "00c03238",
        null,
        "undefined *"
      ]
    ],
    [
      "0085487c",
      "READ",
      [
        "storage",
        "00c03258",
        null,
        "pointer"
      ]
    ],
    [
      "0085487c",
      "READ",
      [
        "storage",
        "00c03260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00854834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854808.md#insn-00854834)
- 新版 `00854834`（命令位置の公開資料なし）

~~~diff
- 00854834 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00854834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00854834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00854834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00854834 ["COPY", "tmp:0:8", ["const:238:8"]]
+ 00854834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00854834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00854834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00854834 bytes 08a10791
+ 00854834 bytes 08e10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fed3cb2e6af92dc8447bc923d4a5759b"></a>

### [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) → [`00854900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854900.md) FUN_00854900

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e02b0.md) [`0068d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md) [`007127f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00712/007127f8.md) [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 24件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`00574bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bb4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0084bae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084b/0084bae8.md) [`00855054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855054.md)
- 新版 呼出元 7件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) [`0068d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d484.md) [`007127f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00712/007127f8.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 24件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`00574bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bb4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0084bae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bae8.md) [`00855054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855054.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.76% / 新版 99.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00854a50",
      "incomplete_value": true,
      "site": "00854a58",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:880:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00854a50",
      "incomplete_value": true,
      "site": "00854a58",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
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
      "00854a50",
      "READ",
      [
        "storage",
        "00c1b830",
        null,
        "pointer"
      ]
    ],
    [
      "00854a50",
      "PARAM",
      [
        "storage",
        "0109e430",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00854a50",
      "READ",
      [
        "storage",
        "00c1b880",
        null,
        "pointer"
      ]
    ],
    [
      "00854a50",
      "PARAM",
      [
        "storage",
        "0109e470",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00854a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md#insn-00854a50)
- 新版 `00854a50`（命令位置の公開資料なし）

~~~diff
- 00854a50 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:830:8"]]
- 00854a50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00854a50 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:880:8"]]
+ 00854a50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00854a50 bytes 211844f9
+ 00854a50 bytes 214044f9
~~~


<a id="compare-3688a932ade347421bcfc590973e0ca6"></a>

### [`00855450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855450.md) → [`00855450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855450.md) FUN_00855450

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`005f0e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0e9c.md) [`0060081c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/0060081c.md) [`006d5524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d5524.md) [`007172c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/007172c8.md) [`007ca13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca13c.md) · 呼出先 11件 [`0056c55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c55c.md) [`00858960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858960.md) [`00858964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858964.md) [`00858a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858a70.md) [`00858a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858a74.md)
- 新版 呼出元 6件 [`005f0e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0e9c.md) [`0060081c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00600/0060081c.md) [`006d5524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5524.md) [`007172c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/007172c8.md) [`007ca13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca13c.md) · 呼出先 11件 [`0056c55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c55c.md) [`00858960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858960.md) [`00858964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858964.md) [`00858a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858a70.md) [`00858a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00858/00858a74.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.43% / 新版 95.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008555b0",
      "incomplete_value": false,
      "site": "008555b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008555b0",
      "incomplete_value": false,
      "site": "008555b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "definition_site": "008555d4",
      "incomplete_value": false,
      "site": "008555d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008555d4",
      "incomplete_value": false,
      "site": "008555d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "definition_site": "008555ec",
      "incomplete_value": false,
      "site": "008555ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008555ec",
      "incomplete_value": false,
      "site": "008555ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "008555b0",
      "DATA",
      [
        "storage",
        "00c03618",
        null,
        "undefined *"
      ]
    ],
    [
      "008555d4",
      "DATA",
      [
        "storage",
        "00c03698",
        null,
        "undefined *"
      ]
    ],
    [
      "008555ec",
      "DATA",
      [
        "storage",
        "00c03718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008555b0",
      "DATA",
      [
        "storage",
        "00c03668",
        null,
        "undefined *"
      ]
    ],
    [
      "008555d4",
      "DATA",
      [
        "storage",
        "00c036e8",
        null,
        "undefined *"
      ]
    ],
    [
      "008555ec",
      "DATA",
      [
        "storage",
        "00c03768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008555ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855450.md#insn-008555ac) · [`008555d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855450.md#insn-008555d0) · [`008555e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855450.md#insn-008555e8)
- 新版 `008555ac`（命令位置の公開資料なし） · `008555d0`（命令位置の公開資料なし） · `008555e8`（命令位置の公開資料なし）

~~~diff
- 008555ac ["COPY", "tmp:0:8", ["const:618:8"]]
- 008555ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008555ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008555ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008555ac ["COPY", "tmp:0:8", ["const:668:8"]]
+ 008555ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008555ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008555ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008555ac bytes 29611891
+ 008555ac bytes 29a11991
- 008555d0 ["COPY", "tmp:0:8", ["const:698:8"]]
- 008555d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008555d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008555d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008555d0 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 008555d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008555d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008555d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008555d0 bytes 4a611a91
+ 008555d0 bytes 4aa11b91
- 008555e8 ["COPY", "tmp:0:8", ["const:718:8"]]
- 008555e8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008555e8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008555e8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008555e8 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 008555e8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008555e8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008555e8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008555e8 bytes 4a611c91
+ 008555e8 bytes 4aa11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25c453135e61e29ffc82914a51d32ef6"></a>

### [`0085587c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/0085587c.md) → [`0085587c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/0085587c.md) FUN_0085587c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ca3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca3b0.md) · 呼出先 4件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)
- 新版 呼出元 1件 [`007ca3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007ca3b0.md) · 呼出先 4件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0085595c",
      "incomplete_value": false,
      "site": "0085596c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085595c",
      "incomplete_value": false,
      "site": "0085596c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00855964",
      "incomplete_value": false,
      "site": "0085596c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00855964",
      "incomplete_value": false,
      "site": "0085596c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
      "0085595c",
      "PARAM",
      [
        "storage",
        "00c02f00",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00855964",
      "PARAM",
      [
        "storage",
        "00c02f10",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0085595c",
      "PARAM",
      [
        "storage",
        "00c02f50",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00855964",
      "PARAM",
      [
        "storage",
        "00c02f60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085595c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/0085587c.md#insn-0085595c) · [`00855964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/0085587c.md#insn-00855964)
- 新版 `0085595c`（命令位置の公開資料なし） · `00855964`（命令位置の公開資料なし）

~~~diff
- 0085595c ["COPY", "tmp:0:8", ["const:f00:8"]]
- 0085595c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0085595c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0085595c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0085595c ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 0085595c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0085595c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0085595c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0085595c bytes 21003c91
+ 0085595c bytes 21403d91
- 00855964 ["COPY", "tmp:0:8", ["const:f10:8"]]
- 00855964 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00855964 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00855964 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00855964 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00855964 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00855964 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00855964 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00855964 bytes 42403c91
+ 00855964 bytes 42803d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ffdd6572d5cf3e6f39efbd0e311619c"></a>

### [`008559d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/008559d8.md) → [`008559d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/008559d8.md) FUN_008559d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006d584c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d584c.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 5件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)
- 新版 呼出元 2件 [`006d584c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d584c.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 5件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.55% / 新版 97.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00855ca4",
      "incomplete_value": false,
      "site": "00855cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00855ca4",
      "incomplete_value": false,
      "site": "00855cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
      "definition_site": "00855d28",
      "incomplete_value": false,
      "site": "00855d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00855d28",
      "incomplete_value": false,
      "site": "00855d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "definition_site": "00855d30",
      "incomplete_value": false,
      "site": "00855d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00855d30",
      "incomplete_value": false,
      "site": "00855d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
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
      "00855c44",
      "PARAM",
      [
        "storage",
        "00c02f00",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00855c4c",
      "PARAM",
      [
        "storage",
        "00c02f88",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00855c9c",
      "PARAM",
      [
        "storage",
        "00c02f00",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00855c44",
      "PARAM",
      [
        "storage",
        "00c02f50",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00855c4c",
      "PARAM",
      [
        "storage",
        "00c02fd8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00855c9c",
      "PARAM",
      [
        "storage",
        "00c02f50",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00855c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/008559d8.md#insn-00855c44) · [`00855c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/008559d8.md#insn-00855c4c) · [`00855c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/008559d8.md#insn-00855c9c)
- 新版 `00855c44`（命令位置の公開資料なし） · `00855c4c`（命令位置の公開資料なし） · `00855c9c`（命令位置の公開資料なし）

~~~diff
- 00855c44 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 00855c44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00855c44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00855c44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00855c44 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 00855c44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00855c44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00855c44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00855c44 bytes 21003c91
+ 00855c44 bytes 21403d91
- 00855c4c ["COPY", "tmp:0:8", ["const:f88:8"]]
- 00855c4c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00855c4c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00855c4c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00855c4c ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 00855c4c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00855c4c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00855c4c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00855c4c bytes 42203e91
+ 00855c4c bytes 42603f91
- 00855c9c ["COPY", "tmp:0:8", ["const:f00:8"]]
- 00855c9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00855c9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00855c9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00855c9c ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 00855c9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00855c9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00855c9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00855c9c bytes 21003c91
+ 00855c9c bytes 21403d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd43b65be67e0add367854afb883fad0"></a>

### [`00855e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e10.md) → [`00855e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00855/00855e10.md) FUN_00855e10

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00855e34",
      "incomplete_value": true,
      "site": "00855e34",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00855e34",
      "incomplete_value": true,
      "site": "00855e34",
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
            "const:fc8:8"
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
      "00855e34",
      "DATA",
      [
        "storage",
        "00c02fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00855e34",
      "DATA",
      [
        "storage",
        "00c03018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00855e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e10.md#insn-00855e2c) · [`00855e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e10.md#insn-00855e30)
- 新版 `00855e2c`（命令位置の公開資料なし） · `00855e30`（命令位置の公開資料なし）

~~~diff
- 00855e2c ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 00855e2c ["COPY", "register:4040:8", ["const:c03000:8"]]
- 00855e2c bytes 681d00b0
+ 00855e2c bytes 681d00d0
- 00855e30 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 00855e30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00855e30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00855e30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00855e30 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00855e30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00855e30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00855e30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00855e30 bytes 08213f91
+ 00855e30 bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

