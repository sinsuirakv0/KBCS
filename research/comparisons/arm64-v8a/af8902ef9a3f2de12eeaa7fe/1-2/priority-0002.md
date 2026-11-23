# v15.7.4 → v16.0.0 · 最優先の変更候補 (2)

[一覧の目次](README.md)

<a id="compare-a22a51d17b73dcef92426d8d3e6967e0"></a>

### [`00428d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428d08.md) → [`0044b858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b858.md) FUN_0044b858

採用 · 移動量 `+0x22b50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 2件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b874",
      "incomplete_value": false,
      "site": "0044b88c",
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
            "const:df3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428d24",
      "incomplete_value": false,
      "site": "00428d3c",
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
            "const:3c5:8"
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
      "definition_site": "0044b880",
      "incomplete_value": false,
      "site": "0044b88c",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428d30",
      "incomplete_value": false,
      "site": "00428d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "definition_site": "0044b894",
      "incomplete_value": false,
      "site": "0044b89c",
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
            "const:529:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428d44",
      "incomplete_value": false,
      "site": "00428d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:8d0:8"
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
      "0044b874",
      "PARAM",
      [
        "storage",
        "002a53c5",
        null,
        "string"
      ]
    ],
    [
      "0044b880",
      "PARAM",
      [
        "storage",
        "00c24ba8",
        null,
        "undefined2"
      ]
    ],
    [
      "0044b894",
      "PARAM",
      [
        "storage",
        "002978d0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b874",
      "PARAM",
      [
        "storage",
        "002b5df3",
        null,
        "string"
      ]
    ],
    [
      "0044b880",
      "PARAM",
      [
        "storage",
        "00ca4668",
        null,
        "undefined2"
      ]
    ],
    [
      "0044b894",
      "PARAM",
      [
        "storage",
        "002a7529",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428d08.md#insn-00428d3c) · [`00428d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428d08.md#insn-00428d4c) · [`00428d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428d08.md#insn-00428d20)
- 新版 [`0044b88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b858.md#insn-0044b88c) · [`0044b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b858.md#insn-0044b89c) · [`0044b870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b858.md#insn-0044b870)

~~~diff
- 00428d3c ["INT_ADD", "register:40f0:8", ["const:428d3c:8", "const:4:8"]]
- 00428d3c ["CALL", null, ["callee:00c57cb0:8"]]
+ 0044b88c ["INT_ADD", "register:40f0:8", ["const:44b88c:8", "const:4:8"]]
+ 0044b88c ["CALL", null, ["callee:00c57cb0:8"]]
- 00428d3c bytes 49c91e94
+ 0044b88c bytes 09312094
- 00428d4c ["INT_ADD", "register:40f0:8", ["const:428d4c:8", "const:4:8"]]
- 00428d4c ["CALL", null, ["callee:00c57b70:8"]]
+ 0044b89c ["INT_ADD", "register:40f0:8", ["const:44b89c:8", "const:4:8"]]
+ 0044b89c ["CALL", null, ["callee:00c57b70:8"]]
- 00428d4c bytes f5c81e94
+ 0044b89c bytes b5302094
- 00428d20 ["COPY", "register:4000:8", ["const:2a5000:8"]]
+ 0044b870 ["COPY", "register:4000:8", ["const:2b5000:8"]]
- 00428d20 bytes e0f3ffb0
+ 0044b870 bytes 40f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8c6fe42710359d562311a73a400954f"></a>

### [`00428dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428dc8.md) → [`0044b918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b918.md) FUN_0044b918

採用 · 移動量 `+0x22b50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00435c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435c18.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00458ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b934",
      "incomplete_value": false,
      "site": "0044b94c",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428de4",
      "incomplete_value": false,
      "site": "00428dfc",
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
            "const:803:8"
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
      "definition_site": "0044b940",
      "incomplete_value": false,
      "site": "0044b94c",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428df0",
      "incomplete_value": false,
      "site": "00428dfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "definition_site": "0044b954",
      "incomplete_value": false,
      "site": "0044b95c",
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
            "const:90f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428e04",
      "incomplete_value": false,
      "site": "00428e0c",
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
            "const:368:8"
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
      "0044b934",
      "PARAM",
      [
        "storage",
        "00296803",
        null,
        "string"
      ]
    ],
    [
      "0044b940",
      "PARAM",
      [
        "storage",
        "00c24ba8",
        null,
        "undefined2"
      ]
    ],
    [
      "0044b954",
      "PARAM",
      [
        "storage",
        "002a0368",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b934",
      "PARAM",
      [
        "storage",
        "002a6338",
        null,
        "string"
      ]
    ],
    [
      "0044b940",
      "PARAM",
      [
        "storage",
        "00ca4668",
        null,
        "undefined2"
      ]
    ],
    [
      "0044b954",
      "PARAM",
      [
        "storage",
        "002b090f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428dc8.md#insn-00428dfc) · [`00428e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428dc8.md#insn-00428e0c) · [`00428de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428dc8.md#insn-00428de0)
- 新版 [`0044b94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b918.md#insn-0044b94c) · [`0044b95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b918.md#insn-0044b95c) · [`0044b930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b918.md#insn-0044b930)

~~~diff
- 00428dfc ["INT_ADD", "register:40f0:8", ["const:428dfc:8", "const:4:8"]]
- 00428dfc ["CALL", null, ["callee:00c57cb0:8"]]
+ 0044b94c ["INT_ADD", "register:40f0:8", ["const:44b94c:8", "const:4:8"]]
+ 0044b94c ["CALL", null, ["callee:00c57cb0:8"]]
- 00428dfc bytes 19c91e94
+ 0044b94c bytes d9302094
- 00428e0c ["INT_ADD", "register:40f0:8", ["const:428e0c:8", "const:4:8"]]
- 00428e0c ["CALL", null, ["callee:00c57b70:8"]]
+ 0044b95c ["INT_ADD", "register:40f0:8", ["const:44b95c:8", "const:4:8"]]
+ 0044b95c ["CALL", null, ["callee:00c57b70:8"]]
- 00428e0c bytes c5c81e94
+ 0044b95c bytes 85302094
- 00428de0 ["COPY", "register:4000:8", ["const:296000:8"]]
+ 0044b930 ["COPY", "register:4000:8", ["const:2a6000:8"]]
- 00428de0 bytes 60f3ffd0
+ 0044b930 bytes c0f2fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe69d100c0e696eadb59effd3afa83da"></a>

### [`00428e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428e88.md) → [`0044b9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b9d8.md) FUN_0044b9d8

採用 · 移動量 `+0x22b50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00949c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00949/00949c4c.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`0097f6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f6f8.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b9f4",
      "incomplete_value": false,
      "site": "0044ba0c",
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
            "const:91d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428ea4",
      "incomplete_value": false,
      "site": "00428ebc",
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
            "const:376:8"
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
      "definition_site": "0044ba00",
      "incomplete_value": false,
      "site": "0044ba0c",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428eb0",
      "incomplete_value": false,
      "site": "00428ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "definition_site": "0044ba14",
      "incomplete_value": false,
      "site": "0044ba1c",
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
            "const:27e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428ec4",
      "incomplete_value": false,
      "site": "00428ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:845:8"
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
      "0044b9f4",
      "PARAM",
      [
        "storage",
        "002a0376",
        null,
        "string"
      ]
    ],
    [
      "0044ba00",
      "PARAM",
      [
        "storage",
        "00c24ba8",
        null,
        "undefined2"
      ]
    ],
    [
      "0044ba14",
      "PARAM",
      [
        "storage",
        "00295845",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b9f4",
      "PARAM",
      [
        "storage",
        "002b091d",
        null,
        "string"
      ]
    ],
    [
      "0044ba00",
      "PARAM",
      [
        "storage",
        "00ca4668",
        null,
        "undefined2"
      ]
    ],
    [
      "0044ba14",
      "PARAM",
      [
        "storage",
        "002a527e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428e88.md#insn-00428ebc) · [`00428ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428e88.md#insn-00428ecc) · [`00428ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428e88.md#insn-00428ea0)
- 新版 [`0044ba0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b9d8.md#insn-0044ba0c) · [`0044ba1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b9d8.md#insn-0044ba1c) · [`0044b9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b9d8.md#insn-0044b9f0)

~~~diff
- 00428ebc ["INT_ADD", "register:40f0:8", ["const:428ebc:8", "const:4:8"]]
- 00428ebc ["CALL", null, ["callee:00c57cb0:8"]]
+ 0044ba0c ["INT_ADD", "register:40f0:8", ["const:44ba0c:8", "const:4:8"]]
+ 0044ba0c ["CALL", null, ["callee:00c57cb0:8"]]
- 00428ebc bytes e9c81e94
+ 0044ba0c bytes a9302094
- 00428ecc ["INT_ADD", "register:40f0:8", ["const:428ecc:8", "const:4:8"]]
- 00428ecc ["CALL", null, ["callee:00c57b70:8"]]
+ 0044ba1c ["INT_ADD", "register:40f0:8", ["const:44ba1c:8", "const:4:8"]]
+ 0044ba1c ["CALL", null, ["callee:00c57b70:8"]]
- 00428ecc bytes 95c81e94
+ 0044ba1c bytes 55302094
- 00428ea0 ["COPY", "register:4000:8", ["const:2a0000:8"]]
+ 0044b9f0 ["COPY", "register:4000:8", ["const:2b0000:8"]]
- 00428ea0 bytes c0f3ff90
+ 0044b9f0 bytes 20f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e5e1f3c869103d1cf014adada0e985b"></a>

### [`00428f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428f48.md) → [`0044ba98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044ba98.md) FUN_0044ba98

採用 · 移動量 `+0x22b50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006833dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00683/006833dc.md) [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 3件 [`006a9724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a9/006a9724.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bac0",
      "incomplete_value": true,
      "site": "0044bad0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428f70",
      "incomplete_value": true,
      "site": "00428f80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044bad4",
      "incomplete_value": true,
      "site": "0044bad4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00428f84",
      "incomplete_value": true,
      "site": "00428f84",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044bae0",
      "incomplete_value": false,
      "site": "0044bae8",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428f90",
      "incomplete_value": false,
      "site": "00428f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044bac0",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044bac8",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044bae0",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044bac0",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044bac8",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044bae0",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428f48.md#insn-00428f98) · [`00428fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428f48.md#insn-00428fd0) · [`00428f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428f48.md#insn-00428f60)
- 新版 [`0044bae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044ba98.md#insn-0044bae8) · [`0044bb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044ba98.md#insn-0044bb20) · [`0044bab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044ba98.md#insn-0044bab0)

~~~diff
- 00428f98 ["INT_ADD", "register:40f0:8", ["const:428f98:8", "const:4:8"]]
- 00428f98 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044bae8 ["INT_ADD", "register:40f0:8", ["const:44bae8:8", "const:4:8"]]
+ 0044bae8 ["CALL", null, ["callee:00c57b70:8"]]
- 00428f98 bytes 62c81e94
+ 0044bae8 bytes 22302094
- 00428fd0 ["INT_ADD", "register:40f0:8", ["const:428fd0:8", "const:4:8"]]
- 00428fd0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044bb20 ["INT_ADD", "register:40f0:8", ["const:44bb20:8", "const:4:8"]]
+ 0044bb20 ["CALL", null, ["callee:00c57b70:8"]]
- 00428fd0 bytes 54c81e94
+ 0044bb20 bytes 14302094
- 00428f60 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044bab0 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 00428f60 bytes 29f4ffd0
+ 0044bab0 bytes a9f3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19b3a990185bbb48a6ebb5b9ac9dc614"></a>

### [`00429060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429060.md) → [`0044bbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bbb0.md) FUN_0044bbb0

採用 · 移動量 `+0x22b50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0068d810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d810.md) [`008c2a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2a7c.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 2件 [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) [`008f694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f694c.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bbd8",
      "incomplete_value": true,
      "site": "0044bbe8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429088",
      "incomplete_value": true,
      "site": "00429098",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044bbec",
      "incomplete_value": true,
      "site": "0044bbec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042909c",
      "incomplete_value": true,
      "site": "0042909c",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044bbf8",
      "incomplete_value": false,
      "site": "0044bc00",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004290a8",
      "incomplete_value": false,
      "site": "004290b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044bbd8",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044bbe0",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044bbf8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044bbd8",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044bbe0",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044bbf8",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004290b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429060.md#insn-004290b0) · [`004290e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429060.md#insn-004290e8) · [`00429078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429060.md#insn-00429078)
- 新版 [`0044bc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bbb0.md#insn-0044bc00) · [`0044bc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bbb0.md#insn-0044bc38) · [`0044bbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bbb0.md#insn-0044bbc8)

~~~diff
- 004290b0 ["INT_ADD", "register:40f0:8", ["const:4290b0:8", "const:4:8"]]
- 004290b0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044bc00 ["INT_ADD", "register:40f0:8", ["const:44bc00:8", "const:4:8"]]
+ 0044bc00 ["CALL", null, ["callee:00c57b70:8"]]
- 004290b0 bytes 1cc81e94
+ 0044bc00 bytes dc2f2094
- 004290e8 ["INT_ADD", "register:40f0:8", ["const:4290e8:8", "const:4:8"]]
- 004290e8 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044bc38 ["INT_ADD", "register:40f0:8", ["const:44bc38:8", "const:4:8"]]
+ 0044bc38 ["CALL", null, ["callee:00c57b70:8"]]
- 004290e8 bytes 0ec81e94
+ 0044bc38 bytes ce2f2094
- 00429078 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044bbc8 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 00429078 bytes 29f4ffb0
+ 0044bbc8 bytes a9f3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c076302648f49fbd39eedd6ae89f3252"></a>

### [`00429178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429178.md) → [`0044bcc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bcc8.md) FUN_0044bcc8

採用 · 移動量 `+0x22b50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bcf4",
      "incomplete_value": true,
      "site": "0044bd08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004291a4",
      "incomplete_value": true,
      "site": "004291b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044bd0c",
      "incomplete_value": true,
      "site": "0044bd0c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004291bc",
      "incomplete_value": true,
      "site": "004291bc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044bd18",
      "incomplete_value": false,
      "site": "0044bd20",
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
            "const:daa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004291c8",
      "incomplete_value": false,
      "site": "004291d0",
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
            "const:37c:8"
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
      "0044bcf4",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044bd00",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044bd18",
      "PARAM",
      [
        "storage",
        "002a537c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044bcf4",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044bd00",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044bd18",
      "PARAM",
      [
        "storage",
        "002b5daa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004291d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429178.md#insn-004291d0) · [`00429208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429178.md#insn-00429208) · [`00429268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429178.md#insn-00429268)
- 新版 [`0044bd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bcc8.md#insn-0044bd20) · [`0044bd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bcc8.md#insn-0044bd58) · [`0044bdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bcc8.md#insn-0044bdb8)

~~~diff
- 004291d0 ["INT_ADD", "register:40f0:8", ["const:4291d0:8", "const:4:8"]]
- 004291d0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044bd20 ["INT_ADD", "register:40f0:8", ["const:44bd20:8", "const:4:8"]]
+ 0044bd20 ["CALL", null, ["callee:00c57b70:8"]]
- 004291d0 bytes d4c71e94
+ 0044bd20 bytes 942f2094
- 00429208 ["INT_ADD", "register:40f0:8", ["const:429208:8", "const:4:8"]]
- 00429208 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044bd58 ["INT_ADD", "register:40f0:8", ["const:44bd58:8", "const:4:8"]]
+ 0044bd58 ["CALL", null, ["callee:00c57b70:8"]]
- 00429208 bytes c6c71e94
+ 0044bd58 bytes 862f2094
- 00429268 ["INT_ADD", "register:40f0:8", ["const:429268:8", "const:4:8"]]
- 00429268 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044bdb8 ["INT_ADD", "register:40f0:8", ["const:44bdb8:8", "const:4:8"]]
+ 0044bdb8 ["CALL", null, ["callee:00c57b70:8"]]
- 00429268 bytes aec71e94
+ 0044bdb8 bytes 6e2f2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61e3f710f7c019314dd7fde0e8a13ee8"></a>

### [`00429384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429384.md) → [`0044bed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bed4.md) FUN_0044bed4

採用 · 移動量 `+0x22b50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00758dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758dd0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00783234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783234.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044befc",
      "incomplete_value": true,
      "site": "0044bf0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004293ac",
      "incomplete_value": true,
      "site": "004293bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044bf10",
      "incomplete_value": true,
      "site": "0044bf10",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004293c0",
      "incomplete_value": true,
      "site": "004293c0",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044bf1c",
      "incomplete_value": false,
      "site": "0044bf24",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004293cc",
      "incomplete_value": false,
      "site": "004293d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044befc",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044bf04",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044bf1c",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044befc",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044bf04",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044bf1c",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004293d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429384.md#insn-004293d4) · [`0042940c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429384.md#insn-0042940c) · [`0042939c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429384.md#insn-0042939c)
- 新版 [`0044bf24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bed4.md#insn-0044bf24) · [`0044bf5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bed4.md#insn-0044bf5c) · [`0044beec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bed4.md#insn-0044beec)

~~~diff
- 004293d4 ["INT_ADD", "register:40f0:8", ["const:4293d4:8", "const:4:8"]]
- 004293d4 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044bf24 ["INT_ADD", "register:40f0:8", ["const:44bf24:8", "const:4:8"]]
+ 0044bf24 ["CALL", null, ["callee:00c57b70:8"]]
- 004293d4 bytes 53c71e94
+ 0044bf24 bytes 132f2094
- 0042940c ["INT_ADD", "register:40f0:8", ["const:42940c:8", "const:4:8"]]
- 0042940c ["CALL", null, ["callee:00c57b70:8"]]
+ 0044bf5c ["INT_ADD", "register:40f0:8", ["const:44bf5c:8", "const:4:8"]]
+ 0044bf5c ["CALL", null, ["callee:00c57b70:8"]]
- 0042940c bytes 45c71e94
+ 0044bf5c bytes 052f2094
- 0042939c ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044beec ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042939c bytes 29f4ffb0
+ 0044beec bytes a9f3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b37bb643621838e131f6f642d1b9a670"></a>

### [`0042949c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/0042949c.md) → [`0044bfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bfec.md) FUN_0044bfec

採用 · 移動量 `+0x22b50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00758dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758dd0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00783234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783234.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c014",
      "incomplete_value": true,
      "site": "0044c024",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004294c4",
      "incomplete_value": true,
      "site": "004294d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044c028",
      "incomplete_value": true,
      "site": "0044c028",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004294d8",
      "incomplete_value": true,
      "site": "004294d8",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c034",
      "incomplete_value": false,
      "site": "0044c03c",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004294e4",
      "incomplete_value": false,
      "site": "004294ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044c014",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044c01c",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044c034",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c014",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c01c",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c034",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004294ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/0042949c.md#insn-004294ec) · [`00429524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/0042949c.md#insn-00429524) · [`004294b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/0042949c.md#insn-004294b4)
- 新版 [`0044c03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bfec.md#insn-0044c03c) · [`0044c074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bfec.md#insn-0044c074) · [`0044c004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bfec.md#insn-0044c004)

~~~diff
- 004294ec ["INT_ADD", "register:40f0:8", ["const:4294ec:8", "const:4:8"]]
- 004294ec ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c03c ["INT_ADD", "register:40f0:8", ["const:44c03c:8", "const:4:8"]]
+ 0044c03c ["CALL", null, ["callee:00c57b70:8"]]
- 004294ec bytes 0dc71e94
+ 0044c03c bytes cd2e2094
- 00429524 ["INT_ADD", "register:40f0:8", ["const:429524:8", "const:4:8"]]
- 00429524 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c074 ["INT_ADD", "register:40f0:8", ["const:44c074:8", "const:4:8"]]
+ 0044c074 ["CALL", null, ["callee:00c57b70:8"]]
- 00429524 bytes ffc61e94
+ 0044c074 bytes bf2e2094
- 004294b4 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044c004 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 004294b4 bytes 29f4ffb0
+ 0044c004 bytes 89f3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2da75d8ac53eb5ec7fc804d5cffe18a"></a>

### [`004295b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004295b4.md) → [`0044c104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c104.md) FUN_0044c104

採用 · 移動量 `+0x22b50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c12c",
      "incomplete_value": true,
      "site": "0044c13c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004295dc",
      "incomplete_value": true,
      "site": "004295ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044c140",
      "incomplete_value": true,
      "site": "0044c140",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004295f0",
      "incomplete_value": true,
      "site": "004295f0",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c14c",
      "incomplete_value": false,
      "site": "0044c154",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004295fc",
      "incomplete_value": false,
      "site": "00429604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044c12c",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044c134",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044c14c",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c12c",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c134",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c14c",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00429604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004295b4.md#insn-00429604) · [`0042963c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004295b4.md#insn-0042963c) · [`004295cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004295b4.md#insn-004295cc)
- 新版 [`0044c154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c104.md#insn-0044c154) · [`0044c18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c104.md#insn-0044c18c) · [`0044c11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c104.md#insn-0044c11c)

~~~diff
- 00429604 ["INT_ADD", "register:40f0:8", ["const:429604:8", "const:4:8"]]
- 00429604 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c154 ["INT_ADD", "register:40f0:8", ["const:44c154:8", "const:4:8"]]
+ 0044c154 ["CALL", null, ["callee:00c57b70:8"]]
- 00429604 bytes c7c61e94
+ 0044c154 bytes 872e2094
- 0042963c ["INT_ADD", "register:40f0:8", ["const:42963c:8", "const:4:8"]]
- 0042963c ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c18c ["INT_ADD", "register:40f0:8", ["const:44c18c:8", "const:4:8"]]
+ 0044c18c ["CALL", null, ["callee:00c57b70:8"]]
- 0042963c bytes b9c61e94
+ 0044c18c bytes 792e2094
- 004295cc ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044c11c ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 004295cc bytes 29f4ffb0
+ 0044c11c bytes 89f3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a14b41789bff2fadd1efb97e9fe80d58"></a>

### [`004296cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004296cc.md) → [`0044c21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c21c.md) FUN_0044c21c

採用 · 移動量 `+0x22b50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007f9cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f9cd4.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 2件 [`0082f0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082f0e8.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c244",
      "incomplete_value": true,
      "site": "0044c254",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004296f4",
      "incomplete_value": true,
      "site": "00429704",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044c258",
      "incomplete_value": true,
      "site": "0044c258",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00429708",
      "incomplete_value": true,
      "site": "00429708",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c264",
      "incomplete_value": false,
      "site": "0044c26c",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429714",
      "incomplete_value": false,
      "site": "0042971c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044c244",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044c24c",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044c264",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c244",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c24c",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c264",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042971c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004296cc.md#insn-0042971c) · [`00429754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004296cc.md#insn-00429754) · [`004296e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004296cc.md#insn-004296e4)
- 新版 [`0044c26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c21c.md#insn-0044c26c) · [`0044c2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c21c.md#insn-0044c2a4) · [`0044c234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c21c.md#insn-0044c234)

~~~diff
- 0042971c ["INT_ADD", "register:40f0:8", ["const:42971c:8", "const:4:8"]]
- 0042971c ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c26c ["INT_ADD", "register:40f0:8", ["const:44c26c:8", "const:4:8"]]
+ 0044c26c ["CALL", null, ["callee:00c57b70:8"]]
- 0042971c bytes 81c61e94
+ 0044c26c bytes 412e2094
- 00429754 ["INT_ADD", "register:40f0:8", ["const:429754:8", "const:4:8"]]
- 00429754 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c2a4 ["INT_ADD", "register:40f0:8", ["const:44c2a4:8", "const:4:8"]]
+ 0044c2a4 ["CALL", null, ["callee:00c57b70:8"]]
- 00429754 bytes 73c61e94
+ 0044c2a4 bytes 332e2094
- 004296e4 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044c234 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 004296e4 bytes 29f4ffb0
+ 0044c234 bytes 89f3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1002e54f68264ed3eadd046b45bcda3e"></a>

### [`004297e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004297e4.md) → [`0044c564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c564.md) FUN_0044c564

採用 · 移動量 `+0x22d80` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007e0354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e0/007e0354.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 2件 [`00814bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00814/00814bb8.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c58c",
      "incomplete_value": true,
      "site": "0044c59c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042980c",
      "incomplete_value": true,
      "site": "0042981c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044c5a0",
      "incomplete_value": true,
      "site": "0044c5a0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00429820",
      "incomplete_value": true,
      "site": "00429820",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c5ac",
      "incomplete_value": false,
      "site": "0044c5b4",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042982c",
      "incomplete_value": false,
      "site": "00429834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044c58c",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044c594",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044c5ac",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c58c",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c594",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c5ac",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00429834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004297e4.md#insn-00429834) · [`0042986c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004297e4.md#insn-0042986c) · [`004297fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004297e4.md#insn-004297fc)
- 新版 [`0044c5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c564.md#insn-0044c5b4) · [`0044c5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c564.md#insn-0044c5ec) · [`0044c57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c564.md#insn-0044c57c)

~~~diff
- 00429834 ["INT_ADD", "register:40f0:8", ["const:429834:8", "const:4:8"]]
- 00429834 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c5b4 ["INT_ADD", "register:40f0:8", ["const:44c5b4:8", "const:4:8"]]
+ 0044c5b4 ["CALL", null, ["callee:00c57b70:8"]]
- 00429834 bytes 3bc61e94
+ 0044c5b4 bytes 6f2d2094
- 0042986c ["INT_ADD", "register:40f0:8", ["const:42986c:8", "const:4:8"]]
- 0042986c ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c5ec ["INT_ADD", "register:40f0:8", ["const:44c5ec:8", "const:4:8"]]
+ 0044c5ec ["CALL", null, ["callee:00c57b70:8"]]
- 0042986c bytes 2dc61e94
+ 0044c5ec bytes 612d2094
- 004297fc ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044c57c ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 004297fc bytes 29f4ffb0
+ 0044c57c bytes 89f3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e64923721c52464132e4376cbf5c7eff"></a>

### [`004298fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004298fc.md) → [`0044c67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c67c.md) FUN_0044c67c

採用 · 移動量 `+0x22d80` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c6a4",
      "incomplete_value": true,
      "site": "0044c6b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429924",
      "incomplete_value": true,
      "site": "00429934",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044c6b8",
      "incomplete_value": true,
      "site": "0044c6b8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00429938",
      "incomplete_value": true,
      "site": "00429938",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c6c4",
      "incomplete_value": false,
      "site": "0044c6cc",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429944",
      "incomplete_value": false,
      "site": "0042994c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044c6a4",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044c6ac",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044c6c4",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c6a4",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c6ac",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c6c4",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042994c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004298fc.md#insn-0042994c) · [`00429984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004298fc.md#insn-00429984) · [`00429914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/004298fc.md#insn-00429914)
- 新版 [`0044c6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c67c.md#insn-0044c6cc) · [`0044c704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c67c.md#insn-0044c704) · [`0044c694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c67c.md#insn-0044c694)

~~~diff
- 0042994c ["INT_ADD", "register:40f0:8", ["const:42994c:8", "const:4:8"]]
- 0042994c ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c6cc ["INT_ADD", "register:40f0:8", ["const:44c6cc:8", "const:4:8"]]
+ 0044c6cc ["CALL", null, ["callee:00c57b70:8"]]
- 0042994c bytes f5c51e94
+ 0044c6cc bytes 292d2094
- 00429984 ["INT_ADD", "register:40f0:8", ["const:429984:8", "const:4:8"]]
- 00429984 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c704 ["INT_ADD", "register:40f0:8", ["const:44c704:8", "const:4:8"]]
+ 0044c704 ["CALL", null, ["callee:00c57b70:8"]]
- 00429984 bytes e7c51e94
+ 0044c704 bytes 1b2d2094
- 00429914 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044c694 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 00429914 bytes 29f4ffb0
+ 0044c694 bytes 89f3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af771550d706f6cdfc1cd4c9ebb6910c"></a>

### [`00429a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429a14.md) → [`0044c794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c794.md) FUN_0044c794

採用 · 移動量 `+0x22d80` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008594d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/008594d4.md) · 呼出先 4件 [`00428714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428714.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`0088c46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c46c.md) · 呼出先 4件 [`0044b214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b214.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c7c0",
      "incomplete_value": false,
      "site": "0044c7c8",
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
            "const:f3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429a40",
      "incomplete_value": false,
      "site": "00429a48",
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
            "const:3cf:8"
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
      "0044c7c0",
      "PARAM",
      [
        "storage",
        "002a73cf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c7c0",
      "PARAM",
      [
        "storage",
        "002b7f3e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00429a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429a14.md#insn-00429a48) · [`00429a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429a14.md#insn-00429a38) · [`00429a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429a14.md#insn-00429a3c)
- 新版 [`0044c7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c794.md#insn-0044c7c8) · [`0044c7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c794.md#insn-0044c7b8) · [`0044c7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c794.md#insn-0044c7bc)

~~~diff
- 00429a48 ["INT_ADD", "register:40f0:8", ["const:429a48:8", "const:4:8"]]
- 00429a48 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c7c8 ["INT_ADD", "register:40f0:8", ["const:44c7c8:8", "const:4:8"]]
+ 0044c7c8 ["CALL", null, ["callee:00c57b70:8"]]
- 00429a48 bytes b6c51e94
+ 0044c7c8 bytes ea2c2094
- 00429a38 ["INT_ADD", "register:40f0:8", ["const:429a38:8", "const:4:8"]]
- 00429a38 ["CALL", null, ["callee:0044b214:8"]]
+ 0044c7b8 ["INT_ADD", "register:40f0:8", ["const:44c7b8:8", "const:4:8"]]
+ 0044c7b8 ["CALL", null, ["callee:0044b214:8"]]
- 00429a38 bytes 37fbff97
+ 0044c7b8 bytes 97faff97
- 00429a3c ["COPY", "register:4008:8", ["const:2a7000:8"]]
+ 0044c7bc ["COPY", "register:4008:8", ["const:2b7000:8"]]
- 00429a3c bytes e1f3ffd0
+ 0044c7bc bytes 41f3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bce66b330412c50a63a90e825db6f1f0"></a>

### [`00429ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429ac4.md) → [`0044c844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c844.md) FUN_0044c844

採用 · 移動量 `+0x22d80` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00897400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00897/00897400.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`008cb298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb298.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c86c",
      "incomplete_value": true,
      "site": "0044c87c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429aec",
      "incomplete_value": true,
      "site": "00429afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044c880",
      "incomplete_value": true,
      "site": "0044c880",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00429b00",
      "incomplete_value": true,
      "site": "00429b00",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c88c",
      "incomplete_value": false,
      "site": "0044c894",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429b0c",
      "incomplete_value": false,
      "site": "00429b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044c86c",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044c874",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044c88c",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c86c",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c874",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c88c",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00429b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429ac4.md#insn-00429b14) · [`00429b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429ac4.md#insn-00429b4c) · [`00429adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429ac4.md#insn-00429adc)
- 新版 [`0044c894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c844.md#insn-0044c894) · [`0044c8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c844.md#insn-0044c8cc) · [`0044c85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c844.md#insn-0044c85c)

~~~diff
- 00429b14 ["INT_ADD", "register:40f0:8", ["const:429b14:8", "const:4:8"]]
- 00429b14 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c894 ["INT_ADD", "register:40f0:8", ["const:44c894:8", "const:4:8"]]
+ 0044c894 ["CALL", null, ["callee:00c57b70:8"]]
- 00429b14 bytes 83c51e94
+ 0044c894 bytes b72c2094
- 00429b4c ["INT_ADD", "register:40f0:8", ["const:429b4c:8", "const:4:8"]]
- 00429b4c ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c8cc ["INT_ADD", "register:40f0:8", ["const:44c8cc:8", "const:4:8"]]
+ 0044c8cc ["CALL", null, ["callee:00c57b70:8"]]
- 00429b4c bytes 75c51e94
+ 0044c8cc bytes a92c2094
- 00429adc ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044c85c ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 00429adc bytes 29f4ffb0
+ 0044c85c bytes 89f3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f54e37940ea7178be5688b3271227507"></a>

### [`00429bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429bdc.md) → [`0044c95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c95c.md) FUN_0044c95c

採用 · 移動量 `+0x22d80` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009e1120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1120.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00a3e01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e01c.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c988",
      "incomplete_value": true,
      "site": "0044c99c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429c08",
      "incomplete_value": true,
      "site": "00429c1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044c9a0",
      "incomplete_value": true,
      "site": "0044c9a0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00429c20",
      "incomplete_value": true,
      "site": "00429c20",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c9ac",
      "incomplete_value": false,
      "site": "0044c9b4",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429c2c",
      "incomplete_value": false,
      "site": "00429c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044c988",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044c994",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044c9ac",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c988",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c994",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c9ac",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00429c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429bdc.md#insn-00429c34) · [`00429c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429bdc.md#insn-00429c6c) · [`00429ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429bdc.md#insn-00429ccc)
- 新版 [`0044c9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c95c.md#insn-0044c9b4) · [`0044c9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c95c.md#insn-0044c9ec) · [`0044ca4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c95c.md#insn-0044ca4c)

~~~diff
- 00429c34 ["INT_ADD", "register:40f0:8", ["const:429c34:8", "const:4:8"]]
- 00429c34 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c9b4 ["INT_ADD", "register:40f0:8", ["const:44c9b4:8", "const:4:8"]]
+ 0044c9b4 ["CALL", null, ["callee:00c57b70:8"]]
- 00429c34 bytes 3bc51e94
+ 0044c9b4 bytes 6f2c2094
- 00429c6c ["INT_ADD", "register:40f0:8", ["const:429c6c:8", "const:4:8"]]
- 00429c6c ["CALL", null, ["callee:00c57b70:8"]]
+ 0044c9ec ["INT_ADD", "register:40f0:8", ["const:44c9ec:8", "const:4:8"]]
+ 0044c9ec ["CALL", null, ["callee:00c57b70:8"]]
- 00429c6c bytes 2dc51e94
+ 0044c9ec bytes 612c2094
- 00429ccc ["INT_ADD", "register:40f0:8", ["const:429ccc:8", "const:4:8"]]
- 00429ccc ["CALL", null, ["callee:00c57b70:8"]]
+ 0044ca4c ["INT_ADD", "register:40f0:8", ["const:44ca4c:8", "const:4:8"]]
+ 0044ca4c ["CALL", null, ["callee:00c57b70:8"]]
- 00429ccc bytes 15c51e94
+ 0044ca4c bytes 492c2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc25080635a5bbb70379743b909e0577"></a>

### [`00429de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429de8.md) → [`0044cb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cb68.md) FUN_0044cb68

採用 · 移動量 `+0x22d80` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) [`009e1120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1120.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00a3e01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e01c.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044cb94",
      "incomplete_value": true,
      "site": "0044cba8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429e14",
      "incomplete_value": true,
      "site": "00429e28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044cbac",
      "incomplete_value": true,
      "site": "0044cbac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00429e2c",
      "incomplete_value": true,
      "site": "00429e2c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044cbb8",
      "incomplete_value": false,
      "site": "0044cbc0",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00429e38",
      "incomplete_value": false,
      "site": "00429e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044cb94",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044cba0",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044cbb8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044cb94",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044cba0",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044cbb8",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00429e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429de8.md#insn-00429e40) · [`00429e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429de8.md#insn-00429e78) · [`00429ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429de8.md#insn-00429ed8)
- 新版 [`0044cbc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cb68.md#insn-0044cbc0) · [`0044cbf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cb68.md#insn-0044cbf8) · [`0044cc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cb68.md#insn-0044cc58)

~~~diff
- 00429e40 ["INT_ADD", "register:40f0:8", ["const:429e40:8", "const:4:8"]]
- 00429e40 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044cbc0 ["INT_ADD", "register:40f0:8", ["const:44cbc0:8", "const:4:8"]]
+ 0044cbc0 ["CALL", null, ["callee:00c57b70:8"]]
- 00429e40 bytes b8c41e94
+ 0044cbc0 bytes ec2b2094
- 00429e78 ["INT_ADD", "register:40f0:8", ["const:429e78:8", "const:4:8"]]
- 00429e78 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044cbf8 ["INT_ADD", "register:40f0:8", ["const:44cbf8:8", "const:4:8"]]
+ 0044cbf8 ["CALL", null, ["callee:00c57b70:8"]]
- 00429e78 bytes aac41e94
+ 0044cbf8 bytes de2b2094
- 00429ed8 ["INT_ADD", "register:40f0:8", ["const:429ed8:8", "const:4:8"]]
- 00429ed8 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044cc58 ["INT_ADD", "register:40f0:8", ["const:44cc58:8", "const:4:8"]]
+ 0044cc58 ["CALL", null, ["callee:00c57b70:8"]]
- 00429ed8 bytes 92c41e94
+ 0044cc58 bytes c62b2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c8796ec0e7d72c816a0e27736e8740a"></a>

### [`00429ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429ff4.md) → [`0044cd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cd74.md) FUN_0044cd74

採用 · 移動量 `+0x22d80` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008cacc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ca/008cacc4.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`008feb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008feb94.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044cda0",
      "incomplete_value": true,
      "site": "0044cdb4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a020",
      "incomplete_value": true,
      "site": "0042a034",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044cdb8",
      "incomplete_value": true,
      "site": "0044cdb8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042a038",
      "incomplete_value": true,
      "site": "0042a038",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044cdc4",
      "incomplete_value": false,
      "site": "0044cdcc",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a044",
      "incomplete_value": false,
      "site": "0042a04c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044cda0",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044cdac",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044cdc4",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044cda0",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044cdac",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044cdc4",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042a04c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429ff4.md#insn-0042a04c) · [`0042a084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429ff4.md#insn-0042a084) · [`0042a0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429ff4.md#insn-0042a0e4)
- 新版 [`0044cdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cd74.md#insn-0044cdcc) · [`0044ce04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cd74.md#insn-0044ce04) · [`0044ce64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cd74.md#insn-0044ce64)

~~~diff
- 0042a04c ["INT_ADD", "register:40f0:8", ["const:42a04c:8", "const:4:8"]]
- 0042a04c ["CALL", null, ["callee:00c57b70:8"]]
+ 0044cdcc ["INT_ADD", "register:40f0:8", ["const:44cdcc:8", "const:4:8"]]
+ 0044cdcc ["CALL", null, ["callee:00c57b70:8"]]
- 0042a04c bytes 35c41e94
+ 0044cdcc bytes 692b2094
- 0042a084 ["INT_ADD", "register:40f0:8", ["const:42a084:8", "const:4:8"]]
- 0042a084 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044ce04 ["INT_ADD", "register:40f0:8", ["const:44ce04:8", "const:4:8"]]
+ 0044ce04 ["CALL", null, ["callee:00c57b70:8"]]
- 0042a084 bytes 27c41e94
+ 0044ce04 bytes 5b2b2094
- 0042a0e4 ["INT_ADD", "register:40f0:8", ["const:42a0e4:8", "const:4:8"]]
- 0042a0e4 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044ce64 ["INT_ADD", "register:40f0:8", ["const:44ce64:8", "const:4:8"]]
+ 0044ce64 ["CALL", null, ["callee:00c57b70:8"]]
- 0042a0e4 bytes 0fc41e94
+ 0044ce64 bytes 432b2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-197fea5c33919396329301181f069c21"></a>

### [`0042a200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a200.md) → [`0044cf80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cf80.md) FUN_0044cf80

採用 · 移動量 `+0x22d80` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008cacc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ca/008cacc4.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`008feb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008feb94.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044cfac",
      "incomplete_value": true,
      "site": "0044cfc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a22c",
      "incomplete_value": true,
      "site": "0042a240",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044cfc4",
      "incomplete_value": true,
      "site": "0044cfc4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042a244",
      "incomplete_value": true,
      "site": "0042a244",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044cfd0",
      "incomplete_value": false,
      "site": "0044cfd8",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a250",
      "incomplete_value": false,
      "site": "0042a258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044cfac",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044cfb8",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044cfd0",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044cfac",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044cfb8",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044cfd0",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042a258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a200.md#insn-0042a258) · [`0042a290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a200.md#insn-0042a290) · [`0042a2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a200.md#insn-0042a2f0)
- 新版 [`0044cfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cf80.md#insn-0044cfd8) · [`0044d010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cf80.md#insn-0044d010) · [`0044d070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cf80.md#insn-0044d070)

~~~diff
- 0042a258 ["INT_ADD", "register:40f0:8", ["const:42a258:8", "const:4:8"]]
- 0042a258 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044cfd8 ["INT_ADD", "register:40f0:8", ["const:44cfd8:8", "const:4:8"]]
+ 0044cfd8 ["CALL", null, ["callee:00c57b70:8"]]
- 0042a258 bytes b2c31e94
+ 0044cfd8 bytes e62a2094
- 0042a290 ["INT_ADD", "register:40f0:8", ["const:42a290:8", "const:4:8"]]
- 0042a290 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044d010 ["INT_ADD", "register:40f0:8", ["const:44d010:8", "const:4:8"]]
+ 0044d010 ["CALL", null, ["callee:00c57b70:8"]]
- 0042a290 bytes a4c31e94
+ 0044d010 bytes d82a2094
- 0042a2f0 ["INT_ADD", "register:40f0:8", ["const:42a2f0:8", "const:4:8"]]
- 0042a2f0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044d070 ["INT_ADD", "register:40f0:8", ["const:44d070:8", "const:4:8"]]
+ 0044d070 ["CALL", null, ["callee:00c57b70:8"]]
- 0042a2f0 bytes 8cc31e94
+ 0044d070 bytes c02a2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f47629612ef1d39545ea7dceee28c88a"></a>

### [`0042a40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a40c.md) → [`0044d18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d18c.md) FUN_0044d18c

採用 · 移動量 `+0x22d80` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008e6014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e6/008e6014.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`0091a0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a0f8.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d1c4",
      "incomplete_value": true,
      "site": "0044d1d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a444",
      "incomplete_value": true,
      "site": "0042a458",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044d1dc",
      "incomplete_value": true,
      "site": "0044d1dc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042a45c",
      "incomplete_value": true,
      "site": "0042a45c",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d1e4",
      "incomplete_value": false,
      "site": "0044d1ec",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a464",
      "incomplete_value": false,
      "site": "0042a46c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044d1c4",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044d1c8",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044d1e4",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d1c4",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044d1c8",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044d1e4",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042a46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a40c.md#insn-0042a46c) · [`0042a4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a40c.md#insn-0042a4a4) · [`0042a504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a40c.md#insn-0042a504)
- 新版 [`0044d1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d18c.md#insn-0044d1ec) · [`0044d224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d18c.md#insn-0044d224) · [`0044d284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d18c.md#insn-0044d284)

~~~diff
- 0042a46c ["INT_ADD", "register:40f0:8", ["const:42a46c:8", "const:4:8"]]
- 0042a46c ["CALL", null, ["callee:00c57b70:8"]]
+ 0044d1ec ["INT_ADD", "register:40f0:8", ["const:44d1ec:8", "const:4:8"]]
+ 0044d1ec ["CALL", null, ["callee:00c57b70:8"]]
- 0042a46c bytes 2dc31e94
+ 0044d1ec bytes 612a2094
- 0042a4a4 ["INT_ADD", "register:40f0:8", ["const:42a4a4:8", "const:4:8"]]
- 0042a4a4 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044d224 ["INT_ADD", "register:40f0:8", ["const:44d224:8", "const:4:8"]]
+ 0044d224 ["CALL", null, ["callee:00c57b70:8"]]
- 0042a4a4 bytes 1fc31e94
+ 0044d224 bytes 532a2094
- 0042a504 ["INT_ADD", "register:40f0:8", ["const:42a504:8", "const:4:8"]]
- 0042a504 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044d284 ["INT_ADD", "register:40f0:8", ["const:44d284:8", "const:4:8"]]
+ 0044d284 ["CALL", null, ["callee:00c57b70:8"]]
- 0042a504 bytes 07c31e94
+ 0044d284 bytes 3b2a2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01a8759e0309c9f4b3b840a7136da7ca"></a>

### [`0042a700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a700.md) → [`0044d480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d480.md) FUN_0044d480

採用 · 移動量 `+0x22d80` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008e0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e0/008e0bc0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d4a8",
      "incomplete_value": true,
      "site": "0044d4b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a728",
      "incomplete_value": true,
      "site": "0042a738",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044d4bc",
      "incomplete_value": true,
      "site": "0044d4bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042a73c",
      "incomplete_value": true,
      "site": "0042a73c",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d4c8",
      "incomplete_value": false,
      "site": "0044d4d0",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a748",
      "incomplete_value": false,
      "site": "0042a750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044d4a8",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044d4b0",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044d4c8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d4a8",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044d4b0",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044d4c8",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042a750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a700.md#insn-0042a750) · [`0042a788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a700.md#insn-0042a788) · [`0042a718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a700.md#insn-0042a718)
- 新版 [`0044d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d480.md#insn-0044d4d0) · [`0044d508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d480.md#insn-0044d508) · [`0044d498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d480.md#insn-0044d498)

~~~diff
- 0042a750 ["INT_ADD", "register:40f0:8", ["const:42a750:8", "const:4:8"]]
- 0042a750 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044d4d0 ["INT_ADD", "register:40f0:8", ["const:44d4d0:8", "const:4:8"]]
+ 0044d4d0 ["CALL", null, ["callee:00c57b70:8"]]
- 0042a750 bytes 74c21e94
+ 0044d4d0 bytes a8292094
- 0042a788 ["INT_ADD", "register:40f0:8", ["const:42a788:8", "const:4:8"]]
- 0042a788 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044d508 ["INT_ADD", "register:40f0:8", ["const:44d508:8", "const:4:8"]]
+ 0044d508 ["CALL", null, ["callee:00c57b70:8"]]
- 0042a788 bytes 66c21e94
+ 0044d508 bytes 9a292094
- 0042a718 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044d498 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042a718 bytes 29f4ff90
+ 0044d498 bytes 89f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f627f1688dfe51694ae0700a5dbdbe4"></a>

### [`0042a818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a818.md) → [`0044d598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d598.md) FUN_0044d598

採用 · 移動量 `+0x22d80` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d5c0",
      "incomplete_value": true,
      "site": "0044d5d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a840",
      "incomplete_value": true,
      "site": "0042a850",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044d5d4",
      "incomplete_value": true,
      "site": "0044d5d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042a854",
      "incomplete_value": true,
      "site": "0042a854",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d5e0",
      "incomplete_value": false,
      "site": "0044d5e8",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a860",
      "incomplete_value": false,
      "site": "0042a868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044d5c0",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044d5c8",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044d5e0",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d5c0",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044d5c8",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044d5e0",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042a868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a818.md#insn-0042a868) · [`0042a8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a818.md#insn-0042a8a0) · [`0042a830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a818.md#insn-0042a830)
- 新版 [`0044d5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d598.md#insn-0044d5e8) · [`0044d620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d598.md#insn-0044d620) · [`0044d5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d598.md#insn-0044d5b0)

~~~diff
- 0042a868 ["INT_ADD", "register:40f0:8", ["const:42a868:8", "const:4:8"]]
- 0042a868 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044d5e8 ["INT_ADD", "register:40f0:8", ["const:44d5e8:8", "const:4:8"]]
+ 0044d5e8 ["CALL", null, ["callee:00c57b70:8"]]
- 0042a868 bytes 2ec21e94
+ 0044d5e8 bytes 62292094
- 0042a8a0 ["INT_ADD", "register:40f0:8", ["const:42a8a0:8", "const:4:8"]]
- 0042a8a0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044d620 ["INT_ADD", "register:40f0:8", ["const:44d620:8", "const:4:8"]]
+ 0044d620 ["CALL", null, ["callee:00c57b70:8"]]
- 0042a8a0 bytes 20c21e94
+ 0044d620 bytes 54292094
- 0042a830 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044d5b0 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042a830 bytes 29f4ff90
+ 0044d5b0 bytes 89f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77c4e3e294d97d0e9a9ca71001ebbea7"></a>

### [`0042a930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a930.md) → [`0044d7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d7c8.md) FUN_0044d7c8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d7f0",
      "incomplete_value": true,
      "site": "0044d800",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a958",
      "incomplete_value": true,
      "site": "0042a968",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044d804",
      "incomplete_value": true,
      "site": "0044d804",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042a96c",
      "incomplete_value": true,
      "site": "0042a96c",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d810",
      "incomplete_value": false,
      "site": "0044d818",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042a978",
      "incomplete_value": false,
      "site": "0042a980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044d7f0",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044d7f8",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044d810",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d7f0",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044d7f8",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044d810",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042a980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a930.md#insn-0042a980) · [`0042a9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a930.md#insn-0042a9b8) · [`0042a948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042a930.md#insn-0042a948)
- 新版 [`0044d818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d7c8.md#insn-0044d818) · [`0044d850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d7c8.md#insn-0044d850) · [`0044d7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d7c8.md#insn-0044d7e0)

~~~diff
- 0042a980 ["INT_ADD", "register:40f0:8", ["const:42a980:8", "const:4:8"]]
- 0042a980 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044d818 ["INT_ADD", "register:40f0:8", ["const:44d818:8", "const:4:8"]]
+ 0044d818 ["CALL", null, ["callee:00c57b70:8"]]
- 0042a980 bytes e8c11e94
+ 0044d818 bytes d6282094
- 0042a9b8 ["INT_ADD", "register:40f0:8", ["const:42a9b8:8", "const:4:8"]]
- 0042a9b8 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044d850 ["INT_ADD", "register:40f0:8", ["const:44d850:8", "const:4:8"]]
+ 0044d850 ["CALL", null, ["callee:00c57b70:8"]]
- 0042a9b8 bytes dac11e94
+ 0044d850 bytes c8282094
- 0042a948 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044d7e0 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042a948 bytes 29f4ff90
+ 0044d7e0 bytes 89f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a78b20709759472f81e8757bc1c922cc"></a>

### [`0042aa48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042aa48.md) → [`0044d8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d8e0.md) FUN_0044d8e0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a2308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a2/005a2308.md) [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 4件 [`005c6938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md) [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d908",
      "incomplete_value": true,
      "site": "0044d918",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042aa70",
      "incomplete_value": true,
      "site": "0042aa80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044d91c",
      "incomplete_value": true,
      "site": "0044d91c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042aa84",
      "incomplete_value": true,
      "site": "0042aa84",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d928",
      "incomplete_value": false,
      "site": "0044d930",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042aa90",
      "incomplete_value": false,
      "site": "0042aa98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044d908",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044d910",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044d928",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d908",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044d910",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044d928",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042aa98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042aa48.md#insn-0042aa98) · [`0042aad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042aa48.md#insn-0042aad0) · [`0042aa60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042aa48.md#insn-0042aa60)
- 新版 [`0044d930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d8e0.md#insn-0044d930) · [`0044d968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d8e0.md#insn-0044d968) · [`0044d8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d8e0.md#insn-0044d8f8)

~~~diff
- 0042aa98 ["INT_ADD", "register:40f0:8", ["const:42aa98:8", "const:4:8"]]
- 0042aa98 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044d930 ["INT_ADD", "register:40f0:8", ["const:44d930:8", "const:4:8"]]
+ 0044d930 ["CALL", null, ["callee:00c57b70:8"]]
- 0042aa98 bytes a2c11e94
+ 0044d930 bytes 90282094
- 0042aad0 ["INT_ADD", "register:40f0:8", ["const:42aad0:8", "const:4:8"]]
- 0042aad0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044d968 ["INT_ADD", "register:40f0:8", ["const:44d968:8", "const:4:8"]]
+ 0044d968 ["CALL", null, ["callee:00c57b70:8"]]
- 0042aad0 bytes 94c11e94
+ 0044d968 bytes 82282094
- 0042aa60 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044d8f8 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042aa60 bytes 29f4ff90
+ 0044d8f8 bytes 89f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edbc1044683ea94001e3886f39364c44"></a>

### [`0042ab60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042ab60.md) → [`0044d9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d9f8.md) FUN_0044d9f8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0089f1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089f/0089f1c4.md) [`008a5bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5bd0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 2件 [`008d305c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d305c.md) [`008d9a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a68.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044da20",
      "incomplete_value": true,
      "site": "0044da30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ab88",
      "incomplete_value": true,
      "site": "0042ab98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044da34",
      "incomplete_value": true,
      "site": "0044da34",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042ab9c",
      "incomplete_value": true,
      "site": "0042ab9c",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044da40",
      "incomplete_value": false,
      "site": "0044da48",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042aba8",
      "incomplete_value": false,
      "site": "0042abb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044da20",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044da28",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044da40",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044da20",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044da28",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044da40",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042abb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042ab60.md#insn-0042abb0) · [`0042abe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042ab60.md#insn-0042abe8) · [`0042ab78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042ab60.md#insn-0042ab78)
- 新版 [`0044da48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d9f8.md#insn-0044da48) · [`0044da80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d9f8.md#insn-0044da80) · [`0044da10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d9f8.md#insn-0044da10)

~~~diff
- 0042abb0 ["INT_ADD", "register:40f0:8", ["const:42abb0:8", "const:4:8"]]
- 0042abb0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044da48 ["INT_ADD", "register:40f0:8", ["const:44da48:8", "const:4:8"]]
+ 0044da48 ["CALL", null, ["callee:00c57b70:8"]]
- 0042abb0 bytes 5cc11e94
+ 0044da48 bytes 4a282094
- 0042abe8 ["INT_ADD", "register:40f0:8", ["const:42abe8:8", "const:4:8"]]
- 0042abe8 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044da80 ["INT_ADD", "register:40f0:8", ["const:44da80:8", "const:4:8"]]
+ 0044da80 ["CALL", null, ["callee:00c57b70:8"]]
- 0042abe8 bytes 4ec11e94
+ 0044da80 bytes 3c282094
- 0042ab78 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044da10 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042ab78 bytes 29f4ff90
+ 0044da10 bytes 89f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6935433b94726b9d31558ce2da170bd7"></a>

### [`0042ac78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042ac78.md) → [`0044db10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044db10.md) FUN_0044db10

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00632468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/00632468.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00657f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657f4c.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044db38",
      "incomplete_value": true,
      "site": "0044db48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042aca0",
      "incomplete_value": true,
      "site": "0042acb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044db4c",
      "incomplete_value": true,
      "site": "0044db4c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042acb4",
      "incomplete_value": true,
      "site": "0042acb4",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044db58",
      "incomplete_value": false,
      "site": "0044db60",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042acc0",
      "incomplete_value": false,
      "site": "0042acc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044db38",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044db40",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044db58",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044db38",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044db40",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044db58",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042acc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042ac78.md#insn-0042acc8) · [`0042ad00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042ac78.md#insn-0042ad00) · [`0042ac90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042ac78.md#insn-0042ac90)
- 新版 [`0044db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044db10.md#insn-0044db60) · [`0044db98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044db10.md#insn-0044db98) · [`0044db28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044db10.md#insn-0044db28)

~~~diff
- 0042acc8 ["INT_ADD", "register:40f0:8", ["const:42acc8:8", "const:4:8"]]
- 0042acc8 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044db60 ["INT_ADD", "register:40f0:8", ["const:44db60:8", "const:4:8"]]
+ 0044db60 ["CALL", null, ["callee:00c57b70:8"]]
- 0042acc8 bytes 16c11e94
+ 0044db60 bytes 04282094
- 0042ad00 ["INT_ADD", "register:40f0:8", ["const:42ad00:8", "const:4:8"]]
- 0042ad00 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044db98 ["INT_ADD", "register:40f0:8", ["const:44db98:8", "const:4:8"]]
+ 0044db98 ["CALL", null, ["callee:00c57b70:8"]]
- 0042ad00 bytes 08c11e94
+ 0044db98 bytes f6272094
- 0042ac90 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044db28 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042ac90 bytes 29f4ff90
+ 0044db28 bytes 89f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc9187159236ab98159fd0bb99e9c970"></a>

### [`0042ad90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042ad90.md) → [`0044dc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dc28.md) FUN_0044dc28

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 2件 [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044dc50",
      "incomplete_value": true,
      "site": "0044dc60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042adb8",
      "incomplete_value": true,
      "site": "0042adc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044dc64",
      "incomplete_value": true,
      "site": "0044dc64",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042adcc",
      "incomplete_value": true,
      "site": "0042adcc",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044dc70",
      "incomplete_value": false,
      "site": "0044dc78",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042add8",
      "incomplete_value": false,
      "site": "0042ade0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044dc50",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044dc58",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044dc70",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044dc50",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044dc58",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044dc70",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042ade0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042ad90.md#insn-0042ade0) · [`0042ae18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042ad90.md#insn-0042ae18) · [`0042ada8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042ad90.md#insn-0042ada8)
- 新版 [`0044dc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dc28.md#insn-0044dc78) · [`0044dcb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dc28.md#insn-0044dcb0) · [`0044dc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dc28.md#insn-0044dc40)

~~~diff
- 0042ade0 ["INT_ADD", "register:40f0:8", ["const:42ade0:8", "const:4:8"]]
- 0042ade0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044dc78 ["INT_ADD", "register:40f0:8", ["const:44dc78:8", "const:4:8"]]
+ 0044dc78 ["CALL", null, ["callee:00c57b70:8"]]
- 0042ade0 bytes d0c01e94
+ 0044dc78 bytes be272094
- 0042ae18 ["INT_ADD", "register:40f0:8", ["const:42ae18:8", "const:4:8"]]
- 0042ae18 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044dcb0 ["INT_ADD", "register:40f0:8", ["const:44dcb0:8", "const:4:8"]]
+ 0044dcb0 ["CALL", null, ["callee:00c57b70:8"]]
- 0042ae18 bytes c2c01e94
+ 0044dcb0 bytes b0272094
- 0042ada8 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044dc40 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042ada8 bytes 29f4ff90
+ 0044dc40 bytes 89f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ce0a10d53b5d33dcd4c6882ae07da52"></a>

### [`0042aea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042aea8.md) → [`0044dd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dd40.md) FUN_0044dd40

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0083d5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083d5f0.md) [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 2件 [`0086f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f8dc.md) [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044dd68",
      "incomplete_value": true,
      "site": "0044dd78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042aed0",
      "incomplete_value": true,
      "site": "0042aee0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044dd7c",
      "incomplete_value": true,
      "site": "0044dd7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042aee4",
      "incomplete_value": true,
      "site": "0042aee4",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044dd88",
      "incomplete_value": false,
      "site": "0044dd90",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042aef0",
      "incomplete_value": false,
      "site": "0042aef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044dd68",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044dd70",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044dd88",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044dd68",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044dd70",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044dd88",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042aef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042aea8.md#insn-0042aef8) · [`0042af30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042aea8.md#insn-0042af30) · [`0042aec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042aea8.md#insn-0042aec0)
- 新版 [`0044dd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dd40.md#insn-0044dd90) · [`0044ddc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dd40.md#insn-0044ddc8) · [`0044dd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dd40.md#insn-0044dd58)

~~~diff
- 0042aef8 ["INT_ADD", "register:40f0:8", ["const:42aef8:8", "const:4:8"]]
- 0042aef8 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044dd90 ["INT_ADD", "register:40f0:8", ["const:44dd90:8", "const:4:8"]]
+ 0044dd90 ["CALL", null, ["callee:00c57b70:8"]]
- 0042aef8 bytes 8ac01e94
+ 0044dd90 bytes 78272094
- 0042af30 ["INT_ADD", "register:40f0:8", ["const:42af30:8", "const:4:8"]]
- 0042af30 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044ddc8 ["INT_ADD", "register:40f0:8", ["const:44ddc8:8", "const:4:8"]]
+ 0044ddc8 ["CALL", null, ["callee:00c57b70:8"]]
- 0042af30 bytes 7cc01e94
+ 0044ddc8 bytes 6a272094
- 0042aec0 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044dd58 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042aec0 bytes 29f4ff90
+ 0044dd58 bytes 89f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-063d5e79f1fc53a9555c178a706c063e"></a>

### [`0042afc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042afc0.md) → [`0044de58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044de58.md) FUN_0044de58

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044de80",
      "incomplete_value": true,
      "site": "0044de90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042afe8",
      "incomplete_value": true,
      "site": "0042aff8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044de94",
      "incomplete_value": true,
      "site": "0044de94",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042affc",
      "incomplete_value": true,
      "site": "0042affc",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044dea0",
      "incomplete_value": false,
      "site": "0044dea8",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b008",
      "incomplete_value": false,
      "site": "0042b010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044de80",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044de88",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044dea0",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044de80",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044de88",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044dea0",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042afc0.md#insn-0042b010) · [`0042b048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042afc0.md#insn-0042b048) · [`0042afd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042afc0.md#insn-0042afd8)
- 新版 [`0044dea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044de58.md#insn-0044dea8) · [`0044dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044de58.md#insn-0044dee0) · [`0044de70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044de58.md#insn-0044de70)

~~~diff
- 0042b010 ["INT_ADD", "register:40f0:8", ["const:42b010:8", "const:4:8"]]
- 0042b010 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044dea8 ["INT_ADD", "register:40f0:8", ["const:44dea8:8", "const:4:8"]]
+ 0044dea8 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b010 bytes 44c01e94
+ 0044dea8 bytes 32272094
- 0042b048 ["INT_ADD", "register:40f0:8", ["const:42b048:8", "const:4:8"]]
- 0042b048 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044dee0 ["INT_ADD", "register:40f0:8", ["const:44dee0:8", "const:4:8"]]
+ 0044dee0 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b048 bytes 36c01e94
+ 0044dee0 bytes 24272094
- 0042afd8 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044de70 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042afd8 bytes 29f4ff90
+ 0044de70 bytes 89f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b61df3620103a8cbfbe068710afbf75"></a>

### [`0042b0d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b0d8.md) → [`0044df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044df70.md) FUN_0044df70

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044df98",
      "incomplete_value": true,
      "site": "0044dfa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b100",
      "incomplete_value": true,
      "site": "0042b110",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044dfac",
      "incomplete_value": true,
      "site": "0044dfac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042b114",
      "incomplete_value": true,
      "site": "0042b114",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044dfb8",
      "incomplete_value": false,
      "site": "0044dfc0",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b120",
      "incomplete_value": false,
      "site": "0042b128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044df98",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044dfa0",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044dfb8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044df98",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044dfa0",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044dfb8",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b0d8.md#insn-0042b128) · [`0042b160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b0d8.md#insn-0042b160) · [`0042b0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b0d8.md#insn-0042b0f0)
- 新版 [`0044dfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044df70.md#insn-0044dfc0) · [`0044dff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044df70.md#insn-0044dff8) · [`0044df88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044df70.md#insn-0044df88)

~~~diff
- 0042b128 ["INT_ADD", "register:40f0:8", ["const:42b128:8", "const:4:8"]]
- 0042b128 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044dfc0 ["INT_ADD", "register:40f0:8", ["const:44dfc0:8", "const:4:8"]]
+ 0044dfc0 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b128 bytes febf1e94
+ 0044dfc0 bytes ec262094
- 0042b160 ["INT_ADD", "register:40f0:8", ["const:42b160:8", "const:4:8"]]
- 0042b160 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044dff8 ["INT_ADD", "register:40f0:8", ["const:44dff8:8", "const:4:8"]]
+ 0044dff8 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b160 bytes f0bf1e94
+ 0044dff8 bytes de262094
- 0042b0f0 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044df88 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042b0f0 bytes 09f4fff0
+ 0044df88 bytes 89f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32a6ffab22b3a5c7b73e928c13d71baa"></a>

### [`0042b1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b1f0.md) → [`0044e088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e088.md) FUN_0044e088

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e0b0",
      "incomplete_value": true,
      "site": "0044e0c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b218",
      "incomplete_value": true,
      "site": "0042b228",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044e0c4",
      "incomplete_value": true,
      "site": "0044e0c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042b22c",
      "incomplete_value": true,
      "site": "0042b22c",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e0d0",
      "incomplete_value": false,
      "site": "0044e0d8",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b238",
      "incomplete_value": false,
      "site": "0042b240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044e0b0",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044e0b8",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044e0d0",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e0b0",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e0b8",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e0d0",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b1f0.md#insn-0042b240) · [`0042b278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b1f0.md#insn-0042b278) · [`0042b208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b1f0.md#insn-0042b208)
- 新版 [`0044e0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e088.md#insn-0044e0d8) · [`0044e110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e088.md#insn-0044e110) · [`0044e0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e088.md#insn-0044e0a0)

~~~diff
- 0042b240 ["INT_ADD", "register:40f0:8", ["const:42b240:8", "const:4:8"]]
- 0042b240 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e0d8 ["INT_ADD", "register:40f0:8", ["const:44e0d8:8", "const:4:8"]]
+ 0044e0d8 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b240 bytes b8bf1e94
+ 0044e0d8 bytes a6262094
- 0042b278 ["INT_ADD", "register:40f0:8", ["const:42b278:8", "const:4:8"]]
- 0042b278 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e110 ["INT_ADD", "register:40f0:8", ["const:44e110:8", "const:4:8"]]
+ 0044e110 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b278 bytes aabf1e94
+ 0044e110 bytes 98262094
- 0042b208 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044e0a0 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042b208 bytes 09f4fff0
+ 0044e0a0 bytes 89f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b06d7fa4aeedc9857c6813d513a14b2"></a>

### [`0042b308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b308.md) → [`0044e1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e1a0.md) FUN_0044e1a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 4件 [`005fa7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fa/005fa7e4.md) [`005faf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fa/005faf94.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e1c8",
      "incomplete_value": true,
      "site": "0044e1d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b330",
      "incomplete_value": true,
      "site": "0042b340",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044e1dc",
      "incomplete_value": true,
      "site": "0044e1dc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042b344",
      "incomplete_value": true,
      "site": "0042b344",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e1e8",
      "incomplete_value": false,
      "site": "0044e1f0",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b350",
      "incomplete_value": false,
      "site": "0042b358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044e1c8",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044e1d0",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044e1e8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e1c8",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e1d0",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e1e8",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b308.md#insn-0042b358) · [`0042b390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b308.md#insn-0042b390) · [`0042b320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b308.md#insn-0042b320)
- 新版 [`0044e1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e1a0.md#insn-0044e1f0) · [`0044e228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e1a0.md#insn-0044e228) · [`0044e1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e1a0.md#insn-0044e1b8)

~~~diff
- 0042b358 ["INT_ADD", "register:40f0:8", ["const:42b358:8", "const:4:8"]]
- 0042b358 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e1f0 ["INT_ADD", "register:40f0:8", ["const:44e1f0:8", "const:4:8"]]
+ 0044e1f0 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b358 bytes 72bf1e94
+ 0044e1f0 bytes 60262094
- 0042b390 ["INT_ADD", "register:40f0:8", ["const:42b390:8", "const:4:8"]]
- 0042b390 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e228 ["INT_ADD", "register:40f0:8", ["const:44e228:8", "const:4:8"]]
+ 0044e228 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b390 bytes 64bf1e94
+ 0044e228 bytes 52262094
- 0042b320 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044e1b8 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042b320 bytes 09f4fff0
+ 0044e1b8 bytes 89f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3608b592c1ca59b2add5e97da92a570e"></a>

### [`0042b420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b420.md) → [`0044e2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e2b8.md) FUN_0044e2b8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e2e0",
      "incomplete_value": true,
      "site": "0044e2f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b448",
      "incomplete_value": true,
      "site": "0042b458",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044e2f4",
      "incomplete_value": true,
      "site": "0044e2f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042b45c",
      "incomplete_value": true,
      "site": "0042b45c",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e300",
      "incomplete_value": false,
      "site": "0044e308",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b468",
      "incomplete_value": false,
      "site": "0042b470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044e2e0",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044e2e8",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044e300",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e2e0",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e2e8",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e300",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b420.md#insn-0042b470) · [`0042b4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b420.md#insn-0042b4a8) · [`0042b438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b420.md#insn-0042b438)
- 新版 [`0044e308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e2b8.md#insn-0044e308) · [`0044e340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e2b8.md#insn-0044e340) · [`0044e2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e2b8.md#insn-0044e2d0)

~~~diff
- 0042b470 ["INT_ADD", "register:40f0:8", ["const:42b470:8", "const:4:8"]]
- 0042b470 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e308 ["INT_ADD", "register:40f0:8", ["const:44e308:8", "const:4:8"]]
+ 0044e308 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b470 bytes 2cbf1e94
+ 0044e308 bytes 1a262094
- 0042b4a8 ["INT_ADD", "register:40f0:8", ["const:42b4a8:8", "const:4:8"]]
- 0042b4a8 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e340 ["INT_ADD", "register:40f0:8", ["const:44e340:8", "const:4:8"]]
+ 0044e340 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b4a8 bytes 1ebf1e94
+ 0044e340 bytes 0c262094
- 0042b438 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044e2d0 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042b438 bytes 09f4fff0
+ 0044e2d0 bytes 89f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1bf54a54f20a16989e2c25e91155b36"></a>

### [`0042b538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b538.md) → [`0044e3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e3d0.md) FUN_0044e3d0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e3f8",
      "incomplete_value": true,
      "site": "0044e408",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b560",
      "incomplete_value": true,
      "site": "0042b570",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044e40c",
      "incomplete_value": true,
      "site": "0044e40c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042b574",
      "incomplete_value": true,
      "site": "0042b574",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e418",
      "incomplete_value": false,
      "site": "0044e420",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b580",
      "incomplete_value": false,
      "site": "0042b588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044e3f8",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044e400",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044e418",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e3f8",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e400",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e418",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b538.md#insn-0042b588) · [`0042b5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b538.md#insn-0042b5c0) · [`0042b550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b538.md#insn-0042b550)
- 新版 [`0044e420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e3d0.md#insn-0044e420) · [`0044e458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e3d0.md#insn-0044e458) · [`0044e3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e3d0.md#insn-0044e3e8)

~~~diff
- 0042b588 ["INT_ADD", "register:40f0:8", ["const:42b588:8", "const:4:8"]]
- 0042b588 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e420 ["INT_ADD", "register:40f0:8", ["const:44e420:8", "const:4:8"]]
+ 0044e420 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b588 bytes e6be1e94
+ 0044e420 bytes d4252094
- 0042b5c0 ["INT_ADD", "register:40f0:8", ["const:42b5c0:8", "const:4:8"]]
- 0042b5c0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e458 ["INT_ADD", "register:40f0:8", ["const:44e458:8", "const:4:8"]]
+ 0044e458 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b5c0 bytes d8be1e94
+ 0044e458 bytes c6252094
- 0042b550 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044e3e8 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042b550 bytes 09f4fff0
+ 0044e3e8 bytes 89f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2cd887fd4d2b49ef14d3cafa0771c81"></a>

### [`0042b650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b650.md) → [`0044e4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e4e8.md) FUN_0044e4e8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e510",
      "incomplete_value": true,
      "site": "0044e520",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b678",
      "incomplete_value": true,
      "site": "0042b688",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044e524",
      "incomplete_value": true,
      "site": "0044e524",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042b68c",
      "incomplete_value": true,
      "site": "0042b68c",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e530",
      "incomplete_value": false,
      "site": "0044e538",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b698",
      "incomplete_value": false,
      "site": "0042b6a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044e510",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044e518",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044e530",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e510",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e518",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e530",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b650.md#insn-0042b6a0) · [`0042b6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b650.md#insn-0042b6d8) · [`0042b668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b650.md#insn-0042b668)
- 新版 [`0044e538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e4e8.md#insn-0044e538) · [`0044e570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e4e8.md#insn-0044e570) · [`0044e500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e4e8.md#insn-0044e500)

~~~diff
- 0042b6a0 ["INT_ADD", "register:40f0:8", ["const:42b6a0:8", "const:4:8"]]
- 0042b6a0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e538 ["INT_ADD", "register:40f0:8", ["const:44e538:8", "const:4:8"]]
+ 0044e538 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b6a0 bytes a0be1e94
+ 0044e538 bytes 8e252094
- 0042b6d8 ["INT_ADD", "register:40f0:8", ["const:42b6d8:8", "const:4:8"]]
- 0042b6d8 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e570 ["INT_ADD", "register:40f0:8", ["const:44e570:8", "const:4:8"]]
+ 0044e570 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b6d8 bytes 92be1e94
+ 0044e570 bytes 80252094
- 0042b668 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044e500 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042b668 bytes 09f4fff0
+ 0044e500 bytes 89f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16772c77edadc6bc6b3c66290c7d43ce"></a>

### [`0042b768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b768.md) → [`0044e600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e600.md) FUN_0044e600

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a62748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62748.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00ac0700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0700.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e628",
      "incomplete_value": true,
      "site": "0044e638",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b790",
      "incomplete_value": true,
      "site": "0042b7a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044e63c",
      "incomplete_value": true,
      "site": "0044e63c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042b7a4",
      "incomplete_value": true,
      "site": "0042b7a4",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e648",
      "incomplete_value": false,
      "site": "0044e650",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b7b0",
      "incomplete_value": false,
      "site": "0042b7b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044e628",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044e630",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044e648",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e628",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e630",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e648",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b768.md#insn-0042b7b8) · [`0042b7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b768.md#insn-0042b7f0) · [`0042b780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b768.md#insn-0042b780)
- 新版 [`0044e650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e600.md#insn-0044e650) · [`0044e688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e600.md#insn-0044e688) · [`0044e618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e600.md#insn-0044e618)

~~~diff
- 0042b7b8 ["INT_ADD", "register:40f0:8", ["const:42b7b8:8", "const:4:8"]]
- 0042b7b8 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e650 ["INT_ADD", "register:40f0:8", ["const:44e650:8", "const:4:8"]]
+ 0044e650 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b7b8 bytes 5abe1e94
+ 0044e650 bytes 48252094
- 0042b7f0 ["INT_ADD", "register:40f0:8", ["const:42b7f0:8", "const:4:8"]]
- 0042b7f0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e688 ["INT_ADD", "register:40f0:8", ["const:44e688:8", "const:4:8"]]
+ 0044e688 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b7f0 bytes 4cbe1e94
+ 0044e688 bytes 3a252094
- 0042b780 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044e618 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042b780 bytes 09f4fff0
+ 0044e618 bytes 89f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc79afadbc8a4c631143bb4b25ce5056"></a>

### [`0042b880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b880.md) → [`0044e718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e718.md) FUN_0044e718

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e740",
      "incomplete_value": true,
      "site": "0044e750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b8a8",
      "incomplete_value": true,
      "site": "0042b8b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044e754",
      "incomplete_value": true,
      "site": "0044e754",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042b8bc",
      "incomplete_value": true,
      "site": "0042b8bc",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e760",
      "incomplete_value": false,
      "site": "0044e768",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b8c8",
      "incomplete_value": false,
      "site": "0042b8d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044e740",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044e748",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044e760",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e740",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e748",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e760",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b880.md#insn-0042b8d0) · [`0042b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b880.md#insn-0042b908) · [`0042b898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b880.md#insn-0042b898)
- 新版 [`0044e768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e718.md#insn-0044e768) · [`0044e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e718.md#insn-0044e7a0) · [`0044e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e718.md#insn-0044e730)

~~~diff
- 0042b8d0 ["INT_ADD", "register:40f0:8", ["const:42b8d0:8", "const:4:8"]]
- 0042b8d0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e768 ["INT_ADD", "register:40f0:8", ["const:44e768:8", "const:4:8"]]
+ 0044e768 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b8d0 bytes 14be1e94
+ 0044e768 bytes 02252094
- 0042b908 ["INT_ADD", "register:40f0:8", ["const:42b908:8", "const:4:8"]]
- 0042b908 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e7a0 ["INT_ADD", "register:40f0:8", ["const:44e7a0:8", "const:4:8"]]
+ 0044e7a0 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b908 bytes 06be1e94
+ 0044e7a0 bytes f4242094
- 0042b898 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044e730 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042b898 bytes 09f4fff0
+ 0044e730 bytes 89f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-304b95d310d29afd222d4a86755bb7ab"></a>

### [`0042b998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b998.md) → [`0044e830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e830.md) FUN_0044e830

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e858",
      "incomplete_value": true,
      "site": "0044e868",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b9c0",
      "incomplete_value": true,
      "site": "0042b9d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044e86c",
      "incomplete_value": true,
      "site": "0044e86c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042b9d4",
      "incomplete_value": true,
      "site": "0042b9d4",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e878",
      "incomplete_value": false,
      "site": "0044e880",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042b9e0",
      "incomplete_value": false,
      "site": "0042b9e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044e858",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044e860",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044e878",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e858",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e860",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e878",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042b9e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b998.md#insn-0042b9e8) · [`0042ba20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b998.md#insn-0042ba20) · [`0042b9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042b998.md#insn-0042b9b0)
- 新版 [`0044e880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e830.md#insn-0044e880) · [`0044e8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e830.md#insn-0044e8b8) · [`0044e848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e830.md#insn-0044e848)

~~~diff
- 0042b9e8 ["INT_ADD", "register:40f0:8", ["const:42b9e8:8", "const:4:8"]]
- 0042b9e8 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e880 ["INT_ADD", "register:40f0:8", ["const:44e880:8", "const:4:8"]]
+ 0044e880 ["CALL", null, ["callee:00c57b70:8"]]
- 0042b9e8 bytes cebd1e94
+ 0044e880 bytes bc242094
- 0042ba20 ["INT_ADD", "register:40f0:8", ["const:42ba20:8", "const:4:8"]]
- 0042ba20 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e8b8 ["INT_ADD", "register:40f0:8", ["const:44e8b8:8", "const:4:8"]]
+ 0044e8b8 ["CALL", null, ["callee:00c57b70:8"]]
- 0042ba20 bytes c0bd1e94
+ 0044e8b8 bytes ae242094
- 0042b9b0 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044e848 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042b9b0 bytes 09f4fff0
+ 0044e848 bytes 89f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acf4d7c4132c4740646484a78f56313a"></a>

### [`0042bab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bab0.md) → [`0044e948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e948.md) FUN_0044e948

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008b266c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b2/008b266c.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`008e6510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e6/008e6510.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e970",
      "incomplete_value": true,
      "site": "0044e980",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bad8",
      "incomplete_value": true,
      "site": "0042bae8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044e984",
      "incomplete_value": true,
      "site": "0044e984",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042baec",
      "incomplete_value": true,
      "site": "0042baec",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e990",
      "incomplete_value": false,
      "site": "0044e998",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042baf8",
      "incomplete_value": false,
      "site": "0042bb00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044e970",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044e978",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044e990",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e970",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e978",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e990",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042bb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bab0.md#insn-0042bb00) · [`0042bb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bab0.md#insn-0042bb38) · [`0042bac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bab0.md#insn-0042bac8)
- 新版 [`0044e998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e948.md#insn-0044e998) · [`0044e9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e948.md#insn-0044e9d0) · [`0044e960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e948.md#insn-0044e960)

~~~diff
- 0042bb00 ["INT_ADD", "register:40f0:8", ["const:42bb00:8", "const:4:8"]]
- 0042bb00 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e998 ["INT_ADD", "register:40f0:8", ["const:44e998:8", "const:4:8"]]
+ 0044e998 ["CALL", null, ["callee:00c57b70:8"]]
- 0042bb00 bytes 88bd1e94
+ 0044e998 bytes 76242094
- 0042bb38 ["INT_ADD", "register:40f0:8", ["const:42bb38:8", "const:4:8"]]
- 0042bb38 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044e9d0 ["INT_ADD", "register:40f0:8", ["const:44e9d0:8", "const:4:8"]]
+ 0044e9d0 ["CALL", null, ["callee:00c57b70:8"]]
- 0042bb38 bytes 7abd1e94
+ 0044e9d0 bytes 68242094
- 0042bac8 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044e960 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042bac8 bytes 09f4fff0
+ 0044e960 bytes 89f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b8047a13aa9419c250d330d56e86ca8"></a>

### [`0042bc18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bc18.md) → [`0044eab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044eab0.md) FUN_0044eab0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ead8",
      "incomplete_value": true,
      "site": "0044eae8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bc40",
      "incomplete_value": true,
      "site": "0042bc50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044eaec",
      "incomplete_value": true,
      "site": "0044eaec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042bc54",
      "incomplete_value": true,
      "site": "0042bc54",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044eaf8",
      "incomplete_value": false,
      "site": "0044eb00",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bc60",
      "incomplete_value": false,
      "site": "0042bc68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044ead8",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044eae0",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044eaf8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ead8",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044eae0",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044eaf8",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042bc68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bc18.md#insn-0042bc68) · [`0042bca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bc18.md#insn-0042bca0) · [`0042bc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bc18.md#insn-0042bc30)
- 新版 [`0044eb00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044eab0.md#insn-0044eb00) · [`0044eb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044eab0.md#insn-0044eb38) · [`0044eac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044eab0.md#insn-0044eac8)

~~~diff
- 0042bc68 ["INT_ADD", "register:40f0:8", ["const:42bc68:8", "const:4:8"]]
- 0042bc68 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044eb00 ["INT_ADD", "register:40f0:8", ["const:44eb00:8", "const:4:8"]]
+ 0044eb00 ["CALL", null, ["callee:00c57b70:8"]]
- 0042bc68 bytes 2ebd1e94
+ 0044eb00 bytes 1c242094
- 0042bca0 ["INT_ADD", "register:40f0:8", ["const:42bca0:8", "const:4:8"]]
- 0042bca0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044eb38 ["INT_ADD", "register:40f0:8", ["const:44eb38:8", "const:4:8"]]
+ 0044eb38 ["CALL", null, ["callee:00c57b70:8"]]
- 0042bca0 bytes 20bd1e94
+ 0044eb38 bytes 0e242094
- 0042bc30 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044eac8 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042bc30 bytes 09f4fff0
+ 0044eac8 bytes 89f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-970d4134226eab52d3399d9869a9b460"></a>

### [`0042bd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bd30.md) → [`0044ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ebc8.md) FUN_0044ebc8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ebf0",
      "incomplete_value": true,
      "site": "0044ec00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bd58",
      "incomplete_value": true,
      "site": "0042bd68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044ec04",
      "incomplete_value": true,
      "site": "0044ec04",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042bd6c",
      "incomplete_value": true,
      "site": "0042bd6c",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ec10",
      "incomplete_value": false,
      "site": "0044ec18",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bd78",
      "incomplete_value": false,
      "site": "0042bd80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044ebf0",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044ebf8",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044ec10",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ebf0",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044ebf8",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044ec10",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042bd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bd30.md#insn-0042bd80) · [`0042bdb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bd30.md#insn-0042bdb8) · [`0042bd48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bd30.md#insn-0042bd48)
- 新版 [`0044ec18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ebc8.md#insn-0044ec18) · [`0044ec50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ebc8.md#insn-0044ec50) · [`0044ebe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ebc8.md#insn-0044ebe0)

~~~diff
- 0042bd80 ["INT_ADD", "register:40f0:8", ["const:42bd80:8", "const:4:8"]]
- 0042bd80 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044ec18 ["INT_ADD", "register:40f0:8", ["const:44ec18:8", "const:4:8"]]
+ 0044ec18 ["CALL", null, ["callee:00c57b70:8"]]
- 0042bd80 bytes e8bc1e94
+ 0044ec18 bytes d6232094
- 0042bdb8 ["INT_ADD", "register:40f0:8", ["const:42bdb8:8", "const:4:8"]]
- 0042bdb8 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044ec50 ["INT_ADD", "register:40f0:8", ["const:44ec50:8", "const:4:8"]]
+ 0044ec50 ["CALL", null, ["callee:00c57b70:8"]]
- 0042bdb8 bytes dabc1e94
+ 0044ec50 bytes c8232094
- 0042bd48 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044ebe0 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042bd48 bytes 09f4fff0
+ 0044ebe0 bytes 89f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f4b4d72055a933dc1b5942f356a5d0f"></a>

### [`0042be48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042be48.md) → [`0044ece0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ece0.md) FUN_0044ece0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00871a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871a6c.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`008a4c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4c0c.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ed08",
      "incomplete_value": true,
      "site": "0044ed18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042be70",
      "incomplete_value": true,
      "site": "0042be80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044ed1c",
      "incomplete_value": true,
      "site": "0044ed1c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042be84",
      "incomplete_value": true,
      "site": "0042be84",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ed28",
      "incomplete_value": false,
      "site": "0044ed30",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042be90",
      "incomplete_value": false,
      "site": "0042be98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044ed08",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044ed10",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044ed28",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ed08",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044ed10",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044ed28",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042be98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042be48.md#insn-0042be98) · [`0042bed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042be48.md#insn-0042bed0) · [`0042be60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042be48.md#insn-0042be60)
- 新版 [`0044ed30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ece0.md#insn-0044ed30) · [`0044ed68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ece0.md#insn-0044ed68) · [`0044ecf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ece0.md#insn-0044ecf8)

~~~diff
- 0042be98 ["INT_ADD", "register:40f0:8", ["const:42be98:8", "const:4:8"]]
- 0042be98 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044ed30 ["INT_ADD", "register:40f0:8", ["const:44ed30:8", "const:4:8"]]
+ 0044ed30 ["CALL", null, ["callee:00c57b70:8"]]
- 0042be98 bytes a2bc1e94
+ 0044ed30 bytes 90232094
- 0042bed0 ["INT_ADD", "register:40f0:8", ["const:42bed0:8", "const:4:8"]]
- 0042bed0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044ed68 ["INT_ADD", "register:40f0:8", ["const:44ed68:8", "const:4:8"]]
+ 0044ed68 ["CALL", null, ["callee:00c57b70:8"]]
- 0042bed0 bytes 94bc1e94
+ 0044ed68 bytes 82232094
- 0042be60 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044ecf8 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042be60 bytes 09f4fff0
+ 0044ecf8 bytes 89f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ac3036b06ef8bcf75a6ef2a045360c9"></a>

### [`0042bf64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bf64.md) → [`0044edfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044edfc.md) FUN_0044edfc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0075900c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/0075900c.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00783470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783470.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ee24",
      "incomplete_value": true,
      "site": "0044ee34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bf8c",
      "incomplete_value": true,
      "site": "0042bf9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044ee38",
      "incomplete_value": true,
      "site": "0044ee38",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042bfa0",
      "incomplete_value": true,
      "site": "0042bfa0",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ee44",
      "incomplete_value": false,
      "site": "0044ee4c",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042bfac",
      "incomplete_value": false,
      "site": "0042bfb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044ee24",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044ee2c",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044ee44",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ee24",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044ee2c",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044ee44",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042bfb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bf64.md#insn-0042bfb4) · [`0042bfec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bf64.md#insn-0042bfec) · [`0042bf7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bf64.md#insn-0042bf7c)
- 新版 [`0044ee4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044edfc.md#insn-0044ee4c) · [`0044ee84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044edfc.md#insn-0044ee84) · [`0044ee14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044edfc.md#insn-0044ee14)

~~~diff
- 0042bfb4 ["INT_ADD", "register:40f0:8", ["const:42bfb4:8", "const:4:8"]]
- 0042bfb4 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044ee4c ["INT_ADD", "register:40f0:8", ["const:44ee4c:8", "const:4:8"]]
+ 0044ee4c ["CALL", null, ["callee:00c57b70:8"]]
- 0042bfb4 bytes 5bbc1e94
+ 0044ee4c bytes 49232094
- 0042bfec ["INT_ADD", "register:40f0:8", ["const:42bfec:8", "const:4:8"]]
- 0042bfec ["CALL", null, ["callee:00c57b70:8"]]
+ 0044ee84 ["INT_ADD", "register:40f0:8", ["const:44ee84:8", "const:4:8"]]
+ 0044ee84 ["CALL", null, ["callee:00c57b70:8"]]
- 0042bfec bytes 4dbc1e94
+ 0044ee84 bytes 3b232094
- 0042bf7c ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044ee14 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042bf7c bytes 09f4fff0
+ 0044ee14 bytes 89f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5d8e1e72b47e9dac84b0a76dd303bef"></a>

### [`0042c07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c07c.md) → [`0044ef14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ef14.md) FUN_0044ef14

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`008746c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/008746c0.md) [`00874958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/00874958.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 3件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`008a7860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7860.md) [`008a7af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7af8.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ef40",
      "incomplete_value": true,
      "site": "0044ef54",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c0a8",
      "incomplete_value": true,
      "site": "0042c0bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044ef58",
      "incomplete_value": true,
      "site": "0044ef58",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042c0c0",
      "incomplete_value": true,
      "site": "0042c0c0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ef64",
      "incomplete_value": false,
      "site": "0044ef6c",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c0cc",
      "incomplete_value": false,
      "site": "0042c0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044ef40",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044ef4c",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044ef64",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ef40",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044ef4c",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044ef64",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042c0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c07c.md#insn-0042c0d4) · [`0042c10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c07c.md#insn-0042c10c) · [`0042c16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c07c.md#insn-0042c16c)
- 新版 [`0044ef6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ef14.md#insn-0044ef6c) · [`0044efa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ef14.md#insn-0044efa4) · [`0044f004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ef14.md#insn-0044f004)

~~~diff
- 0042c0d4 ["INT_ADD", "register:40f0:8", ["const:42c0d4:8", "const:4:8"]]
- 0042c0d4 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044ef6c ["INT_ADD", "register:40f0:8", ["const:44ef6c:8", "const:4:8"]]
+ 0044ef6c ["CALL", null, ["callee:00c57b70:8"]]
- 0042c0d4 bytes 13bc1e94
+ 0044ef6c bytes 01232094
- 0042c10c ["INT_ADD", "register:40f0:8", ["const:42c10c:8", "const:4:8"]]
- 0042c10c ["CALL", null, ["callee:00c57b70:8"]]
+ 0044efa4 ["INT_ADD", "register:40f0:8", ["const:44efa4:8", "const:4:8"]]
+ 0044efa4 ["CALL", null, ["callee:00c57b70:8"]]
- 0042c10c bytes 05bc1e94
+ 0044efa4 bytes f3222094
- 0042c16c ["INT_ADD", "register:40f0:8", ["const:42c16c:8", "const:4:8"]]
- 0042c16c ["CALL", null, ["callee:00c57b70:8"]]
+ 0044f004 ["INT_ADD", "register:40f0:8", ["const:44f004:8", "const:4:8"]]
+ 0044f004 ["CALL", null, ["callee:00c57b70:8"]]
- 0042c16c bytes edbb1e94
+ 0044f004 bytes db222094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-551ab159355315ce1d98aa404de04b72"></a>

### [`0042c288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c288.md) → [`0044f120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f120.md) FUN_0044f120

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044f148",
      "incomplete_value": true,
      "site": "0044f158",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c2b0",
      "incomplete_value": true,
      "site": "0042c2c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044f15c",
      "incomplete_value": true,
      "site": "0044f15c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042c2c4",
      "incomplete_value": true,
      "site": "0042c2c4",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f168",
      "incomplete_value": false,
      "site": "0044f170",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c2d0",
      "incomplete_value": false,
      "site": "0042c2d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044f148",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044f150",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044f168",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f148",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044f150",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044f168",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042c2d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c288.md#insn-0042c2d8) · [`0042c310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c288.md#insn-0042c310) · [`0042c2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c288.md#insn-0042c2a0)
- 新版 [`0044f170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f120.md#insn-0044f170) · [`0044f1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f120.md#insn-0044f1a8) · [`0044f138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f120.md#insn-0044f138)

~~~diff
- 0042c2d8 ["INT_ADD", "register:40f0:8", ["const:42c2d8:8", "const:4:8"]]
- 0042c2d8 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044f170 ["INT_ADD", "register:40f0:8", ["const:44f170:8", "const:4:8"]]
+ 0044f170 ["CALL", null, ["callee:00c57b70:8"]]
- 0042c2d8 bytes 92bb1e94
+ 0044f170 bytes 80222094
- 0042c310 ["INT_ADD", "register:40f0:8", ["const:42c310:8", "const:4:8"]]
- 0042c310 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044f1a8 ["INT_ADD", "register:40f0:8", ["const:44f1a8:8", "const:4:8"]]
+ 0044f1a8 ["CALL", null, ["callee:00c57b70:8"]]
- 0042c310 bytes 84bb1e94
+ 0044f1a8 bytes 72222094
- 0042c2a0 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044f138 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042c2a0 bytes 09f4ffd0
+ 0044f138 bytes 89f3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea7baf510f88cc37f842107beb1fbe0b"></a>

### [`0042c3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c3a0.md) → [`0044f238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f238.md) FUN_0044f238

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044f260",
      "incomplete_value": true,
      "site": "0044f270",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c3c8",
      "incomplete_value": true,
      "site": "0042c3d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044f274",
      "incomplete_value": true,
      "site": "0044f274",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042c3dc",
      "incomplete_value": true,
      "site": "0042c3dc",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f280",
      "incomplete_value": false,
      "site": "0044f288",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c3e8",
      "incomplete_value": false,
      "site": "0042c3f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5f9:8"
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
      "0044f260",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044f268",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044f280",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f260",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044f268",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044f280",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042c3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c3a0.md#insn-0042c3f0) · [`0042c428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c3a0.md#insn-0042c428) · [`0042c3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c3a0.md#insn-0042c3b8)
- 新版 [`0044f288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f238.md#insn-0044f288) · [`0044f2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f238.md#insn-0044f2c0) · [`0044f250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f238.md#insn-0044f250)

~~~diff
- 0042c3f0 ["INT_ADD", "register:40f0:8", ["const:42c3f0:8", "const:4:8"]]
- 0042c3f0 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044f288 ["INT_ADD", "register:40f0:8", ["const:44f288:8", "const:4:8"]]
+ 0044f288 ["CALL", null, ["callee:00c57b70:8"]]
- 0042c3f0 bytes 4cbb1e94
+ 0044f288 bytes 3a222094
- 0042c428 ["INT_ADD", "register:40f0:8", ["const:42c428:8", "const:4:8"]]
- 0042c428 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044f2c0 ["INT_ADD", "register:40f0:8", ["const:44f2c0:8", "const:4:8"]]
+ 0044f2c0 ["CALL", null, ["callee:00c57b70:8"]]
- 0042c428 bytes 3ebb1e94
+ 0044f2c0 bytes 2c222094
- 0042c3b8 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044f250 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0042c3b8 bytes 09f4ffd0
+ 0044f250 bytes 89f3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ecd3a0ac9c94e9d246c565c61ef8f97"></a>

### [`0042c4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c4b8.md) → [`0044f350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f350.md) FUN_0044f350

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008446e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008446e4.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)
- 新版 呼出元 1件 [`008769d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769d0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)

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
      "definition_site": "0044f37c",
      "incomplete_value": false,
      "site": "0044f384",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c4e4",
      "incomplete_value": false,
      "site": "0042c4ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:227:8"
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
      "definition_site": "0044f38c",
      "incomplete_value": false,
      "site": "0044f398",
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
            "const:b85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c4f4",
      "incomplete_value": false,
      "site": "0042c500",
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
            "const:6a1:8"
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
      "0044f37c",
      "PARAM",
      [
        "storage",
        "0029b227",
        null,
        "string"
      ]
    ],
    [
      "0044f38c",
      "PARAM",
      [
        "storage",
        "002ae6a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f37c",
      "PARAM",
      [
        "storage",
        "002ab208",
        null,
        "string"
      ]
    ],
    [
      "0044f38c",
      "PARAM",
      [
        "storage",
        "002bfb85",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042c4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c4b8.md#insn-0042c4ec) · [`0042c500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c4b8.md#insn-0042c500) · [`0042c4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c4b8.md#insn-0042c4e0)
- 新版 [`0044f384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f350.md#insn-0044f384) · [`0044f398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f350.md#insn-0044f398) · [`0044f378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f350.md#insn-0044f378)

~~~diff
- 0042c4ec ["INT_ADD", "register:40f0:8", ["const:42c4ec:8", "const:4:8"]]
- 0042c4ec ["CALL", null, ["callee:00c57d90:8"]]
+ 0044f384 ["INT_ADD", "register:40f0:8", ["const:44f384:8", "const:4:8"]]
+ 0044f384 ["CALL", null, ["callee:00c57d90:8"]]
- 0042c4ec bytes 95bb1e94
+ 0044f384 bytes 83222094
- 0042c500 ["INT_ADD", "register:40f0:8", ["const:42c500:8", "const:4:8"]]
- 0042c500 ["CALL", null, ["callee:00c57cb0:8"]]
+ 0044f398 ["INT_ADD", "register:40f0:8", ["const:44f398:8", "const:4:8"]]
+ 0044f398 ["CALL", null, ["callee:00c57cb0:8"]]
- 0042c500 bytes 58bb1e94
+ 0044f398 bytes 46222094
- 0042c4e0 ["COPY", "register:4008:8", ["const:29b000:8"]]
+ 0044f378 ["COPY", "register:4008:8", ["const:2ab000:8"]]
- 0042c4e0 bytes 61f3fff0
+ 0044f378 bytes e1f2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d40700fe30f5f727e19732de7f6689e8"></a>

### [`0042c564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c564.md) → [`0044f3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f3fc.md) FUN_0044f3fc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008446e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008446e4.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)
- 新版 呼出元 1件 [`008769d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769d0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)

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
      "definition_site": "0044f428",
      "incomplete_value": false,
      "site": "0044f430",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c590",
      "incomplete_value": false,
      "site": "0042c598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:227:8"
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
      "definition_site": "0044f438",
      "incomplete_value": false,
      "site": "0044f444",
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
            "const:efe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c5a0",
      "incomplete_value": false,
      "site": "0042c5ac",
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
            "const:8da:8"
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
      "0044f428",
      "PARAM",
      [
        "storage",
        "0029b227",
        null,
        "string"
      ]
    ],
    [
      "0044f438",
      "PARAM",
      [
        "storage",
        "002af8da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f428",
      "PARAM",
      [
        "storage",
        "002ab208",
        null,
        "string"
      ]
    ],
    [
      "0044f438",
      "PARAM",
      [
        "storage",
        "002c0efe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042c598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c564.md#insn-0042c598) · [`0042c5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c564.md#insn-0042c5ac) · [`0042c58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c564.md#insn-0042c58c)
- 新版 [`0044f430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f3fc.md#insn-0044f430) · [`0044f444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f3fc.md#insn-0044f444) · [`0044f424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f3fc.md#insn-0044f424)

~~~diff
- 0042c598 ["INT_ADD", "register:40f0:8", ["const:42c598:8", "const:4:8"]]
- 0042c598 ["CALL", null, ["callee:00c57d90:8"]]
+ 0044f430 ["INT_ADD", "register:40f0:8", ["const:44f430:8", "const:4:8"]]
+ 0044f430 ["CALL", null, ["callee:00c57d90:8"]]
- 0042c598 bytes 6abb1e94
+ 0044f430 bytes 58222094
- 0042c5ac ["INT_ADD", "register:40f0:8", ["const:42c5ac:8", "const:4:8"]]
- 0042c5ac ["CALL", null, ["callee:00c57cb0:8"]]
+ 0044f444 ["INT_ADD", "register:40f0:8", ["const:44f444:8", "const:4:8"]]
+ 0044f444 ["CALL", null, ["callee:00c57cb0:8"]]
- 0042c5ac bytes 2dbb1e94
+ 0044f444 bytes 1b222094
- 0042c58c ["COPY", "register:4008:8", ["const:29b000:8"]]
+ 0044f424 ["COPY", "register:4008:8", ["const:2ab000:8"]]
- 0042c58c bytes 61f3fff0
+ 0044f424 bytes e1f2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a50058242ad9d68a8e23d5ef20f98f4"></a>

### [`0042c610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c610.md) → [`0044f4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f4a8.md) _INIT_10

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 80.54% / 新版 80.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 4件, `store_value` 8件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044f4e4",
      "incomplete_value": true,
      "site": "0044f500",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0042c64c",
      "incomplete_value": true,
      "site": "0042c668",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044f508",
      "incomplete_value": true,
      "site": "0044f524",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0042c670",
      "incomplete_value": true,
      "site": "0042c68c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044f528",
      "incomplete_value": true,
      "site": "0044f544",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0042c690",
      "incomplete_value": true,
      "site": "0042c6ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0044f4e4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0044f508",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0044f528",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f4e4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0044f508",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0044f528",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042c770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c610.md#insn-0042c770) · [`0042c848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c610.md#insn-0042c848) · [`0042c864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c610.md#insn-0042c864)
- 新版 [`0044f608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f4a8.md#insn-0044f608) · [`0044f6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f4a8.md#insn-0044f6fc)

~~~diff
- 0042c770 ["INT_ADD", "register:40f0:8", ["const:42c770:8", "const:4:8"]]
- 0042c770 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0044f608 ["INT_ADD", "register:40f0:8", ["const:44f608:8", "const:4:8"]]
+ 0044f608 ["CALL", null, ["callee:0043b7b8:8"]]
- 0042c770 bytes 52b1ff97
+ 0044f608 bytes 6cb0ff97
- 0042c848 ["INT_ADD", "register:40f0:8", ["const:42c848:8", "const:4:8"]]
- 0042c848 ["CALL", null, ["callee:00c57a30:8"]]
- 0042c848 bytes e6b91e94
- 0042c864 ["INT_ADD", "register:40f0:8", ["const:42c864:8", "const:4:8"]]
- 0042c864 ["CALL", null, ["callee:00c57a30:8"]]
+ 0044f6fc ["INT_ADD", "register:40f0:8", ["const:44f6fc:8", "const:4:8"]]
+ 0044f6fc ["CALL", null, ["callee:00c57a30:8"]]
- 0042c864 bytes dfb91e94
+ 0044f6fc bytes cd202094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7f5ea30aadbc39235f7c3dc5239ba3a"></a>

### [`0042c9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c9c0.md) → [`0044f858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f858.md) FUN_0044f858

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0083b3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b3f0.md) [`0083bad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083bad8.md) [`00873c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873c68.md) [`008740c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/008740c4.md) [`008742c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00874/008742c4.md) · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 6件 [`0086d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md) [`0086ddc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086ddc4.md) [`008a6e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a6/008a6e08.md) [`008a7264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7264.md) [`008a7464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7464.md) · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f884",
      "incomplete_value": false,
      "site": "0044f888",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c9ec",
      "incomplete_value": false,
      "site": "0042c9f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:be0:8"
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
      "definition_site": "0044f894",
      "incomplete_value": false,
      "site": "0044f898",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c9fc",
      "incomplete_value": false,
      "site": "0042ca00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0044f874",
      "incomplete_value": true,
      "site": "0044f87c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:698:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042c9dc",
      "incomplete_value": true,
      "site": "0042c9e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:bd8:8"
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
      "0044f868",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "0044f874",
      "READ",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined8"
      ]
    ],
    [
      "0044f884",
      "PARAM",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044f868",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0044f874",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "0044f884",
      "PARAM",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042c9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c9c0.md#insn-0042c9f0) · [`0042ca00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c9c0.md#insn-0042ca00) · [`0042c9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c9c0.md#insn-0042c9c8)
- 新版 [`0044f888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f858.md#insn-0044f888) · [`0044f898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f858.md#insn-0044f898) · [`0044f860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f858.md#insn-0044f860)

~~~diff
- 0042c9f0 ["INT_ADD", "register:40f0:8", ["const:42c9f0:8", "const:4:8"]]
- 0042c9f0 ["CALL", null, ["callee:00c57a50:8"]]
+ 0044f888 ["INT_ADD", "register:40f0:8", ["const:44f888:8", "const:4:8"]]
+ 0044f888 ["CALL", null, ["callee:00c57a50:8"]]
- 0042c9f0 bytes 84b91e94
+ 0044f888 bytes 72202094
- 0042ca00 ["INT_ADD", "register:40f0:8", ["const:42ca00:8", "const:4:8"]]
- 0042ca00 ["CALL", null, ["callee:00c57a70:8"]]
+ 0044f898 ["INT_ADD", "register:40f0:8", ["const:44f898:8", "const:4:8"]]
+ 0044f898 ["CALL", null, ["callee:00c57a70:8"]]
- 0042ca00 bytes 88b91e94
+ 0044f898 bytes 76202094
- 0042c9c8 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0044f860 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 0042c9c8 bytes c83f0090
+ 0044f860 bytes a84200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54d6dfd28e2972fc4b896526b878b954"></a>

### [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) → [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) FUN_0044f8a0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 23件 [`004537f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md) [`00454af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454af4.md) [`00576eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576eec.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`00770bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770bfc.md) · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 23件 [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) [`005997c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`0079b0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b0d0.md) · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f8cc",
      "incomplete_value": false,
      "site": "0044f8d0",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ca34",
      "incomplete_value": false,
      "site": "0042ca38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:be0:8"
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
      "definition_site": "0044f8dc",
      "incomplete_value": false,
      "site": "0044f8e0",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ca44",
      "incomplete_value": false,
      "site": "0042ca48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0044f8bc",
      "incomplete_value": false,
      "site": "0044f8c4",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ca24",
      "incomplete_value": false,
      "site": "0042ca2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
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
      "0044f8b0",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "0044f8bc",
      "DATA",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined8"
      ]
    ],
    [
      "0044f8cc",
      "PARAM",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044f8b0",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0044f8bc",
      "DATA",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "0044f8cc",
      "PARAM",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042ca38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md#insn-0042ca38) · [`0042ca48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md#insn-0042ca48) · [`0042ca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md#insn-0042ca10)
- 新版 [`0044f8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md#insn-0044f8d0) · [`0044f8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md#insn-0044f8e0) · [`0044f8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md#insn-0044f8a8)

~~~diff
- 0042ca38 ["INT_ADD", "register:40f0:8", ["const:42ca38:8", "const:4:8"]]
- 0042ca38 ["CALL", null, ["callee:00c57a50:8"]]
+ 0044f8d0 ["INT_ADD", "register:40f0:8", ["const:44f8d0:8", "const:4:8"]]
+ 0044f8d0 ["CALL", null, ["callee:00c57a50:8"]]
- 0042ca38 bytes 72b91e94
+ 0044f8d0 bytes 60202094
- 0042ca48 ["INT_ADD", "register:40f0:8", ["const:42ca48:8", "const:4:8"]]
- 0042ca48 ["CALL", null, ["callee:00c57a70:8"]]
+ 0044f8e0 ["INT_ADD", "register:40f0:8", ["const:44f8e0:8", "const:4:8"]]
+ 0044f8e0 ["CALL", null, ["callee:00c57a70:8"]]
- 0042ca48 bytes 76b91e94
+ 0044f8e0 bytes 64202094
- 0042ca10 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0044f8a8 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 0042ca10 bytes c83f0090
+ 0044f8a8 bytes a84200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfdd99ba06cdd216c4deeedcb400161f"></a>

### [`0042ca70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca70.md) → [`0044f908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md) FUN_0044f908

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084177c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/0084177c.md) · 呼出先 10件 [`004289f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289f4.md) [`004370c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004370c8.md) [`0053ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00873a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873a68.md) · 呼出先 10件 [`0044b4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4f4.md) [`00459f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459f60.md) [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0044fa5c",
      "incomplete_value": false,
      "site": "0044fa5c",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042cbc4",
      "incomplete_value": false,
      "site": "0042cbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "definition_site": "0044f93c",
      "incomplete_value": false,
      "site": "0044f944",
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
            "const:e2a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042caa4",
      "incomplete_value": false,
      "site": "0042caac",
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
            "const:3fc:8"
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
      "definition_site": "0044f9a8",
      "incomplete_value": true,
      "site": "0044f9b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042cb10",
      "incomplete_value": true,
      "site": "0042cb18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
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
      "0044f93c",
      "PARAM",
      [
        "storage",
        "002a53fc",
        null,
        "string"
      ]
    ],
    [
      "0044f9a8",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "0044f9a8",
      "PARAM",
      [
        "storage",
        "00c25e10",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044f93c",
      "PARAM",
      [
        "storage",
        "002b5e2a",
        null,
        "string"
      ]
    ],
    [
      "0044f9a8",
      "READ",
      [
        "storage",
        "00c9a7c8",
        null,
        "pointer"
      ]
    ],
    [
      "0044f9a8",
      "PARAM",
      [
        "storage",
        "00ca58d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042caac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca70.md#insn-0042caac) · [`0042cb18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca70.md#insn-0042cb18) · [`0042ca9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca70.md#insn-0042ca9c)
- 新版 [`0044f944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md#insn-0044f944) · [`0044f9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md#insn-0044f9b0) · [`0044f934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md#insn-0044f934)

~~~diff
- 0042caac ["INT_ADD", "register:40f0:8", ["const:42caac:8", "const:4:8"]]
- 0042caac ["CALL", null, ["callee:00c57b70:8"]]
+ 0044f944 ["INT_ADD", "register:40f0:8", ["const:44f944:8", "const:4:8"]]
+ 0044f944 ["CALL", null, ["callee:00c57b70:8"]]
- 0042caac bytes 9db91e94
+ 0044f944 bytes 8b202094
- 0042cb18 ["INT_ADD", "register:40f0:8", ["const:42cb18:8", "const:4:8"]]
- 0042cb18 ["CALL", null, ["callee:00561cf4:8"]]
+ 0044f9b0 ["INT_ADD", "register:40f0:8", ["const:44f9b0:8", "const:4:8"]]
+ 0044f9b0 ["CALL", null, ["callee:00561cf4:8"]]
- 0042cb18 bytes d1480494
+ 0044f9b0 bytes d1480494
- 0042ca9c ["INT_ADD", "register:40f0:8", ["const:42ca9c:8", "const:4:8"]]
- 0042ca9c ["CALL", null, ["callee:0044b4f4:8"]]
+ 0044f934 ["INT_ADD", "register:40f0:8", ["const:44f934:8", "const:4:8"]]
+ 0044f934 ["CALL", null, ["callee:0044b4f4:8"]]
- 0042ca9c bytes d6efff97
+ 0044f934 bytes f0eeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6580c0c7bafe63b813239dcf832bb1b6"></a>

### [`0042ce34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ce34.md) → [`0044fccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fccc.md) FUN_0044fccc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 10件 [`004289f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289f4.md) [`00437890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437890.md) [`00437894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437894.md) [`0053ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 10件 [`0044b4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4f4.md) [`0045a728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a728.md) [`0045a72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a72c.md) [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0044fda0",
      "incomplete_value": false,
      "site": "0044fda0",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042cf08",
      "incomplete_value": false,
      "site": "0042cf08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "definition_site": "0044fcf8",
      "incomplete_value": false,
      "site": "0044fd00",
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
            "const:f2d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ce60",
      "incomplete_value": false,
      "site": "0042ce68",
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
            "const:909:8"
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
      "definition_site": "0044fd64",
      "incomplete_value": true,
      "site": "0044fd6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042cecc",
      "incomplete_value": true,
      "site": "0042ced4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
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
      "0044fcf8",
      "PARAM",
      [
        "storage",
        "002af909",
        null,
        "string"
      ]
    ],
    [
      "0044fd64",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "0044fd64",
      "PARAM",
      [
        "storage",
        "00c25e10",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044fcf8",
      "PARAM",
      [
        "storage",
        "002c0f2d",
        null,
        "string"
      ]
    ],
    [
      "0044fd64",
      "READ",
      [
        "storage",
        "00c9a7c8",
        null,
        "pointer"
      ]
    ],
    [
      "0044fd64",
      "PARAM",
      [
        "storage",
        "00ca58d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042ce68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ce34.md#insn-0042ce68) · [`0042ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ce34.md#insn-0042ced4) · [`0042ce58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ce34.md#insn-0042ce58)
- 新版 [`0044fd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fccc.md#insn-0044fd00) · [`0044fd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fccc.md#insn-0044fd6c) · [`0044fcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fccc.md#insn-0044fcf0)

~~~diff
- 0042ce68 ["INT_ADD", "register:40f0:8", ["const:42ce68:8", "const:4:8"]]
- 0042ce68 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044fd00 ["INT_ADD", "register:40f0:8", ["const:44fd00:8", "const:4:8"]]
+ 0044fd00 ["CALL", null, ["callee:00c57b70:8"]]
- 0042ce68 bytes aeb81e94
+ 0044fd00 bytes 9c1f2094
- 0042ced4 ["INT_ADD", "register:40f0:8", ["const:42ced4:8", "const:4:8"]]
- 0042ced4 ["CALL", null, ["callee:00561cf4:8"]]
+ 0044fd6c ["INT_ADD", "register:40f0:8", ["const:44fd6c:8", "const:4:8"]]
+ 0044fd6c ["CALL", null, ["callee:00561cf4:8"]]
- 0042ced4 bytes e2470494
+ 0044fd6c bytes e2470494
- 0042ce58 ["INT_ADD", "register:40f0:8", ["const:42ce58:8", "const:4:8"]]
- 0042ce58 ["CALL", null, ["callee:0044b4f4:8"]]
+ 0044fcf0 ["INT_ADD", "register:40f0:8", ["const:44fcf0:8", "const:4:8"]]
+ 0044fcf0 ["CALL", null, ["callee:0044b4f4:8"]]
- 0042ce58 bytes e7eeff97
+ 0044fcf0 bytes 01eeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5d4d2d21751a0927025cd389f8b1a7a"></a>

### [`0042d2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d2a8.md) → [`00450140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md) FUN_00450140

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0042d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d484.md) [`00442a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442a64.md) [`005891dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00589/005891dc.md) [`0058a2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058a/0058a2e0.md) · 呼出先 14件 [`0041b014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b014.md) [`00423a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423a40.md) [`00428620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428620.md) [`0052dd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd60.md) [`0053bda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bda8.md)
- 新版 呼出元 4件 [`0045031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md) [`004658fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md) [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) · 呼出先 14件 [`0043db14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db14.md) [`00446540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446540.md) [`0044b120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b120.md) [`00550bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf8.md) [`0055ec40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ec40.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 78.12% / 新版 78.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004501a8",
      "value": [
        "leaf",
        "ram:55ec48:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0042d310",
      "value": [
        "leaf",
        "ram:53bdb0:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045019c",
      "incomplete_value": false,
      "site": "004501a8",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042d304",
      "incomplete_value": false,
      "site": "0042d310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:c08:8"
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
      "definition_site": "0045020c",
      "incomplete_value": false,
      "site": "00450210",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042d374",
      "incomplete_value": false,
      "site": "0042d378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:c00:8"
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
      "00450170",
      "READ",
      [
        "storage",
        "00c24c00",
        null,
        "undefined1"
      ]
    ],
    [
      "00450180",
      "READ",
      [
        "storage",
        "00c24c18",
        null,
        "undefined1"
      ]
    ],
    [
      "0045019c",
      "PARAM",
      [
        "storage",
        "00c24c08",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00450170",
      "READ",
      [
        "storage",
        "00ca46c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00450180",
      "READ",
      [
        "storage",
        "00ca46d8",
        null,
        "undefined1"
      ]
    ],
    [
      "0045019c",
      "PARAM",
      [
        "storage",
        "00ca46c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042d310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d2a8.md#insn-0042d310) · [`0042d378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d2a8.md#insn-0042d378) · [`0042d3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d2a8.md#insn-0042d3a4)
- 新版 [`004501a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md#insn-004501a8) · [`00450210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md#insn-00450210) · [`0045023c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md#insn-0045023c)

~~~diff
- 0042d310 ["INT_ADD", "register:40f0:8", ["const:42d310:8", "const:4:8"]]
- 0042d310 ["CALL", null, ["ram:53bdb0:8"]]
+ 004501a8 ["INT_ADD", "register:40f0:8", ["const:4501a8:8", "const:4:8"]]
+ 004501a8 ["CALL", null, ["ram:55ec48:8"]]
- 0042d310 bytes a83a0494
+ 004501a8 bytes a83a0494
- 0042d378 ["INT_ADD", "register:40f0:8", ["const:42d378:8", "const:4:8"]]
- 0042d378 ["CALL", null, ["callee:00c57a50:8"]]
+ 00450210 ["INT_ADD", "register:40f0:8", ["const:450210:8", "const:4:8"]]
+ 00450210 ["CALL", null, ["callee:00c57a50:8"]]
- 0042d378 bytes 22b71e94
+ 00450210 bytes 101e2094
- 0042d3a4 ["INT_ADD", "register:40f0:8", ["const:42d3a4:8", "const:4:8"]]
- 0042d3a4 ["CALL", null, ["callee:00c57a30:8"]]
+ 0045023c ["INT_ADD", "register:40f0:8", ["const:45023c:8", "const:4:8"]]
+ 0045023c ["CALL", null, ["callee:00c57a30:8"]]
- 0042d3a4 bytes 0fb71e94
+ 0045023c bytes fd1d2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-381fa19106e0bb8d505ce35bdf7046a6"></a>

### [`0042d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d484.md) → [`0045031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md) FUN_0045031c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0042d878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d878.md) · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0042d2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d2a8.md) [`00574054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00450710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md) · 呼出先 9件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00450140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md) [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.54% / 新版 98.54%

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
      "definition_site": "004503b4",
      "incomplete_value": true,
      "site": "004503b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0042d51c",
      "incomplete_value": true,
      "site": "0042d51c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:674:8"
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
      "definition_site": "00450504",
      "incomplete_value": true,
      "site": "0045050c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042d66c",
      "incomplete_value": true,
      "site": "0042d674",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba0:8"
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
      "004503a4",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "00450504",
      "READ",
      [
        "storage",
        "002b2ba0",
        null,
        "undefined8"
      ]
    ],
    [
      "00450548",
      "READ",
      [
        "storage",
        "002b2990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004503a4",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "00450504",
      "READ",
      [
        "storage",
        "002c42b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00450548",
      "READ",
      [
        "storage",
        "002c4090",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042d4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d484.md#insn-0042d4d0) · [`0042d4dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d484.md#insn-0042d4dc) · [`0042d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d484.md#insn-0042d4f0)
- 新版 [`00450368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md#insn-00450368) · [`00450374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md#insn-00450374) · [`00450388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md#insn-00450388)

~~~diff
- 0042d4d0 ["INT_ADD", "register:40f0:8", ["const:42d4d0:8", "const:4:8"]]
- 0042d4d0 ["CALL", null, ["callee:00c538b0:8"]]
+ 00450368 ["INT_ADD", "register:40f0:8", ["const:450368:8", "const:4:8"]]
+ 00450368 ["CALL", null, ["callee:00c538b0:8"]]
- 0042d4d0 bytes 64a61e94
+ 00450368 bytes 520d2094
- 0042d4dc ["INT_ADD", "register:40f0:8", ["const:42d4dc:8", "const:4:8"]]
- 0042d4dc ["CALL", null, ["callee:00596eec:8"]]
+ 00450374 ["INT_ADD", "register:40f0:8", ["const:450374:8", "const:4:8"]]
+ 00450374 ["CALL", null, ["callee:00596eec:8"]]
- 0042d4dc bytes de1a0594
+ 00450374 bytes de1a0594
- 0042d4f0 ["INT_ADD", "register:40f0:8", ["const:42d4f0:8", "const:4:8"]]
- 0042d4f0 ["CALL", null, ["callee:00c538e0:8"]]
+ 00450388 ["INT_ADD", "register:40f0:8", ["const:450388:8", "const:4:8"]]
+ 00450388 ["CALL", null, ["callee:00c538e0:8"]]
- 0042d4f0 bytes 68a61e94
+ 00450388 bytes 560d2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d83285de17d7371c3c3d71dc7501c1e"></a>

### [`0042d878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d878.md) → [`00450710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md) FUN_00450710

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00437c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437c94.md) [`00442a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442a64.md) [`005891dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00589/005891dc.md) [`0058a2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058a/0058a2e0.md) [`0068d810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d810.md) · 呼出先 3件 [`0042d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d484.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 4件 [`0045ab2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045ab2c.md) [`004658fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md) [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) · 呼出先 3件 [`0045031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
      "definition_site": "00450734",
      "incomplete_value": true,
      "site": "00450754",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e36:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042d89c",
      "incomplete_value": true,
      "site": "0042d8bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8f4:8"
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
      "00450734",
      "READ",
      [
        "storage",
        "002908f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00450734",
      "READ",
      [
        "storage",
        "0029fe36",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042d890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d878.md#insn-0042d890) · [`0042d894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d878.md#insn-0042d894) · [`0042d8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d878.md#insn-0042d8d4)
- 新版 [`00450728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md#insn-00450728) · [`0045072c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md#insn-0045072c) · [`0045076c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md#insn-0045076c)

~~~diff
- 0042d890 ["COPY", "register:4050:8", ["const:290000:8"]]
+ 00450728 ["COPY", "register:4050:8", ["const:29f000:8"]]
- 0042d890 bytes 0af3fff0
+ 00450728 bytes 6af2fff0
- 0042d894 ["COPY", "tmp:0:8", ["const:8f4:8"]]
- 0042d894 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0042d894 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0042d894 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045072c ["COPY", "tmp:0:8", ["const:e36:8"]]
+ 0045072c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045072c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045072c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0042d894 bytes 4ad12391
+ 0045072c bytes 4ad93891
- 0042d8d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0042d8d4 ["INT_ADD", "register:40f0:8", ["const:42d8d4:8", "const:4:8"]]
- 0042d8d4 ["CALLIND", null, ["register:0:8"]]
+ 0045076c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045076c ["INT_ADD", "register:40f0:8", ["const:45076c:8", "const:4:8"]]
+ 0045076c ["CALLIND", null, ["register:0:8"]]
- 0042d8d4 bytes 20013fd6
+ 0045076c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8fe5f9039df8b309398a23c645c99e6"></a>

### [`0042d974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d974.md) → [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) FUN_0045080c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`0042f000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f000.md) [`0042f610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`004303e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/004303e0.md) [`00430dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430dd8.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 5件 [`00451e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md) [`004524a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`00453278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md) [`00453c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453c70.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004508bc",
      "incomplete_value": true,
      "site": "004508d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042da24",
      "incomplete_value": true,
      "site": "0042da38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "004508bc",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "004508bc",
      "PARAM",
      [
        "storage",
        "00c25e28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004508bc",
      "READ",
      [
        "storage",
        "00c9a808",
        null,
        "pointer"
      ]
    ],
    [
      "004508bc",
      "PARAM",
      [
        "storage",
        "00ca58e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042da38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d974.md#insn-0042da38) · [`0042d9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d974.md#insn-0042d9d4) · [`0042da0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d974.md#insn-0042da0c)
- 新版 [`004508d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md#insn-004508d0) · [`0045086c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md#insn-0045086c) · [`004508a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md#insn-004508a4)

~~~diff
- 0042da38 ["INT_ADD", "register:40f0:8", ["const:42da38:8", "const:4:8"]]
- 0042da38 ["CALL", null, ["callee:00450970:8"]]
+ 004508d0 ["INT_ADD", "register:40f0:8", ["const:4508d0:8", "const:4:8"]]
+ 004508d0 ["CALL", null, ["callee:00450970:8"]]
- 0042da38 bytes 28000094
+ 004508d0 bytes 28000094
- 0042d9d4 ["INT_ADD", "register:40f0:8", ["const:42d9d4:8", "const:4:8"]]
- 0042d9d4 ["CALL", null, ["callee:0043bae0:8"]]
+ 0045086c ["INT_ADD", "register:40f0:8", ["const:45086c:8", "const:4:8"]]
+ 0045086c ["CALL", null, ["callee:0043bae0:8"]]
- 0042d9d4 bytes 83adff97
+ 0045086c bytes 9dacff97
- 0042da0c ["INT_ADD", "register:40f0:8", ["const:42da0c:8", "const:4:8"]]
- 0042da0c ["CALL", null, ["callee:0043bae0:8"]]
+ 004508a4 ["INT_ADD", "register:40f0:8", ["const:4508a4:8", "const:4:8"]]
+ 004508a4 ["CALL", null, ["callee:0043bae0:8"]]
- 0042da0c bytes 75adff97
+ 004508a4 bytes 8facff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3700bf275d0463e57b7b5c3b0139351"></a>

### [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) → [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) FUN_00450970

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 11件 [`0042d974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d974.md) [`0043196c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/0043196c.md) [`00431e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431e50.md) [`00432420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432420.md) [`00432904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432904.md) · 呼出先 28件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042d084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d084.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md)
- 新版 呼出元 11件 [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) [`00454804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454804.md) [`00454ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md) [`004552b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/004552b8.md) [`0045579c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md) · 呼出先 28件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044ff1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044ff1c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.65% / 新版 91.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 19件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00450ad8",
      "incomplete_value": true,
      "site": "00450ae0",
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
      "definition_site": "0042dc40",
      "incomplete_value": true,
      "site": "0042dc48",
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00450ae8",
      "incomplete_value": true,
      "site": "00450ae8",
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
                "const:180:8"
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
      "definition_site": "0042dc50",
      "incomplete_value": true,
      "site": "0042dc50",
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
                "const:180:8"
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
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00450ae8",
      "incomplete_value": true,
      "site": "00450ae8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042dc50",
      "incomplete_value": true,
      "site": "0042dc50",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 26,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00450ad4",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ],
    [
      "00450ad8",
      "READ",
      [
        "storage",
        "00c13340",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00450adc",
      "READ",
      [
        "storage",
        "00c13380",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "00450ad4",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "00450ad8",
      "READ",
      [
        "storage",
        "00c92ce8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00450adc",
      "READ",
      [
        "storage",
        "00c92d28",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042dd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md#insn-0042dd5c) · [`0042dd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md#insn-0042dd98) · [`0042df20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md#insn-0042df20)
- 新版 [`00450bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md#insn-00450bf4) · [`00450c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md#insn-00450c30) · [`00450db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md#insn-00450db8)

~~~diff
- 0042dd5c ["INT_ADD", "register:40f0:8", ["const:42dd5c:8", "const:4:8"]]
- 0042dd5c ["CALL", null, ["callee:00c57cb0:8"]]
+ 00450bf4 ["INT_ADD", "register:40f0:8", ["const:450bf4:8", "const:4:8"]]
+ 00450bf4 ["CALL", null, ["callee:00c57cb0:8"]]
- 0042dd5c bytes 41b51e94
+ 00450bf4 bytes 2f1c2094
- 0042dd98 ["INT_ADD", "register:40f0:8", ["const:42dd98:8", "const:4:8"]]
- 0042dd98 ["CALL", null, ["callee:00c57cb0:8"]]
+ 00450c30 ["INT_ADD", "register:40f0:8", ["const:450c30:8", "const:4:8"]]
+ 00450c30 ["CALL", null, ["callee:00c57cb0:8"]]
- 0042dd98 bytes 32b51e94
+ 00450c30 bytes 201c2094
- 0042df20 ["INT_ADD", "register:40f0:8", ["const:42df20:8", "const:4:8"]]
- 0042df20 ["CALL", null, ["callee:00c57cb0:8"]]
+ 00450db8 ["INT_ADD", "register:40f0:8", ["const:450db8:8", "const:4:8"]]
+ 00450db8 ["CALL", null, ["callee:00c57cb0:8"]]
- 0042df20 bytes d0b41e94
+ 00450db8 bytes be1b2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d2c7d5ac766fbc39a4cfdf34fc58e3e"></a>

### [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) → [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) FUN_0045175c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 16件 [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`0042f000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f000.md) [`0042f610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`004303e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/004303e0.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00435e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435e50.md) [`00436518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436518.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 27件 [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00451e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md) [`004524a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`00453278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00458ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ce8.md) [`004593b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004517a8",
      "incomplete_value": false,
      "site": "004517ac",
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
    "old": {
      "definition_site": "0042e910",
      "incomplete_value": false,
      "site": "0042e914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "004517ac",
      "DATA",
      [
        "storage",
        "00be67a0",
        null,
        "pointer"
      ]
    ],
    [
      "004517f8",
      "READ",
      [
        "storage",
        "00be67a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004517ac",
      "DATA",
      [
        "storage",
        "00c63360",
        null,
        "pointer"
      ]
    ],
    [
      "004517f8",
      "READ",
      [
        "storage",
        "00c63368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042e8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md#insn-0042e8f8) · [`0042e90c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md#insn-0042e90c) · [`0042e910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md#insn-0042e910)
- 新版 [`00451790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md#insn-00451790) · [`004517a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md#insn-004517a4) · [`004517a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md#insn-004517a8)

~~~diff
- 0042e8f8 ["INT_ADD", "register:40f0:8", ["const:42e8f8:8", "const:4:8"]]
- 0042e8f8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00451790 ["INT_ADD", "register:40f0:8", ["const:451790:8", "const:4:8"]]
+ 00451790 ["CALL", null, ["callee:00c57a90:8"]]
- 0042e8f8 bytes d2b11e94
+ 00451790 bytes c0182094
- 0042e90c ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 004517a4 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0042e90c bytes c83d0090
+ 004517a4 bytes 884000d0
- 0042e910 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 0042e910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042e910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042e910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004517a8 ["COPY", "tmp:0:8", ["const:360:8"]]
+ 004517a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004517a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004517a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042e910 bytes 08811e91
+ 004517a8 bytes 08810d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8723a3a02bcb525cee1555b26c535272"></a>

### [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) → [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) FUN_00451870

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 15件 [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`00434024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434024.md) [`00434528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434528.md) [`004349a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/004349a0.md) [`004744e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004744e8.md) · 呼出先 2件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3a0.md)
- 新版 呼出元 15件 [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00456ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md) [`004573c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md) [`00457838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md) [`00497380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497380.md) · 呼出先 2件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57df0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004518b4",
      "incomplete_value": true,
      "site": "004518b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ea1c",
      "incomplete_value": true,
      "site": "0042ea1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "definition_site": "004518b8",
      "incomplete_value": true,
      "site": "004518b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "0042ea20",
      "incomplete_value": true,
      "site": "0042ea20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004518b0",
      "incomplete_value": true,
      "site": "004518c0",
      "value": [
        "LOAD",
        "8",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ea18",
      "incomplete_value": true,
      "site": "0042ea28",
      "value": [
        "LOAD",
        "8",
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
                "const:10:8"
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
      "00451894",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "004518a0",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ],
    [
      "004518b0",
      "READ",
      [
        "storage",
        "00c13350",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00451894",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "004518a0",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "004518b0",
      "READ",
      [
        "storage",
        "00c92cf8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042e9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md#insn-0042e9f0) · [`0042e9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md#insn-0042e9f4) · [`0042e9fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md#insn-0042e9fc)
- 新版 [`00451888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md#insn-00451888) · [`0045188c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md#insn-0045188c) · [`00451894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md#insn-00451894)

~~~diff
- 0042e9f0 ["COPY", "register:40b8:8", ["const:c1a000:8"]]
+ 00451888 ["COPY", "register:40b8:8", ["const:c9a000:8"]]
- 0042e9f0 bytes 773f0090
+ 00451888 bytes 574200b0
- 0042e9f4 ["COPY", "register:40b0:8", ["const:c1a000:8"]]
+ 0045188c ["COPY", "register:40b0:8", ["const:c9a000:8"]]
- 0042e9f4 bytes 763f0090
+ 0045188c bytes 564200b0
- 0042e9fc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:e28:8"]]
- 0042e9fc ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00451894 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:818:8"]]
+ 00451894 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 0042e9fc bytes f71647f9
+ 00451894 bytes f70e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40b441f62f6317aa550ebec15b20c8ff"></a>

### [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) → [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) FUN_00451998

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 13件 [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`00434024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434024.md) [`00434528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434528.md) [`004349a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/004349a0.md) · 呼出先 7件 [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 15件 [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`00456ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md) [`004573c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md) [`00457838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md) · 呼出先 7件 [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00451a44",
      "incomplete_value": false,
      "site": "00451a4c",
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
            "const:e4d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ebac",
      "incomplete_value": false,
      "site": "0042ebb4",
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
            "const:41f:8"
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
      "definition_site": "00451a90",
      "incomplete_value": false,
      "site": "00451a98",
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
            "const:e4d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ebf8",
      "incomplete_value": false,
      "site": "0042ec00",
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
            "const:41f:8"
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
      "definition_site": "00451b00",
      "incomplete_value": false,
      "site": "00451b08",
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
            "const:b9a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042ec68",
      "incomplete_value": false,
      "site": "0042ec70",
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
            "const:6b6:8"
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
      "00451a0c",
      "PARAM",
      [
        "storage",
        "0028f920",
        null,
        "string"
      ]
    ],
    [
      "00451a44",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00451a90",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00451a0c",
      "PARAM",
      [
        "storage",
        "0029ed60",
        null,
        "string"
      ]
    ],
    [
      "00451a44",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ],
    [
      "00451a90",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042ebb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md#insn-0042ebb4) · [`0042ec00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md#insn-0042ec00) · [`0042ec70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md#insn-0042ec70)
- 新版 [`00451a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md#insn-00451a4c) · [`00451a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md#insn-00451a98) · [`00451b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md#insn-00451b08)

~~~diff
- 0042ebb4 ["INT_ADD", "register:40f0:8", ["const:42ebb4:8", "const:4:8"]]
- 0042ebb4 ["CALL", null, ["callee:00459490:8"]]
+ 00451a4c ["INT_ADD", "register:40f0:8", ["const:451a4c:8", "const:4:8"]]
+ 00451a4c ["CALL", null, ["callee:00459490:8"]]
- 0042ebb4 bytes 911e0094
+ 00451a4c bytes 911e0094
- 0042ec00 ["INT_ADD", "register:40f0:8", ["const:42ec00:8", "const:4:8"]]
- 0042ec00 ["CALL", null, ["callee:00459490:8"]]
+ 00451a98 ["INT_ADD", "register:40f0:8", ["const:451a98:8", "const:4:8"]]
+ 00451a98 ["CALL", null, ["callee:00459490:8"]]
- 0042ec00 bytes 7e1e0094
+ 00451a98 bytes 7e1e0094
- 0042ec70 ["INT_ADD", "register:40f0:8", ["const:42ec70:8", "const:4:8"]]
- 0042ec70 ["CALL", null, ["callee:00459490:8"]]
+ 00451b08 ["INT_ADD", "register:40f0:8", ["const:451b08:8", "const:4:8"]]
+ 00451b08 ["CALL", null, ["callee:00459490:8"]]
- 0042ec70 bytes 621e0094
+ 00451b08 bytes 621e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04cae717db394e346d7ef7ed70ab08f3"></a>

### [`0042ee74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042ee74.md) → [`00451d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451d0c.md) FUN_00451d0c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md) [`00bdb370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb370.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md) [`00c57dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57dc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 65.62% / 新版 65.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00451d30",
      "incomplete_value": true,
      "site": "00451d38",
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
      "definition_site": "0042ee98",
      "incomplete_value": true,
      "site": "0042eea0",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00451d44",
      "incomplete_value": true,
      "site": "00451d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "definition_site": "0042eeac",
      "incomplete_value": true,
      "site": "0042eeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00451d44",
      "incomplete_value": true,
      "site": "00451d44",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0042eeac",
      "incomplete_value": true,
      "site": "0042eeac",
      "value": [
        "LOAD",
        "8",
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
      "00451d28",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ],
    [
      "00451d30",
      "READ",
      [
        "storage",
        "00c13340",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00451d34",
      "READ",
      [
        "storage",
        "00c13380",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "00451d28",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "00451d30",
      "READ",
      [
        "storage",
        "00c92ce8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00451d34",
      "READ",
      [
        "storage",
        "00c92d28",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042ee84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042ee74.md#insn-0042ee84) · [`0042ee88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042ee74.md#insn-0042ee88) · [`0042ee90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042ee74.md#insn-0042ee90)
- 新版 [`00451d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451d0c.md#insn-00451d1c) · [`00451d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451d0c.md#insn-00451d20) · [`00451d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451d0c.md#insn-00451d28)

~~~diff
- 0042ee84 ["COPY", "register:40a8:8", ["const:c1a000:8"]]
+ 00451d1c ["COPY", "register:40a8:8", ["const:c9a000:8"]]
- 0042ee84 bytes 753f0090
+ 00451d1c bytes 554200b0
- 0042ee88 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 00451d20 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 0042ee88 bytes 693f0090
+ 00451d20 bytes 494200b0
- 0042ee90 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e20:8"]]
- 0042ee90 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00451d28 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:810:8"]]
+ 00451d28 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 0042ee90 bytes b51247f9
+ 00451d28 bytes b50a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e6fd6c745fada0de00143ea37614a59"></a>

### [`0042f000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f000.md) → [`00451e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md) FUN_00451e98

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0084d6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d6d0.md) · 呼出先 16件 [`004288b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004288b4.md) [`0042d974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d974.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`00436954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436954.md) [`00438ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438ef4.md)
- 新版 呼出元 1件 [`00880668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md) · 呼出先 16件 [`0044b3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b3b4.md) [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`0045bd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd8c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.21% / 新版 93.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00451f20",
      "incomplete_value": false,
      "site": "00451f28",
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
    "old": {
      "definition_site": "0042f088",
      "incomplete_value": false,
      "site": "0042f090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "definition_site": "00451f48",
      "incomplete_value": false,
      "site": "00451f48",
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
    "old": {
      "definition_site": "0042f0b0",
      "incomplete_value": false,
      "site": "0042f0b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "00451f84",
      "incomplete_value": true,
      "site": "00451f84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0042f0ec",
      "incomplete_value": true,
      "site": "0042f0ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:91e:8"
              ]
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
      "00451ee0",
      "PARAM",
      [
        "storage",
        "002a73e3",
        null,
        "string"
      ]
    ],
    [
      "00451f28",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "00451f48",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00451ee0",
      "PARAM",
      [
        "storage",
        "002b7f52",
        null,
        "string"
      ]
    ],
    [
      "00451f28",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ],
    [
      "00451f48",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042f050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f000.md#insn-0042f050) · [`0042f040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f000.md#insn-0042f040) · [`0042f044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f000.md#insn-0042f044)
- 新版 [`00451ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md#insn-00451ee8) · [`00451ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md#insn-00451ed8) · [`00451edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md#insn-00451edc)

~~~diff
- 0042f050 ["INT_ADD", "register:40f0:8", ["const:42f050:8", "const:4:8"]]
- 0042f050 ["CALL", null, ["callee:00c57b70:8"]]
+ 00451ee8 ["INT_ADD", "register:40f0:8", ["const:451ee8:8", "const:4:8"]]
+ 00451ee8 ["CALL", null, ["callee:00c57b70:8"]]
- 0042f050 bytes 34b01e94
+ 00451ee8 bytes 22172094
- 0042f040 ["INT_ADD", "register:40f0:8", ["const:42f040:8", "const:4:8"]]
- 0042f040 ["CALL", null, ["callee:0044b3b4:8"]]
+ 00451ed8 ["INT_ADD", "register:40f0:8", ["const:451ed8:8", "const:4:8"]]
+ 00451ed8 ["CALL", null, ["callee:0044b3b4:8"]]
- 0042f040 bytes 1de6ff97
+ 00451ed8 bytes 37e5ff97
- 0042f044 ["COPY", "register:4008:8", ["const:2a7000:8"]]
+ 00451edc ["COPY", "register:4008:8", ["const:2b7000:8"]]
- 0042f044 bytes c1f3ff90
+ 00451edc bytes 21f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7046613e21c8ea95cbc77fb6daea92"></a>

### [`0042f610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md) → [`004524a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md) FUN_004524a8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0084d6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d6d0.md) · 呼出先 20件 [`004288b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004288b4.md) [`0042d974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d974.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`0042fcec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fcec.md) [`00438ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438ef4.md)
- 新版 呼出元 1件 [`00880668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md) · 呼出先 20件 [`0044b3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b3b4.md) [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00452b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452b84.md) [`0045bd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd8c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.31% / 新版 86.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 13件, `store_destination` 6件, `store_value` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045257c",
      "incomplete_value": true,
      "site": "0045257c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042f6e4",
      "incomplete_value": true,
      "site": "0042f6e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00452584",
      "incomplete_value": true,
      "site": "00452584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042f6ec",
      "incomplete_value": true,
      "site": "0042f6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00452594",
      "incomplete_value": true,
      "site": "00452594",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042f6fc",
      "incomplete_value": true,
      "site": "0042f6fc",
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
            "const:c70:8"
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
      "004524ec",
      "READ",
      [
        "storage",
        "00c24c48",
        null,
        "undefined1"
      ]
    ],
    [
      "004524fc",
      "READ",
      [
        "storage",
        "00c24c68",
        null,
        "undefined1"
      ]
    ],
    [
      "00452508",
      "PARAM",
      [
        "storage",
        "00c24c20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004524ec",
      "READ",
      [
        "storage",
        "00ca4708",
        null,
        "undefined1"
      ]
    ],
    [
      "004524fc",
      "READ",
      [
        "storage",
        "00ca4728",
        null,
        "undefined1"
      ]
    ],
    [
      "00452508",
      "PARAM",
      [
        "storage",
        "00ca46e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042f674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md#insn-0042f674) · [`0042f6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md#insn-0042f6c0) · [`0042f6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md#insn-0042f6e4)
- 新版 [`0045250c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md#insn-0045250c) · [`00452558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md#insn-00452558) · [`0045257c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md#insn-0045257c)

~~~diff
- 0042f674 ["INT_ADD", "register:40f0:8", ["const:42f674:8", "const:4:8"]]
- 0042f674 ["CALL", null, ["callee:00c57ce0:8"]]
+ 0045250c ["INT_ADD", "register:40f0:8", ["const:45250c:8", "const:4:8"]]
+ 0045250c ["CALL", null, ["callee:00c57ce0:8"]]
- 0042f674 bytes 07af1e94
+ 0045250c bytes f5152094
- 0042f6c0 ["INT_ADD", "register:40f0:8", ["const:42f6c0:8", "const:4:8"]]
- 0042f6c0 ["CALL", null, ["callee:0045ca58:8"]]
+ 00452558 ["INT_ADD", "register:40f0:8", ["const:452558:8", "const:4:8"]]
+ 00452558 ["CALL", null, ["callee:0045ca58:8"]]
- 0042f6c0 bytes 40290094
+ 00452558 bytes 40290094
- 0042f6e4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c58:8"]]
- 0042f6e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 0045257c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:718:8"]]
+ 0045257c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0042f6e4 bytes c02e06f9
+ 0045257c bytes c08e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd9cba584ca022e1378ba5d33b17618b"></a>

### [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) → [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) FUN_00452c14

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00437c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437c94.md) [`00576eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576eec.md) [`00770bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00770/00770bfc.md) [`0084dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md) [`00873c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00873/00873c68.md) · 呼出先 24件 [`004288b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004288b4.md) [`0042d974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d974.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`00430300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430300.md) [`00436bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436bf8.md)
- 新版 呼出元 5件 [`0045ab2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045ab2c.md) [`005997c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md) [`0079b0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b0d0.md) [`00880cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md) [`008a6e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a6/008a6e08.md) · 呼出先 24件 [`0044b3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b3b4.md) [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00453198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453198.md) [`00459a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459a90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.78% / 新版 82.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 13件, `store_destination` 6件, `store_value` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00452ce8",
      "incomplete_value": true,
      "site": "00452ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042fe50",
      "incomplete_value": true,
      "site": "0042fe50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00452cf0",
      "incomplete_value": true,
      "site": "00452cf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042fe58",
      "incomplete_value": true,
      "site": "0042fe58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00452d00",
      "incomplete_value": true,
      "site": "00452d00",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042fe68",
      "incomplete_value": true,
      "site": "0042fe68",
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
            "const:cc8:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00452c58",
      "READ",
      [
        "storage",
        "00c24ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00452c68",
      "READ",
      [
        "storage",
        "00c24cc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00452c74",
      "PARAM",
      [
        "storage",
        "00c24c74",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00452c58",
      "READ",
      [
        "storage",
        "00ca4760",
        null,
        "undefined1"
      ]
    ],
    [
      "00452c68",
      "READ",
      [
        "storage",
        "00ca4780",
        null,
        "undefined1"
      ]
    ],
    [
      "00452c74",
      "PARAM",
      [
        "storage",
        "00ca4734",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042fde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md#insn-0042fde0) · [`0042fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md#insn-0042fe2c) · [`0042fe50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md#insn-0042fe50)
- 新版 [`00452c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md#insn-00452c78) · [`00452cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md#insn-00452cc4) · [`00452ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md#insn-00452ce8)

~~~diff
- 0042fde0 ["INT_ADD", "register:40f0:8", ["const:42fde0:8", "const:4:8"]]
- 0042fde0 ["CALL", null, ["callee:00c57ce0:8"]]
+ 00452c78 ["INT_ADD", "register:40f0:8", ["const:452c78:8", "const:4:8"]]
+ 00452c78 ["CALL", null, ["callee:00c57ce0:8"]]
- 0042fde0 bytes 2cad1e94
+ 00452c78 bytes 1a142094
- 0042fe2c ["INT_ADD", "register:40f0:8", ["const:42fe2c:8", "const:4:8"]]
- 0042fe2c ["CALL", null, ["callee:0045db38:8"]]
+ 00452cc4 ["INT_ADD", "register:40f0:8", ["const:452cc4:8", "const:4:8"]]
+ 00452cc4 ["CALL", null, ["callee:0045db38:8"]]
- 0042fe2c bytes 9d2b0094
+ 00452cc4 bytes 9d2b0094
- 0042fe50 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:cb0:8"]]
- 0042fe50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00452ce8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:770:8"]]
+ 00452ce8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0042fe50 bytes 005b06f9
+ 00452ce8 bytes 00bb03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc88e5eeb7ff8df8deb8ee96b47b76f3"></a>

### [`004303e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/004303e0.md) → [`00453278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md) FUN_00453278

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00430b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430b04.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00428904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428904.md) [`0042d974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d974.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`00436954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436954.md)
- 新版 呼出元 1件 [`0045399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md) · 呼出先 16件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b404.md) [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.22% / 新版 93.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00453318",
      "incomplete_value": false,
      "site": "00453320",
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
    "old": {
      "definition_site": "00430480",
      "incomplete_value": false,
      "site": "00430488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "definition_site": "0045332c",
      "incomplete_value": false,
      "site": "0045332c",
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
    "old": {
      "definition_site": "00430494",
      "incomplete_value": false,
      "site": "00430494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "004533d0",
      "incomplete_value": true,
      "site": "004533e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8db:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00430538",
      "incomplete_value": true,
      "site": "00430548",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:201:8"
              ]
            ]
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
      "004532cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00428904"
      ]
    ],
    [
      "004532d4",
      "PARAM",
      [
        "storage",
        "002af926",
        null,
        "string"
      ]
    ],
    [
      "00453320",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004532cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b404"
      ]
    ],
    [
      "004532d4",
      "PARAM",
      [
        "storage",
        "002c0f4a",
        null,
        "string"
      ]
    ],
    [
      "00453320",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00430434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/004303e0.md#insn-00430434) · [`00430444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/004303e0.md#insn-00430444) · [`00430438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/004303e0.md#insn-00430438)
- 新版 [`004532cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md#insn-004532cc) · [`004532dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md#insn-004532dc) · [`004532d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md#insn-004532d0)

~~~diff
- 00430434 ["INT_ADD", "register:40f0:8", ["const:430434:8", "const:4:8"]]
- 00430434 ["CALL", null, ["ram:428904:8"]]
+ 004532cc ["INT_ADD", "register:40f0:8", ["const:4532cc:8", "const:4:8"]]
+ 004532cc ["CALL", null, ["ram:44b404:8"]]
- 00430434 bytes 34e1ff97
+ 004532cc bytes 4ee0ff97
- 00430444 ["INT_ADD", "register:40f0:8", ["const:430444:8", "const:4:8"]]
- 00430444 ["CALL", null, ["callee:00c57b70:8"]]
+ 004532dc ["INT_ADD", "register:40f0:8", ["const:4532dc:8", "const:4:8"]]
+ 004532dc ["CALL", null, ["callee:00c57b70:8"]]
- 00430444 bytes 37ab1e94
+ 004532dc bytes 25122094
- 00430438 ["COPY", "register:4008:8", ["const:2af000:8"]]
+ 004532d0 ["COPY", "register:4008:8", ["const:2c0000:8"]]
- 00430438 bytes e1f3fff0
+ 004532d0 bytes 61f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a16c9990221dc84eef6508b4f0596fe"></a>

### [`00430b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430b04.md) → [`0045399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md) FUN_0045399c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`004537f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md) [`00454af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454af4.md) · 呼出先 12件 [`004303e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/004303e0.md) [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`0043bf84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bf84.md) [`0043cb64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cb64.md) [`0043cbb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cbb4.md)
- 新版 呼出元 2件 [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) · 呼出先 12件 [`00453278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md) [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`0045ee1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045ee1c.md) [`0045f9fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f9fc.md) [`0045fa4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fa4c.md)

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
      "definition_site": "004539f4",
      "incomplete_value": false,
      "site": "00453a04",
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
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00430b5c",
      "incomplete_value": false,
      "site": "00430b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "definition_site": "00453a28",
      "incomplete_value": false,
      "site": "00453a30",
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
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00430b90",
      "incomplete_value": false,
      "site": "00430b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "definition_site": "00453a9c",
      "incomplete_value": false,
      "site": "00453a9c",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00430c04",
      "incomplete_value": false,
      "site": "00430c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00453a04",
      "DATA",
      [
        "storage",
        "00be6eb0",
        null,
        "pointer"
      ]
    ],
    [
      "00453a30",
      "DATA",
      [
        "storage",
        "00be6f00",
        null,
        "undefined *"
      ]
    ],
    [
      "00453a9c",
      "DATA",
      [
        "storage",
        "00be7058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00453a04",
      "DATA",
      [
        "storage",
        "00c63a70",
        null,
        "pointer"
      ]
    ],
    [
      "00453a30",
      "DATA",
      [
        "storage",
        "00c63ac0",
        null,
        "undefined *"
      ]
    ],
    [
      "00453a9c",
      "DATA",
      [
        "storage",
        "00c63c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00430b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430b04.md#insn-00430b50) · [`00430b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430b04.md#insn-00430b58) · [`00430b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430b04.md#insn-00430b5c)
- 新版 [`004539e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md#insn-004539e8) · [`004539f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md#insn-004539f0) · [`004539f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md#insn-004539f4)

~~~diff
- 00430b50 ["INT_ADD", "register:40f0:8", ["const:430b50:8", "const:4:8"]]
- 00430b50 ["CALL", null, ["callee:00c57a90:8"]]
+ 004539e8 ["INT_ADD", "register:40f0:8", ["const:4539e8:8", "const:4:8"]]
+ 004539e8 ["CALL", null, ["callee:00c57a90:8"]]
- 00430b50 bytes 3ca91e94
+ 004539e8 bytes 2a102094
- 00430b58 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 004539f0 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00430b58 bytes a83d00d0
+ 004539f0 bytes 88400090
- 00430b5c ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 00430b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00430b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00430b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004539f4 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 004539f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004539f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004539f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00430b5c bytes 08c13a91
+ 004539f4 bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4052e0a6033fa8bac8b8e8658daa6c8e"></a>

### [`00430dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430dd8.md) → [`00453c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453c70.md) FUN_00453c70

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00841c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00428954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428954.md) [`0042d974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d974.md) [`00436954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436954.md) [`00438ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438ef4.md)
- 新版 呼出元 1件 [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b454.md) [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`0045bd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd8c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.77% / 新版 94.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00453d04",
      "incomplete_value": false,
      "site": "00453d0c",
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
    "old": {
      "definition_site": "00430e6c",
      "incomplete_value": false,
      "site": "00430e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "definition_site": "00453d20",
      "incomplete_value": false,
      "site": "00453d20",
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
    "old": {
      "definition_site": "00430e88",
      "incomplete_value": false,
      "site": "00430e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "00453e54",
      "incomplete_value": true,
      "site": "00453e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00430fbc",
      "incomplete_value": true,
      "site": "00430fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "00453cbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00428954"
      ]
    ],
    [
      "00453cc4",
      "PARAM",
      [
        "storage",
        "0029c3a8",
        null,
        "string"
      ]
    ],
    [
      "00453d0c",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00453cbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b454"
      ]
    ],
    [
      "00453cc4",
      "PARAM",
      [
        "storage",
        "002ac5ce",
        null,
        "string"
      ]
    ],
    [
      "00453d0c",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00430e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430dd8.md#insn-00430e24) · [`00430e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430dd8.md#insn-00430e34) · [`00430e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430dd8.md#insn-00430e28)
- 新版 [`00453cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453c70.md#insn-00453cbc) · [`00453ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453c70.md#insn-00453ccc) · [`00453cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453c70.md#insn-00453cc0)

~~~diff
- 00430e24 ["INT_ADD", "register:40f0:8", ["const:430e24:8", "const:4:8"]]
- 00430e24 ["CALL", null, ["ram:428954:8"]]
+ 00453cbc ["INT_ADD", "register:40f0:8", ["const:453cbc:8", "const:4:8"]]
+ 00453cbc ["CALL", null, ["ram:44b454:8"]]
- 00430e24 bytes ccdeff97
+ 00453cbc bytes e6ddff97
- 00430e34 ["INT_ADD", "register:40f0:8", ["const:430e34:8", "const:4:8"]]
- 00430e34 ["CALL", null, ["callee:00c57b70:8"]]
+ 00453ccc ["INT_ADD", "register:40f0:8", ["const:453ccc:8", "const:4:8"]]
+ 00453ccc ["CALL", null, ["callee:00c57b70:8"]]
- 00430e34 bytes bba81e94
+ 00453ccc bytes a90f2094
- 00430e28 ["COPY", "register:4008:8", ["const:29c000:8"]]
+ 00453cc0 ["COPY", "register:4008:8", ["const:2ac000:8"]]
- 00430e28 bytes 61f3ff90
+ 00453cc0 bytes c1f2ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f22d3195320fb914dd14d3200e11b0a"></a>

### [`00431534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md) → [`004543cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md) FUN_004543cc

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0084e780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e780.md) · 呼出先 15件 [`004289f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289f4.md) [`0043d22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d22c.md) [`0043d230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d230.md) [`0053e18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e18c.md) [`0053e1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e1dc.md)
- 新版 呼出元 1件 [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) · 呼出先 15件 [`0044b4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4f4.md) [`004600c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600c4.md) [`004600c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600c8.md) [`00561024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md) [`00561074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.37% / 新版 93.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004544fc",
      "incomplete_value": true,
      "site": "0045450c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:28a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00431664",
      "incomplete_value": true,
      "site": "00431674",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:295000:8"
              ],
              [
                "leaf",
                "const:851:8"
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
      "definition_site": "00454500",
      "incomplete_value": true,
      "site": "00454510",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00431668",
      "incomplete_value": true,
      "site": "00431678",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00454504",
      "incomplete_value": true,
      "site": "00454514",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0043166c",
      "incomplete_value": true,
      "site": "0043167c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00454404",
      "PARAM",
      [
        "storage",
        "002a8124",
        null,
        "string"
      ]
    ],
    [
      "00454474",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "00454474",
      "PARAM",
      [
        "storage",
        "00c25e28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00454404",
      "PARAM",
      [
        "storage",
        "002b8dc6",
        null,
        "string"
      ]
    ],
    [
      "00454474",
      "READ",
      [
        "storage",
        "00c9a808",
        null,
        "pointer"
      ]
    ],
    [
      "00454474",
      "PARAM",
      [
        "storage",
        "00ca58e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00431574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md#insn-00431574) · [`004315e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md#insn-004315e4) · [`0043155c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md#insn-0043155c)
- 新版 [`0045440c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md#insn-0045440c) · [`0045447c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md#insn-0045447c) · [`004543f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md#insn-004543f4)

~~~diff
- 00431574 ["INT_ADD", "register:40f0:8", ["const:431574:8", "const:4:8"]]
- 00431574 ["CALL", null, ["callee:00c57b70:8"]]
+ 0045440c ["INT_ADD", "register:40f0:8", ["const:45440c:8", "const:4:8"]]
+ 0045440c ["CALL", null, ["callee:00c57b70:8"]]
- 00431574 bytes eba61e94
+ 0045440c bytes d90d2094
- 004315e4 ["INT_ADD", "register:40f0:8", ["const:4315e4:8", "const:4:8"]]
- 004315e4 ["CALL", null, ["callee:00561cf4:8"]]
+ 0045447c ["INT_ADD", "register:40f0:8", ["const:45447c:8", "const:4:8"]]
+ 0045447c ["CALL", null, ["callee:00561cf4:8"]]
- 004315e4 bytes 1e360494
+ 0045447c bytes 1e360494
- 0043155c ["INT_ADD", "register:40f0:8", ["const:43155c:8", "const:4:8"]]
- 0043155c ["CALL", null, ["callee:00752240:8"]]
+ 004543f4 ["INT_ADD", "register:40f0:8", ["const:4543f4:8", "const:4:8"]]
+ 004543f4 ["CALL", null, ["callee:00752240:8"]]
- 0043155c bytes cdda0b94
+ 004543f4 bytes 93f70b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceed175f62b0e1c96910dc944712170e"></a>

### [`0043196c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/0043196c.md) → [`00454804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454804.md) FUN_00454804

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00987b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/00987b70.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00428bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428bc0.md) [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`0043d868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d868.md) [`0043f32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f32c.md)
- 新版 呼出元 1件 [`009bd650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd650.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b6c0.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00460700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460700.md) [`004621c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004621c4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.79% / 新版 96.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00454944",
      "incomplete_value": false,
      "site": "00454944",
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
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00431aac",
      "incomplete_value": false,
      "site": "00431aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:258:8"
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
      "definition_site": "004549e4",
      "incomplete_value": false,
      "site": "004549e4",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00431b4c",
      "incomplete_value": false,
      "site": "00431b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045483c",
      "value": [
        "leaf",
        "ram:44b6c0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004319a4",
      "value": [
        "leaf",
        "ram:428bc0:8"
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
      "0045483c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00428bc0"
      ]
    ],
    [
      "00454844",
      "PARAM",
      [
        "storage",
        "002a931e",
        null,
        "string"
      ]
    ],
    [
      "00454944",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045483c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b6c0"
      ]
    ],
    [
      "00454844",
      "PARAM",
      [
        "storage",
        "002b9fc1",
        null,
        "string"
      ]
    ],
    [
      "00454944",
      "DATA",
      [
        "storage",
        "00c63e18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004319a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/0043196c.md#insn-004319a4) · [`004319b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/0043196c.md#insn-004319b4) · [`00431bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/0043196c.md#insn-00431bb0)
- 新版 [`0045483c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454804.md#insn-0045483c) · [`0045484c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454804.md#insn-0045484c) · [`00454a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454804.md#insn-00454a48)

~~~diff
- 004319a4 ["INT_ADD", "register:40f0:8", ["const:4319a4:8", "const:4:8"]]
- 004319a4 ["CALL", null, ["ram:428bc0:8"]]
+ 0045483c ["INT_ADD", "register:40f0:8", ["const:45483c:8", "const:4:8"]]
+ 0045483c ["CALL", null, ["ram:44b6c0:8"]]
- 004319a4 bytes 87dcff97
+ 0045483c bytes a1dbff97
- 004319b4 ["INT_ADD", "register:40f0:8", ["const:4319b4:8", "const:4:8"]]
- 004319b4 ["CALL", null, ["callee:00c57b70:8"]]
+ 0045484c ["INT_ADD", "register:40f0:8", ["const:45484c:8", "const:4:8"]]
+ 0045484c ["CALL", null, ["callee:00c57b70:8"]]
- 004319b4 bytes dba51e94
+ 0045484c bytes c90c2094
- 00431bb0 ["INT_ADD", "register:40f0:8", ["const:431bb0:8", "const:4:8"]]
- 00431bb0 ["CALL", null, ["callee:00450970:8"]]
+ 00454a48 ["INT_ADD", "register:40f0:8", ["const:454a48:8", "const:4:8"]]
+ 00454a48 ["CALL", null, ["callee:00450970:8"]]
- 00431bb0 bytes caefff97
+ 00454a48 bytes caefff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc8418c7b96b0562bcbeb3d94a56c058"></a>

### [`00431e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431e50.md) → [`00454ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md) FUN_00454ce8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00984ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/00984ce0.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00428bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428bc0.md) [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`0043f6bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f6bc.md) [`0043f97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f97c.md)
- 新版 呼出元 1件 [`009ba7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba7c0.md) · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b6c0.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00462554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462554.md) [`00462814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462814.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.48% / 新版 96.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00454ec0",
      "incomplete_value": false,
      "site": "00454ec0",
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
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00432028",
      "incomplete_value": false,
      "site": "00432028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00454f60",
      "incomplete_value": false,
      "site": "00454f60",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004320c8",
      "incomplete_value": false,
      "site": "004320c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00454d24",
      "value": [
        "leaf",
        "ram:44b6c0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00431e8c",
      "value": [
        "leaf",
        "ram:428bc0:8"
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
      "00454d24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00428bc0"
      ]
    ],
    [
      "00454d2c",
      "PARAM",
      [
        "storage",
        "0029d366",
        null,
        "string"
      ]
    ],
    [
      "00454d8c",
      "PARAM",
      [
        "storage",
        "0029457f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00454d24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b6c0"
      ]
    ],
    [
      "00454d2c",
      "PARAM",
      [
        "storage",
        "002ad5f0",
        null,
        "string"
      ]
    ],
    [
      "00454d8c",
      "PARAM",
      [
        "storage",
        "002a3e95",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00431e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431e50.md#insn-00431e8c) · [`00431e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431e50.md#insn-00431e9c) · [`00431efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431e50.md#insn-00431efc)
- 新版 [`00454d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md#insn-00454d24) · [`00454d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md#insn-00454d34) · [`00454d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md#insn-00454d94)

~~~diff
- 00431e8c ["INT_ADD", "register:40f0:8", ["const:431e8c:8", "const:4:8"]]
- 00431e8c ["CALL", null, ["ram:428bc0:8"]]
+ 00454d24 ["INT_ADD", "register:40f0:8", ["const:454d24:8", "const:4:8"]]
+ 00454d24 ["CALL", null, ["ram:44b6c0:8"]]
- 00431e8c bytes 4ddbff97
+ 00454d24 bytes 67daff97
- 00431e9c ["INT_ADD", "register:40f0:8", ["const:431e9c:8", "const:4:8"]]
- 00431e9c ["CALL", null, ["callee:00c57b70:8"]]
+ 00454d34 ["INT_ADD", "register:40f0:8", ["const:454d34:8", "const:4:8"]]
+ 00454d34 ["CALL", null, ["callee:00c57b70:8"]]
- 00431e9c bytes a1a41e94
+ 00454d34 bytes 8f0b2094
- 00431efc ["INT_ADD", "register:40f0:8", ["const:431efc:8", "const:4:8"]]
- 00431efc ["CALL", null, ["callee:00c57b70:8"]]
+ 00454d94 ["INT_ADD", "register:40f0:8", ["const:454d94:8", "const:4:8"]]
+ 00454d94 ["CALL", null, ["callee:00c57b70:8"]]
- 00431efc bytes 89a41e94
+ 00454d94 bytes 770b2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-193874a792949b6cf409ba49d9053825"></a>

### [`00432420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432420.md) → [`004552b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/004552b8.md) FUN_004552b8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) [`00a3c714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c714.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00428bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428bc0.md) [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`0043fc3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fc3c.md) [`004400b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/004400b8.md)
- 新版 呼出元 2件 [`00a8a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8a/00a8a220.md) [`00a9a608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a608.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b6c0.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00462ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462ad4.md) [`00462f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462f50.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.79% / 新版 96.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004553f8",
      "incomplete_value": false,
      "site": "004553f8",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00432560",
      "incomplete_value": false,
      "site": "00432560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "definition_site": "00455498",
      "incomplete_value": false,
      "site": "00455498",
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
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00432600",
      "incomplete_value": false,
      "site": "00432600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004552f0",
      "value": [
        "leaf",
        "ram:44b6c0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00432458",
      "value": [
        "leaf",
        "ram:428bc0:8"
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
      "004552f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00428bc0"
      ]
    ],
    [
      "004552f8",
      "PARAM",
      [
        "storage",
        "0029d374",
        null,
        "string"
      ]
    ],
    [
      "004553f8",
      "DATA",
      [
        "storage",
        "00be7458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004552f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b6c0"
      ]
    ],
    [
      "004552f8",
      "PARAM",
      [
        "storage",
        "002ad5fe",
        null,
        "string"
      ]
    ],
    [
      "004553f8",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00432458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432420.md#insn-00432458) · [`00432468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432420.md#insn-00432468) · [`00432664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432420.md#insn-00432664)
- 新版 [`004552f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/004552b8.md#insn-004552f0) · [`00455300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/004552b8.md#insn-00455300) · [`004554fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/004552b8.md#insn-004554fc)

~~~diff
- 00432458 ["INT_ADD", "register:40f0:8", ["const:432458:8", "const:4:8"]]
- 00432458 ["CALL", null, ["ram:428bc0:8"]]
+ 004552f0 ["INT_ADD", "register:40f0:8", ["const:4552f0:8", "const:4:8"]]
+ 004552f0 ["CALL", null, ["ram:44b6c0:8"]]
- 00432458 bytes dad9ff97
+ 004552f0 bytes f4d8ff97
- 00432468 ["INT_ADD", "register:40f0:8", ["const:432468:8", "const:4:8"]]
- 00432468 ["CALL", null, ["callee:00c57b70:8"]]
+ 00455300 ["INT_ADD", "register:40f0:8", ["const:455300:8", "const:4:8"]]
+ 00455300 ["CALL", null, ["callee:00c57b70:8"]]
- 00432468 bytes 2ea31e94
+ 00455300 bytes 1c0a2094
- 00432664 ["INT_ADD", "register:40f0:8", ["const:432664:8", "const:4:8"]]
- 00432664 ["CALL", null, ["callee:00450970:8"]]
+ 004554fc ["INT_ADD", "register:40f0:8", ["const:4554fc:8", "const:4:8"]]
+ 004554fc ["CALL", null, ["callee:00450970:8"]]
- 00432664 bytes 1dedff97
+ 004554fc bytes 1dedff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eea890eeee86d1e934d2489c771bf5a3"></a>

### [`00432904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432904.md) → [`0045579c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md) FUN_0045579c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00853228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853228.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004288b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004288b4.md) [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`00438ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438ef4.md) [`00440380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440380.md)
- 新版 呼出元 1件 [`008861c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008861c0.md) · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b3b4.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`0045bd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd8c.md) [`00463218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463218.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00455828",
      "incomplete_value": false,
      "site": "00455830",
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
    "old": {
      "definition_site": "00432990",
      "incomplete_value": false,
      "site": "00432998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "definition_site": "0045584c",
      "incomplete_value": false,
      "site": "0045584c",
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
    "old": {
      "definition_site": "004329b4",
      "incomplete_value": false,
      "site": "004329b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "00455930",
      "incomplete_value": false,
      "site": "00455930",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00432a98",
      "incomplete_value": false,
      "site": "00432a98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "004557e0",
      "PARAM",
      [
        "storage",
        "0029b23e",
        null,
        "string"
      ]
    ],
    [
      "00455830",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "0045584c",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004557e0",
      "PARAM",
      [
        "storage",
        "002ab21f",
        null,
        "string"
      ]
    ],
    [
      "00455830",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ],
    [
      "0045584c",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00432950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432904.md#insn-00432950) · [`00432b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432904.md#insn-00432b9c) · [`00432940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432904.md#insn-00432940)
- 新版 [`004557e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md#insn-004557e8) · [`00455a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md#insn-00455a34) · [`004557d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md#insn-004557d8)

~~~diff
- 00432950 ["INT_ADD", "register:40f0:8", ["const:432950:8", "const:4:8"]]
- 00432950 ["CALL", null, ["callee:00c57b70:8"]]
+ 004557e8 ["INT_ADD", "register:40f0:8", ["const:4557e8:8", "const:4:8"]]
+ 004557e8 ["CALL", null, ["callee:00c57b70:8"]]
- 00432950 bytes f4a11e94
+ 004557e8 bytes e2082094
- 00432b9c ["INT_ADD", "register:40f0:8", ["const:432b9c:8", "const:4:8"]]
- 00432b9c ["CALL", null, ["callee:00450970:8"]]
+ 00455a34 ["INT_ADD", "register:40f0:8", ["const:455a34:8", "const:4:8"]]
+ 00455a34 ["CALL", null, ["callee:00450970:8"]]
- 00432b9c bytes cfebff97
+ 00455a34 bytes cfebff97
- 00432940 ["INT_ADD", "register:40f0:8", ["const:432940:8", "const:4:8"]]
- 00432940 ["CALL", null, ["callee:0044b3b4:8"]]
+ 004557d8 ["INT_ADD", "register:40f0:8", ["const:4557d8:8", "const:4:8"]]
+ 004557d8 ["CALL", null, ["callee:0044b3b4:8"]]
- 00432940 bytes ddd7ff97
+ 004557d8 bytes f7d6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b87cfca4095620b7a6e0f632498476b"></a>

### [`00432e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432e80.md) → [`00455d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/00455d18.md) FUN_00455d18

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00868b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868b14.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004288b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004288b4.md) [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`00438ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438ef4.md)
- 新版 呼出元 1件 [`0089c00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089c/0089c00c.md) · 呼出先 13件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b3b4.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`0045bd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd8c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.78% / 新版 94.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00455da8",
      "incomplete_value": false,
      "site": "00455db0",
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
    "old": {
      "definition_site": "00432f10",
      "incomplete_value": false,
      "site": "00432f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "definition_site": "00455dd0",
      "incomplete_value": false,
      "site": "00455dd0",
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
    "old": {
      "definition_site": "00432f38",
      "incomplete_value": false,
      "site": "00432f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "00455e08",
      "incomplete_value": true,
      "site": "00455e08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ece:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00432f70",
      "incomplete_value": true,
      "site": "00432f70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b5:8"
              ]
            ]
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
      "00455d60",
      "PARAM",
      [
        "storage",
        "002a42f4",
        null,
        "string"
      ]
    ],
    [
      "00455db0",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "00455dd0",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00455d60",
      "PARAM",
      [
        "storage",
        "002b4b61",
        null,
        "string"
      ]
    ],
    [
      "00455db0",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ],
    [
      "00455dd0",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00432ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432e80.md#insn-00432ed0) · [`00433158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432e80.md#insn-00433158) · [`00432ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432e80.md#insn-00432ec0)
- 新版 [`00455d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/00455d18.md#insn-00455d68) · [`00455ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/00455d18.md#insn-00455ff0) · [`00455d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/00455d18.md#insn-00455d58)

~~~diff
- 00432ed0 ["INT_ADD", "register:40f0:8", ["const:432ed0:8", "const:4:8"]]
- 00432ed0 ["CALL", null, ["callee:00c57b70:8"]]
+ 00455d68 ["INT_ADD", "register:40f0:8", ["const:455d68:8", "const:4:8"]]
+ 00455d68 ["CALL", null, ["callee:00c57b70:8"]]
- 00432ed0 bytes 94a01e94
+ 00455d68 bytes 82072094
- 00433158 ["INT_ADD", "register:40f0:8", ["const:433158:8", "const:4:8"]]
- 00433158 ["CALL", null, ["callee:00450970:8"]]
+ 00455ff0 ["INT_ADD", "register:40f0:8", ["const:455ff0:8", "const:4:8"]]
+ 00455ff0 ["CALL", null, ["callee:00450970:8"]]
- 00433158 bytes 60eaff97
+ 00455ff0 bytes 60eaff97
- 00432ec0 ["INT_ADD", "register:40f0:8", ["const:432ec0:8", "const:4:8"]]
- 00432ec0 ["CALL", null, ["callee:0044b3b4:8"]]
+ 00455d58 ["INT_ADD", "register:40f0:8", ["const:455d58:8", "const:4:8"]]
+ 00455d58 ["CALL", null, ["callee:0044b3b4:8"]]
- 00432ec0 bytes 7dd6ff97
+ 00455d58 bytes 97d5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bbc4052f3a023e4a7576b82b495fd12"></a>

### [`0043344c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/0043344c.md) → [`004562e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md) FUN_004562e4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`0084e780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e780.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289a4.md) [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`00441100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441100.md) [`00441e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441e04.md)
- 新版 呼出元 2件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4a4.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00463f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463f98.md) [`00464c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464c9c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00456424",
      "incomplete_value": false,
      "site": "00456424",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043358c",
      "incomplete_value": false,
      "site": "0043358c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:758:8"
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
      "definition_site": "004564c4",
      "incomplete_value": false,
      "site": "004564c4",
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
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043362c",
      "incomplete_value": false,
      "site": "0043362c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00456324",
      "incomplete_value": false,
      "site": "0045632c",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043348c",
      "incomplete_value": false,
      "site": "00433494",
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
            "const:3ba:8"
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
      "00456324",
      "PARAM",
      [
        "storage",
        "0029c3ba",
        null,
        "string"
      ]
    ],
    [
      "00456424",
      "DATA",
      [
        "storage",
        "00be7758",
        null,
        "undefined *"
      ]
    ],
    [
      "004564c4",
      "DATA",
      [
        "storage",
        "00be77d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00456324",
      "PARAM",
      [
        "storage",
        "002ac5e0",
        null,
        "string"
      ]
    ],
    [
      "00456424",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ],
    [
      "004564c4",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00433494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/0043344c.md#insn-00433494) · [`00433690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/0043344c.md#insn-00433690) · [`00433484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/0043344c.md#insn-00433484)
- 新版 [`0045632c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md#insn-0045632c) · [`00456528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md#insn-00456528) · [`0045631c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md#insn-0045631c)

~~~diff
- 00433494 ["INT_ADD", "register:40f0:8", ["const:433494:8", "const:4:8"]]
- 00433494 ["CALL", null, ["callee:00c57b70:8"]]
+ 0045632c ["INT_ADD", "register:40f0:8", ["const:45632c:8", "const:4:8"]]
+ 0045632c ["CALL", null, ["callee:00c57b70:8"]]
- 00433494 bytes 239f1e94
+ 0045632c bytes 11062094
- 00433690 ["INT_ADD", "register:40f0:8", ["const:433690:8", "const:4:8"]]
- 00433690 ["CALL", null, ["callee:00450970:8"]]
+ 00456528 ["INT_ADD", "register:40f0:8", ["const:456528:8", "const:4:8"]]
+ 00456528 ["CALL", null, ["callee:00450970:8"]]
- 00433690 bytes 12e9ff97
+ 00456528 bytes 12e9ff97
- 00433484 ["INT_ADD", "register:40f0:8", ["const:433484:8", "const:4:8"]]
- 00433484 ["CALL", null, ["callee:0044b4a4:8"]]
+ 0045631c ["INT_ADD", "register:40f0:8", ["const:45631c:8", "const:4:8"]]
+ 0045631c ["CALL", null, ["callee:0044b4a4:8"]]
- 00433484 bytes 48d5ff97
+ 0045631c bytes 62d4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc3b7497688d387f6d67419b04a12dcc"></a>

### [`00433930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/00433930.md) → [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) FUN_004567c8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0083b3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b3f0.md) [`00853acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853acc.md) · 呼出先 11件 [`0044210c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044210c.md) [`0053e13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e13c.md) [`0053e18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e18c.md) [`0053e1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e1dc.md) [`0053e9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e9d0.md)
- 新版 呼出元 2件 [`0086d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md) [`00886a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886a64.md) · 呼出先 11件 [`00464fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464fa4.md) [`00560fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fd4.md) [`00561024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md) [`00561074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md) [`00561868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561868.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.13% / 新版 91.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00456854",
      "incomplete_value": true,
      "site": "00456854",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004339bc",
      "incomplete_value": true,
      "site": "004339bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ff:8"
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
      "definition_site": "00456920",
      "incomplete_value": true,
      "site": "00456920",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00433a88",
      "incomplete_value": true,
      "site": "00433a88",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:298000:8"
              ],
              [
                "leaf",
                "const:c29:8"
              ]
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
    "kind": "store_value",
    "new": {
      "definition_site": "00456924",
      "incomplete_value": true,
      "site": "00456924",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00433a8c",
      "incomplete_value": true,
      "site": "00433a8c",
      "value": [
        "LOAD",
        "8",
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
      "00456804",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "00456804",
      "PARAM",
      [
        "storage",
        "00c25e28",
        null,
        "undefined1"
      ]
    ],
    [
      "0045683c",
      "READ",
      [
        "storage",
        "002a73ff",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00456804",
      "READ",
      [
        "storage",
        "00c9a808",
        null,
        "pointer"
      ]
    ],
    [
      "00456804",
      "PARAM",
      [
        "storage",
        "00ca58e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00456830",
      "DATA",
      [
        "storage",
        "0079656b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00433974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/00433930.md#insn-00433974) · [`0043394c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/00433930.md#insn-0043394c) · [`0043396c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/00433930.md#insn-0043396c)
- 新版 [`0045680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md#insn-0045680c) · [`004567e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md#insn-004567e4) · [`00456804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md#insn-00456804)

~~~diff
- 00433974 ["INT_ADD", "register:40f0:8", ["const:433974:8", "const:4:8"]]
- 00433974 ["CALL", null, ["callee:00561cf4:8"]]
+ 0045680c ["INT_ADD", "register:40f0:8", ["const:45680c:8", "const:4:8"]]
+ 0045680c ["CALL", null, ["callee:00561cf4:8"]]
- 00433974 bytes 3a2d0494
+ 0045680c bytes 3a2d0494
- 0043394c ["COPY", "register:4000:8", ["const:c1a000:8"]]
+ 004567e4 ["COPY", "register:4000:8", ["const:c9a000:8"]]
- 0043394c bytes 203f00f0
+ 004567e4 bytes 20420090
- 0043396c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:e18:8"]]
- 0043396c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00456804 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:808:8"]]
+ 00456804 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0043396c bytes 000c47f9
+ 00456804 bytes 000444f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df19ad9b846c92165a1fc0c8b0094d69"></a>

### [`00434024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434024.md) → [`00456ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md) FUN_00456ebc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289a4.md) [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md)
- 新版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 22件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4a4.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.47% / 新版 94.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004570a0",
      "incomplete_value": false,
      "site": "004570a0",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00434208",
      "incomplete_value": false,
      "site": "00434208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004570a4",
      "incomplete_value": false,
      "site": "004570a4",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043420c",
      "incomplete_value": false,
      "site": "0043420c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "definition_site": "00457190",
      "incomplete_value": true,
      "site": "00457198",
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
      "definition_site": "004342f8",
      "incomplete_value": true,
      "site": "00434300",
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
      "00456f04",
      "PARAM",
      [
        "storage",
        "002a0394",
        null,
        "string"
      ]
    ],
    [
      "004570a0",
      "DATA",
      [
        "storage",
        "00be78d8",
        null,
        "undefined *"
      ]
    ],
    [
      "004570a4",
      "DATA",
      [
        "storage",
        "00be7958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00456f04",
      "PARAM",
      [
        "storage",
        "002b094e",
        null,
        "string"
      ]
    ],
    [
      "004570a0",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ],
    [
      "004570a4",
      "DATA",
      [
        "storage",
        "00c64518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00434074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434024.md#insn-00434074) · [`00434234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434024.md#insn-00434234) · [`00434064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434024.md#insn-00434064)
- 新版 [`00456f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md#insn-00456f0c) · [`004570cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md#insn-004570cc) · [`00456efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md#insn-00456efc)

~~~diff
- 00434074 ["INT_ADD", "register:40f0:8", ["const:434074:8", "const:4:8"]]
- 00434074 ["CALL", null, ["callee:00c57b70:8"]]
+ 00456f0c ["INT_ADD", "register:40f0:8", ["const:456f0c:8", "const:4:8"]]
+ 00456f0c ["CALL", null, ["callee:00c57b70:8"]]
- 00434074 bytes 2b9c1e94
+ 00456f0c bytes 19032094
- 00434234 ["INT_ADD", "register:40f0:8", ["const:434234:8", "const:4:8"]]
- 00434234 ["CALL", null, ["callee:00450970:8"]]
+ 004570cc ["INT_ADD", "register:40f0:8", ["const:4570cc:8", "const:4:8"]]
+ 004570cc ["CALL", null, ["callee:00450970:8"]]
- 00434234 bytes 29e6ff97
+ 004570cc bytes 29e6ff97
- 00434064 ["INT_ADD", "register:40f0:8", ["const:434064:8", "const:4:8"]]
- 00434064 ["CALL", null, ["callee:0044b4a4:8"]]
+ 00456efc ["INT_ADD", "register:40f0:8", ["const:456efc:8", "const:4:8"]]
+ 00456efc ["CALL", null, ["callee:0044b4a4:8"]]
- 00434064 bytes 50d2ff97
+ 00456efc bytes 6ad1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba678d5e46f6391c5d61882e00c50fac"></a>

### [`00434528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434528.md) → [`004573c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md) FUN_004573c0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00853f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853f6c.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289a4.md) [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md)
- 新版 呼出元 1件 [`00886f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886f04.md) · 呼出先 20件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4a4.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.87% / 新版 93.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00457578",
      "incomplete_value": false,
      "site": "00457578",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004346e0",
      "incomplete_value": false,
      "site": "004346e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045757c",
      "incomplete_value": false,
      "site": "0045757c",
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
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004346e4",
      "incomplete_value": false,
      "site": "004346e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "00457638",
      "incomplete_value": true,
      "site": "00457640",
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
      "definition_site": "004347a0",
      "incomplete_value": true,
      "site": "004347a8",
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
      "00457408",
      "PARAM",
      [
        "storage",
        "0029793b",
        null,
        "string"
      ]
    ],
    [
      "00457578",
      "DATA",
      [
        "storage",
        "00be79d8",
        null,
        "undefined *"
      ]
    ],
    [
      "0045757c",
      "DATA",
      [
        "storage",
        "00be7a58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00457408",
      "PARAM",
      [
        "storage",
        "002a7594",
        null,
        "string"
      ]
    ],
    [
      "00457578",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ],
    [
      "0045757c",
      "DATA",
      [
        "storage",
        "00c64618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00434578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434528.md#insn-00434578) · [`0043470c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434528.md#insn-0043470c) · [`00434568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434528.md#insn-00434568)
- 新版 [`00457410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md#insn-00457410) · [`004575a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md#insn-004575a4) · [`00457400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md#insn-00457400)

~~~diff
- 00434578 ["INT_ADD", "register:40f0:8", ["const:434578:8", "const:4:8"]]
- 00434578 ["CALL", null, ["callee:00c57b70:8"]]
+ 00457410 ["INT_ADD", "register:40f0:8", ["const:457410:8", "const:4:8"]]
+ 00457410 ["CALL", null, ["callee:00c57b70:8"]]
- 00434578 bytes ea9a1e94
+ 00457410 bytes d8012094
- 0043470c ["INT_ADD", "register:40f0:8", ["const:43470c:8", "const:4:8"]]
- 0043470c ["CALL", null, ["callee:00450970:8"]]
+ 004575a4 ["INT_ADD", "register:40f0:8", ["const:4575a4:8", "const:4:8"]]
+ 004575a4 ["CALL", null, ["callee:00450970:8"]]
- 0043470c bytes f3e4ff97
+ 004575a4 bytes f3e4ff97
- 00434568 ["INT_ADD", "register:40f0:8", ["const:434568:8", "const:4:8"]]
- 00434568 ["CALL", null, ["callee:0044b4a4:8"]]
+ 00457400 ["INT_ADD", "register:40f0:8", ["const:457400:8", "const:4:8"]]
+ 00457400 ["CALL", null, ["callee:0044b4a4:8"]]
- 00434568 bytes 0fd1ff97
+ 00457400 bytes 29d0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e0d0504aab5fd0fc796e75ea8055548"></a>

### [`004349a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/004349a0.md) → [`00457838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md) FUN_00457838

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00860de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860de0.md) · 呼出先 25件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289a4.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md)
- 新版 呼出元 1件 [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) · 呼出先 25件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4a4.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00457890",
      "incomplete_value": false,
      "site": "00457898",
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
    "old": {
      "definition_site": "004349f8",
      "incomplete_value": false,
      "site": "00434a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "definition_site": "004578a4",
      "incomplete_value": false,
      "site": "004578a4",
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
    "old": {
      "definition_site": "00434a0c",
      "incomplete_value": false,
      "site": "00434a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "0045795c",
      "incomplete_value": true,
      "site": "0045795c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00434ac4",
      "incomplete_value": true,
      "site": "00434ac4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:298000:8"
              ],
              [
                "leaf",
                "const:c1e:8"
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
      "00457898",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "004578a4",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ],
    [
      "0045794c",
      "READ",
      [
        "storage",
        "00298c1e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00457898",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ],
    [
      "004578a4",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ],
    [
      "0045794c",
      "READ",
      [
        "storage",
        "002a89dc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00434b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/004349a0.md#insn-00434b88) · [`00434be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/004349a0.md#insn-00434be8) · [`00434c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/004349a0.md#insn-00434c1c)
- 新版 [`00457a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md#insn-00457a20) · [`00457a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md#insn-00457a80) · [`00457ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md#insn-00457ab4)

~~~diff
- 00434b88 ["INT_ADD", "register:40f0:8", ["const:434b88:8", "const:4:8"]]
- 00434b88 ["CALL", null, ["callee:00c57b70:8"]]
+ 00457a20 ["INT_ADD", "register:40f0:8", ["const:457a20:8", "const:4:8"]]
+ 00457a20 ["CALL", null, ["callee:00c57b70:8"]]
- 00434b88 bytes 66991e94
+ 00457a20 bytes 54002094
- 00434be8 ["INT_ADD", "register:40f0:8", ["const:434be8:8", "const:4:8"]]
- 00434be8 ["CALL", null, ["callee:00c57b70:8"]]
+ 00457a80 ["INT_ADD", "register:40f0:8", ["const:457a80:8", "const:4:8"]]
+ 00457a80 ["CALL", null, ["callee:00c57b70:8"]]
- 00434be8 bytes 4e991e94
+ 00457a80 bytes 3c002094
- 00434c1c ["INT_ADD", "register:40f0:8", ["const:434c1c:8", "const:4:8"]]
- 00434c1c ["CALL", null, ["callee:00561cf4:8"]]
+ 00457ab4 ["INT_ADD", "register:40f0:8", ["const:457ab4:8", "const:4:8"]]
+ 00457ab4 ["CALL", null, ["callee:00561cf4:8"]]
- 00434c1c bytes 90280494
+ 00457ab4 bytes 90280494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00445c11b1b1bfd8d7adc45f0aee0980"></a>

### [`00435358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435358.md) → [`004581f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/004581f0.md) FUN_004581f0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0084c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004289a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289a4.md) [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`00436bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436bf8.md)
- 新版 呼出元 1件 [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) · 呼出先 18件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4a4.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00459a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459a90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004582c8",
      "incomplete_value": false,
      "site": "004582d0",
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
    "old": {
      "definition_site": "00435430",
      "incomplete_value": false,
      "site": "00435438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004582ec",
      "incomplete_value": false,
      "site": "004582ec",
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
    "old": {
      "definition_site": "00435454",
      "incomplete_value": false,
      "site": "00435454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00458354",
      "incomplete_value": true,
      "site": "00458354",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004354bc",
      "incomplete_value": true,
      "site": "004354bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:298000:8"
              ],
              [
                "leaf",
                "const:c1e:8"
              ]
            ]
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
      "00458234",
      "PARAM",
      [
        "storage",
        "002a3212",
        null,
        "string"
      ]
    ],
    [
      "004582d0",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ],
    [
      "004582ec",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00458234",
      "PARAM",
      [
        "storage",
        "002b38ec",
        null,
        "string"
      ]
    ],
    [
      "004582d0",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ],
    [
      "004582ec",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004353a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435358.md#insn-004353a4) · [`004355a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435358.md#insn-004355a8) · [`00435394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435358.md#insn-00435394)
- 新版 [`0045823c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/004581f0.md#insn-0045823c) · [`00458440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/004581f0.md#insn-00458440) · [`0045822c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/004581f0.md#insn-0045822c)

~~~diff
- 004353a4 ["INT_ADD", "register:40f0:8", ["const:4353a4:8", "const:4:8"]]
- 004353a4 ["CALL", null, ["callee:00c57b70:8"]]
+ 0045823c ["INT_ADD", "register:40f0:8", ["const:45823c:8", "const:4:8"]]
+ 0045823c ["CALL", null, ["callee:00c57b70:8"]]
- 004353a4 bytes 5f971e94
+ 0045823c bytes 4dfe1f94
- 004355a8 ["INT_ADD", "register:40f0:8", ["const:4355a8:8", "const:4:8"]]
- 004355a8 ["CALL", null, ["callee:00450970:8"]]
+ 00458440 ["INT_ADD", "register:40f0:8", ["const:458440:8", "const:4:8"]]
+ 00458440 ["CALL", null, ["callee:00450970:8"]]
- 004355a8 bytes 4ce1ff97
+ 00458440 bytes 4ce1ff97
- 00435394 ["INT_ADD", "register:40f0:8", ["const:435394:8", "const:4:8"]]
- 00435394 ["CALL", null, ["callee:0044b4a4:8"]]
+ 0045822c ["INT_ADD", "register:40f0:8", ["const:45822c:8", "const:4:8"]]
+ 0045822c ["CALL", null, ["callee:0044b4a4:8"]]
- 00435394 bytes 84cdff97
+ 0045822c bytes 9eccff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c13749675fd6e8bc5424454906450c03"></a>

### [`004357f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/004357f4.md) → [`0045868c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/0045868c.md) FUN_0045868c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00435c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435c18.md) · 呼出先 11件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00443e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443e34.md) [`0053ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00458ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md) · 呼出先 11件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00466ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ccc.md) [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00458894",
      "incomplete_value": false,
      "site": "00458894",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004359fc",
      "incomplete_value": false,
      "site": "004359fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00458824",
      "incomplete_value": true,
      "site": "0045882c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043598c",
      "incomplete_value": true,
      "site": "00435994",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
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
      "004587b4",
      "READ",
      [
        "storage",
        "0029583f",
        null,
        "undefined4"
      ]
    ],
    [
      "004587b8",
      "READ",
      [
        "storage",
        "00295843",
        null,
        "undefined1"
      ]
    ],
    [
      "00458824",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004587b4",
      "READ",
      [
        "storage",
        "002a5278",
        null,
        "undefined4"
      ]
    ],
    [
      "004587b8",
      "READ",
      [
        "storage",
        "002a527c",
        null,
        "undefined1"
      ]
    ],
    [
      "00458824",
      "READ",
      [
        "storage",
        "00c9a7c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00435994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/004357f4.md#insn-00435994) · [`00435858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/004357f4.md#insn-00435858) · [`00435894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/004357f4.md#insn-00435894)
- 新版 [`0045882c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/0045868c.md#insn-0045882c) · [`004586f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/0045868c.md#insn-004586f0) · [`0045872c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/0045868c.md#insn-0045872c)

~~~diff
- 00435994 ["INT_ADD", "register:40f0:8", ["const:435994:8", "const:4:8"]]
- 00435994 ["CALL", null, ["callee:00561cf4:8"]]
+ 0045882c ["INT_ADD", "register:40f0:8", ["const:45882c:8", "const:4:8"]]
+ 0045882c ["CALL", null, ["callee:00561cf4:8"]]
- 00435994 bytes 32250494
+ 0045882c bytes 32250494
- 00435858 ["INT_ADD", "register:40f0:8", ["const:435858:8", "const:4:8"]]
- 00435858 ["CALL", null, ["callee:00c57bd0:8"]]
+ 004586f0 ["INT_ADD", "register:40f0:8", ["const:4586f0:8", "const:4:8"]]
+ 004586f0 ["CALL", null, ["callee:00c57bd0:8"]]
- 00435858 bytes 4a961e94
+ 004586f0 bytes 38fd1f94
- 00435894 ["COPY", "register:40d0:8", ["const:298000:8"]]
+ 0045872c ["COPY", "register:40d0:8", ["const:2a8000:8"]]
- 00435894 bytes 1af3fff0
+ 0045872c bytes 9af2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dab12dfe68bfe8086a557987ed91e1e4"></a>

### [`00435c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435c18.md) → [`00458ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md) FUN_00458ab0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 11件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`00428cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428cb4.md) [`00428dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428dc8.md) [`004357f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/004357f4.md) [`00444068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444068.md)
- 新版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 11件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0044b804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b804.md) [`0044b918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b918.md) [`0045868c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/0045868c.md) [`00466f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466f00.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.59% / 新版 96.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00458b38",
      "incomplete_value": false,
      "site": "00458b40",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00435ca0",
      "incomplete_value": false,
      "site": "00435ca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00458ad8",
      "value": [
        "leaf",
        "ram:44b804:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00435c40",
      "value": [
        "leaf",
        "ram:428cb4:8"
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
      "00458ad8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00428cb4"
      ]
    ],
    [
      "00458b40",
      "DATA",
      [
        "storage",
        "00be7cd8",
        null,
        "undefined *"
      ]
    ],
    [
      "00458ba0",
      "READ",
      [
        "storage",
        "00be7cf8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00458ad8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b804"
      ]
    ],
    [
      "00458b40",
      "DATA",
      [
        "storage",
        "00c64898",
        null,
        "undefined *"
      ]
    ],
    [
      "00458ba0",
      "READ",
      [
        "storage",
        "00c648b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00435c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435c18.md#insn-00435c40) · [`00435c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435c18.md#insn-00435c48) · [`00435c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435c18.md#insn-00435c58)
- 新版 [`00458ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md#insn-00458ad8) · [`00458ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md#insn-00458ae0) · [`00458af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md#insn-00458af0)

~~~diff
- 00435c40 ["INT_ADD", "register:40f0:8", ["const:435c40:8", "const:4:8"]]
- 00435c40 ["CALL", null, ["ram:428cb4:8"]]
+ 00458ad8 ["INT_ADD", "register:40f0:8", ["const:458ad8:8", "const:4:8"]]
+ 00458ad8 ["CALL", null, ["ram:44b804:8"]]
- 00435c40 bytes 1dccff97
+ 00458ad8 bytes 4bcbff97
- 00435c48 ["INT_ADD", "register:40f0:8", ["const:435c48:8", "const:4:8"]]
- 00435c48 ["CALL", null, ["callee:0044b918:8"]]
+ 00458ae0 ["INT_ADD", "register:40f0:8", ["const:458ae0:8", "const:4:8"]]
+ 00458ae0 ["CALL", null, ["callee:0044b918:8"]]
- 00435c48 bytes 60ccff97
+ 00458ae0 bytes 8ecbff97
- 00435c58 ["INT_ADD", "register:40f0:8", ["const:435c58:8", "const:4:8"]]
- 00435c58 ["CALL", null, ["callee:0043db64:8"]]
+ 00458af0 ["INT_ADD", "register:40f0:8", ["const:458af0:8", "const:4:8"]]
+ 00458af0 ["CALL", null, ["callee:0043db64:8"]]
- 00435c58 bytes 0395ff97
+ 00458af0 bytes 1d94ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de97dcb76afaccf3eb9512406613553a"></a>

### [`004364f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004364f8.md) → [`00459390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459390.md) FUN_00459390

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00459398",
      "incomplete_value": false,
      "site": "0045939c",
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
    "old": {
      "definition_site": "00436500",
      "incomplete_value": false,
      "site": "00436504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "0045939c",
      "DATA",
      [
        "storage",
        "00be67a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045939c",
      "DATA",
      [
        "storage",
        "00c63360",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004364fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004364f8.md#insn-004364fc) · [`00436500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004364f8.md#insn-00436500)
- 新版 [`00459394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459390.md#insn-00459394) · [`00459398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459390.md#insn-00459398)

~~~diff
- 004364fc ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 00459394 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 004364fc bytes 893d0090
+ 00459394 bytes 494000d0
- 00436500 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 00436500 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00436500 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00436500 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00459398 ["COPY", "tmp:0:8", ["const:360:8"]]
+ 00459398 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00459398 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00459398 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00436500 bytes 29811e91
+ 00459398 bytes 29810d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6aa6d80e4dadedc4dd160a61a08665c"></a>

### [`00436518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436518.md) → [`004593b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md) FUN_004593b0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`00575024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00575/00575024.md) [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) [`0076e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e98c.md) [`00aaebc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaebc4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 6件 [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`0059baa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059baa4.md) [`005a1430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1430.md) [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00798e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "004593b8",
      "incomplete_value": false,
      "site": "004593bc",
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
    "old": {
      "definition_site": "00436520",
      "incomplete_value": false,
      "site": "00436524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "004593bc",
      "DATA",
      [
        "storage",
        "00be67a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004593bc",
      "DATA",
      [
        "storage",
        "00c63360",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043651c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436518.md#insn-0043651c) · [`00436520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436518.md#insn-00436520) · [`00436544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436518.md#insn-00436544)
- 新版 [`004593b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md#insn-004593b4) · [`004593b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md#insn-004593b8) · [`004593dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md#insn-004593dc)

~~~diff
- 0043651c ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 004593b4 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0043651c bytes 893d0090
+ 004593b4 bytes 494000d0
- 00436520 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 00436520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00436520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00436520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004593b8 ["COPY", "tmp:0:8", ["const:360:8"]]
+ 004593b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004593b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004593b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00436520 bytes 29811e91
+ 004593b8 bytes 29810d91
- 00436544 ["INT_ADD", "register:40f0:8", ["const:436544:8", "const:4:8"]]
- 00436544 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004593dc ["INT_ADD", "register:40f0:8", ["const:4593dc:8", "const:4:8"]]
+ 004593dc ["CALL", null, ["callee:00c57ab0:8"]]
- 00436544 bytes c7921e94
+ 004593dc bytes b5f91f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01f72906a09a7be6ef09da206125f42b"></a>

### [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) → [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) FUN_00459490

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 25件 [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`00444070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444070.md) [`0045543c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/0045543c.md) [`004656ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004656ac.md) [`0046a090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a090.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md)
- 新版 呼出元 25件 [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`00466f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466f08.md) [`004782d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/004782d4.md) [`00488544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488544.md) [`0048cf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cf28.md) · 呼出先 8件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00459510",
      "incomplete_value": true,
      "site": "00459514",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00436678",
      "incomplete_value": true,
      "site": "0043667c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00459530",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00436698",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "site": "00459584",
      "value": [
        "leaf",
        "ram:c57eb0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004366ec",
      "value": [
        "leaf",
        "ram:bdb460:8"
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
      "00459510",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00459510",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00459530",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00459510",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00459510",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00459530",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043667c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md#insn-0043667c) · [`00436698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md#insn-00436698) · [`004366ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md#insn-004366ec)
- 新版 [`00459514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md#insn-00459514) · [`00459530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md#insn-00459530) · [`00459584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md#insn-00459584)

~~~diff
- 0043667c ["INT_ADD", "register:40f0:8", ["const:43667c:8", "const:4:8"]]
- 0043667c ["CALL", null, ["callee:00c57e80:8"]]
+ 00459514 ["INT_ADD", "register:40f0:8", ["const:459514:8", "const:4:8"]]
+ 00459514 ["CALL", null, ["callee:00c57e80:8"]]
- 0043667c bytes 6d931e94
+ 00459514 bytes 5bfa1f94
- 00436698 ["INT_ADD", "register:40f0:8", ["const:436698:8", "const:4:8"]]
- 00436698 ["CALL", null, ["ram:bdb440:8"]]
+ 00459530 ["INT_ADD", "register:40f0:8", ["const:459530:8", "const:4:8"]]
+ 00459530 ["CALL", null, ["ram:c57e90:8"]]
- 00436698 bytes 6a931e94
+ 00459530 bytes 58fa1f94
- 004366ec ["INT_ADD", "register:40f0:8", ["const:4366ec:8", "const:4:8"]]
- 004366ec ["CALL", null, ["ram:bdb460:8"]]
+ 00459584 ["INT_ADD", "register:40f0:8", ["const:459584:8", "const:4:8"]]
+ 00459584 ["CALL", null, ["ram:c57eb0:8"]]
- 004366ec bytes 5d931e94
+ 00459584 bytes 4bfa1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e7c69fcdd22c9bc992494c9ddb1b5a7"></a>

### [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) → [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) FUN_00459d34

採用 · 移動量 `+0x22e98` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 169件 [`00437118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437118.md) [`00437c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437c94.md) [`004389fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/004389fc.md) [`004391e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004391e0.md) [`00439a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439a30.md) · 呼出先 3件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 207件 [`00459fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459fb0.md) [`0045ab2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045ab2c.md) [`0045b894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b894.md) [`0045c078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c078.md) [`0045c8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c8c8.md) · 呼出先 3件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00459d54",
      "incomplete_value": true,
      "site": "00459d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00436ebc",
      "incomplete_value": true,
      "site": "00436ec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00459d5c",
      "incomplete_value": true,
      "site": "00459d64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:840:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00436ec4",
      "incomplete_value": true,
      "site": "00436ecc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
              ]
            ]
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
      "definition_site": "00459d60",
      "incomplete_value": true,
      "site": "00459d64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:848:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00436ec8",
      "incomplete_value": true,
      "site": "00436ecc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
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
      "00459d50",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "00459d58",
      "DATA",
      [
        "storage",
        "00be6838",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00459d5c",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00459d50",
      "READ",
      [
        "storage",
        "00c9a838",
        null,
        "pointer"
      ]
    ],
    [
      "00459d58",
      "DATA",
      [
        "storage",
        "00c633f8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00459d5c",
      "READ",
      [
        "storage",
        "00c9a840",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00436ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md#insn-00436ecc) · [`00436ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md#insn-00436ea8) · [`00436eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md#insn-00436eac)
- 新版 [`00459d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md#insn-00459d64) · [`00459d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md#insn-00459d40) · [`00459d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md#insn-00459d44)

~~~diff
- 00436ecc ["INT_ADD", "register:40f0:8", ["const:436ecc:8", "const:4:8"]]
- 00436ecc ["CALL", null, ["callee:00c57b10:8"]]
+ 00459d64 ["INT_ADD", "register:40f0:8", ["const:459d64:8", "const:4:8"]]
+ 00459d64 ["CALL", null, ["callee:00c57b10:8"]]
- 00436ecc bytes 7d901e94
+ 00459d64 bytes 6bf71f94
- 00436ea8 ["INT_ADD", "register:40f0:8", ["const:436ea8:8", "const:4:8"]]
- 00436ea8 ["CALL", null, ["callee:00c57af0:8"]]
+ 00459d40 ["INT_ADD", "register:40f0:8", ["const:459d40:8", "const:4:8"]]
+ 00459d40 ["CALL", null, ["callee:00c57af0:8"]]
- 00436ea8 bytes 7e901e94
+ 00459d40 bytes 6cf71f94
- 00436eac ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00459d44 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00436eac bytes 283f0090
+ 00459d44 bytes 084200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3edb609da0423528be464640ae881ea2"></a>

### [`00436ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436ef4.md) → [`00459d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d8c.md) FUN_00459d8c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00459d98",
      "incomplete_value": false,
      "site": "00459da4",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00436f00",
      "incomplete_value": false,
      "site": "00436f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "00459da4",
      "DATA",
      [
        "storage",
        "00be6860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00459da4",
      "DATA",
      [
        "storage",
        "00c63420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00436efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436ef4.md#insn-00436efc) · [`00436f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436ef4.md#insn-00436f00)
- 新版 [`00459d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d8c.md#insn-00459d94) · [`00459d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d8c.md#insn-00459d98)

~~~diff
- 00436efc ["COPY", "register:4050:8", ["const:be6000:8"]]
+ 00459d94 ["COPY", "register:4050:8", ["const:c63000:8"]]
- 00436efc bytes 8a3d0090
+ 00459d94 bytes 4a4000d0
- 00436f00 ["COPY", "tmp:0:8", ["const:860:8"]]
- 00436f00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00436f00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00436f00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00459d98 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 00459d98 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00459d98 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00459d98 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00436f00 bytes 4a812191
+ 00459d98 bytes 4a811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-023363d2e1eb81d82749ebd3710abf72"></a>

### [`00436f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436f38.md) → [`00459dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459dd0.md) FUN_00459dd0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00459de8",
      "incomplete_value": false,
      "site": "00459df4",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00436f50",
      "incomplete_value": false,
      "site": "00436f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "00459df4",
      "DATA",
      [
        "storage",
        "00be6860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00459df4",
      "DATA",
      [
        "storage",
        "00c63420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00436f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436f38.md#insn-00436f4c) · [`00436f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436f38.md#insn-00436f50) · [`00436f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436f38.md#insn-00436f80)
- 新版 [`00459de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459dd0.md#insn-00459de4) · [`00459de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459dd0.md#insn-00459de8) · [`00459e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459dd0.md#insn-00459e18)

~~~diff
- 00436f4c ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00459de4 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00436f4c bytes 883d0090
+ 00459de4 bytes 484000d0
- 00436f50 ["COPY", "tmp:0:8", ["const:860:8"]]
- 00436f50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00436f50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00436f50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00459de8 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 00459de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00459de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00459de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00436f50 bytes 08812191
+ 00459de8 bytes 08811091
- 00436f80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00436f80 ["INT_ADD", "register:40f0:8", ["const:436f80:8", "const:4:8"]]
- 00436f80 ["CALLIND", null, ["register:0:8"]]
+ 00459e18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00459e18 ["INT_ADD", "register:40f0:8", ["const:459e18:8", "const:4:8"]]
+ 00459e18 ["CALLIND", null, ["register:0:8"]]
- 00436f80 bytes 00013fd6
+ 00459e18 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cce37e0b09a3bf287b66d365c5201952"></a>

### [`00436f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436f94.md) → [`00459e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459e2c.md) FUN_00459e2c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00459e58",
      "incomplete_value": false,
      "site": "00459e58",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00436fc0",
      "incomplete_value": false,
      "site": "00436fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "00459e58",
      "DATA",
      [
        "storage",
        "00be6860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00459e58",
      "DATA",
      [
        "storage",
        "00c63420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00436fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436f94.md#insn-00436fa8) · [`00436fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436f94.md#insn-00436fb4) · [`00436fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436f94.md#insn-00436fb8)
- 新版 [`00459e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459e2c.md#insn-00459e40) · [`00459e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459e2c.md#insn-00459e4c) · [`00459e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459e2c.md#insn-00459e50)

~~~diff
- 00436fa8 ["INT_ADD", "register:40f0:8", ["const:436fa8:8", "const:4:8"]]
- 00436fa8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00459e40 ["INT_ADD", "register:40f0:8", ["const:459e40:8", "const:4:8"]]
+ 00459e40 ["CALL", null, ["callee:00c57a90:8"]]
- 00436fa8 bytes 26901e94
+ 00459e40 bytes 14f71f94
- 00436fb4 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00459e4c ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00436fb4 bytes 883d0090
+ 00459e4c bytes 484000d0
- 00436fb8 ["COPY", "tmp:0:8", ["const:860:8"]]
- 00436fb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00436fb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00436fb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00459e50 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 00459e50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00459e50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00459e50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00436fb8 bytes 08812191
+ 00459e50 bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7a070556ffb5d1a53907b829d17965a"></a>

### [`0043701c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/0043701c.md) → [`00459eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459eb4.md) FUN_00459eb4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00459ed0",
      "incomplete_value": false,
      "site": "00459ed0",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437038",
      "incomplete_value": false,
      "site": "00437038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "00459ed0",
      "DATA",
      [
        "storage",
        "00be6860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00459ed0",
      "DATA",
      [
        "storage",
        "00c63420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/0043701c.md#insn-00437030) · [`00437034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/0043701c.md#insn-00437034) · [`00437058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/0043701c.md#insn-00437058)
- 新版 [`00459ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459eb4.md#insn-00459ec8) · [`00459ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459eb4.md#insn-00459ecc) · [`00459ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459eb4.md#insn-00459ef0)

~~~diff
- 00437030 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 00459ec8 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 00437030 bytes 693d00f0
+ 00459ec8 bytes 494000d0
- 00437034 ["COPY", "tmp:0:8", ["const:860:8"]]
- 00437034 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00437034 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00437034 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00459ecc ["COPY", "tmp:0:8", ["const:420:8"]]
+ 00459ecc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00459ecc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00459ecc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00437034 bytes 29812191
+ 00459ecc bytes 29811091
- 00437058 ["COPY", "register:0:8", ["register:4048:8"]]
- 00437058 ["INT_ADD", "register:40f0:8", ["const:437058:8", "const:4:8"]]
- 00437058 ["CALLIND", null, ["register:0:8"]]
+ 00459ef0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00459ef0 ["INT_ADD", "register:40f0:8", ["const:459ef0:8", "const:4:8"]]
+ 00459ef0 ["CALLIND", null, ["register:0:8"]]
- 00437058 bytes 20013fd6
+ 00459ef0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc6329ecd118d73e32d2a4d6e1387d8e"></a>

### [`00437118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437118.md) → [`00459fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459fb0.md) FUN_00459fb0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.45% / 新版 93.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045a0d4",
      "incomplete_value": true,
      "site": "0045a0d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e4f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043723c",
      "incomplete_value": true,
      "site": "0043723c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:421:8"
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
      "definition_site": "0045a134",
      "incomplete_value": true,
      "site": "0045a134",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0043729c",
      "incomplete_value": true,
      "site": "0043729c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045a124",
      "incomplete_value": true,
      "site": "0045a134",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:698:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043728c",
      "incomplete_value": true,
      "site": "0043729c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045a0c4",
      "READ",
      [
        "storage",
        "002a5421",
        null,
        "string"
      ]
    ],
    [
      "0045a118",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045a124",
      "READ",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0045a0c4",
      "READ",
      [
        "storage",
        "002b5e4f",
        null,
        "string"
      ]
    ],
    [
      "0045a118",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045a124",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043729c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437118.md#insn-0043729c) · [`004372dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437118.md#insn-004372dc) · [`00437364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437118.md#insn-00437364)
- 新版 [`0045a134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459fb0.md#insn-0045a134) · [`0045a174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459fb0.md#insn-0045a174) · [`0045a1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459fb0.md#insn-0045a1fc)

~~~diff
- 0043729c ["COPY", "register:0:8", ["register:4040:8"]]
- 0043729c ["INT_ADD", "register:40f0:8", ["const:43729c:8", "const:4:8"]]
- 0043729c ["CALLIND", null, ["register:0:8"]]
+ 0045a134 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a134 ["INT_ADD", "register:40f0:8", ["const:45a134:8", "const:4:8"]]
+ 0045a134 ["CALLIND", null, ["register:0:8"]]
- 0043729c bytes 00013fd6
+ 0045a134 bytes 00013fd6
- 004372dc ["COPY", "register:0:8", ["register:4040:8"]]
- 004372dc ["INT_ADD", "register:40f0:8", ["const:4372dc:8", "const:4:8"]]
- 004372dc ["CALLIND", null, ["register:0:8"]]
+ 0045a174 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a174 ["INT_ADD", "register:40f0:8", ["const:45a174:8", "const:4:8"]]
+ 0045a174 ["CALLIND", null, ["register:0:8"]]
- 004372dc bytes 00013fd6
+ 0045a174 bytes 00013fd6
- 00437364 ["COPY", "register:0:8", ["register:4040:8"]]
- 00437364 ["INT_ADD", "register:40f0:8", ["const:437364:8", "const:4:8"]]
- 00437364 ["CALLIND", null, ["register:0:8"]]
+ 0045a1fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a1fc ["INT_ADD", "register:40f0:8", ["const:45a1fc:8", "const:4:8"]]
+ 0045a1fc ["CALLIND", null, ["register:0:8"]]
- 00437364 bytes 00013fd6
+ 0045a1fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-808d9dae65548905ead0a41424a7601f"></a>

### [`004376c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004376c8.md) → [`0045a560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a560.md) FUN_0045a560

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004376bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004376bc.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377f0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)
- 新版 呼出元 1件 [`0045a554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a554.md) · 呼出先 12件 [`0045a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a688.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045a604",
      "incomplete_value": true,
      "site": "0045a608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0043776c",
      "incomplete_value": true,
      "site": "00437770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "site": "0045a5a0",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00437708",
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
      "definition_site": "0045a5e0",
      "incomplete_value": true,
      "site": "0045a5e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00437748",
      "incomplete_value": true,
      "site": "00437750",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0045a5a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ],
    [
      "0045a5dc",
      "PARAM",
      [
        "storage",
        "004377f0",
        null,
        null
      ]
    ],
    [
      "0045a5e0",
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
      "0045a5a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ],
    [
      "0045a5dc",
      "PARAM",
      [
        "storage",
        "0045a688",
        null,
        null
      ]
    ],
    [
      "0045a5e0",
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

- 旧版 [`00437708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004376c8.md#insn-00437708) · [`00437750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004376c8.md#insn-00437750) · [`0043775c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004376c8.md#insn-0043775c)
- 新版 [`0045a5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a560.md#insn-0045a5a0) · [`0045a5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a560.md#insn-0045a5e8) · [`0045a5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a560.md#insn-0045a5f4)

~~~diff
- 00437708 ["INT_ADD", "register:40f0:8", ["const:437708:8", "const:4:8"]]
- 00437708 ["CALL", null, ["ram:bdb4a0:8"]]
+ 0045a5a0 ["INT_ADD", "register:40f0:8", ["const:45a5a0:8", "const:4:8"]]
+ 0045a5a0 ["CALL", null, ["ram:c57ef0:8"]]
- 00437708 bytes 668f1e94
+ 0045a5a0 bytes 54f61f94
- 00437750 ["INT_ADD", "register:40f0:8", ["const:437750:8", "const:4:8"]]
- 00437750 ["CALL", null, ["callee:00c57f30:8"]]
+ 0045a5e8 ["INT_ADD", "register:40f0:8", ["const:45a5e8:8", "const:4:8"]]
+ 0045a5e8 ["CALL", null, ["callee:00c57f30:8"]]
- 00437750 bytes 648f1e94
+ 0045a5e8 bytes 52f61f94
- 0043775c ["INT_ADD", "register:40f0:8", ["const:43775c:8", "const:4:8"]]
- 0043775c ["CALL", null, ["ram:bdb4f0:8"]]
+ 0045a5f4 ["INT_ADD", "register:40f0:8", ["const:45a5f4:8", "const:4:8"]]
+ 0045a5f4 ["CALL", null, ["ram:c57f40:8"]]
- 0043775c bytes 658f1e94
+ 0045a5f4 bytes 53f61f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99643b9766fdc5d6881e62680bfa3444"></a>

### [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) → [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) FUN_0045a694

採用 · 移動量 `+0x22e98` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 20件 [`00430b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430b04.md) [`0043c164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c164.md) [`0043cc04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cc04.md) [`00515468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515468.md) [`00515718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515718.md) · 呼出先 5件 [`00b7c7c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c7c8.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4c0.md) [`00bdb4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4d0.md)
- 新版 呼出元 20件 [`0045399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md) [`0045effc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045effc.md) [`0045fa9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fa9c.md) [`00538300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538300.md) [`005385b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/005385b0.md) · 呼出先 5件 [`00bf9210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9210.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f10.md) [`00c57f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045a6d0",
      "incomplete_value": true,
      "site": "0045a6d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00437838",
      "incomplete_value": true,
      "site": "00437840",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045a6d4",
      "incomplete_value": true,
      "site": "0045a6d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:868:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043783c",
      "incomplete_value": true,
      "site": "00437840",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
              ]
            ]
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
      "0045a6d0",
      "READ",
      [
        "storage",
        "00c1ae68",
        null,
        "pointer"
      ]
    ],
    [
      "0045a6d0",
      "PARAM",
      [
        "storage",
        "00c12f08",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0045a6d4",
      "READ",
      [
        "storage",
        "00c1ae78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045a6d0",
      "READ",
      [
        "storage",
        "00c9a858",
        null,
        "pointer"
      ]
    ],
    [
      "0045a6d0",
      "PARAM",
      [
        "storage",
        "00c928b0",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0045a6d4",
      "READ",
      [
        "storage",
        "00c9a868",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md#insn-00437840) · [`00437810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md#insn-00437810) · [`00437818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md#insn-00437818)
- 新版 [`0045a6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md#insn-0045a6d8) · [`0045a6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md#insn-0045a6a8) · [`0045a6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md#insn-0045a6b0)

~~~diff
- 00437840 ["INT_ADD", "register:40f0:8", ["const:437840:8", "const:4:8"]]
- 00437840 ["CALL", null, ["callee:00c57b10:8"]]
+ 0045a6d8 ["INT_ADD", "register:40f0:8", ["const:45a6d8:8", "const:4:8"]]
+ 0045a6d8 ["CALL", null, ["callee:00c57b10:8"]]
- 00437840 bytes 208e1e94
+ 0045a6d8 bytes 0ef51f94
- 00437810 ["INT_ADD", "register:40f0:8", ["const:437810:8", "const:4:8"]]
- 00437810 ["CALL", null, ["callee:00c57af0:8"]]
+ 0045a6a8 ["INT_ADD", "register:40f0:8", ["const:45a6a8:8", "const:4:8"]]
+ 0045a6a8 ["CALL", null, ["callee:00c57af0:8"]]
- 00437810 bytes 248e1e94
+ 0045a6a8 bytes 12f51f94
- 00437818 ["INT_ADD", "register:40f0:8", ["const:437818:8", "const:4:8"]]
- 00437818 ["CALL", null, ["callee:00c57f10:8"]]
+ 0045a6b0 ["INT_ADD", "register:40f0:8", ["const:45a6b0:8", "const:4:8"]]
+ 0045a6b0 ["CALL", null, ["callee:00c57f10:8"]]
- 00437818 bytes 2a8f1e94
+ 0045a6b0 bytes 18f61f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dbaa87947241c6663977845349f9f33"></a>

### [`0043785c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/0043785c.md) → [`0045a6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a6f4.md) FUN_0045a6f4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0045a708",
      "incomplete_value": false,
      "site": "0045a70c",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437870",
      "incomplete_value": false,
      "site": "00437874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "0045a70c",
      "DATA",
      [
        "storage",
        "00be6940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045a70c",
      "DATA",
      [
        "storage",
        "00c63500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/0043785c.md#insn-00437868) · [`0043786c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/0043785c.md#insn-0043786c) · [`00437870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/0043785c.md#insn-00437870)
- 新版 [`0045a700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a6f4.md#insn-0045a700) · [`0045a704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a6f4.md#insn-0045a704) · [`0045a708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a6f4.md#insn-0045a708)

~~~diff
- 00437868 ["INT_ADD", "register:40f0:8", ["const:437868:8", "const:4:8"]]
- 00437868 ["CALL", null, ["callee:00c57a90:8"]]
+ 0045a700 ["INT_ADD", "register:40f0:8", ["const:45a700:8", "const:4:8"]]
+ 0045a700 ["CALL", null, ["callee:00c57a90:8"]]
- 00437868 bytes f68d1e94
+ 0045a700 bytes e4f41f94
- 0043786c ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045a704 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0043786c bytes 683d00f0
+ 0045a704 bytes 484000b0
- 00437870 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00437870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045a708 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0045a708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437870 bytes 08012591
+ 0045a708 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da1a8b7b224817638c1b1c74a07b2436"></a>

### [`00437880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437880.md) → [`0045a718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a718.md) FUN_0045a718

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0045a71c",
      "incomplete_value": false,
      "site": "0045a720",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437884",
      "incomplete_value": false,
      "site": "00437888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "0045a720",
      "DATA",
      [
        "storage",
        "00be6940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045a720",
      "DATA",
      [
        "storage",
        "00c63500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437880.md#insn-00437880) · [`00437884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437880.md#insn-00437884)
- 新版 [`0045a718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a718.md#insn-0045a718) · [`0045a71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a718.md#insn-0045a71c)

~~~diff
- 00437880 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045a718 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00437880 bytes 683d00f0
+ 0045a718 bytes 484000b0
- 00437884 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00437884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045a71c ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0045a71c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a71c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a71c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437884 bytes 08012591
+ 0045a71c bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ddea9ed0beeec321e6605ee77d0485a"></a>

### [`00437898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437898.md) → [`0045a730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a730.md) FUN_0045a730

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.72% / 新版 91.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0045a85c",
      "incomplete_value": true,
      "site": "0045a85c",
      "value": [
        "LOAD",
        "8",
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004379c4",
      "incomplete_value": true,
      "site": "004379c4",
      "value": [
        "LOAD",
        "8",
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045a850",
      "incomplete_value": true,
      "site": "0045a85c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:698:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004379b8",
      "incomplete_value": true,
      "site": "004379c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0045a8cc",
      "incomplete_value": true,
      "site": "0045a8cc",
      "value": [
        "LOAD",
        "8",
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
                "const:58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437a34",
      "incomplete_value": true,
      "site": "00437a34",
      "value": [
        "LOAD",
        "8",
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
                "const:58:8"
              ]
            ]
          ]
        ]
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
      "0045a840",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045a850",
      "READ",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined8"
      ]
    ],
    [
      "0045a86c",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0045a840",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045a850",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "0045a86c",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004379c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437898.md#insn-004379c4) · [`00437a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437898.md#insn-00437a34) · [`00437aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437898.md#insn-00437aa0)
- 新版 [`0045a85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a730.md#insn-0045a85c) · [`0045a8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a730.md#insn-0045a8cc) · [`0045a938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a730.md#insn-0045a938)

~~~diff
- 004379c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004379c4 ["INT_ADD", "register:40f0:8", ["const:4379c4:8", "const:4:8"]]
- 004379c4 ["CALLIND", null, ["register:0:8"]]
+ 0045a85c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a85c ["INT_ADD", "register:40f0:8", ["const:45a85c:8", "const:4:8"]]
+ 0045a85c ["CALLIND", null, ["register:0:8"]]
- 004379c4 bytes 00013fd6
+ 0045a85c bytes 00013fd6
- 00437a34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00437a34 ["INT_ADD", "register:40f0:8", ["const:437a34:8", "const:4:8"]]
- 00437a34 ["CALLIND", null, ["register:0:8"]]
+ 0045a8cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a8cc ["INT_ADD", "register:40f0:8", ["const:45a8cc:8", "const:4:8"]]
+ 0045a8cc ["CALLIND", null, ["register:0:8"]]
- 00437a34 bytes 00013fd6
+ 0045a8cc bytes 00013fd6
- 00437aa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00437aa0 ["INT_ADD", "register:40f0:8", ["const:437aa0:8", "const:4:8"]]
- 00437aa0 ["CALLIND", null, ["register:0:8"]]
+ 0045a938 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a938 ["INT_ADD", "register:40f0:8", ["const:45a938:8", "const:4:8"]]
+ 0045a938 ["CALLIND", null, ["register:0:8"]]
- 00437aa0 bytes 00013fd6
+ 0045a938 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b75b7b7da93fde326876049cd09f017"></a>

### [`00437bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bb4.md) → [`0045aa4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa4c.md) FUN_0045aa4c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0042eef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eef4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00451d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451d8c.md)

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
      "definition_site": "0045aa54",
      "incomplete_value": false,
      "site": "0045aa54",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437bbc",
      "incomplete_value": false,
      "site": "00437bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "0045aa54",
      "DATA",
      [
        "storage",
        "00be69c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045aa54",
      "DATA",
      [
        "storage",
        "00c63580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bb4.md#insn-00437bb4) · [`00437bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bb4.md#insn-00437bb8)
- 新版 [`0045aa4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa4c.md#insn-0045aa4c) · [`0045aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa4c.md#insn-0045aa50)

~~~diff
- 00437bb4 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045aa4c ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00437bb4 bytes 683d00f0
+ 0045aa4c bytes 484000b0
- 00437bb8 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00437bb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437bb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437bb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045aa50 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 0045aa50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aa50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aa50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437bb8 bytes 08012791
+ 0045aa50 bytes 08011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52193798d600121d9a74ad1e5274f9f1"></a>

### [`00437bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bc4.md) → [`0045aa5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa5c.md) FUN_0045aa5c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0042eef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eef4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00451d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451d8c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0045aa74",
      "incomplete_value": false,
      "site": "0045aa74",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437bdc",
      "incomplete_value": false,
      "site": "00437bdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "0045aa74",
      "DATA",
      [
        "storage",
        "00be69c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045aa74",
      "DATA",
      [
        "storage",
        "00c63580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bc4.md#insn-00437bd0) · [`00437bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bc4.md#insn-00437bd4) · [`00437be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bc4.md#insn-00437be0)
- 新版 [`0045aa68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa5c.md#insn-0045aa68) · [`0045aa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa5c.md#insn-0045aa6c) · [`0045aa78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa5c.md#insn-0045aa78)

~~~diff
- 00437bd0 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045aa68 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00437bd0 bytes 683d00f0
+ 0045aa68 bytes 484000b0
- 00437bd4 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00437bd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437bd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045aa6c ["COPY", "tmp:0:8", ["const:580:8"]]
+ 0045aa6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aa6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aa6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437bd4 bytes 08012791
+ 0045aa6c bytes 08011691
- 00437be0 ["INT_ADD", "register:40f0:8", ["const:437be0:8", "const:4:8"]]
- 00437be0 ["CALL", null, ["callee:00451d8c:8"]]
+ 0045aa78 ["INT_ADD", "register:40f0:8", ["const:45aa78:8", "const:4:8"]]
+ 0045aa78 ["CALL", null, ["callee:00451d8c:8"]]
- 00437be0 bytes c5dcff97
+ 0045aa78 bytes c5dcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c16e66d47411b14df76fd914f3932bc1"></a>

### [`00437bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bf4.md) → [`0045aa8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa8c.md) FUN_0045aa8c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00438418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438418.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b2b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0045aab0",
      "incomplete_value": false,
      "site": "0045aab0",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437c18",
      "incomplete_value": false,
      "site": "00437c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "0045aab0",
      "DATA",
      [
        "storage",
        "00be69c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045aab0",
      "DATA",
      [
        "storage",
        "00c63580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bf4.md#insn-00437c08) · [`00437c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bf4.md#insn-00437c10) · [`00437c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bf4.md#insn-00437c14)
- 新版 [`0045aaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa8c.md#insn-0045aaa0) · [`0045aaa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa8c.md#insn-0045aaa8) · [`0045aaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa8c.md#insn-0045aaac)

~~~diff
- 00437c08 ["INT_ADD", "register:40f0:8", ["const:437c08:8", "const:4:8"]]
- 00437c08 ["CALL", null, ["callee:00c57a90:8"]]
+ 0045aaa0 ["INT_ADD", "register:40f0:8", ["const:45aaa0:8", "const:4:8"]]
+ 0045aaa0 ["CALL", null, ["callee:00c57a90:8"]]
- 00437c08 bytes 0e8d1e94
+ 0045aaa0 bytes fcf31f94
- 00437c10 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0045aaa8 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00437c10 bytes 683d00f0
+ 0045aaa8 bytes 484000b0
- 00437c14 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00437c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045aaac ["COPY", "tmp:0:8", ["const:580:8"]]
+ 0045aaac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aaac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aaac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437c14 bytes 08012791
+ 0045aaac bytes 08011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7e4972c583091683bdab8b996620b00"></a>

### [`00437c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437c48.md) → [`0045aae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aae0.md) FUN_0045aae0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00438418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438418.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b2b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045aaec",
      "incomplete_value": false,
      "site": "0045aaec",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437c54",
      "incomplete_value": false,
      "site": "00437c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "0045aaec",
      "DATA",
      [
        "storage",
        "00be69c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045aaec",
      "DATA",
      [
        "storage",
        "00c63580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437c48.md#insn-00437c4c) · [`00437c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437c48.md#insn-00437c50)
- 新版 [`0045aae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aae0.md#insn-0045aae4) · [`0045aae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aae0.md#insn-0045aae8)

~~~diff
- 00437c4c ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0045aae4 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 00437c4c bytes 693d00f0
+ 0045aae4 bytes 494000b0
- 00437c50 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00437c50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00437c50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00437c50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045aae8 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 0045aae8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045aae8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045aae8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00437c50 bytes 29012791
+ 0045aae8 bytes 29011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25b5ebc6b8ebbaff04b20ced12389ed7"></a>

### [`00437c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437c94.md) → [`0045ab2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045ab2c.md) FUN_0045ab2c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042d878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d878.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`004389d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/004389d4.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00450710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0045b86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b86c.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 95.79% / 新版 95.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件, `store_value` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045ae14",
      "incomplete_value": false,
      "site": "0045ae14",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437f7c",
      "incomplete_value": false,
      "site": "00437f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045ac4c",
      "value": [
        "leaf",
        "ram:769084:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00437db4",
      "value": [
        "leaf",
        "ram:73ed78:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00437db8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045ac4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073ed78"
      ]
    ],
    [
      "unmatched:00437db8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "0045acac",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0045ac4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00769084"
      ]
    ],
    [
      "0045ac50",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "0045acac",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437c94.md#insn-00437db4) · [`00437db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437c94.md#insn-00437db8) · [`00437e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437c94.md#insn-00437e1c)
- 新版 [`0045ac4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045ab2c.md#insn-0045ac4c)

~~~diff
- 00437db4 ["INT_ADD", "register:40f0:8", ["const:437db4:8", "const:4:8"]]
- 00437db4 ["CALL", null, ["ram:73ed78:8"]]
+ 0045ac4c ["INT_ADD", "register:40f0:8", ["const:45ac4c:8", "const:4:8"]]
+ 0045ac4c ["CALL", null, ["ram:769084:8"]]
- 00437db4 bytes f11b0c94
+ 0045ac4c bytes 0e390c94
- 00437db8 ["INT_ADD", "register:40f0:8", ["const:437db8:8", "const:4:8"]]
- 00437db8 ["CALL", null, ["callee:008514b8:8"]]
- 00437db8 bytes f29d0f94
- 00437e1c ["INT_ADD", "register:40f0:8", ["const:437e1c:8", "const:4:8"]]
- 00437e1c ["CALL", null, ["callee:008514b8:8"]]
- 00437e1c bytes d99d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

