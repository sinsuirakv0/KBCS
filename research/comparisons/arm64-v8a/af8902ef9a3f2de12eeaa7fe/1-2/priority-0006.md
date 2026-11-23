# v15.7.4 → v16.0.0 · 最優先の変更候補 (6)

[一覧の目次](README.md)

<a id="compare-244e6df62400375a240fed91b0c1bc59"></a>

### [`00470404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470404.md) → [`0049329c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/0049329c.md) FUN_0049329c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`0083d5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083d5f0.md) [`00850180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850180.md) [`008e0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e0/008e0bc0.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004703fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/004703fc.md) [`00471ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471ca4.md) [`0052db38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db38.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 4件 [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`0086f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f8dc.md) [`00883118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883118.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · 呼出先 12件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00493294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493294.md) [`00494b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b3c.md) [`005509d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 89.45% / 新版 89.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_condition` 1件, `store_destination` 5件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004932f4",
      "incomplete_value": false,
      "site": "004932f4",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047045c",
      "incomplete_value": false,
      "site": "0047045c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049335c",
      "incomplete_value": false,
      "site": "0049335c",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004704c4",
      "incomplete_value": false,
      "site": "004704c4",
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
            "const:e28:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004934ac",
      "incomplete_value": true,
      "site": "004934ac",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00470614",
      "incomplete_value": true,
      "site": "00470614",
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
            "const:2f0:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004932dc",
      "READ",
      [
        "storage",
        "00c25308",
        null,
        "undefined1"
      ]
    ],
    [
      "004932ec",
      "READ",
      [
        "storage",
        "00c252e8",
        null,
        "undefined4"
      ]
    ],
    [
      "004932f4",
      "WRITE",
      [
        "storage",
        "00c252e8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "004932dc",
      "READ",
      [
        "storage",
        "00ca4dc8",
        null,
        "undefined1"
      ]
    ],
    [
      "004932ec",
      "READ",
      [
        "storage",
        "00ca4da8",
        null,
        "undefined4"
      ]
    ],
    [
      "004932f4",
      "WRITE",
      [
        "storage",
        "00ca4da8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047045c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470404.md#insn-0047045c) · [`00470614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470404.md#insn-00470614) · [`004706d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470404.md#insn-004706d0)
- 新版 [`004932f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/0049329c.md#insn-004932f4) · [`004934ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/0049329c.md#insn-004934ac) · [`00493568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/0049329c.md#insn-00493568)

~~~diff
- 0047045c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e8:8"]]
- 0047045c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:4"]]
+ 004932f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da8:8"]]
+ 004932f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:4"]]
- 0047045c bytes 18e902b9
+ 004932f4 bytes 18a90db9
- 00470614 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
- 00470614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 004934ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db0:8"]]
+ 004934ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00470614 bytes 097901f9
+ 004934ac bytes 09d906f9
- 004706d0 ["INT_ADD", "register:40f0:8", ["const:4706d0:8", "const:4:8"]]
- 004706d0 ["CALL", null, ["callee:00c57a50:8"]]
+ 00493568 ["INT_ADD", "register:40f0:8", ["const:493568:8", "const:4:8"]]
+ 00493568 ["CALL", null, ["callee:00c57a50:8"]]
- 004706d0 bytes 4caa1d94
+ 00493568 bytes 3a111f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-111fab0a0d98f43057a62fb334c64a8c"></a>

### [`004711b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004711b4.md) → [`0049404c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049404c.md) FUN_0049404c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0049406c",
      "incomplete_value": false,
      "site": "00494070",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004711d4",
      "incomplete_value": false,
      "site": "004711d8",
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
            "const:b98:8"
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
      "00494070",
      "DATA",
      [
        "storage",
        "00be8b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494070",
      "DATA",
      [
        "storage",
        "00c65758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004711c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004711b4.md#insn-004711c8) · [`004711d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004711b4.md#insn-004711d0) · [`004711d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004711b4.md#insn-004711d4)
- 新版 [`00494060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049404c.md#insn-00494060) · [`00494068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049404c.md#insn-00494068) · [`0049406c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049404c.md#insn-0049406c)

~~~diff
- 004711c8 ["INT_ADD", "register:40f0:8", ["const:4711c8:8", "const:4:8"]]
- 004711c8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00494060 ["INT_ADD", "register:40f0:8", ["const:494060:8", "const:4:8"]]
+ 00494060 ["CALL", null, ["callee:00c57a90:8"]]
- 004711c8 bytes 9ea71d94
+ 00494060 bytes 8c0e1f94
- 004711d0 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00494068 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 004711d0 bytes a83b00f0
+ 00494068 bytes 883e00b0
- 004711d4 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 004711d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004711d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004711d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049406c ["COPY", "tmp:0:8", ["const:758:8"]]
+ 0049406c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049406c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049406c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004711d4 bytes 08612e91
+ 0049406c bytes 08611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b06eb32be00cc28769350c67438df2ea"></a>

### [`004711ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004711ec.md) → [`00494084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494084.md) FUN_00494084

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00494088",
      "incomplete_value": false,
      "site": "0049408c",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004711f0",
      "incomplete_value": false,
      "site": "004711f4",
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
            "const:b98:8"
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
      "0049408c",
      "DATA",
      [
        "storage",
        "00be8b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049408c",
      "DATA",
      [
        "storage",
        "00c65758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004711ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004711ec.md#insn-004711ec) · [`004711f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004711ec.md#insn-004711f0)
- 新版 [`00494084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494084.md#insn-00494084) · [`00494088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494084.md#insn-00494088)

~~~diff
- 004711ec ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00494084 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 004711ec bytes a83b00f0
+ 00494084 bytes 883e00b0
- 004711f0 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 004711f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004711f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004711f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494088 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00494088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004711f0 bytes 08612e91
+ 00494088 bytes 08611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c876b48992eab4507a531165b1e4734"></a>

### [`00471254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471254.md) → [`004940ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004940ec.md) FUN_004940ec

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0049410c",
      "incomplete_value": false,
      "site": "00494110",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471274",
      "incomplete_value": false,
      "site": "00471278",
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
            "const:c18:8"
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
      "00494110",
      "DATA",
      [
        "storage",
        "00be8c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494110",
      "DATA",
      [
        "storage",
        "00c657d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471254.md#insn-00471268) · [`00471270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471254.md#insn-00471270) · [`00471274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471254.md#insn-00471274)
- 新版 [`00494100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004940ec.md#insn-00494100) · [`00494108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004940ec.md#insn-00494108) · [`0049410c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004940ec.md#insn-0049410c)

~~~diff
- 00471268 ["INT_ADD", "register:40f0:8", ["const:471268:8", "const:4:8"]]
- 00471268 ["CALL", null, ["callee:00c57a90:8"]]
+ 00494100 ["INT_ADD", "register:40f0:8", ["const:494100:8", "const:4:8"]]
+ 00494100 ["CALL", null, ["callee:00c57a90:8"]]
- 00471268 bytes 76a71d94
+ 00494100 bytes 640e1f94
- 00471270 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00494108 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00471270 bytes a83b00f0
+ 00494108 bytes 883e00b0
- 00471274 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 00471274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049410c ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0049410c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049410c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049410c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471274 bytes 08613091
+ 0049410c bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9849369d575febaec49be94412d8c570"></a>

### [`0047128c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047128c.md) → [`00494124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494124.md) FUN_00494124

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00494128",
      "incomplete_value": false,
      "site": "0049412c",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471290",
      "incomplete_value": false,
      "site": "00471294",
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
            "const:c18:8"
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
      "0049412c",
      "DATA",
      [
        "storage",
        "00be8c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049412c",
      "DATA",
      [
        "storage",
        "00c657d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047128c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047128c.md#insn-0047128c) · [`00471290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047128c.md#insn-00471290)
- 新版 [`00494124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494124.md#insn-00494124) · [`00494128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494124.md#insn-00494128)

~~~diff
- 0047128c ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00494124 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0047128c bytes a83b00f0
+ 00494124 bytes 883e00b0
- 00471290 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 00471290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494128 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00494128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471290 bytes 08613091
+ 00494128 bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-503ab26bbdc9377a3979c3d081f8c6c1"></a>

### [`004712f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004712f4.md) → [`0049418c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049418c.md) FUN_0049418c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "004941ac",
      "incomplete_value": false,
      "site": "004941b0",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471314",
      "incomplete_value": false,
      "site": "00471318",
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
            "const:c98:8"
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
      "004941b0",
      "DATA",
      [
        "storage",
        "00be8c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004941b0",
      "DATA",
      [
        "storage",
        "00c65858",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004712f4.md#insn-00471308) · [`00471310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004712f4.md#insn-00471310) · [`00471314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004712f4.md#insn-00471314)
- 新版 [`004941a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049418c.md#insn-004941a0) · [`004941a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049418c.md#insn-004941a8) · [`004941ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049418c.md#insn-004941ac)

~~~diff
- 00471308 ["INT_ADD", "register:40f0:8", ["const:471308:8", "const:4:8"]]
- 00471308 ["CALL", null, ["callee:00c57a90:8"]]
+ 004941a0 ["INT_ADD", "register:40f0:8", ["const:4941a0:8", "const:4:8"]]
+ 004941a0 ["CALL", null, ["callee:00c57a90:8"]]
- 00471308 bytes 4ea71d94
+ 004941a0 bytes 3c0e1f94
- 00471310 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 004941a8 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00471310 bytes a83b00f0
+ 004941a8 bytes 883e00b0
- 00471314 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 00471314 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471314 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471314 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004941ac ["COPY", "tmp:0:8", ["const:858:8"]]
+ 004941ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004941ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004941ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471314 bytes 08613291
+ 004941ac bytes 08612191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c27fa955d701f06194e3c37513d068c9"></a>

### [`0047132c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047132c.md) → [`004941c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004941c4.md) FUN_004941c4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004941c8",
      "incomplete_value": false,
      "site": "004941cc",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471330",
      "incomplete_value": false,
      "site": "00471334",
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
            "const:c98:8"
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
      "004941cc",
      "DATA",
      [
        "storage",
        "00be8c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004941cc",
      "DATA",
      [
        "storage",
        "00c65858",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047132c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047132c.md#insn-0047132c) · [`00471330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047132c.md#insn-00471330)
- 新版 [`004941c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004941c4.md#insn-004941c4) · [`004941c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004941c4.md#insn-004941c8)

~~~diff
- 0047132c ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 004941c4 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0047132c bytes a83b00f0
+ 004941c4 bytes 883e00b0
- 00471330 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 00471330 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471330 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471330 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004941c8 ["COPY", "tmp:0:8", ["const:858:8"]]
+ 004941c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004941c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004941c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471330 bytes 08613291
+ 004941c8 bytes 08612191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4cfc456e74a21a1bb32be9ec9b2a75a"></a>

### [`00471394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471394.md) → [`0049422c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049422c.md) FUN_0049422c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0049424c",
      "incomplete_value": false,
      "site": "00494250",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004713b4",
      "incomplete_value": false,
      "site": "004713b8",
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
            "const:d18:8"
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
      "00494250",
      "DATA",
      [
        "storage",
        "00be8d18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494250",
      "DATA",
      [
        "storage",
        "00c658d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004713a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471394.md#insn-004713a8) · [`004713b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471394.md#insn-004713b0) · [`004713b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471394.md#insn-004713b4)
- 新版 [`00494240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049422c.md#insn-00494240) · [`00494248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049422c.md#insn-00494248) · [`0049424c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049422c.md#insn-0049424c)

~~~diff
- 004713a8 ["INT_ADD", "register:40f0:8", ["const:4713a8:8", "const:4:8"]]
- 004713a8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00494240 ["INT_ADD", "register:40f0:8", ["const:494240:8", "const:4:8"]]
+ 00494240 ["CALL", null, ["callee:00c57a90:8"]]
- 004713a8 bytes 26a71d94
+ 00494240 bytes 140e1f94
- 004713b0 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00494248 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 004713b0 bytes a83b00f0
+ 00494248 bytes 883e00b0
- 004713b4 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 004713b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004713b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004713b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049424c ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 0049424c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049424c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049424c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004713b4 bytes 08613491
+ 0049424c bytes 08612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c553d2731cec351f1d49b1bb9f7fbf1"></a>

### [`004713cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004713cc.md) → [`00494264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494264.md) FUN_00494264

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00494268",
      "incomplete_value": false,
      "site": "0049426c",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004713d0",
      "incomplete_value": false,
      "site": "004713d4",
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
            "const:d18:8"
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
      "0049426c",
      "DATA",
      [
        "storage",
        "00be8d18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049426c",
      "DATA",
      [
        "storage",
        "00c658d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004713cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004713cc.md#insn-004713cc) · [`004713d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004713cc.md#insn-004713d0)
- 新版 [`00494264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494264.md#insn-00494264) · [`00494268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494264.md#insn-00494268)

~~~diff
- 004713cc ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00494264 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 004713cc bytes a83b00f0
+ 00494264 bytes 883e00b0
- 004713d0 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 004713d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004713d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004713d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494268 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 00494268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004713d0 bytes 08613491
+ 00494268 bytes 08612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30c35044c99b6818d04fd9d712e88f4e"></a>

### [`0047155c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047155c.md) → [`004943f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004943f4.md) FUN_004943f4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00494414",
      "incomplete_value": false,
      "site": "00494418",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047157c",
      "incomplete_value": false,
      "site": "00471580",
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
            "const:d98:8"
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
      "00494418",
      "DATA",
      [
        "storage",
        "00be8d98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494418",
      "DATA",
      [
        "storage",
        "00c65958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047155c.md#insn-00471570) · [`00471578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047155c.md#insn-00471578) · [`0047157c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047155c.md#insn-0047157c)
- 新版 [`00494408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004943f4.md#insn-00494408) · [`00494410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004943f4.md#insn-00494410) · [`00494414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004943f4.md#insn-00494414)

~~~diff
- 00471570 ["INT_ADD", "register:40f0:8", ["const:471570:8", "const:4:8"]]
- 00471570 ["CALL", null, ["callee:00c57a90:8"]]
+ 00494408 ["INT_ADD", "register:40f0:8", ["const:494408:8", "const:4:8"]]
+ 00494408 ["CALL", null, ["callee:00c57a90:8"]]
- 00471570 bytes b4a61d94
+ 00494408 bytes a20d1f94
- 00471578 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00494410 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00471578 bytes a83b00f0
+ 00494410 bytes 883e00b0
- 0047157c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 0047157c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047157c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047157c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494414 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00494414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047157c bytes 08613691
+ 00494414 bytes 08612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8708e40c4e47558c62de74f57ff3dc20"></a>

### [`00471594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471594.md) → [`0049442c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049442c.md) FUN_0049442c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00494430",
      "incomplete_value": false,
      "site": "00494434",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471598",
      "incomplete_value": false,
      "site": "0047159c",
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
            "const:d98:8"
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
      "00494434",
      "DATA",
      [
        "storage",
        "00be8d98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494434",
      "DATA",
      [
        "storage",
        "00c65958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471594.md#insn-00471594) · [`00471598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471594.md#insn-00471598)
- 新版 [`0049442c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049442c.md#insn-0049442c) · [`00494430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049442c.md#insn-00494430)

~~~diff
- 00471594 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 0049442c ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00471594 bytes a83b00f0
+ 0049442c bytes 883e00b0
- 00471598 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00471598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494430 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00494430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471598 bytes 08613691
+ 00494430 bytes 08612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-add679635fb4925b7d92c32696a6110d"></a>

### [`00471ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471ac4.md) → [`0049495c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049495c.md) FUN_0049495c

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
      "definition_site": "00494968",
      "incomplete_value": false,
      "site": "00494974",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471ad0",
      "incomplete_value": false,
      "site": "00471adc",
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
            "const:e28:8"
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
      "00494974",
      "DATA",
      [
        "storage",
        "00be8e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494974",
      "DATA",
      [
        "storage",
        "00c659e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471ac4.md#insn-00471acc) · [`00471ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471ac4.md#insn-00471ad0)
- 新版 [`00494964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049495c.md#insn-00494964) · [`00494968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049495c.md#insn-00494968)

~~~diff
- 00471acc ["COPY", "register:4050:8", ["const:be8000:8"]]
+ 00494964 ["COPY", "register:4050:8", ["const:c65000:8"]]
- 00471acc bytes aa3b00f0
+ 00494964 bytes 8a3e00b0
- 00471ad0 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00471ad0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00471ad0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00471ad0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00494968 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00494968 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00494968 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00494968 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00471ad0 bytes 4aa13891
+ 00494968 bytes 4aa12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bab2f3d352ad502ea0665d9fd66e46c7"></a>

### [`00471b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471b08.md) → [`004949a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949a0.md) FUN_004949a0

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
      "definition_site": "004949b8",
      "incomplete_value": false,
      "site": "004949c4",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471b20",
      "incomplete_value": false,
      "site": "00471b2c",
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
            "const:e28:8"
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
      "004949c4",
      "DATA",
      [
        "storage",
        "00be8e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004949c4",
      "DATA",
      [
        "storage",
        "00c659e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471b08.md#insn-00471b1c) · [`00471b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471b08.md#insn-00471b20) · [`00471b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471b08.md#insn-00471b50)
- 新版 [`004949b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949a0.md#insn-004949b4) · [`004949b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949a0.md#insn-004949b8) · [`004949e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949a0.md#insn-004949e8)

~~~diff
- 00471b1c ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 004949b4 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00471b1c bytes a83b00f0
+ 004949b4 bytes 883e00b0
- 00471b20 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00471b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004949b8 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 004949b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004949b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004949b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471b20 bytes 08a13891
+ 004949b8 bytes 08a12791
- 00471b50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00471b50 ["INT_ADD", "register:40f0:8", ["const:471b50:8", "const:4:8"]]
- 00471b50 ["CALLIND", null, ["register:0:8"]]
+ 004949e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004949e8 ["INT_ADD", "register:40f0:8", ["const:4949e8:8", "const:4:8"]]
+ 004949e8 ["CALLIND", null, ["register:0:8"]]
- 00471b50 bytes 00013fd6
+ 004949e8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9458896398c9f8cfa64795e6bd54472a"></a>

### [`00471b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471b64.md) → [`004949fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949fc.md) FUN_004949fc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00494a28",
      "incomplete_value": false,
      "site": "00494a28",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471b90",
      "incomplete_value": false,
      "site": "00471b90",
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
            "const:e28:8"
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
      "00494a28",
      "DATA",
      [
        "storage",
        "00be8e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494a28",
      "DATA",
      [
        "storage",
        "00c659e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471b64.md#insn-00471b78) · [`00471b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471b64.md#insn-00471b84) · [`00471b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471b64.md#insn-00471b88)
- 新版 [`00494a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949fc.md#insn-00494a10) · [`00494a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949fc.md#insn-00494a1c) · [`00494a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949fc.md#insn-00494a20)

~~~diff
- 00471b78 ["INT_ADD", "register:40f0:8", ["const:471b78:8", "const:4:8"]]
- 00471b78 ["CALL", null, ["callee:00c57a90:8"]]
+ 00494a10 ["INT_ADD", "register:40f0:8", ["const:494a10:8", "const:4:8"]]
+ 00494a10 ["CALL", null, ["callee:00c57a90:8"]]
- 00471b78 bytes 32a51d94
+ 00494a10 bytes 200c1f94
- 00471b84 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00494a1c ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00471b84 bytes a83b00f0
+ 00494a1c bytes 883e00b0
- 00471b88 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00471b88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471b88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471b88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494a20 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00494a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471b88 bytes 08a13891
+ 00494a20 bytes 08a12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c094bfb1749ded6827d3f678b5090a74"></a>

### [`00471bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471bf4.md) → [`00494a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494a8c.md) FUN_00494a8c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00494aac",
      "incomplete_value": false,
      "site": "00494aac",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471c14",
      "incomplete_value": false,
      "site": "00471c14",
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
            "const:e28:8"
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
      "00494aac",
      "DATA",
      [
        "storage",
        "00be8e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494aac",
      "DATA",
      [
        "storage",
        "00c659e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471bf4.md#insn-00471c0c) · [`00471c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471bf4.md#insn-00471c10) · [`00471c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471bf4.md#insn-00471c30)
- 新版 [`00494aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494a8c.md#insn-00494aa4) · [`00494aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494a8c.md#insn-00494aa8) · [`00494ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494a8c.md#insn-00494ac8)

~~~diff
- 00471c0c ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00494aa4 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00471c0c bytes a83b00f0
+ 00494aa4 bytes 883e00b0
- 00471c10 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00471c10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471c10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471c10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494aa8 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00494aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471c10 bytes 08a13891
+ 00494aa8 bytes 08a12791
- 00471c30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00471c30 ["INT_ADD", "register:40f0:8", ["const:471c30:8", "const:4:8"]]
- 00471c30 ["CALLIND", null, ["register:0:8"]]
+ 00494ac8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494ac8 ["INT_ADD", "register:40f0:8", ["const:494ac8:8", "const:4:8"]]
+ 00494ac8 ["CALLIND", null, ["register:0:8"]]
- 00471c30 bytes 00013fd6
+ 00494ac8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceed83056eea2b625c54ea886999be5d"></a>

### [`00471cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471cf4.md) → [`00494b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b8c.md) FUN_00494b8c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0047163c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/0047163c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`004944d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004944d4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00494bd0",
      "incomplete_value": false,
      "site": "00494bd8",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471d38",
      "incomplete_value": false,
      "site": "00471d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "00494bd0",
      "PARAM",
      [
        "storage",
        "00c252f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00494bd0",
      "PARAM",
      [
        "storage",
        "00ca4db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471cf4.md#insn-00471d40) · [`00471d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471cf4.md#insn-00471d30) · [`00471d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471cf4.md#insn-00471d34)
- 新版 [`00494bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b8c.md#insn-00494bd8) · [`00494bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b8c.md#insn-00494bc8) · [`00494bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b8c.md#insn-00494bcc)

~~~diff
- 00471d40 ["INT_ADD", "register:40f0:8", ["const:471d40:8", "const:4:8"]]
- 00471d40 ["CALL", null, ["callee:004944d4:8"]]
+ 00494bd8 ["INT_ADD", "register:40f0:8", ["const:494bd8:8", "const:4:8"]]
+ 00494bd8 ["CALL", null, ["callee:004944d4:8"]]
- 00471d40 bytes 3ffeff97
+ 00494bd8 bytes 3ffeff97
- 00471d30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00471d30 ["INT_ADD", "register:40f0:8", ["const:471d30:8", "const:4:8"]]
- 00471d30 ["CALLIND", null, ["register:0:8"]]
+ 00494bc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494bc8 ["INT_ADD", "register:40f0:8", ["const:494bc8:8", "const:4:8"]]
+ 00494bc8 ["CALLIND", null, ["register:0:8"]]
- 00471d30 bytes 00013fd6
+ 00494bc8 bytes 00013fd6
- 00471d34 ["COPY", "register:4000:8", ["const:c25000:8"]]
+ 00494bcc ["COPY", "register:4000:8", ["const:ca4000:8"]]
- 00471d34 bytes a03d0090
+ 00494bcc bytes 80400090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7581ed4bb5c2a4e034a1c64d57012d30"></a>

### [`00471f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471f30.md) → [`00494dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494dc8.md) _INIT_22

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`0046ad90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046ad90.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`0048dc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dc28.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 15件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00494e08",
      "incomplete_value": true,
      "site": "00494e24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00471f70",
      "incomplete_value": true,
      "site": "00471f8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00494e2c",
      "incomplete_value": true,
      "site": "00494e48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00471f94",
      "incomplete_value": true,
      "site": "00471fb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00494e4c",
      "incomplete_value": true,
      "site": "00494e68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00471fb4",
      "incomplete_value": true,
      "site": "00471fd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00494e08",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00494e2c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00494e4c",
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
      "00494e08",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00494e2c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00494e4c",
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

- 旧版 [`00472094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471f30.md#insn-00472094) · [`0047216c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471f30.md#insn-0047216c) · [`004721a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471f30.md#insn-004721a4)
- 新版 [`00494f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494dc8.md#insn-00494f2c) · [`00495004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494dc8.md#insn-00495004) · [`0049503c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494dc8.md#insn-0049503c)

~~~diff
- 00472094 ["INT_ADD", "register:40f0:8", ["const:472094:8", "const:4:8"]]
- 00472094 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00494f2c ["INT_ADD", "register:40f0:8", ["const:494f2c:8", "const:4:8"]]
+ 00494f2c ["CALL", null, ["callee:0043b7b8:8"]]
- 00472094 bytes 099bfe97
+ 00494f2c bytes 239afe97
- 0047216c ["INT_ADD", "register:40f0:8", ["const:47216c:8", "const:4:8"]]
- 0047216c ["CALL", null, ["callee:00c57a30:8"]]
+ 00495004 ["INT_ADD", "register:40f0:8", ["const:495004:8", "const:4:8"]]
+ 00495004 ["CALL", null, ["callee:00c57a30:8"]]
- 0047216c bytes 9da31d94
+ 00495004 bytes 8b0a1f94
- 004721a4 ["INT_ADD", "register:40f0:8", ["const:4721a4:8", "const:4:8"]]
- 004721a4 ["CALL", null, ["callee:00c57a30:8"]]
+ 0049503c ["INT_ADD", "register:40f0:8", ["const:49503c:8", "const:4:8"]]
+ 0049503c ["CALL", null, ["callee:00c57a30:8"]]
- 004721a4 bytes 8fa31d94
+ 0049503c bytes 7d0a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b69298d29c695f03c17396c48f58a963"></a>

### [`004723a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004723a8.md) → [`00495240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495240.md) FUN_00495240

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) [`00acba3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acba3c.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) [`00b2b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4cc.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049526c",
      "incomplete_value": true,
      "site": "00495278",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004723d4",
      "incomplete_value": true,
      "site": "004723e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:890:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00495248",
      "incomplete_value": true,
      "site": "00495248",
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
      "definition_site": "004723b0",
      "incomplete_value": true,
      "site": "004723b0",
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
    "guard": [
      [
        "FALL_THROUGH",
        "004723b0"
      ],
      [
        "FALL_THROUGH",
        "00495248"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00495248",
      "incomplete_value": true,
      "site": "00495250",
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
      "definition_site": "004723b0",
      "incomplete_value": true,
      "site": "004723b8",
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
      "00495244",
      "READ",
      [
        "storage",
        "00c25350",
        null,
        "undefined8"
      ]
    ],
    [
      "0049526c",
      "READ",
      [
        "storage",
        "002b1890",
        null,
        null
      ]
    ],
    [
      "0049527c",
      "READ",
      [
        "storage",
        "00c25348",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00495244",
      "READ",
      [
        "storage",
        "00ca4e10",
        null,
        "undefined8"
      ]
    ],
    [
      "0049526c",
      "READ",
      [
        "storage",
        "002c2f20",
        null,
        null
      ]
    ],
    [
      "0049527c",
      "READ",
      [
        "storage",
        "00ca4e08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004723a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004723a8.md#insn-004723a8) · [`004723ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004723a8.md#insn-004723ac) · [`004723c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004723a8.md#insn-004723c8)
- 新版 [`00495240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495240.md#insn-00495240) · [`00495244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495240.md#insn-00495244) · [`00495260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495240.md#insn-00495260)

~~~diff
- 004723a8 ["COPY", "register:4040:8", ["const:c25000:8"]]
+ 00495240 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 004723a8 bytes 883d00f0
+ 00495240 bytes 684000f0
- 004723ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
- 004723ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00495244 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 00495244 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004723ac bytes 08a941f9
+ 00495244 bytes 080947f9
- 004723c8 ["COPY", "register:4040:8", ["const:2b1000:8"]]
+ 00495260 ["COPY", "register:4040:8", ["const:2c2000:8"]]
- 004723c8 bytes e8f1fff0
+ 00495260 bytes 68f1ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f70dafbcf5ed96dca9c6b0234c583792"></a>

### [`004724fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004724fc.md) → [`00495394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495394.md) FUN_00495394

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00821350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821350.md) [`00821cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cbc.md) [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) [`008443c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443c8.md) · 呼出先 2件 [`00472e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472e6c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 5件 [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`008532c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/008532c8.md) [`00853c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c38.md) [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) [`008766b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008766b4.md) · 呼出先 2件 [`00495d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00495450",
      "incomplete_value": true,
      "site": "00495450",
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
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004725b8",
      "incomplete_value": true,
      "site": "004725b8",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004953b0",
      "incomplete_value": true,
      "site": "004953b0",
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
      "definition_site": "00472518",
      "incomplete_value": true,
      "site": "00472518",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00495408",
      "incomplete_value": false,
      "site": "0049540c",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00472570",
      "incomplete_value": false,
      "site": "00472574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "004953ac",
      "READ",
      [
        "storage",
        "00c25350",
        null,
        "undefined8"
      ]
    ],
    [
      "004953c4",
      "READ",
      [
        "storage",
        "00c25350",
        null,
        "undefined8"
      ]
    ],
    [
      "004953d0",
      "READ",
      [
        "storage",
        "00c25330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004953ac",
      "READ",
      [
        "storage",
        "00ca4e10",
        null,
        "undefined8"
      ]
    ],
    [
      "004953c4",
      "READ",
      [
        "storage",
        "00ca4e10",
        null,
        "undefined8"
      ]
    ],
    [
      "004953d0",
      "READ",
      [
        "storage",
        "00ca4df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00472574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004724fc.md#insn-00472574) · [`004725b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004724fc.md#insn-004725b8) · [`0047250c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004724fc.md#insn-0047250c)
- 新版 [`0049540c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495394.md#insn-0049540c) · [`00495450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495394.md#insn-00495450) · [`004953a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495394.md#insn-004953a4)

~~~diff
- 00472574 ["INT_ADD", "register:40f0:8", ["const:472574:8", "const:4:8"]]
- 00472574 ["CALL", null, ["callee:00495d04:8"]]
+ 0049540c ["INT_ADD", "register:40f0:8", ["const:49540c:8", "const:4:8"]]
+ 0049540c ["CALL", null, ["callee:00495d04:8"]]
- 00472574 bytes 3e020094
+ 0049540c bytes 3e020094
- 004725b8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:350:8"]]
- 004725b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00495450 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e10:8"]]
+ 00495450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 004725b8 bytes a8aa01f9
+ 00495450 bytes a80a07f9
- 0047250c ["COPY", "register:40a8:8", ["const:c25000:8"]]
+ 004953a4 ["COPY", "register:40a8:8", ["const:ca4000:8"]]
- 0047250c bytes 953d00f0
+ 004953a4 bytes 754000f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79610b3a58cdef32c98e56efa7c177e3"></a>

### [`004725e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004725e0.md) → [`00495478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495478.md) FUN_00495478

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 2件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004954a4",
      "incomplete_value": true,
      "site": "004954ac",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047260c",
      "incomplete_value": true,
      "site": "00472614",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00495480",
      "incomplete_value": true,
      "site": "00495480",
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
      "definition_site": "004725e8",
      "incomplete_value": true,
      "site": "004725e8",
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
    "guard": [
      [
        "FALL_THROUGH",
        "004725e8"
      ],
      [
        "FALL_THROUGH",
        "00495480"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00495480",
      "incomplete_value": true,
      "site": "004954ac",
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
      "definition_site": "004725e8",
      "incomplete_value": true,
      "site": "00472614",
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
      "0049547c",
      "READ",
      [
        "storage",
        "00c25350",
        null,
        "undefined8"
      ]
    ],
    [
      "0049548c",
      "READ",
      [
        "storage",
        "00c25348",
        null,
        "undefined8"
      ]
    ],
    [
      "00495490",
      "READ",
      [
        "storage",
        "00c25330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0049547c",
      "READ",
      [
        "storage",
        "00ca4e10",
        null,
        "undefined8"
      ]
    ],
    [
      "0049548c",
      "READ",
      [
        "storage",
        "00ca4e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00495490",
      "READ",
      [
        "storage",
        "00ca4df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004725e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004725e0.md#insn-004725e0) · [`004725e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004725e0.md#insn-004725e4) · [`004725ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004725e0.md#insn-004725ec)
- 新版 [`00495478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495478.md#insn-00495478) · [`0049547c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495478.md#insn-0049547c) · [`00495484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495478.md#insn-00495484)

~~~diff
- 004725e0 ["COPY", "register:4048:8", ["const:c25000:8"]]
+ 00495478 ["COPY", "register:4048:8", ["const:ca4000:8"]]
- 004725e0 bytes 893d00f0
+ 00495478 bytes 694000f0
- 004725e4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:350:8"]]
- 004725e4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049547c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
+ 0049547c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004725e4 bytes 29a941f9
+ 0049547c bytes 290947f9
- 004725ec ["COPY", "register:4048:8", ["const:c25000:8"]]
+ 00495484 ["COPY", "register:4048:8", ["const:ca4000:8"]]
- 004725ec bytes 893d00f0
+ 00495484 bytes 694000f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-581ec8b01128c2bcf499a5224cd909fb"></a>

### [`00472640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472640.md) → [`004954d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/004954d8.md) FUN_004954d8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 19件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`00445ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445ae8.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md)
- 新版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 19件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468980.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 84.97% / 新版 84.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_destination` 1件, `store_value` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00495548",
      "incomplete_value": true,
      "site": "00495550",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004726b0",
      "incomplete_value": true,
      "site": "004726b8",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00495a2c",
      "incomplete_value": false,
      "site": "00495a2c",
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
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00472b94",
      "incomplete_value": false,
      "site": "00472b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00495514",
      "incomplete_value": true,
      "site": "00495514",
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
      "definition_site": "0047267c",
      "incomplete_value": true,
      "site": "0047267c",
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
      "00495510",
      "READ",
      [
        "storage",
        "00c25350",
        null,
        "undefined8"
      ]
    ],
    [
      "00495524",
      "READ",
      [
        "storage",
        "00c25348",
        null,
        "undefined8"
      ]
    ],
    [
      "00495528",
      "READ",
      [
        "storage",
        "00c25330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00495510",
      "READ",
      [
        "storage",
        "00ca4e10",
        null,
        "undefined8"
      ]
    ],
    [
      "00495524",
      "READ",
      [
        "storage",
        "00ca4e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00495528",
      "READ",
      [
        "storage",
        "00ca4df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00472730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472640.md#insn-00472730) · [`00472828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472640.md#insn-00472828) · [`00472838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/00472640.md#insn-00472838)
- 新版 [`004956c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/004954d8.md#insn-004956c0) · [`004956d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/004954d8.md#insn-004956d0)

~~~diff
- 00472730 ["INT_ADD", "register:40f0:8", ["const:472730:8", "const:4:8"]]
- 00472730 ["CALL", null, ["callee:008514b8:8"]]
- 00472730 bytes 94b30e94
- 00472828 ["INT_ADD", "register:40f0:8", ["const:472828:8", "const:4:8"]]
- 00472828 ["CALL", null, ["callee:00c58210:8"]]
+ 004956c0 ["INT_ADD", "register:40f0:8", ["const:4956c0:8", "const:4:8"]]
+ 004956c0 ["CALL", null, ["callee:00c58210:8"]]
- 00472828 bytes e6a31d94
+ 004956c0 bytes d40a1f94
- 00472838 ["INT_ADD", "register:40f0:8", ["const:472838:8", "const:4:8"]]
- 00472838 ["CALL", null, ["callee:0046cacc:8"]]
+ 004956d0 ["INT_ADD", "register:40f0:8", ["const:4956d0:8", "const:4:8"]]
+ 004956d0 ["CALL", null, ["callee:0046cacc:8"]]
- 00472838 bytes ff5cff97
+ 004956d0 bytes ff5cff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d65b7fc87e9fb4e962185c2e2060d94"></a>

### [`004737cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/004737cc.md) → [`00496664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496664.md) _INIT_23

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`004723a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004723a4.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`0049523c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/0049523c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 6件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004966a0",
      "incomplete_value": true,
      "site": "004966bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00473808",
      "incomplete_value": true,
      "site": "00473824",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004966c4",
      "incomplete_value": true,
      "site": "004966e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0047382c",
      "incomplete_value": true,
      "site": "00473848",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004966e4",
      "incomplete_value": true,
      "site": "00496700",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0047384c",
      "incomplete_value": true,
      "site": "00473868",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "004966a0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "004966c4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "004966e4",
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
      "004966a0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "004966c4",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "004966e4",
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

- 旧版 [`0047392c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/004737cc.md#insn-0047392c) · [`00473a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/004737cc.md#insn-00473a04) · [`00473a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/004737cc.md#insn-00473a28)
- 新版 [`004967c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496664.md#insn-004967c4) · [`0049689c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496664.md#insn-0049689c) · [`004968c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496664.md#insn-004968c0)

~~~diff
- 0047392c ["INT_ADD", "register:40f0:8", ["const:47392c:8", "const:4:8"]]
- 0047392c ["CALL", null, ["callee:0043b7b8:8"]]
+ 004967c4 ["INT_ADD", "register:40f0:8", ["const:4967c4:8", "const:4:8"]]
+ 004967c4 ["CALL", null, ["callee:0043b7b8:8"]]
- 0047392c bytes e394fe97
+ 004967c4 bytes fd93fe97
- 00473a04 ["INT_ADD", "register:40f0:8", ["const:473a04:8", "const:4:8"]]
- 00473a04 ["CALL", null, ["callee:00c57a30:8"]]
+ 0049689c ["INT_ADD", "register:40f0:8", ["const:49689c:8", "const:4:8"]]
+ 0049689c ["CALL", null, ["callee:00c57a30:8"]]
- 00473a04 bytes 779d1d94
+ 0049689c bytes 65041f94
- 00473a28 ["INT_ADD", "register:40f0:8", ["const:473a28:8", "const:4:8"]]
- 00473a28 ["CALL", null, ["callee:00c57a30:8"]]
+ 004968c0 ["INT_ADD", "register:40f0:8", ["const:4968c0:8", "const:4:8"]]
+ 004968c0 ["CALL", null, ["callee:00c57a30:8"]]
- 00473a28 bytes 6e9d1d94
+ 004968c0 bytes 5c041f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-020008b3f5ad8d7534c5b9d545145eda"></a>

### [`00473b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473b84.md) → [`00496a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496a1c.md) FUN_00496a1c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`0073ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073ab94.md) [`0073e258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e258.md) [`0073e4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e4a4.md) [`0073e6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e6dc.md) [`0073eb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073eb44.md) · 呼出先 12件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0052dd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd54.md) [`00574144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574144.md)
- 新版 呼出元 6件 [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`00768564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768564.md) [`007687b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007687b0.md) [`007689e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007689e8.md) [`00768e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768e50.md) · 呼出先 12件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00550bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bec.md) [`00596fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596fdc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00496b2c",
      "incomplete_value": false,
      "site": "00496b34",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00473c94",
      "incomplete_value": false,
      "site": "00473c9c",
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
            "const:ed0:8"
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
      "definition_site": "00496b4c",
      "incomplete_value": false,
      "site": "00496b4c",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00473cb4",
      "incomplete_value": false,
      "site": "00473cb4",
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
            "const:f20:8"
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
      "definition_site": "00496bd0",
      "incomplete_value": false,
      "site": "00496bd8",
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
      "definition_site": "00473d38",
      "incomplete_value": false,
      "site": "00473d40",
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
      "00496b34",
      "DATA",
      [
        "storage",
        "00be8ed0",
        null,
        "undefined *"
      ]
    ],
    [
      "00496b4c",
      "DATA",
      [
        "storage",
        "00be8f20",
        null,
        "undefined *"
      ]
    ],
    [
      "00496bd8",
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
      "00496b34",
      "DATA",
      [
        "storage",
        "00c65a90",
        null,
        "undefined *"
      ]
    ],
    [
      "00496b4c",
      "DATA",
      [
        "storage",
        "00c65ae0",
        null,
        "undefined *"
      ]
    ],
    [
      "00496bd8",
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

- 旧版 [`00473bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473b84.md#insn-00473bb8) · [`00473c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473b84.md#insn-00473c20) · [`00473c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473b84.md#insn-00473c48)
- 新版 [`00496a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496a1c.md#insn-00496a50) · [`00496ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496a1c.md#insn-00496ab8) · [`00496ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496a1c.md#insn-00496ae0)

~~~diff
- 00473bb8 ["INT_ADD", "register:40f0:8", ["const:473bb8:8", "const:4:8"]]
- 00473bb8 ["CALL", null, ["callee:00550bec:8"]]
+ 00496a50 ["INT_ADD", "register:40f0:8", ["const:496a50:8", "const:4:8"]]
+ 00496a50 ["CALL", null, ["callee:00550bec:8"]]
- 00473bb8 bytes 67e80294
+ 00496a50 bytes 67e80294
- 00473c20 ["INT_ADD", "register:40f0:8", ["const:473c20:8", "const:4:8"]]
- 00473c20 ["CALL", null, ["callee:00c57a90:8"]]
+ 00496ab8 ["INT_ADD", "register:40f0:8", ["const:496ab8:8", "const:4:8"]]
+ 00496ab8 ["CALL", null, ["callee:00c57a90:8"]]
- 00473c20 bytes 089d1d94
+ 00496ab8 bytes f6031f94
- 00473c48 ["INT_ADD", "register:40f0:8", ["const:473c48:8", "const:4:8"]]
- 00473c48 ["CALL", null, ["callee:00c57b40:8"]]
+ 00496ae0 ["INT_ADD", "register:40f0:8", ["const:496ae0:8", "const:4:8"]]
+ 00496ae0 ["CALL", null, ["callee:00c57b40:8"]]
- 00473c48 bytes 2a9d1d94
+ 00496ae0 bytes 18041f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-636961733811faad753a9ebbdb0598bf"></a>

### [`00473f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473f20.md) → [`00496db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496db8.md) FUN_00496db8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00496dd0",
      "incomplete_value": false,
      "site": "00496dd4",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00473f38",
      "incomplete_value": false,
      "site": "00473f3c",
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
            "const:f20:8"
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
      "00496dd4",
      "DATA",
      [
        "storage",
        "00be8f20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00496dd4",
      "DATA",
      [
        "storage",
        "00c65ae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00473f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473f20.md#insn-00473f34) · [`00473f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473f20.md#insn-00473f38) · [`00473f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00473/00473f20.md#insn-00473f4c)
- 新版 [`00496dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496db8.md#insn-00496dcc) · [`00496dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496db8.md#insn-00496dd0) · [`00496de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496db8.md#insn-00496de4)

~~~diff
- 00473f34 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00496dcc ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00473f34 bytes a83b00b0
+ 00496dcc bytes 683e00f0
- 00473f38 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00473f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00473f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00473f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00496dd0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 00496dd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00496dd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00496dd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00473f38 bytes 08813c91
+ 00496dd0 bytes 08812b91
- 00473f4c ["INT_ADD", "register:40f0:8", ["const:473f4c:8", "const:4:8"]]
- 00473f4c ["CALL", null, ["callee:00c538e0:8"]]
+ 00496de4 ["INT_ADD", "register:40f0:8", ["const:496de4:8", "const:4:8"]]
+ 00496de4 ["CALL", null, ["callee:00c538e0:8"]]
- 00473f4c bytes d18b1d94
+ 00496de4 bytes bff21e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-161491b90b6db0803e9e46caba54e56c"></a>

### [`00474160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474160.md) → [`00496ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496ff8.md) FUN_00496ff8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574238.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`005970d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
      "definition_site": "00497040",
      "incomplete_value": true,
      "site": "00497048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004741a8",
      "incomplete_value": true,
      "site": "004741b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00497034",
      "READ",
      [
        "storage",
        "00c1ae30",
        null,
        "pointer"
      ]
    ],
    [
      "00497048",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ],
    [
      "00497070",
      "READ",
      [
        "storage",
        "00bf0650",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00497034",
      "READ",
      [
        "storage",
        "00c9a820",
        null,
        "pointer"
      ]
    ],
    [
      "00497048",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ],
    [
      "00497070",
      "READ",
      [
        "storage",
        "00c6d210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474160.md#insn-00474190) · [`00474194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474160.md#insn-00474194) · [`0047419c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474160.md#insn-0047419c)
- 新版 [`00497028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496ff8.md#insn-00497028) · [`0049702c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496ff8.md#insn-0049702c) · [`00497034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496ff8.md#insn-00497034)

~~~diff
- 00474190 ["INT_ADD", "register:40f0:8", ["const:474190:8", "const:4:8"]]
- 00474190 ["CALL", null, ["callee:00c57a90:8"]]
+ 00497028 ["INT_ADD", "register:40f0:8", ["const:497028:8", "const:4:8"]]
+ 00497028 ["CALL", null, ["callee:00c57a90:8"]]
- 00474190 bytes ac9b1d94
+ 00497028 bytes 9a021f94
- 00474194 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 0049702c ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00474194 bytes 293d00d0
+ 0049702c bytes 094000f0
- 0047419c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e30:8"]]
- 0047419c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00497034 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:820:8"]]
+ 00497034 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0047419c bytes 291947f9
+ 00497034 bytes 291144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aafa63e9aa86f503e79058df9e4b095b"></a>

### [`0047423c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047423c.md) → [`004970d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004970d4.md) FUN_004970d4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574238.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`005970d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
      "definition_site": "00497124",
      "incomplete_value": true,
      "site": "0049712c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0047428c",
      "incomplete_value": true,
      "site": "00474294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00497118",
      "READ",
      [
        "storage",
        "00c1ae30",
        null,
        "pointer"
      ]
    ],
    [
      "0049712c",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ],
    [
      "00497154",
      "READ",
      [
        "storage",
        "00bf0650",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00497118",
      "READ",
      [
        "storage",
        "00c9a820",
        null,
        "pointer"
      ]
    ],
    [
      "0049712c",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ],
    [
      "00497154",
      "READ",
      [
        "storage",
        "00c6d210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047423c.md#insn-00474270) · [`00474274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047423c.md#insn-00474274) · [`00474280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047423c.md#insn-00474280)
- 新版 [`00497108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004970d4.md#insn-00497108) · [`0049710c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004970d4.md#insn-0049710c) · [`00497118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004970d4.md#insn-00497118)

~~~diff
- 00474270 ["INT_ADD", "register:40f0:8", ["const:474270:8", "const:4:8"]]
- 00474270 ["CALL", null, ["callee:00c57a90:8"]]
+ 00497108 ["INT_ADD", "register:40f0:8", ["const:497108:8", "const:4:8"]]
+ 00497108 ["CALL", null, ["callee:00c57a90:8"]]
- 00474270 bytes 749b1d94
+ 00497108 bytes 62021f94
- 00474274 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 0049710c ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00474274 bytes 293d00d0
+ 0049710c bytes 094000f0
- 00474280 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e30:8"]]
- 00474280 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00497118 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:820:8"]]
+ 00497118 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00474280 bytes 291947f9
+ 00497118 bytes 291144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f76fc4429f667fb2b584c6cea649de64"></a>

### [`00474324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474324.md) → [`004971bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004971bc.md) FUN_004971bc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574238.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`005970d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
      "definition_site": "00497208",
      "incomplete_value": true,
      "site": "00497210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00474370",
      "incomplete_value": true,
      "site": "00474378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004971fc",
      "READ",
      [
        "storage",
        "00c1ae30",
        null,
        "pointer"
      ]
    ],
    [
      "00497210",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ],
    [
      "00497238",
      "READ",
      [
        "storage",
        "00bf0650",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004971fc",
      "READ",
      [
        "storage",
        "00c9a820",
        null,
        "pointer"
      ]
    ],
    [
      "00497210",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ],
    [
      "00497238",
      "READ",
      [
        "storage",
        "00c6d210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474324.md#insn-00474354) · [`00474358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474324.md#insn-00474358) · [`00474364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474324.md#insn-00474364)
- 新版 [`004971ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004971bc.md#insn-004971ec) · [`004971f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004971bc.md#insn-004971f0) · [`004971fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004971bc.md#insn-004971fc)

~~~diff
- 00474354 ["INT_ADD", "register:40f0:8", ["const:474354:8", "const:4:8"]]
- 00474354 ["CALL", null, ["callee:00c57a90:8"]]
+ 004971ec ["INT_ADD", "register:40f0:8", ["const:4971ec:8", "const:4:8"]]
+ 004971ec ["CALL", null, ["callee:00c57a90:8"]]
- 00474354 bytes 3b9b1d94
+ 004971ec bytes 29021f94
- 00474358 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 004971f0 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00474358 bytes 293d00d0
+ 004971f0 bytes 094000f0
- 00474364 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e30:8"]]
- 00474364 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004971fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:820:8"]]
+ 004971fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00474364 bytes 291947f9
+ 004971fc bytes 291144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4e096a2650f50cfce7e99d690c37bfc"></a>

### [`00474404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474404.md) → [`0049729c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/0049729c.md) FUN_0049729c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574238.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`005970d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
      "definition_site": "004972e4",
      "incomplete_value": true,
      "site": "004972ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0047444c",
      "incomplete_value": true,
      "site": "00474454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004972d8",
      "READ",
      [
        "storage",
        "00c1ae30",
        null,
        "pointer"
      ]
    ],
    [
      "004972ec",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ],
    [
      "00497314",
      "READ",
      [
        "storage",
        "00bf0650",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004972d8",
      "READ",
      [
        "storage",
        "00c9a820",
        null,
        "pointer"
      ]
    ],
    [
      "004972ec",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ],
    [
      "00497314",
      "READ",
      [
        "storage",
        "00c6d210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474404.md#insn-00474434) · [`00474438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474404.md#insn-00474438) · [`00474440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474404.md#insn-00474440)
- 新版 [`004972cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/0049729c.md#insn-004972cc) · [`004972d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/0049729c.md#insn-004972d0) · [`004972d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/0049729c.md#insn-004972d8)

~~~diff
- 00474434 ["INT_ADD", "register:40f0:8", ["const:474434:8", "const:4:8"]]
- 00474434 ["CALL", null, ["callee:00c57a90:8"]]
+ 004972cc ["INT_ADD", "register:40f0:8", ["const:4972cc:8", "const:4:8"]]
+ 004972cc ["CALL", null, ["callee:00c57a90:8"]]
- 00474434 bytes 039b1d94
+ 004972cc bytes f1011f94
- 00474438 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 004972d0 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00474438 bytes 293d00d0
+ 004972d0 bytes 094000f0
- 00474440 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e30:8"]]
- 00474440 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004972d8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:820:8"]]
+ 004972d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00474440 bytes 291947f9
+ 004972d8 bytes 291144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6571eb5cbad2c9982480409ff527883e"></a>

### [`004744e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004744e8.md) → [`00497380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497380.md) FUN_00497380

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`0052de60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052de60.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`00550cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.71% / 新版 88.71%

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
      "definition_site": "004973f8",
      "incomplete_value": true,
      "site": "00497400",
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
      "definition_site": "00474560",
      "incomplete_value": true,
      "site": "00474568",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00497408",
      "incomplete_value": true,
      "site": "00497408",
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
      "definition_site": "00474570",
      "incomplete_value": true,
      "site": "00474570",
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497408",
      "incomplete_value": true,
      "site": "00497408",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00474570",
      "incomplete_value": true,
      "site": "00474570",
      "value": [
        "LOAD",
        "8",
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004973f4",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ],
    [
      "004973f8",
      "READ",
      [
        "storage",
        "00c13340",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004973fc",
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
      "004973f4",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "004973f8",
      "READ",
      [
        "storage",
        "00c92ce8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004973fc",
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

- 旧版 [`00474518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004744e8.md#insn-00474518) · [`00474524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004744e8.md#insn-00474524) · [`00474530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004744e8.md#insn-00474530)
- 新版 [`004973b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497380.md#insn-004973b0) · [`004973bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497380.md#insn-004973bc) · [`004973c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497380.md#insn-004973c8)

~~~diff
- 00474518 ["INT_ADD", "register:40f0:8", ["const:474518:8", "const:4:8"]]
- 00474518 ["CALL", null, ["callee:00451870:8"]]
+ 004973b0 ["INT_ADD", "register:40f0:8", ["const:4973b0:8", "const:4:8"]]
+ 004973b0 ["CALL", null, ["callee:00451870:8"]]
- 00474518 bytes 30e9fe97
+ 004973b0 bytes 30e9fe97
- 00474524 ["INT_ADD", "register:40f0:8", ["const:474524:8", "const:4:8"]]
- 00474524 ["CALL", null, ["callee:00451998:8"]]
+ 004973bc ["INT_ADD", "register:40f0:8", ["const:4973bc:8", "const:4:8"]]
+ 004973bc ["CALL", null, ["callee:00451998:8"]]
- 00474524 bytes 77e9fe97
+ 004973bc bytes 77e9fe97
- 00474530 ["INT_ADD", "register:40f0:8", ["const:474530:8", "const:4:8"]]
- 00474530 ["CALL", null, ["callee:00c57db0:8"]]
+ 004973c8 ["INT_ADD", "register:40f0:8", ["const:4973c8:8", "const:4:8"]]
+ 004973c8 ["CALL", null, ["callee:00c57db0:8"]]
- 00474530 bytes 8c9b1d94
+ 004973c8 bytes 7a021f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46d7e39ea15c3c814df895c12645fab1"></a>

### [`004747cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004747cc.md) → [`00497664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md) FUN_00497664

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00469fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fa8.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0048ce40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce40.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.94% / 新版 92.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004976a0",
      "incomplete_value": true,
      "site": "004976b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:967:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474808",
      "incomplete_value": true,
      "site": "00474820",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3ad:8"
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
      "definition_site": "004976bc",
      "incomplete_value": true,
      "site": "004976d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00474824",
      "incomplete_value": true,
      "site": "00474838",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "004976a0",
      "READ",
      [
        "storage",
        "002a03ad",
        null,
        "string"
      ]
    ],
    [
      "004976bc",
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
      "004976a0",
      "READ",
      [
        "storage",
        "002b0967",
        null,
        "string"
      ]
    ],
    [
      "004976bc",
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

- 旧版 [`004747f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004747cc.md#insn-004747f0) · [`004747f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004747cc.md#insn-004747f8) · [`00474800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004747cc.md#insn-00474800)
- 新版 [`00497688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md#insn-00497688) · [`00497690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md#insn-00497690) · [`00497698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md#insn-00497698)

~~~diff
- 004747f0 ["INT_ADD", "register:40f0:8", ["const:4747f0:8", "const:4:8"]]
- 004747f0 ["CALL", null, ["callee:00588e2c:8"]]
+ 00497688 ["INT_ADD", "register:40f0:8", ["const:497688:8", "const:4:8"]]
+ 00497688 ["CALL", null, ["callee:00588e2c:8"]]
- 004747f0 bytes e9c50394
+ 00497688 bytes e9c50394
- 004747f8 ["INT_ADD", "register:40f0:8", ["const:4747f8:8", "const:4:8"]]
- 004747f8 ["CALL", null, ["callee:0058911c:8"]]
+ 00497690 ["INT_ADD", "register:40f0:8", ["const:497690:8", "const:4:8"]]
+ 00497690 ["CALL", null, ["callee:0058911c:8"]]
- 004747f8 bytes a3c60394
+ 00497690 bytes a3c60394
- 00474800 ["COPY", "register:4048:8", ["const:2a0000:8"]]
+ 00497698 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00474800 bytes 69f1ff90
+ 00497698 bytes c9f0ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9f240aa12ed4972ffeb1ee0ac09891b"></a>

### [`004749f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004749f8.md) → [`00497890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md) FUN_00497890

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00469f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f78.md) · 呼出先 8件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) · 呼出先 8件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004978d0",
      "incomplete_value": true,
      "site": "004978e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:252:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474a38",
      "incomplete_value": true,
      "site": "00474a50",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:271:8"
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
      "004978d0",
      "READ",
      [
        "storage",
        "0029b271",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004978d0",
      "READ",
      [
        "storage",
        "002ab252",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004749f8.md#insn-00474a18) · [`00474a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004749f8.md#insn-00474a20) · [`00474a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004749f8.md#insn-00474a28)
- 新版 [`004978b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md#insn-004978b0) · [`004978b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md#insn-004978b8) · [`004978c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md#insn-004978c0)

~~~diff
- 00474a18 ["INT_ADD", "register:40f0:8", ["const:474a18:8", "const:4:8"]]
- 00474a18 ["CALL", null, ["callee:00588e2c:8"]]
+ 004978b0 ["INT_ADD", "register:40f0:8", ["const:4978b0:8", "const:4:8"]]
+ 004978b0 ["CALL", null, ["callee:00588e2c:8"]]
- 00474a18 bytes 5fc50394
+ 004978b0 bytes 5fc50394
- 00474a20 ["INT_ADD", "register:40f0:8", ["const:474a20:8", "const:4:8"]]
- 00474a20 ["CALL", null, ["callee:0058911c:8"]]
+ 004978b8 ["INT_ADD", "register:40f0:8", ["const:4978b8:8", "const:4:8"]]
+ 004978b8 ["CALL", null, ["callee:0058911c:8"]]
- 00474a20 bytes 19c60394
+ 004978b8 bytes 19c60394
- 00474a28 ["COPY", "register:4048:8", ["const:29b000:8"]]
+ 004978c0 ["COPY", "register:4048:8", ["const:2ab000:8"]]
- 00474a28 bytes 29f1fff0
+ 004978c0 bytes a9f0ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89265223188e67f3035aa8be0a577fd6"></a>

### [`00474c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474c0c.md) → [`00497aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497aa4.md) FUN_00497aa4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0060f9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060f9b8.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`006354b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006354b0.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00497ae4",
      "incomplete_value": false,
      "site": "00497ae8",
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
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474c4c",
      "incomplete_value": false,
      "site": "00474c50",
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
            "const:fb8:8"
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
      "definition_site": "00497b2c",
      "incomplete_value": false,
      "site": "00497b30",
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
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474c94",
      "incomplete_value": false,
      "site": "00474c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "00497ae8",
      "DATA",
      [
        "storage",
        "00be8fb8",
        null,
        "undefined *"
      ]
    ],
    [
      "00497b30",
      "DATA",
      [
        "storage",
        "00be9008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00497ae8",
      "DATA",
      [
        "storage",
        "00c65b78",
        null,
        "undefined *"
      ]
    ],
    [
      "00497b30",
      "DATA",
      [
        "storage",
        "00c65bc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474c0c.md#insn-00474c40) · [`00474c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474c0c.md#insn-00474c48) · [`00474c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474c0c.md#insn-00474c4c)
- 新版 [`00497ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497aa4.md#insn-00497ad8) · [`00497ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497aa4.md#insn-00497ae0) · [`00497ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497aa4.md#insn-00497ae4)

~~~diff
- 00474c40 ["INT_ADD", "register:40f0:8", ["const:474c40:8", "const:4:8"]]
- 00474c40 ["CALL", null, ["callee:00c57a90:8"]]
+ 00497ad8 ["INT_ADD", "register:40f0:8", ["const:497ad8:8", "const:4:8"]]
+ 00497ad8 ["CALL", null, ["callee:00c57a90:8"]]
- 00474c40 bytes 00991d94
+ 00497ad8 bytes eeff1e94
- 00474c48 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00497ae0 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00474c48 bytes a83b0090
+ 00497ae0 bytes 683e00d0
- 00474c4c ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 00474c4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00474c4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00474c4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00497ae4 ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 00497ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00497ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00497ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00474c4c bytes 08e13e91
+ 00497ae4 bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d35c9631c896b19eca494a3ecb348a4e"></a>

### [`00474da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474da4.md) → [`00497c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md) FUN_00497c3c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0060f9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060f9b8.md) · 呼出先 7件 [`004751fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004751fc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb320.md)
- 新版 呼出元 2件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`006354b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006354b0.md) · 呼出先 7件 [`00498094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497c84",
      "incomplete_value": true,
      "site": "00497c88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474dec",
      "incomplete_value": true,
      "site": "00474df0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:820:8"
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
      "definition_site": "00497c70",
      "incomplete_value": false,
      "site": "00497c74",
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
            "const:649:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474dd8",
      "incomplete_value": false,
      "site": "00474ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:3bf:8"
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
      "00497c70",
      "PARAM",
      [
        "storage",
        "0029d3bf",
        null,
        "string"
      ]
    ],
    [
      "00497c84",
      "READ",
      [
        "storage",
        "002b2820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00497c70",
      "PARAM",
      [
        "storage",
        "002ad649",
        null,
        "string"
      ]
    ],
    [
      "00497c84",
      "READ",
      [
        "storage",
        "002c3f00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474da4.md#insn-00474ddc) · [`00474dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474da4.md#insn-00474dd4) · [`00474dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474da4.md#insn-00474dd8)
- 新版 [`00497c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md#insn-00497c74) · [`00497c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md#insn-00497c6c) · [`00497c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md#insn-00497c70)

~~~diff
- 00474ddc ["INT_ADD", "register:40f0:8", ["const:474ddc:8", "const:4:8"]]
- 00474ddc ["CALL", null, ["callee:00c58070:8"]]
+ 00497c74 ["INT_ADD", "register:40f0:8", ["const:497c74:8", "const:4:8"]]
+ 00497c74 ["CALL", null, ["callee:00c58070:8"]]
- 00474ddc bytes 119a1d94
+ 00497c74 bytes ff001f94
- 00474dd4 ["COPY", "register:4000:8", ["const:29d000:8"]]
+ 00497c6c ["COPY", "register:4000:8", ["const:2ad000:8"]]
- 00474dd4 bytes 40f1ffb0
+ 00497c6c bytes a0f0ffd0
- 00474dd8 ["COPY", "tmp:0:8", ["const:3bf:8"]]
- 00474dd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00474dd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00474dd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00497c70 ["COPY", "tmp:0:8", ["const:649:8"]]
+ 00497c70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00497c70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00497c70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00474dd8 bytes 00fc0e91
+ 00497c70 bytes 00241991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9451564873c38e2486bbbd1b23623156"></a>

### [`00474f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474f1c.md) → [`00497db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497db4.md) FUN_00497db4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0060f9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060f9b8.md) · 呼出先 11件 [`004751fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004751fc.md) [`00475e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475e24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)
- 新版 呼出元 1件 [`006354b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006354b0.md) · 呼出先 11件 [`00498094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md) [`00498cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

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
      "definition_site": "00497e04",
      "incomplete_value": true,
      "site": "00497e08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474f6c",
      "incomplete_value": true,
      "site": "00474f70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:820:8"
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
      "definition_site": "00497df0",
      "incomplete_value": false,
      "site": "00497df4",
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
            "const:649:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474f58",
      "incomplete_value": false,
      "site": "00474f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:3bf:8"
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
      "definition_site": "00497f14",
      "incomplete_value": false,
      "site": "00497f24",
      "value": [
        "leaf",
        "const:498cbc:8"
      ]
    },
    "old": {
      "definition_site": "0047507c",
      "incomplete_value": false,
      "site": "0047508c",
      "value": [
        "leaf",
        "const:475e24:8"
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
      "00497df0",
      "PARAM",
      [
        "storage",
        "0029d3bf",
        null,
        "string"
      ]
    ],
    [
      "00497e04",
      "READ",
      [
        "storage",
        "002b2820",
        null,
        "undefined8"
      ]
    ],
    [
      "00497f14",
      "PARAM",
      [
        "storage",
        "00475e24",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00497df0",
      "PARAM",
      [
        "storage",
        "002ad649",
        null,
        "string"
      ]
    ],
    [
      "00497e04",
      "READ",
      [
        "storage",
        "002c3f00",
        null,
        "undefined8"
      ]
    ],
    [
      "00497f14",
      "PARAM",
      [
        "storage",
        "00498cbc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474f1c.md#insn-00474f5c) · [`0047508c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474f1c.md#insn-0047508c) · [`00475120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474f1c.md#insn-00475120)
- 新版 [`00497df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497db4.md#insn-00497df4) · [`00497f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497db4.md#insn-00497f24) · [`00497fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497db4.md#insn-00497fb8)

~~~diff
- 00474f5c ["INT_ADD", "register:40f0:8", ["const:474f5c:8", "const:4:8"]]
- 00474f5c ["CALL", null, ["callee:00c58070:8"]]
+ 00497df4 ["INT_ADD", "register:40f0:8", ["const:497df4:8", "const:4:8"]]
+ 00497df4 ["CALL", null, ["callee:00c58070:8"]]
- 00474f5c bytes b1991d94
+ 00497df4 bytes 9f001f94
- 0047508c ["INT_ADD", "register:40f0:8", ["const:47508c:8", "const:4:8"]]
- 0047508c ["CALL", null, ["callee:00c57d10:8"]]
+ 00497f24 ["INT_ADD", "register:40f0:8", ["const:497f24:8", "const:4:8"]]
+ 00497f24 ["CALL", null, ["callee:00c57d10:8"]]
- 0047508c bytes 8d981d94
+ 00497f24 bytes 7bff1e94
- 00475120 ["INT_ADD", "register:40f0:8", ["const:475120:8", "const:4:8"]]
- 00475120 ["CALL", null, ["callee:00c57d20:8"]]
+ 00497fb8 ["INT_ADD", "register:40f0:8", ["const:497fb8:8", "const:4:8"]]
+ 00497fb8 ["CALL", null, ["callee:00c57d20:8"]]
- 00475120 bytes 6c981d94
+ 00497fb8 bytes 5aff1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61205e2a59818b15f50b0896133ac157"></a>

### [`00475470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475470.md) → [`00498308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md) FUN_00498308

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0047580c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/0047580c.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) [`0060dcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060dcac.md) [`008216e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/008216e4.md) · 呼出先 4件 [`004751fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004751fc.md) [`00475708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475708.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7d0.md)
- 新版 呼出元 4件 [`004986a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) [`00853660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853660.md) · 呼出先 4件 [`00498094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md) [`004985a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004985a0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58220.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049838c",
      "incomplete_value": true,
      "site": "00498398",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004754f4",
      "incomplete_value": true,
      "site": "00475500",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:938:8"
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
      "0049838c",
      "READ",
      [
        "storage",
        "002b2938",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0049838c",
      "READ",
      [
        "storage",
        "002c4030",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00475498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475470.md#insn-00475498) · [`004754d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475470.md#insn-004754d8) · [`004754e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475470.md#insn-004754e8)
- 新版 [`00498330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md#insn-00498330) · [`00498370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md#insn-00498370) · [`00498380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md#insn-00498380)

~~~diff
- 00475498 ["INT_ADD", "register:40f0:8", ["const:475498:8", "const:4:8"]]
- 00475498 ["CALL", null, ["callee:00c58220:8"]]
+ 00498330 ["INT_ADD", "register:40f0:8", ["const:498330:8", "const:4:8"]]
+ 00498330 ["CALL", null, ["callee:00c58220:8"]]
- 00475498 bytes ce981d94
+ 00498330 bytes bcff1e94
- 004754d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004754d8 ["INT_ADD", "register:40f0:8", ["const:4754d8:8", "const:4:8"]]
- 004754d8 ["CALLIND", null, ["register:0:8"]]
+ 00498370 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00498370 ["INT_ADD", "register:40f0:8", ["const:498370:8", "const:4:8"]]
+ 00498370 ["CALLIND", null, ["register:0:8"]]
- 004754d8 bytes 00013fd6
+ 00498370 bytes 00013fd6
- 004754e8 ["COPY", "register:4040:8", ["const:2b2000:8"]]
+ 00498380 ["COPY", "register:4040:8", ["const:2c4000:8"]]
- 004754e8 bytes e8f1ffb0
+ 00498380 bytes 68f1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-380c37123889381798588618d75e4584"></a>

### [`0047580c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/0047580c.md) → [`004986a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md) FUN_004986a4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 4件 [`0060ffa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060ffa8.md) [`00610540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610540.md) [`00838c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838c74.md) [`00838ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838ef4.md) · 呼出先 6件 [`00475470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475470.md) [`00477e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477e0c.md) [`00477e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477e1c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 4件 [`00635aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635aa0.md) [`00636038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636038.md) [`0086af14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086af14.md) [`0086b194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b194.md) · 呼出先 6件 [`00498308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md) [`0049aca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049aca4.md) [`0049acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049acb4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004986f8",
      "incomplete_value": false,
      "site": "004986f8",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475860",
      "incomplete_value": false,
      "site": "00475860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "004986f8",
      "DATA",
      [
        "storage",
        "00be9158",
        null,
        "undefined *"
      ]
    ],
    [
      "00498730",
      "READ",
      [
        "storage",
        "00be9178",
        null,
        "pointer"
      ]
    ],
    [
      "00498730",
      "READ",
      [
        "storage",
        "00be9180",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004986f8",
      "DATA",
      [
        "storage",
        "00c65d18",
        null,
        "undefined *"
      ]
    ],
    [
      "00498730",
      "READ",
      [
        "storage",
        "00c65d38",
        null,
        "pointer"
      ]
    ],
    [
      "00498730",
      "READ",
      [
        "storage",
        "00c65d40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00475840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/0047580c.md#insn-00475840) · [`0047584c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/0047580c.md#insn-0047584c) · [`00475854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/0047580c.md#insn-00475854)
- 新版 [`004986d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md#insn-004986d8) · [`004986e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md#insn-004986e4) · [`004986ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md#insn-004986ec)

~~~diff
- 00475840 ["INT_ADD", "register:40f0:8", ["const:475840:8", "const:4:8"]]
- 00475840 ["CALL", null, ["callee:00c538b0:8"]]
+ 004986d8 ["INT_ADD", "register:40f0:8", ["const:4986d8:8", "const:4:8"]]
+ 004986d8 ["CALL", null, ["callee:00c538b0:8"]]
- 00475840 bytes 88851d94
+ 004986d8 bytes 76ec1e94
- 0047584c ["INT_ADD", "register:40f0:8", ["const:47584c:8", "const:4:8"]]
- 0047584c ["CALL", null, ["callee:00c538b0:8"]]
+ 004986e4 ["INT_ADD", "register:40f0:8", ["const:4986e4:8", "const:4:8"]]
+ 004986e4 ["CALL", null, ["callee:00c538b0:8"]]
- 0047584c bytes 85851d94
+ 004986e4 bytes 73ec1e94
- 00475854 ["COPY", "register:4040:8", ["const:be9000:8"]]
+ 004986ec ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00475854 bytes a83b0090
+ 004986ec bytes 683e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-434be37902c2144e14f8e25d6ae6bd56"></a>

### [`00475e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475e24.md) → [`00498cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md) FUN_00498cbc

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00474f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474f1c.md) · 呼出先 15件 [`004763f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/004763f8.md) [`00476598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476598.md) [`00476868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476868.md) [`0047686c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/0047686c.md) [`00574778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574778.md)
- 新版 呼出元 1件 [`00497db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497db4.md) · 呼出先 15件 [`00499290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499290.md) [`00499430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md) [`00499700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499700.md) [`00499704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499704.md) [`00597610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597610.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00498f24",
      "incomplete_value": false,
      "site": "00498f24",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047608c",
      "incomplete_value": false,
      "site": "0047608c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00498d10",
      "incomplete_value": false,
      "site": "00498d14",
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
            "const:6bf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475e78",
      "incomplete_value": false,
      "site": "00475e7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:33a:8"
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
      "definition_site": "00498fc4",
      "incomplete_value": false,
      "site": "00498fc8",
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
            "const:16:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047612c",
      "incomplete_value": false,
      "site": "00476130",
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
            "const:4a7:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00498d10",
      "PARAM",
      [
        "storage",
        "0029e33a",
        null,
        "string"
      ]
    ],
    [
      "00498f08",
      "PARAM",
      [
        "storage",
        "002a9384",
        null,
        "string"
      ]
    ],
    [
      "00498f24",
      "DATA",
      [
        "storage",
        "00be90d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00498d10",
      "PARAM",
      [
        "storage",
        "002ae6bf",
        null,
        "string"
      ]
    ],
    [
      "00498f08",
      "PARAM",
      [
        "storage",
        "002ba027",
        null,
        "string"
      ]
    ],
    [
      "00498f24",
      "DATA",
      [
        "storage",
        "00c65c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00475e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475e24.md#insn-00475e7c) · [`00476130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475e24.md#insn-00476130) · [`004761e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475e24.md#insn-004761e4)
- 新版 [`00498d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md#insn-00498d14) · [`00498fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md#insn-00498fc8) · [`0049907c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md#insn-0049907c)

~~~diff
- 00475e7c ["INT_ADD", "register:40f0:8", ["const:475e7c:8", "const:4:8"]]
- 00475e7c ["CALL", null, ["callee:00c58070:8"]]
+ 00498d14 ["INT_ADD", "register:40f0:8", ["const:498d14:8", "const:4:8"]]
+ 00498d14 ["CALL", null, ["callee:00c58070:8"]]
- 00475e7c bytes e9951d94
+ 00498d14 bytes d7fc1e94
- 00476130 ["INT_ADD", "register:40f0:8", ["const:476130:8", "const:4:8"]]
- 00476130 ["CALL", null, ["callee:00c58070:8"]]
+ 00498fc8 ["INT_ADD", "register:40f0:8", ["const:498fc8:8", "const:4:8"]]
+ 00498fc8 ["CALL", null, ["callee:00c58070:8"]]
- 00476130 bytes 3c951d94
+ 00498fc8 bytes 2afc1e94
- 004761e4 ["INT_ADD", "register:40f0:8", ["const:4761e4:8", "const:4:8"]]
- 004761e4 ["CALL", null, ["ram:bdb300:8"]]
+ 0049907c ["INT_ADD", "register:40f0:8", ["const:49907c:8", "const:4:8"]]
+ 0049907c ["CALL", null, ["ram:c57d50:8"]]
- 004761e4 bytes 47941d94
+ 0049907c bytes 35fb1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4641c4feb5f7536bf39904ceba0e2b16"></a>

### [`00476704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476704.md) → [`0049959c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049959c.md) FUN_0049959c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "004995c0",
      "incomplete_value": false,
      "site": "004995c4",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476728",
      "incomplete_value": false,
      "site": "0047672c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "004995c4",
      "DATA",
      [
        "storage",
        "00be9058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004995c4",
      "DATA",
      [
        "storage",
        "00c65c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00476718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476704.md#insn-00476718) · [`00476724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476704.md#insn-00476724) · [`00476728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476704.md#insn-00476728)
- 新版 [`004995b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049959c.md#insn-004995b0) · [`004995bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049959c.md#insn-004995bc) · [`004995c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049959c.md#insn-004995c0)

~~~diff
- 00476718 ["INT_ADD", "register:40f0:8", ["const:476718:8", "const:4:8"]]
- 00476718 ["CALL", null, ["callee:00c57a90:8"]]
+ 004995b0 ["INT_ADD", "register:40f0:8", ["const:4995b0:8", "const:4:8"]]
+ 004995b0 ["CALL", null, ["callee:00c57a90:8"]]
- 00476718 bytes 4a921d94
+ 004995b0 bytes 38f91e94
- 00476724 ["COPY", "register:4040:8", ["const:be9000:8"]]
+ 004995bc ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00476724 bytes 883b00f0
+ 004995bc bytes 683e0090
- 00476728 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00476728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00476728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00476728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004995c0 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 004995c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004995c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004995c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00476728 bytes 08610191
+ 004995c0 bytes 08613091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca32b738c11e5f310f008a6a01fce1a4"></a>

### [`00476744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476744.md) → [`004995dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004995dc.md) FUN_004995dc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004995e0",
      "incomplete_value": false,
      "site": "004995e4",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476748",
      "incomplete_value": false,
      "site": "0047674c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "004995e4",
      "DATA",
      [
        "storage",
        "00be9058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004995e4",
      "DATA",
      [
        "storage",
        "00c65c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00476744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476744.md#insn-00476744) · [`00476748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476744.md#insn-00476748)
- 新版 [`004995dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004995dc.md#insn-004995dc) · [`004995e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004995dc.md#insn-004995e0)

~~~diff
- 00476744 ["COPY", "register:4040:8", ["const:be9000:8"]]
+ 004995dc ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00476744 bytes 883b00f0
+ 004995dc bytes 683e0090
- 00476748 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00476748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00476748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00476748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004995e0 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 004995e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004995e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004995e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00476748 bytes 08610191
+ 004995e0 bytes 08613091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b33b111b7d234af9c42768a1e770cc56"></a>

### [`00476818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476818.md) → [`004996b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996b0.md) FUN_004996b0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "004996d0",
      "incomplete_value": false,
      "site": "004996d4",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476838",
      "incomplete_value": false,
      "site": "0047683c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "004996d4",
      "DATA",
      [
        "storage",
        "00be90d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004996d4",
      "DATA",
      [
        "storage",
        "00c65c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047682c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476818.md#insn-0047682c) · [`00476834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476818.md#insn-00476834) · [`00476838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476818.md#insn-00476838)
- 新版 [`004996c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996b0.md#insn-004996c4) · [`004996cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996b0.md#insn-004996cc) · [`004996d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996b0.md#insn-004996d0)

~~~diff
- 0047682c ["INT_ADD", "register:40f0:8", ["const:47682c:8", "const:4:8"]]
- 0047682c ["CALL", null, ["callee:00c57a90:8"]]
+ 004996c4 ["INT_ADD", "register:40f0:8", ["const:4996c4:8", "const:4:8"]]
+ 004996c4 ["CALL", null, ["callee:00c57a90:8"]]
- 0047682c bytes 05921d94
+ 004996c4 bytes f3f81e94
- 00476834 ["COPY", "register:4040:8", ["const:be9000:8"]]
+ 004996cc ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00476834 bytes 883b00f0
+ 004996cc bytes 683e0090
- 00476838 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 00476838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00476838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00476838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004996d0 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 004996d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004996d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004996d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00476838 bytes 08610391
+ 004996d0 bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d1b4aee61e516d29a5e7aa999185e59"></a>

### [`00476850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476850.md) → [`004996e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996e8.md) FUN_004996e8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004996ec",
      "incomplete_value": false,
      "site": "004996f0",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476854",
      "incomplete_value": false,
      "site": "00476858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "004996f0",
      "DATA",
      [
        "storage",
        "00be90d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004996f0",
      "DATA",
      [
        "storage",
        "00c65c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00476850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476850.md#insn-00476850) · [`00476854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00476/00476850.md#insn-00476854)
- 新版 [`004996e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996e8.md#insn-004996e8) · [`004996ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996e8.md#insn-004996ec)

~~~diff
- 00476850 ["COPY", "register:4040:8", ["const:be9000:8"]]
+ 004996e8 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00476850 bytes 883b00f0
+ 004996e8 bytes 683e0090
- 00476854 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 00476854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00476854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00476854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004996ec ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 004996ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004996ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004996ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00476854 bytes 08610391
+ 004996ec bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dc189d913efe048799bcf791d28b281"></a>

### [`00477d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477d2c.md) → [`0049abc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abc4.md) FUN_0049abc4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "0049abd0",
      "incomplete_value": false,
      "site": "0049abd4",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477d38",
      "incomplete_value": false,
      "site": "00477d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "0049abd4",
      "DATA",
      [
        "storage",
        "00be9158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049abd4",
      "DATA",
      [
        "storage",
        "00c65d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00477d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477d2c.md#insn-00477d34) · [`00477d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477d2c.md#insn-00477d38)
- 新版 [`0049abcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abc4.md#insn-0049abcc) · [`0049abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abc4.md#insn-0049abd0)

~~~diff
- 00477d34 ["COPY", "register:4048:8", ["const:be9000:8"]]
+ 0049abcc ["COPY", "register:4048:8", ["const:c65000:8"]]
- 00477d34 bytes 893b00d0
+ 0049abcc bytes 493e00f0
- 00477d38 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00477d38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00477d38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00477d38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0049abd0 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 0049abd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0049abd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0049abd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00477d38 bytes 29610591
+ 0049abd0 bytes 29613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6c9fdfc1f418e92dc4eb346dc2b8288"></a>

### [`00477d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477d4c.md) → [`0049abe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abe4.md) FUN_0049abe4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0049abec",
      "incomplete_value": false,
      "site": "0049abf0",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477d54",
      "incomplete_value": false,
      "site": "00477d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "0049abf0",
      "DATA",
      [
        "storage",
        "00be9158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049abf0",
      "DATA",
      [
        "storage",
        "00c65d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00477d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477d4c.md#insn-00477d50) · [`00477d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477d4c.md#insn-00477d54) · [`00477d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477d4c.md#insn-00477d74)
- 新版 [`0049abe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abe4.md#insn-0049abe8) · [`0049abec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abe4.md#insn-0049abec) · [`0049ac0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abe4.md#insn-0049ac0c)

~~~diff
- 00477d50 ["COPY", "register:4048:8", ["const:be9000:8"]]
+ 0049abe8 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 00477d50 bytes 893b00d0
+ 0049abe8 bytes 493e00f0
- 00477d54 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00477d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00477d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00477d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0049abec ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 0049abec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0049abec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0049abec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00477d54 bytes 29610591
+ 0049abec bytes 29613491
- 00477d74 ["INT_ADD", "register:40f0:8", ["const:477d74:8", "const:4:8"]]
- 00477d74 ["CALL", null, ["callee:00c57a80:8"]]
+ 0049ac0c ["INT_ADD", "register:40f0:8", ["const:49ac0c:8", "const:4:8"]]
+ 0049ac0c ["CALL", null, ["callee:00c57a80:8"]]
- 00477d74 bytes af8c1d94
+ 0049ac0c bytes 9df31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3aeca741dbb040f3d87cc2c94471de1b"></a>

### [`00477d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477d88.md) → [`0049ac20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac20.md) FUN_0049ac20

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
      "definition_site": "0049ac44",
      "incomplete_value": false,
      "site": "0049ac44",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477dac",
      "incomplete_value": false,
      "site": "00477dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
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
      "0049ac44",
      "DATA",
      [
        "storage",
        "00be9158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049ac44",
      "DATA",
      [
        "storage",
        "00c65d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00477d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477d88.md#insn-00477d9c) · [`00477da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477d88.md#insn-00477da4) · [`00477da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477d88.md#insn-00477da8)
- 新版 [`0049ac34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac20.md#insn-0049ac34) · [`0049ac3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac20.md#insn-0049ac3c) · [`0049ac40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac20.md#insn-0049ac40)

~~~diff
- 00477d9c ["INT_ADD", "register:40f0:8", ["const:477d9c:8", "const:4:8"]]
- 00477d9c ["CALL", null, ["callee:00c57a90:8"]]
+ 0049ac34 ["INT_ADD", "register:40f0:8", ["const:49ac34:8", "const:4:8"]]
+ 0049ac34 ["CALL", null, ["callee:00c57a90:8"]]
- 00477d9c bytes a98c1d94
+ 0049ac34 bytes 97f31e94
- 00477da4 ["COPY", "register:4048:8", ["const:be9000:8"]]
+ 0049ac3c ["COPY", "register:4048:8", ["const:c65000:8"]]
- 00477da4 bytes 893b00d0
+ 0049ac3c bytes 493e00f0
- 00477da8 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00477da8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00477da8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00477da8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0049ac40 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 0049ac40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0049ac40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0049ac40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00477da8 bytes 29610591
+ 0049ac40 bytes 29613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-131f9b91c797e3ba7a93fc26eed636d0"></a>

### [`00477dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477dd8.md) → [`0049ac70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac70.md) FUN_0049ac70

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
      "definition_site": "0049ac7c",
      "incomplete_value": false,
      "site": "0049ac7c",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477de4",
      "incomplete_value": false,
      "site": "00477de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "0049ac7c",
      "DATA",
      [
        "storage",
        "00be9158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049ac7c",
      "DATA",
      [
        "storage",
        "00c65d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00477ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477dd8.md#insn-00477ddc) · [`00477de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477dd8.md#insn-00477de0) · [`00477e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477dd8.md#insn-00477e00)
- 新版 [`0049ac74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac70.md#insn-0049ac74) · [`0049ac78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac70.md#insn-0049ac78) · [`0049ac98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac70.md#insn-0049ac98)

~~~diff
- 00477ddc ["COPY", "register:4048:8", ["const:be9000:8"]]
+ 0049ac74 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 00477ddc bytes 893b00d0
+ 0049ac74 bytes 493e00f0
- 00477de0 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00477de0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00477de0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00477de0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0049ac78 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 0049ac78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0049ac78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0049ac78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00477de0 bytes 29610591
+ 0049ac78 bytes 29613491
- 00477e00 ["INT_ADD", "register:40f0:8", ["const:477e00:8", "const:4:8"]]
- 00477e00 ["CALL", null, ["callee:00c538b0:8"]]
+ 0049ac98 ["INT_ADD", "register:40f0:8", ["const:49ac98:8", "const:4:8"]]
+ 0049ac98 ["CALL", null, ["callee:00c538b0:8"]]
- 00477e00 bytes 187c1d94
+ 0049ac98 bytes 06e31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e6949e7dbc4ef61aa5267e469345fa2"></a>

### [`00477f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477f54.md) → [`0049adec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049adec.md) _INIT_24

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
      "definition_site": "0049ae28",
      "incomplete_value": true,
      "site": "0049ae44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00477f90",
      "incomplete_value": true,
      "site": "00477fac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0049ae4c",
      "incomplete_value": true,
      "site": "0049ae68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00477fb4",
      "incomplete_value": true,
      "site": "00477fd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0049ae6c",
      "incomplete_value": true,
      "site": "0049ae88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00477fd4",
      "incomplete_value": true,
      "site": "00477ff0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0049ae28",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0049ae4c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0049ae6c",
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
      "0049ae28",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0049ae4c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0049ae6c",
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

- 旧版 [`004780b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477f54.md#insn-004780b4) · [`00478188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477f54.md#insn-00478188) · [`00477f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00477/00477f54.md#insn-00477f7c)
- 新版 [`0049af4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049adec.md#insn-0049af4c) · [`0049b020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049adec.md#insn-0049b020) · [`0049ae14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049adec.md#insn-0049ae14)

~~~diff
- 004780b4 ["INT_ADD", "register:40f0:8", ["const:4780b4:8", "const:4:8"]]
- 004780b4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0049af4c ["INT_ADD", "register:40f0:8", ["const:49af4c:8", "const:4:8"]]
+ 0049af4c ["CALL", null, ["callee:0043b7b8:8"]]
- 004780b4 bytes 0183fe97
+ 0049af4c bytes 1b82fe97
- 00478188 ["INT_ADD", "register:40f0:8", ["const:478188:8", "const:4:8"]]
- 00478188 ["CALL", null, ["callee:00c57a30:8"]]
+ 0049b020 ["INT_ADD", "register:40f0:8", ["const:49b020:8", "const:4:8"]]
+ 0049b020 ["CALL", null, ["callee:00c57a30:8"]]
- 00478188 bytes 968b1d94
+ 0049b020 bytes 84f21e94
- 00477f7c ["COPY", "register:4098:8", ["const:c25000:8"]]
+ 0049ae14 ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 00477f7c bytes 733d00d0
+ 0049ae14 bytes 534000d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f5697926f6a740c7c398a48d3843578"></a>

### [`004782e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004782e4.md) → [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) FUN_0049b17c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00423bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423bbc.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 1件 [`004466bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004466bc.md) · 呼出先 11件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049b1ec",
      "incomplete_value": true,
      "site": "0049b1f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00478354",
      "incomplete_value": true,
      "site": "00478360",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d20:8"
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
      "definition_site": "0049b1e8",
      "incomplete_value": true,
      "site": "0049b1fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f57:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478350",
      "incomplete_value": true,
      "site": "00478364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:933:8"
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
      "definition_site": "0049b1e8",
      "incomplete_value": true,
      "site": "0049b1fc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00478350",
      "incomplete_value": true,
      "site": "00478364",
      "value": [
        "LOAD",
        "16",
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
      "0049b1e8",
      "READ",
      [
        "storage",
        "002af933",
        null,
        "string"
      ]
    ],
    [
      "0049b1e8",
      "READ",
      [
        "storage",
        "002af943",
        null,
        "string"
      ]
    ],
    [
      "0049b1ec",
      "READ",
      [
        "storage",
        "002b0d20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0049b1e8",
      "READ",
      [
        "storage",
        "002c0f57",
        null,
        "string"
      ]
    ],
    [
      "0049b1e8",
      "READ",
      [
        "storage",
        "002c0f67",
        null,
        "string"
      ]
    ],
    [
      "0049b1ec",
      "READ",
      [
        "storage",
        "002c2320",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00478310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004782e4.md#insn-00478310) · [`00478318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004782e4.md#insn-00478318) · [`00478340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004782e4.md#insn-00478340)
- 新版 [`0049b1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md#insn-0049b1a8) · [`0049b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md#insn-0049b1b0) · [`0049b1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md#insn-0049b1d8)

~~~diff
- 00478310 ["INT_ADD", "register:40f0:8", ["const:478310:8", "const:4:8"]]
- 00478310 ["CALL", null, ["callee:00588e2c:8"]]
+ 0049b1a8 ["INT_ADD", "register:40f0:8", ["const:49b1a8:8", "const:4:8"]]
+ 0049b1a8 ["CALL", null, ["callee:00588e2c:8"]]
- 00478310 bytes 21b70394
+ 0049b1a8 bytes 21b70394
- 00478318 ["INT_ADD", "register:40f0:8", ["const:478318:8", "const:4:8"]]
- 00478318 ["CALL", null, ["callee:0058911c:8"]]
+ 0049b1b0 ["INT_ADD", "register:40f0:8", ["const:49b1b0:8", "const:4:8"]]
+ 0049b1b0 ["CALL", null, ["callee:0058911c:8"]]
- 00478318 bytes dbb70394
+ 0049b1b0 bytes dbb70394
- 00478340 ["INT_ADD", "register:40f0:8", ["const:478340:8", "const:4:8"]]
- 00478340 ["CALL", null, ["callee:00c57a90:8"]]
+ 0049b1d8 ["INT_ADD", "register:40f0:8", ["const:49b1d8:8", "const:4:8"]]
+ 0049b1d8 ["CALL", null, ["callee:00c57a90:8"]]
- 00478340 bytes 408b1d94
+ 0049b1d8 bytes 2ef21e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad56ca9a9edce23b48f75e788b27f3b4"></a>

### [`004785c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004785c8.md) → [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) FUN_0049b460

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004787b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004787b4.md) [`0047cc18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cc18.md) [`0047cd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cd90.md) [`0047cef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cef8.md) · 呼出先 4件 [`0045a6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a6dc.md) [`0045a7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7e0.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 4件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) [`0049fab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fab0.md) [`0049fc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fc28.md) [`0049fd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fd90.md) · 呼出先 4件 [`0047d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d574.md) [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049b554",
      "incomplete_value": false,
      "site": "0049b55c",
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
            "const:a11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004786bc",
      "incomplete_value": false,
      "site": "004786c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:c53:8"
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
      "definition_site": "0049b564",
      "incomplete_value": true,
      "site": "0049b568",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004786cc",
      "incomplete_value": true,
      "site": "004786d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "0049b55c",
      "DATA",
      [
        "storage",
        "00298c53",
        null,
        "string"
      ]
    ],
    [
      "0049b564",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "0049b564",
      "PARAM",
      [
        "storage",
        "00c16e98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049b55c",
      "DATA",
      [
        "storage",
        "002a8a11",
        null,
        "string"
      ]
    ],
    [
      "0049b564",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049b564",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004786d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004785c8.md#insn-004786d0) · [`0047865c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004785c8.md#insn-0047865c) · [`004786ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004785c8.md#insn-004786ac)
- 新版 [`0049b568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md#insn-0049b568) · [`0049b4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md#insn-0049b4f4) · [`0049b544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md#insn-0049b544)

~~~diff
- 004786d0 ["INT_ADD", "register:40f0:8", ["const:4786d0:8", "const:4:8"]]
- 004786d0 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049b568 ["INT_ADD", "register:40f0:8", ["const:49b568:8", "const:4:8"]]
+ 0049b568 ["CALL", null, ["callee:00c57b10:8"]]
- 004786d0 bytes 7c8a1d94
+ 0049b568 bytes 6af11e94
- 0047865c ["INT_ADD", "register:40f0:8", ["const:47865c:8", "const:4:8"]]
- 0047865c ["CALL", null, ["callee:0047d574:8"]]
+ 0049b4f4 ["INT_ADD", "register:40f0:8", ["const:49b4f4:8", "const:4:8"]]
+ 0049b4f4 ["CALL", null, ["callee:0047d574:8"]]
- 0047865c bytes 2088ff97
+ 0049b4f4 bytes 2088ff97
- 004786ac ["INT_ADD", "register:40f0:8", ["const:4786ac:8", "const:4:8"]]
- 004786ac ["CALL", null, ["callee:0047d678:8"]]
+ 0049b544 ["INT_ADD", "register:40f0:8", ["const:49b544:8", "const:4:8"]]
+ 0049b544 ["CALL", null, ["callee:0047d678:8"]]
- 004786ac bytes 4d88ff97
+ 0049b544 bytes 4d88ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caf714265489e0f939e9de954eef9d78"></a>

### [`004787b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004787b4.md) → [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) FUN_0049b64c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004786d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004786d4.md) · 呼出先 15件 [`004784f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004784f0.md) [`004784fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004784fc.md) [`004785c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004785c8.md) [`00478d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d84.md) [`0047bdcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bdcc.md)
- 新版 呼出元 1件 [`0049b56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b56c.md) · 呼出先 15件 [`0049b388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b388.md) [`0049b394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b394.md) [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) [`0049ec64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ec64.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.22% / 新版 95.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049bb04",
      "incomplete_value": false,
      "site": "0049bb08",
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
            "const:a24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478c6c",
      "incomplete_value": false,
      "site": "00478c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:c66:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049bac8",
      "incomplete_value": true,
      "site": "0049bacc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478c30",
      "incomplete_value": true,
      "site": "00478c34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "definition_site": "0049bb28",
      "incomplete_value": true,
      "site": "0049bb2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478c90",
      "incomplete_value": true,
      "site": "00478c94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "0049b83c",
      "DATA",
      [
        "storage",
        "002b8f8d",
        null,
        null
      ]
    ],
    [
      "0049b840",
      "DATA",
      [
        "storage",
        "002b8ee9",
        null,
        null
      ]
    ],
    [
      "0049b848",
      "DATA",
      [
        "storage",
        "002b8f12",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0049b83c",
      "DATA",
      [
        "storage",
        "002ca69d",
        null,
        null
      ]
    ],
    [
      "0049b840",
      "DATA",
      [
        "storage",
        "002ca5f9",
        null,
        null
      ]
    ],
    [
      "0049b848",
      "DATA",
      [
        "storage",
        "002ca622",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00478c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004787b4.md#insn-00478c34) · [`00478c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004787b4.md#insn-00478c94) · [`00478830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004787b4.md#insn-00478830)
- 新版 [`0049bacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md#insn-0049bacc) · [`0049bb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md#insn-0049bb2c) · [`0049b6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md#insn-0049b6c8)

~~~diff
- 00478c34 ["INT_ADD", "register:40f0:8", ["const:478c34:8", "const:4:8"]]
- 00478c34 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049bacc ["INT_ADD", "register:40f0:8", ["const:49bacc:8", "const:4:8"]]
+ 0049bacc ["CALL", null, ["callee:00c57b10:8"]]
- 00478c34 bytes 23891d94
+ 0049bacc bytes 11f01e94
- 00478c94 ["INT_ADD", "register:40f0:8", ["const:478c94:8", "const:4:8"]]
- 00478c94 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049bb2c ["INT_ADD", "register:40f0:8", ["const:49bb2c:8", "const:4:8"]]
+ 0049bb2c ["CALL", null, ["callee:00c57b10:8"]]
- 00478c94 bytes 0b891d94
+ 0049bb2c bytes f9ef1e94
- 00478830 ["COPY", "register:4058:8", ["const:2b8000:8"]]
+ 0049b6c8 ["COPY", "register:4058:8", ["const:2ca000:8"]]
- 00478830 bytes 0bf2ff90
+ 0049b6c8 bytes 6bf1fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca0c1a3c1f8f1a0a04b755ca8e350b61"></a>

### [`00478d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d84.md) → [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) FUN_0049bc1c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004787b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004787b4.md) · 呼出先 15件 [`0045a7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7e0.md) [`0047914c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/0047914c.md) [`004794a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/004794a0.md) [`00479c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479c04.md) [`00479f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479f48.md)
- 新版 呼出元 1件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) · 呼出先 15件 [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) [`0049ca9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md) [`0049cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.62% / 新版 98.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049bef0",
      "incomplete_value": false,
      "site": "0049bef4",
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
            "const:a11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479058",
      "incomplete_value": false,
      "site": "0047905c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:c53:8"
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
      "definition_site": "0049bf14",
      "incomplete_value": true,
      "site": "0049bf18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047907c",
      "incomplete_value": true,
      "site": "00479080",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "0049bef4",
      "DATA",
      [
        "storage",
        "00298c53",
        null,
        "string"
      ]
    ],
    [
      "0049bf14",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "0049bf14",
      "PARAM",
      [
        "storage",
        "00c16e98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049bef4",
      "DATA",
      [
        "storage",
        "002a8a11",
        null,
        "string"
      ]
    ],
    [
      "0049bf14",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049bf14",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d84.md#insn-00479080) · [`00478e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d84.md#insn-00478e04) · [`00478e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d84.md#insn-00478e3c)
- 新版 [`0049bf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md#insn-0049bf18) · [`0049bc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md#insn-0049bc9c) · [`0049bcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md#insn-0049bcd4)

~~~diff
- 00479080 ["INT_ADD", "register:40f0:8", ["const:479080:8", "const:4:8"]]
- 00479080 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049bf18 ["INT_ADD", "register:40f0:8", ["const:49bf18:8", "const:4:8"]]
+ 0049bf18 ["CALL", null, ["callee:00c57b10:8"]]
- 00479080 bytes 10881d94
+ 0049bf18 bytes feee1e94
- 00478e04 ["INT_ADD", "register:40f0:8", ["const:478e04:8", "const:4:8"]]
- 00478e04 ["CALL", null, ["callee:00c57a90:8"]]
+ 0049bc9c ["INT_ADD", "register:40f0:8", ["const:49bc9c:8", "const:4:8"]]
+ 0049bc9c ["CALL", null, ["callee:00c57a90:8"]]
- 00478e04 bytes 8f881d94
+ 0049bc9c bytes 7def1e94
- 00478e3c ["INT_ADD", "register:40f0:8", ["const:478e3c:8", "const:4:8"]]
- 00478e3c ["CALL", null, ["callee:00c57c90:8"]]
+ 0049bcd4 ["INT_ADD", "register:40f0:8", ["const:49bcd4:8", "const:4:8"]]
+ 0049bcd4 ["CALL", null, ["callee:00c57c90:8"]]
- 00478e3c bytes 01891d94
+ 0049bcd4 bytes efef1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-619cd66accb1d066a87bb452cee10859"></a>

### [`004794a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/004794a0.md) → [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) FUN_0049c338

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00478d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d84.md) · 呼出先 14件 [`0047ab48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047ab48.md) [`0047ba2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047ba2c.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`0047c568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c568.md) [`0047c854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c854.md)
- 新版 呼出元 1件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) · 呼出先 14件 [`0049d9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md) [`0049e8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0049f400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f400.md) [`0049f6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f6ec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.96% / 新版 96.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049c9b4",
      "incomplete_value": false,
      "site": "0049c9b8",
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
            "const:a24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479b1c",
      "incomplete_value": false,
      "site": "00479b20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:c66:8"
          ]
        ]
      ]
    },
    "ordinal": 62,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049c9a0",
      "incomplete_value": true,
      "site": "0049c9a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479b08",
      "incomplete_value": true,
      "site": "00479b0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "definition_site": "0049c9d8",
      "incomplete_value": true,
      "site": "0049c9dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479b40",
      "incomplete_value": true,
      "site": "00479b44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "0049c994",
      "DATA",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "0049c994",
      "DATA",
      [
        "storage",
        "002a227c",
        null,
        "string"
      ]
    ],
    [
      "0049c9a0",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049c994",
      "DATA",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      "0049c994",
      "DATA",
      [
        "storage",
        "002b293d",
        null,
        "string"
      ]
    ],
    [
      "0049c9a0",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/004794a0.md#insn-00479b0c) · [`00479b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/004794a0.md#insn-00479b44) · [`0047955c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/004794a0.md#insn-0047955c)
- 新版 [`0049c9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md#insn-0049c9a4) · [`0049c9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md#insn-0049c9dc) · [`0049c3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md#insn-0049c3f4)

~~~diff
- 00479b0c ["INT_ADD", "register:40f0:8", ["const:479b0c:8", "const:4:8"]]
- 00479b0c ["CALL", null, ["callee:00c57b10:8"]]
+ 0049c9a4 ["INT_ADD", "register:40f0:8", ["const:49c9a4:8", "const:4:8"]]
+ 0049c9a4 ["CALL", null, ["callee:00c57b10:8"]]
- 00479b0c bytes 6d851d94
+ 0049c9a4 bytes 5bec1e94
- 00479b44 ["INT_ADD", "register:40f0:8", ["const:479b44:8", "const:4:8"]]
- 00479b44 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049c9dc ["INT_ADD", "register:40f0:8", ["const:49c9dc:8", "const:4:8"]]
+ 0049c9dc ["CALL", null, ["callee:00c57b10:8"]]
- 00479b44 bytes 5f851d94
+ 0049c9dc bytes 4dec1e94
- 0047955c ["COPY", "register:4078:8", ["const:2b8000:8"]]
+ 0049c3f4 ["COPY", "register:4078:8", ["const:2ca000:8"]]
- 0047955c bytes eff1fff0
+ 0049c3f4 bytes 6ff1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6413594fc18ca30d978900103b998be"></a>

### [`00479c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479c04.md) → [`0049ca9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md) FUN_0049ca9c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00478d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d84.md) · 呼出先 5件 [`0047c52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c52c.md) [`0047c540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c540.md) [`0047ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047ca08.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) · 呼出先 5件 [`0049f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md) [`0049f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md) [`0049f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8a0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.09% / 新版 98.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049cdd8",
      "incomplete_value": true,
      "site": "0049cddc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479f40",
      "incomplete_value": true,
      "site": "00479f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "0049cdcc",
      "DATA",
      [
        "storage",
        "002a227c",
        null,
        "string"
      ]
    ],
    [
      "0049cdcc",
      "DATA",
      [
        "storage",
        "00298c66",
        null,
        "string"
      ]
    ],
    [
      "0049cdcc",
      "DATA",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049cdcc",
      "DATA",
      [
        "storage",
        "002b293d",
        null,
        "string"
      ]
    ],
    [
      "0049cdcc",
      "DATA",
      [
        "storage",
        "002a8a24",
        null,
        "string"
      ]
    ],
    [
      "0049cdcc",
      "DATA",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479c04.md#insn-00479f44) · [`00479ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479c04.md#insn-00479ea8) · [`00479ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479c04.md#insn-00479ee8)
- 新版 [`0049cddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md#insn-0049cddc) · [`0049cd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md#insn-0049cd40) · [`0049cd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md#insn-0049cd80)

~~~diff
- 00479f44 ["INT_ADD", "register:40f0:8", ["const:479f44:8", "const:4:8"]]
- 00479f44 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049cddc ["INT_ADD", "register:40f0:8", ["const:49cddc:8", "const:4:8"]]
+ 0049cddc ["CALL", null, ["callee:00c57b10:8"]]
- 00479f44 bytes 5f841d94
+ 0049cddc bytes 4deb1e94
- 00479ea8 ["INT_ADD", "register:40f0:8", ["const:479ea8:8", "const:4:8"]]
- 00479ea8 ["CALL", null, ["callee:0049f3d8:8"]]
+ 0049cd40 ["INT_ADD", "register:40f0:8", ["const:49cd40:8", "const:4:8"]]
+ 0049cd40 ["CALL", null, ["callee:0049f3d8:8"]]
- 00479ea8 bytes a6090094
+ 0049cd40 bytes a6090094
- 00479ee8 ["INT_ADD", "register:40f0:8", ["const:479ee8:8", "const:4:8"]]
- 00479ee8 ["CALL", null, ["callee:0049f3c4:8"]]
+ 0049cd80 ["INT_ADD", "register:40f0:8", ["const:49cd80:8", "const:4:8"]]
+ 0049cd80 ["CALL", null, ["callee:0049f3c4:8"]]
- 00479ee8 bytes 91090094
+ 0049cd80 bytes 91090094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8cfb250dac0e2944bf1d7691db08ebf"></a>

### [`00479f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479f48.md) → [`0049cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md) FUN_0049cde0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00478d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d84.md) · 呼出先 5件 [`0047a5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a5ec.md) [`0047adfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047adfc.md) [`0047b068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b068.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) · 呼出先 5件 [`0049d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md) [`0049dc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md) [`0049df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.05% / 新版 98.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049d030",
      "incomplete_value": false,
      "site": "0049d038",
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
            "const:a24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a198",
      "incomplete_value": false,
      "site": "0047a1a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:c66:8"
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
      "definition_site": "0049d040",
      "incomplete_value": true,
      "site": "0049d044",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a1a8",
      "incomplete_value": true,
      "site": "0047a1ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049d038",
      "DATA",
      [
        "storage",
        "00298c66",
        null,
        "string"
      ]
    ],
    [
      "0049d040",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "0049d040",
      "PARAM",
      [
        "storage",
        "00c16e98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049d038",
      "DATA",
      [
        "storage",
        "002a8a24",
        null,
        "string"
      ]
    ],
    [
      "0049d040",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049d040",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479f48.md#insn-0047a1ac) · [`00479f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479f48.md#insn-00479f7c) · [`00479f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479f48.md#insn-00479f88)
- 新版 [`0049d044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md#insn-0049d044) · [`0049ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md#insn-0049ce14) · [`0049ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md#insn-0049ce20)

~~~diff
- 0047a1ac ["INT_ADD", "register:40f0:8", ["const:47a1ac:8", "const:4:8"]]
- 0047a1ac ["CALL", null, ["callee:00c57b10:8"]]
+ 0049d044 ["INT_ADD", "register:40f0:8", ["const:49d044:8", "const:4:8"]]
+ 0049d044 ["CALL", null, ["callee:00c57b10:8"]]
- 0047a1ac bytes c5831d94
+ 0049d044 bytes b3ea1e94
- 00479f7c ["INT_ADD", "register:40f0:8", ["const:479f7c:8", "const:4:8"]]
- 00479f7c ["CALL", null, ["callee:0049d484:8"]]
+ 0049ce14 ["INT_ADD", "register:40f0:8", ["const:49ce14:8", "const:4:8"]]
+ 0049ce14 ["CALL", null, ["callee:0049d484:8"]]
- 00479f7c bytes 9c010094
+ 0049ce14 bytes 9c010094
- 00479f88 ["INT_ADD", "register:40f0:8", ["const:479f88:8", "const:4:8"]]
- 00479f88 ["CALL", null, ["callee:0049dc94:8"]]
+ 0049ce20 ["INT_ADD", "register:40f0:8", ["const:49ce20:8", "const:4:8"]]
+ 0049ce20 ["CALL", null, ["callee:0049dc94:8"]]
- 00479f88 bytes 9d030094
+ 0049ce20 bytes 9d030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0862e4bf5f961b68c1956dab9a099b91"></a>

### [`0047a39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a39c.md) → [`0049d234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md) FUN_0049d234

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047914c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/0047914c.md) · 呼出先 5件 [`0047b5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b5ec.md) [`0047b7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b7fc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) · 呼出先 5件 [`0049e484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e484.md) [`0049e694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e694.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049d36c",
      "incomplete_value": false,
      "site": "0049d374",
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
            "const:93d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a4d4",
      "incomplete_value": false,
      "site": "0047a4dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:27c:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049d37c",
      "incomplete_value": true,
      "site": "0049d380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a4e4",
      "incomplete_value": true,
      "site": "0047a4e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "0049d374",
      "DATA",
      [
        "storage",
        "002a227c",
        null,
        "string"
      ]
    ],
    [
      "0049d37c",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "0049d37c",
      "PARAM",
      [
        "storage",
        "00c16e98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049d374",
      "DATA",
      [
        "storage",
        "002b293d",
        null,
        "string"
      ]
    ],
    [
      "0049d37c",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049d37c",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a39c.md#insn-0047a4e8) · [`0047a464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a39c.md#insn-0047a464) · [`0047a490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a39c.md#insn-0047a490)
- 新版 [`0049d380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md#insn-0049d380) · [`0049d2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md#insn-0049d2fc) · [`0049d328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md#insn-0049d328)

~~~diff
- 0047a4e8 ["INT_ADD", "register:40f0:8", ["const:47a4e8:8", "const:4:8"]]
- 0047a4e8 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049d380 ["INT_ADD", "register:40f0:8", ["const:49d380:8", "const:4:8"]]
+ 0049d380 ["CALL", null, ["callee:00c57b10:8"]]
- 0047a4e8 bytes f6821d94
+ 0049d380 bytes e4e91e94
- 0047a464 ["INT_ADD", "register:40f0:8", ["const:47a464:8", "const:4:8"]]
- 0047a464 ["CALL", null, ["callee:0049e484:8"]]
+ 0049d2fc ["INT_ADD", "register:40f0:8", ["const:49d2fc:8", "const:4:8"]]
+ 0049d2fc ["CALL", null, ["callee:0049e484:8"]]
- 0047a464 bytes 62040094
+ 0049d2fc bytes 62040094
- 0047a490 ["INT_ADD", "register:40f0:8", ["const:47a490:8", "const:4:8"]]
- 0047a490 ["CALL", null, ["callee:0049e694:8"]]
+ 0049d328 ["INT_ADD", "register:40f0:8", ["const:49d328:8", "const:4:8"]]
+ 0049d328 ["CALL", null, ["callee:0049e694:8"]]
- 0047a490 bytes db040094
+ 0049d328 bytes db040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52701d9be591114618e8270fd06f5671"></a>

### [`0047a5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a5ec.md) → [`0049d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md) FUN_0049d484

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0047914c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/0047914c.md) [`00479f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479f48.md) · 呼出先 3件 [`0047a2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a2c0.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 2件 [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) [`0049cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md) · 呼出先 3件 [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049d860",
      "incomplete_value": false,
      "site": "0049d868",
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
            "const:a24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a9c8",
      "incomplete_value": false,
      "site": "0047a9d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:c66:8"
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
      "definition_site": "0049d870",
      "incomplete_value": true,
      "site": "0049d874",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a9d8",
      "incomplete_value": true,
      "site": "0047a9dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "0049d4c0",
      "DATA",
      [
        "storage",
        "002b16c0",
        null,
        null
      ]
    ],
    [
      "0049d868",
      "DATA",
      [
        "storage",
        "00298c66",
        null,
        "string"
      ]
    ],
    [
      "0049d870",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049d4c0",
      "DATA",
      [
        "storage",
        "002c2d20",
        null,
        null
      ]
    ],
    [
      "0049d868",
      "DATA",
      [
        "storage",
        "002a8a24",
        null,
        "string"
      ]
    ],
    [
      "0049d870",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a5ec.md#insn-0047a9dc) · [`0047a61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a5ec.md#insn-0047a61c) · [`0047a620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a5ec.md#insn-0047a620)
- 新版 [`0049d874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md#insn-0049d874) · [`0049d4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md#insn-0049d4b4) · [`0049d4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md#insn-0049d4b8)

~~~diff
- 0047a9dc ["INT_ADD", "register:40f0:8", ["const:47a9dc:8", "const:4:8"]]
- 0047a9dc ["CALL", null, ["callee:00c57b10:8"]]
+ 0049d874 ["INT_ADD", "register:40f0:8", ["const:49d874:8", "const:4:8"]]
+ 0049d874 ["CALL", null, ["callee:00c57b10:8"]]
- 0047a9dc bytes b9811d94
+ 0049d874 bytes a7e81e94
- 0047a61c ["COPY", "register:4050:8", ["const:2b1000:8"]]
+ 0049d4b4 ["COPY", "register:4050:8", ["const:2c2000:8"]]
- 0047a61c bytes aaf1fff0
+ 0049d4b4 bytes 2af1ffb0
- 0047a620 ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 0047a620 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0047a620 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0047a620 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0049d4b8 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 0049d4b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0049d4b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0049d4b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0047a620 bytes 4a011b91
+ 0049d4b8 bytes 4a813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-923a3fc22ef2703ca044db3e71220f1e"></a>

### [`0047a9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a9e0.md) → [`0049d878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d878.md) FUN_0049d878

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047914c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/0047914c.md) · 呼出先 3件 [`0047a2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a2c0.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) · 呼出先 3件 [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049d9c8",
      "incomplete_value": false,
      "site": "0049d9d0",
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
            "const:a24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ab30",
      "incomplete_value": false,
      "site": "0047ab38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:c66:8"
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
      "definition_site": "0049d9d8",
      "incomplete_value": true,
      "site": "0049d9dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ab40",
      "incomplete_value": true,
      "site": "0047ab44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "0049d9d0",
      "DATA",
      [
        "storage",
        "00298c66",
        null,
        "string"
      ]
    ],
    [
      "0049d9d8",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "0049d9d8",
      "PARAM",
      [
        "storage",
        "00c16e98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049d9d0",
      "DATA",
      [
        "storage",
        "002a8a24",
        null,
        "string"
      ]
    ],
    [
      "0049d9d8",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049d9d8",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047ab44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a9e0.md#insn-0047ab44) · [`0047aae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a9e0.md#insn-0047aae8) · [`0047aafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a9e0.md#insn-0047aafc)
- 新版 [`0049d9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d878.md#insn-0049d9dc) · [`0049d980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d878.md#insn-0049d980) · [`0049d994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d878.md#insn-0049d994)

~~~diff
- 0047ab44 ["INT_ADD", "register:40f0:8", ["const:47ab44:8", "const:4:8"]]
- 0047ab44 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049d9dc ["INT_ADD", "register:40f0:8", ["const:49d9dc:8", "const:4:8"]]
+ 0049d9dc ["CALL", null, ["callee:00c57b10:8"]]
- 0047ab44 bytes 5f811d94
+ 0049d9dc bytes 4de81e94
- 0047aae8 ["INT_ADD", "register:40f0:8", ["const:47aae8:8", "const:4:8"]]
- 0047aae8 ["CALL", null, ["callee:0049d158:8"]]
+ 0049d980 ["INT_ADD", "register:40f0:8", ["const:49d980:8", "const:4:8"]]
+ 0049d980 ["CALL", null, ["callee:0049d158:8"]]
- 0047aae8 bytes f6fdff97
+ 0049d980 bytes f6fdff97
- 0047aafc ["INT_ADD", "register:40f0:8", ["const:47aafc:8", "const:4:8"]]
- 0047aafc ["CALL", null, ["callee:0049d158:8"]]
+ 0049d994 ["INT_ADD", "register:40f0:8", ["const:49d994:8", "const:4:8"]]
+ 0049d994 ["CALL", null, ["callee:0049d158:8"]]
- 0047aafc bytes f1fdff97
+ 0049d994 bytes f1fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2508a5a4020833401ffda113d145fc72"></a>

### [`0047adfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047adfc.md) → [`0049dc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md) FUN_0049dc94

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00479f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479f48.md) · 呼出先 4件 [`0047c52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c52c.md) [`0047c540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c540.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`0049cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md) · 呼出先 4件 [`0049f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md) [`0049f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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
      "definition_site": "0049dee8",
      "incomplete_value": false,
      "site": "0049def0",
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
            "const:991:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047b050",
      "incomplete_value": false,
      "site": "0047b058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
      "definition_site": "0049def8",
      "incomplete_value": true,
      "site": "0049defc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047b060",
      "incomplete_value": true,
      "site": "0047b064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "0049def0",
      "DATA",
      [
        "storage",
        "00299ab8",
        null,
        "string"
      ]
    ],
    [
      "0049def8",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "0049def8",
      "PARAM",
      [
        "storage",
        "00c16e98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049def0",
      "DATA",
      [
        "storage",
        "002a9991",
        null,
        "string"
      ]
    ],
    [
      "0049def8",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049def8",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047adfc.md#insn-0047b064) · [`0047b028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047adfc.md#insn-0047b028) · [`0047b030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047adfc.md#insn-0047b030)
- 新版 [`0049defc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md#insn-0049defc) · [`0049dec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md#insn-0049dec0) · [`0049dec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md#insn-0049dec8)

~~~diff
- 0047b064 ["INT_ADD", "register:40f0:8", ["const:47b064:8", "const:4:8"]]
- 0047b064 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049defc ["INT_ADD", "register:40f0:8", ["const:49defc:8", "const:4:8"]]
+ 0049defc ["CALL", null, ["callee:00c57b10:8"]]
- 0047b064 bytes 17801d94
+ 0049defc bytes 05e71e94
- 0047b028 ["INT_ADD", "register:40f0:8", ["const:47b028:8", "const:4:8"]]
- 0047b028 ["CALL", null, ["callee:0049f3c4:8"]]
+ 0049dec0 ["INT_ADD", "register:40f0:8", ["const:49dec0:8", "const:4:8"]]
+ 0049dec0 ["CALL", null, ["callee:0049f3c4:8"]]
- 0047b028 bytes 41050094
+ 0049dec0 bytes 41050094
- 0047b030 ["INT_ADD", "register:40f0:8", ["const:47b030:8", "const:4:8"]]
- 0047b030 ["CALL", null, ["callee:0049f3d8:8"]]
+ 0049dec8 ["INT_ADD", "register:40f0:8", ["const:49dec8:8", "const:4:8"]]
+ 0049dec8 ["CALL", null, ["callee:0049f3d8:8"]]
- 0047b030 bytes 44050094
+ 0049dec8 bytes 44050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43a6f3e30b248b96fd128007c74dfd44"></a>

### [`0047ba2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047ba2c.md) → [`0049e8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md) FUN_0049e8c4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004794a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/004794a0.md) · 呼出先 8件 [`0047bbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bbd4.md) [`0047ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047ca08.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) · 呼出先 8件 [`0049ea6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ea6c.md) [`0049f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8a0.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049e9fc",
      "incomplete_value": false,
      "site": "0049ea00",
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
            "const:a24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047bb64",
      "incomplete_value": false,
      "site": "0047bb68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:c66:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049ea20",
      "incomplete_value": false,
      "site": "0049ea24",
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
            "const:a34:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047bb88",
      "incomplete_value": false,
      "site": "0047bb8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:c76:8"
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
      "definition_site": "0049ea0c",
      "incomplete_value": true,
      "site": "0049ea10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047bb74",
      "incomplete_value": true,
      "site": "0047bb78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "0049ea00",
      "DATA",
      [
        "storage",
        "00298c66",
        null,
        "string"
      ]
    ],
    [
      "0049ea0c",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "0049ea0c",
      "PARAM",
      [
        "storage",
        "00c16e98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049ea00",
      "DATA",
      [
        "storage",
        "002a8a24",
        null,
        "string"
      ]
    ],
    [
      "0049ea0c",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049ea0c",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047bb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047ba2c.md#insn-0047bb78) · [`0047bb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047ba2c.md#insn-0047bb9c) · [`0047ba68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047ba2c.md#insn-0047ba68)
- 新版 [`0049ea10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md#insn-0049ea10) · [`0049ea34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md#insn-0049ea34) · [`0049e900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md#insn-0049e900)

~~~diff
- 0047bb78 ["INT_ADD", "register:40f0:8", ["const:47bb78:8", "const:4:8"]]
- 0047bb78 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049ea10 ["INT_ADD", "register:40f0:8", ["const:49ea10:8", "const:4:8"]]
+ 0049ea10 ["CALL", null, ["callee:00c57b10:8"]]
- 0047bb78 bytes 527d1d94
+ 0049ea10 bytes 40e41e94
- 0047bb9c ["INT_ADD", "register:40f0:8", ["const:47bb9c:8", "const:4:8"]]
- 0047bb9c ["CALL", null, ["callee:00c57b10:8"]]
+ 0049ea34 ["INT_ADD", "register:40f0:8", ["const:49ea34:8", "const:4:8"]]
+ 0049ea34 ["CALL", null, ["callee:00c57b10:8"]]
- 0047bb9c bytes 497d1d94
+ 0049ea34 bytes 37e41e94
- 0047ba68 ["INT_ADD", "register:40f0:8", ["const:47ba68:8", "const:4:8"]]
- 0047ba68 ["CALL", null, ["callee:00c57a90:8"]]
+ 0049e900 ["INT_ADD", "register:40f0:8", ["const:49e900:8", "const:4:8"]]
+ 0049e900 ["CALL", null, ["callee:00c57a90:8"]]
- 0047ba68 bytes 767d1d94
+ 0049e900 bytes 64e41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcb48589584e6d463e0903a15abba81b"></a>

### [`0047bbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bbd4.md) → [`0049ea6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ea6c.md) FUN_0049ea6c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0047ab48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047ab48.md) [`0047ba2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047ba2c.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 2件 [`0049d9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md) [`0049e8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md) · 呼出先 2件 [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049eb48",
      "incomplete_value": false,
      "site": "0049eb50",
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
            "const:a24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047bcb0",
      "incomplete_value": false,
      "site": "0047bcb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:c66:8"
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
      "definition_site": "0049eb58",
      "incomplete_value": true,
      "site": "0049eb5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047bcc0",
      "incomplete_value": true,
      "site": "0047bcc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "0049eb50",
      "DATA",
      [
        "storage",
        "00298c66",
        null,
        "string"
      ]
    ],
    [
      "0049eb58",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "0049eb58",
      "PARAM",
      [
        "storage",
        "00c16e98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049eb50",
      "DATA",
      [
        "storage",
        "002a8a24",
        null,
        "string"
      ]
    ],
    [
      "0049eb58",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049eb58",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047bcc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bbd4.md#insn-0047bcc4) · [`0047bca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bbd4.md#insn-0047bca8) · [`0047bcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bbd4.md#insn-0047bcac)
- 新版 [`0049eb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ea6c.md#insn-0049eb5c) · [`0049eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ea6c.md#insn-0049eb40) · [`0049eb44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ea6c.md#insn-0049eb44)

~~~diff
- 0047bcc4 ["INT_ADD", "register:40f0:8", ["const:47bcc4:8", "const:4:8"]]
- 0047bcc4 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049eb5c ["INT_ADD", "register:40f0:8", ["const:49eb5c:8", "const:4:8"]]
+ 0049eb5c ["CALL", null, ["callee:00c57b10:8"]]
- 0047bcc4 bytes ff7c1d94
+ 0049eb5c bytes ede31e94
- 0047bca8 ["INT_ADD", "register:40f0:8", ["const:47bca8:8", "const:4:8"]]
- 0047bca8 ["CALL", null, ["callee:00c57af0:8"]]
+ 0049eb40 ["INT_ADD", "register:40f0:8", ["const:49eb40:8", "const:4:8"]]
+ 0049eb40 ["CALL", null, ["callee:00c57af0:8"]]
- 0047bca8 bytes fe7c1d94
+ 0049eb40 bytes ece31e94
- 0047bcac ["COPY", "register:4040:8", ["const:298000:8"]]
+ 0049eb44 ["COPY", "register:4040:8", ["const:2a8000:8"]]
- 0047bcac bytes e8f0ffb0
+ 0049eb44 bytes 48f0ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cf1f63dcdf45709e68604960fedec80"></a>

### [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) → [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) FUN_0049f3b0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 65件 [`0047914c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/0047914c.md) [`0058c05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058c05c.md) [`005b8a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b8/005b8a40.md) [`005be130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be130.md) [`005c27f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c27f4.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 66件 [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) [`005b068c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b068c.md) [`005dd710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005dd710.md) [`005e2e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2e00.md) [`005e74c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e74c4.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "0049f3c0",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047c528",
      "value": [
        "leaf",
        "ram:41fdf0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049f3bc",
      "incomplete_value": false,
      "site": "0049f3c0",
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
      "definition_site": "0047c524",
      "incomplete_value": false,
      "site": "0047c528",
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
      "0049f3bc",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0049f3c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "0049f3bc",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0049f3c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004428f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047c528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md#insn-0047c528) · [`0047c520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md#insn-0047c520) · [`0047c524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md#insn-0047c524)
- 新版 [`0049f3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md#insn-0049f3c0) · [`0049f3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md#insn-0049f3b8) · [`0049f3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md#insn-0049f3bc)

~~~diff
- 0047c528 ["INT_ADD", "register:40f0:8", ["const:47c528:8", "const:4:8"]]
- 0047c528 ["CALL", null, ["ram:41fdf0:8"]]
+ 0049f3c0 ["INT_ADD", "register:40f0:8", ["const:49f3c0:8", "const:4:8"]]
+ 0049f3c0 ["CALL", null, ["ram:4428f0:8"]]
- 0047c528 bytes 328efe97
+ 0049f3c0 bytes 4c8dfe97
- 0047c520 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0049f3b8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0047c520 bytes 40f1fff0
+ 0049f3b8 bytes c0f0ff90
- 0047c524 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0047c524 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047c524 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047c524 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f3bc ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0049f3bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f3bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f3bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047c524 bytes 00740e91
+ 0049f3bc bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bd87c09edecd3dceb25ce21073fc742"></a>

### [`0047c52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c52c.md) → [`0049f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md) FUN_0049f3c4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00479c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479c04.md) [`0047a228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a228.md) [`0047a2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a2c0.md) [`0047adfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047adfc.md) [`0047b068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b068.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 5件 [`0049ca9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md) [`0049d0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d0c0.md) [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md) [`0049dc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md) [`0049df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "0049f3d4",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047c53c",
      "value": [
        "leaf",
        "ram:41fdf0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049f3d0",
      "incomplete_value": false,
      "site": "0049f3d4",
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
      "definition_site": "0047c538",
      "incomplete_value": false,
      "site": "0047c53c",
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
      "0049f3d0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0049f3d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "0049f3d0",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0049f3d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004428f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047c53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c52c.md#insn-0047c53c) · [`0047c534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c52c.md#insn-0047c534) · [`0047c538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c52c.md#insn-0047c538)
- 新版 [`0049f3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md#insn-0049f3d4) · [`0049f3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md#insn-0049f3cc) · [`0049f3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md#insn-0049f3d0)

~~~diff
- 0047c53c ["INT_ADD", "register:40f0:8", ["const:47c53c:8", "const:4:8"]]
- 0047c53c ["CALL", null, ["ram:41fdf0:8"]]
+ 0049f3d4 ["INT_ADD", "register:40f0:8", ["const:49f3d4:8", "const:4:8"]]
+ 0049f3d4 ["CALL", null, ["ram:4428f0:8"]]
- 0047c53c bytes 2d8efe97
+ 0049f3d4 bytes 478dfe97
- 0047c534 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0049f3cc ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0047c534 bytes 40f1fff0
+ 0049f3cc bytes c0f0ff90
- 0047c538 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0047c538 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047c538 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047c538 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f3d0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0049f3d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f3d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f3d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047c538 bytes 00740e91
+ 0049f3d0 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d5dfc68e398ae8ffc1a4942913d5969"></a>

### [`0047c540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c540.md) → [`0049f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md) FUN_0049f3d8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00479c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479c04.md) [`0047a228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a228.md) [`0047a2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047a2c0.md) [`0047adfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047adfc.md) [`0047b068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047b068.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 5件 [`0049ca9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md) [`0049d0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d0c0.md) [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md) [`0049dc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md) [`0049df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "0049f3e8",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047c550",
      "value": [
        "leaf",
        "ram:41fdf0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049f3e4",
      "incomplete_value": false,
      "site": "0049f3e8",
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
      "definition_site": "0047c54c",
      "incomplete_value": false,
      "site": "0047c550",
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
      "0049f3e4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0049f3e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "0049f3e4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0049f3e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004428f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047c550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c540.md#insn-0047c550) · [`0047c548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c540.md#insn-0047c548) · [`0047c54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c540.md#insn-0047c54c)
- 新版 [`0049f3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md#insn-0049f3e8) · [`0049f3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md#insn-0049f3e0) · [`0049f3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md#insn-0049f3e4)

~~~diff
- 0047c550 ["INT_ADD", "register:40f0:8", ["const:47c550:8", "const:4:8"]]
- 0047c550 ["CALL", null, ["ram:41fdf0:8"]]
+ 0049f3e8 ["INT_ADD", "register:40f0:8", ["const:49f3e8:8", "const:4:8"]]
+ 0049f3e8 ["CALL", null, ["ram:4428f0:8"]]
- 0047c550 bytes 288efe97
+ 0049f3e8 bytes 428dfe97
- 0047c548 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0049f3e0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0047c548 bytes 40f1fff0
+ 0049f3e0 bytes c0f0ff90
- 0047c54c ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0047c54c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047c54c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047c54c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f3e4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0049f3e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f3e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f3e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047c54c bytes 00740e91
+ 0049f3e4 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f221b486656c5e34e058261ece054da3"></a>

### [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) → [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) FUN_0049f3ec

採用 · 移動量 `+0x22e98` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 77件 [`004794a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/004794a0.md) [`0047ab48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047ab48.md) [`0047c568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c568.md) [`0047d078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d078.md) [`0047f2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f2d0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 77件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) [`0049d9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md) [`0049f400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f400.md) [`0049ff10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049ff10.md) [`004a2168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2168.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0049f3fc",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047c564",
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
      "definition_site": "0049f3f8",
      "incomplete_value": false,
      "site": "0049f3fc",
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
      "definition_site": "0047c560",
      "incomplete_value": false,
      "site": "0047c564",
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
      "0049f3f8",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0049f3fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0049f3f8",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0049f3fc",
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

- 旧版 [`0047c564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md#insn-0047c564) · [`0047c55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md#insn-0047c55c) · [`0047c560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md#insn-0047c560)
- 新版 [`0049f3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md#insn-0049f3fc) · [`0049f3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md#insn-0049f3f4) · [`0049f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md#insn-0049f3f8)

~~~diff
- 0047c564 ["INT_ADD", "register:40f0:8", ["const:47c564:8", "const:4:8"]]
- 0047c564 ["CALL", null, ["ram:418c38:8"]]
+ 0049f3fc ["INT_ADD", "register:40f0:8", ["const:49f3fc:8", "const:4:8"]]
+ 0049f3fc ["CALL", null, ["ram:43b738:8"]]
- 0047c564 bytes b571fe97
+ 0049f3fc bytes cf70fe97
- 0047c55c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0049f3f4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0047c55c bytes 40f1fff0
+ 0049f3f4 bytes c0f0ff90
- 0047c560 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0047c560 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047c560 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047c560 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f3f8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0049f3f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f3f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f3f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047c560 bytes 00740e91
+ 0049f3f8 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8e320c46250a2a9792730ef99816849"></a>

### [`0047c9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c9e0.md) → [`0049f878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f878.md) FUN_0049f878

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047c854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c854.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0049f6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f6ec.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0049f888",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047c9f0",
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
      "definition_site": "0049f884",
      "incomplete_value": false,
      "site": "0049f888",
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
      "definition_site": "0047c9ec",
      "incomplete_value": false,
      "site": "0047c9f0",
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
      "0049f884",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0049f888",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0049f884",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0049f888",
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

- 旧版 [`0047c9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c9e0.md#insn-0047c9f0) · [`0047c9e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c9e0.md#insn-0047c9e8) · [`0047c9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c9e0.md#insn-0047c9ec)
- 新版 [`0049f888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f878.md#insn-0049f888) · [`0049f880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f878.md#insn-0049f880) · [`0049f884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f878.md#insn-0049f884)

~~~diff
- 0047c9f0 ["INT_ADD", "register:40f0:8", ["const:47c9f0:8", "const:4:8"]]
- 0047c9f0 ["CALL", null, ["ram:418c38:8"]]
+ 0049f888 ["INT_ADD", "register:40f0:8", ["const:49f888:8", "const:4:8"]]
+ 0049f888 ["CALL", null, ["ram:43b738:8"]]
- 0047c9f0 bytes 9270fe97
+ 0049f888 bytes ac6ffe97
- 0047c9e8 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0049f880 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0047c9e8 bytes 40f1fff0
+ 0049f880 bytes c0f0ff90
- 0047c9ec ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0047c9ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047c9ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047c9ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f884 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0049f884 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f884 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f884 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047c9ec bytes 00740e91
+ 0049f884 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c4539d24ba1d8db7cd46610d5ea14c9"></a>

### [`0047c9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c9f4.md) → [`0049f88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f88c.md) FUN_0049f88c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004794a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/004794a0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "0049f89c",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047ca04",
      "value": [
        "leaf",
        "ram:41fdf0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049f898",
      "incomplete_value": false,
      "site": "0049f89c",
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
      "definition_site": "0047ca00",
      "incomplete_value": false,
      "site": "0047ca04",
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
      "0049f898",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0049f89c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "0049f898",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0049f89c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004428f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047ca04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c9f4.md#insn-0047ca04) · [`0047c9fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c9f4.md#insn-0047c9fc) · [`0047ca00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c9f4.md#insn-0047ca00)
- 新版 [`0049f89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f88c.md#insn-0049f89c) · [`0049f894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f88c.md#insn-0049f894) · [`0049f898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f88c.md#insn-0049f898)

~~~diff
- 0047ca04 ["INT_ADD", "register:40f0:8", ["const:47ca04:8", "const:4:8"]]
- 0047ca04 ["CALL", null, ["ram:41fdf0:8"]]
+ 0049f89c ["INT_ADD", "register:40f0:8", ["const:49f89c:8", "const:4:8"]]
+ 0049f89c ["CALL", null, ["ram:4428f0:8"]]
- 0047ca04 bytes fb8cfe97
+ 0049f89c bytes 158cfe97
- 0047c9fc ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0049f894 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0047c9fc bytes 40f1fff0
+ 0049f894 bytes c0f0ff90
- 0047ca00 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0047ca00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047ca00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047ca00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f898 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0049f898 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f898 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f898 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047ca00 bytes 00740e91
+ 0049f898 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b6a529aa0881f41db385b241c2a88da"></a>

### [`0047ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047ca08.md) → [`0049f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8a0.md) FUN_0049f8a0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`004794a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/004794a0.md) [`00479c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00479/00479c04.md) [`0047ab48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047a/0047ab48.md) [`0047ba2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047ba2c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 4件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) [`0049ca9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md) [`0049d9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md) [`0049e8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "0049f8b0",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047ca18",
      "value": [
        "leaf",
        "ram:41fdf0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049f8ac",
      "incomplete_value": false,
      "site": "0049f8b0",
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
      "definition_site": "0047ca14",
      "incomplete_value": false,
      "site": "0047ca18",
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
      "0049f8ac",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0049f8b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "0049f8ac",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0049f8b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004428f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047ca18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047ca08.md#insn-0047ca18) · [`0047ca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047ca08.md#insn-0047ca10) · [`0047ca14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047ca08.md#insn-0047ca14)
- 新版 [`0049f8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8a0.md#insn-0049f8b0) · [`0049f8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8a0.md#insn-0049f8a8) · [`0049f8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8a0.md#insn-0049f8ac)

~~~diff
- 0047ca18 ["INT_ADD", "register:40f0:8", ["const:47ca18:8", "const:4:8"]]
- 0047ca18 ["CALL", null, ["ram:41fdf0:8"]]
+ 0049f8b0 ["INT_ADD", "register:40f0:8", ["const:49f8b0:8", "const:4:8"]]
+ 0049f8b0 ["CALL", null, ["ram:4428f0:8"]]
- 0047ca18 bytes f68cfe97
+ 0049f8b0 bytes 108cfe97
- 0047ca10 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0049f8a8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0047ca10 bytes 40f1fff0
+ 0049f8a8 bytes c0f0ff90
- 0047ca14 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0047ca14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047ca14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047ca14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f8ac ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0049f8ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f8ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f8ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047ca14 bytes 00740e91
+ 0049f8ac bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-330dd1131e09f1226d2cab441cbef99d"></a>

### [`0047cba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cba4.md) → [`0049fa3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fa3c.md) FUN_0049fa3c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004787b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004787b4.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) · 呼出先 2件 [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fa98",
      "incomplete_value": false,
      "site": "0049faa0",
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
            "const:93d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cc00",
      "incomplete_value": false,
      "site": "0047cc08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:27c:8"
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
      "definition_site": "0049faa8",
      "incomplete_value": true,
      "site": "0049faac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cc10",
      "incomplete_value": true,
      "site": "0047cc14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "0049faa0",
      "DATA",
      [
        "storage",
        "002a227c",
        null,
        "string"
      ]
    ],
    [
      "0049faa8",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "0049faa8",
      "PARAM",
      [
        "storage",
        "00c16e98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049faa0",
      "DATA",
      [
        "storage",
        "002b293d",
        null,
        "string"
      ]
    ],
    [
      "0049faa8",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049faa8",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047cc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cba4.md#insn-0047cc14) · [`0047cbf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cba4.md#insn-0047cbf8) · [`0047cbfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cba4.md#insn-0047cbfc)
- 新版 [`0049faac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fa3c.md#insn-0049faac) · [`0049fa90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fa3c.md#insn-0049fa90) · [`0049fa94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fa3c.md#insn-0049fa94)

~~~diff
- 0047cc14 ["INT_ADD", "register:40f0:8", ["const:47cc14:8", "const:4:8"]]
- 0047cc14 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049faac ["INT_ADD", "register:40f0:8", ["const:49faac:8", "const:4:8"]]
+ 0049faac ["CALL", null, ["callee:00c57b10:8"]]
- 0047cc14 bytes 2b791d94
+ 0049faac bytes 19e01e94
- 0047cbf8 ["INT_ADD", "register:40f0:8", ["const:47cbf8:8", "const:4:8"]]
- 0047cbf8 ["CALL", null, ["callee:00c57af0:8"]]
+ 0049fa90 ["INT_ADD", "register:40f0:8", ["const:49fa90:8", "const:4:8"]]
+ 0049fa90 ["CALL", null, ["callee:00c57af0:8"]]
- 0047cbf8 bytes 2a791d94
+ 0049fa90 bytes 18e01e94
- 0047cbfc ["COPY", "register:4040:8", ["const:2a2000:8"]]
+ 0049fa94 ["COPY", "register:4040:8", ["const:2b2000:8"]]
- 0047cbfc bytes 28f1ffd0
+ 0049fa94 bytes 88f0fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08bd282e89ffb5a4c87c6529a484012f"></a>

### [`0047cc18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cc18.md) → [`0049fab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fab0.md) FUN_0049fab0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047d078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d078.md) · 呼出先 5件 [`004784f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004784f0.md) [`004785c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004785c8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`0049ff10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049ff10.md) · 呼出先 5件 [`0049b388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b388.md) [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.87% / 新版 89.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fb34",
      "incomplete_value": true,
      "site": "0049fb4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cc9c",
      "incomplete_value": true,
      "site": "0047ccb4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:640:8"
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
      "definition_site": "0049fb9c",
      "incomplete_value": false,
      "site": "0049fba4",
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
            "const:2d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cd04",
      "incomplete_value": false,
      "site": "0047cd0c",
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
            "const:4be:8"
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
      "definition_site": "0049fbc0",
      "incomplete_value": false,
      "site": "0049fbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:3a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cd28",
      "incomplete_value": false,
      "site": "0047cd2c",
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
            "const:397:8"
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
      "0049fb34",
      "READ",
      [
        "storage",
        "002b1640",
        null,
        null
      ]
    ],
    [
      "0049fba4",
      "DATA",
      [
        "storage",
        "002a74be",
        null,
        "string"
      ]
    ],
    [
      "0049fbac",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049fb34",
      "READ",
      [
        "storage",
        "002c2c90",
        null,
        null
      ]
    ],
    [
      "0049fba4",
      "DATA",
      [
        "storage",
        "002b802d",
        null,
        "string"
      ]
    ],
    [
      "0049fbac",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047cd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cc18.md#insn-0047cd18) · [`0047cd4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cc18.md#insn-0047cd4c) · [`0047cc58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cc18.md#insn-0047cc58)
- 新版 [`0049fbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fab0.md#insn-0049fbb0) · [`0049fbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fab0.md#insn-0049fbe4) · [`0049faf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fab0.md#insn-0049faf0)

~~~diff
- 0047cd18 ["INT_ADD", "register:40f0:8", ["const:47cd18:8", "const:4:8"]]
- 0047cd18 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049fbb0 ["INT_ADD", "register:40f0:8", ["const:49fbb0:8", "const:4:8"]]
+ 0049fbb0 ["CALL", null, ["callee:00c57b10:8"]]
- 0047cd18 bytes ea781d94
+ 0049fbb0 bytes d8df1e94
- 0047cd4c ["INT_ADD", "register:40f0:8", ["const:47cd4c:8", "const:4:8"]]
- 0047cd4c ["CALL", null, ["callee:00c57b10:8"]]
+ 0049fbe4 ["INT_ADD", "register:40f0:8", ["const:49fbe4:8", "const:4:8"]]
+ 0049fbe4 ["CALL", null, ["callee:00c57b10:8"]]
- 0047cd4c bytes dd781d94
+ 0049fbe4 bytes cbdf1e94
- 0047cc58 ["INT_ADD", "register:40f0:8", ["const:47cc58:8", "const:4:8"]]
- 0047cc58 ["CALL", null, ["callee:0049b388:8"]]
+ 0049faf0 ["INT_ADD", "register:40f0:8", ["const:49faf0:8", "const:4:8"]]
+ 0049faf0 ["CALL", null, ["callee:0049b388:8"]]
- 0047cc58 bytes 26eeff97
+ 0049faf0 bytes 26eeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acf18b5d67a7769ebb4a2e8018f419c2"></a>

### [`0047cd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cd90.md) → [`0049fc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fc28.md) FUN_0049fc28

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047d078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d078.md) · 呼出先 5件 [`004784f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004784f0.md) [`004785c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004785c8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`0049ff10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049ff10.md) · 呼出先 5件 [`0049b388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b388.md) [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fcec",
      "incomplete_value": true,
      "site": "0049fcf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ce54",
      "incomplete_value": true,
      "site": "0047ce60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e90:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fd34",
      "incomplete_value": false,
      "site": "0049fd38",
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
            "const:8fd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ce9c",
      "incomplete_value": false,
      "site": "0047cea0",
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
            "const:223:8"
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
      "definition_site": "0049fd54",
      "incomplete_value": true,
      "site": "0049fd58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cebc",
      "incomplete_value": true,
      "site": "0047cec0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "0049fcec",
      "READ",
      [
        "storage",
        "002b0e90",
        null,
        null
      ]
    ],
    [
      "0049fd38",
      "DATA",
      [
        "storage",
        "002a3223",
        null,
        "string"
      ]
    ],
    [
      "0049fd54",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049fcec",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ],
    [
      "0049fd38",
      "DATA",
      [
        "storage",
        "002b38fd",
        null,
        "string"
      ]
    ],
    [
      "0049fd54",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047cec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cd90.md#insn-0047cec0) · [`0047cdc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cd90.md#insn-0047cdc0) · [`0047ce18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cd90.md#insn-0047ce18)
- 新版 [`0049fd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fc28.md#insn-0049fd58) · [`0049fc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fc28.md#insn-0049fc58) · [`0049fcb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fc28.md#insn-0049fcb0)

~~~diff
- 0047cec0 ["INT_ADD", "register:40f0:8", ["const:47cec0:8", "const:4:8"]]
- 0047cec0 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049fd58 ["INT_ADD", "register:40f0:8", ["const:49fd58:8", "const:4:8"]]
+ 0049fd58 ["CALL", null, ["callee:00c57b10:8"]]
- 0047cec0 bytes 80781d94
+ 0049fd58 bytes 6edf1e94
- 0047cdc0 ["INT_ADD", "register:40f0:8", ["const:47cdc0:8", "const:4:8"]]
- 0047cdc0 ["CALL", null, ["callee:0049b388:8"]]
+ 0049fc58 ["INT_ADD", "register:40f0:8", ["const:49fc58:8", "const:4:8"]]
+ 0049fc58 ["CALL", null, ["callee:0049b388:8"]]
- 0047cdc0 bytes ccedff97
+ 0049fc58 bytes ccedff97
- 0047ce18 ["INT_ADD", "register:40f0:8", ["const:47ce18:8", "const:4:8"]]
- 0047ce18 ["CALL", null, ["callee:0049b460:8"]]
+ 0049fcb0 ["INT_ADD", "register:40f0:8", ["const:49fcb0:8", "const:4:8"]]
+ 0049fcb0 ["CALL", null, ["callee:0049b460:8"]]
- 0047ce18 bytes ecedff97
+ 0049fcb0 bytes ecedff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77c3d5d915a2ae10597ceabd32f8ec70"></a>

### [`0047cef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cef8.md) → [`0049fd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fd90.md) FUN_0049fd90

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047d078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d078.md) · 呼出先 6件 [`004784f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004784f0.md) [`004785c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004785c8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`0049ff10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049ff10.md) · 呼出先 6件 [`0049b388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b388.md) [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fe68",
      "incomplete_value": true,
      "site": "0049fe74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cfd0",
      "incomplete_value": true,
      "site": "0047cfdc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:170:8"
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
      "definition_site": "0049feb4",
      "incomplete_value": false,
      "site": "0049feb8",
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
            "const:b9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d01c",
      "incomplete_value": false,
      "site": "0047d020",
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
            "const:6b8:8"
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
      "definition_site": "0049fdfc",
      "incomplete_value": true,
      "site": "0049fe04",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:390:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cf64",
      "incomplete_value": true,
      "site": "0047cf6c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:8a8:8"
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
      "0049fdfc",
      "READ",
      [
        "storage",
        "00c238a8",
        null,
        "pointer"
      ]
    ],
    [
      "0049fdfc",
      "PARAM",
      [
        "storage",
        "002ab4b1",
        null,
        "string"
      ]
    ],
    [
      "0049fe0c",
      "READ",
      [
        "storage",
        "00c238a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049fdfc",
      "READ",
      [
        "storage",
        "00ca3390",
        null,
        "pointer"
      ]
    ],
    [
      "0049fdfc",
      "PARAM",
      [
        "storage",
        "002bc3d4",
        null,
        "string"
      ]
    ],
    [
      "0049fe0c",
      "READ",
      [
        "storage",
        "00ca3390",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047cf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cef8.md#insn-0047cf6c) · [`0047d040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cef8.md#insn-0047d040) · [`0047cf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047cef8.md#insn-0047cf2c)
- 新版 [`0049fe04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fd90.md#insn-0049fe04) · [`0049fed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fd90.md#insn-0049fed8) · [`0049fdc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fd90.md#insn-0049fdc4)

~~~diff
- 0047cf6c ["INT_ADD", "register:40f0:8", ["const:47cf6c:8", "const:4:8"]]
- 0047cf6c ["CALL", null, ["callee:00c58230:8"]]
+ 0049fe04 ["INT_ADD", "register:40f0:8", ["const:49fe04:8", "const:4:8"]]
+ 0049fe04 ["CALL", null, ["callee:00c58230:8"]]
- 0047cf6c bytes 1d7a1d94
+ 0049fe04 bytes 0be11e94
- 0047d040 ["INT_ADD", "register:40f0:8", ["const:47d040:8", "const:4:8"]]
- 0047d040 ["CALL", null, ["callee:00c57b10:8"]]
+ 0049fed8 ["INT_ADD", "register:40f0:8", ["const:49fed8:8", "const:4:8"]]
+ 0049fed8 ["CALL", null, ["callee:00c57b10:8"]]
- 0047d040 bytes 20781d94
+ 0049fed8 bytes 0edf1e94
- 0047cf2c ["INT_ADD", "register:40f0:8", ["const:47cf2c:8", "const:4:8"]]
- 0047cf2c ["CALL", null, ["callee:0049b388:8"]]
+ 0049fdc4 ["INT_ADD", "register:40f0:8", ["const:49fdc4:8", "const:4:8"]]
+ 0049fdc4 ["CALL", null, ["callee:0049b388:8"]]
- 0047cf2c bytes 71edff97
+ 0049fdc4 bytes 71edff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-579c391472388cd06866bd72d6bc293c"></a>

### [`0047d3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d3a0.md) → [`004a0238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0238.md) FUN_004a0238

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004787b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004787b4.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) · 呼出先 2件 [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.34% / 新版 94.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004a02f4",
      "incomplete_value": false,
      "site": "004a02fc",
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
            "const:93d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d45c",
      "incomplete_value": false,
      "site": "0047d464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:27c:8"
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
      "definition_site": "004a0304",
      "incomplete_value": true,
      "site": "004a0308",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d46c",
      "incomplete_value": true,
      "site": "0047d470",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
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
      "004a02fc",
      "DATA",
      [
        "storage",
        "002a227c",
        null,
        "string"
      ]
    ],
    [
      "004a0304",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "004a0304",
      "PARAM",
      [
        "storage",
        "00c16e98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a02fc",
      "DATA",
      [
        "storage",
        "002b293d",
        null,
        "string"
      ]
    ],
    [
      "004a0304",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "004a0304",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d3a0.md#insn-0047d470) · [`0047d454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d3a0.md#insn-0047d454) · [`0047d458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d3a0.md#insn-0047d458)
- 新版 [`004a0308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0238.md#insn-004a0308) · [`004a02ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0238.md#insn-004a02ec) · [`004a02f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0238.md#insn-004a02f0)

~~~diff
- 0047d470 ["INT_ADD", "register:40f0:8", ["const:47d470:8", "const:4:8"]]
- 0047d470 ["CALL", null, ["callee:00c57b10:8"]]
+ 004a0308 ["INT_ADD", "register:40f0:8", ["const:4a0308:8", "const:4:8"]]
+ 004a0308 ["CALL", null, ["callee:00c57b10:8"]]
- 0047d470 bytes 14771d94
+ 004a0308 bytes 02de1e94
- 0047d454 ["INT_ADD", "register:40f0:8", ["const:47d454:8", "const:4:8"]]
- 0047d454 ["CALL", null, ["callee:00c57af0:8"]]
+ 004a02ec ["INT_ADD", "register:40f0:8", ["const:4a02ec:8", "const:4:8"]]
+ 004a02ec ["CALL", null, ["callee:00c57af0:8"]]
- 0047d454 bytes 13771d94
+ 004a02ec bytes 01de1e94
- 0047d458 ["COPY", "register:4040:8", ["const:2a2000:8"]]
+ 004a02f0 ["COPY", "register:4040:8", ["const:2b2000:8"]]
- 0047d458 bytes 28f1ffb0
+ 004a02f0 bytes 88f0ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5144fe58b04d80d8ca59f49bc2f5b06"></a>

### [`0047d610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d610.md) → [`004a04a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a04a8.md) FUN_004a04a8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047d490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d490.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`004a0328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0328.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "004a04b8",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047d620",
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
      "definition_site": "004a04b4",
      "incomplete_value": false,
      "site": "004a04b8",
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
      "definition_site": "0047d61c",
      "incomplete_value": false,
      "site": "0047d620",
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
      "004a04b4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "004a04b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "004a04b4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "004a04b8",
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

- 旧版 [`0047d620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d610.md#insn-0047d620) · [`0047d618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d610.md#insn-0047d618) · [`0047d61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d610.md#insn-0047d61c)
- 新版 [`004a04b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a04a8.md#insn-004a04b8) · [`004a04b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a04a8.md#insn-004a04b0) · [`004a04b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a04a8.md#insn-004a04b4)

~~~diff
- 0047d620 ["INT_ADD", "register:40f0:8", ["const:47d620:8", "const:4:8"]]
- 0047d620 ["CALL", null, ["ram:418c38:8"]]
+ 004a04b8 ["INT_ADD", "register:40f0:8", ["const:4a04b8:8", "const:4:8"]]
+ 004a04b8 ["CALL", null, ["ram:43b738:8"]]
- 0047d620 bytes 866dfe97
+ 004a04b8 bytes a06cfe97
- 0047d618 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 004a04b0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0047d618 bytes 40f1ffd0
+ 004a04b0 bytes a0f0fff0
- 0047d61c ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0047d61c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047d61c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047d61c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004a04b4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 004a04b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004a04b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004a04b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047d61c bytes 00740e91
+ 004a04b4 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fe14f16f1d8702a5b3e0bf84641af2a"></a>

### [`0047d690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d690.md) → [`004a0528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0528.md) _ZNK5Botan7AES_1289encrypt_nEPKhPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047d7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d7b0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

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
      "site": "004a05c4",
      "value": [
        "leaf",
        "ram:c58240:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047d72c",
      "value": [
        "leaf",
        "ram:bdb7f0:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a05e8",
      "incomplete_value": true,
      "site": "004a05f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d750",
      "incomplete_value": true,
      "site": "0047d75c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
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
      "definition_site": "004a05e4",
      "incomplete_value": false,
      "site": "004a05f4",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0047d74c",
      "incomplete_value": false,
      "site": "0047d75c",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004a05c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb7f0"
      ]
    ],
    [
      "004a05e4",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004a05e8",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a05c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58240"
      ]
    ],
    [
      "004a05e4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a05e8",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d690.md#insn-0047d72c) · [`0047d75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d690.md#insn-0047d75c) · [`0047d704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d690.md#insn-0047d704)
- 新版 [`004a05c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0528.md#insn-004a05c4) · [`004a05f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0528.md#insn-004a05f4) · [`004a059c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0528.md#insn-004a059c)

~~~diff
- 0047d72c ["INT_ADD", "register:40f0:8", ["const:47d72c:8", "const:4:8"]]
- 0047d72c ["CALL", null, ["ram:bdb7f0:8"]]
+ 004a05c4 ["INT_ADD", "register:40f0:8", ["const:4a05c4:8", "const:4:8"]]
+ 004a05c4 ["CALL", null, ["ram:c58240:8"]]
- 0047d72c bytes 31781d94
+ 004a05c4 bytes 1fdf1e94
- 0047d75c ["INT_ADD", "register:40f0:8", ["const:47d75c:8", "const:4:8"]]
- 0047d75c ["CALL", null, ["callee:00c57b10:8"]]
+ 004a05f4 ["INT_ADD", "register:40f0:8", ["const:4a05f4:8", "const:4:8"]]
+ 004a05f4 ["CALL", null, ["callee:00c57b10:8"]]
- 0047d75c bytes 59761d94
+ 004a05f4 bytes 47dd1e94
- 0047d704 ["INT_ADD", "register:40f0:8", ["const:47d704:8", "const:4:8"]]
- 0047d704 ["CALL", null, ["callee:00c57af0:8"]]
+ 004a059c ["INT_ADD", "register:40f0:8", ["const:4a059c:8", "const:4:8"]]
+ 004a059c ["CALL", null, ["callee:00c57af0:8"]]
- 0047d704 bytes 67761d94
+ 004a059c bytes 55dd1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1a6dde9c899a3d837b16fc900adb710"></a>

### [`0047d7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d7b0.md) → [`004a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md) FUN_004a0648

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0047d690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d690.md) [`0047ec98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047ec98.md) [`0047efb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047efb4.md) · 呼出先 4件 [`00512a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512a64.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 3件 [`004a0528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0528.md) [`004a1b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1b30.md) [`004a1e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1e4c.md) · 呼出先 4件 [`005358fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005358fc.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.01% / 新版 97.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004a0688",
      "incomplete_value": true,
      "site": "004a0688",
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
              "LOAD"
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
      "definition_site": "0047d7f0",
      "incomplete_value": true,
      "site": "0047d7f0",
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
              "LOAD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a0b94",
      "incomplete_value": false,
      "site": "004a0bb4",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047dcfc",
      "incomplete_value": false,
      "site": "0047dd1c",
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
            "const:4f2:8"
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
      "definition_site": "004a0b9c",
      "incomplete_value": false,
      "site": "004a0bb4",
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
            "const:16a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047dd04",
      "incomplete_value": false,
      "site": "0047dd1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:b51:8"
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
      "004a0680",
      "READ",
      [
        "storage",
        "00c1af28",
        null,
        "pointer"
      ]
    ],
    [
      "004a0684",
      "READ",
      [
        "storage",
        "00c25378",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004a0690",
      "WRITE",
      [
        "storage",
        "00c25378",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004a0680",
      "READ",
      [
        "storage",
        "00c9a918",
        null,
        "pointer"
      ]
    ],
    [
      "004a0684",
      "READ",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004a0690",
      "WRITE",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d7b0.md#insn-0047dd1c) · [`0047dd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d7b0.md#insn-0047dd38) · [`0047dd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d7b0.md#insn-0047dd50)
- 新版 [`004a0bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md#insn-004a0bb4) · [`004a0bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md#insn-004a0bd0) · [`004a0be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md#insn-004a0be8)

~~~diff
- 0047dd1c ["INT_ADD", "register:40f0:8", ["const:47dd1c:8", "const:4:8"]]
- 0047dd1c ["CALL", null, ["callee:00c58250:8"]]
+ 004a0bb4 ["INT_ADD", "register:40f0:8", ["const:4a0bb4:8", "const:4:8"]]
+ 004a0bb4 ["CALL", null, ["callee:00c58250:8"]]
- 0047dd1c bytes b9761d94
+ 004a0bb4 bytes a7dd1e94
- 0047dd38 ["INT_ADD", "register:40f0:8", ["const:47dd38:8", "const:4:8"]]
- 0047dd38 ["CALL", null, ["callee:00c57a50:8"]]
+ 004a0bd0 ["INT_ADD", "register:40f0:8", ["const:4a0bd0:8", "const:4:8"]]
+ 004a0bd0 ["CALL", null, ["callee:00c57a50:8"]]
- 0047dd38 bytes b2741d94
+ 004a0bd0 bytes a0db1e94
- 0047dd50 ["INT_ADD", "register:40f0:8", ["const:47dd50:8", "const:4:8"]]
- 0047dd50 ["CALL", null, ["ram:512a64:8"]]
+ 004a0be8 ["INT_ADD", "register:40f0:8", ["const:4a0be8:8", "const:4:8"]]
+ 004a0be8 ["CALL", null, ["ram:5358fc:8"]]
- 0047dd50 bytes 45530294
+ 004a0be8 bytes 45530294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c915a48926833b3ff9a3ed888560cbb"></a>

### [`0047dd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047dd70.md) → [`004a0c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0c08.md) _ZNK5Botan7AES_1289decrypt_nEPKhPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047de90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047de90.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

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
      "site": "004a0ca4",
      "value": [
        "leaf",
        "ram:c58240:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047de0c",
      "value": [
        "leaf",
        "ram:bdb7f0:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a0cc8",
      "incomplete_value": true,
      "site": "004a0cd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047de30",
      "incomplete_value": true,
      "site": "0047de3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
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
      "definition_site": "004a0cc4",
      "incomplete_value": false,
      "site": "004a0cd4",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0047de2c",
      "incomplete_value": false,
      "site": "0047de3c",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004a0ca4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb7f0"
      ]
    ],
    [
      "004a0cc4",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004a0cc8",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a0ca4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58240"
      ]
    ],
    [
      "004a0cc4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a0cc8",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047de0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047dd70.md#insn-0047de0c) · [`0047de3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047dd70.md#insn-0047de3c) · [`0047dde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047dd70.md#insn-0047dde4)
- 新版 [`004a0ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0c08.md#insn-004a0ca4) · [`004a0cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0c08.md#insn-004a0cd4) · [`004a0c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0c08.md#insn-004a0c7c)

~~~diff
- 0047de0c ["INT_ADD", "register:40f0:8", ["const:47de0c:8", "const:4:8"]]
- 0047de0c ["CALL", null, ["ram:bdb7f0:8"]]
+ 004a0ca4 ["INT_ADD", "register:40f0:8", ["const:4a0ca4:8", "const:4:8"]]
+ 004a0ca4 ["CALL", null, ["ram:c58240:8"]]
- 0047de0c bytes 79761d94
+ 004a0ca4 bytes 67dd1e94
- 0047de3c ["INT_ADD", "register:40f0:8", ["const:47de3c:8", "const:4:8"]]
- 0047de3c ["CALL", null, ["callee:00c57b10:8"]]
+ 004a0cd4 ["INT_ADD", "register:40f0:8", ["const:4a0cd4:8", "const:4:8"]]
+ 004a0cd4 ["CALL", null, ["callee:00c57b10:8"]]
- 0047de3c bytes a1741d94
+ 004a0cd4 bytes 8fdb1e94
- 0047dde4 ["INT_ADD", "register:40f0:8", ["const:47dde4:8", "const:4:8"]]
- 0047dde4 ["CALL", null, ["callee:00c57af0:8"]]
+ 004a0c7c ["INT_ADD", "register:40f0:8", ["const:4a0c7c:8", "const:4:8"]]
+ 004a0c7c ["CALL", null, ["callee:00c57af0:8"]]
- 0047dde4 bytes af741d94
+ 004a0c7c bytes 9ddb1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47bf64199897915c495745e145cfc2d5"></a>

### [`0047de90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047de90.md) → [`004a0d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md) FUN_004a0d28

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0047dd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047dd70.md) [`0047edb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047edb8.md) [`0047f0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f0d4.md) · 呼出先 4件 [`00512b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512b5c.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 3件 [`004a0c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0c08.md) [`004a1c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1c50.md) [`004a1f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1f6c.md) · 呼出先 4件 [`005359f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005359f4.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004a0d68",
      "incomplete_value": true,
      "site": "004a0d68",
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
              "LOAD"
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
      "definition_site": "0047ded0",
      "incomplete_value": true,
      "site": "0047ded0",
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
              "LOAD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1280",
      "incomplete_value": false,
      "site": "004a12a0",
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
            "const:172:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e3e8",
      "incomplete_value": false,
      "site": "0047e408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:979:8"
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
      "definition_site": "004a1288",
      "incomplete_value": false,
      "site": "004a12a0",
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
            "const:16a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e3f0",
      "incomplete_value": false,
      "site": "0047e408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:b51:8"
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
      "004a0d60",
      "READ",
      [
        "storage",
        "00c1af28",
        null,
        "pointer"
      ]
    ],
    [
      "004a0d64",
      "READ",
      [
        "storage",
        "00c25378",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004a0d70",
      "WRITE",
      [
        "storage",
        "00c25378",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004a0d60",
      "READ",
      [
        "storage",
        "00c9a918",
        null,
        "pointer"
      ]
    ],
    [
      "004a0d64",
      "READ",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004a0d70",
      "WRITE",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047e408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047de90.md#insn-0047e408) · [`0047e424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047de90.md#insn-0047e424) · [`0047e43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047de90.md#insn-0047e43c)
- 新版 [`004a12a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md#insn-004a12a0) · [`004a12bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md#insn-004a12bc) · [`004a12d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md#insn-004a12d4)

~~~diff
- 0047e408 ["INT_ADD", "register:40f0:8", ["const:47e408:8", "const:4:8"]]
- 0047e408 ["CALL", null, ["callee:00c58250:8"]]
+ 004a12a0 ["INT_ADD", "register:40f0:8", ["const:4a12a0:8", "const:4:8"]]
+ 004a12a0 ["CALL", null, ["callee:00c58250:8"]]
- 0047e408 bytes fe741d94
+ 004a12a0 bytes ecdb1e94
- 0047e424 ["INT_ADD", "register:40f0:8", ["const:47e424:8", "const:4:8"]]
- 0047e424 ["CALL", null, ["callee:00c57a50:8"]]
+ 004a12bc ["INT_ADD", "register:40f0:8", ["const:4a12bc:8", "const:4:8"]]
+ 004a12bc ["CALL", null, ["callee:00c57a50:8"]]
- 0047e424 bytes f7721d94
+ 004a12bc bytes e5d91e94
- 0047e43c ["INT_ADD", "register:40f0:8", ["const:47e43c:8", "const:4:8"]]
- 0047e43c ["CALL", null, ["ram:512b5c:8"]]
+ 004a12d4 ["INT_ADD", "register:40f0:8", ["const:4a12d4:8", "const:4:8"]]
+ 004a12d4 ["CALL", null, ["ram:5359f4:8"]]
- 0047e43c bytes c8510294
+ 004a12d4 bytes c8510294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53de5b1ab2b2c10f4ec0db0484035012"></a>

### [`0047e47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047e47c.md) → [`004a1314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1314.md) FUN_004a1314

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0047e45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047e45c.md) [`0047eed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047eed8.md) [`0047f1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f1f4.md) · 呼出先 15件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512b5c.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md)
- 新版 呼出元 3件 [`004a12f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a12f4.md) [`004a1d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1d70.md) [`004a208c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a208c.md) · 呼出先 15件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005359f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005359f4.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.84% / 新版 96.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a170c",
      "value": [
        "leaf",
        "ram:5359f4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047e874",
      "value": [
        "leaf",
        "ram:512b5c:8"
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
      "site": "004a1728",
      "value": [
        "leaf",
        "ram:5359f4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047e890",
      "value": [
        "leaf",
        "ram:512b5c:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a1744",
      "value": [
        "leaf",
        "ram:5359f4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047e8ac",
      "value": [
        "leaf",
        "ram:512b5c:8"
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
      "004a1488",
      "DATA",
      [
        "storage",
        "002bdbc0",
        null,
        null
      ]
    ],
    [
      "004a148c",
      "DATA",
      [
        "storage",
        "002bdbc0",
        null,
        null
      ]
    ],
    [
      "004a1490",
      "DATA",
      [
        "storage",
        "002bdbc0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a1488",
      "DATA",
      [
        "storage",
        "002cf300",
        null,
        null
      ]
    ],
    [
      "004a148c",
      "DATA",
      [
        "storage",
        "002cf300",
        null,
        null
      ]
    ],
    [
      "004a1490",
      "DATA",
      [
        "storage",
        "002cf300",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047e874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047e47c.md#insn-0047e874) · [`0047e890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047e47c.md#insn-0047e890) · [`0047e8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047e47c.md#insn-0047e8ac)
- 新版 [`004a170c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1314.md#insn-004a170c) · [`004a1728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1314.md#insn-004a1728) · [`004a1744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1314.md#insn-004a1744)

~~~diff
- 0047e874 ["INT_ADD", "register:40f0:8", ["const:47e874:8", "const:4:8"]]
- 0047e874 ["CALL", null, ["ram:512b5c:8"]]
+ 004a170c ["INT_ADD", "register:40f0:8", ["const:4a170c:8", "const:4:8"]]
+ 004a170c ["CALL", null, ["ram:5359f4:8"]]
- 0047e874 bytes ba500294
+ 004a170c bytes ba500294
- 0047e890 ["INT_ADD", "register:40f0:8", ["const:47e890:8", "const:4:8"]]
- 0047e890 ["CALL", null, ["ram:512b5c:8"]]
+ 004a1728 ["INT_ADD", "register:40f0:8", ["const:4a1728:8", "const:4:8"]]
+ 004a1728 ["CALL", null, ["ram:5359f4:8"]]
- 0047e890 bytes b3500294
+ 004a1728 bytes b3500294
- 0047e8ac ["INT_ADD", "register:40f0:8", ["const:47e8ac:8", "const:4:8"]]
- 0047e8ac ["CALL", null, ["ram:512b5c:8"]]
+ 004a1744 ["INT_ADD", "register:40f0:8", ["const:4a1744:8", "const:4:8"]]
+ 004a1744 ["CALL", null, ["ram:5359f4:8"]]
- 0047e8ac bytes ac500294
+ 004a1744 bytes ac500294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c425d23e06a47605cff7aa0114e435c0"></a>

### [`0047ec98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047ec98.md) → [`004a1b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1b30.md) _ZNK5Botan7AES_1929encrypt_nEPKhPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047d7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d7b0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

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
      "site": "004a1bcc",
      "value": [
        "leaf",
        "ram:c58240:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047ed34",
      "value": [
        "leaf",
        "ram:bdb7f0:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1bf0",
      "incomplete_value": true,
      "site": "004a1bfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ed58",
      "incomplete_value": true,
      "site": "0047ed64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
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
      "definition_site": "004a1bec",
      "incomplete_value": false,
      "site": "004a1bfc",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0047ed54",
      "incomplete_value": false,
      "site": "0047ed64",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004a1bcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb7f0"
      ]
    ],
    [
      "004a1bec",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004a1bf0",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a1bcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58240"
      ]
    ],
    [
      "004a1bec",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a1bf0",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047ed34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047ec98.md#insn-0047ed34) · [`0047ed64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047ec98.md#insn-0047ed64) · [`0047ed0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047ec98.md#insn-0047ed0c)
- 新版 [`004a1bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1b30.md#insn-004a1bcc) · [`004a1bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1b30.md#insn-004a1bfc) · [`004a1ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1b30.md#insn-004a1ba4)

~~~diff
- 0047ed34 ["INT_ADD", "register:40f0:8", ["const:47ed34:8", "const:4:8"]]
- 0047ed34 ["CALL", null, ["ram:bdb7f0:8"]]
+ 004a1bcc ["INT_ADD", "register:40f0:8", ["const:4a1bcc:8", "const:4:8"]]
+ 004a1bcc ["CALL", null, ["ram:c58240:8"]]
- 0047ed34 bytes af721d94
+ 004a1bcc bytes 9dd91e94
- 0047ed64 ["INT_ADD", "register:40f0:8", ["const:47ed64:8", "const:4:8"]]
- 0047ed64 ["CALL", null, ["callee:00c57b10:8"]]
+ 004a1bfc ["INT_ADD", "register:40f0:8", ["const:4a1bfc:8", "const:4:8"]]
+ 004a1bfc ["CALL", null, ["callee:00c57b10:8"]]
- 0047ed64 bytes d7701d94
+ 004a1bfc bytes c5d71e94
- 0047ed0c ["INT_ADD", "register:40f0:8", ["const:47ed0c:8", "const:4:8"]]
- 0047ed0c ["CALL", null, ["callee:00c57af0:8"]]
+ 004a1ba4 ["INT_ADD", "register:40f0:8", ["const:4a1ba4:8", "const:4:8"]]
+ 004a1ba4 ["CALL", null, ["callee:00c57af0:8"]]
- 0047ed0c bytes e5701d94
+ 004a1ba4 bytes d3d71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a032f1fb37f97c29867e932f9de2551"></a>

### [`0047edb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047edb8.md) → [`004a1c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1c50.md) _ZNK5Botan7AES_1929decrypt_nEPKhPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047de90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047de90.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

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
      "site": "004a1cec",
      "value": [
        "leaf",
        "ram:c58240:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047ee54",
      "value": [
        "leaf",
        "ram:bdb7f0:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1d10",
      "incomplete_value": true,
      "site": "004a1d1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ee78",
      "incomplete_value": true,
      "site": "0047ee84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
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
      "definition_site": "004a1d0c",
      "incomplete_value": false,
      "site": "004a1d1c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0047ee74",
      "incomplete_value": false,
      "site": "0047ee84",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004a1cec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb7f0"
      ]
    ],
    [
      "004a1d0c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004a1d10",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a1cec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58240"
      ]
    ],
    [
      "004a1d0c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a1d10",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047ee54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047edb8.md#insn-0047ee54) · [`0047ee84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047edb8.md#insn-0047ee84) · [`0047ee2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047edb8.md#insn-0047ee2c)
- 新版 [`004a1cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1c50.md#insn-004a1cec) · [`004a1d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1c50.md#insn-004a1d1c) · [`004a1cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1c50.md#insn-004a1cc4)

~~~diff
- 0047ee54 ["INT_ADD", "register:40f0:8", ["const:47ee54:8", "const:4:8"]]
- 0047ee54 ["CALL", null, ["ram:bdb7f0:8"]]
+ 004a1cec ["INT_ADD", "register:40f0:8", ["const:4a1cec:8", "const:4:8"]]
+ 004a1cec ["CALL", null, ["ram:c58240:8"]]
- 0047ee54 bytes 67721d94
+ 004a1cec bytes 55d91e94
- 0047ee84 ["INT_ADD", "register:40f0:8", ["const:47ee84:8", "const:4:8"]]
- 0047ee84 ["CALL", null, ["callee:00c57b10:8"]]
+ 004a1d1c ["INT_ADD", "register:40f0:8", ["const:4a1d1c:8", "const:4:8"]]
+ 004a1d1c ["CALL", null, ["callee:00c57b10:8"]]
- 0047ee84 bytes 8f701d94
+ 004a1d1c bytes 7dd71e94
- 0047ee2c ["INT_ADD", "register:40f0:8", ["const:47ee2c:8", "const:4:8"]]
- 0047ee2c ["CALL", null, ["callee:00c57af0:8"]]
+ 004a1cc4 ["INT_ADD", "register:40f0:8", ["const:4a1cc4:8", "const:4:8"]]
+ 004a1cc4 ["CALL", null, ["callee:00c57af0:8"]]
- 0047ee2c bytes 9d701d94
+ 004a1cc4 bytes 8bd71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b02c6013009c9757e3e5677bb6721ad"></a>

### [`0047efb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047efb4.md) → [`004a1e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1e4c.md) _ZNK5Botan7AES_2569encrypt_nEPKhPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047d7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047d7b0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

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
      "site": "004a1ee8",
      "value": [
        "leaf",
        "ram:c58240:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047f050",
      "value": [
        "leaf",
        "ram:bdb7f0:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1f0c",
      "incomplete_value": true,
      "site": "004a1f18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f074",
      "incomplete_value": true,
      "site": "0047f080",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
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
      "definition_site": "004a1f08",
      "incomplete_value": false,
      "site": "004a1f18",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0047f070",
      "incomplete_value": false,
      "site": "0047f080",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004a1ee8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb7f0"
      ]
    ],
    [
      "004a1f08",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004a1f0c",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a1ee8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58240"
      ]
    ],
    [
      "004a1f08",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a1f0c",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047efb4.md#insn-0047f050) · [`0047f080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047efb4.md#insn-0047f080) · [`0047f028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047efb4.md#insn-0047f028)
- 新版 [`004a1ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1e4c.md#insn-004a1ee8) · [`004a1f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1e4c.md#insn-004a1f18) · [`004a1ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1e4c.md#insn-004a1ec0)

~~~diff
- 0047f050 ["INT_ADD", "register:40f0:8", ["const:47f050:8", "const:4:8"]]
- 0047f050 ["CALL", null, ["ram:bdb7f0:8"]]
+ 004a1ee8 ["INT_ADD", "register:40f0:8", ["const:4a1ee8:8", "const:4:8"]]
+ 004a1ee8 ["CALL", null, ["ram:c58240:8"]]
- 0047f050 bytes e8711d94
+ 004a1ee8 bytes d6d81e94
- 0047f080 ["INT_ADD", "register:40f0:8", ["const:47f080:8", "const:4:8"]]
- 0047f080 ["CALL", null, ["callee:00c57b10:8"]]
+ 004a1f18 ["INT_ADD", "register:40f0:8", ["const:4a1f18:8", "const:4:8"]]
+ 004a1f18 ["CALL", null, ["callee:00c57b10:8"]]
- 0047f080 bytes 10701d94
+ 004a1f18 bytes fed61e94
- 0047f028 ["INT_ADD", "register:40f0:8", ["const:47f028:8", "const:4:8"]]
- 0047f028 ["CALL", null, ["callee:00c57af0:8"]]
+ 004a1ec0 ["INT_ADD", "register:40f0:8", ["const:4a1ec0:8", "const:4:8"]]
+ 004a1ec0 ["CALL", null, ["callee:00c57af0:8"]]
- 0047f028 bytes 1e701d94
+ 004a1ec0 bytes 0cd71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10b7df001963ae59595326e1ebacce20"></a>

### [`0047f0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f0d4.md) → [`004a1f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1f6c.md) _ZNK5Botan7AES_2569decrypt_nEPKhPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047de90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047d/0047de90.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

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
      "site": "004a2008",
      "value": [
        "leaf",
        "ram:c58240:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047f170",
      "value": [
        "leaf",
        "ram:bdb7f0:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a202c",
      "incomplete_value": true,
      "site": "004a2038",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f194",
      "incomplete_value": true,
      "site": "0047f1a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
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
      "definition_site": "004a2028",
      "incomplete_value": false,
      "site": "004a2038",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0047f190",
      "incomplete_value": false,
      "site": "0047f1a0",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004a2008",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb7f0"
      ]
    ],
    [
      "004a2028",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004a202c",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a2008",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58240"
      ]
    ],
    [
      "004a2028",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a202c",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f0d4.md#insn-0047f170) · [`0047f1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f0d4.md#insn-0047f1a0) · [`0047f148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f0d4.md#insn-0047f148)
- 新版 [`004a2008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1f6c.md#insn-004a2008) · [`004a2038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1f6c.md#insn-004a2038) · [`004a1fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1f6c.md#insn-004a1fe0)

~~~diff
- 0047f170 ["INT_ADD", "register:40f0:8", ["const:47f170:8", "const:4:8"]]
- 0047f170 ["CALL", null, ["ram:bdb7f0:8"]]
+ 004a2008 ["INT_ADD", "register:40f0:8", ["const:4a2008:8", "const:4:8"]]
+ 004a2008 ["CALL", null, ["ram:c58240:8"]]
- 0047f170 bytes a0711d94
+ 004a2008 bytes 8ed81e94
- 0047f1a0 ["INT_ADD", "register:40f0:8", ["const:47f1a0:8", "const:4:8"]]
- 0047f1a0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004a2038 ["INT_ADD", "register:40f0:8", ["const:4a2038:8", "const:4:8"]]
+ 004a2038 ["CALL", null, ["callee:00c57b10:8"]]
- 0047f1a0 bytes c86f1d94
+ 004a2038 bytes b6d61e94
- 0047f148 ["INT_ADD", "register:40f0:8", ["const:47f148:8", "const:4:8"]]
- 0047f148 ["CALL", null, ["callee:00c57af0:8"]]
+ 004a1fe0 ["INT_ADD", "register:40f0:8", ["const:4a1fe0:8", "const:4:8"]]
+ 004a1fe0 ["CALL", null, ["callee:00c57af0:8"]]
- 0047f148 bytes d66f1d94
+ 004a1fe0 bytes c4d61e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-290759a76fd7e070e242f5e67df765e4"></a>

### [`0047f2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f2d0.md) → [`004a2168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2168.md) _ZN5Botan19AlgorithmIdentifierC1ERKNS_3OIDERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5f0.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c59040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59040.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

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
      "definition_site": "004a21b0",
      "incomplete_value": true,
      "site": "004a21b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0047f318",
      "incomplete_value": true,
      "site": "0047f318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a21b0",
      "incomplete_value": true,
      "site": "004a21b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0047f318",
      "incomplete_value": true,
      "site": "0047f318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a2190",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004a219c",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "004a21b0",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a2190",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004a219c",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "004a21b0",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f2d0.md#insn-0047f2e8) · [`0047f2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f2d0.md#insn-0047f2ec) · [`0047f2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f2d0.md#insn-0047f2f8)
- 新版 [`004a2180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2168.md#insn-004a2180) · [`004a2184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2168.md#insn-004a2184) · [`004a2190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2168.md#insn-004a2190)

~~~diff
- 0047f2e8 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004a2180 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0047f2e8 bytes c83c00f0
+ 004a2180 bytes c83f0090
- 0047f2ec ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 004a2184 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 0047f2ec bytes c93c00f0
+ 004a2184 bytes c93f0090
- 0047f2f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
- 0047f2f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a2190 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:938:8"]]
+ 004a2190 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0047f2f8 bytes 08a547f9
+ 004a2190 bytes 089d44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4837a32f9b2228fb99985fdd45014295"></a>

### [`0047f40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f40c.md) → [`004a22a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a22a4.md) _ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdbfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfd0.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md)
- 新版 呼出元 1件 [`00c58a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a20.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a22d0",
      "incomplete_value": true,
      "site": "004a22d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0047f438",
      "incomplete_value": true,
      "site": "0047f438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a22c0",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004a22d0",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a22c0",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004a22d0",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f40c.md#insn-0047f41c) · [`0047f428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f40c.md#insn-0047f428) · [`0047f430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f40c.md#insn-0047f430)
- 新版 [`004a22b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a22a4.md#insn-004a22b4) · [`004a22c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a22a4.md#insn-004a22c0)

~~~diff
- 0047f41c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004a22b4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0047f41c bytes c83c00f0
+ 004a22b4 bytes c83f0090
- 0047f428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
- 0047f428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a22c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:938:8"]]
+ 004a22c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0047f428 bytes 08a547f9
+ 004a22c0 bytes 089d44f9
- 0047f430 ["COPY", "register:4040:8", ["register:4000:8"]]
- 0047f430 bytes e80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a454053d499709177ebb47500a4ddff9"></a>

### [`0047f4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f4d8.md) → [`004a2370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2370.md) _ZN5Botan4OIDS6lookupERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 26.47% / 新版 26.47%

CFGの説明率　旧版 24.79% / 新版 24.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 84件, `store_value` 12件, `unresolved_branch_alignment` 127件, `unresolved_call_alignment` 425件

アドレスに依存する影響 `call_argument_candidate` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a252c",
      "incomplete_value": true,
      "site": "004a253c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c8b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f694",
      "incomplete_value": true,
      "site": "0047f6a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:41e:8"
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
      "definition_site": "004a2540",
      "incomplete_value": true,
      "site": "004a2540",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0047f6a8",
      "incomplete_value": true,
      "site": "0047f6a8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a2594",
      "incomplete_value": true,
      "site": "004a25a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:102:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f6fc",
      "incomplete_value": true,
      "site": "0047f70c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:593:8"
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
      "004a24bc",
      "PARAM",
      [
        "storage",
        "00298ce5",
        null,
        "string"
      ]
    ],
    [
      "004a24c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0047f654"
      ]
    ],
    [
      "unmatched:0047f638",
      "PARAM",
      [
        "storage",
        "002aa515",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a24bc",
      "PARAM",
      [
        "storage",
        "002a8aa3",
        null,
        "string"
      ]
    ],
    [
      "004a24c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "004a24ec"
      ]
    ],
    [
      "004a24d0",
      "PARAM",
      [
        "storage",
        "002bb291",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f4d8.md#insn-0047f664) · [`0047f6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f4d8.md#insn-0047f6cc) · [`0047f768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f4d8.md#insn-0047f768)

~~~diff
- 0047f664 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 0047f664 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0047f664 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0047f664 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0047f664 bytes c0020036
- 0047f6cc ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 0047f6cc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0047f6cc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0047f6cc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0047f6cc bytes 60040036
- 0047f768 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 0047f768 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0047f768 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0047f768 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0047f768 bytes 40030036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4f80c3c3f4ef4ee4ab7d8bdc243399f"></a>

### [`00482154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482154.md) → [`004a4fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a4/004a4fec.md) _ZN5Botan19AlgorithmIdentifierC2ERKNS_3OIDENS0_15Encoding_OptionE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8d0.md) · 呼出先 5件 [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c59320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59320.md) · 呼出先 5件 [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a5034",
      "incomplete_value": true,
      "site": "004a5034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0048219c",
      "incomplete_value": true,
      "site": "0048219c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a5034",
      "incomplete_value": true,
      "site": "004a5034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0048219c",
      "incomplete_value": true,
      "site": "0048219c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a5014",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004a5020",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "004a5034",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a5014",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004a5020",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "004a5034",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048216c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482154.md#insn-0048216c) · [`00482170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482154.md#insn-00482170) · [`0048217c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482154.md#insn-0048217c)
- 新版 [`004a5004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a4/004a4fec.md#insn-004a5004) · [`004a5008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a4/004a4fec.md#insn-004a5008) · [`004a5014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a4/004a4fec.md#insn-004a5014)

~~~diff
- 0048216c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004a5004 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0048216c bytes c83c0090
+ 004a5004 bytes a83f00b0
- 00482170 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 004a5008 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00482170 bytes c93c0090
+ 004a5008 bytes a93f00b0
- 0048217c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
- 0048217c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5014 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:938:8"]]
+ 004a5014 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0048217c bytes 08a547f9
+ 004a5014 bytes 089d44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b6c78a80b7ab4583cad3ff62a87bbd1"></a>

### [`00482240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482240.md) → [`004a50d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a50d8.md) _ZN5Botan19AlgorithmIdentifierC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS0_15Encoding_OptionE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfc0.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md)
- 新版 呼出元 1件 [`00c58a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a10.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md)

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
      "definition_site": "004a50f4",
      "incomplete_value": true,
      "site": "004a50f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0048225c",
      "incomplete_value": true,
      "site": "00482260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a50f0",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004a50f8",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a50f0",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004a50f8",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048224c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482240.md#insn-0048224c) · [`00482258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482240.md#insn-00482258) · [`0048226c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482240.md#insn-0048226c)
- 新版 [`004a50e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a50d8.md#insn-004a50e4) · [`004a50f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a50d8.md#insn-004a50f0) · [`004a5104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a50d8.md#insn-004a5104)

~~~diff
- 0048224c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004a50e4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0048224c bytes c83c0090
+ 004a50e4 bytes a83f00b0
- 00482258 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
- 00482258 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a50f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:938:8"]]
+ 004a50f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00482258 bytes 08a547f9
+ 004a50f0 bytes 089d44f9
- 0048226c ["INT_ADD", "register:40f0:8", ["const:48226c:8", "const:4:8"]]
- 0048226c ["CALL", null, ["callee:00c58280:8"]]
+ 004a5104 ["INT_ADD", "register:40f0:8", ["const:4a5104:8", "const:4:8"]]
+ 004a5104 ["CALL", null, ["callee:00c58280:8"]]
- 0048226c bytes 71651d94
+ 004a5104 bytes 5fcc1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77564c9b4be87aca8ffbbcc45c83955b"></a>

### [`00482500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482500.md) → [`004a5398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5398.md) _ZN5Botan11DER_Encoder10start_consENS_8ASN1_TagES1_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb860.md) · 呼出先 6件 [`005200b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/005200b0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb890.md)
- 新版 呼出元 1件 [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md) · 呼出先 6件 [`00542f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542f48.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c582e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582e0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.63% / 新版 96.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a53c4",
      "value": [
        "leaf",
        "ram:c582e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048252c",
      "value": [
        "leaf",
        "ram:bdb890:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a5480",
      "incomplete_value": true,
      "site": "004a5480",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004825e8",
      "incomplete_value": true,
      "site": "004825e8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "definition_site": "004a54c0",
      "incomplete_value": true,
      "site": "004a54c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00482628",
      "incomplete_value": true,
      "site": "00482628",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
      "004a53c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb890"
      ]
    ],
    [
      "004a5470",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004a54b0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a53c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c582e0"
      ]
    ],
    [
      "004a5470",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004a54b0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048252c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482500.md#insn-0048252c) · [`004825e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482500.md#insn-004825e8) · [`00482628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482500.md#insn-00482628)
- 新版 [`004a53c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5398.md#insn-004a53c4) · [`004a5480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5398.md#insn-004a5480) · [`004a54c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5398.md#insn-004a54c0)

~~~diff
- 0048252c ["INT_ADD", "register:40f0:8", ["const:48252c:8", "const:4:8"]]
- 0048252c ["CALL", null, ["ram:bdb890:8"]]
+ 004a53c4 ["INT_ADD", "register:40f0:8", ["const:4a53c4:8", "const:4:8"]]
+ 004a53c4 ["CALL", null, ["ram:c582e0:8"]]
- 0048252c bytes d9641d94
+ 004a53c4 bytes c7cb1e94
- 004825e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004825e8 ["INT_ADD", "register:40f0:8", ["const:4825e8:8", "const:4:8"]]
- 004825e8 ["CALLIND", null, ["register:0:8"]]
+ 004a5480 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a5480 ["INT_ADD", "register:40f0:8", ["const:4a5480:8", "const:4:8"]]
+ 004a5480 ["CALLIND", null, ["register:0:8"]]
- 004825e8 bytes 20013fd6
+ 004a5480 bytes 20013fd6
- 00482628 ["COPY", "register:0:8", ["register:4048:8"]]
- 00482628 ["INT_ADD", "register:40f0:8", ["const:482628:8", "const:4:8"]]
- 00482628 ["CALLIND", null, ["register:0:8"]]
+ 004a54c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a54c0 ["INT_ADD", "register:40f0:8", ["const:4a54c0:8", "const:4:8"]]
+ 004a54c0 ["CALLIND", null, ["register:0:8"]]
- 00482628 bytes 20013fd6
+ 004a54c0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fceeae812aac7d9ffc08a8f28a2b230"></a>

### [`004826c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004826c4.md) → [`004a555c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a555c.md) _ZN5Botan11DER_Encoder8end_consEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb880.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md)
- 新版 呼出元 1件 [`00c582d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582d0.md) · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.94% / 新版 97.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a564c",
      "incomplete_value": true,
      "site": "004a564c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004827b4",
      "incomplete_value": true,
      "site": "004827b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
      "definition_site": "004a5694",
      "incomplete_value": false,
      "site": "004a569c",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004827fc",
      "incomplete_value": false,
      "site": "00482804",
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
            "const:46a:8"
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
      "definition_site": "004a56cc",
      "incomplete_value": true,
      "site": "004a56d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00482834",
      "incomplete_value": true,
      "site": "00482840",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
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
      "004a563c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004a5694",
      "PARAM",
      [
        "storage",
        "002a546a",
        null,
        "string"
      ]
    ],
    [
      "004a56c8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a563c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004a5694",
      "PARAM",
      [
        "storage",
        "002b5e98",
        null,
        "string"
      ]
    ],
    [
      "004a56c8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004827b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004826c4.md#insn-004827b4) · [`00482804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004826c4.md#insn-00482804) · [`00482840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004826c4.md#insn-00482840)
- 新版 [`004a564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a555c.md#insn-004a564c) · [`004a569c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a555c.md#insn-004a569c) · [`004a56d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a555c.md#insn-004a56d8)

~~~diff
- 004827b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004827b4 ["INT_ADD", "register:40f0:8", ["const:4827b4:8", "const:4:8"]]
- 004827b4 ["CALLIND", null, ["register:0:8"]]
+ 004a564c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a564c ["INT_ADD", "register:40f0:8", ["const:4a564c:8", "const:4:8"]]
+ 004a564c ["CALLIND", null, ["register:0:8"]]
- 004827b4 bytes 20013fd6
+ 004a564c bytes 20013fd6
- 00482804 ["INT_ADD", "register:40f0:8", ["const:482804:8", "const:4:8"]]
- 00482804 ["CALL", null, ["callee:0043dd98:8"]]
+ 004a569c ["INT_ADD", "register:40f0:8", ["const:4a569c:8", "const:4:8"]]
+ 004a569c ["CALL", null, ["callee:0043dd98:8"]]
- 00482804 bytes a562fe97
+ 004a569c bytes bf61fe97
- 00482840 ["INT_ADD", "register:40f0:8", ["const:482840:8", "const:4:8"]]
- 00482840 ["CALL", null, ["callee:00c57b10:8"]]
+ 004a56d8 ["INT_ADD", "register:40f0:8", ["const:4a56d8:8", "const:4:8"]]
+ 004a56d8 ["CALL", null, ["callee:00c57b10:8"]]
- 00482840 bytes 20621d94
+ 004a56d8 bytes 0ec91e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a76a85da5edaa9482a8f313ad0808c38"></a>

### [`00482990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482990.md) → [`004a5828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5828.md) _ZN5Botan11BER_Decoder10start_consENS_8ASN1_TagES1_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md) · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8d0.md) [`00bdb8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8e0.md) [`00bdb8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8f0.md)
- 新版 呼出元 1件 [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md) · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58320.md) [`00c58330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58330.md) [`00c58340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58340.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a5880",
      "value": [
        "leaf",
        "ram:c58340:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004829e8",
      "value": [
        "leaf",
        "ram:bdb8f0:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a58ac",
      "incomplete_value": true,
      "site": "004a58ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00482a14",
      "incomplete_value": true,
      "site": "00482a14",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
      "004a5880",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb8f0"
      ]
    ],
    [
      "004a589c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a5880",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58340"
      ]
    ],
    [
      "004a589c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004829e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482990.md#insn-004829e8) · [`00482a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482990.md#insn-00482a14) · [`004829c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482990.md#insn-004829c8)
- 新版 [`004a5880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5828.md#insn-004a5880) · [`004a58ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5828.md#insn-004a58ac) · [`004a5860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5828.md#insn-004a5860)

~~~diff
- 004829e8 ["INT_ADD", "register:40f0:8", ["const:4829e8:8", "const:4:8"]]
- 004829e8 ["CALL", null, ["ram:bdb8f0:8"]]
+ 004a5880 ["INT_ADD", "register:40f0:8", ["const:4a5880:8", "const:4:8"]]
+ 004a5880 ["CALL", null, ["ram:c58340:8"]]
- 004829e8 bytes c2631d94
+ 004a5880 bytes b0ca1e94
- 00482a14 ["COPY", "register:0:8", ["register:4048:8"]]
- 00482a14 ["INT_ADD", "register:40f0:8", ["const:482a14:8", "const:4:8"]]
- 00482a14 ["CALLIND", null, ["register:0:8"]]
+ 004a58ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a58ac ["INT_ADD", "register:40f0:8", ["const:4a58ac:8", "const:4:8"]]
+ 004a58ac ["CALLIND", null, ["register:0:8"]]
- 00482a14 bytes 20013fd6
+ 004a58ac bytes 20013fd6
- 004829c8 ["INT_ADD", "register:40f0:8", ["const:4829c8:8", "const:4:8"]]
- 004829c8 ["CALL", null, ["callee:00c58320:8"]]
+ 004a5860 ["INT_ADD", "register:40f0:8", ["const:4a5860:8", "const:4:8"]]
+ 004a5860 ["CALL", null, ["callee:00c58320:8"]]
- 004829c8 bytes c2631d94
+ 004a5860 bytes b0ca1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02bf5a36d15f83dfc1c33e4e0f3db560"></a>

### [`00482c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482c08.md) → [`004a5aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5aa0.md) _ZN5Botan11BER_Decoder8end_consEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8c0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58310.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.67% / 新版 94.67%

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
      "definition_site": "004a5b1c",
      "incomplete_value": false,
      "site": "004a5b24",
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
            "const:b32:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00482c84",
      "incomplete_value": false,
      "site": "00482c8c",
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
            "const:80c:8"
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
      "definition_site": "004a5b58",
      "incomplete_value": true,
      "site": "004a5b64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00482cc0",
      "incomplete_value": true,
      "site": "00482ccc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
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
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a5b54",
      "incomplete_value": false,
      "site": "004a5b64",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00482cbc",
      "incomplete_value": false,
      "site": "00482ccc",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a5b1c",
      "PARAM",
      [
        "storage",
        "002ad80c",
        null,
        "string"
      ]
    ],
    [
      "004a5b54",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004a5b58",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a5b1c",
      "PARAM",
      [
        "storage",
        "002beb32",
        null,
        "string"
      ]
    ],
    [
      "004a5b54",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a5b58",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00482c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482c08.md#insn-00482c8c) · [`00482ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482c08.md#insn-00482ccc) · [`00482cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482c08.md#insn-00482cf0)
- 新版 [`004a5b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5aa0.md#insn-004a5b24) · [`004a5b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5aa0.md#insn-004a5b64) · [`004a5b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5aa0.md#insn-004a5b88)

~~~diff
- 00482c8c ["INT_ADD", "register:40f0:8", ["const:482c8c:8", "const:4:8"]]
- 00482c8c ["CALL", null, ["callee:0043dd98:8"]]
+ 004a5b24 ["INT_ADD", "register:40f0:8", ["const:4a5b24:8", "const:4:8"]]
+ 004a5b24 ["CALL", null, ["callee:0043dd98:8"]]
- 00482c8c bytes 8361fe97
+ 004a5b24 bytes 9d60fe97
- 00482ccc ["INT_ADD", "register:40f0:8", ["const:482ccc:8", "const:4:8"]]
- 00482ccc ["CALL", null, ["callee:00c57b10:8"]]
+ 004a5b64 ["INT_ADD", "register:40f0:8", ["const:4a5b64:8", "const:4:8"]]
+ 004a5b64 ["CALL", null, ["callee:00c57b10:8"]]
- 00482ccc bytes fd601d94
+ 004a5b64 bytes ebc71e94
- 00482cf0 ["INT_ADD", "register:40f0:8", ["const:482cf0:8", "const:4:8"]]
- 00482cf0 ["CALL", null, ["callee:0043dd98:8"]]
+ 004a5b88 ["INT_ADD", "register:40f0:8", ["const:4a5b88:8", "const:4:8"]]
+ 004a5b88 ["CALL", null, ["callee:0043dd98:8"]]
- 00482cf0 bytes 6a61fe97
+ 004a5b88 bytes 8460fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61f510022ded63589024b26502932191"></a>

### [`00482df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482df4.md) → [`004a5c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5c8c.md) _ZN5Botan9AttributeC2ERKNS_3OIDERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

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
      "definition_site": "004a5cd4",
      "incomplete_value": true,
      "site": "004a5cd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00482e3c",
      "incomplete_value": true,
      "site": "00482e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a5cd4",
      "incomplete_value": true,
      "site": "004a5cd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00482e3c",
      "incomplete_value": true,
      "site": "00482e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a5cb4",
      "READ",
      [
        "storage",
        "00c1af68",
        null,
        "pointer"
      ]
    ],
    [
      "004a5cc0",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "004a5cd4",
      "DATA",
      [
        "storage",
        "00be9218",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a5cb4",
      "READ",
      [
        "storage",
        "00c9a958",
        null,
        "pointer"
      ]
    ],
    [
      "004a5cc0",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "004a5cd4",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00482e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482df4.md#insn-00482e0c) · [`00482e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482df4.md#insn-00482e10) · [`00482e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482df4.md#insn-00482e1c)
- 新版 [`004a5ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5c8c.md#insn-004a5ca4) · [`004a5ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5c8c.md#insn-004a5ca8) · [`004a5cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5c8c.md#insn-004a5cb4)

~~~diff
- 00482e0c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004a5ca4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00482e0c bytes c83c0090
+ 004a5ca4 bytes a83f00b0
- 00482e10 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 004a5ca8 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00482e10 bytes c93c0090
+ 004a5ca8 bytes a93f00b0
- 00482e1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f68:8"]]
- 00482e1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5cb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:958:8"]]
+ 004a5cb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00482e1c bytes 08b547f9
+ 004a5cb4 bytes 08ad44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaa79aff5d70cfa4ec8e81be085796b2"></a>

### [`00482f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482f18.md) → [`004a5db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5db0.md) _ZN5Botan9AttributeC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdd110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd110.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md)
- 新版 呼出元 1件 [`00c59b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b60.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a5ddc",
      "incomplete_value": true,
      "site": "004a5ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00482f44",
      "incomplete_value": true,
      "site": "00482f44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a5dcc",
      "READ",
      [
        "storage",
        "00c1af68",
        null,
        "pointer"
      ]
    ],
    [
      "004a5ddc",
      "DATA",
      [
        "storage",
        "00be9218",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a5dcc",
      "READ",
      [
        "storage",
        "00c9a958",
        null,
        "pointer"
      ]
    ],
    [
      "004a5ddc",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00482f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482f18.md#insn-00482f28) · [`00482f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482f18.md#insn-00482f34) · [`00482f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482f18.md#insn-00482f3c)
- 新版 [`004a5dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5db0.md#insn-004a5dc0) · [`004a5dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5db0.md#insn-004a5dcc)

~~~diff
- 00482f28 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004a5dc0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00482f28 bytes c83c0090
+ 004a5dc0 bytes a83f00b0
- 00482f34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f68:8"]]
- 00482f34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5dcc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:958:8"]]
+ 004a5dcc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00482f34 bytes 08b547f9
+ 004a5dcc bytes 08ad44f9
- 00482f3c ["COPY", "register:4040:8", ["register:4000:8"]]
- 00482f3c bytes e80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3984ab9e7ff63383aa031ed6ab2acc11"></a>

### [`004830c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004830c8.md) → [`004a5f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5f60.md) _ZN5Botan9Attribute11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004eb16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb16c.md) · 呼出先 6件 [`00482aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482aa8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md) [`00bdb8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8c0.md)
- 新版 呼出元 1件 [`0050e004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md) · 呼出先 6件 [`004a5940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md) [`00c58310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58310.md)

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
      "definition_site": "004a6010",
      "incomplete_value": true,
      "site": "004a6010",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "00483178",
      "incomplete_value": true,
      "site": "00483178",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a6054",
      "incomplete_value": true,
      "site": "004a6054",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004831bc",
      "incomplete_value": true,
      "site": "004831bc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "004a6000",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004a6044",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a6000",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004a6044",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00483178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004830c8.md#insn-00483178) · [`004831bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004830c8.md#insn-004831bc) · [`004830fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004830c8.md#insn-004830fc)
- 新版 [`004a6010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5f60.md#insn-004a6010) · [`004a6054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5f60.md#insn-004a6054) · [`004a5f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5f60.md#insn-004a5f94)

~~~diff
- 00483178 ["COPY", "register:0:8", ["register:4048:8"]]
- 00483178 ["INT_ADD", "register:40f0:8", ["const:483178:8", "const:4:8"]]
- 00483178 ["CALLIND", null, ["register:0:8"]]
+ 004a6010 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a6010 ["INT_ADD", "register:40f0:8", ["const:4a6010:8", "const:4:8"]]
+ 004a6010 ["CALLIND", null, ["register:0:8"]]
- 00483178 bytes 20013fd6
+ 004a6010 bytes 20013fd6
- 004831bc ["COPY", "register:0:8", ["register:4048:8"]]
- 004831bc ["INT_ADD", "register:40f0:8", ["const:4831bc:8", "const:4:8"]]
- 004831bc ["CALLIND", null, ["register:0:8"]]
+ 004a6054 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a6054 ["INT_ADD", "register:40f0:8", ["const:4a6054:8", "const:4:8"]]
+ 004a6054 ["CALLIND", null, ["register:0:8"]]
- 004831bc bytes 20013fd6
+ 004a6054 bytes 20013fd6
- 004830fc ["INT_ADD", "register:40f0:8", ["const:4830fc:8", "const:4:8"]]
- 004830fc ["CALL", null, ["callee:00c58300:8"]]
+ 004a5f94 ["INT_ADD", "register:40f0:8", ["const:4a5f94:8", "const:4:8"]]
+ 004a5f94 ["CALL", null, ["callee:00c58300:8"]]
- 004830fc bytes ed611d94
+ 004a5f94 bytes dbc81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aad580923581924f68a8d2f0181d4738"></a>

### [`0048322c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/0048322c.md) → [`004a60c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a60c4.md) _ZN5Botan18asn1_tag_to_stringENS_8ASN1_TagE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb910.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb310.md)
- 新版 呼出元 1件 [`00c58360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58360.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.65% / 新版 88.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a61e0",
      "incomplete_value": true,
      "site": "004a61e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:383:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483348",
      "incomplete_value": true,
      "site": "00483348",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:84e:8"
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
      "definition_site": "004a62b8",
      "incomplete_value": true,
      "site": "004a62b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:924:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483420",
      "incomplete_value": true,
      "site": "00483420",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:24a:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6200",
      "incomplete_value": false,
      "site": "004a620c",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483368",
      "incomplete_value": false,
      "site": "00483374",
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
            "const:156:8"
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
      "004a60f8",
      "DATA",
      [
        "storage",
        "002b9008",
        "switchD_00483268::switchdataD_002b9008",
        "byte"
      ]
    ],
    [
      "004a61cc",
      "READ",
      [
        "storage",
        "0029684e",
        null,
        "string"
      ]
    ],
    [
      "004a6200",
      "PARAM",
      [
        "storage",
        "002a8156",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a60f8",
      "DATA",
      [
        "storage",
        "002ca718",
        "switchD_004a6100::switchdataD_002ca718",
        "byte"
      ]
    ],
    [
      "004a61cc",
      "READ",
      [
        "storage",
        "002a6383",
        null,
        "string"
      ]
    ],
    [
      "004a6200",
      "PARAM",
      [
        "storage",
        "002b8df8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00483374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/0048322c.md#insn-00483374) · [`0048339c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/0048322c.md#insn-0048339c) · [`00483254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/0048322c.md#insn-00483254)
- 新版 [`004a620c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a60c4.md#insn-004a620c) · [`004a6234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a60c4.md#insn-004a6234) · [`004a60ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a60c4.md#insn-004a60ec)

~~~diff
- 00483374 ["INT_ADD", "register:40f0:8", ["const:483374:8", "const:4:8"]]
- 00483374 ["CALL", null, ["callee:00c57b60:8"]]
+ 004a620c ["INT_ADD", "register:40f0:8", ["const:4a620c:8", "const:4:8"]]
+ 004a620c ["CALL", null, ["callee:00c57b60:8"]]
- 00483374 bytes 675f1d94
+ 004a620c bytes 55c61e94
- 0048339c ["INT_ADD", "register:40f0:8", ["const:48339c:8", "const:4:8"]]
- 0048339c ["CALL", null, ["callee:00c57b70:8"]]
+ 004a6234 ["INT_ADD", "register:40f0:8", ["const:4a6234:8", "const:4:8"]]
+ 004a6234 ["CALL", null, ["callee:00c57b70:8"]]
- 0048339c bytes 615f1d94
+ 004a6234 bytes 4fc61e94
- 00483254 ["COPY", "register:4050:8", ["const:2b9000:8"]]
+ 004a60ec ["COPY", "register:4050:8", ["const:2ca000:8"]]
- 00483254 bytes aaf1ffd0
+ 004a60ec bytes 2af1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b82d86851063c02028eeeff5cadc541c"></a>

### [`00483554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483554.md) → [`004a63ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a63ec.md) _ZN5Botan18BER_Decoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bdb920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb920.md) [`00bdba00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba00.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 2件 [`00c58370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58370.md) [`00c58450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58450.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a6450",
      "incomplete_value": true,
      "site": "004a6454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004835b8",
      "incomplete_value": true,
      "site": "004835bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a6470",
      "incomplete_value": true,
      "site": "004a6474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004835d8",
      "incomplete_value": true,
      "site": "004835dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a648c",
      "incomplete_value": true,
      "site": "004a6490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004835f4",
      "incomplete_value": true,
      "site": "004835f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004a6408",
      "PARAM",
      [
        "storage",
        "00293762",
        null,
        "string"
      ]
    ],
    [
      "004a6420",
      "PARAM",
      [
        "storage",
        "002ae900",
        null,
        "string"
      ]
    ],
    [
      "004a6434",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a6408",
      "PARAM",
      [
        "storage",
        "002a2f5b",
        null,
        "string"
      ]
    ],
    [
      "004a6420",
      "PARAM",
      [
        "storage",
        "002bfde4",
        null,
        "string"
      ]
    ],
    [
      "004a6434",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00483580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483554.md#insn-00483580) · [`00483594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483554.md#insn-00483594) · [`004835a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483554.md#insn-004835a8)
- 新版 [`004a6418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a63ec.md#insn-004a6418) · [`004a642c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a63ec.md#insn-004a642c) · [`004a6440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a63ec.md#insn-004a6440)

~~~diff
- 00483580 ["INT_ADD", "register:40f0:8", ["const:483580:8", "const:4:8"]]
- 00483580 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004a6418 ["INT_ADD", "register:40f0:8", ["const:4a6418:8", "const:4:8"]]
+ 004a6418 ["CALL", null, ["callee:00c57cb0:8"]]
- 00483580 bytes 385f1d94
+ 004a6418 bytes 26c61e94
- 00483594 ["INT_ADD", "register:40f0:8", ["const:483594:8", "const:4:8"]]
- 00483594 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004a642c ["INT_ADD", "register:40f0:8", ["const:4a642c:8", "const:4:8"]]
+ 004a642c ["CALL", null, ["callee:00c57cb0:8"]]
- 00483594 bytes 335f1d94
+ 004a642c bytes 21c61e94
- 004835a8 ["INT_ADD", "register:40f0:8", ["const:4835a8:8", "const:4:8"]]
- 004835a8 ["CALL", null, ["ram:bdb930:8"]]
+ 004a6440 ["INT_ADD", "register:40f0:8", ["const:4a6440:8", "const:4:8"]]
+ 004a6440 ["CALL", null, ["ram:c58380:8"]]
- 004835a8 bytes e2601d94
+ 004a6440 bytes d0c71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8441ea509c488f5404e80304eb4743cf"></a>

### [`00483664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483664.md) → [`004a64fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a64fc.md) _ZN5Botan14Decoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb900.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`00c58350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58350.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a654c",
      "incomplete_value": true,
      "site": "004a6550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004836b4",
      "incomplete_value": true,
      "site": "004836b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a6568",
      "incomplete_value": true,
      "site": "004a656c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004836d0",
      "incomplete_value": true,
      "site": "004836d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6518",
      "incomplete_value": false,
      "site": "004a6528",
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
            "const:de4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483680",
      "incomplete_value": false,
      "site": "00483690",
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
            "const:900:8"
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
      "004a6518",
      "PARAM",
      [
        "storage",
        "002ae900",
        null,
        "string"
      ]
    ],
    [
      "004a6530",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "004a653c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb930"
      ]
    ]
  ],
  "added": [
    [
      "004a6518",
      "PARAM",
      [
        "storage",
        "002bfde4",
        null,
        "string"
      ]
    ],
    [
      "004a6530",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      "004a653c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58380"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00483690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483664.md#insn-00483690) · [`004836a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483664.md#insn-004836a4) · [`0048367c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483664.md#insn-0048367c)
- 新版 [`004a6528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a64fc.md#insn-004a6528) · [`004a653c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a64fc.md#insn-004a653c) · [`004a6514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a64fc.md#insn-004a6514)

~~~diff
- 00483690 ["INT_ADD", "register:40f0:8", ["const:483690:8", "const:4:8"]]
- 00483690 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004a6528 ["INT_ADD", "register:40f0:8", ["const:4a6528:8", "const:4:8"]]
+ 004a6528 ["CALL", null, ["callee:00c57cb0:8"]]
- 00483690 bytes f45e1d94
+ 004a6528 bytes e2c51e94
- 004836a4 ["INT_ADD", "register:40f0:8", ["const:4836a4:8", "const:4:8"]]
- 004836a4 ["CALL", null, ["ram:bdb930:8"]]
+ 004a653c ["INT_ADD", "register:40f0:8", ["const:4a653c:8", "const:4:8"]]
+ 004a653c ["CALL", null, ["ram:c58380:8"]]
- 004836a4 bytes a3601d94
+ 004a653c bytes 91c71e94
- 0048367c ["COPY", "register:4000:8", ["const:2ae000:8"]]
+ 004a6514 ["COPY", "register:4000:8", ["const:2bf000:8"]]
- 0048367c bytes 40f1fff0
+ 004a6514 bytes c0f0ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba9b5de597e261db17e956196471fe7d"></a>

### [`00483728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483728.md) → [`004a65c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a65c0.md) _ZN5Botan11BER_Bad_TagC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbca0.md) · 呼出先 8件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c586f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586f0.md) · 呼出先 8件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.13% / 新版 99.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a6714",
      "incomplete_value": true,
      "site": "004a6718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0048387c",
      "incomplete_value": true,
      "site": "00483880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a66e8",
      "value": [
        "leaf",
        "ram:c58370:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00483850",
      "value": [
        "leaf",
        "ram:bdb920:8"
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
      "004a66e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb920"
      ]
    ],
    [
      "004a6710",
      "READ",
      [
        "storage",
        "00c1af88",
        null,
        "pointer"
      ]
    ],
    [
      "004a6718",
      "DATA",
      [
        "storage",
        "00be9270",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004a66e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58370"
      ]
    ],
    [
      "004a6710",
      "READ",
      [
        "storage",
        "00c9a978",
        null,
        "pointer"
      ]
    ],
    [
      "004a6718",
      "DATA",
      [
        "storage",
        "00c65e30",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00483850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483728.md#insn-00483850) · [`004837c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483728.md#insn-004837c4) · [`004837ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483728.md#insn-004837ec)
- 新版 [`004a66e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a65c0.md#insn-004a66e8) · [`004a665c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a65c0.md#insn-004a665c) · [`004a6684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a65c0.md#insn-004a6684)

~~~diff
- 00483850 ["INT_ADD", "register:40f0:8", ["const:483850:8", "const:4:8"]]
- 00483850 ["CALL", null, ["ram:bdb920:8"]]
+ 004a66e8 ["INT_ADD", "register:40f0:8", ["const:4a66e8:8", "const:4:8"]]
+ 004a66e8 ["CALL", null, ["ram:c58370:8"]]
- 00483850 bytes 34601d94
+ 004a66e8 bytes 22c71e94
- 004837c4 ["INT_ADD", "register:40f0:8", ["const:4837c4:8", "const:4:8"]]
- 004837c4 ["CALL", null, ["callee:00c57a90:8"]]
+ 004a665c ["INT_ADD", "register:40f0:8", ["const:4a665c:8", "const:4:8"]]
+ 004a665c ["CALL", null, ["callee:00c57a90:8"]]
- 004837c4 bytes 1f5e1d94
+ 004a665c bytes 0dc51e94
- 004837ec ["INT_ADD", "register:40f0:8", ["const:4837ec:8", "const:4:8"]]
- 004837ec ["CALL", null, ["callee:00c57b40:8"]]
+ 004a6684 ["INT_ADD", "register:40f0:8", ["const:4a6684:8", "const:4:8"]]
+ 004a6684 ["CALL", null, ["callee:00c57b40:8"]]
- 004837ec bytes 415e1d94
+ 004a6684 bytes 2fc51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d535c588cdb91242a6160e6bda63e00"></a>

### [`004839c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004839c4.md) → [`004a685c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a685c.md) _ZN5Botan11BER_Bad_TagC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagESA_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9f0.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c58440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58440.md) · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a6a3c",
      "incomplete_value": true,
      "site": "004a6a40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00483ba4",
      "incomplete_value": true,
      "site": "00483ba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6984",
      "incomplete_value": false,
      "site": "004a698c",
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
            "const:276:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483aec",
      "incomplete_value": false,
      "site": "00483af4",
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
            "const:83d:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a69f8",
      "value": [
        "leaf",
        "ram:c58370:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00483b60",
      "value": [
        "leaf",
        "ram:bdb920:8"
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
      "004a6984",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ],
    [
      "004a69f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb920"
      ]
    ],
    [
      "004a6a38",
      "READ",
      [
        "storage",
        "00c1af88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a6984",
      "PARAM",
      [
        "storage",
        "002a5276",
        null,
        null
      ]
    ],
    [
      "004a69f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58370"
      ]
    ],
    [
      "004a6a38",
      "READ",
      [
        "storage",
        "00c9a978",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00483af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004839c4.md#insn-00483af4) · [`00483b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004839c4.md#insn-00483b60) · [`00483a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004839c4.md#insn-00483a64)
- 新版 [`004a698c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a685c.md#insn-004a698c) · [`004a69f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a685c.md#insn-004a69f8) · [`004a68fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a685c.md#insn-004a68fc)

~~~diff
- 00483af4 ["INT_ADD", "register:40f0:8", ["const:483af4:8", "const:4:8"]]
- 00483af4 ["CALL", null, ["callee:00c57b70:8"]]
+ 004a698c ["INT_ADD", "register:40f0:8", ["const:4a698c:8", "const:4:8"]]
+ 004a698c ["CALL", null, ["callee:00c57b70:8"]]
- 00483af4 bytes 8b5d1d94
+ 004a698c bytes 79c41e94
- 00483b60 ["INT_ADD", "register:40f0:8", ["const:483b60:8", "const:4:8"]]
- 00483b60 ["CALL", null, ["ram:bdb920:8"]]
+ 004a69f8 ["INT_ADD", "register:40f0:8", ["const:4a69f8:8", "const:4:8"]]
+ 004a69f8 ["CALL", null, ["ram:c58370:8"]]
- 00483b60 bytes 705f1d94
+ 004a69f8 bytes 5ec61e94
- 00483a64 ["INT_ADD", "register:40f0:8", ["const:483a64:8", "const:4:8"]]
- 00483a64 ["CALL", null, ["callee:00c57a90:8"]]
+ 004a68fc ["INT_ADD", "register:40f0:8", ["const:4a68fc:8", "const:4:8"]]
+ 004a68fc ["CALL", null, ["callee:00c57a90:8"]]
- 00483a64 bytes 775d1d94
+ 004a68fc bytes 65c41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78f63badf007345635999ce1060a544f"></a>

### [`004840c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/004840c4.md) → [`004a6f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md) FUN_004a6f5c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`004ce004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md) [`004ea660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea660.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 3件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`004f0e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0e9c.md) [`0050d4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d4f8.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6ffc",
      "incomplete_value": false,
      "site": "004a7004",
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
            "const:b7e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00484164",
      "incomplete_value": false,
      "site": "0048416c",
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
            "const:311:8"
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
      "definition_site": "004a7038",
      "incomplete_value": true,
      "site": "004a7044",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:980:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004841a0",
      "incomplete_value": true,
      "site": "004841ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f90:8"
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
      "definition_site": "004a7034",
      "incomplete_value": false,
      "site": "004a7044",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0048419c",
      "incomplete_value": false,
      "site": "004841ac",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004a6ffc",
      "PARAM",
      [
        "storage",
        "002a4311",
        null,
        "string"
      ]
    ],
    [
      "004a7034",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004a7038",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a6ffc",
      "PARAM",
      [
        "storage",
        "002b4b7e",
        null,
        "string"
      ]
    ],
    [
      "004a7034",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a7038",
      "READ",
      [
        "storage",
        "00c9a980",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048416c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/004840c4.md#insn-0048416c) · [`004841ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/004840c4.md#insn-004841ac) · [`004841e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/004840c4.md#insn-004841e8)
- 新版 [`004a7004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md#insn-004a7004) · [`004a7044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md#insn-004a7044) · [`004a7080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md#insn-004a7080)

~~~diff
- 0048416c ["INT_ADD", "register:40f0:8", ["const:48416c:8", "const:4:8"]]
- 0048416c ["CALL", null, ["callee:0043dd98:8"]]
+ 004a7004 ["INT_ADD", "register:40f0:8", ["const:4a7004:8", "const:4:8"]]
+ 004a7004 ["CALL", null, ["callee:0043dd98:8"]]
- 0048416c bytes 4b5cfe97
+ 004a7004 bytes 655bfe97
- 004841ac ["INT_ADD", "register:40f0:8", ["const:4841ac:8", "const:4:8"]]
- 004841ac ["CALL", null, ["callee:00c57b10:8"]]
+ 004a7044 ["INT_ADD", "register:40f0:8", ["const:4a7044:8", "const:4:8"]]
+ 004a7044 ["CALL", null, ["callee:00c57b10:8"]]
- 004841ac bytes c55b1d94
+ 004a7044 bytes b3c21e94
- 004841e8 ["INT_ADD", "register:40f0:8", ["const:4841e8:8", "const:4:8"]]
- 004841e8 ["CALL", null, ["callee:00c58250:8"]]
+ 004a7080 ["INT_ADD", "register:40f0:8", ["const:4a7080:8", "const:4:8"]]
+ 004a7080 ["CALL", null, ["callee:00c58250:8"]]
- 004841e8 bytes 865d1d94
+ 004a7080 bytes 74c41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a40822476e4f90f82df23e4854384212"></a>

### [`00484260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484260.md) → [`004a70f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a70f8.md) _ZN5Botan17assertion_failureEPKcS1_S1_S1_i

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md) · 呼出先 11件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md) · 呼出先 11件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 85.62% / 新版 85.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a7140",
      "incomplete_value": true,
      "site": "004a7150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004842a8",
      "incomplete_value": true,
      "site": "004842b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004a7148",
      "incomplete_value": true,
      "site": "004a715c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004842b0",
      "incomplete_value": true,
      "site": "004842c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a7164",
      "incomplete_value": true,
      "site": "004a7164",
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
                "const:28:8"
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
      "definition_site": "004842cc",
      "incomplete_value": true,
      "site": "004842cc",
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
                "const:28:8"
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
      "004a712c",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "004a7130",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "004a7148",
      "READ",
      [
        "storage",
        "00c13460",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004a712c",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "004a7130",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "004a7148",
      "READ",
      [
        "storage",
        "00c92e08",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00484338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484260.md#insn-00484338) · [`00484384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484260.md#insn-00484384) · [`004843b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484260.md#insn-004843b0)
- 新版 [`004a71d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a70f8.md#insn-004a71d0) · [`004a721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a70f8.md#insn-004a721c) · [`004a7248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a70f8.md#insn-004a7248)

~~~diff
- 00484338 ["INT_ADD", "register:40f0:8", ["const:484338:8", "const:4:8"]]
- 00484338 ["CALL", null, ["callee:00459490:8"]]
+ 004a71d0 ["INT_ADD", "register:40f0:8", ["const:4a71d0:8", "const:4:8"]]
+ 004a71d0 ["CALL", null, ["callee:00459490:8"]]
- 00484338 bytes b0c8fe97
+ 004a71d0 bytes b0c8fe97
- 00484384 ["INT_ADD", "register:40f0:8", ["const:484384:8", "const:4:8"]]
- 00484384 ["CALL", null, ["callee:00459490:8"]]
+ 004a721c ["INT_ADD", "register:40f0:8", ["const:4a721c:8", "const:4:8"]]
+ 004a721c ["CALL", null, ["callee:00459490:8"]]
- 00484384 bytes 9dc8fe97
+ 004a721c bytes 9dc8fe97
- 004843b0 ["INT_ADD", "register:40f0:8", ["const:4843b0:8", "const:4:8"]]
- 004843b0 ["CALL", null, ["callee:00459490:8"]]
+ 004a7248 ["INT_ADD", "register:40f0:8", ["const:4a7248:8", "const:4:8"]]
+ 004a7248 ["CALL", null, ["callee:00459490:8"]]
- 004843b0 bytes 92c8fe97
+ 004a7248 bytes 92c8fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

