# v15.7.4 → v16.0.0 · 最優先の変更候補 (4)

[一覧の目次](README.md)

<a id="compare-5b17655bd56d739937a901c7b4ee2ff2"></a>

### [`00440ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440ad4.md) → [`0046396c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046396c.md) FUN_0046396c

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
      "definition_site": "00463988",
      "incomplete_value": false,
      "site": "00463988",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00440af0",
      "incomplete_value": false,
      "site": "00440af0",
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
            "const:658:8"
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
      "00463988",
      "DATA",
      [
        "storage",
        "00be7658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463988",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440ad4.md#insn-00440ae8) · [`00440aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440ad4.md#insn-00440aec) · [`00440b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440ad4.md#insn-00440b10)
- 新版 [`00463980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046396c.md#insn-00463980) · [`00463984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046396c.md#insn-00463984) · [`004639a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046396c.md#insn-004639a8)

~~~diff
- 00440ae8 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 00463980 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00440ae8 bytes 293d00f0
+ 00463980 bytes 094000b0
- 00440aec ["COPY", "tmp:0:8", ["const:658:8"]]
- 00440aec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00440aec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00440aec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00463984 ["COPY", "tmp:0:8", ["const:218:8"]]
+ 00463984 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00463984 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00463984 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00440aec bytes 29611991
+ 00463984 bytes 29610891
- 00440b10 ["COPY", "register:0:8", ["register:4048:8"]]
- 00440b10 ["INT_ADD", "register:40f0:8", ["const:440b10:8", "const:4:8"]]
- 00440b10 ["CALLIND", null, ["register:0:8"]]
+ 004639a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004639a8 ["INT_ADD", "register:40f0:8", ["const:4639a8:8", "const:4:8"]]
+ 004639a8 ["CALLIND", null, ["register:0:8"]]
- 00440b10 bytes 20013fd6
+ 004639a8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eb2ae711ad124bc26b112018662a7c5"></a>

### [`00440c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440c6c.md) → [`00463b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463b04.md) FUN_00463b04

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
      "definition_site": "00463b10",
      "incomplete_value": false,
      "site": "00463b1c",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00440c78",
      "incomplete_value": false,
      "site": "00440c84",
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
            "const:6d8:8"
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
      "00463b1c",
      "DATA",
      [
        "storage",
        "00be76d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463b1c",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440c6c.md#insn-00440c74) · [`00440c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440c6c.md#insn-00440c78)
- 新版 [`00463b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463b04.md#insn-00463b0c) · [`00463b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463b04.md#insn-00463b10)

~~~diff
- 00440c74 ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 00463b0c ["COPY", "register:4050:8", ["const:c64000:8"]]
- 00440c74 bytes 2a3d00f0
+ 00463b0c bytes 0a4000b0
- 00440c78 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 00440c78 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00440c78 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00440c78 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00463b10 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00463b10 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00463b10 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00463b10 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00440c78 bytes 4a611b91
+ 00463b10 bytes 4a610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e5f373240fe09f6084422a5363c5d91"></a>

### [`00440cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440cb0.md) → [`00463b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463b48.md) FUN_00463b48

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
      "definition_site": "00463b60",
      "incomplete_value": false,
      "site": "00463b6c",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00440cc8",
      "incomplete_value": false,
      "site": "00440cd4",
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
            "const:6d8:8"
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
      "00463b6c",
      "DATA",
      [
        "storage",
        "00be76d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463b6c",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440cb0.md#insn-00440cc4) · [`00440cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440cb0.md#insn-00440cc8) · [`00440cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440cb0.md#insn-00440cf8)
- 新版 [`00463b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463b48.md#insn-00463b5c) · [`00463b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463b48.md#insn-00463b60) · [`00463b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463b48.md#insn-00463b90)

~~~diff
- 00440cc4 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00463b5c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00440cc4 bytes 283d00f0
+ 00463b5c bytes 084000b0
- 00440cc8 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 00440cc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00440cc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00440cc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463b60 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00463b60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463b60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463b60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00440cc8 bytes 08611b91
+ 00463b60 bytes 08610a91
- 00440cf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00440cf8 ["INT_ADD", "register:40f0:8", ["const:440cf8:8", "const:4:8"]]
- 00440cf8 ["CALLIND", null, ["register:0:8"]]
+ 00463b90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463b90 ["INT_ADD", "register:40f0:8", ["const:463b90:8", "const:4:8"]]
+ 00463b90 ["CALLIND", null, ["register:0:8"]]
- 00440cf8 bytes 00013fd6
+ 00463b90 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a83cddc7e1e1286e202aa3c8f6e6f7e"></a>

### [`00440d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440d0c.md) → [`00463ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463ba4.md) FUN_00463ba4

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
      "definition_site": "00463bd0",
      "incomplete_value": false,
      "site": "00463bd0",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00440d38",
      "incomplete_value": false,
      "site": "00440d38",
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
            "const:6d8:8"
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
      "00463bd0",
      "DATA",
      [
        "storage",
        "00be76d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463bd0",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440d0c.md#insn-00440d20) · [`00440d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440d0c.md#insn-00440d2c) · [`00440d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440d0c.md#insn-00440d30)
- 新版 [`00463bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463ba4.md#insn-00463bb8) · [`00463bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463ba4.md#insn-00463bc4) · [`00463bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463ba4.md#insn-00463bc8)

~~~diff
- 00440d20 ["INT_ADD", "register:40f0:8", ["const:440d20:8", "const:4:8"]]
- 00440d20 ["CALL", null, ["callee:00c57a90:8"]]
+ 00463bb8 ["INT_ADD", "register:40f0:8", ["const:463bb8:8", "const:4:8"]]
+ 00463bb8 ["CALL", null, ["callee:00c57a90:8"]]
- 00440d20 bytes c8681e94
+ 00463bb8 bytes b6cf1f94
- 00440d2c ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00463bc4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00440d2c bytes 283d00f0
+ 00463bc4 bytes 084000b0
- 00440d30 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 00440d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00440d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00440d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463bc8 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00463bc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463bc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463bc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00440d30 bytes 08611b91
+ 00463bc8 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3463149a460e23ad314300930a65d6c1"></a>

### [`00440d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440d94.md) → [`00463c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463c2c.md) FUN_00463c2c

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
      "definition_site": "00463c48",
      "incomplete_value": false,
      "site": "00463c48",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00440db0",
      "incomplete_value": false,
      "site": "00440db0",
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
            "const:6d8:8"
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
      "00463c48",
      "DATA",
      [
        "storage",
        "00be76d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463c48",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440d94.md#insn-00440da8) · [`00440dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440d94.md#insn-00440dac) · [`00440dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440d94.md#insn-00440dd0)
- 新版 [`00463c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463c2c.md#insn-00463c40) · [`00463c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463c2c.md#insn-00463c44) · [`00463c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463c2c.md#insn-00463c68)

~~~diff
- 00440da8 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 00463c40 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00440da8 bytes 293d00f0
+ 00463c40 bytes 094000b0
- 00440dac ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 00440dac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00440dac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00440dac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00463c44 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00463c44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00463c44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00463c44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00440dac bytes 29611b91
+ 00463c44 bytes 29610a91
- 00440dd0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00440dd0 ["INT_ADD", "register:40f0:8", ["const:440dd0:8", "const:4:8"]]
- 00440dd0 ["CALLIND", null, ["register:0:8"]]
+ 00463c68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00463c68 ["INT_ADD", "register:40f0:8", ["const:463c68:8", "const:4:8"]]
+ 00463c68 ["CALLIND", null, ["register:0:8"]]
- 00440dd0 bytes 20013fd6
+ 00463c68 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-792596664c5042e89f3715e9787e739b"></a>

### [`00440f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440f2c.md) → [`00463dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463dc4.md) FUN_00463dc4

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
      "definition_site": "00463dd0",
      "incomplete_value": false,
      "site": "00463ddc",
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
      "definition_site": "00440f38",
      "incomplete_value": false,
      "site": "00440f44",
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
      "00463ddc",
      "DATA",
      [
        "storage",
        "00be7758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463ddc",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440f2c.md#insn-00440f34) · [`00440f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440f2c.md#insn-00440f38)
- 新版 [`00463dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463dc4.md#insn-00463dcc) · [`00463dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463dc4.md#insn-00463dd0)

~~~diff
- 00440f34 ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 00463dcc ["COPY", "register:4050:8", ["const:c64000:8"]]
- 00440f34 bytes 2a3d00f0
+ 00463dcc bytes 0a4000b0
- 00440f38 ["COPY", "tmp:0:8", ["const:758:8"]]
- 00440f38 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00440f38 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00440f38 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00463dd0 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 00463dd0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00463dd0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00463dd0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00440f38 bytes 4a611d91
+ 00463dd0 bytes 4a610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d6cf3f490c013289203e42bfede6c65"></a>

### [`00440f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440f70.md) → [`00463e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e08.md) FUN_00463e08

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
      "definition_site": "00463e20",
      "incomplete_value": false,
      "site": "00463e2c",
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
      "definition_site": "00440f88",
      "incomplete_value": false,
      "site": "00440f94",
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
      "00463e2c",
      "DATA",
      [
        "storage",
        "00be7758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463e2c",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440f70.md#insn-00440f84) · [`00440f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440f70.md#insn-00440f88) · [`00440fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440f70.md#insn-00440fb8)
- 新版 [`00463e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e08.md#insn-00463e1c) · [`00463e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e08.md#insn-00463e20) · [`00463e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e08.md#insn-00463e50)

~~~diff
- 00440f84 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00463e1c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00440f84 bytes 283d00f0
+ 00463e1c bytes 084000b0
- 00440f88 ["COPY", "tmp:0:8", ["const:758:8"]]
- 00440f88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00440f88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00440f88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463e20 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 00463e20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463e20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463e20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00440f88 bytes 08611d91
+ 00463e20 bytes 08610c91
- 00440fb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00440fb8 ["INT_ADD", "register:40f0:8", ["const:440fb8:8", "const:4:8"]]
- 00440fb8 ["CALLIND", null, ["register:0:8"]]
+ 00463e50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463e50 ["INT_ADD", "register:40f0:8", ["const:463e50:8", "const:4:8"]]
+ 00463e50 ["CALLIND", null, ["register:0:8"]]
- 00440fb8 bytes 00013fd6
+ 00463e50 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af69c8dfe4def14efbea10c804bbca0f"></a>

### [`00440fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440fcc.md) → [`00463e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e64.md) FUN_00463e64

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
      "definition_site": "00463e90",
      "incomplete_value": false,
      "site": "00463e90",
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
      "definition_site": "00440ff8",
      "incomplete_value": false,
      "site": "00440ff8",
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
      "00463e90",
      "DATA",
      [
        "storage",
        "00be7758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463e90",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440fcc.md#insn-00440fe0) · [`00440fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440fcc.md#insn-00440fec) · [`00440ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00440/00440fcc.md#insn-00440ff0)
- 新版 [`00463e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e64.md#insn-00463e78) · [`00463e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e64.md#insn-00463e84) · [`00463e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e64.md#insn-00463e88)

~~~diff
- 00440fe0 ["INT_ADD", "register:40f0:8", ["const:440fe0:8", "const:4:8"]]
- 00440fe0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00463e78 ["INT_ADD", "register:40f0:8", ["const:463e78:8", "const:4:8"]]
+ 00463e78 ["CALL", null, ["callee:00c57a90:8"]]
- 00440fe0 bytes 18681e94
+ 00463e78 bytes 06cf1f94
- 00440fec ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00463e84 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00440fec bytes 283d00f0
+ 00463e84 bytes 084000b0
- 00440ff0 ["COPY", "tmp:0:8", ["const:758:8"]]
- 00440ff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00440ff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00440ff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463e88 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 00463e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00440ff0 bytes 08611d91
+ 00463e88 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae24ce9339225f6d00aa44b251b65349"></a>

### [`00441054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441054.md) → [`00463eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463eec.md) FUN_00463eec

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
      "definition_site": "00463f08",
      "incomplete_value": false,
      "site": "00463f08",
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
      "definition_site": "00441070",
      "incomplete_value": false,
      "site": "00441070",
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
      "00463f08",
      "DATA",
      [
        "storage",
        "00be7758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463f08",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00441068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441054.md#insn-00441068) · [`0044106c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441054.md#insn-0044106c) · [`00441090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441054.md#insn-00441090)
- 新版 [`00463f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463eec.md#insn-00463f00) · [`00463f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463eec.md#insn-00463f04) · [`00463f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463eec.md#insn-00463f28)

~~~diff
- 00441068 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 00463f00 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00441068 bytes 293d00d0
+ 00463f00 bytes 094000b0
- 0044106c ["COPY", "tmp:0:8", ["const:758:8"]]
- 0044106c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0044106c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0044106c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00463f04 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 00463f04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00463f04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00463f04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0044106c bytes 29611d91
+ 00463f04 bytes 29610c91
- 00441090 ["COPY", "register:0:8", ["register:4048:8"]]
- 00441090 ["INT_ADD", "register:40f0:8", ["const:441090:8", "const:4:8"]]
- 00441090 ["CALLIND", null, ["register:0:8"]]
+ 00463f28 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00463f28 ["INT_ADD", "register:40f0:8", ["const:463f28:8", "const:4:8"]]
+ 00463f28 ["CALLIND", null, ["register:0:8"]]
- 00441090 bytes 20013fd6
+ 00463f28 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4889efbe42eb59f1a697100557a64ceb"></a>

### [`00441150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441150.md) → [`00463fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463fe8.md) FUN_00463fe8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0043eba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043eba8.md) [`004418c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004418c4.md) [`004419a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004419a0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00461a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md) [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md) [`00464838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464838.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.54% / 新版 95.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004642c0",
      "incomplete_value": true,
      "site": "004642c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00441428",
      "incomplete_value": true,
      "site": "00441428",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 60,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004642b4",
      "incomplete_value": true,
      "site": "004642c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044141c",
      "incomplete_value": true,
      "site": "0044142c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 61,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046434c",
      "incomplete_value": true,
      "site": "00464358",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:583:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004414b4",
      "incomplete_value": true,
      "site": "004414c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:92a:8"
              ]
            ]
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
      "004642b0",
      "READ",
      [
        "storage",
        "00298c29",
        null,
        "string"
      ]
    ],
    [
      "004642b4",
      "READ",
      [
        "storage",
        "00298c30",
        null,
        "string"
      ]
    ],
    [
      "0046434c",
      "READ",
      [
        "storage",
        "0029792a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00464128",
      "DATA",
      [
        "storage",
        "0079656b",
        null,
        null
      ]
    ],
    [
      "004642b0",
      "READ",
      [
        "storage",
        "002a89e7",
        null,
        "string"
      ]
    ],
    [
      "004642b4",
      "READ",
      [
        "storage",
        "002a89ee",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004411b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441150.md#insn-004411b8) · [`004411e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441150.md#insn-004411e4) · [`00441228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441150.md#insn-00441228)
- 新版 [`00464050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463fe8.md#insn-00464050) · [`0046407c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463fe8.md#insn-0046407c) · [`004640c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463fe8.md#insn-004640c0)

~~~diff
- 004411b8 ["INT_ADD", "register:40f0:8", ["const:4411b8:8", "const:4:8"]]
- 004411b8 ["CALL", null, ["callee:0044104c:8"]]
+ 00464050 ["INT_ADD", "register:40f0:8", ["const:464050:8", "const:4:8"]]
+ 00464050 ["CALL", null, ["callee:0044104c:8"]]
- 004411b8 bytes e574ff97
+ 00464050 bytes ff73ff97
- 004411e4 ["INT_ADD", "register:40f0:8", ["const:4411e4:8", "const:4:8"]]
- 004411e4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0046407c ["INT_ADD", "register:40f0:8", ["const:46407c:8", "const:4:8"]]
+ 0046407c ["CALL", null, ["callee:00c57ab0:8"]]
- 004411e4 bytes 9f671e94
+ 0046407c bytes 8dce1f94
- 00441228 ["INT_ADD", "register:40f0:8", ["const:441228:8", "const:4:8"]]
- 00441228 ["CALL", null, ["callee:0044104c:8"]]
+ 004640c0 ["INT_ADD", "register:40f0:8", ["const:4640c0:8", "const:4:8"]]
+ 004640c0 ["CALL", null, ["callee:0044104c:8"]]
- 00441228 bytes c974ff97
+ 004640c0 bytes e373ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9998897d37e8eb8df7cecc43452114ea"></a>

### [`00441c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441c30.md) → [`00464ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ac8.md) FUN_00464ac8

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
      "definition_site": "00464ad4",
      "incomplete_value": false,
      "site": "00464ae0",
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
      "definition_site": "00441c3c",
      "incomplete_value": false,
      "site": "00441c48",
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
      "00464ae0",
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
      "00464ae0",
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

- 旧版 [`00441c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441c30.md#insn-00441c38) · [`00441c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441c30.md#insn-00441c3c)
- 新版 [`00464ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ac8.md#insn-00464ad0) · [`00464ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ac8.md#insn-00464ad4)

~~~diff
- 00441c38 ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 00464ad0 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 00441c38 bytes 2a3d00d0
+ 00464ad0 bytes 0a400090
- 00441c3c ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00441c3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00441c3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00441c3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00464ad4 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 00464ad4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00464ad4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00464ad4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00441c3c bytes 4a611f91
+ 00464ad4 bytes 4a610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c071c1db672fe56f1695ec2dae536dc"></a>

### [`00441c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441c74.md) → [`00464b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b0c.md) FUN_00464b0c

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
      "definition_site": "00464b24",
      "incomplete_value": false,
      "site": "00464b30",
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
      "definition_site": "00441c8c",
      "incomplete_value": false,
      "site": "00441c98",
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
      "00464b30",
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
      "00464b30",
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

- 旧版 [`00441c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441c74.md#insn-00441c88) · [`00441c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441c74.md#insn-00441c8c) · [`00441cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441c74.md#insn-00441cbc)
- 新版 [`00464b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b0c.md#insn-00464b20) · [`00464b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b0c.md#insn-00464b24) · [`00464b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b0c.md#insn-00464b54)

~~~diff
- 00441c88 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00464b20 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00441c88 bytes 283d00d0
+ 00464b20 bytes 08400090
- 00441c8c ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00441c8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00441c8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00441c8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00464b24 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 00464b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00464b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00464b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00441c8c bytes 08611f91
+ 00464b24 bytes 08610e91
- 00441cbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00441cbc ["INT_ADD", "register:40f0:8", ["const:441cbc:8", "const:4:8"]]
- 00441cbc ["CALLIND", null, ["register:0:8"]]
+ 00464b54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464b54 ["INT_ADD", "register:40f0:8", ["const:464b54:8", "const:4:8"]]
+ 00464b54 ["CALLIND", null, ["register:0:8"]]
- 00441cbc bytes 00013fd6
+ 00464b54 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06b767d7d5b0b0fd7b4a957d5420e967"></a>

### [`00441cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441cd0.md) → [`00464b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b68.md) FUN_00464b68

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
      "definition_site": "00464b94",
      "incomplete_value": false,
      "site": "00464b94",
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
      "definition_site": "00441cfc",
      "incomplete_value": false,
      "site": "00441cfc",
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
      "00464b94",
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
      "00464b94",
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

- 旧版 [`00441ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441cd0.md#insn-00441ce4) · [`00441cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441cd0.md#insn-00441cf0) · [`00441cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441cd0.md#insn-00441cf4)
- 新版 [`00464b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b68.md#insn-00464b7c) · [`00464b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b68.md#insn-00464b88) · [`00464b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b68.md#insn-00464b8c)

~~~diff
- 00441ce4 ["INT_ADD", "register:40f0:8", ["const:441ce4:8", "const:4:8"]]
- 00441ce4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00464b7c ["INT_ADD", "register:40f0:8", ["const:464b7c:8", "const:4:8"]]
+ 00464b7c ["CALL", null, ["callee:00c57a90:8"]]
- 00441ce4 bytes d7641e94
+ 00464b7c bytes c5cb1f94
- 00441cf0 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00464b88 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00441cf0 bytes 283d00d0
+ 00464b88 bytes 08400090
- 00441cf4 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00441cf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00441cf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00441cf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00464b8c ["COPY", "tmp:0:8", ["const:398:8"]]
+ 00464b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00464b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00464b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00441cf4 bytes 08611f91
+ 00464b8c bytes 08610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3996e012373749f046354dc831dc5b0b"></a>

### [`00441d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441d58.md) → [`00464bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464bf0.md) FUN_00464bf0

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
      "definition_site": "00464c0c",
      "incomplete_value": false,
      "site": "00464c0c",
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
      "definition_site": "00441d74",
      "incomplete_value": false,
      "site": "00441d74",
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
      "00464c0c",
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
      "00464c0c",
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

- 旧版 [`00441d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441d58.md#insn-00441d6c) · [`00441d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441d58.md#insn-00441d70) · [`00441d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441d58.md#insn-00441d94)
- 新版 [`00464c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464bf0.md#insn-00464c04) · [`00464c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464bf0.md#insn-00464c08) · [`00464c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464bf0.md#insn-00464c2c)

~~~diff
- 00441d6c ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 00464c04 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00441d6c bytes 293d00d0
+ 00464c04 bytes 09400090
- 00441d70 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00441d70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00441d70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00441d70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00464c08 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 00464c08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00464c08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00464c08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00441d70 bytes 29611f91
+ 00464c08 bytes 29610e91
- 00441d94 ["COPY", "register:0:8", ["register:4048:8"]]
- 00441d94 ["INT_ADD", "register:40f0:8", ["const:441d94:8", "const:4:8"]]
- 00441d94 ["CALLIND", null, ["register:0:8"]]
+ 00464c2c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00464c2c ["INT_ADD", "register:40f0:8", ["const:464c2c:8", "const:4:8"]]
+ 00464c2c ["CALLIND", null, ["register:0:8"]]
- 00441d94 bytes 20013fd6
+ 00464c2c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8266eaf16827e2385d704382beafe0c"></a>

### [`00441f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441f38.md) → [`00464dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464dd0.md) FUN_00464dd0

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
      "definition_site": "00464ddc",
      "incomplete_value": false,
      "site": "00464de8",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00441f44",
      "incomplete_value": false,
      "site": "00441f50",
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
            "const:858:8"
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
      "00464de8",
      "DATA",
      [
        "storage",
        "00be7858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464de8",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00441f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441f38.md#insn-00441f40) · [`00441f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441f38.md#insn-00441f44)
- 新版 [`00464dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464dd0.md#insn-00464dd8) · [`00464ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464dd0.md#insn-00464ddc)

~~~diff
- 00441f40 ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 00464dd8 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 00441f40 bytes 2a3d00d0
+ 00464dd8 bytes 0a400090
- 00441f44 ["COPY", "tmp:0:8", ["const:858:8"]]
- 00441f44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00441f44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00441f44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00464ddc ["COPY", "tmp:0:8", ["const:418:8"]]
+ 00464ddc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00464ddc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00464ddc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00441f44 bytes 4a612191
+ 00464ddc bytes 4a611091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e46b7178b7829534e4b70d0f9e079444"></a>

### [`00441f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441f7c.md) → [`00464e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e14.md) FUN_00464e14

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
      "definition_site": "00464e2c",
      "incomplete_value": false,
      "site": "00464e38",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00441f94",
      "incomplete_value": false,
      "site": "00441fa0",
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
            "const:858:8"
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
      "00464e38",
      "DATA",
      [
        "storage",
        "00be7858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464e38",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00441f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441f7c.md#insn-00441f90) · [`00441f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441f7c.md#insn-00441f94) · [`00441fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441f7c.md#insn-00441fc4)
- 新版 [`00464e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e14.md#insn-00464e28) · [`00464e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e14.md#insn-00464e2c) · [`00464e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e14.md#insn-00464e5c)

~~~diff
- 00441f90 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00464e28 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00441f90 bytes 283d00d0
+ 00464e28 bytes 08400090
- 00441f94 ["COPY", "tmp:0:8", ["const:858:8"]]
- 00441f94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00441f94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00441f94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00464e2c ["COPY", "tmp:0:8", ["const:418:8"]]
+ 00464e2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00464e2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00464e2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00441f94 bytes 08612191
+ 00464e2c bytes 08611091
- 00441fc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00441fc4 ["INT_ADD", "register:40f0:8", ["const:441fc4:8", "const:4:8"]]
- 00441fc4 ["CALLIND", null, ["register:0:8"]]
+ 00464e5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464e5c ["INT_ADD", "register:40f0:8", ["const:464e5c:8", "const:4:8"]]
+ 00464e5c ["CALLIND", null, ["register:0:8"]]
- 00441fc4 bytes 00013fd6
+ 00464e5c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5875008a69de6415683819ef5c60eae1"></a>

### [`00441fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441fd8.md) → [`00464e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e70.md) FUN_00464e70

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
      "definition_site": "00464e9c",
      "incomplete_value": false,
      "site": "00464e9c",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00442004",
      "incomplete_value": false,
      "site": "00442004",
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
            "const:858:8"
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
      "00464e9c",
      "DATA",
      [
        "storage",
        "00be7858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464e9c",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00441fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441fd8.md#insn-00441fec) · [`00441ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441fd8.md#insn-00441ff8) · [`00441ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/00441fd8.md#insn-00441ffc)
- 新版 [`00464e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e70.md#insn-00464e84) · [`00464e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e70.md#insn-00464e90) · [`00464e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e70.md#insn-00464e94)

~~~diff
- 00441fec ["INT_ADD", "register:40f0:8", ["const:441fec:8", "const:4:8"]]
- 00441fec ["CALL", null, ["callee:00c57a90:8"]]
+ 00464e84 ["INT_ADD", "register:40f0:8", ["const:464e84:8", "const:4:8"]]
+ 00464e84 ["CALL", null, ["callee:00c57a90:8"]]
- 00441fec bytes 15641e94
+ 00464e84 bytes 03cb1f94
- 00441ff8 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00464e90 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00441ff8 bytes 283d00d0
+ 00464e90 bytes 08400090
- 00441ffc ["COPY", "tmp:0:8", ["const:858:8"]]
- 00441ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00441ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00441ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00464e94 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 00464e94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00464e94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00464e94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00441ffc bytes 08612191
+ 00464e94 bytes 08611091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68181345fb4ab39832f2731012daff60"></a>

### [`00442060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442060.md) → [`00464ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ef8.md) FUN_00464ef8

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
      "definition_site": "00464f14",
      "incomplete_value": false,
      "site": "00464f14",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044207c",
      "incomplete_value": false,
      "site": "0044207c",
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
            "const:858:8"
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
      "00464f14",
      "DATA",
      [
        "storage",
        "00be7858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464f14",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00442074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442060.md#insn-00442074) · [`00442078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442060.md#insn-00442078) · [`0044209c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442060.md#insn-0044209c)
- 新版 [`00464f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ef8.md#insn-00464f0c) · [`00464f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ef8.md#insn-00464f10) · [`00464f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ef8.md#insn-00464f34)

~~~diff
- 00442074 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 00464f0c ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00442074 bytes 293d00b0
+ 00464f0c bytes 09400090
- 00442078 ["COPY", "tmp:0:8", ["const:858:8"]]
- 00442078 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00442078 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00442078 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00464f10 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 00464f10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00464f10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00464f10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00442078 bytes 29612191
+ 00464f10 bytes 29611091
- 0044209c ["COPY", "register:0:8", ["register:4048:8"]]
- 0044209c ["INT_ADD", "register:40f0:8", ["const:44209c:8", "const:4:8"]]
- 0044209c ["CALLIND", null, ["register:0:8"]]
+ 00464f34 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00464f34 ["INT_ADD", "register:40f0:8", ["const:464f34:8", "const:4:8"]]
+ 00464f34 ["CALLIND", null, ["register:0:8"]]
- 0044209c bytes 20013fd6
+ 00464f34 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26dd95d9d57f925b3ef7ca1859edbfa5"></a>

### [`00442238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442238.md) → [`004650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004650d0.md) FUN_004650d0

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
      "definition_site": "004650e4",
      "incomplete_value": false,
      "site": "004650e8",
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
      "definition_site": "0044224c",
      "incomplete_value": false,
      "site": "00442250",
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
      "004650e8",
      "DATA",
      [
        "storage",
        "00be78d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004650e8",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00442244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442238.md#insn-00442244) · [`00442248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442238.md#insn-00442248) · [`0044224c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442238.md#insn-0044224c)
- 新版 [`004650dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004650d0.md#insn-004650dc) · [`004650e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004650d0.md#insn-004650e0) · [`004650e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004650d0.md#insn-004650e4)

~~~diff
- 00442244 ["INT_ADD", "register:40f0:8", ["const:442244:8", "const:4:8"]]
- 00442244 ["CALL", null, ["callee:00c57a90:8"]]
+ 004650dc ["INT_ADD", "register:40f0:8", ["const:4650dc:8", "const:4:8"]]
+ 004650dc ["CALL", null, ["callee:00c57a90:8"]]
- 00442244 bytes 7f631e94
+ 004650dc bytes 6dca1f94
- 00442248 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004650e0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00442248 bytes 283d00b0
+ 004650e0 bytes e83f00f0
- 0044224c ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 0044224c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044224c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044224c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004650e4 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 004650e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004650e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004650e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044224c bytes 08612391
+ 004650e4 bytes 08611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9afc3c5016c490630837c1e21022b848"></a>

### [`0044225c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044225c.md) → [`004650f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004650f4.md) FUN_004650f4

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
      "definition_site": "004650f8",
      "incomplete_value": false,
      "site": "004650fc",
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
      "definition_site": "00442260",
      "incomplete_value": false,
      "site": "00442264",
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
      "004650fc",
      "DATA",
      [
        "storage",
        "00be78d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004650fc",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044225c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044225c.md#insn-0044225c) · [`00442260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044225c.md#insn-00442260)
- 新版 [`004650f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004650f4.md#insn-004650f4) · [`004650f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004650f4.md#insn-004650f8)

~~~diff
- 0044225c ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004650f4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0044225c bytes 283d00b0
+ 004650f4 bytes e83f00f0
- 00442260 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 00442260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00442260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00442260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004650f8 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 004650f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004650f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004650f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00442260 bytes 08612391
+ 004650f8 bytes 08611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c3322594ebf4c1157238702ada62982"></a>

### [`00442274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442274.md) → [`0046510c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046510c.md) FUN_0046510c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00465140",
      "incomplete_value": false,
      "site": "00465144",
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
      "definition_site": "004422a8",
      "incomplete_value": false,
      "site": "004422ac",
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
      "definition_site": "00465150",
      "incomplete_value": false,
      "site": "00465154",
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
      "definition_site": "004422b8",
      "incomplete_value": false,
      "site": "004422bc",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046511c",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465128",
      "READ",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00465140",
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
      "0046511c",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465128",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "00465140",
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

- 旧版 [`004422ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442274.md#insn-004422ac) · [`004422bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442274.md#insn-004422bc) · [`0044227c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442274.md#insn-0044227c)
- 新版 [`00465144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046510c.md#insn-00465144) · [`00465154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046510c.md#insn-00465154) · [`00465114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046510c.md#insn-00465114)

~~~diff
- 004422ac ["INT_ADD", "register:40f0:8", ["const:4422ac:8", "const:4:8"]]
- 004422ac ["CALL", null, ["callee:00c57a50:8"]]
+ 00465144 ["INT_ADD", "register:40f0:8", ["const:465144:8", "const:4:8"]]
+ 00465144 ["CALL", null, ["callee:00c57a50:8"]]
- 004422ac bytes 55631e94
+ 00465144 bytes 43ca1f94
- 004422bc ["INT_ADD", "register:40f0:8", ["const:4422bc:8", "const:4:8"]]
- 004422bc ["CALL", null, ["callee:00c57a70:8"]]
+ 00465154 ["INT_ADD", "register:40f0:8", ["const:465154:8", "const:4:8"]]
+ 00465154 ["CALL", null, ["callee:00c57a70:8"]]
- 004422bc bytes 59631e94
+ 00465154 bytes 47ca1f94
- 0044227c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 00465114 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 0044227c bytes 083f00d0
+ 00465114 bytes e84100f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce37906de48aa4ee2dcc44d49d8a6386"></a>

### [`004422f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004422f0.md) → [`00465188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465188.md) FUN_00465188

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
      "definition_site": "0046519c",
      "incomplete_value": false,
      "site": "004651a0",
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
      "definition_site": "00442304",
      "incomplete_value": false,
      "site": "00442308",
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
      "004651a0",
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
      "004651a0",
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

- 旧版 [`004422fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004422f0.md#insn-004422fc) · [`00442300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004422f0.md#insn-00442300) · [`00442304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004422f0.md#insn-00442304)
- 新版 [`00465194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465188.md#insn-00465194) · [`00465198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465188.md#insn-00465198) · [`0046519c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465188.md#insn-0046519c)

~~~diff
- 004422fc ["INT_ADD", "register:40f0:8", ["const:4422fc:8", "const:4:8"]]
- 004422fc ["CALL", null, ["callee:00c57a90:8"]]
+ 00465194 ["INT_ADD", "register:40f0:8", ["const:465194:8", "const:4:8"]]
+ 00465194 ["CALL", null, ["callee:00c57a90:8"]]
- 004422fc bytes 51631e94
+ 00465194 bytes 3fca1f94
- 00442300 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00465198 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00442300 bytes 283d00b0
+ 00465198 bytes e83f00f0
- 00442304 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00442304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00442304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00442304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046519c ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0046519c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046519c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046519c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00442304 bytes 08612591
+ 0046519c bytes 08611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e13e5a05251ebf8c03d4a76c0e69a936"></a>

### [`00442314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442314.md) → [`004651ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004651ac.md) FUN_004651ac

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
      "definition_site": "004651b0",
      "incomplete_value": false,
      "site": "004651b4",
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
      "definition_site": "00442318",
      "incomplete_value": false,
      "site": "0044231c",
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
      "004651b4",
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
      "004651b4",
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

- 旧版 [`00442314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442314.md#insn-00442314) · [`00442318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442314.md#insn-00442318)
- 新版 [`004651ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004651ac.md#insn-004651ac) · [`004651b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004651ac.md#insn-004651b0)

~~~diff
- 00442314 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004651ac ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00442314 bytes 283d00b0
+ 004651ac bytes e83f00f0
- 00442318 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00442318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00442318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00442318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004651b0 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 004651b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004651b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004651b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00442318 bytes 08612591
+ 004651b0 bytes 08611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bffdb6a34df9a60da044fdc2c5018244"></a>

### [`0044232c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044232c.md) → [`004651c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004651c4.md) FUN_004651c4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00465204",
      "incomplete_value": false,
      "site": "0046520c",
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
      "definition_site": "0044236c",
      "incomplete_value": false,
      "site": "00442374",
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
      "definition_site": "0046521c",
      "incomplete_value": false,
      "site": "00465220",
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
      "definition_site": "00442384",
      "incomplete_value": false,
      "site": "00442388",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004651dc",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "004651e8",
      "READ",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00465204",
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
      "004651dc",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "004651e8",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "00465204",
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

- 旧版 [`00442374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044232c.md#insn-00442374) · [`00442388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044232c.md#insn-00442388) · [`00442338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044232c.md#insn-00442338)
- 新版 [`0046520c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004651c4.md#insn-0046520c) · [`00465220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004651c4.md#insn-00465220) · [`004651d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004651c4.md#insn-004651d0)

~~~diff
- 00442374 ["INT_ADD", "register:40f0:8", ["const:442374:8", "const:4:8"]]
- 00442374 ["CALL", null, ["callee:00c57a50:8"]]
+ 0046520c ["INT_ADD", "register:40f0:8", ["const:46520c:8", "const:4:8"]]
+ 0046520c ["CALL", null, ["callee:00c57a50:8"]]
- 00442374 bytes 23631e94
+ 0046520c bytes 11ca1f94
- 00442388 ["INT_ADD", "register:40f0:8", ["const:442388:8", "const:4:8"]]
- 00442388 ["CALL", null, ["callee:00c57a70:8"]]
+ 00465220 ["INT_ADD", "register:40f0:8", ["const:465220:8", "const:4:8"]]
+ 00465220 ["CALL", null, ["callee:00c57a70:8"]]
- 00442388 bytes 26631e94
+ 00465220 bytes 14ca1f94
- 00442338 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 004651d0 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00442338 bytes 083f00d0
+ 004651d0 bytes e84100f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ced138db376705d8f463c8f04533dbd"></a>

### [`004423c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004423c0.md) → [`00465258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465258.md) FUN_00465258

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
      "definition_site": "0046526c",
      "incomplete_value": false,
      "site": "00465270",
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
      "definition_site": "004423d4",
      "incomplete_value": false,
      "site": "004423d8",
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
      "00465270",
      "DATA",
      [
        "storage",
        "00be79d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465270",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004423cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004423c0.md#insn-004423cc) · [`004423d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004423c0.md#insn-004423d0) · [`004423d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004423c0.md#insn-004423d4)
- 新版 [`00465264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465258.md#insn-00465264) · [`00465268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465258.md#insn-00465268) · [`0046526c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465258.md#insn-0046526c)

~~~diff
- 004423cc ["INT_ADD", "register:40f0:8", ["const:4423cc:8", "const:4:8"]]
- 004423cc ["CALL", null, ["callee:00c57a90:8"]]
+ 00465264 ["INT_ADD", "register:40f0:8", ["const:465264:8", "const:4:8"]]
+ 00465264 ["CALL", null, ["callee:00c57a90:8"]]
- 004423cc bytes 1d631e94
+ 00465264 bytes 0bca1f94
- 004423d0 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00465268 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004423d0 bytes 283d00b0
+ 00465268 bytes e83f00f0
- 004423d4 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 004423d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004423d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004423d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046526c ["COPY", "tmp:0:8", ["const:598:8"]]
+ 0046526c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046526c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046526c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004423d4 bytes 08612791
+ 0046526c bytes 08611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69b6f93d726617f6b2d7f198d2cc4d30"></a>

### [`004423e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004423e4.md) → [`0046527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046527c.md) FUN_0046527c

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
      "definition_site": "00465280",
      "incomplete_value": false,
      "site": "00465284",
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
      "definition_site": "004423e8",
      "incomplete_value": false,
      "site": "004423ec",
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
      "00465284",
      "DATA",
      [
        "storage",
        "00be79d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465284",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004423e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004423e4.md#insn-004423e4) · [`004423e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004423e4.md#insn-004423e8)
- 新版 [`0046527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046527c.md#insn-0046527c) · [`00465280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046527c.md#insn-00465280)

~~~diff
- 004423e4 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0046527c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004423e4 bytes 283d00b0
+ 0046527c bytes e83f00f0
- 004423e8 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 004423e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004423e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004423e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465280 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00465280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004423e8 bytes 08612791
+ 00465280 bytes 08611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e3328f673c8f3af1872310cc0f8b735"></a>

### [`004423fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004423fc.md) → [`00465294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465294.md) FUN_00465294

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.73% / 新版 89.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00465338",
      "incomplete_value": true,
      "site": "00465338",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ac:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004424a0",
      "incomplete_value": true,
      "site": "004424a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:489:8"
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
      "definition_site": "00465424",
      "incomplete_value": true,
      "site": "00465424",
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
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044258c",
      "incomplete_value": true,
      "site": "0044258c",
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
              "LOAD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046540c",
      "incomplete_value": true,
      "site": "00465424",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00442574",
      "incomplete_value": true,
      "site": "0044258c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00465324",
      "READ",
      [
        "storage",
        "002ab489",
        null,
        "string"
      ]
    ],
    [
      "00465400",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046540c",
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
      "00465324",
      "READ",
      [
        "storage",
        "002bc3ac",
        null,
        "string"
      ]
    ],
    [
      "00465400",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046540c",
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

- 旧版 [`0044258c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004423fc.md#insn-0044258c) · [`004425b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004423fc.md#insn-004425b8) · [`00442614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004423fc.md#insn-00442614)
- 新版 [`00465424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465294.md#insn-00465424) · [`00465450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465294.md#insn-00465450) · [`004654ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465294.md#insn-004654ac)

~~~diff
- 0044258c ["COPY", "register:0:8", ["register:4040:8"]]
- 0044258c ["INT_ADD", "register:40f0:8", ["const:44258c:8", "const:4:8"]]
- 0044258c ["CALLIND", null, ["register:0:8"]]
+ 00465424 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465424 ["INT_ADD", "register:40f0:8", ["const:465424:8", "const:4:8"]]
+ 00465424 ["CALLIND", null, ["register:0:8"]]
- 0044258c bytes 00013fd6
+ 00465424 bytes 00013fd6
- 004425b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004425b8 ["INT_ADD", "register:40f0:8", ["const:4425b8:8", "const:4:8"]]
- 004425b8 ["CALLIND", null, ["register:0:8"]]
+ 00465450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465450 ["INT_ADD", "register:40f0:8", ["const:465450:8", "const:4:8"]]
+ 00465450 ["CALLIND", null, ["register:0:8"]]
- 004425b8 bytes 00013fd6
+ 00465450 bytes 00013fd6
- 00442614 ["COPY", "register:0:8", ["register:4040:8"]]
- 00442614 ["INT_ADD", "register:40f0:8", ["const:442614:8", "const:4:8"]]
- 00442614 ["CALLIND", null, ["register:0:8"]]
+ 004654ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004654ac ["INT_ADD", "register:40f0:8", ["const:4654ac:8", "const:4:8"]]
+ 004654ac ["CALLIND", null, ["register:0:8"]]
- 00442614 bytes 00013fd6
+ 004654ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-871cb612fe52acd15f4599818e679340"></a>

### [`00442780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442780.md) → [`00465618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465618.md) FUN_00465618

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
      "definition_site": "0046562c",
      "incomplete_value": false,
      "site": "00465630",
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
      "definition_site": "00442794",
      "incomplete_value": false,
      "site": "00442798",
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
      "00465630",
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
      "00465630",
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

- 旧版 [`0044278c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442780.md#insn-0044278c) · [`00442790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442780.md#insn-00442790) · [`00442794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442780.md#insn-00442794)
- 新版 [`00465624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465618.md#insn-00465624) · [`00465628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465618.md#insn-00465628) · [`0046562c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465618.md#insn-0046562c)

~~~diff
- 0044278c ["INT_ADD", "register:40f0:8", ["const:44278c:8", "const:4:8"]]
- 0044278c ["CALL", null, ["callee:00c57a90:8"]]
+ 00465624 ["INT_ADD", "register:40f0:8", ["const:465624:8", "const:4:8"]]
+ 00465624 ["CALL", null, ["callee:00c57a90:8"]]
- 0044278c bytes 2d621e94
+ 00465624 bytes 1bc91f94
- 00442790 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00465628 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00442790 bytes 283d00b0
+ 00465628 bytes e83f00f0
- 00442794 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 00442794 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00442794 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00442794 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046562c ["COPY", "tmp:0:8", ["const:618:8"]]
+ 0046562c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046562c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046562c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00442794 bytes 08612991
+ 0046562c bytes 08611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df772b6fbf6773d5c091ed89c692815e"></a>

### [`004427a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004427a4.md) → [`0046563c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046563c.md) FUN_0046563c

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
      "definition_site": "00465640",
      "incomplete_value": false,
      "site": "00465644",
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
      "definition_site": "004427a8",
      "incomplete_value": false,
      "site": "004427ac",
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
      "00465644",
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
      "00465644",
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

- 旧版 [`004427a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004427a4.md#insn-004427a4) · [`004427a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004427a4.md#insn-004427a8)
- 新版 [`0046563c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046563c.md#insn-0046563c) · [`00465640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046563c.md#insn-00465640)

~~~diff
- 004427a4 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0046563c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004427a4 bytes 283d00b0
+ 0046563c bytes e83f00f0
- 004427a8 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 004427a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004427a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004427a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465640 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 00465640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004427a8 bytes 08612991
+ 00465640 bytes 08611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91f8533428c4922078acdb799c861c08"></a>

### [`004427bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004427bc.md) → [`00465654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465654.md) FUN_00465654

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00465694",
      "incomplete_value": false,
      "site": "0046569c",
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
      "definition_site": "004427fc",
      "incomplete_value": false,
      "site": "00442804",
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
      "definition_site": "004656ac",
      "incomplete_value": false,
      "site": "004656b0",
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
      "definition_site": "00442814",
      "incomplete_value": false,
      "site": "00442818",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046566c",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465678",
      "READ",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00465694",
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
      "0046566c",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465678",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "00465694",
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

- 旧版 [`00442804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004427bc.md#insn-00442804) · [`00442818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004427bc.md#insn-00442818) · [`004427c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004427bc.md#insn-004427c8)
- 新版 [`0046569c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465654.md#insn-0046569c) · [`004656b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465654.md#insn-004656b0) · [`00465660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465654.md#insn-00465660)

~~~diff
- 00442804 ["INT_ADD", "register:40f0:8", ["const:442804:8", "const:4:8"]]
- 00442804 ["CALL", null, ["callee:00c57a50:8"]]
+ 0046569c ["INT_ADD", "register:40f0:8", ["const:46569c:8", "const:4:8"]]
+ 0046569c ["CALL", null, ["callee:00c57a50:8"]]
- 00442804 bytes ff611e94
+ 0046569c bytes edc81f94
- 00442818 ["INT_ADD", "register:40f0:8", ["const:442818:8", "const:4:8"]]
- 00442818 ["CALL", null, ["callee:00c57a70:8"]]
+ 004656b0 ["INT_ADD", "register:40f0:8", ["const:4656b0:8", "const:4:8"]]
+ 004656b0 ["CALL", null, ["callee:00c57a70:8"]]
- 00442818 bytes 02621e94
+ 004656b0 bytes f0c81f94
- 004427c8 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 00465660 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 004427c8 bytes 083f00d0
+ 00465660 bytes e84100f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67327f7f91cf603814ec3d4b704d7fbf"></a>

### [`0044284c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044284c.md) → [`004656e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004656e4.md) FUN_004656e4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "004656fc",
      "incomplete_value": false,
      "site": "00465700",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00442864",
      "incomplete_value": false,
      "site": "00442868",
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
            "const:ad8:8"
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
      "00465700",
      "DATA",
      [
        "storage",
        "00be7ad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465700",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00442860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044284c.md#insn-00442860) · [`00442864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044284c.md#insn-00442864) · [`00442890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044284c.md#insn-00442890)
- 新版 [`004656f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004656e4.md#insn-004656f8) · [`004656fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004656e4.md#insn-004656fc) · [`00465728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004656e4.md#insn-00465728)

~~~diff
- 00442860 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 004656f8 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00442860 bytes 293d00b0
+ 004656f8 bytes e93f00f0
- 00442864 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 00442864 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00442864 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00442864 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004656fc ["COPY", "tmp:0:8", ["const:698:8"]]
+ 004656fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004656fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004656fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00442864 bytes 29612b91
+ 004656fc bytes 29611a91
- 00442890 ["INT_ADD", "register:40f0:8", ["const:442890:8", "const:4:8"]]
- 00442890 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00465728 ["INT_ADD", "register:40f0:8", ["const:465728:8", "const:4:8"]]
+ 00465728 ["CALL", null, ["callee:00c57ab0:8"]]
- 00442890 bytes f4611e94
+ 00465728 bytes e2c81f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39d90b82d3f05eef9187c671762653ec"></a>

### [`004428bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004428bc.md) → [`00465754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465754.md) FUN_00465754

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0046576c",
      "incomplete_value": false,
      "site": "00465770",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004428d4",
      "incomplete_value": false,
      "site": "004428d8",
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
            "const:ad8:8"
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
      "00465770",
      "DATA",
      [
        "storage",
        "00be7ad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465770",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004428d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004428bc.md#insn-004428d0) · [`004428d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004428bc.md#insn-004428d4) · [`004428f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/004428bc.md#insn-004428f4)
- 新版 [`00465768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465754.md#insn-00465768) · [`0046576c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465754.md#insn-0046576c) · [`0046578c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465754.md#insn-0046578c)

~~~diff
- 004428d0 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 00465768 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 004428d0 bytes 293d00b0
+ 00465768 bytes e93f00f0
- 004428d4 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 004428d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004428d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004428d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0046576c ["COPY", "tmp:0:8", ["const:698:8"]]
+ 0046576c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0046576c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0046576c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004428d4 bytes 29612b91
+ 0046576c bytes 29611a91
- 004428f4 ["INT_ADD", "register:40f0:8", ["const:4428f4:8", "const:4:8"]]
- 004428f4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0046578c ["INT_ADD", "register:40f0:8", ["const:46578c:8", "const:4:8"]]
+ 0046578c ["CALL", null, ["callee:00c57ab0:8"]]
- 004428f4 bytes db611e94
+ 0046578c bytes c9c81f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82dc9685e227eaead365e3d9acdf567c"></a>

### [`0044292c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044292c.md) → [`004657c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004657c4.md) FUN_004657c4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`004439f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/004439f4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/0046688c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "004657e8",
      "incomplete_value": false,
      "site": "004657e8",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00442950",
      "incomplete_value": false,
      "site": "00442950",
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
            "const:ad8:8"
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
      "004657e8",
      "DATA",
      [
        "storage",
        "00be7ad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004657e8",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00442940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044292c.md#insn-00442940) · [`00442948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044292c.md#insn-00442948) · [`0044294c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/0044292c.md#insn-0044294c)
- 新版 [`004657d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004657c4.md#insn-004657d8) · [`004657e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004657c4.md#insn-004657e0) · [`004657e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004657c4.md#insn-004657e4)

~~~diff
- 00442940 ["INT_ADD", "register:40f0:8", ["const:442940:8", "const:4:8"]]
- 00442940 ["CALL", null, ["callee:00c57a90:8"]]
+ 004657d8 ["INT_ADD", "register:40f0:8", ["const:4657d8:8", "const:4:8"]]
+ 004657d8 ["CALL", null, ["callee:00c57a90:8"]]
- 00442940 bytes c0611e94
+ 004657d8 bytes aec81f94
- 00442948 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004657e0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00442948 bytes 283d00b0
+ 004657e0 bytes e83f00f0
- 0044294c ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 0044294c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044294c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044294c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004657e4 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 004657e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004657e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004657e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044294c bytes 08612b91
+ 004657e4 bytes 08611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d3a3af85b9cd0b9ced4887af3e72b5c"></a>

### [`00442980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442980.md) → [`00465818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465818.md) FUN_00465818

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`004439f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/004439f4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/0046688c.md)

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
      "definition_site": "00465824",
      "incomplete_value": false,
      "site": "00465824",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044298c",
      "incomplete_value": false,
      "site": "0044298c",
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
            "const:ad8:8"
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
      "00465824",
      "DATA",
      [
        "storage",
        "00be7ad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465824",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00442984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442980.md#insn-00442984) · [`00442988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442980.md#insn-00442988)
- 新版 [`0046581c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465818.md#insn-0046581c) · [`00465820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465818.md#insn-00465820)

~~~diff
- 00442984 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 0046581c ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00442984 bytes 293d00b0
+ 0046581c bytes e93f00f0
- 00442988 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 00442988 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00442988 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00442988 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00465820 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 00465820 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00465820 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00465820 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00442988 bytes 29612b91
+ 00465820 bytes 29611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-914ffdf1403578aef0294ae57654c5e5"></a>

### [`00442a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442a64.md) → [`004658fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md) FUN_004658fc

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 22件 [`0041b014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b014.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`0042d2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d2a8.md) [`0042d878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d878.md) [`0053b99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b99c.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0043db14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db14.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`00450140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md) [`00450710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md) [`0055e834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e834.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 91.58% / 新版 91.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `call_target` 5件, `store_value` 9件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046597c",
      "incomplete_value": true,
      "site": "0046597c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00442ae4",
      "incomplete_value": true,
      "site": "00442ae4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f4:8"
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
      "definition_site": "00465b50",
      "incomplete_value": true,
      "site": "00465b50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00442cb8",
      "incomplete_value": true,
      "site": "00442cb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:307:8"
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
      "definition_site": "00465d50",
      "incomplete_value": true,
      "site": "00465d60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00442eb8",
      "incomplete_value": true,
      "site": "00442ec8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:25f:8"
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
      "00465960",
      "READ",
      [
        "storage",
        "002a31f4",
        null,
        "string"
      ]
    ],
    [
      "00465a1c",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465a28",
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
      "00465960",
      "READ",
      [
        "storage",
        "002b38ce",
        null,
        "string"
      ]
    ],
    [
      "00465a1c",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465a28",
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

- 旧版 [`00442dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442a64.md#insn-00442dc0) · [`00442e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442a64.md#insn-00442e2c) · [`00442e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00442/00442a64.md#insn-00442e68)
- 新版 [`00465c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md#insn-00465c58) · [`00465cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md#insn-00465cc4) · [`00465d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md#insn-00465d00)

~~~diff
- 00442dc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00442dc0 ["INT_ADD", "register:40f0:8", ["const:442dc0:8", "const:4:8"]]
- 00442dc0 ["CALLIND", null, ["register:0:8"]]
+ 00465c58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465c58 ["INT_ADD", "register:40f0:8", ["const:465c58:8", "const:4:8"]]
+ 00465c58 ["CALLIND", null, ["register:0:8"]]
- 00442dc0 bytes 00013fd6
+ 00465c58 bytes 00013fd6
- 00442e2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00442e2c ["INT_ADD", "register:40f0:8", ["const:442e2c:8", "const:4:8"]]
- 00442e2c ["CALLIND", null, ["register:0:8"]]
+ 00465cc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465cc4 ["INT_ADD", "register:40f0:8", ["const:465cc4:8", "const:4:8"]]
+ 00465cc4 ["CALLIND", null, ["register:0:8"]]
- 00442e2c bytes 00013fd6
+ 00465cc4 bytes 00013fd6
- 00442e68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00442e68 ["INT_ADD", "register:40f0:8", ["const:442e68:8", "const:4:8"]]
- 00442e68 ["CALLIND", null, ["register:0:8"]]
+ 00465d00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465d00 ["INT_ADD", "register:40f0:8", ["const:465d00:8", "const:4:8"]]
+ 00465d00 ["CALLIND", null, ["register:0:8"]]
- 00442e68 bytes 00013fd6
+ 00465d00 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87c0c4fcd76a04324551c57137375a37"></a>

### [`00443ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443ae8.md) → [`00466980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466980.md) FUN_00466980

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
      "definition_site": "00466994",
      "incomplete_value": false,
      "site": "00466998",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00443afc",
      "incomplete_value": false,
      "site": "00443b00",
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
            "const:b58:8"
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
      "00466998",
      "DATA",
      [
        "storage",
        "00be7b58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466998",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443ae8.md#insn-00443af4) · [`00443af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443ae8.md#insn-00443af8) · [`00443afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443ae8.md#insn-00443afc)
- 新版 [`0046698c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466980.md#insn-0046698c) · [`00466990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466980.md#insn-00466990) · [`00466994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466980.md#insn-00466994)

~~~diff
- 00443af4 ["INT_ADD", "register:40f0:8", ["const:443af4:8", "const:4:8"]]
- 00443af4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0046698c ["INT_ADD", "register:40f0:8", ["const:46698c:8", "const:4:8"]]
+ 0046698c ["CALL", null, ["callee:00c57a90:8"]]
- 00443af4 bytes 535d1e94
+ 0046698c bytes 41c41f94
- 00443af8 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00466990 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00443af8 bytes 283d0090
+ 00466990 bytes e83f00d0
- 00443afc ["COPY", "tmp:0:8", ["const:b58:8"]]
- 00443afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00443afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00443afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466994 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00466994 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466994 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466994 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00443afc bytes 08612d91
+ 00466994 bytes 08611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39d407a3d17d3b1017e04dfdba249240"></a>

### [`00443b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443b0c.md) → [`004669a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/004669a4.md) FUN_004669a4

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
      "definition_site": "004669a8",
      "incomplete_value": false,
      "site": "004669ac",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00443b10",
      "incomplete_value": false,
      "site": "00443b14",
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
            "const:b58:8"
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
      "004669ac",
      "DATA",
      [
        "storage",
        "00be7b58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004669ac",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443b0c.md#insn-00443b0c) · [`00443b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443b0c.md#insn-00443b10)
- 新版 [`004669a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/004669a4.md#insn-004669a4) · [`004669a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/004669a4.md#insn-004669a8)

~~~diff
- 00443b0c ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004669a4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00443b0c bytes 283d0090
+ 004669a4 bytes e83f00d0
- 00443b10 ["COPY", "tmp:0:8", ["const:b58:8"]]
- 00443b10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00443b10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00443b10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004669a8 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 004669a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004669a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004669a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00443b10 bytes 08612d91
+ 004669a8 bytes 08611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09152c82febba9421eb38f7559ed74ff"></a>

### [`00443b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443b24.md) → [`004669bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/004669bc.md) FUN_004669bc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004669f4",
      "incomplete_value": false,
      "site": "004669f8",
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
      "definition_site": "00443b5c",
      "incomplete_value": false,
      "site": "00443b60",
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
      "definition_site": "00466a04",
      "incomplete_value": false,
      "site": "00466a08",
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
      "definition_site": "00443b6c",
      "incomplete_value": false,
      "site": "00443b70",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004669cc",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "004669d8",
      "READ",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined8"
      ]
    ],
    [
      "004669f4",
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
      "004669cc",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "004669d8",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "004669f4",
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

- 旧版 [`00443b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443b24.md#insn-00443b60) · [`00443b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443b24.md#insn-00443b70) · [`00443b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443b24.md#insn-00443b2c)
- 新版 [`004669f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/004669bc.md#insn-004669f8) · [`00466a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/004669bc.md#insn-00466a08) · [`004669c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/004669bc.md#insn-004669c4)

~~~diff
- 00443b60 ["INT_ADD", "register:40f0:8", ["const:443b60:8", "const:4:8"]]
- 00443b60 ["CALL", null, ["callee:00c57a50:8"]]
+ 004669f8 ["INT_ADD", "register:40f0:8", ["const:4669f8:8", "const:4:8"]]
+ 004669f8 ["CALL", null, ["callee:00c57a50:8"]]
- 00443b60 bytes 285d1e94
+ 004669f8 bytes 16c41f94
- 00443b70 ["INT_ADD", "register:40f0:8", ["const:443b70:8", "const:4:8"]]
- 00443b70 ["CALL", null, ["callee:00c57a70:8"]]
+ 00466a08 ["INT_ADD", "register:40f0:8", ["const:466a08:8", "const:4:8"]]
+ 00466a08 ["CALL", null, ["callee:00c57a70:8"]]
- 00443b70 bytes 2c5d1e94
+ 00466a08 bytes 1ac41f94
- 00443b2c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 004669c4 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00443b2c bytes 083f00b0
+ 004669c4 bytes e84100d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05d8f6517c0977d4386670a3344340e9"></a>

### [`00443ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443ba8.md) → [`00466a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a40.md) FUN_00466a40

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
      "definition_site": "00466a54",
      "incomplete_value": false,
      "site": "00466a58",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00443bbc",
      "incomplete_value": false,
      "site": "00443bc0",
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
            "const:bd8:8"
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
      "00466a58",
      "DATA",
      [
        "storage",
        "00be7bd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466a58",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443ba8.md#insn-00443bb4) · [`00443bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443ba8.md#insn-00443bb8) · [`00443bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443ba8.md#insn-00443bbc)
- 新版 [`00466a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a40.md#insn-00466a4c) · [`00466a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a40.md#insn-00466a50) · [`00466a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a40.md#insn-00466a54)

~~~diff
- 00443bb4 ["INT_ADD", "register:40f0:8", ["const:443bb4:8", "const:4:8"]]
- 00443bb4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00466a4c ["INT_ADD", "register:40f0:8", ["const:466a4c:8", "const:4:8"]]
+ 00466a4c ["CALL", null, ["callee:00c57a90:8"]]
- 00443bb4 bytes 235d1e94
+ 00466a4c bytes 11c41f94
- 00443bb8 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00466a50 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00443bb8 bytes 283d0090
+ 00466a50 bytes e83f00d0
- 00443bbc ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 00443bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00443bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00443bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466a54 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00466a54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00443bbc bytes 08612f91
+ 00466a54 bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35c7c0ef8853f56b54d6db6070f7668b"></a>

### [`00443bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443bcc.md) → [`00466a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a64.md) FUN_00466a64

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
      "definition_site": "00466a68",
      "incomplete_value": false,
      "site": "00466a6c",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00443bd0",
      "incomplete_value": false,
      "site": "00443bd4",
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
            "const:bd8:8"
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
      "00466a6c",
      "DATA",
      [
        "storage",
        "00be7bd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466a6c",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443bcc.md#insn-00443bcc) · [`00443bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443bcc.md#insn-00443bd0)
- 新版 [`00466a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a64.md#insn-00466a64) · [`00466a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a64.md#insn-00466a68)

~~~diff
- 00443bcc ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00466a64 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00443bcc bytes 283d0090
+ 00466a64 bytes e83f00d0
- 00443bd0 ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 00443bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00443bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00443bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466a68 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00466a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00443bd0 bytes 08612f91
+ 00466a68 bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db7333eec2df8207f39cf23a68f7736f"></a>

### [`00443be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443be4.md) → [`00466a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a7c.md) FUN_00466a7c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00466ab4",
      "incomplete_value": false,
      "site": "00466ab8",
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
      "definition_site": "00443c1c",
      "incomplete_value": false,
      "site": "00443c20",
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
      "definition_site": "00466ac4",
      "incomplete_value": false,
      "site": "00466ac8",
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
      "definition_site": "00443c2c",
      "incomplete_value": false,
      "site": "00443c30",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00466a8c",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "00466a98",
      "READ",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00466ab4",
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
      "00466a8c",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00466a98",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "00466ab4",
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

- 旧版 [`00443c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443be4.md#insn-00443c20) · [`00443c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443be4.md#insn-00443c30) · [`00443bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443be4.md#insn-00443bec)
- 新版 [`00466ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a7c.md#insn-00466ab8) · [`00466ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a7c.md#insn-00466ac8) · [`00466a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a7c.md#insn-00466a84)

~~~diff
- 00443c20 ["INT_ADD", "register:40f0:8", ["const:443c20:8", "const:4:8"]]
- 00443c20 ["CALL", null, ["callee:00c57a50:8"]]
+ 00466ab8 ["INT_ADD", "register:40f0:8", ["const:466ab8:8", "const:4:8"]]
+ 00466ab8 ["CALL", null, ["callee:00c57a50:8"]]
- 00443c20 bytes f85c1e94
+ 00466ab8 bytes e6c31f94
- 00443c30 ["INT_ADD", "register:40f0:8", ["const:443c30:8", "const:4:8"]]
- 00443c30 ["CALL", null, ["callee:00c57a70:8"]]
+ 00466ac8 ["INT_ADD", "register:40f0:8", ["const:466ac8:8", "const:4:8"]]
+ 00466ac8 ["CALL", null, ["callee:00c57a70:8"]]
- 00443c30 bytes fc5c1e94
+ 00466ac8 bytes eac31f94
- 00443bec ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 00466a84 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00443bec bytes 083f00b0
+ 00466a84 bytes e84100d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d463a7230226a1c9abe6a7db9816f4a6"></a>

### [`00443c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443c60.md) → [`00466af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466af8.md) FUN_00466af8

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
      "definition_site": "00466b04",
      "incomplete_value": false,
      "site": "00466b10",
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
      "definition_site": "00443c6c",
      "incomplete_value": false,
      "site": "00443c78",
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
      "00466b10",
      "DATA",
      [
        "storage",
        "00be7c58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466b10",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443c60.md#insn-00443c68) · [`00443c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443c60.md#insn-00443c6c)
- 新版 [`00466b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466af8.md#insn-00466b00) · [`00466b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466af8.md#insn-00466b04)

~~~diff
- 00443c68 ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 00466b00 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 00443c68 bytes 2a3d0090
+ 00466b00 bytes ea3f00d0
- 00443c6c ["COPY", "tmp:0:8", ["const:c58:8"]]
- 00443c6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00443c6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00443c6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00466b04 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00466b04 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00466b04 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00466b04 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00443c6c bytes 4a613191
+ 00466b04 bytes 4a612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ca8475f564b8ac742f62058a40c233c"></a>

### [`00443ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443ca4.md) → [`00466b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b3c.md) FUN_00466b3c

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
      "definition_site": "00466b54",
      "incomplete_value": false,
      "site": "00466b60",
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
      "definition_site": "00443cbc",
      "incomplete_value": false,
      "site": "00443cc8",
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
      "00466b60",
      "DATA",
      [
        "storage",
        "00be7c58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466b60",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443ca4.md#insn-00443cb8) · [`00443cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443ca4.md#insn-00443cbc) · [`00443cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443ca4.md#insn-00443cec)
- 新版 [`00466b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b3c.md#insn-00466b50) · [`00466b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b3c.md#insn-00466b54) · [`00466b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b3c.md#insn-00466b84)

~~~diff
- 00443cb8 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00466b50 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00443cb8 bytes 283d0090
+ 00466b50 bytes e83f00d0
- 00443cbc ["COPY", "tmp:0:8", ["const:c58:8"]]
- 00443cbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00443cbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00443cbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466b54 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00466b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00443cbc bytes 08613191
+ 00466b54 bytes 08612091
- 00443cec ["COPY", "register:0:8", ["register:4040:8"]]
- 00443cec ["INT_ADD", "register:40f0:8", ["const:443cec:8", "const:4:8"]]
- 00443cec ["CALLIND", null, ["register:0:8"]]
+ 00466b84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00466b84 ["INT_ADD", "register:40f0:8", ["const:466b84:8", "const:4:8"]]
+ 00466b84 ["CALLIND", null, ["register:0:8"]]
- 00443cec bytes 00013fd6
+ 00466b84 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4b3ad6666e8a6a506baa8a344ba518d"></a>

### [`00443d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443d00.md) → [`00466b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b98.md) FUN_00466b98

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
      "definition_site": "00466bc4",
      "incomplete_value": false,
      "site": "00466bc4",
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
      "definition_site": "00443d2c",
      "incomplete_value": false,
      "site": "00443d2c",
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
      "00466bc4",
      "DATA",
      [
        "storage",
        "00be7c58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466bc4",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443d00.md#insn-00443d14) · [`00443d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443d00.md#insn-00443d20) · [`00443d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443d00.md#insn-00443d24)
- 新版 [`00466bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b98.md#insn-00466bac) · [`00466bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b98.md#insn-00466bb8) · [`00466bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b98.md#insn-00466bbc)

~~~diff
- 00443d14 ["INT_ADD", "register:40f0:8", ["const:443d14:8", "const:4:8"]]
- 00443d14 ["CALL", null, ["callee:00c57a90:8"]]
+ 00466bac ["INT_ADD", "register:40f0:8", ["const:466bac:8", "const:4:8"]]
+ 00466bac ["CALL", null, ["callee:00c57a90:8"]]
- 00443d14 bytes cb5c1e94
+ 00466bac bytes b9c31f94
- 00443d20 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00466bb8 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00443d20 bytes 283d0090
+ 00466bb8 bytes e83f00d0
- 00443d24 ["COPY", "tmp:0:8", ["const:c58:8"]]
- 00443d24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00443d24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00443d24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466bbc ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00466bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00443d24 bytes 08613191
+ 00466bbc bytes 08612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54ead2021eb15d62b01c47d8f01b798b"></a>

### [`00443d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443d88.md) → [`00466c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466c20.md) FUN_00466c20

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
      "definition_site": "00466c3c",
      "incomplete_value": false,
      "site": "00466c3c",
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
      "definition_site": "00443da4",
      "incomplete_value": false,
      "site": "00443da4",
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
      "00466c3c",
      "DATA",
      [
        "storage",
        "00be7c58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466c3c",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443d88.md#insn-00443d9c) · [`00443da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443d88.md#insn-00443da0) · [`00443dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00443/00443d88.md#insn-00443dc4)
- 新版 [`00466c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466c20.md#insn-00466c34) · [`00466c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466c20.md#insn-00466c38) · [`00466c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466c20.md#insn-00466c5c)

~~~diff
- 00443d9c ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 00466c34 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00443d9c bytes 293d0090
+ 00466c34 bytes e93f00d0
- 00443da0 ["COPY", "tmp:0:8", ["const:c58:8"]]
- 00443da0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00443da0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00443da0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00466c38 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00466c38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00466c38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00466c38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00443da0 bytes 29613191
+ 00466c38 bytes 29612091
- 00443dc4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00443dc4 ["INT_ADD", "register:40f0:8", ["const:443dc4:8", "const:4:8"]]
- 00443dc4 ["CALLIND", null, ["register:0:8"]]
+ 00466c5c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00466c5c ["INT_ADD", "register:40f0:8", ["const:466c5c:8", "const:4:8"]]
+ 00466c5c ["CALLIND", null, ["register:0:8"]]
- 00443dc4 bytes 20013fd6
+ 00466c5c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b3da1d121c79b84f40397d2be287dfc"></a>

### [`00444034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444034.md) → [`00466ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ecc.md) FUN_00466ecc

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
      "definition_site": "00466ee0",
      "incomplete_value": false,
      "site": "00466ee4",
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
      "definition_site": "00444048",
      "incomplete_value": false,
      "site": "0044404c",
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
      "00466ee4",
      "DATA",
      [
        "storage",
        "00be7cd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466ee4",
      "DATA",
      [
        "storage",
        "00c64898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00444040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444034.md#insn-00444040) · [`00444044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444034.md#insn-00444044) · [`00444048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444034.md#insn-00444048)
- 新版 [`00466ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ecc.md#insn-00466ed8) · [`00466edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ecc.md#insn-00466edc) · [`00466ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ecc.md#insn-00466ee0)

~~~diff
- 00444040 ["INT_ADD", "register:40f0:8", ["const:444040:8", "const:4:8"]]
- 00444040 ["CALL", null, ["callee:00c57a90:8"]]
+ 00466ed8 ["INT_ADD", "register:40f0:8", ["const:466ed8:8", "const:4:8"]]
+ 00466ed8 ["CALL", null, ["callee:00c57a90:8"]]
- 00444040 bytes 005c1e94
+ 00466ed8 bytes eec21f94
- 00444044 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00466edc ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00444044 bytes 083d00f0
+ 00466edc bytes e83f00d0
- 00444048 ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 00444048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00444048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00444048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466ee0 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00466ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00444048 bytes 08613391
+ 00466ee0 bytes 08612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f3a6c8813305575af7fb715cbc5c37f"></a>

### [`00444058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444058.md) → [`00466ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ef0.md) FUN_00466ef0

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
      "definition_site": "00466ef4",
      "incomplete_value": false,
      "site": "00466ef8",
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
      "definition_site": "0044405c",
      "incomplete_value": false,
      "site": "00444060",
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
      "00466ef8",
      "DATA",
      [
        "storage",
        "00be7cd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466ef8",
      "DATA",
      [
        "storage",
        "00c64898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00444058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444058.md#insn-00444058) · [`0044405c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444058.md#insn-0044405c)
- 新版 [`00466ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ef0.md#insn-00466ef0) · [`00466ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ef0.md#insn-00466ef4)

~~~diff
- 00444058 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00466ef0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00444058 bytes 083d00f0
+ 00466ef0 bytes e83f00d0
- 0044405c ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 0044405c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044405c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044405c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466ef4 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00466ef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466ef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466ef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044405c bytes 08613391
+ 00466ef4 bytes 08612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89af78d7f80beab96b5e95bba2f28cdc"></a>

### [`00444070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444070.md) → [`00466f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466f08.md) FUN_00466f08

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.63% / 新版 89.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00466fbc",
      "incomplete_value": true,
      "site": "00466fbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00444124",
      "incomplete_value": true,
      "site": "00444124",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:66b:8"
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
      "definition_site": "00466f68",
      "incomplete_value": true,
      "site": "00466f6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:870:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004440d0",
      "incomplete_value": true,
      "site": "004440d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e80:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00467024",
      "incomplete_value": true,
      "site": "00467024",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044418c",
      "incomplete_value": true,
      "site": "0044418c",
      "value": [
        "LOAD",
        "8",
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
      "00466f68",
      "READ",
      [
        "storage",
        "00c1ae80",
        null,
        "pointer"
      ]
    ],
    [
      "00466f68",
      "PARAM",
      [
        "storage",
        "010a21f8",
        "_ZNSt6__ndk14coutE",
        "undefined8"
      ]
    ],
    [
      "00466fac",
      "READ",
      [
        "storage",
        "002ac66b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00466f68",
      "READ",
      [
        "storage",
        "00c9a870",
        null,
        "pointer"
      ]
    ],
    [
      "00466f68",
      "PARAM",
      [
        "storage",
        "01127100",
        "_ZNSt6__ndk14coutE",
        "undefined8"
      ]
    ],
    [
      "00466fac",
      "READ",
      [
        "storage",
        "002bd6e3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004440d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444070.md#insn-004440d4) · [`0044418c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444070.md#insn-0044418c) · [`004441b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444070.md#insn-004441b4)
- 新版 [`00466f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466f08.md#insn-00466f6c) · [`00467024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466f08.md#insn-00467024) · [`0046704c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466f08.md#insn-0046704c)

~~~diff
- 004440d4 ["INT_ADD", "register:40f0:8", ["const:4440d4:8", "const:4:8"]]
- 004440d4 ["CALL", null, ["callee:00459490:8"]]
+ 00466f6c ["INT_ADD", "register:40f0:8", ["const:466f6c:8", "const:4:8"]]
+ 00466f6c ["CALL", null, ["callee:00459490:8"]]
- 004440d4 bytes 49c9ff97
+ 00466f6c bytes 49c9ff97
- 0044418c ["COPY", "register:0:8", ["register:4040:8"]]
- 0044418c ["INT_ADD", "register:40f0:8", ["const:44418c:8", "const:4:8"]]
- 0044418c ["CALLIND", null, ["register:0:8"]]
+ 00467024 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00467024 ["INT_ADD", "register:40f0:8", ["const:467024:8", "const:4:8"]]
+ 00467024 ["CALLIND", null, ["register:0:8"]]
- 0044418c bytes 00013fd6
+ 00467024 bytes 00013fd6
- 004441b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004441b4 ["INT_ADD", "register:40f0:8", ["const:4441b4:8", "const:4:8"]]
- 004441b4 ["CALLIND", null, ["register:0:8"]]
+ 0046704c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046704c ["INT_ADD", "register:40f0:8", ["const:46704c:8", "const:4:8"]]
+ 0046704c ["CALLIND", null, ["register:0:8"]]
- 004441b4 bytes 00013fd6
+ 0046704c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e457c3de3379d50903b56492f27253ef"></a>

### [`00444380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444380.md) → [`00467218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467218.md) _INIT_11

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00467254",
      "incomplete_value": true,
      "site": "00467270",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004443bc",
      "incomplete_value": true,
      "site": "004443d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00467278",
      "incomplete_value": true,
      "site": "00467294",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004443e0",
      "incomplete_value": true,
      "site": "004443fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00467298",
      "incomplete_value": true,
      "site": "004672b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00444400",
      "incomplete_value": true,
      "site": "0044441c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00467254",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00467278",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00467298",
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
      "00467254",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00467278",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00467298",
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

- 旧版 [`004444e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444380.md#insn-004444e0) · [`004445b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444380.md#insn-004445b4) · [`004443a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444380.md#insn-004443a8)
- 新版 [`00467378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467218.md#insn-00467378) · [`0046744c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467218.md#insn-0046744c) · [`00467240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467218.md#insn-00467240)

~~~diff
- 004444e0 ["INT_ADD", "register:40f0:8", ["const:4444e0:8", "const:4:8"]]
- 004444e0 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00467378 ["INT_ADD", "register:40f0:8", ["const:467378:8", "const:4:8"]]
+ 00467378 ["CALL", null, ["callee:0043b7b8:8"]]
- 004444e0 bytes f651ff97
+ 00467378 bytes 1051ff97
- 004445b4 ["INT_ADD", "register:40f0:8", ["const:4445b4:8", "const:4:8"]]
- 004445b4 ["CALL", null, ["callee:00c57a30:8"]]
+ 0046744c ["INT_ADD", "register:40f0:8", ["const:46744c:8", "const:4:8"]]
+ 0046744c ["CALL", null, ["callee:00c57a30:8"]]
- 004445b4 bytes 8b5a1e94
+ 0046744c bytes 79c11f94
- 004443a8 ["COPY", "register:4098:8", ["const:c24000:8"]]
+ 00467240 ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 004443a8 bytes 133f0090
+ 00467240 bytes f34100b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbdc3c36278f4cc4dac693ae0155728d"></a>

### [`00444778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444778.md) → [`00467610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467610.md) FUN_00467610

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0044af4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044af4c.md) [`005d76a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d7/005d76a0.md) · 呼出先 0件 
- 新版 呼出元 2件 [`0046dde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dde4.md) [`005fc360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc360.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

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
      "definition_site": "0046761c",
      "incomplete_value": true,
      "site": "00467628",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00444784",
      "incomplete_value": true,
      "site": "00444790",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:680:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00467624",
      "incomplete_value": true,
      "site": "0046762c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044478c",
      "incomplete_value": true,
      "site": "00444794",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:688:8"
              ]
            ]
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
      "0046761c",
      "READ",
      [
        "storage",
        "002b2680",
        null,
        "undefined8"
      ]
    ],
    [
      "00467624",
      "READ",
      [
        "storage",
        "002b2688",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0046761c",
      "READ",
      [
        "storage",
        "002c3d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00467624",
      "READ",
      [
        "storage",
        "002c3d60",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00444778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444778.md#insn-00444778) · [`00444784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444778.md#insn-00444784) · [`00444788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444778.md#insn-00444788)
- 新版 [`00467610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467610.md#insn-00467610) · [`0046761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467610.md#insn-0046761c)

~~~diff
- 00444778 ["COPY", "register:4040:8", ["const:2b2000:8"]]
+ 00467610 ["COPY", "register:4040:8", ["const:2c3000:8"]]
- 00444778 bytes 68f3ffd0
+ 00467610 bytes e8f2ff90
- 00444784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:680:8"]]
- 00444784 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00444784 ["COPY", "register:5008:8", ["const:0:8"]]
- 00444784 ["COPY", "register:5010:8", ["const:0:8"]]
+ 0046761c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 0046761c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046761c ["COPY", "register:5008:8", ["const:0:8"]]
+ 0046761c ["COPY", "register:5010:8", ["const:0:8"]]
- 00444784 bytes 004143fd
+ 0046761c bytes 00ad46fd
- 00444788 ["COPY", "register:4040:8", ["const:2b2000:8"]]
- 00444788 bytes 68f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad3952d719fe296f1bb32c6f4f2746a3"></a>

### [`004447a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/004447a4.md) → [`0046763c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046763c.md) FUN_0046763c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009ea010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea010.md) [`009ea540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea540.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00a46f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46f0c.md) [`00a4743c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a4743c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00467648",
      "incomplete_value": true,
      "site": "00467654",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004447b0",
      "incomplete_value": true,
      "site": "004447bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:680:8"
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
      "definition_site": "0046764c",
      "incomplete_value": true,
      "site": "00467658",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004447b4",
      "incomplete_value": true,
      "site": "004447c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:688:8"
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
      "00467648",
      "READ",
      [
        "storage",
        "002b2680",
        null,
        "undefined8"
      ]
    ],
    [
      "0046764c",
      "READ",
      [
        "storage",
        "002b2688",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00467648",
      "READ",
      [
        "storage",
        "002c3d58",
        null,
        "undefined8"
      ]
    ],
    [
      "0046764c",
      "READ",
      [
        "storage",
        "002c3d60",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004447a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/004447a4.md#insn-004447a4) · [`004447a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/004447a4.md#insn-004447a8) · [`004447b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/004447a4.md#insn-004447b0)
- 新版 [`0046763c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046763c.md#insn-0046763c) · [`00467640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046763c.md#insn-00467640) · [`00467648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046763c.md#insn-00467648)

~~~diff
- 004447a4 ["COPY", "register:4040:8", ["const:2b2000:8"]]
+ 0046763c ["COPY", "register:4040:8", ["const:2c3000:8"]]
- 004447a4 bytes 68f3ffd0
+ 0046763c bytes e8f2ff90
- 004447a8 ["COPY", "register:4048:8", ["const:2b2000:8"]]
+ 00467640 ["COPY", "register:4048:8", ["const:2c3000:8"]]
- 004447a8 bytes 69f3ffd0
+ 00467640 bytes e9f2ff90
- 004447b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:680:8"]]
- 004447b0 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
- 004447b0 ["COPY", "register:5048:8", ["const:0:8"]]
- 004447b0 ["COPY", "register:5050:8", ["const:0:8"]]
+ 00467648 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 00467648 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00467648 ["COPY", "register:5048:8", ["const:0:8"]]
+ 00467648 ["COPY", "register:5050:8", ["const:0:8"]]
- 004447b0 bytes 024143fd
+ 00467648 bytes 02ad46fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9d30cd5f7d360beb189061146105bc1"></a>

### [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) → [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) FUN_00467820

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 151件 [`005a02e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a0/005a02e8.md) [`005a33f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a33f8.md) [`005bb714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb714.md) [`005bf364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bf/005bf364.md) [`005c8548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8548.md) · 呼出先 5件 [`00444a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444a18.md) [`00444a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444a44.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 154件 [`005c4918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md) [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) [`005e03e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e03e4.md) [`005e4034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4034.md) [`005ed234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005ed234.md) · 呼出先 5件 [`004678b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004678b0.md) [`004678dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004678dc.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 63.33% / 新版 63.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00467854",
      "incomplete_value": false,
      "site": "00467858",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004449bc",
      "incomplete_value": false,
      "site": "004449c0",
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
            "const:d50:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00467868",
      "value": [
        "leaf",
        "ram:4678b0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004449d0",
      "value": [
        "leaf",
        "ram:444a18:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00467864",
      "incomplete_value": false,
      "site": "00467868",
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
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004449cc",
      "incomplete_value": false,
      "site": "004449d0",
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
            "const:ce8:8"
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
      "00467834",
      "READ",
      [
        "storage",
        "00c24d50",
        null,
        "undefined1"
      ]
    ],
    [
      "00467840",
      "DATA",
      [
        "storage",
        "00c24ce8",
        null,
        null
      ]
    ],
    [
      "00467854",
      "PARAM",
      [
        "storage",
        "00c24d50",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00467834",
      "READ",
      [
        "storage",
        "00ca4810",
        null,
        "undefined1"
      ]
    ],
    [
      "00467840",
      "DATA",
      [
        "storage",
        "00ca47a8",
        null,
        null
      ]
    ],
    [
      "00467854",
      "PARAM",
      [
        "storage",
        "00ca4810",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004449c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md#insn-004449c0) · [`004449d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md#insn-004449d0) · [`004449ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md#insn-004449ec)
- 新版 [`00467858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md#insn-00467858) · [`00467868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md#insn-00467868) · [`00467884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md#insn-00467884)

~~~diff
- 004449c0 ["INT_ADD", "register:40f0:8", ["const:4449c0:8", "const:4:8"]]
- 004449c0 ["CALL", null, ["callee:00c57a50:8"]]
+ 00467858 ["INT_ADD", "register:40f0:8", ["const:467858:8", "const:4:8"]]
+ 00467858 ["CALL", null, ["callee:00c57a50:8"]]
- 004449c0 bytes 90591e94
+ 00467858 bytes 7ec01f94
- 004449d0 ["INT_ADD", "register:40f0:8", ["const:4449d0:8", "const:4:8"]]
- 004449d0 ["CALL", null, ["ram:444a18:8"]]
+ 00467868 ["INT_ADD", "register:40f0:8", ["const:467868:8", "const:4:8"]]
+ 00467868 ["CALL", null, ["ram:4678b0:8"]]
- 004449d0 bytes 12000094
+ 00467868 bytes 12000094
- 004449ec ["INT_ADD", "register:40f0:8", ["const:4449ec:8", "const:4:8"]]
- 004449ec ["CALL", null, ["callee:00c57a30:8"]]
+ 00467884 ["INT_ADD", "register:40f0:8", ["const:467884:8", "const:4:8"]]
+ 00467884 ["CALL", null, ["callee:00c57a30:8"]]
- 004449ec bytes 7d591e94
+ 00467884 bytes 6bc01f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28d9cb14d6ba9dee14b3b50594f02adc"></a>

### [`00444a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444a94.md) → [`0046792c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md) FUN_0046792c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00acc348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc348.md) · 呼出先 11件 [`00444ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444ee4.md) [`00449b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449b7c.md) [`00449c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md) [`0053774c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053774c.md) [`005377cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377cc.md)
- 新版 呼出元 1件 [`00b2bdd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bdd8.md) · 呼出先 11件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0046ca14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca14.md) [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md) [`0055a5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5e4.md) [`0055a664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a664.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.14% / 新版 90.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004679e4",
      "incomplete_value": true,
      "site": "004679ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00444b4c",
      "incomplete_value": true,
      "site": "00444b54",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:290:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00467980",
      "incomplete_value": false,
      "site": "00467984",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00444ae8",
      "incomplete_value": false,
      "site": "00444aec",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00467990",
      "value": [
        "leaf",
        "ram:85ad18:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00444af8",
      "value": [
        "leaf",
        "ram:828da0:8"
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
      "00467980",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00467990",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00828da0"
      ]
    ],
    [
      "004679a4",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00467980",
      "PARAM",
      [
        "storage",
        "00ca4870",
        null,
        "undefined8"
      ]
    ],
    [
      "00467990",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0085ad18"
      ]
    ],
    [
      "004679a4",
      "PARAM",
      [
        "storage",
        "00ca4870",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00444aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444a94.md#insn-00444aec) · [`00444af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444a94.md#insn-00444af8) · [`00444b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444a94.md#insn-00444b10)
- 新版 [`00467984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md#insn-00467984) · [`00467990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md#insn-00467990) · [`004679a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md#insn-004679a8)

~~~diff
- 00444aec ["INT_ADD", "register:40f0:8", ["const:444aec:8", "const:4:8"]]
- 00444aec ["CALL", null, ["callee:0046ca14:8"]]
+ 00467984 ["INT_ADD", "register:40f0:8", ["const:467984:8", "const:4:8"]]
+ 00467984 ["CALL", null, ["callee:0046ca14:8"]]
- 00444aec bytes 24140094
+ 00467984 bytes 24140094
- 00444af8 ["INT_ADD", "register:40f0:8", ["const:444af8:8", "const:4:8"]]
- 00444af8 ["CALL", null, ["ram:828da0:8"]]
+ 00467990 ["INT_ADD", "register:40f0:8", ["const:467990:8", "const:4:8"]]
+ 00467990 ["CALL", null, ["ram:85ad18:8"]]
- 00444af8 bytes aa900f94
+ 00467990 bytes e2cc0f94
- 00444b10 ["INT_ADD", "register:40f0:8", ["const:444b10:8", "const:4:8"]]
- 00444b10 ["CALL", null, ["callee:0046cacc:8"]]
+ 004679a8 ["INT_ADD", "register:40f0:8", ["const:4679a8:8", "const:4:8"]]
+ 004679a8 ["CALL", null, ["callee:0046cacc:8"]]
- 00444b10 bytes 49140094
+ 004679a8 bytes 49140094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fd532c3382f9a037e017aefee04ce5b"></a>

### [`00444bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444bb0.md) → [`00467a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md) FUN_00467a48

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`005cf984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cf/005cf984.md) [`005d0044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d0/005d0044.md) [`006369bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00636/006369bc.md) [`00637320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637320.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 4件 [`00449b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449b7c.md) [`00449c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00828da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00828/00828da0.md)
- 新版 呼出元 11件 [`005f466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f4/005f466c.md) [`005f4d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f4/005f4d2c.md) [`0065cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md) [`0065d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065d5f0.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 4件 [`0046ca14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca14.md) [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0085ad18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085a/0085ad18.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00467a64",
      "incomplete_value": true,
      "site": "00467a6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:768:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00444bcc",
      "incomplete_value": true,
      "site": "00444bd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00467a78",
      "value": [
        "leaf",
        "ram:85ad18:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00444be0",
      "value": [
        "leaf",
        "ram:828da0:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00467a84",
      "incomplete_value": false,
      "site": "00467a88",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00444bec",
      "incomplete_value": false,
      "site": "00444bf0",
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
            "const:db0:8"
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
      "00467a64",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00467a64",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00467a78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00828da0"
      ]
    ]
  ],
  "added": [
    [
      "00467a64",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ],
    [
      "00467a64",
      "PARAM",
      [
        "storage",
        "00ca4870",
        null,
        "undefined8"
      ]
    ],
    [
      "00467a78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0085ad18"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00444bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444bb0.md#insn-00444bd4) · [`00444be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444bb0.md#insn-00444be0) · [`00444bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444bb0.md#insn-00444bf0)
- 新版 [`00467a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md#insn-00467a6c) · [`00467a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md#insn-00467a78) · [`00467a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md#insn-00467a88)

~~~diff
- 00444bd4 ["INT_ADD", "register:40f0:8", ["const:444bd4:8", "const:4:8"]]
- 00444bd4 ["CALL", null, ["callee:0046ca14:8"]]
+ 00467a6c ["INT_ADD", "register:40f0:8", ["const:467a6c:8", "const:4:8"]]
+ 00467a6c ["CALL", null, ["callee:0046ca14:8"]]
- 00444bd4 bytes ea130094
+ 00467a6c bytes ea130094
- 00444be0 ["INT_ADD", "register:40f0:8", ["const:444be0:8", "const:4:8"]]
- 00444be0 ["CALL", null, ["ram:828da0:8"]]
+ 00467a78 ["INT_ADD", "register:40f0:8", ["const:467a78:8", "const:4:8"]]
+ 00467a78 ["CALL", null, ["ram:85ad18:8"]]
- 00444be0 bytes 70900f94
+ 00467a78 bytes a8cc0f94
- 00444bf0 ["INT_ADD", "register:40f0:8", ["const:444bf0:8", "const:4:8"]]
- 00444bf0 ["CALL", null, ["callee:0046cacc:8"]]
+ 00467a88 ["INT_ADD", "register:40f0:8", ["const:467a88:8", "const:4:8"]]
+ 00467a88 ["CALL", null, ["callee:0046cacc:8"]]
- 00444bf0 bytes 11140094
+ 00467a88 bytes 11140094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7060b0ff5b51923bf81568165ae50e7"></a>

### [`00444c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c24.md) → [`00467abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467abc.md) FUN_00467abc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`006994e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00699/006994e8.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 3件 [`00444ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444ee4.md) [`005377cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377cc.md) [`005377d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377d0.md)
- 新版 呼出元 4件 [`006bf84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bf/006bf84c.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 3件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0055a664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a664.md) [`0055a668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a668.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

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
      "site": "00467ad4",
      "value": [
        "leaf",
        "ram:55a664:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00444c3c",
      "value": [
        "leaf",
        "ram:5377cc:8"
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
      "00467ad4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005377cc"
      ]
    ],
    [
      "00467ae8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005377d0"
      ]
    ]
  ],
  "added": [
    [
      "00467ad4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a664"
      ]
    ],
    [
      "00467ae8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a668"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00444c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c24.md#insn-00444c3c) · [`00444c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c24.md#insn-00444c38) · [`00444c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c24.md#insn-00444c50)
- 新版 [`00467ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467abc.md#insn-00467ad4) · [`00467ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467abc.md#insn-00467ad0) · [`00467ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467abc.md#insn-00467ae8)

~~~diff
- 00444c3c ["INT_ADD", "register:40f0:8", ["const:444c3c:8", "const:4:8"]]
- 00444c3c ["CALL", null, ["ram:5377cc:8"]]
+ 00467ad4 ["INT_ADD", "register:40f0:8", ["const:467ad4:8", "const:4:8"]]
+ 00467ad4 ["CALL", null, ["ram:55a664:8"]]
- 00444c3c bytes e4ca0394
+ 00467ad4 bytes e4ca0394
- 00444c38 ["INT_ADD", "register:40f0:8", ["const:444c38:8", "const:4:8"]]
- 00444c38 ["CALL", null, ["callee:00467d7c:8"]]
+ 00467ad0 ["INT_ADD", "register:40f0:8", ["const:467ad0:8", "const:4:8"]]
+ 00467ad0 ["CALL", null, ["callee:00467d7c:8"]]
- 00444c38 bytes ab000094
+ 00467ad0 bytes ab000094
- 00444c50 ["BRANCH", null, ["ram:5377d0:8"]]
+ 00467ae8 ["BRANCH", null, ["ram:55a668:8"]]
- 00444c50 bytes e0ca0314
+ 00467ae8 bytes e0ca0314
~~~


<a id="compare-addad32c785245bec7ce66f15ae463ea"></a>

### [`00444fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fd4.md) → [`00467e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e6c.md) FUN_00467e6c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005c8548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8548.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`0075f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075f/0075f8cc.md) · 呼出先 5件 [`00444ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444ee4.md) [`005377cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377cc.md) [`005377d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377d0.md) [`005377d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377d4.md) [`005377d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377d8.md)
- 新版 呼出元 3件 [`005ed234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005ed234.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) · 呼出先 5件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0055a664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a664.md) [`0055a668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a668.md) [`0055a66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a66c.md) [`0055a670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a670.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

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
      "site": "00467e8c",
      "value": [
        "leaf",
        "ram:55a664:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00444ff4",
      "value": [
        "leaf",
        "ram:5377cc:8"
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
      "site": "00467e98",
      "value": [
        "leaf",
        "ram:55a668:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00445000",
      "value": [
        "leaf",
        "ram:5377d0:8"
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
      "site": "00467ec0",
      "value": [
        "leaf",
        "ram:55a670:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00445028",
      "value": [
        "leaf",
        "ram:5377d8:8"
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
      "00467e8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005377cc"
      ]
    ],
    [
      "00467e98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005377d0"
      ]
    ],
    [
      "00467ec0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005377d8"
      ]
    ]
  ],
  "added": [
    [
      "00467e8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a664"
      ]
    ],
    [
      "00467e98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a668"
      ]
    ],
    [
      "00467ec0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a670"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00444ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fd4.md#insn-00444ff4) · [`00445000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fd4.md#insn-00445000) · [`00445028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fd4.md#insn-00445028)
- 新版 [`00467e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e6c.md#insn-00467e8c) · [`00467e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e6c.md#insn-00467e98) · [`00467ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e6c.md#insn-00467ec0)

~~~diff
- 00444ff4 ["INT_ADD", "register:40f0:8", ["const:444ff4:8", "const:4:8"]]
- 00444ff4 ["CALL", null, ["ram:5377cc:8"]]
+ 00467e8c ["INT_ADD", "register:40f0:8", ["const:467e8c:8", "const:4:8"]]
+ 00467e8c ["CALL", null, ["ram:55a664:8"]]
- 00444ff4 bytes f6c90394
+ 00467e8c bytes f6c90394
- 00445000 ["INT_ADD", "register:40f0:8", ["const:445000:8", "const:4:8"]]
- 00445000 ["CALL", null, ["ram:5377d0:8"]]
+ 00467e98 ["INT_ADD", "register:40f0:8", ["const:467e98:8", "const:4:8"]]
+ 00467e98 ["CALL", null, ["ram:55a668:8"]]
- 00445000 bytes f4c90394
+ 00467e98 bytes f4c90394
- 00445028 ["INT_ADD", "register:40f0:8", ["const:445028:8", "const:4:8"]]
- 00445028 ["CALL", null, ["ram:5377d8:8"]]
+ 00467ec0 ["INT_ADD", "register:40f0:8", ["const:467ec0:8", "const:4:8"]]
+ 00467ec0 ["CALL", null, ["ram:55a670:8"]]
- 00445028 bytes ecc90394
+ 00467ec0 bytes ecc90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8176bfcb3c94fa6404c744c15a177400"></a>

### [`004452e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/004452e8.md) → [`00468180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468180.md) FUN_00468180

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`005c8548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8548.md) [`005ca880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ca/005ca880.md) [`0068fe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068f/0068fe30.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) [`008f17a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f1/008f17a8.md) · 呼出先 12件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00444ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444ee4.md) [`00445610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445610.md) [`00445628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445628.md) [`00449574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449574.md)
- 新版 呼出元 5件 [`005ed234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005ed234.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) [`006b6184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b6/006b6184.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`00925834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00925/00925834.md) · 呼出先 12件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`004684a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684a8.md) [`004684c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684c0.md) [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md)

変更の種類 branch_value, call_argument_candidate, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 89.11% / 新版 89.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 4件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046823c",
      "incomplete_value": true,
      "site": "0046823c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004453a4",
      "incomplete_value": true,
      "site": "004453a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00468334",
      "incomplete_value": false,
      "site": "00468334",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044549c",
      "incomplete_value": false,
      "site": "0044549c",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00468334",
      "incomplete_value": false,
      "site": "00468334",
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
                "const:818:8"
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
      "definition_site": "0044549c",
      "incomplete_value": false,
      "site": "0044549c",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:d58:8"
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
    "ordinal": 36,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004681bc",
      "READ",
      [
        "storage",
        "00c24d70",
        null,
        "undefined1"
      ]
    ],
    [
      "004681d8",
      "READ",
      [
        "storage",
        "00c24d58",
        null,
        "undefined8"
      ]
    ],
    [
      "004681e0",
      "WRITE",
      [
        "storage",
        "00c24d60",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004681bc",
      "READ",
      [
        "storage",
        "00ca4830",
        null,
        "undefined1"
      ]
    ],
    [
      "004681d8",
      "READ",
      [
        "storage",
        "00ca4818",
        null,
        "undefined8"
      ]
    ],
    [
      "004681e0",
      "WRITE",
      [
        "storage",
        "00ca4820",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004453a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/004452e8.md#insn-004453a4) · [`004454fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/004452e8.md#insn-004454fc) · [`0044557c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/004452e8.md#insn-0044557c)
- 新版 [`0046823c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468180.md#insn-0046823c) · [`00468394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468180.md#insn-00468394) · [`00468414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468180.md#insn-00468414)

~~~diff
- 004453a4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d60:8"]]
- 004453a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
+ 0046823c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:820:8"]]
+ 0046823c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 004453a4 bytes 5cb106f9
+ 0046823c bytes 5c1104f9
- 004454fc ["INT_ADD", "register:40f0:8", ["const:4454fc:8", "const:4:8"]]
- 004454fc ["CALL", null, ["callee:004684c0:8"]]
+ 00468394 ["INT_ADD", "register:40f0:8", ["const:468394:8", "const:4:8"]]
+ 00468394 ["CALL", null, ["callee:004684c0:8"]]
- 004454fc bytes 4b000094
+ 00468394 bytes 4b000094
- 0044557c ["INT_ADD", "register:40f0:8", ["const:44557c:8", "const:4:8"]]
- 0044557c ["CALL", null, ["callee:0046c40c:8"]]
+ 00468414 ["INT_ADD", "register:40f0:8", ["const:468414:8", "const:4:8"]]
+ 00468414 ["CALL", null, ["callee:0046c40c:8"]]
- 0044557c bytes fe0f0094
+ 00468414 bytes fe0f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16d94f870ca067a219d2c4c96659fdbf"></a>

### [`00449574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449574.md) → [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) FUN_0046c40c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`004452e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/004452e8.md) [`00445628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445628.md) [`005325a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005325a0.md) [`00532f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532f34.md) [`00536d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/00536d38.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 10件 [`00468180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468180.md) [`004684c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684c0.md) [`00555438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md) [`00555dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md) [`00559bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559bd0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0046c41c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00449584",
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
      "definition_site": "0046c418",
      "incomplete_value": false,
      "site": "0046c41c",
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
      "definition_site": "00449580",
      "incomplete_value": false,
      "site": "00449584",
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
      "0046c418",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0046c41c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0046c418",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0046c41c",
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

- 旧版 [`00449584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449574.md#insn-00449584) · [`0044957c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449574.md#insn-0044957c) · [`00449580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449574.md#insn-00449580)
- 新版 [`0046c41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md#insn-0046c41c) · [`0046c414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md#insn-0046c414) · [`0046c418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md#insn-0046c418)

~~~diff
- 00449584 ["INT_ADD", "register:40f0:8", ["const:449584:8", "const:4:8"]]
- 00449584 ["CALL", null, ["ram:418c38:8"]]
+ 0046c41c ["INT_ADD", "register:40f0:8", ["const:46c41c:8", "const:4:8"]]
+ 0046c41c ["CALL", null, ["ram:43b738:8"]]
- 00449584 bytes ad3dff97
+ 0046c41c bytes c73cff97
- 0044957c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0046c414 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0044957c bytes e0f2ffd0
+ 0046c414 bytes 40f2fff0
- 00449580 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00449580 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00449580 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00449580 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046c418 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0046c418 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c418 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c418 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00449580 bytes 00740e91
+ 0046c418 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e16f79a7d98bc4d57a5dd9b16f716f61"></a>

### [`00449588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449588.md) → [`0046c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md) FUN_0046c420

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`00445124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445124.md) [`00536a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/00536a8c.md) [`005b9970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9970.md) [`007de628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007de/007de628.md) [`007df5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007df/007df5ac.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 7件 [`00467fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467fbc.md) [`00559924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md) [`005de640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005de640.md) [`00812e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00812/00812e8c.md) [`00813e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813e10.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0046c430",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00449598",
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
      "definition_site": "0046c42c",
      "incomplete_value": false,
      "site": "0046c430",
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
      "definition_site": "00449594",
      "incomplete_value": false,
      "site": "00449598",
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
      "0046c42c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0046c430",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0046c42c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0046c430",
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

- 旧版 [`00449598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449588.md#insn-00449598) · [`00449590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449588.md#insn-00449590) · [`00449594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449588.md#insn-00449594)
- 新版 [`0046c430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md#insn-0046c430) · [`0046c428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md#insn-0046c428) · [`0046c42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md#insn-0046c42c)

~~~diff
- 00449598 ["INT_ADD", "register:40f0:8", ["const:449598:8", "const:4:8"]]
- 00449598 ["CALL", null, ["ram:418c38:8"]]
+ 0046c430 ["INT_ADD", "register:40f0:8", ["const:46c430:8", "const:4:8"]]
+ 0046c430 ["CALL", null, ["ram:43b738:8"]]
- 00449598 bytes a83dff97
+ 0046c430 bytes c23cff97
- 00449590 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0046c428 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00449590 bytes e0f2ffd0
+ 0046c428 bytes 40f2fff0
- 00449594 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00449594 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00449594 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00449594 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046c42c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0046c42c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c42c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c42c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00449594 bytes 00740e91
+ 0046c42c bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be79a93f77e8c4e1f094953f4418171b"></a>

### [`0044973c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/0044973c.md) → [`0046c5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5d4.md) FUN_0046c5d4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0044959c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/0044959c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0046c434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c434.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0046c5e4",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0044974c",
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
      "definition_site": "0046c5e0",
      "incomplete_value": false,
      "site": "0046c5e4",
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
      "definition_site": "00449748",
      "incomplete_value": false,
      "site": "0044974c",
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
      "0046c5e0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0046c5e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0046c5e0",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0046c5e4",
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

- 旧版 [`0044974c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/0044973c.md#insn-0044974c) · [`00449744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/0044973c.md#insn-00449744) · [`00449748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/0044973c.md#insn-00449748)
- 新版 [`0046c5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5d4.md#insn-0046c5e4) · [`0046c5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5d4.md#insn-0046c5dc) · [`0046c5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5d4.md#insn-0046c5e0)

~~~diff
- 0044974c ["INT_ADD", "register:40f0:8", ["const:44974c:8", "const:4:8"]]
- 0044974c ["CALL", null, ["ram:418c38:8"]]
+ 0046c5e4 ["INT_ADD", "register:40f0:8", ["const:46c5e4:8", "const:4:8"]]
+ 0046c5e4 ["CALL", null, ["ram:43b738:8"]]
- 0044974c bytes 3b3dff97
+ 0046c5e4 bytes 553cff97
- 00449744 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0046c5dc ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00449744 bytes e0f2ffd0
+ 0046c5dc bytes 40f2fff0
- 00449748 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00449748 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00449748 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00449748 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046c5e0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0046c5e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c5e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c5e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00449748 bytes 00740e91
+ 0046c5e0 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-934b44eb6cabbeb28d0f91c80a835623"></a>

### [`00449750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449750.md) → [`0046c5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5e8.md) _INIT_12

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046c624",
      "incomplete_value": true,
      "site": "0046c640",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044978c",
      "incomplete_value": true,
      "site": "004497a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0046c648",
      "incomplete_value": true,
      "site": "0046c664",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004497b0",
      "incomplete_value": true,
      "site": "004497cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0046c668",
      "incomplete_value": true,
      "site": "0046c684",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004497d0",
      "incomplete_value": true,
      "site": "004497ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0046c624",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0046c648",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0046c668",
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
      "0046c624",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0046c648",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0046c668",
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

- 旧版 [`004498b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449750.md#insn-004498b0) · [`00449984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449750.md#insn-00449984) · [`00449778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449750.md#insn-00449778)
- 新版 [`0046c748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5e8.md#insn-0046c748) · [`0046c81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5e8.md#insn-0046c81c) · [`0046c610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5e8.md#insn-0046c610)

~~~diff
- 004498b0 ["INT_ADD", "register:40f0:8", ["const:4498b0:8", "const:4:8"]]
- 004498b0 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0046c748 ["INT_ADD", "register:40f0:8", ["const:46c748:8", "const:4:8"]]
+ 0046c748 ["CALL", null, ["callee:0043b7b8:8"]]
- 004498b0 bytes 023dff97
+ 0046c748 bytes 1c3cff97
- 00449984 ["INT_ADD", "register:40f0:8", ["const:449984:8", "const:4:8"]]
- 00449984 ["CALL", null, ["callee:00c57a30:8"]]
+ 0046c81c ["INT_ADD", "register:40f0:8", ["const:46c81c:8", "const:4:8"]]
+ 0046c81c ["CALL", null, ["callee:00c57a30:8"]]
- 00449984 bytes 97451e94
+ 0046c81c bytes 85ac1f94
- 00449778 ["COPY", "register:4098:8", ["const:c24000:8"]]
+ 0046c610 ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 00449778 bytes d33e00f0
+ 0046c610 bytes d3410090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-409711d995b5528423f00145d78c14f6"></a>

### [`00449bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bcc.md) → [`0046ca64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca64.md) FUN_0046ca64

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00acbd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd14.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00b2b7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046ca6c",
      "incomplete_value": false,
      "site": "0046ca6c",
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
            "const:8b4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00449bd4",
      "incomplete_value": false,
      "site": "00449bd4",
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
            "const:df4:8"
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
      "0046ca6c",
      "WRITE",
      [
        "storage",
        "00c24df4",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046ca6c",
      "WRITE",
      [
        "storage",
        "00ca48b4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00449bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bcc.md#insn-00449bd4) · [`00449bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bcc.md#insn-00449bcc)
- 新版 [`0046ca6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca64.md#insn-0046ca6c) · [`0046ca64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca64.md#insn-0046ca64)

~~~diff
- 00449bd4 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00449bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:df4:8"]]
- 00449bd4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0046ca6c ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0046ca6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:8b4:8"]]
+ 0046ca6c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00449bd4 bytes 09d13739
+ 0046ca6c bytes 09d12239
- 00449bcc ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0046ca64 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00449bcc bytes c83e00f0
+ 0046ca64 bytes c8410090
~~~


<a id="compare-885b7c0b0dfdfe0c0e368a1a722fba57"></a>

### [`00449c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md) → [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md) FUN_0046cacc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 26件 [`00444a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444a94.md) [`00444bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444bb0.md) [`0046dc5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046dc5c.md) [`0046f248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f248.md) [`0046f694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f694.md) · 呼出先 0件 
- 新版 呼出元 26件 [`0046792c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md) [`00467a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md) [`00490af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490af4.md) [`004920e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md) [`0049252c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049252c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0046cb0c",
      "incomplete_value": true,
      "site": "0046cb10",
      "value": [
        "TRUNC",
        "4",
        [
          [
            "FLOAT_DIV",
            "4",
            [
              "FLOAT_MULT",
              "INT2FLOAT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00449c74",
      "incomplete_value": true,
      "site": "00449c78",
      "value": [
        "TRUNC",
        "4",
        [
          [
            "FLOAT_DIV",
            "4",
            [
              "FLOAT_MULT",
              "INT2FLOAT"
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
      "0046caf0",
      "READ",
      [
        "storage",
        "00c24de4",
        null,
        "undefined4"
      ]
    ],
    [
      "0046caf4",
      "READ",
      [
        "storage",
        "00c24db8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0046caf0",
      "READ",
      [
        "storage",
        "00ca48a4",
        null,
        "undefined4"
      ]
    ],
    [
      "0046caf4",
      "READ",
      [
        "storage",
        "00ca4878",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00449c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md#insn-00449c4c) · [`00449c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md#insn-00449c50)
- 新版 [`0046cae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md#insn-0046cae4) · [`0046cae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md#insn-0046cae8)

~~~diff
- 00449c4c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0046cae4 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00449c4c bytes c83e00f0
+ 0046cae4 bytes c8410090
- 00449c50 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 00449c50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00449c50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00449c50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046cae8 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 0046cae8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046cae8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046cae8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00449c50 bytes 08e13691
+ 0046cae8 bytes 08e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ca73af71d04f0d413fec332b6485161"></a>

### [`00449e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449e1c.md) → [`0046ccb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ccb4.md) _INIT_13

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 80.54% / 新版 80.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 8件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046ccf0",
      "incomplete_value": true,
      "site": "0046cd0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00449e58",
      "incomplete_value": true,
      "site": "00449e74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0046cd14",
      "incomplete_value": true,
      "site": "0046cd30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00449e7c",
      "incomplete_value": true,
      "site": "00449e98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0046cd34",
      "incomplete_value": true,
      "site": "0046cd50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00449e9c",
      "incomplete_value": true,
      "site": "00449eb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0046ccf0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0046cd14",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0046cd34",
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
      "0046ccf0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0046cd14",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0046cd34",
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

- 旧版 [`00449f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449e1c.md#insn-00449f7c) · [`0044a050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449e1c.md#insn-0044a050) · [`00449e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449e1c.md#insn-00449e44)
- 新版 [`0046ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ccb4.md#insn-0046ce14) · [`0046cee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ccb4.md#insn-0046cee8) · [`0046ccdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ccb4.md#insn-0046ccdc)

~~~diff
- 00449f7c ["INT_ADD", "register:40f0:8", ["const:449f7c:8", "const:4:8"]]
- 00449f7c ["CALL", null, ["callee:0043b7b8:8"]]
+ 0046ce14 ["INT_ADD", "register:40f0:8", ["const:46ce14:8", "const:4:8"]]
+ 0046ce14 ["CALL", null, ["callee:0043b7b8:8"]]
- 00449f7c bytes 4f3bff97
+ 0046ce14 bytes 693aff97
- 0044a050 ["INT_ADD", "register:40f0:8", ["const:44a050:8", "const:4:8"]]
- 0044a050 ["CALL", null, ["callee:00c57a30:8"]]
+ 0046cee8 ["INT_ADD", "register:40f0:8", ["const:46cee8:8", "const:4:8"]]
+ 0046cee8 ["CALL", null, ["callee:00c57a30:8"]]
- 0044a050 bytes e4431e94
+ 0046cee8 bytes d2aa1f94
- 00449e44 ["COPY", "register:4098:8", ["const:c24000:8"]]
+ 0046ccdc ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 00449e44 bytes d33e00f0
+ 0046ccdc bytes d3410090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b29e52017ef2f80241b1ef64988bd9b9"></a>

### [`0044a1cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a1cc.md) → [`0046d064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d064.md) FUN_0046d064

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 4件 [`0044a240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a240.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 2件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 4件 [`0046d0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0d8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_destination, store_value

命令の説明率　旧版 62.07% / 新版 62.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `store_destination` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046d0b8",
      "incomplete_value": false,
      "site": "0046d0b8",
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
                "const:8b8:8"
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
      "definition_site": "0044a220",
      "incomplete_value": false,
      "site": "0044a220",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:df8:8"
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046d0bc",
      "incomplete_value": false,
      "site": "0046d0bc",
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
                "const:8b8:8"
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
      "definition_site": "0044a224",
      "incomplete_value": false,
      "site": "0044a224",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:df8:8"
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
      "definition_site": "0046d0c0",
      "incomplete_value": false,
      "site": "0046d0c0",
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
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044a228",
      "incomplete_value": false,
      "site": "0044a228",
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
            "const:df8:8"
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
      "0046d074",
      "READ",
      [
        "storage",
        "00c24e10",
        null,
        "undefined1"
      ]
    ],
    [
      "0046d080",
      "DATA",
      [
        "storage",
        "00c24df8",
        null,
        "undefined8"
      ]
    ],
    [
      "0046d090",
      "PARAM",
      [
        "storage",
        "00c24e10",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046d074",
      "READ",
      [
        "storage",
        "00ca48d0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046d080",
      "DATA",
      [
        "storage",
        "00ca48b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0046d090",
      "PARAM",
      [
        "storage",
        "00ca48d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044a1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a1cc.md#insn-0044a1fc) · [`0044a22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a1cc.md#insn-0044a22c) · [`0044a238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a1cc.md#insn-0044a238)
- 新版 [`0046d094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d064.md#insn-0046d094) · [`0046d0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d064.md#insn-0046d0c4) · [`0046d0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d064.md#insn-0046d0d0)

~~~diff
- 0044a1fc ["INT_ADD", "register:40f0:8", ["const:44a1fc:8", "const:4:8"]]
- 0044a1fc ["CALL", null, ["callee:00c57a50:8"]]
+ 0046d094 ["INT_ADD", "register:40f0:8", ["const:46d094:8", "const:4:8"]]
+ 0046d094 ["CALL", null, ["callee:00c57a50:8"]]
- 0044a1fc bytes 81431e94
+ 0046d094 bytes 6faa1f94
- 0044a22c ["INT_ADD", "register:40f0:8", ["const:44a22c:8", "const:4:8"]]
- 0044a22c ["CALL", null, ["callee:00c57a30:8"]]
+ 0046d0c4 ["INT_ADD", "register:40f0:8", ["const:46d0c4:8", "const:4:8"]]
+ 0046d0c4 ["CALL", null, ["callee:00c57a30:8"]]
- 0044a22c bytes 6d431e94
+ 0046d0c4 bytes 5baa1f94
- 0044a238 ["INT_ADD", "register:40f0:8", ["const:44a238:8", "const:4:8"]]
- 0044a238 ["CALL", null, ["callee:00c57a70:8"]]
+ 0046d0d0 ["INT_ADD", "register:40f0:8", ["const:46d0d0:8", "const:4:8"]]
+ 0046d0d0 ["CALL", null, ["callee:00c57a70:8"]]
- 0044a238 bytes 7a431e94
+ 0046d0d0 bytes 68aa1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ad86d0d624dfabb0f242df296e799c1"></a>

### [`0044a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a248.md) → [`0046d0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md) FUN_0046d0e0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 15件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.10% / 新版 89.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046d12c",
      "incomplete_value": false,
      "site": "0046d138",
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
    "old": {
      "definition_site": "0044a294",
      "incomplete_value": false,
      "site": "0044a2a0",
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
            "const:d78:8"
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
      "definition_site": "0046d150",
      "incomplete_value": true,
      "site": "0046d150",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2a3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044a2b8",
      "incomplete_value": true,
      "site": "0044a2b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:86a:8"
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
      "definition_site": "0046d148",
      "incomplete_value": true,
      "site": "0046d154",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044a2b0",
      "incomplete_value": true,
      "site": "0044a2bc",
      "value": [
        "LOAD",
        "8",
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
      "0046d138",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0046d140",
      "READ",
      [
        "storage",
        "0029586a",
        null,
        "string"
      ]
    ],
    [
      "0046d148",
      "READ",
      [
        "storage",
        "00295871",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0046d138",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0046d140",
      "READ",
      [
        "storage",
        "002a52a3",
        null,
        "string"
      ]
    ],
    [
      "0046d148",
      "READ",
      [
        "storage",
        "002a52aa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044a278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a248.md#insn-0044a278) · [`0044a28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a248.md#insn-0044a28c) · [`0044a290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a248.md#insn-0044a290)
- 新版 [`0046d110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md#insn-0046d110) · [`0046d124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md#insn-0046d124) · [`0046d128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md#insn-0046d128)

~~~diff
- 0044a278 ["INT_ADD", "register:40f0:8", ["const:44a278:8", "const:4:8"]]
- 0044a278 ["CALL", null, ["callee:0046d450:8"]]
+ 0046d110 ["INT_ADD", "register:40f0:8", ["const:46d110:8", "const:4:8"]]
+ 0046d110 ["CALL", null, ["callee:0046d450:8"]]
- 0044a278 bytes d0000094
+ 0046d110 bytes d0000094
- 0044a28c ["INT_ADD", "register:40f0:8", ["const:44a28c:8", "const:4:8"]]
- 0044a28c ["CALL", null, ["callee:00487de0:8"]]
+ 0046d124 ["INT_ADD", "register:40f0:8", ["const:46d124:8", "const:4:8"]]
+ 0046d124 ["CALL", null, ["callee:00487de0:8"]]
- 0044a28c bytes 2f6b0094
+ 0046d124 bytes 2f6b0094
- 0044a290 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0046d128 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0044a290 bytes e83c00b0
+ 0046d128 bytes a83f00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-200eb9fa49e348630613a387809a50cf"></a>

### [`0044a618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a618.md) → [`0046d4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d4b0.md) FUN_0046d4b0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md) [`00bdb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 73.91% / 新版 73.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046d4e0",
      "incomplete_value": true,
      "site": "0046d4e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0044a648",
      "incomplete_value": true,
      "site": "0044a650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046d4ec",
      "incomplete_value": true,
      "site": "0046d4ec",
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
      "definition_site": "0044a654",
      "incomplete_value": true,
      "site": "0044a654",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046d4fc",
      "incomplete_value": true,
      "site": "0046d4fc",
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "definition_site": "0044a664",
      "incomplete_value": true,
      "site": "0044a664",
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "0046d4cc",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "0046d4d0",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "0046d4dc",
      "READ",
      [
        "storage",
        "00c13458",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0046d4cc",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      "0046d4d0",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "0046d4dc",
      "READ",
      [
        "storage",
        "00c92e00",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044a628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a618.md#insn-0044a628) · [`0044a62c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a618.md#insn-0044a62c) · [`0044a634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a618.md#insn-0044a634)
- 新版 [`0046d4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d4b0.md#insn-0046d4c0) · [`0046d4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d4b0.md#insn-0046d4c4) · [`0046d4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d4b0.md#insn-0046d4cc)

~~~diff
- 0044a628 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0046d4c0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0044a628 bytes 883e0090
+ 0046d4c0 bytes 684100b0
- 0044a62c ["COPY", "register:40b0:8", ["const:c1a000:8"]]
+ 0046d4c4 ["COPY", "register:40b0:8", ["const:c9a000:8"]]
- 0044a62c bytes 963e0090
+ 0046d4c4 bytes 764100b0
- 0044a634 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
- 0044a634 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046d4cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7b0:8"]]
+ 0046d4cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0044a634 bytes 08e146f9
+ 0046d4cc bytes 08d943f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5331785e65d78bc623c0c3b30c715a3b"></a>

### [`0044a8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8e8.md) → [`0046d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d780.md) FUN_0046d780

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`009a6228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a6228.md) [`009a6234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a6234.md) [`009a6240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a6/009a6240.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 7件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)
- 新版 呼出元 5件 [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`009dbf88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbf88.md) [`009dbf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbf94.md) [`009dbfa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbfa0.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 7件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.22% / 新版 92.22%

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
      "site": "0046d814",
      "value": [
        "leaf",
        "ram:c57fa0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0044a97c",
      "value": [
        "leaf",
        "ram:bdb550:8"
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
      "site": "0046d86c",
      "value": [
        "leaf",
        "ram:46dac0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0044a9d4",
      "value": [
        "leaf",
        "ram:44ac28:8"
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
      "site": "0046d87c",
      "value": [
        "leaf",
        "ram:c57fd0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0044a9e4",
      "value": [
        "leaf",
        "ram:bdb580:8"
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
      "0046d7d8",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "0046d7dc",
      "READ",
      [
        "storage",
        "002b2a08",
        null,
        "undefined8"
      ]
    ],
    [
      "0046d814",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb550"
      ]
    ]
  ],
  "added": [
    [
      "0046d7d8",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0046d7dc",
      "READ",
      [
        "storage",
        "002c4108",
        null,
        "undefined8"
      ]
    ],
    [
      "0046d814",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57fa0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044a97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8e8.md#insn-0044a97c) · [`0044a9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8e8.md#insn-0044a9d4) · [`0044a9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8e8.md#insn-0044a9e4)
- 新版 [`0046d814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d780.md#insn-0046d814) · [`0046d86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d780.md#insn-0046d86c) · [`0046d87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d780.md#insn-0046d87c)

~~~diff
- 0044a97c ["INT_ADD", "register:40f0:8", ["const:44a97c:8", "const:4:8"]]
- 0044a97c ["CALL", null, ["ram:bdb550:8"]]
+ 0046d814 ["INT_ADD", "register:40f0:8", ["const:46d814:8", "const:4:8"]]
+ 0046d814 ["CALL", null, ["ram:c57fa0:8"]]
- 0044a97c bytes f5421e94
+ 0046d814 bytes e3a91f94
- 0044a9d4 ["INT_ADD", "register:40f0:8", ["const:44a9d4:8", "const:4:8"]]
- 0044a9d4 ["CALL", null, ["ram:44ac28:8"]]
+ 0046d86c ["INT_ADD", "register:40f0:8", ["const:46d86c:8", "const:4:8"]]
+ 0046d86c ["CALL", null, ["ram:46dac0:8"]]
- 0044a9d4 bytes 95000094
+ 0046d86c bytes 95000094
- 0044a9e4 ["INT_ADD", "register:40f0:8", ["const:44a9e4:8", "const:4:8"]]
- 0044a9e4 ["CALL", null, ["ram:bdb580:8"]]
+ 0046d87c ["INT_ADD", "register:40f0:8", ["const:46d87c:8", "const:4:8"]]
+ 0046d87c ["CALL", null, ["ram:c57fd0:8"]]
- 0044a9e4 bytes e7421e94
+ 0046d87c bytes d5a91f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bc1240ef5bf840f5dbcf5f8aef485d5"></a>

### [`0044b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md) → [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) FUN_0046e784

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 25件 [`005ba9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba9c0.md) [`005c0264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c0264.md) [`0065c134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065c/0065c134.md) [`00761d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761d08.md) [`0078b0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078b/0078b0ec.md) · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)
- 新版 呼出元 25件 [`005df690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df690.md) [`005e4f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4f34.md) [`00682424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682424.md) [`0078c1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078c/0078c1dc.md) [`007bbddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbddc.md) · 呼出先 1件 [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046e7b0",
      "incomplete_value": false,
      "site": "0046e7b8",
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
    "old": {
      "definition_site": "0044b918",
      "incomplete_value": false,
      "site": "0044b920",
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
            "const:7d9:8"
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
      "0046e7b0",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046e7b0",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md#insn-0044b920) · [`0044b914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md#insn-0044b914) · [`0044b918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md#insn-0044b918)
- 新版 [`0046e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md#insn-0046e7b8) · [`0046e7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md#insn-0046e7ac) · [`0046e7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md#insn-0046e7b0)

~~~diff
- 0044b920 ["INT_ADD", "register:40f0:8", ["const:44b920:8", "const:4:8"]]
- 0044b920 ["CALL", null, ["callee:00c57d90:8"]]
+ 0046e7b8 ["INT_ADD", "register:40f0:8", ["const:46e7b8:8", "const:4:8"]]
+ 0046e7b8 ["CALL", null, ["callee:00c57d90:8"]]
- 0044b920 bytes 883e1e94
+ 0046e7b8 bytes 76a51f94
- 0044b914 ["COPY", "register:4008:8", ["const:296000:8"]]
+ 0046e7ac ["COPY", "register:4008:8", ["const:2a6000:8"]]
- 0044b914 bytes 41f2fff0
+ 0046e7ac bytes c1f1ff90
- 0044b918 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 0044b918 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044b918 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044b918 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0046e7b0 ["COPY", "tmp:0:8", ["const:30e:8"]]
+ 0046e7b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0046e7b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0046e7b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044b918 bytes 21641f91
+ 0046e7b0 bytes 21380c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a81e25c11e7a9e0778dcb055f4bcea3"></a>

### [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) → [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) FUN_0046e864

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 38件 [`005baa68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005baa68.md) [`005c03a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c03a8.md) [`0065bee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bee8.md) [`007638b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/007638b8.md) [`00763940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763940.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)
- 新版 呼出元 38件 [`005df738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df738.md) [`005e5078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e5/005e5078.md) [`006821d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006821d8.md) [`0078dd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dd8c.md) [`0078de14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078de14.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046e8ac",
      "incomplete_value": false,
      "site": "0046e8b4",
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
    "old": {
      "definition_site": "0044ba14",
      "incomplete_value": false,
      "site": "0044ba1c",
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
            "const:7d9:8"
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
      "0046e8ac",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046e8ac",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ba1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md#insn-0044ba1c) · [`0044ba00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md#insn-0044ba00) · [`0044ba10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md#insn-0044ba10)
- 新版 [`0046e8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md#insn-0046e8b4) · [`0046e898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md#insn-0046e898) · [`0046e8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md#insn-0046e8a8)

~~~diff
- 0044ba1c ["INT_ADD", "register:40f0:8", ["const:44ba1c:8", "const:4:8"]]
- 0044ba1c ["CALL", null, ["callee:00c57d90:8"]]
+ 0046e8b4 ["INT_ADD", "register:40f0:8", ["const:46e8b4:8", "const:4:8"]]
+ 0046e8b4 ["CALL", null, ["callee:00c57d90:8"]]
- 0044ba1c bytes 493e1e94
+ 0046e8b4 bytes 37a51f94
- 0044ba00 ["INT_ADD", "register:40f0:8", ["const:44ba00:8", "const:4:8"]]
- 0044ba00 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0046e898 ["INT_ADD", "register:40f0:8", ["const:46e898:8", "const:4:8"]]
+ 0046e898 ["CALL", null, ["callee:00c57ab0:8"]]
- 0044ba00 bytes 983d1e94
+ 0046e898 bytes 86a41f94
- 0044ba10 ["COPY", "register:4008:8", ["const:296000:8"]]
+ 0046e8a8 ["COPY", "register:4008:8", ["const:2a6000:8"]]
- 0044ba10 bytes 41f2fff0
+ 0046e8a8 bytes c1f1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26b78ca3c05daa9850e2b2866ac275a8"></a>

### [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) → [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) FUN_0046e930

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 36件 [`005bcea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bcea8.md) [`005be404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) [`005c47c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c47c4.md) [`0060b7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b7bc.md) [`00614c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/00614c6c.md) · 呼出先 15件 [`0044d28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d28c.md) [`0044d490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d490.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)
- 新版 呼出元 36件 [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) [`006312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md) [`0063a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a764.md) · 呼出先 15件 [`00470124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470124.md) [`00470328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470328.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.20% / 新版 95.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046e974",
      "incomplete_value": false,
      "site": "0046e978",
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
    "old": {
      "definition_site": "0044badc",
      "incomplete_value": false,
      "site": "0044bae0",
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
            "const:d78:8"
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
      "definition_site": "0046ec6c",
      "incomplete_value": true,
      "site": "0046ec70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0044bdd4",
      "incomplete_value": true,
      "site": "0044bdd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "0046ec68",
      "incomplete_value": true,
      "site": "0046ec74",
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
      "definition_site": "0044bdd0",
      "incomplete_value": true,
      "site": "0044bddc",
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
      "0046e978",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0046e990",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "0046ec5c",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0046e978",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0046e990",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "0046ec5c",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044bb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md#insn-0044bb00) · [`0044bad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md#insn-0044bad0) · [`0044bad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md#insn-0044bad8)
- 新版 [`0046e998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md#insn-0046e998) · [`0046e968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md#insn-0046e968) · [`0046e970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md#insn-0046e970)

~~~diff
- 0044bb00 ["INT_ADD", "register:40f0:8", ["const:44bb00:8", "const:4:8"]]
- 0044bb00 ["CALL", null, ["callee:00c57d90:8"]]
+ 0046e998 ["INT_ADD", "register:40f0:8", ["const:46e998:8", "const:4:8"]]
+ 0046e998 ["CALL", null, ["callee:00c57d90:8"]]
- 0044bb00 bytes 103e1e94
+ 0046e998 bytes fea41f94
- 0044bad0 ["INT_ADD", "register:40f0:8", ["const:44bad0:8", "const:4:8"]]
- 0044bad0 ["CALL", null, ["callee:00487de0:8"]]
+ 0046e968 ["INT_ADD", "register:40f0:8", ["const:46e968:8", "const:4:8"]]
+ 0046e968 ["CALL", null, ["callee:00487de0:8"]]
- 0044bad0 bytes 1e650094
+ 0046e968 bytes 1e650094
- 0044bad8 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0046e970 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0044bad8 bytes e83c0090
+ 0046e970 bytes a83f00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-394d8f68e99554e84c1ead52faf2cf75"></a>

### [`0044c020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c020.md) → [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md) FUN_0046eeb8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 26件 [`005cc128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cc/005cc128.md) [`00658090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/00658090.md) [`006e4094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4094.md) [`00761d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761d08.md) [`007802c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00780/007802c0.md) · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)
- 新版 呼出元 26件 [`005f0e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0e14.md) [`0067e370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e370.md) [`0070dfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070dfc4.md) [`0078c1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078c/0078c1dc.md) [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) · 呼出先 1件 [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046eef8",
      "incomplete_value": false,
      "site": "0046ef00",
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
    "old": {
      "definition_site": "0044c060",
      "incomplete_value": false,
      "site": "0044c068",
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
            "const:7d9:8"
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
      "0046eef8",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046eef8",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c020.md#insn-0044c068) · [`0044c05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c020.md#insn-0044c05c) · [`0044c060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c020.md#insn-0044c060)
- 新版 [`0046ef00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md#insn-0046ef00) · [`0046eef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md#insn-0046eef4) · [`0046eef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md#insn-0046eef8)

~~~diff
- 0044c068 ["INT_ADD", "register:40f0:8", ["const:44c068:8", "const:4:8"]]
- 0044c068 ["CALL", null, ["callee:00c57d90:8"]]
+ 0046ef00 ["INT_ADD", "register:40f0:8", ["const:46ef00:8", "const:4:8"]]
+ 0046ef00 ["CALL", null, ["callee:00c57d90:8"]]
- 0044c068 bytes b63c1e94
+ 0046ef00 bytes a4a31f94
- 0044c05c ["COPY", "register:4008:8", ["const:296000:8"]]
+ 0046eef4 ["COPY", "register:4008:8", ["const:2a6000:8"]]
- 0044c05c bytes 41f2ffd0
+ 0046eef4 bytes c1f1ff90
- 0044c060 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 0044c060 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c060 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c060 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0046eef8 ["COPY", "tmp:0:8", ["const:30e:8"]]
+ 0046eef8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0046eef8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0046eef8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c060 bytes 21641f91
+ 0046eef8 bytes 21380c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b2485c26e27f354e21afa40e11916ce"></a>

### [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md) → [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) FUN_0046ef9c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 31件 [`005cc1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cc/005cc1d0.md) [`006581ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006581ec.md) [`0065bcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bcc8.md) [`006e41d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e41d8.md) [`007638b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/007638b8.md) · 呼出先 4件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)
- 新版 呼出元 31件 [`005f0ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0ebc.md) [`0067e4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e4cc.md) [`00681fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00681/00681fb8.md) [`0070e108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e108.md) [`0078dd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dd8c.md) · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046efd0",
      "incomplete_value": false,
      "site": "0046efd8",
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
    "old": {
      "definition_site": "0044c138",
      "incomplete_value": false,
      "site": "0044c140",
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
            "const:7d9:8"
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
      "0046efd0",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046efd0",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md#insn-0044c140) · [`0044c134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md#insn-0044c134) · [`0044c138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md#insn-0044c138)
- 新版 [`0046efd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md#insn-0046efd8) · [`0046efcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md#insn-0046efcc) · [`0046efd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md#insn-0046efd0)

~~~diff
- 0044c140 ["INT_ADD", "register:40f0:8", ["const:44c140:8", "const:4:8"]]
- 0044c140 ["CALL", null, ["callee:00c57d90:8"]]
+ 0046efd8 ["INT_ADD", "register:40f0:8", ["const:46efd8:8", "const:4:8"]]
+ 0046efd8 ["CALL", null, ["callee:00c57d90:8"]]
- 0044c140 bytes 803c1e94
+ 0046efd8 bytes 6ea31f94
- 0044c134 ["COPY", "register:4008:8", ["const:296000:8"]]
+ 0046efcc ["COPY", "register:4008:8", ["const:2a6000:8"]]
- 0044c134 bytes 41f2ffd0
+ 0046efcc bytes c1f1ff90
- 0044c138 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 0044c138 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c138 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c138 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0046efd0 ["COPY", "tmp:0:8", ["const:30e:8"]]
+ 0046efd0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0046efd0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0046efd0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c138 bytes 21641f91
+ 0046efd0 bytes 21380c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16c181f1f9e6ce3ba9218d42e6979353"></a>

### [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) → [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) FUN_0046f074

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 36件 [`005bcea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bcea8.md) [`005be404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) [`005c47c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c47c4.md) [`0060b7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b7bc.md) [`00614c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/00614c6c.md) · 呼出先 16件 [`0044d5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d5d0.md) [`0044d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d83c.md) [`0044d97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d97c.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)
- 新版 呼出元 36件 [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) [`006312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md) [`0063a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a764.md) · 呼出先 16件 [`00470468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470468.md) [`004706d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706d4.md) [`00470814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470814.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.60% / 新版 96.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046f0b4",
      "incomplete_value": false,
      "site": "0046f0bc",
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
    "old": {
      "definition_site": "0044c21c",
      "incomplete_value": false,
      "site": "0044c224",
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
            "const:d78:8"
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
      "definition_site": "0046f434",
      "incomplete_value": true,
      "site": "0046f440",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c59c",
      "incomplete_value": true,
      "site": "0044c5a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046f54c",
      "incomplete_value": true,
      "site": "0046f550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0044c6b4",
      "incomplete_value": true,
      "site": "0044c6b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046f0bc",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0046f0f0",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "0046f434",
      "READ",
      [
        "storage",
        "002b2ca8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0046f0bc",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0046f0f0",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "0046f434",
      "READ",
      [
        "storage",
        "002c43b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md#insn-0044c260) · [`0044c214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md#insn-0044c214) · [`0044c218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md#insn-0044c218)
- 新版 [`0046f0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md#insn-0046f0f8) · [`0046f0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md#insn-0046f0ac) · [`0046f0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md#insn-0046f0b0)

~~~diff
- 0044c260 ["INT_ADD", "register:40f0:8", ["const:44c260:8", "const:4:8"]]
- 0044c260 ["CALL", null, ["callee:00c57d90:8"]]
+ 0046f0f8 ["INT_ADD", "register:40f0:8", ["const:46f0f8:8", "const:4:8"]]
+ 0046f0f8 ["CALL", null, ["callee:00c57d90:8"]]
- 0044c260 bytes 383c1e94
+ 0046f0f8 bytes 26a31f94
- 0044c214 ["INT_ADD", "register:40f0:8", ["const:44c214:8", "const:4:8"]]
- 0044c214 ["CALL", null, ["callee:00487de0:8"]]
+ 0046f0ac ["INT_ADD", "register:40f0:8", ["const:46f0ac:8", "const:4:8"]]
+ 0046f0ac ["CALL", null, ["callee:00487de0:8"]]
- 0044c214 bytes 4d630094
+ 0046f0ac bytes 4d630094
- 0044c218 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0046f0b0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0044c218 bytes c83c00f0
+ 0046f0b0 bytes a83f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e753d0aca32f74d7bb837a084509d04e"></a>

### [`0044d47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d47c.md) → [`00470314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470314.md) FUN_00470314

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0044d28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d28c.md) [`0078b0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078b/0078b0ec.md) [`007bf8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bf8dc.md) [`008cb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cb/008cb860.md) [`009e2258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e2/009e2258.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 5件 [`00470124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470124.md) [`007bbddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbddc.md) [`007f1a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1a78.md) [`008ff730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff730.md) [`00a3f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3f/00a3f154.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00470324",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0044d48c",
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
      "definition_site": "00470320",
      "incomplete_value": false,
      "site": "00470324",
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
      "definition_site": "0044d488",
      "incomplete_value": false,
      "site": "0044d48c",
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
      "00470320",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00470324",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00470320",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00470324",
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

- 旧版 [`0044d48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d47c.md#insn-0044d48c) · [`0044d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d47c.md#insn-0044d484) · [`0044d488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d47c.md#insn-0044d488)
- 新版 [`00470324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470314.md#insn-00470324) · [`0047031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470314.md#insn-0047031c) · [`00470320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470314.md#insn-00470320)

~~~diff
- 0044d48c ["INT_ADD", "register:40f0:8", ["const:44d48c:8", "const:4:8"]]
- 0044d48c ["CALL", null, ["ram:418c38:8"]]
+ 00470324 ["INT_ADD", "register:40f0:8", ["const:470324:8", "const:4:8"]]
+ 00470324 ["CALL", null, ["ram:43b738:8"]]
- 0044d48c bytes eb2dff97
+ 00470324 bytes 052dff97
- 0044d484 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0047031c ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0044d484 bytes c0f2ffd0
+ 0047031c bytes 20f2fff0
- 0044d488 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0044d488 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0044d488 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0044d488 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00470320 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00470320 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00470320 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00470320 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0044d488 bytes 00740e91
+ 00470320 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29c430753b4199ccbd5b742ea4f58c13"></a>

### [`0044d5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d5bc.md) → [`00470454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470454.md) FUN_00470454

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0044d490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d490.md) [`007bfad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bfad4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00470328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470328.md) [`007f1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1c70.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00470464",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0044d5cc",
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
      "definition_site": "00470460",
      "incomplete_value": false,
      "site": "00470464",
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
      "definition_site": "0044d5c8",
      "incomplete_value": false,
      "site": "0044d5cc",
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
      "00470460",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00470464",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00470460",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00470464",
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

- 旧版 [`0044d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d5bc.md#insn-0044d5cc) · [`0044d5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d5bc.md#insn-0044d5c4) · [`0044d5c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d5bc.md#insn-0044d5c8)
- 新版 [`00470464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470454.md#insn-00470464) · [`0047045c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470454.md#insn-0047045c) · [`00470460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470454.md#insn-00470460)

~~~diff
- 0044d5cc ["INT_ADD", "register:40f0:8", ["const:44d5cc:8", "const:4:8"]]
- 0044d5cc ["CALL", null, ["ram:418c38:8"]]
+ 00470464 ["INT_ADD", "register:40f0:8", ["const:470464:8", "const:4:8"]]
+ 00470464 ["CALL", null, ["ram:43b738:8"]]
- 0044d5cc bytes 9b2dff97
+ 00470464 bytes b52cff97
- 0044d5c4 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0047045c ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0044d5c4 bytes c0f2ffd0
+ 0047045c bytes 20f2fff0
- 0044d5c8 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0044d5c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0044d5c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0044d5c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00470460 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00470460 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00470460 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00470460 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0044d5c8 bytes 00740e91
+ 00470460 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1506e42538762843dee1876ba75ab7f0"></a>

### [`0044d5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d5d0.md) → [`00470468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470468.md) FUN_00470468

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00444710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444710.md) [`0044d828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d828.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004675a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004675a8.md) [`004706c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706c0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.55% / 新版 98.55%

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
      "site": "00470564",
      "value": [
        "leaf",
        "ram:4675a8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0044d6cc",
      "value": [
        "leaf",
        "ram:444710:8"
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
      "site": "004705ec",
      "value": [
        "leaf",
        "ram:4675a8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0044d754",
      "value": [
        "leaf",
        "ram:444710:8"
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
      "00470564",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00444710"
      ]
    ],
    [
      "004705ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00444710"
      ]
    ]
  ],
  "added": [
    [
      "00470564",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004675a8"
      ]
    ],
    [
      "004705ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004675a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d5d0.md#insn-0044d6cc) · [`0044d754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d5d0.md#insn-0044d754) · [`0044d688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d5d0.md#insn-0044d688)
- 新版 [`00470564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470468.md#insn-00470564) · [`004705ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470468.md#insn-004705ec) · [`00470520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470468.md#insn-00470520)

~~~diff
- 0044d6cc ["INT_ADD", "register:40f0:8", ["const:44d6cc:8", "const:4:8"]]
- 0044d6cc ["CALL", null, ["ram:444710:8"]]
+ 00470564 ["INT_ADD", "register:40f0:8", ["const:470564:8", "const:4:8"]]
+ 00470564 ["CALL", null, ["ram:4675a8:8"]]
- 0044d6cc bytes 11dcff97
+ 00470564 bytes 11dcff97
- 0044d754 ["INT_ADD", "register:40f0:8", ["const:44d754:8", "const:4:8"]]
- 0044d754 ["CALL", null, ["ram:444710:8"]]
+ 004705ec ["INT_ADD", "register:40f0:8", ["const:4705ec:8", "const:4:8"]]
+ 004705ec ["CALL", null, ["ram:4675a8:8"]]
- 0044d754 bytes efdbff97
+ 004705ec bytes efdbff97
- 0044d688 ["INT_ADD", "register:40f0:8", ["const:44d688:8", "const:4:8"]]
- 0044d688 ["CALL", null, ["callee:00c57a90:8"]]
+ 00470520 ["INT_ADD", "register:40f0:8", ["const:470520:8", "const:4:8"]]
+ 00470520 ["CALL", null, ["callee:00c57a90:8"]]
- 0044d688 bytes 6e361e94
+ 00470520 bytes 5c9d1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5f16042e9b932bfb2146725618e92c4"></a>

### [`0044d828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d828.md) → [`004706c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706c0.md) FUN_004706c0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0044d5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d5d0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00470468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470468.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "004706d0",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0044d838",
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
      "definition_site": "004706cc",
      "incomplete_value": false,
      "site": "004706d0",
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
      "definition_site": "0044d834",
      "incomplete_value": false,
      "site": "0044d838",
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
      "004706cc",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "004706d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "004706cc",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "004706d0",
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

- 旧版 [`0044d838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d828.md#insn-0044d838) · [`0044d830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d828.md#insn-0044d830) · [`0044d834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d828.md#insn-0044d834)
- 新版 [`004706d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706c0.md#insn-004706d0) · [`004706c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706c0.md#insn-004706c8) · [`004706cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706c0.md#insn-004706cc)

~~~diff
- 0044d838 ["INT_ADD", "register:40f0:8", ["const:44d838:8", "const:4:8"]]
- 0044d838 ["CALL", null, ["ram:418c38:8"]]
+ 004706d0 ["INT_ADD", "register:40f0:8", ["const:4706d0:8", "const:4:8"]]
+ 004706d0 ["CALL", null, ["ram:43b738:8"]]
- 0044d838 bytes 002dff97
+ 004706d0 bytes 1a2cff97
- 0044d830 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 004706c8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0044d830 bytes c0f2ffd0
+ 004706c8 bytes 20f2fff0
- 0044d834 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0044d834 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0044d834 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0044d834 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004706cc ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 004706cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004706cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004706cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0044d834 bytes 00740e91
+ 004706cc bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ccfe05c98e98b548ec71a71570973ee"></a>

### [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) → [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) FUN_00470800

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 244件 [`0044c884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c884.md) [`0044d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d83c.md) [`0044dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dabc.md) [`00458038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458038.md) [`0047b5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b5ec.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 261件 [`0046f71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f71c.md) [`004706d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706d4.md) [`00470954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) [`0047aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md) [`0049e484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e484.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00470810",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0044d978",
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
      "definition_site": "0047080c",
      "incomplete_value": false,
      "site": "00470810",
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
      "definition_site": "0044d974",
      "incomplete_value": false,
      "site": "0044d978",
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
      "0047080c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00470810",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0047080c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00470810",
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

- 旧版 [`0044d978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md#insn-0044d978) · [`0044d970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md#insn-0044d970) · [`0044d974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md#insn-0044d974)
- 新版 [`00470810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md#insn-00470810) · [`00470808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md#insn-00470808) · [`0047080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md#insn-0047080c)

~~~diff
- 0044d978 ["INT_ADD", "register:40f0:8", ["const:44d978:8", "const:4:8"]]
- 0044d978 ["CALL", null, ["ram:418c38:8"]]
+ 00470810 ["INT_ADD", "register:40f0:8", ["const:470810:8", "const:4:8"]]
+ 00470810 ["CALL", null, ["ram:43b738:8"]]
- 0044d978 bytes b02cff97
+ 00470810 bytes ca2bff97
- 0044d970 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00470808 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0044d970 bytes c0f2ffd0
+ 00470808 bytes 20f2fff0
- 0044d974 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0044d974 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0044d974 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0044d974 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047080c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0047080c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047080c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047080c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0044d974 bytes 00740e91
+ 0047080c bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5193bf491a3b753b9dd1316132a960e7"></a>

### [`0044daa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044daa8.md) → [`00470940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470940.md) FUN_00470940

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0044d97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d97c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00470814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470814.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00470950",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0044dab8",
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
      "definition_site": "0047094c",
      "incomplete_value": false,
      "site": "00470950",
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
      "definition_site": "0044dab4",
      "incomplete_value": false,
      "site": "0044dab8",
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
      "0047094c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00470950",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0047094c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00470950",
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

- 旧版 [`0044dab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044daa8.md#insn-0044dab8) · [`0044dab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044daa8.md#insn-0044dab0) · [`0044dab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044daa8.md#insn-0044dab4)
- 新版 [`00470950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470940.md#insn-00470950) · [`00470948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470940.md#insn-00470948) · [`0047094c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470940.md#insn-0047094c)

~~~diff
- 0044dab8 ["INT_ADD", "register:40f0:8", ["const:44dab8:8", "const:4:8"]]
- 0044dab8 ["CALL", null, ["ram:418c38:8"]]
+ 00470950 ["INT_ADD", "register:40f0:8", ["const:470950:8", "const:4:8"]]
+ 00470950 ["CALL", null, ["ram:43b738:8"]]
- 0044dab8 bytes 602cff97
+ 00470950 bytes 7a2bff97
- 0044dab0 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00470948 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0044dab0 bytes c0f2ffd0
+ 00470948 bytes 20f2fff0
- 0044dab4 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0044dab4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0044dab4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0044dab4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047094c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0047094c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047094c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047094c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0044dab4 bytes 00740e91
+ 0047094c bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddf9bc462cc0c21ce035d67401a653a0"></a>

### [`0044dbec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dbec.md) → [`00470a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470a84.md) _INIT_14

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00470ac0",
      "incomplete_value": true,
      "site": "00470adc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044dc28",
      "incomplete_value": true,
      "site": "0044dc44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00470ae4",
      "incomplete_value": true,
      "site": "00470b00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044dc4c",
      "incomplete_value": true,
      "site": "0044dc68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00470b04",
      "incomplete_value": true,
      "site": "00470b20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044dc6c",
      "incomplete_value": true,
      "site": "0044dc88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00470ac0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00470ae4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00470b04",
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
      "00470ac0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00470ae4",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00470b04",
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

- 旧版 [`0044dd4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dbec.md#insn-0044dd4c) · [`0044de20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dbec.md#insn-0044de20) · [`0044dc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dbec.md#insn-0044dc14)
- 新版 [`00470be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470a84.md#insn-00470be4) · [`00470cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470a84.md#insn-00470cb8) · [`00470aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470a84.md#insn-00470aac)

~~~diff
- 0044dd4c ["INT_ADD", "register:40f0:8", ["const:44dd4c:8", "const:4:8"]]
- 0044dd4c ["CALL", null, ["callee:0043b7b8:8"]]
+ 00470be4 ["INT_ADD", "register:40f0:8", ["const:470be4:8", "const:4:8"]]
+ 00470be4 ["CALL", null, ["callee:0043b7b8:8"]]
- 0044dd4c bytes db2bff97
+ 00470be4 bytes f52aff97
- 0044de20 ["INT_ADD", "register:40f0:8", ["const:44de20:8", "const:4:8"]]
- 0044de20 ["CALL", null, ["callee:00c57a30:8"]]
+ 00470cb8 ["INT_ADD", "register:40f0:8", ["const:470cb8:8", "const:4:8"]]
+ 00470cb8 ["CALL", null, ["callee:00c57a30:8"]]
- 0044de20 bytes 70341e94
+ 00470cb8 bytes 5e9b1f94
- 0044dc14 ["COPY", "register:4098:8", ["const:c24000:8"]]
+ 00470aac ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 0044dc14 bytes b33e00f0
+ 00470aac bytes b3410090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40e712acd83e3fae3e2ca16493dd9f6a"></a>

### [`0044e05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e05c.md) → [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) FUN_00470ef4

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00844bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844bd8.md) [`00ab1dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1dc8.md) · 呼出先 32件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0044ee44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ee44.md) [`0044f0dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f0dc.md) [`0044f1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f1e0.md)
- 新版 呼出元 3件 [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) [`00b11858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b11858.md) · 呼出先 32件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00471cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471cdc.md) [`00471f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471f74.md) [`00472078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472078.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004712fc",
      "incomplete_value": true,
      "site": "00471300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0044e464",
      "incomplete_value": true,
      "site": "0044e468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004712f8",
      "incomplete_value": true,
      "site": "00471304",
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
      "definition_site": "0044e460",
      "incomplete_value": true,
      "site": "0044e46c",
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
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00471310",
      "incomplete_value": true,
      "site": "00471310",
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
                "const:48:8"
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
      "definition_site": "0044e478",
      "incomplete_value": true,
      "site": "0044e478",
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
                "const:48:8"
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
    "ordinal": 34,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047123c",
      "PARAM",
      [
        "storage",
        "002b6fa5",
        null,
        null
      ]
    ],
    [
      "004712a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0045fc34"
      ]
    ],
    [
      "004712ec",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047123c",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "004712a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00482acc"
      ]
    ],
    [
      "004712ec",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e05c.md#insn-0044e3a8) · [`0044e410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e05c.md#insn-0044e410) · [`0044e548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e05c.md#insn-0044e548)
- 新版 [`00471240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md#insn-00471240) · [`004712a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md#insn-004712a8) · [`004713e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md#insn-004713e0)

~~~diff
- 0044e3a8 ["INT_ADD", "register:40f0:8", ["const:44e3a8:8", "const:4:8"]]
- 0044e3a8 ["CALL", null, ["callee:00471cdc:8"]]
+ 00471240 ["INT_ADD", "register:40f0:8", ["const:471240:8", "const:4:8"]]
+ 00471240 ["CALL", null, ["callee:00471cdc:8"]]
- 0044e3a8 bytes a7020094
+ 00471240 bytes a7020094
- 0044e410 ["INT_ADD", "register:40f0:8", ["const:44e410:8", "const:4:8"]]
- 0044e410 ["CALL", null, ["ram:45fc34:8"]]
+ 004712a8 ["INT_ADD", "register:40f0:8", ["const:4712a8:8", "const:4:8"]]
+ 004712a8 ["CALL", null, ["ram:482acc:8"]]
- 0044e410 bytes 09460094
+ 004712a8 bytes 09460094
- 0044e548 ["INT_ADD", "register:40f0:8", ["const:44e548:8", "const:4:8"]]
- 0044e548 ["CALL", null, ["callee:00472078:8"]]
+ 004713e0 ["INT_ADD", "register:40f0:8", ["const:4713e0:8", "const:4:8"]]
+ 004713e0 ["CALL", null, ["callee:00472078:8"]]
- 0044e548 bytes 26030094
+ 004713e0 bytes 26030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adb3192acee283a1ccf5f269ffb651d0"></a>

### [`0044ea58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ea58.md) → [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) FUN_004718f0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`004618e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/004618e8.md) [`004658b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004658b8.md) [`004667c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004667c4.md) [`00ab1234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1234.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0044f0dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f0dc.md) [`0044f1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f1e0.md) [`0044f48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f48c.md)
- 新版 呼出元 4件 [`00484780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md) [`00488750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md) [`0048965c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/0048965c.md) [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md) · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00471f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471f74.md) [`00472078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472078.md) [`00472324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472324.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.32% / 新版 99.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00471a3c",
      "incomplete_value": false,
      "site": "00471a50",
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
    "old": {
      "definition_site": "0044eba4",
      "incomplete_value": false,
      "site": "0044ebb8",
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
            "const:fa5:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00471a3c",
      "PARAM",
      [
        "storage",
        "002b6fa5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00471a3c",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ebb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ea58.md#insn-0044ebb8) · [`0044ea90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ea58.md#insn-0044ea90) · [`0044ea9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ea58.md#insn-0044ea9c)
- 新版 [`00471a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md#insn-00471a50) · [`00471928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md#insn-00471928) · [`00471934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md#insn-00471934)

~~~diff
- 0044ebb8 ["INT_ADD", "register:40f0:8", ["const:44ebb8:8", "const:4:8"]]
- 0044ebb8 ["CALL", null, ["callee:00472078:8"]]
+ 00471a50 ["INT_ADD", "register:40f0:8", ["const:471a50:8", "const:4:8"]]
+ 00471a50 ["CALL", null, ["callee:00472078:8"]]
- 0044ebb8 bytes 8a010094
+ 00471a50 bytes 8a010094
- 0044ea90 ["INT_ADD", "register:40f0:8", ["const:44ea90:8", "const:4:8"]]
- 0044ea90 ["CALL", null, ["callee:00c57ce0:8"]]
+ 00471928 ["INT_ADD", "register:40f0:8", ["const:471928:8", "const:4:8"]]
+ 00471928 ["CALL", null, ["callee:00c57ce0:8"]]
- 0044ea90 bytes 00321e94
+ 00471928 bytes ee981f94
- 0044ea9c ["INT_ADD", "register:40f0:8", ["const:44ea9c:8", "const:4:8"]]
- 0044ea9c ["CALL", null, ["callee:00472324:8"]]
+ 00471934 ["INT_ADD", "register:40f0:8", ["const:471934:8", "const:4:8"]]
+ 00471934 ["CALL", null, ["callee:00472324:8"]]
- 0044ea9c bytes 7c020094
+ 00471934 bytes 7c020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daf891702eaae5e0c98aafb57f8a839b"></a>

### [`0044f798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f798.md) → [`00472630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472630.md) _INIT_15

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047266c",
      "incomplete_value": true,
      "site": "00472688",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044f7d4",
      "incomplete_value": true,
      "site": "0044f7f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00472690",
      "incomplete_value": true,
      "site": "004726ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044f7f8",
      "incomplete_value": true,
      "site": "0044f814",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004726b0",
      "incomplete_value": true,
      "site": "004726cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044f818",
      "incomplete_value": true,
      "site": "0044f834",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0047266c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00472690",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "004726b0",
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
      "0047266c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00472690",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "004726b0",
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

- 旧版 [`0044f8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f798.md#insn-0044f8f8) · [`0044f9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f798.md#insn-0044f9cc) · [`0044f7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044f798.md#insn-0044f7c0)
- 新版 [`00472790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472630.md#insn-00472790) · [`00472864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472630.md#insn-00472864) · [`00472658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472630.md#insn-00472658)

~~~diff
- 0044f8f8 ["INT_ADD", "register:40f0:8", ["const:44f8f8:8", "const:4:8"]]
- 0044f8f8 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00472790 ["INT_ADD", "register:40f0:8", ["const:472790:8", "const:4:8"]]
+ 00472790 ["CALL", null, ["callee:0043b7b8:8"]]
- 0044f8f8 bytes f024ff97
+ 00472790 bytes 0a24ff97
- 0044f9cc ["INT_ADD", "register:40f0:8", ["const:44f9cc:8", "const:4:8"]]
- 0044f9cc ["CALL", null, ["callee:00c57a30:8"]]
+ 00472864 ["INT_ADD", "register:40f0:8", ["const:472864:8", "const:4:8"]]
+ 00472864 ["CALL", null, ["callee:00c57a30:8"]]
- 0044f9cc bytes 852d1e94
+ 00472864 bytes 73941f94
- 0044f7c0 ["COPY", "register:4098:8", ["const:c24000:8"]]
+ 00472658 ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 0044f7c0 bytes b33e00b0
+ 00472658 bytes 934100d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe02679269a98969c7fc268ad43ccdd8"></a>

### [`0044fecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fecc.md) → [`00472d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d64.md) FUN_00472d64

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 9件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) [`00821350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821350.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00859148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859148.md) · 呼出先 5件 [`0044ff5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044ff5c.md) [`00450150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450150.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 9件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) [`008532c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/008532c8.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`0088c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md) · 呼出先 5件 [`00472df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md) [`00472fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00472d98",
      "incomplete_value": false,
      "site": "00472d9c",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ff00",
      "incomplete_value": false,
      "site": "0044ff04",
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
            "const:f28:8"
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
      "definition_site": "00472da8",
      "incomplete_value": false,
      "site": "00472dac",
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
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ff10",
      "incomplete_value": false,
      "site": "0044ff14",
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
            "const:ee0:8"
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
      "definition_site": "00472db4",
      "incomplete_value": false,
      "site": "00472dc8",
      "value": [
        "leaf",
        "const:472fe8:8"
      ]
    },
    "old": {
      "definition_site": "0044ff1c",
      "incomplete_value": false,
      "site": "0044ff30",
      "value": [
        "leaf",
        "const:450150:8"
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
      "00472d78",
      "READ",
      [
        "storage",
        "00c24f28",
        null,
        "undefined1"
      ]
    ],
    [
      "00472d84",
      "DATA",
      [
        "storage",
        "00c24ee0",
        null,
        null
      ]
    ],
    [
      "00472d98",
      "PARAM",
      [
        "storage",
        "00c24f28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00472d78",
      "READ",
      [
        "storage",
        "00ca49e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00472d84",
      "DATA",
      [
        "storage",
        "00ca49a0",
        null,
        null
      ]
    ],
    [
      "00472d98",
      "PARAM",
      [
        "storage",
        "00ca49e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ff04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fecc.md#insn-0044ff04) · [`0044ff14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fecc.md#insn-0044ff14) · [`0044ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fecc.md#insn-0044ff30)
- 新版 [`00472d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d64.md#insn-00472d9c) · [`00472dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d64.md#insn-00472dac) · [`00472dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d64.md#insn-00472dc8)

~~~diff
- 0044ff04 ["INT_ADD", "register:40f0:8", ["const:44ff04:8", "const:4:8"]]
- 0044ff04 ["CALL", null, ["callee:00c57a50:8"]]
+ 00472d9c ["INT_ADD", "register:40f0:8", ["const:472d9c:8", "const:4:8"]]
+ 00472d9c ["CALL", null, ["callee:00c57a50:8"]]
- 0044ff04 bytes 3f2c1e94
+ 00472d9c bytes 2d931f94
- 0044ff14 ["INT_ADD", "register:40f0:8", ["const:44ff14:8", "const:4:8"]]
- 0044ff14 ["CALL", null, ["callee:00472df4:8"]]
+ 00472dac ["INT_ADD", "register:40f0:8", ["const:472dac:8", "const:4:8"]]
+ 00472dac ["CALL", null, ["callee:00472df4:8"]]
- 0044ff14 bytes 12000094
+ 00472dac bytes 12000094
- 0044ff30 ["INT_ADD", "register:40f0:8", ["const:44ff30:8", "const:4:8"]]
- 0044ff30 ["CALL", null, ["callee:00c57a30:8"]]
+ 00472dc8 ["INT_ADD", "register:40f0:8", ["const:472dc8:8", "const:4:8"]]
+ 00472dc8 ["CALL", null, ["callee:00c57a30:8"]]
- 0044ff30 bytes 2c2c1e94
+ 00472dc8 bytes 1a931f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cbc420d71a4a958f2622a960eb743d1"></a>

### [`0044ff5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044ff5c.md) → [`00472df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md) FUN_00472df4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0044fecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fecc.md) [`004537f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md) [`00454af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454af4.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`00472d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d64.md) [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00472e38",
      "incomplete_value": false,
      "site": "00472e3c",
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
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ffa0",
      "incomplete_value": false,
      "site": "0044ffa4",
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
            "const:df0:8"
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
      "definition_site": "00472e80",
      "incomplete_value": false,
      "site": "00472e84",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ffe8",
      "incomplete_value": false,
      "site": "0044ffec",
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
            "const:e40:8"
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
      "00472e3c",
      "DATA",
      [
        "storage",
        "00be7df0",
        null,
        "undefined *"
      ]
    ],
    [
      "00472e84",
      "DATA",
      [
        "storage",
        "00be7e40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00472e3c",
      "DATA",
      [
        "storage",
        "00c649b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00472e84",
      "DATA",
      [
        "storage",
        "00c64a00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ff94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044ff5c.md#insn-0044ff94) · [`0044ff9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044ff5c.md#insn-0044ff9c) · [`0044ffa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044ff5c.md#insn-0044ffa0)
- 新版 [`00472e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md#insn-00472e2c) · [`00472e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md#insn-00472e34) · [`00472e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md#insn-00472e38)

~~~diff
- 0044ff94 ["INT_ADD", "register:40f0:8", ["const:44ff94:8", "const:4:8"]]
- 0044ff94 ["CALL", null, ["callee:00c57a90:8"]]
+ 00472e2c ["INT_ADD", "register:40f0:8", ["const:472e2c:8", "const:4:8"]]
+ 00472e2c ["CALL", null, ["callee:00c57a90:8"]]
- 0044ff94 bytes 2b2c1e94
+ 00472e2c bytes 19931f94
- 0044ff9c ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00472e34 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0044ff9c bytes c83c0090
+ 00472e34 bytes 883f00d0
- 0044ffa0 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 0044ffa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044ffa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044ffa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00472e38 ["COPY", "tmp:0:8", ["const:9b0:8"]]
+ 00472e38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00472e38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00472e38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044ffa0 bytes 08c13791
+ 00472e38 bytes 08c12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2baa1f2e2c96f25c88e62eb9ddb6ae5d"></a>

### [`00450150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450150.md) → [`00472fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md) FUN_00472fe8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0044fecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044fecc.md) [`004537f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md) [`00454af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454af4.md) · 呼出先 9件 [`00451ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/00451ff0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 3件 [`00472d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d64.md) [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) · 呼出先 9件 [`00474e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047300c",
      "incomplete_value": false,
      "site": "00473010",
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
            "const:fa5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00450174",
      "incomplete_value": false,
      "site": "00450178",
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
            "const:436:8"
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
      "0047300c",
      "PARAM",
      [
        "storage",
        "002a7436",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047300c",
      "PARAM",
      [
        "storage",
        "002b7fa5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00450178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450150.md#insn-00450178) · [`00450170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450150.md#insn-00450170) · [`00450174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450150.md#insn-00450174)
- 新版 [`00473010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md#insn-00473010) · [`00473008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md#insn-00473008) · [`0047300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md#insn-0047300c)

~~~diff
- 00450178 ["INT_ADD", "register:40f0:8", ["const:450178:8", "const:4:8"]]
- 00450178 ["CALL", null, ["callee:00c58070:8"]]
+ 00473010 ["INT_ADD", "register:40f0:8", ["const:473010:8", "const:4:8"]]
+ 00473010 ["CALL", null, ["callee:00c58070:8"]]
- 00450178 bytes 2a2d1e94
+ 00473010 bytes 18941f94
- 00450170 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00473008 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00450170 bytes a0f2fff0
+ 00473008 bytes 20f2ff90
- 00450174 ["COPY", "tmp:0:8", ["const:436:8"]]
- 00450174 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00450174 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00450174 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047300c ["COPY", "tmp:0:8", ["const:fa5:8"]]
+ 0047300c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047300c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047300c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00450174 bytes 00d81091
+ 0047300c bytes 00943e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b204813c4e0ec9fe837bb90e5df5647"></a>

### [`004502bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004502bc.md) → [`00473154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473154.md) FUN_00473154

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) · 呼出先 4件 [`004529a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004529a0.md) [`004529a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/004529a4.md) [`0052dad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 4件 [`00475838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475838.md) [`0047583c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/0047583c.md) [`0055096c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055096c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
      "definition_site": "00473180",
      "incomplete_value": false,
      "site": "00473180",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004502e8",
      "incomplete_value": false,
      "site": "004502e8",
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
            "const:e90:8"
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
      "00473180",
      "DATA",
      [
        "storage",
        "00be7e90",
        null,
        "undefined *"
      ]
    ],
    [
      "004731b4",
      "READ",
      [
        "storage",
        "00be7eb0",
        null,
        "pointer"
      ]
    ],
    [
      "004731b4",
      "READ",
      [
        "storage",
        "00be7eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00473180",
      "DATA",
      [
        "storage",
        "00c64a50",
        null,
        "undefined *"
      ]
    ],
    [
      "004731b4",
      "READ",
      [
        "storage",
        "00c64a70",
        null,
        "pointer"
      ]
    ],
    [
      "004731b4",
      "READ",
      [
        "storage",
        "00c64a78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004502dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004502bc.md#insn-004502dc) · [`004502e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004502bc.md#insn-004502e0) · [`004502f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004502bc.md#insn-004502f4)
- 新版 [`00473174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473154.md#insn-00473174) · [`00473178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473154.md#insn-00473178) · [`0047318c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473154.md#insn-0047318c)

~~~diff
- 004502dc ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00473174 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004502dc bytes a83c00f0
+ 00473174 bytes 883f00b0
- 004502e0 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 004502e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004502e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004502e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00473178 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00473178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00473178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00473178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004502e0 bytes 08413a91
+ 00473178 bytes 08412991
- 004502f4 ["INT_ADD", "register:40f0:8", ["const:4502f4:8", "const:4:8"]]
- 004502f4 ["CALL", null, ["callee:0055096c:8"]]
+ 0047318c ["INT_ADD", "register:40f0:8", ["const:47318c:8", "const:4:8"]]
+ 0047318c ["CALL", null, ["callee:0055096c:8"]]
- 004502f4 bytes f8750394
+ 0047318c bytes f8750394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-942065780a766d9bc00b9b42d3ab7b8f"></a>

### [`00450398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450398.md) → [`00473230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473230.md) FUN_00473230

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`00821350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821350.md) [`008eeba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ee/008eeba0.md) [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) · 呼出先 10件 [`00452ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452ec8.md) [`0073e07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e07c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 4件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`008532c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/008532c8.md) [`00922c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00922/00922c2c.md) [`00a8a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8a/00a8a220.md) · 呼出先 10件 [`00475d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md) [`00768388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768388.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00473258",
      "value": [
        "leaf",
        "ram:768388:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004503c0",
      "value": [
        "leaf",
        "ram:73e07c:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00473294",
      "incomplete_value": false,
      "site": "004732a0",
      "value": [
        "leaf",
        "const:475d60:8"
      ]
    },
    "old": {
      "definition_site": "004503fc",
      "incomplete_value": false,
      "site": "00450408",
      "value": [
        "leaf",
        "const:452ec8:8"
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004732fc",
      "incomplete_value": false,
      "site": "00473300",
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
            "const:e5a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00450464",
      "incomplete_value": false,
      "site": "00450468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:544:8"
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
      "00473258",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073e07c"
      ]
    ],
    [
      "00473294",
      "PARAM",
      [
        "storage",
        "00452ec8",
        null,
        null
      ]
    ],
    [
      "004732fc",
      "PARAM",
      [
        "storage",
        "00294544",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00473258",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768388"
      ]
    ],
    [
      "00473294",
      "PARAM",
      [
        "storage",
        "00475d60",
        null,
        null
      ]
    ],
    [
      "004732fc",
      "PARAM",
      [
        "storage",
        "002a3e5a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004503c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450398.md#insn-004503c0) · [`00450408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450398.md#insn-00450408) · [`00450468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450398.md#insn-00450468)
- 新版 [`00473258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473230.md#insn-00473258) · [`004732a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473230.md#insn-004732a0) · [`00473300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473230.md#insn-00473300)

~~~diff
- 004503c0 ["INT_ADD", "register:40f0:8", ["const:4503c0:8", "const:4:8"]]
- 004503c0 ["CALL", null, ["ram:73e07c:8"]]
+ 00473258 ["INT_ADD", "register:40f0:8", ["const:473258:8", "const:4:8"]]
+ 00473258 ["CALL", null, ["ram:768388:8"]]
- 004503c0 bytes 2fb70b94
+ 00473258 bytes 4cd40b94
- 00450408 ["INT_ADD", "register:40f0:8", ["const:450408:8", "const:4:8"]]
- 00450408 ["CALL", null, ["callee:00c57d10:8"]]
+ 004732a0 ["INT_ADD", "register:40f0:8", ["const:4732a0:8", "const:4:8"]]
+ 004732a0 ["CALL", null, ["callee:00c57d10:8"]]
- 00450408 bytes ae2b1e94
+ 004732a0 bytes 9c921f94
- 00450468 ["INT_ADD", "register:40f0:8", ["const:450468:8", "const:4:8"]]
- 00450468 ["CALL", null, ["callee:00c57d20:8"]]
+ 00473300 ["INT_ADD", "register:40f0:8", ["const:473300:8", "const:4:8"]]
+ 00473300 ["CALL", null, ["callee:00c57d20:8"]]
- 00450468 bytes 9a2b1e94
+ 00473300 bytes 88921f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86901299a59646e81291b259cf74e95c"></a>

### [`004504bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004504bc.md) → [`00473354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473354.md) FUN_00473354

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0086a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086a/0086a350.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`00456884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456884.md) [`00456888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456888.md) [`0052dac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dac8.md)
- 新版 呼出元 1件 [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`0047971c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047971c.md) [`00479720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479720.md) [`00550960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550960.md)

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
      "definition_site": "004733cc",
      "incomplete_value": false,
      "site": "004733cc",
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
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00450534",
      "incomplete_value": false,
      "site": "00450534",
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
            "const:fa0:8"
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
      "004733cc",
      "DATA",
      [
        "storage",
        "00be7fa0",
        null,
        "undefined *"
      ]
    ],
    [
      "00473408",
      "READ",
      [
        "storage",
        "00be7fc0",
        null,
        "pointer"
      ]
    ],
    [
      "00473408",
      "READ",
      [
        "storage",
        "00be7fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004733cc",
      "DATA",
      [
        "storage",
        "00c64b60",
        null,
        "undefined *"
      ]
    ],
    [
      "00473408",
      "READ",
      [
        "storage",
        "00c64b80",
        null,
        "pointer"
      ]
    ],
    [
      "00473408",
      "READ",
      [
        "storage",
        "00c64b88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00450518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004504bc.md#insn-00450518) · [`00450528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004504bc.md#insn-00450528) · [`0045052c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004504bc.md#insn-0045052c)
- 新版 [`004733b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473354.md#insn-004733b0) · [`004733c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473354.md#insn-004733c0) · [`004733c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473354.md#insn-004733c4)

~~~diff
- 00450518 ["INT_ADD", "register:40f0:8", ["const:450518:8", "const:4:8"]]
- 00450518 ["CALL", null, ["callee:0043bae0:8"]]
+ 004733b0 ["INT_ADD", "register:40f0:8", ["const:4733b0:8", "const:4:8"]]
+ 004733b0 ["CALL", null, ["callee:0043bae0:8"]]
- 00450518 bytes b222ff97
+ 004733b0 bytes cc21ff97
- 00450528 ["INT_ADD", "register:40f0:8", ["const:450528:8", "const:4:8"]]
- 00450528 ["CALL", null, ["callee:00473500:8"]]
+ 004733c0 ["INT_ADD", "register:40f0:8", ["const:4733c0:8", "const:4:8"]]
+ 004733c0 ["CALL", null, ["callee:00473500:8"]]
- 00450528 bytes 50000094
+ 004733c0 bytes 50000094
- 0045052c ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004733c4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045052c bytes a83c00f0
+ 004733c4 bytes 883f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06f106d767046a6eef2b176da7618004"></a>

### [`004507b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004507b8.md) → [`00473650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473650.md) FUN_00473650

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 4件 [`0045693c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/0045693c.md) [`00456940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456940.md) [`0052dac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dac8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 4件 [`004797d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004797d4.md) [`004797d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004797d8.md) [`00550960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550960.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
      "definition_site": "0047368c",
      "incomplete_value": false,
      "site": "0047368c",
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
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004507f4",
      "incomplete_value": false,
      "site": "004507f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:30:8"
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
      "0047368c",
      "DATA",
      [
        "storage",
        "00be8030",
        null,
        "undefined *"
      ]
    ],
    [
      "004736c4",
      "READ",
      [
        "storage",
        "00be8050",
        null,
        "pointer"
      ]
    ],
    [
      "004736c4",
      "READ",
      [
        "storage",
        "00be8058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047368c",
      "DATA",
      [
        "storage",
        "00c64bf0",
        null,
        "undefined *"
      ]
    ],
    [
      "004736c4",
      "READ",
      [
        "storage",
        "00c64c10",
        null,
        "pointer"
      ]
    ],
    [
      "004736c4",
      "READ",
      [
        "storage",
        "00c64c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004507ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004507b8.md#insn-004507ec) · [`004507f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004507b8.md#insn-004507f0) · [`00450804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004507b8.md#insn-00450804)
- 新版 [`00473684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473650.md#insn-00473684) · [`00473688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473650.md#insn-00473688) · [`0047369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473650.md#insn-0047369c)

~~~diff
- 004507ec ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 00473684 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 004507ec bytes c93c0090
+ 00473684 bytes 893f00b0
- 004507f0 ["COPY", "tmp:0:8", ["const:30:8"]]
- 004507f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004507f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004507f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00473688 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 00473688 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00473688 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00473688 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004507f0 bytes 29c10091
+ 00473688 bytes 29c12f91
- 00450804 ["INT_ADD", "register:40f0:8", ["const:450804:8", "const:4:8"]]
- 00450804 ["CALL", null, ["callee:00550960:8"]]
+ 0047369c ["INT_ADD", "register:40f0:8", ["const:47369c:8", "const:4:8"]]
+ 0047369c ["CALL", null, ["callee:00550960:8"]]
- 00450804 bytes b1740394
+ 0047369c bytes b1740394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5247d8feb2b2feb20cf5e0d6dd3049f"></a>

### [`004508a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md) → [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) FUN_0047373c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00859148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859148.md) [`00860de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860de0.md) [`0086a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086a/0086a350.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00428a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428a44.md) [`004512c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004512c0.md) [`00456c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456c10.md) [`00457074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457074.md)
- 新版 呼出元 3件 [`0088c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md) [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · 呼出先 20件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b544.md) [`00474158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md) [`00479aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479aa8.md) [`00479f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479f0c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004737f8",
      "incomplete_value": true,
      "site": "00473808",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00450960",
      "incomplete_value": true,
      "site": "00450970",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3e0:8"
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
      "definition_site": "004737fc",
      "incomplete_value": true,
      "site": "0047380c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00450964",
      "incomplete_value": true,
      "site": "00450974",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00473800",
      "incomplete_value": true,
      "site": "00473810",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00450968",
      "incomplete_value": true,
      "site": "00450978",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:400:8"
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
      "004737f8",
      "READ",
      [
        "storage",
        "0029f3e0",
        null,
        "string"
      ]
    ],
    [
      "004737fc",
      "READ",
      [
        "storage",
        "0029f3ea",
        null,
        "string"
      ]
    ],
    [
      "00473800",
      "READ",
      [
        "storage",
        "002b1400",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004737f8",
      "READ",
      [
        "storage",
        "002af7f3",
        null,
        "string"
      ]
    ],
    [
      "004737fc",
      "READ",
      [
        "storage",
        "002af7fd",
        null,
        "string"
      ]
    ],
    [
      "00473800",
      "READ",
      [
        "storage",
        "002c2a50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00450994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md#insn-00450994) · [`00450b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md#insn-00450b60) · [`00450b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md#insn-00450b94)
- 新版 [`0047382c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md#insn-0047382c) · [`004739f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md#insn-004739f8) · [`00473a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md#insn-00473a2c)

~~~diff
- 00450994 ["INT_ADD", "register:40f0:8", ["const:450994:8", "const:4:8"]]
- 00450994 ["CALL", null, ["callee:00474158:8"]]
+ 0047382c ["INT_ADD", "register:40f0:8", ["const:47382c:8", "const:4:8"]]
+ 0047382c ["CALL", null, ["callee:00474158:8"]]
- 00450994 bytes 4b020094
+ 0047382c bytes 4b020094
- 00450b60 ["INT_ADD", "register:40f0:8", ["const:450b60:8", "const:4:8"]]
- 00450b60 ["CALL", null, ["callee:00c57b70:8"]]
+ 004739f8 ["INT_ADD", "register:40f0:8", ["const:4739f8:8", "const:4:8"]]
+ 004739f8 ["CALL", null, ["callee:00c57b70:8"]]
- 00450b60 bytes 70291e94
+ 004739f8 bytes 5e901f94
- 00450b94 ["INT_ADD", "register:40f0:8", ["const:450b94:8", "const:4:8"]]
- 00450b94 ["CALL", null, ["callee:00561cf4:8"]]
+ 00473a2c ["INT_ADD", "register:40f0:8", ["const:473a2c:8", "const:4:8"]]
+ 00473a2c ["CALL", null, ["callee:00561cf4:8"]]
- 00450b94 bytes b2b80394
+ 00473a2c bytes b2b80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00f472d7b394b19a9fcf70f70b37e851"></a>

### [`004512c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004512c0.md) → [`00474158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md) FUN_00474158

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 17件 [`004508a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md) [`004512c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004512c0.md) [`004532cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md) [`00469128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469128.md) [`005fe524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fe524.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 17件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) [`00474158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md) [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) [`0048bfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bfc0.md) [`00623f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00623/00623f28.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004742a8",
      "incomplete_value": false,
      "site": "004742b0",
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
    "old": {
      "definition_site": "00451410",
      "incomplete_value": false,
      "site": "00451418",
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
            "const:3a4:8"
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
      "definition_site": "00474364",
      "incomplete_value": false,
      "site": "0047436c",
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
    "old": {
      "definition_site": "004514cc",
      "incomplete_value": false,
      "site": "004514d4",
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
            "const:379:8"
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
      "definition_site": "0047437c",
      "incomplete_value": false,
      "site": "00474388",
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
    "old": {
      "definition_site": "004514e4",
      "incomplete_value": false,
      "site": "004514f0",
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
            "const:885:8"
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
      "004742a8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00474364",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "0047437c",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004742a8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00474364",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0047437c",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00451418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004512c0.md#insn-00451418) · [`004514d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004512c0.md#insn-004514d4) · [`004514f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004512c0.md#insn-004514f0)
- 新版 [`004742b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md#insn-004742b0) · [`0047436c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md#insn-0047436c) · [`00474388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md#insn-00474388)

~~~diff
- 00451418 ["INT_ADD", "register:40f0:8", ["const:451418:8", "const:4:8"]]
- 00451418 ["CALL", null, ["callee:00441e54:8"]]
+ 004742b0 ["INT_ADD", "register:40f0:8", ["const:4742b0:8", "const:4:8"]]
+ 004742b0 ["CALL", null, ["callee:00441e54:8"]]
- 00451418 bytes cf37ff97
+ 004742b0 bytes e936ff97
- 004514d4 ["INT_ADD", "register:40f0:8", ["const:4514d4:8", "const:4:8"]]
- 004514d4 ["CALL", null, ["callee:00441e54:8"]]
+ 0047436c ["INT_ADD", "register:40f0:8", ["const:47436c:8", "const:4:8"]]
+ 0047436c ["CALL", null, ["callee:00441e54:8"]]
- 004514d4 bytes a037ff97
+ 0047436c bytes ba36ff97
- 004514f0 ["INT_ADD", "register:40f0:8", ["const:4514f0:8", "const:4:8"]]
- 004514f0 ["CALL", null, ["callee:004427b4:8"]]
+ 00474388 ["INT_ADD", "register:40f0:8", ["const:474388:8", "const:4:8"]]
+ 00474388 ["CALL", null, ["callee:004427b4:8"]]
- 004514f0 bytes f139ff97
+ 00474388 bytes 0b39ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab180a34e3426308161e199ba0ffaf49"></a>

### [`00452958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452958.md) → [`004757f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004757f0.md) FUN_004757f0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00475814",
      "incomplete_value": false,
      "site": "00475814",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045297c",
      "incomplete_value": false,
      "site": "0045297c",
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
            "const:e90:8"
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
      "00475814",
      "DATA",
      [
        "storage",
        "00be7e90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00475814",
      "DATA",
      [
        "storage",
        "00c64a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045296c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452958.md#insn-0045296c) · [`00452974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452958.md#insn-00452974) · [`00452978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452958.md#insn-00452978)
- 新版 [`00475804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004757f0.md#insn-00475804) · [`0047580c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004757f0.md#insn-0047580c) · [`00475810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004757f0.md#insn-00475810)

~~~diff
- 0045296c ["INT_ADD", "register:40f0:8", ["const:45296c:8", "const:4:8"]]
- 0045296c ["CALL", null, ["callee:00c57a90:8"]]
+ 00475804 ["INT_ADD", "register:40f0:8", ["const:475804:8", "const:4:8"]]
+ 00475804 ["CALL", null, ["callee:00c57a90:8"]]
- 0045296c bytes b5211e94
+ 00475804 bytes a3881f94
- 00452974 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 0047580c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00452974 bytes a83c00b0
+ 0047580c bytes 683f00f0
- 00452978 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00452978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00452978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00452978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00475810 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00475810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00475810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00475810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00452978 bytes 08413a91
+ 00475810 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82b24e338bd5febf2cf7337f3da59534"></a>

### [`0045298c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/0045298c.md) → [`00475824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475824.md) FUN_00475824

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00475830",
      "incomplete_value": false,
      "site": "00475830",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00452998",
      "incomplete_value": false,
      "site": "00452998",
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
            "const:e90:8"
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
      "00475830",
      "DATA",
      [
        "storage",
        "00be7e90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00475830",
      "DATA",
      [
        "storage",
        "00c64a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00452990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/0045298c.md#insn-00452990) · [`00452994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/0045298c.md#insn-00452994)
- 新版 [`00475828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475824.md#insn-00475828) · [`0047582c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475824.md#insn-0047582c)

~~~diff
- 00452990 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 00475828 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00452990 bytes a93c00b0
+ 00475828 bytes 693f00f0
- 00452994 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00452994 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00452994 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00452994 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047582c ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0047582c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047582c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047582c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00452994 bytes 29413a91
+ 0047582c bytes 29412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e412fac3e268d78ab64c9363e3f67020"></a>

### [`00452ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452ec8.md) → [`00475d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md) FUN_00475d60

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00450398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450398.md) · 呼出先 16件 [`004532cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md) [`004536b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004536b0.md) [`00455dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455dec.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00473230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473230.md) · 呼出先 16件 [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) [`00476548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476548.md) [`00478c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c84.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.06% / 新版 98.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00475db4",
      "incomplete_value": false,
      "site": "00475db8",
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
            "const:fc5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00452f1c",
      "incomplete_value": false,
      "site": "00452f20",
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
            "const:456:8"
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
      "definition_site": "00475ff8",
      "incomplete_value": false,
      "site": "00475ffc",
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
            "const:3b9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453160",
      "incomplete_value": false,
      "site": "00453164",
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
            "const:496:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00476048",
      "value": [
        "leaf",
        "ram:c57d50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004531b0",
      "value": [
        "leaf",
        "ram:bdb300:8"
      ]
    },
    "ordinal": 31,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00475db4",
      "PARAM",
      [
        "storage",
        "002a7456",
        null,
        "string"
      ]
    ],
    [
      "00475dc8",
      "READ",
      [
        "storage",
        "002b2cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00475ff8",
      "PARAM",
      [
        "storage",
        "002ab496",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00475db4",
      "PARAM",
      [
        "storage",
        "002b7fc5",
        null,
        "string"
      ]
    ],
    [
      "00475dc8",
      "READ",
      [
        "storage",
        "002c43c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00475ff8",
      "PARAM",
      [
        "storage",
        "002bc3b9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00452f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452ec8.md#insn-00452f20) · [`00453164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452ec8.md#insn-00453164) · [`004531b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452ec8.md#insn-004531b0)
- 新版 [`00475db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md#insn-00475db8) · [`00475ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md#insn-00475ffc) · [`00476048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md#insn-00476048)

~~~diff
- 00452f20 ["INT_ADD", "register:40f0:8", ["const:452f20:8", "const:4:8"]]
- 00452f20 ["CALL", null, ["callee:00c58070:8"]]
+ 00475db8 ["INT_ADD", "register:40f0:8", ["const:475db8:8", "const:4:8"]]
+ 00475db8 ["CALL", null, ["callee:00c58070:8"]]
- 00452f20 bytes c0211e94
+ 00475db8 bytes ae881f94
- 00453164 ["INT_ADD", "register:40f0:8", ["const:453164:8", "const:4:8"]]
- 00453164 ["CALL", null, ["callee:00c58070:8"]]
+ 00475ffc ["INT_ADD", "register:40f0:8", ["const:475ffc:8", "const:4:8"]]
+ 00475ffc ["CALL", null, ["callee:00c58070:8"]]
- 00453164 bytes 2f211e94
+ 00475ffc bytes 1d881f94
- 004531b0 ["INT_ADD", "register:40f0:8", ["const:4531b0:8", "const:4:8"]]
- 004531b0 ["CALL", null, ["ram:bdb300:8"]]
+ 00476048 ["INT_ADD", "register:40f0:8", ["const:476048:8", "const:4:8"]]
+ 00476048 ["CALL", null, ["ram:c57d50:8"]]
- 004531b0 bytes 54201e94
+ 00476048 bytes 42871f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-600579d9f4039b2f416b4beb68868e50"></a>

### [`004532cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md) → [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) FUN_00476164

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00452ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00452/00452ec8.md) · 呼出先 11件 [`004512c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004512c0.md) [`004537f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md) [`00453c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md) [`00454af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454af4.md) [`00454f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454f34.md)
- 新版 呼出元 1件 [`00475d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md) · 呼出先 11件 [`00474158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md) [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) [`00477dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/00477dcc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004761c4",
      "incomplete_value": true,
      "site": "004761e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0045332c",
      "incomplete_value": true,
      "site": "00453348",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:400:8"
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
      "004761c4",
      "READ",
      [
        "storage",
        "002b1400",
        null,
        null
      ]
    ],
    [
      "004762a8",
      "READ",
      [
        "storage",
        "0029f3e0",
        null,
        "string"
      ]
    ],
    [
      "004762b8",
      "READ",
      [
        "storage",
        "0029f3ea",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004761c4",
      "READ",
      [
        "storage",
        "002c2a50",
        null,
        null
      ]
    ],
    [
      "004762a8",
      "READ",
      [
        "storage",
        "002af7f3",
        null,
        "string"
      ]
    ],
    [
      "004762b8",
      "READ",
      [
        "storage",
        "002af7fd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045331c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md#insn-0045331c) · [`00453320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md#insn-00453320) · [`0045332c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md#insn-0045332c)
- 新版 [`004761b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md#insn-004761b4) · [`004761b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md#insn-004761b8) · [`004761c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md#insn-004761c4)

~~~diff
- 0045331c ["COPY", "register:0:8", ["register:4048:8"]]
- 0045331c ["INT_ADD", "register:40f0:8", ["const:45331c:8", "const:4:8"]]
- 0045331c ["CALLIND", null, ["register:0:8"]]
+ 004761b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004761b4 ["INT_ADD", "register:40f0:8", ["const:4761b4:8", "const:4:8"]]
+ 004761b4 ["CALLIND", null, ["register:0:8"]]
- 0045331c bytes 20013fd6
+ 004761b4 bytes 20013fd6
- 00453320 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004761b8 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 00453320 bytes e9f2ffd0
+ 004761b8 bytes 69f2ff90
- 0045332c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:400:8"]]
- 0045332c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 0045332c ["COPY", "register:5010:8", ["const:0:8"]]
- 0045332c ["COPY", "register:5018:8", ["const:0:8"]]
+ 004761c4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a50:8"]]
+ 004761c4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 004761c4 ["COPY", "register:5010:8", ["const:0:8"]]
+ 004761c4 ["COPY", "register:5018:8", ["const:0:8"]]
- 0045332c bytes 2001c13d
+ 004761c4 bytes 2095c23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0e91ea8106d5176e0a7559facd17bf9"></a>

### [`004537f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md) → [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) FUN_00476688

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004532cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md) · 呼出先 23件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`00430b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430b04.md) [`0044ff5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044ff5c.md) [`00450150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450150.md) [`00455270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455270.md)
- 新版 呼出元 1件 [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) · 呼出先 23件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`0045399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md) [`00472df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md) [`00472fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md) [`00478108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.95% / 新版 92.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004766fc",
      "value": [
        "leaf",
        "ram:764344:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00453864",
      "value": [
        "leaf",
        "ram:73a038:8"
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
      "site": "00453868"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00476708",
      "value": [
        "leaf",
        "ram:764ea0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00453870",
      "value": [
        "leaf",
        "ram:73ab94:8"
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
      "004766fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073a038"
      ]
    ],
    [
      "unmatched:00453868",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "00476708",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073ab94"
      ]
    ]
  ],
  "added": [
    [
      "004766fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ],
    [
      "00476700",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "00476708",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00453864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md#insn-00453864) · [`00453868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md#insn-00453868) · [`00453870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md#insn-00453870)
- 新版 [`004766fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md#insn-004766fc) · [`00476708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md#insn-00476708)

~~~diff
- 00453864 ["INT_ADD", "register:40f0:8", ["const:453864:8", "const:4:8"]]
- 00453864 ["CALL", null, ["ram:73a038:8"]]
+ 004766fc ["INT_ADD", "register:40f0:8", ["const:4766fc:8", "const:4:8"]]
+ 004766fc ["CALL", null, ["ram:764344:8"]]
- 00453864 bytes f5990b94
+ 004766fc bytes 12b70b94
- 00453868 ["INT_ADD", "register:40f0:8", ["const:453868:8", "const:4:8"]]
- 00453868 ["CALL", null, ["callee:008514b8:8"]]
- 00453868 bytes 462f0f94
- 00453870 ["INT_ADD", "register:40f0:8", ["const:453870:8", "const:4:8"]]
- 00453870 ["CALL", null, ["ram:73ab94:8"]]
+ 00476708 ["INT_ADD", "register:40f0:8", ["const:476708:8", "const:4:8"]]
+ 00476708 ["CALL", null, ["ram:764ea0:8"]]
- 00453870 bytes c99c0b94
+ 00476708 bytes e6b90b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0663d292634ffcb7b9e973fc506f6614"></a>

### [`00453c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md) → [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) FUN_00476b10

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004532cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md) · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`00428b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428b68.md) [`0045543c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/0045543c.md)
- 新版 呼出元 1件 [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) · 呼出先 22件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0044b668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b668.md) [`004782d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/004782d4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.63% / 新版 97.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047733c",
      "incomplete_value": true,
      "site": "0047733c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004544a4",
      "incomplete_value": true,
      "site": "004544a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 64,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00476b9c",
      "incomplete_value": true,
      "site": "00476ba0",
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
                "register:4000:8"
              ],
              "INT_LEFT"
            ]
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453d04",
      "incomplete_value": true,
      "site": "00453d08",
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
                "register:4000:8"
              ],
              "INT_LEFT"
            ]
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "definition_site": "00476bdc",
      "incomplete_value": false,
      "site": "00476be8",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453d44",
      "incomplete_value": false,
      "site": "00453d50",
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
            "const:429:8"
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
      "00476bdc",
      "PARAM",
      [
        "storage",
        "002a7429",
        null,
        "string"
      ]
    ],
    [
      "00476ca8",
      "PARAM",
      [
        "storage",
        "002a9377",
        null,
        "string"
      ]
    ],
    [
      "00476e00",
      "PARAM",
      [
        "storage",
        "0029d3b0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00476bdc",
      "PARAM",
      [
        "storage",
        "002b7f98",
        null,
        "string"
      ]
    ],
    [
      "00476ca8",
      "PARAM",
      [
        "storage",
        "002ba01a",
        null,
        "string"
      ]
    ],
    [
      "00476e00",
      "PARAM",
      [
        "storage",
        "002ad63a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00453d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md#insn-00453d08) · [`00453d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md#insn-00453d50) · [`00453e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md#insn-00453e1c)
- 新版 [`00476ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md#insn-00476ba0) · [`00476be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md#insn-00476be8) · [`00476cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md#insn-00476cb4)

~~~diff
- 00453d08 ["INT_ADD", "register:40f0:8", ["const:453d08:8", "const:4:8"]]
- 00453d08 ["CALL", null, ["callee:00b3c4b4:8"]]
+ 00476ba0 ["INT_ADD", "register:40f0:8", ["const:476ba0:8", "const:4:8"]]
+ 00476ba0 ["CALL", null, ["callee:00b3c4b4:8"]]
- 00453d08 bytes 75231a94
+ 00476ba0 bytes 45161b94
- 00453d50 ["INT_ADD", "register:40f0:8", ["const:453d50:8", "const:4:8"]]
- 00453d50 ["CALL", null, ["callee:00c57b60:8"]]
+ 00476be8 ["INT_ADD", "register:40f0:8", ["const:476be8:8", "const:4:8"]]
+ 00476be8 ["CALL", null, ["callee:00c57b60:8"]]
- 00453d50 bytes f01c1e94
+ 00476be8 bytes de831f94
- 00453e1c ["INT_ADD", "register:40f0:8", ["const:453e1c:8", "const:4:8"]]
- 00453e1c ["CALL", null, ["callee:00c57b60:8"]]
+ 00476cb4 ["INT_ADD", "register:40f0:8", ["const:476cb4:8", "const:4:8"]]
+ 00476cb4 ["CALL", null, ["callee:00c57b60:8"]]
- 00453e1c bytes bd1c1e94
+ 00476cb4 bytes ab831f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fdd1b10bbc0f489efbed60bf2a00568"></a>

### [`00454af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454af4.md) → [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) FUN_0047798c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004532cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md) · 呼出先 20件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`00430b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430b04.md) [`0044ff5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044f/0044ff5c.md) [`00450150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450150.md) [`00455270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455270.md)
- 新版 呼出元 1件 [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) · 呼出先 20件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`0045399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md) [`00472df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md) [`00472fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md) [`00478108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 92.38% / 新版 92.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件, `store_value` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00477a8c",
      "incomplete_value": true,
      "site": "00477a98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:150:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454bf4",
      "incomplete_value": true,
      "site": "00454c00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004779e8",
      "value": [
        "leaf",
        "ram:764344:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00454b50",
      "value": [
        "leaf",
        "ram:73a038:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00454b54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004779e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073a038"
      ]
    ],
    [
      "unmatched:00454b54",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "004779f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073ab94"
      ]
    ]
  ],
  "added": [
    [
      "004779e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ],
    [
      "004779ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "004779f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00454b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454af4.md#insn-00454b50) · [`00454b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454af4.md#insn-00454b54) · [`00454b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454af4.md#insn-00454b5c)
- 新版 [`004779e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md#insn-004779e8) · [`004779f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md#insn-004779f4)

~~~diff
- 00454b50 ["INT_ADD", "register:40f0:8", ["const:454b50:8", "const:4:8"]]
- 00454b50 ["CALL", null, ["ram:73a038:8"]]
+ 004779e8 ["INT_ADD", "register:40f0:8", ["const:4779e8:8", "const:4:8"]]
+ 004779e8 ["CALL", null, ["ram:764344:8"]]
- 00454b50 bytes 3a950b94
+ 004779e8 bytes 57b20b94
- 00454b54 ["INT_ADD", "register:40f0:8", ["const:454b54:8", "const:4:8"]]
- 00454b54 ["CALL", null, ["callee:008514b8:8"]]
- 00454b54 bytes 8b2a0f94
- 00454b5c ["INT_ADD", "register:40f0:8", ["const:454b5c:8", "const:4:8"]]
- 00454b5c ["CALL", null, ["ram:73ab94:8"]]
+ 004779f4 ["INT_ADD", "register:40f0:8", ["const:4779f4:8", "const:4:8"]]
+ 004779f4 ["CALL", null, ["ram:764ea0:8"]]
- 00454b5c bytes 0e980b94
+ 004779f4 bytes 2bb50b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

