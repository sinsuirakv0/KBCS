# v15.7.4 → v16.0.0 · 最優先の変更候補 (39)

[一覧の目次](README.md)

<a id="compare-3e5af879b0d5f231f73715f371fcba83"></a>

### [`00838e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838e94.md) → [`0086b134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b134.md) FUN_0086b134

採用 · 移動量 `+0x322a0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`008216e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/008216e4.md) · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00853660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853660.md) · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00838e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838e94.md#insn-00838e98) · [`00838eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838e94.md#insn-00838eb0)
- 新版 `0086b138`（命令位置の公開資料なし） · `0086b150`（命令位置の公開資料なし）

~~~diff
- 00838e98 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00838e98 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 0086b138 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 0086b138 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00838e98 bytes 480100b4
+ 0086b138 bytes 480100b4
- 00838eb0 ["INT_ADD", "register:40f0:8", ["const:838eb0:8", "const:4:8"]]
- 00838eb0 ["CALL", null, ["callee:00c57a80:8"]]
+ 0086b150 ["INT_ADD", "register:40f0:8", ["const:86b150:8", "const:4:8"]]
+ 0086b150 ["CALL", null, ["callee:00c57a80:8"]]
- 00838eb0 bytes 60880e94
+ 0086b150 bytes 4cb20f94
~~~


<a id="compare-406b752c450e2ad846d2a5a8d3e672f0"></a>

### [`00839074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839074.md) → [`0086b314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b314.md) FUN_0086b314

採用 · 移動量 `+0x322a0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008216e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/008216e4.md) · 呼出先 3件 [`004759a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004759a4.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb340.md)
- 新版 呼出元 1件 [`00853660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853660.md) · 呼出先 3件 [`0049883c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049883c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083908c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00839094"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00839094"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00839094",
      "DATA",
      [
        "storage",
        "00c010e8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008390ec",
      "PARAM",
      [
        "storage",
        "002daf72",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0086b334",
      "DATA",
      [
        "storage",
        "00c7ed20",
        null,
        "undefined *"
      ]
    ],
    [
      "0086b38c",
      "PARAM",
      [
        "storage",
        "002ede3e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083908c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839074.md#insn-0083908c) · [`00839094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839074.md#insn-00839094) · [`008390d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839074.md#insn-008390d8)
- 新版 `0086b378`（命令位置の公開資料なし）

~~~diff
- 0083908c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 0083908c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 0083908c bytes 010800f9
- 00839094 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00839094 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00839094 ["COPY", "tmp:2:8", ["tmp:0:8"]]
- 00839094 ["COPY", "tmp:3:8", ["register:4000:8"]]
- 00839094 bytes 087c00a9
- 008390d8 ["INT_ADD", "register:40f0:8", ["const:8390d8:8", "const:4:8"]]
- 008390d8 ["CALL", null, ["callee:00c538b0:8"]]
+ 0086b378 ["INT_ADD", "register:40f0:8", ["const:86b378:8", "const:4:8"]]
+ 0086b378 ["CALL", null, ["callee:00c538b0:8"]]
- 008390d8 bytes 62770e94
+ 0086b378 bytes 4ea10f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c24ee64a4010b8bb5152a059b06410b5"></a>

### [`00839140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839140.md) → [`0086b3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b3e0.md) FUN_0086b3e0

採用 · 移動量 `+0x322a0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0086b3f8",
      "incomplete_value": false,
      "site": "0086b3fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00839158",
      "incomplete_value": false,
      "site": "0083915c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "0086b3fc",
      "DATA",
      [
        "storage",
        "00c010e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086b3fc",
      "DATA",
      [
        "storage",
        "00c7ed20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839140.md#insn-00839154) · [`00839158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839140.md#insn-00839158) · [`00839168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839140.md#insn-00839168)
- 新版 `0086b3f4`（命令位置の公開資料なし） · `0086b3f8`（命令位置の公開資料なし） · `0086b408`（命令位置の公開資料なし）

~~~diff
- 00839154 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 0086b3f4 ["COPY", "register:4048:8", ["const:c7e000:8"]]
- 00839154 bytes 491e0090
+ 0086b3f4 bytes 892000f0
- 00839158 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00839158 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00839158 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00839158 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086b3f8 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 0086b3f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b3f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b3f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00839158 bytes 29a10391
+ 0086b3f8 bytes 29813491
- 00839168 ["INT_ADD", "register:40f0:8", ["const:839168:8", "const:4:8"]]
- 00839168 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086b408 ["INT_ADD", "register:40f0:8", ["const:86b408:8", "const:4:8"]]
+ 0086b408 ["CALL", null, ["callee:00c57ab0:8"]]
- 00839168 bytes be870e94
+ 0086b408 bytes aab10f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52ace54b8b264367dfbb2d671abfdd5e"></a>

### [`008391ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008391ec.md) → [`0086b48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b48c.md) FUN_0086b48c

採用 · 移動量 `+0x322a0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0086b4a4",
      "incomplete_value": false,
      "site": "0086b4a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00839204",
      "incomplete_value": false,
      "site": "00839208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "0086b4a8",
      "DATA",
      [
        "storage",
        "00c010e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086b4a8",
      "DATA",
      [
        "storage",
        "00c7ed20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008391ec.md#insn-00839200) · [`00839204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008391ec.md#insn-00839204) · [`00839214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008391ec.md#insn-00839214)
- 新版 `0086b4a0`（命令位置の公開資料なし） · `0086b4a4`（命令位置の公開資料なし） · `0086b4b4`（命令位置の公開資料なし）

~~~diff
- 00839200 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 0086b4a0 ["COPY", "register:4048:8", ["const:c7e000:8"]]
- 00839200 bytes 491e0090
+ 0086b4a0 bytes 892000f0
- 00839204 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00839204 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00839204 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00839204 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086b4a4 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 0086b4a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b4a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086b4a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00839204 bytes 29a10391
+ 0086b4a4 bytes 29813491
- 00839214 ["INT_ADD", "register:40f0:8", ["const:839214:8", "const:4:8"]]
- 00839214 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086b4b4 ["INT_ADD", "register:40f0:8", ["const:86b4b4:8", "const:4:8"]]
+ 0086b4b4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00839214 bytes 93870e94
+ 0086b4b4 bytes 7fb10f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d18b762b0f66fdc91864d134d0f7f28"></a>

### [`00839300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839300.md) → [`0086b5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b5a0.md) FUN_0086b5a0

採用 · 移動量 `+0x322a0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0082a194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082a/0082a194.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`0085c10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085c/0085c10c.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 66.00% / 新版 82.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00839500"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0086b7a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0083951c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083951c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086b7e8"
      ]
    ]
  ],
  "added": [
    [
      "0086b7bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086b7e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839300.md#insn-00839500) · [`00839504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839300.md#insn-00839504) · [`0083951c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839300.md#insn-0083951c)
- 新版 `0086b7a4`（命令位置の公開資料なし）

~~~diff
- 00839500 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:108:8"]]
- 00839500 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d0:8"]]
- 00839500 bytes 7a8600f9
- 00839504 ["INT_ADD", "register:40f0:8", ["const:839504:8", "const:4:8"]]
- 00839504 ["CALL", null, ["callee:00c57c00:8"]]
+ 0086b7a4 ["INT_ADD", "register:40f0:8", ["const:86b7a4:8", "const:4:8"]]
+ 0086b7a4 ["CALL", null, ["callee:00c57c00:8"]]
- 00839504 bytes 2b870e94
+ 0086b7a4 bytes 17b10f94
- 0083951c ["CBRANCH", null, ["local:b35:8", "register:101:1"]]
- 0083951c bytes 60010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-277806f4140e87e2a1ce04ccc023ca40"></a>

### [`008396f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008396f0.md) → [`0086b990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b990.md) FUN_0086b990

採用 · 移動量 `+0x322a0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0082a194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082a/0082a194.md) [`00839d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839d14.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0085c10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085c/0085c10c.md) [`0086c000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c000.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 38.89% / 新版 46.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0086ba40",
      "incomplete_value": true,
      "site": "0086ba44",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:fffffffffffffff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008397a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008396f0.md#insn-008397a4) · [`00839708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008396f0.md#insn-00839708) · [`00839710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008396f0.md#insn-00839710)
- 新版 `0086ba44`（命令位置の公開資料なし） · `0086b9a8`（命令位置の公開資料なし） · `0086b9b0`（命令位置の公開資料なし）

~~~diff
- 008397a4 ["INT_ADD", "register:40f0:8", ["const:8397a4:8", "const:4:8"]]
- 008397a4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086ba44 ["INT_ADD", "register:40f0:8", ["const:86ba44:8", "const:4:8"]]
+ 0086ba44 ["CALL", null, ["callee:00c57ab0:8"]]
- 008397a4 bytes 2f860e94
+ 0086ba44 bytes 1bb00f94
- 00839708 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00839708 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0086b9a8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 0086b9a8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00839708 bytes 600000b4
+ 0086b9a8 bytes 600000b4
- 00839710 ["INT_ADD", "register:40f0:8", ["const:839710:8", "const:4:8"]]
- 00839710 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086b9b0 ["INT_ADD", "register:40f0:8", ["const:86b9b0:8", "const:4:8"]]
+ 0086b9b0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00839710 bytes 54860e94
+ 0086b9b0 bytes 40b00f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d6c6e8db39fd0d1477a6a06f16fb69a"></a>

### [`00839874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839874.md) → [`0086bb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb14.md) FUN_0086bb14

採用 · 移動量 `+0x322a0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 7件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00817cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/00817cac.md) [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`00839874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839874.md) [`0098d6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0098d/0098d6c0.md) · 呼出先 2件 [`00839874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839874.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 7件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849aa4.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`0086bb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb14.md) [`009c31b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c3/009c31b4.md) · 呼出先 2件 [`0086bb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb14.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0086bb3c",
      "incomplete_value": true,
      "site": "0086bb40",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0086bb38",
      "incomplete_value": true,
      "site": "0086bb40",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008398a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839874.md#insn-008398a0) · [`00839874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839874.md#insn-00839874) · [`00839894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839874.md#insn-00839894)
- 新版 `0086bb40`（命令位置の公開資料なし） · `0086bb14`（命令位置の公開資料なし） · `0086bb34`（命令位置の公開資料なし）

~~~diff
- 008398a0 ["INT_ADD", "register:40f0:8", ["const:8398a0:8", "const:4:8"]]
- 008398a0 ["CALL", null, ["local:b0:8"]]
+ 0086bb40 ["INT_ADD", "register:40f0:8", ["const:86bb40:8", "const:4:8"]]
+ 0086bb40 ["CALL", null, ["local:b0:8"]]
- 008398a0 bytes f5ffff97
+ 0086bb40 bytes f5ffff97
- 00839874 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00839874 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0086bb14 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 0086bb14 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00839874 bytes 010200b4
+ 0086bb14 bytes 010200b4
- 00839894 ["INT_ADD", "register:40f0:8", ["const:839894:8", "const:4:8"]]
- 00839894 ["CALL", null, ["local:b0:8"]]
+ 0086bb34 ["INT_ADD", "register:40f0:8", ["const:86bb34:8", "const:4:8"]]
+ 0086bb34 ["CALL", null, ["local:b0:8"]]
- 00839894 bytes f8ffff97
+ 0086bb34 bytes f8ffff97
~~~


<a id="compare-d4093ba0dba7e8006c9dcfd8836bc1e5"></a>

### [`008398b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008398b8.md) → [`0086bb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb58.md) FUN_0086bb58

採用 · 移動量 `+0x322a0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`008179e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/008179e0.md) [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) [`008398b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008398b8.md) · 呼出先 3件 [`008398b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008398b8.md) [`00839918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839918.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008497d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008497d8.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) [`0086bb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb58.md) · 呼出先 3件 [`0086bb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bb58.md) [`0086bbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bbb8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 25.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008398bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008398bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008398c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008398bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008398c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0086bb5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0086bb60",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008398bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008398b8.md#insn-008398bc) · [`008398c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008398b8.md#insn-008398c0) · [`008398e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008398b8.md#insn-008398e0)
- 新版 `0086bb80`（命令位置の公開資料なし）

~~~diff
- 008398bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008398bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008398bc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008398bc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008398bc bytes fd7bbea9
- 008398c0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008398c0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008398c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008398c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008398c0 bytes f44f01a9
- 008398e0 ["INT_ADD", "register:40f0:8", ["const:8398e0:8", "const:4:8"]]
- 008398e0 ["CALL", null, ["local:b0:8"]]
+ 0086bb80 ["INT_ADD", "register:40f0:8", ["const:86bb80:8", "const:4:8"]]
+ 0086bb80 ["CALL", null, ["local:b0:8"]]
- 008398e0 bytes f6ffff97
+ 0086bb80 bytes f6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c8700435d9da1d6c1be9583e5c40998"></a>

### [`00839afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839afc.md) → [`0086bde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bde8.md) FUN_0086bde8

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`00839afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839afc.md) [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 2件 [`00839afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839afc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`0086bde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bde8.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 2件 [`0086bde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bde8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839afc.md#insn-00839afc) · [`00839b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839afc.md#insn-00839b1c) · [`00839b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839afc.md#insn-00839b28)
- 新版 `0086bde8`（命令位置の公開資料なし） · `0086be08`（命令位置の公開資料なし） · `0086be14`（命令位置の公開資料なし）

~~~diff
- 00839afc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00839afc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0086bde8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 0086bde8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00839afc bytes 010200b4
+ 0086bde8 bytes 010200b4
- 00839b1c ["INT_ADD", "register:40f0:8", ["const:839b1c:8", "const:4:8"]]
- 00839b1c ["CALL", null, ["local:b0:8"]]
+ 0086be08 ["INT_ADD", "register:40f0:8", ["const:86be08:8", "const:4:8"]]
+ 0086be08 ["CALL", null, ["local:b0:8"]]
- 00839b1c bytes f8ffff97
+ 0086be08 bytes f8ffff97
- 00839b28 ["INT_ADD", "register:40f0:8", ["const:839b28:8", "const:4:8"]]
- 00839b28 ["CALL", null, ["local:b0:8"]]
+ 0086be14 ["INT_ADD", "register:40f0:8", ["const:86be14:8", "const:4:8"]]
+ 0086be14 ["CALL", null, ["local:b0:8"]]
- 00839b28 bytes f5ffff97
+ 0086be14 bytes f5ffff97
~~~


<a id="compare-7ed53d18609708a1b30eb90bf6494457"></a>

### [`00839b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839b40.md) → [`0086be2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be2c.md) FUN_0086be2c

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 6件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0081749c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/0081749c.md) [`00839b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839b40.md) [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) [`00a44918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44918.md) · 呼出先 2件 [`00839b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839b40.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 6件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00849294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/00849294.md) [`0086be2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be2c.md) [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) [`00aa281c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa2/00aa281c.md) · 呼出先 2件 [`0086be2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086be2c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00839b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839b40.md#insn-00839b40) · [`00839b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839b40.md#insn-00839b60) · [`00839b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839b40.md#insn-00839b6c)
- 新版 `0086be2c`（命令位置の公開資料なし） · `0086be4c`（命令位置の公開資料なし） · `0086be58`（命令位置の公開資料なし）

~~~diff
- 00839b40 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00839b40 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 0086be2c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 0086be2c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00839b40 bytes 010200b4
+ 0086be2c bytes 010200b4
- 00839b60 ["INT_ADD", "register:40f0:8", ["const:839b60:8", "const:4:8"]]
- 00839b60 ["CALL", null, ["local:b0:8"]]
+ 0086be4c ["INT_ADD", "register:40f0:8", ["const:86be4c:8", "const:4:8"]]
+ 0086be4c ["CALL", null, ["local:b0:8"]]
- 00839b60 bytes f8ffff97
+ 0086be4c bytes f8ffff97
- 00839b6c ["INT_ADD", "register:40f0:8", ["const:839b6c:8", "const:4:8"]]
- 00839b6c ["CALL", null, ["local:b0:8"]]
+ 0086be58 ["INT_ADD", "register:40f0:8", ["const:86be58:8", "const:4:8"]]
+ 0086be58 ["CALL", null, ["local:b0:8"]]
- 00839b6c bytes f5ffff97
+ 0086be58 bytes f5ffff97
~~~


<a id="compare-3ad4f1a23f8335e00624cd4da4d5f38a"></a>

### [`00839bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839bd4.md) → [`0086bec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bec0.md) FUN_0086bec0

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00839bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839bd4.md) [`00ac0004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac0/00ac0004.md) · 呼出先 2件 [`00839bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839bd4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086bec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bec0.md) [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 2件 [`0086bec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bec0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0086bef4",
      "incomplete_value": true,
      "site": "0086bef8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00839c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839bd4.md#insn-00839c0c) · [`00839bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839bd4.md#insn-00839bd4) · [`00839bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839bd4.md#insn-00839bf0)
- 新版 `0086bef8`（命令位置の公開資料なし） · `0086bec0`（命令位置の公開資料なし） · `0086bedc`（命令位置の公開資料なし）

~~~diff
- 00839c0c ["INT_ADD", "register:40f0:8", ["const:839c0c:8", "const:4:8"]]
- 00839c0c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086bef8 ["INT_ADD", "register:40f0:8", ["const:86bef8:8", "const:4:8"]]
+ 0086bef8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00839c0c bytes 15850e94
+ 0086bef8 bytes eeae0f94
- 00839bd4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00839bd4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 0086bec0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 0086bec0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00839bd4 bytes 610200b4
+ 0086bec0 bytes 610200b4
- 00839bf0 ["INT_ADD", "register:40f0:8", ["const:839bf0:8", "const:4:8"]]
- 00839bf0 ["CALL", null, ["local:b0:8"]]
+ 0086bedc ["INT_ADD", "register:40f0:8", ["const:86bedc:8", "const:4:8"]]
+ 0086bedc ["CALL", null, ["local:b0:8"]]
- 00839bf0 bytes f9ffff97
+ 0086bedc bytes f9ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63867cce2423a9e8375f384a486f82d7"></a>

### [`00839d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839d14.md) → [`0086c000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c000.md) FUN_0086c000

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00839d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839d14.md) [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 3件 [`008396f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/008396f0.md) [`00839d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839d14.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c000.md) [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 3件 [`0086b990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b990.md) [`0086c000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c000.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0086c030",
      "incomplete_value": true,
      "site": "0086c034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00839d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839d14.md#insn-00839d48) · [`00839d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839d14.md#insn-00839d14) · [`00839d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839d14.md#insn-00839d34)
- 新版 `0086c034`（命令位置の公開資料なし） · `0086c000`（命令位置の公開資料なし） · `0086c020`（命令位置の公開資料なし）

~~~diff
- 00839d48 ["INT_ADD", "register:40f0:8", ["const:839d48:8", "const:4:8"]]
- 00839d48 ["CALL", null, ["callee:0086b990:8"]]
+ 0086c034 ["INT_ADD", "register:40f0:8", ["const:86c034:8", "const:4:8"]]
+ 0086c034 ["CALL", null, ["callee:0086b990:8"]]
- 00839d48 bytes 6afeff97
+ 0086c034 bytes 57feff97
- 00839d14 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00839d14 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0086c000 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 0086c000 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00839d14 bytes 410200b4
+ 0086c000 bytes 410200b4
- 00839d34 ["INT_ADD", "register:40f0:8", ["const:839d34:8", "const:4:8"]]
- 00839d34 ["CALL", null, ["local:b0:8"]]
+ 0086c020 ["INT_ADD", "register:40f0:8", ["const:86c020:8", "const:4:8"]]
+ 0086c020 ["CALL", null, ["local:b0:8"]]
- 00839d34 bytes f8ffff97
+ 0086c020 bytes f8ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-361b79c866e0e8433de7f0ee7ab1f414"></a>

### [`00839d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839d60.md) → [`0086c04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c04c.md) FUN_0086c04c

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00839d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839d60.md) · 呼出先 4件 [`00839d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839d60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0086c04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c04c.md) · 呼出先 4件 [`0086c04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c04c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 72.22% / 新版 81.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0086c064",
      "incomplete_value": true,
      "site": "0086c06c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4008:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00839d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839d60.md#insn-00839d80) · [`00839d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839d60.md#insn-00839d60) · [`00839d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839d60.md#insn-00839d70)
- 新版 `0086c06c`（命令位置の公開資料なし） · `0086c04c`（命令位置の公開資料なし）

~~~diff
- 00839d80 ["INT_ADD", "register:40f0:8", ["const:839d80:8", "const:4:8"]]
- 00839d80 ["CALL", null, ["local:b0:8"]]
+ 0086c06c ["INT_ADD", "register:40f0:8", ["const:86c06c:8", "const:4:8"]]
+ 0086c06c ["CALL", null, ["local:b0:8"]]
- 00839d80 bytes f8ffff97
+ 0086c06c bytes f8ffff97
- 00839d60 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00839d60 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 0086c04c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 0086c04c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00839d60 bytes 610400b4
+ 0086c04c bytes 610400b4
- 00839d70 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00839d70 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22783009782a26a42f2c728a87b21c2c"></a>

### [`0083a138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a138.md) → [`0086c424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c424.md) FUN_0086c424

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 80.95% / 新版 85.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0086c480",
      "incomplete_value": true,
      "site": "0086c484",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:fffffffffffffff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0083a198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a138.md#insn-0083a198) · [`0083a150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a138.md#insn-0083a150) · [`0083a168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a138.md#insn-0083a168)
- 新版 `0086c484`（命令位置の公開資料なし） · `0086c43c`（命令位置の公開資料なし） · `0086c454`（命令位置の公開資料なし）

~~~diff
- 0083a198 ["INT_ADD", "register:40f0:8", ["const:83a198:8", "const:4:8"]]
- 0083a198 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0086c484 ["INT_ADD", "register:40f0:8", ["const:86c484:8", "const:4:8"]]
+ 0086c484 ["CALL", null, ["callee:00c57ab0:8"]]
- 0083a198 bytes b2830e94
+ 0086c484 bytes 8bad0f94
- 0083a150 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 0083a150 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 0086c43c ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 0086c43c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 0083a150 bytes 750400b4
+ 0086c43c bytes 750400b4
- 0083a168 ["BRANCH", null, ["local:b13:8"]]
+ 0086c454 ["BRANCH", null, ["local:b12:8"]]
- 0083a168 bytes 18000014
+ 0086c454 bytes 18000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daba864e765eeb3ae39c89dbbb4b4544"></a>

### [`0083a270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a270.md) → [`0086c55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c55c.md) FUN_0086c55c

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)
- 新版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.61% / 新版 75.61%

CFGの説明率　旧版 75.00% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083a2a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083a2b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083a2b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083a298",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0083a2a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083a2b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x13c0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0086c584",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086c590",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0086c59c",
      "WRITE",
      [
        "storage",
        "Stack[-0x13c0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083a2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a270.md#insn-0083a2a4) · [`0083a2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a270.md#insn-0083a2b0) · [`0083a2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a270.md#insn-0083a2b4)

~~~diff
- 0083a2a4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0083a2a4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0083a2a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0083a2a4 bytes a8831ff8
- 0083a2b0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0083a2b0 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:10:8"]]
- 0083a2b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0083a2b0 bytes e9430039
- 0083a2b4 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0083a2b4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:19:8"]]
- 0083a2b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 0083a2b4 bytes e89301b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8fc410985f566424fcedd523d0d45e0"></a>

### [`0083a3f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a3f8.md) → [`0086c6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c6e4.md) FUN_0086c6e4

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)
- 新版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 75.00% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083a42c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083a438"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083a43c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083a420",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0083a42c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083a438",
      "WRITE",
      [
        "storage",
        "Stack[-0x13c0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0086c70c",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086c718",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0086c724",
      "WRITE",
      [
        "storage",
        "Stack[-0x13c0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083a42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a3f8.md#insn-0083a42c) · [`0083a438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a3f8.md#insn-0083a438) · [`0083a43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a3f8.md#insn-0083a43c)

~~~diff
- 0083a42c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0083a42c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0083a42c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0083a42c bytes a8831ff8
- 0083a438 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0083a438 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:10:8"]]
- 0083a438 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0083a438 bytes e9430039
- 0083a43c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0083a43c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:19:8"]]
- 0083a43c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 0083a43c bytes e89301b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d0d98216871c6e01060bbfac8c3066d"></a>

### [`0083a588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a588.md) → [`0086c874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086c874.md) FUN_0086c874

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)
- 新版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 33.33% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083a5bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083a5c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083a5cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083a5b0",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0083a5bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083a5c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x13c0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0086c89c",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086c8a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0086c8b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x13c0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083a5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a588.md#insn-0083a5bc) · [`0083a5c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a588.md#insn-0083a5c8) · [`0083a5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a588.md#insn-0083a5cc)

~~~diff
- 0083a5bc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0083a5bc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0083a5bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0083a5bc bytes a8831ff8
- 0083a5c8 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0083a5c8 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:10:8"]]
- 0083a5c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0083a5c8 bytes e9430039
- 0083a5cc ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0083a5cc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:19:8"]]
- 0083a5cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 0083a5cc bytes e89301b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63c69e186b649edb15ce20e4fadb5ea2"></a>

### [`0083a8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a8a8.md) → [`0086cb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086cb94.md) FUN_0086cb94

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)
- 新版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 6件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086cbdc",
      "incomplete_value": true,
      "site": "0086cbdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0083a8f0",
      "incomplete_value": true,
      "site": "0083a8f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086cbec",
      "value": [
        "leaf",
        "ram:c57fa0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0083a900",
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
      "site": "0086cc54",
      "value": [
        "leaf",
        "ram:46dac0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0083a968",
      "value": [
        "leaf",
        "ram:44ac28:8"
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
      "0086cbbc",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "0086cbec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb550"
      ]
    ],
    [
      "0086cc54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044ac28"
      ]
    ]
  ],
  "added": [
    [
      "0086cbbc",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086cbec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57fa0"
      ]
    ],
    [
      "0086cc54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083a900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a8a8.md#insn-0083a900) · [`0083a968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a8a8.md#insn-0083a968) · [`0083a97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083a8a8.md#insn-0083a97c)
- 新版 `0086cbec`（命令位置の公開資料なし） · `0086cc54`（命令位置の公開資料なし） · `0086cc68`（命令位置の公開資料なし）

~~~diff
- 0083a900 ["INT_ADD", "register:40f0:8", ["const:83a900:8", "const:4:8"]]
- 0083a900 ["CALL", null, ["ram:bdb550:8"]]
+ 0086cbec ["INT_ADD", "register:40f0:8", ["const:86cbec:8", "const:4:8"]]
+ 0086cbec ["CALL", null, ["ram:c57fa0:8"]]
- 0083a900 bytes 14830e94
+ 0086cbec bytes edac0f94
- 0083a968 ["INT_ADD", "register:40f0:8", ["const:83a968:8", "const:4:8"]]
- 0083a968 ["CALL", null, ["ram:44ac28:8"]]
+ 0086cc54 ["INT_ADD", "register:40f0:8", ["const:86cc54:8", "const:4:8"]]
+ 0086cc54 ["CALL", null, ["ram:46dac0:8"]]
- 0083a968 bytes b040f097
+ 0086cc54 bytes 9b03f097
- 0083a97c ["INT_ADD", "register:40f0:8", ["const:83a97c:8", "const:4:8"]]
- 0083a97c ["CALL", null, ["ram:44ac28:8"]]
+ 0086cc68 ["INT_ADD", "register:40f0:8", ["const:86cc68:8", "const:4:8"]]
+ 0086cc68 ["CALL", null, ["ram:46dac0:8"]]
- 0083a97c bytes ab40f097
+ 0086cc68 bytes 9603f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c353a6d72ea2ad7520f5cf50a2aa547"></a>

### [`0083aa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083aa38.md) → [`0086cd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086cd24.md) FUN_0086cd24

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) [`009dc30c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dc30c.md) [`009dc434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dc434.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)
- 新版 呼出元 3件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) [`00a39208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39208.md) [`00a39330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39330.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.02% / 新版 89.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 6件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086cd6c",
      "incomplete_value": true,
      "site": "0086cd6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0083aa80",
      "incomplete_value": true,
      "site": "0083aa80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086cd7c",
      "value": [
        "leaf",
        "ram:c57fa0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0083aa90",
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
      "site": "0086cde4",
      "value": [
        "leaf",
        "ram:46dac0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0083aaf8",
      "value": [
        "leaf",
        "ram:44ac28:8"
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
      "0086cd4c",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "0086cd7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb550"
      ]
    ],
    [
      "0086cde4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044ac28"
      ]
    ]
  ],
  "added": [
    [
      "0086cd4c",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086cd7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57fa0"
      ]
    ],
    [
      "0086cde4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083aa90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083aa38.md#insn-0083aa90) · [`0083aaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083aa38.md#insn-0083aaf8) · [`0083ab0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083aa38.md#insn-0083ab0c)
- 新版 `0086cd7c`（命令位置の公開資料なし） · `0086cde4`（命令位置の公開資料なし） · `0086cdf8`（命令位置の公開資料なし）

~~~diff
- 0083aa90 ["INT_ADD", "register:40f0:8", ["const:83aa90:8", "const:4:8"]]
- 0083aa90 ["CALL", null, ["ram:bdb550:8"]]
+ 0086cd7c ["INT_ADD", "register:40f0:8", ["const:86cd7c:8", "const:4:8"]]
+ 0086cd7c ["CALL", null, ["ram:c57fa0:8"]]
- 0083aa90 bytes b0820e94
+ 0086cd7c bytes 89ac0f94
- 0083aaf8 ["INT_ADD", "register:40f0:8", ["const:83aaf8:8", "const:4:8"]]
- 0083aaf8 ["CALL", null, ["ram:44ac28:8"]]
+ 0086cde4 ["INT_ADD", "register:40f0:8", ["const:86cde4:8", "const:4:8"]]
+ 0086cde4 ["CALL", null, ["ram:46dac0:8"]]
- 0083aaf8 bytes 4c40f097
+ 0086cde4 bytes 3703f097
- 0083ab0c ["INT_ADD", "register:40f0:8", ["const:83ab0c:8", "const:4:8"]]
- 0083ab0c ["CALL", null, ["ram:44ac28:8"]]
+ 0086cdf8 ["INT_ADD", "register:40f0:8", ["const:86cdf8:8", "const:4:8"]]
+ 0086cdf8 ["CALL", null, ["ram:46dac0:8"]]
- 0083ab0c bytes 4740f097
+ 0086cdf8 bytes 3203f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0714568e96c9dade65337bfe9714ff03"></a>

### [`0083abc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083abc0.md) → [`0086ceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086c/0086ceac.md) FUN_0086ceac

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)
- 新版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 16.67% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086cef4",
      "incomplete_value": true,
      "site": "0086cef4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0083ac08",
      "incomplete_value": true,
      "site": "0083ac08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083ac48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0086cf34"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0086ced4",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "0086cf04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb550"
      ]
    ],
    [
      "unmatched:0083ac48",
      "WRITE",
      [
        "storage",
        "Stack[-0x13c0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0086ced4",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086cf04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57fa0"
      ]
    ],
    [
      "0086cf34",
      "WRITE",
      [
        "storage",
        "Stack[-0x13c0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083ac18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083abc0.md#insn-0083ac18) · [`0083ac48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083abc0.md#insn-0083ac48) · [`0083ac80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083abc0.md#insn-0083ac80)
- 新版 `0086cf04`（命令位置の公開資料なし）

~~~diff
- 0083ac18 ["INT_ADD", "register:40f0:8", ["const:83ac18:8", "const:4:8"]]
- 0083ac18 ["CALL", null, ["ram:bdb550:8"]]
+ 0086cf04 ["INT_ADD", "register:40f0:8", ["const:86cf04:8", "const:4:8"]]
+ 0086cf04 ["CALL", null, ["ram:c57fa0:8"]]
- 0083ac18 bytes 4e820e94
+ 0086cf04 bytes 27ac0f94
- 0083ac48 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0083ac48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0083ac48 bytes e80b00f9
- 0083ac80 ["INT_ADD", "register:40f0:8", ["const:83ac80:8", "const:4:8"]]
- 0083ac80 ["CALL", null, ["ram:44ac28:8"]]
- 0083ac80 bytes ea3ff097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58bf45b3f207d13fb7af68ccff6f9a65"></a>

### [`0083ad48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083ad48.md) → [`0086d034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d034.md) FUN_0086d034

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)
- 新版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 33.33% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083ad7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083ad88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083ad8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083ad70",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0083ad7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083ad88",
      "WRITE",
      [
        "storage",
        "Stack[-0x13c0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0086d05c",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0086d068",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0086d074",
      "WRITE",
      [
        "storage",
        "Stack[-0x13c0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083ad7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083ad48.md#insn-0083ad7c) · [`0083ad88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083ad48.md#insn-0083ad88) · [`0083ad8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083ad48.md#insn-0083ad8c)

~~~diff
- 0083ad7c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0083ad7c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0083ad7c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0083ad7c bytes a8831ff8
- 0083ad88 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0083ad88 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:10:8"]]
- 0083ad88 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0083ad88 bytes e9430039
- 0083ad8c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0083ad8c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:19:8"]]
- 0083ad8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 0083ad8c bytes e89301b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e084169accbe735ee9e44df59c269a7"></a>

### [`0083afec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083afec.md) → [`0086d2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d2d8.md) FUN_0086d2d8

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083b010"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083b010"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0086d2fc"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083b010",
      "DATA",
      [
        "storage",
        "00c01218",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0083b014",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083b018",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0086d2fc",
      "DATA",
      [
        "storage",
        "00c7ee50",
        null,
        "undefined *"
      ]
    ],
    [
      "0086d300",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0086d304",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083afec.md#insn-0083b000) · [`0083b010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083afec.md#insn-0083b010) · [`0083b01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083a/0083afec.md#insn-0083b01c)
- 新版 `0086d2ec`（命令位置の公開資料なし）

~~~diff
- 0083b000 ["INT_ADD", "register:40f0:8", ["const:83b000:8", "const:4:8"]]
- 0083b000 ["CALL", null, ["callee:00c57a90:8"]]
+ 0086d2ec ["INT_ADD", "register:40f0:8", ["const:86d2ec:8", "const:4:8"]]
+ 0086d2ec ["CALL", null, ["callee:00c57a90:8"]]
- 0083b000 bytes 10800e94
+ 0086d2ec bytes e9a90f94
- 0083b010 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0083b010 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0083b010 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0083b010 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083b010 bytes 082400a9
- 0083b01c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0083b01c ["RETURN", null, ["register:0:8"]]
- 0083b01c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96ee6867993480244b2e2ac4b19e1db8"></a>

### [`0083b03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b03c.md) → [`0086d328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d328.md) FUN_0086d328

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

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
      "site": "0086d34c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0083b060",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "0086d34c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "0086d34c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b03c.md#insn-0083b060) · [`0083b06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b03c.md#insn-0083b06c)
- 新版 `0086d34c`（命令位置の公開資料なし） · `0086d358`（命令位置の公開資料なし）

~~~diff
- 0083b060 ["INT_ADD", "register:40f0:8", ["const:83b060:8", "const:4:8"]]
- 0083b060 ["CALL", null, ["ram:457e1c:8"]]
+ 0086d34c ["INT_ADD", "register:40f0:8", ["const:86d34c:8", "const:4:8"]]
+ 0086d34c ["CALL", null, ["ram:47acb4:8"]]
- 0083b060 bytes 6f73f097
+ 0086d34c bytes 5a36f097
- 0083b06c ["INT_ADD", "register:40f0:8", ["const:83b06c:8", "const:4:8"]]
- 0083b06c ["CALL", null, ["callee:0047cd94:8"]]
+ 0086d358 ["INT_ADD", "register:40f0:8", ["const:86d358:8", "const:4:8"]]
+ 0086d358 ["CALL", null, ["callee:0047cd94:8"]]
- 0083b06c bytes a47bf097
+ 0086d358 bytes 8f3ef097
~~~


<a id="compare-62cc0df6a45836a7f016c954aa4f9524"></a>

### [`0083b100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b100.md) → [`0086d3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d3ec.md) FUN_0086d3ec

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

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
      "site": "0086d410",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0083b124",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "0086d410",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "0086d410",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b100.md#insn-0083b124) · [`0083b130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b100.md#insn-0083b130)
- 新版 `0086d410`（命令位置の公開資料なし） · `0086d41c`（命令位置の公開資料なし）

~~~diff
- 0083b124 ["INT_ADD", "register:40f0:8", ["const:83b124:8", "const:4:8"]]
- 0083b124 ["CALL", null, ["ram:457e1c:8"]]
+ 0086d410 ["INT_ADD", "register:40f0:8", ["const:86d410:8", "const:4:8"]]
+ 0086d410 ["CALL", null, ["ram:47acb4:8"]]
- 0083b124 bytes 3e73f097
+ 0086d410 bytes 2936f097
- 0083b130 ["INT_ADD", "register:40f0:8", ["const:83b130:8", "const:4:8"]]
- 0083b130 ["CALL", null, ["callee:0047cd94:8"]]
+ 0086d41c ["INT_ADD", "register:40f0:8", ["const:86d41c:8", "const:4:8"]]
+ 0086d41c ["CALL", null, ["callee:0047cd94:8"]]
- 0083b130 bytes 737bf097
+ 0086d41c bytes 5e3ef097
~~~


<a id="compare-f9fc721987d24e2107b17da942f76770"></a>

### [`0083b174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b174.md) → [`0086d460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d460.md) FUN_0086d460

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0086d484",
      "incomplete_value": false,
      "site": "0086d484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b198",
      "incomplete_value": false,
      "site": "0083b198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "0086d484",
      "DATA",
      [
        "storage",
        "00c01318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d484",
      "DATA",
      [
        "storage",
        "00c7ef50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b174.md#insn-0083b188) · [`0083b190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b174.md#insn-0083b190) · [`0083b194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b174.md#insn-0083b194)
- 新版 `0086d474`（命令位置の公開資料なし） · `0086d47c`（命令位置の公開資料なし） · `0086d480`（命令位置の公開資料なし）

~~~diff
- 0083b188 ["INT_ADD", "register:40f0:8", ["const:83b188:8", "const:4:8"]]
- 0083b188 ["CALL", null, ["callee:00c57a90:8"]]
+ 0086d474 ["INT_ADD", "register:40f0:8", ["const:86d474:8", "const:4:8"]]
+ 0086d474 ["CALL", null, ["callee:00c57a90:8"]]
- 0083b188 bytes ae7f0e94
+ 0086d474 bytes 87a90f94
- 0083b190 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 0086d47c ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 0083b190 bytes 281e00d0
+ 0086d47c bytes 882000b0
- 0083b194 ["COPY", "tmp:0:8", ["const:318:8"]]
- 0083b194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086d480 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 0086d480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b194 bytes 08610c91
+ 0086d480 bytes 08413d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae837cb089edf97d436ab5f5024d7878"></a>

### [`0083b1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b1c4.md) → [`0086d4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d4b0.md) FUN_0086d4b0

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

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
      "site": "0086d4d4",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0083b1e8",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "0086d4d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "0086d4d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b1c4.md#insn-0083b1e8) · [`0083b1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b1c4.md#insn-0083b1f4)
- 新版 `0086d4d4`（命令位置の公開資料なし） · `0086d4e0`（命令位置の公開資料なし）

~~~diff
- 0083b1e8 ["INT_ADD", "register:40f0:8", ["const:83b1e8:8", "const:4:8"]]
- 0083b1e8 ["CALL", null, ["ram:457e1c:8"]]
+ 0086d4d4 ["INT_ADD", "register:40f0:8", ["const:86d4d4:8", "const:4:8"]]
+ 0086d4d4 ["CALL", null, ["ram:47acb4:8"]]
- 0083b1e8 bytes 0d73f097
+ 0086d4d4 bytes f835f097
- 0083b1f4 ["INT_ADD", "register:40f0:8", ["const:83b1f4:8", "const:4:8"]]
- 0083b1f4 ["CALL", null, ["callee:0047cd94:8"]]
+ 0086d4e0 ["INT_ADD", "register:40f0:8", ["const:86d4e0:8", "const:4:8"]]
+ 0086d4e0 ["CALL", null, ["callee:0047cd94:8"]]
- 0083b1f4 bytes 427bf097
+ 0086d4e0 bytes 2d3ef097
~~~


<a id="compare-ac1b3c3ca2b17bfe3c3ea1bbb3e03f7a"></a>

### [`0083b238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b238.md) → [`0086d524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d524.md) FUN_0086d524

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0086d548",
      "incomplete_value": false,
      "site": "0086d548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b25c",
      "incomplete_value": false,
      "site": "0083b25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
      "0086d548",
      "DATA",
      [
        "storage",
        "00c01398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086d548",
      "DATA",
      [
        "storage",
        "00c7efd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b238.md#insn-0083b24c) · [`0083b254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b238.md#insn-0083b254) · [`0083b258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b238.md#insn-0083b258)
- 新版 `0086d538`（命令位置の公開資料なし） · `0086d540`（命令位置の公開資料なし） · `0086d544`（命令位置の公開資料なし）

~~~diff
- 0083b24c ["INT_ADD", "register:40f0:8", ["const:83b24c:8", "const:4:8"]]
- 0083b24c ["CALL", null, ["callee:00c57a90:8"]]
+ 0086d538 ["INT_ADD", "register:40f0:8", ["const:86d538:8", "const:4:8"]]
+ 0086d538 ["CALL", null, ["callee:00c57a90:8"]]
- 0083b24c bytes 7d7f0e94
+ 0086d538 bytes 56a90f94
- 0083b254 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 0086d540 ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 0083b254 bytes 281e00d0
+ 0086d540 bytes 882000b0
- 0083b258 ["COPY", "tmp:0:8", ["const:398:8"]]
- 0083b258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086d544 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 0086d544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086d544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b258 bytes 08610e91
+ 0086d544 bytes 08413f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c0418658512f37fd4bfa38c120a59ae"></a>

### [`0083b288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b288.md) → [`0086d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d574.md) FUN_0086d574

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

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
      "site": "0086d598",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0083b2ac",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "0086d598",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "0086d598",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b288.md#insn-0083b2ac) · [`0083b2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b288.md#insn-0083b2b8)
- 新版 `0086d598`（命令位置の公開資料なし） · `0086d5a4`（命令位置の公開資料なし）

~~~diff
- 0083b2ac ["INT_ADD", "register:40f0:8", ["const:83b2ac:8", "const:4:8"]]
- 0083b2ac ["CALL", null, ["ram:457e1c:8"]]
+ 0086d598 ["INT_ADD", "register:40f0:8", ["const:86d598:8", "const:4:8"]]
+ 0086d598 ["CALL", null, ["ram:47acb4:8"]]
- 0083b2ac bytes dc72f097
+ 0086d598 bytes c735f097
- 0083b2b8 ["INT_ADD", "register:40f0:8", ["const:83b2b8:8", "const:4:8"]]
- 0083b2b8 ["CALL", null, ["callee:0047cd94:8"]]
+ 0086d5a4 ["INT_ADD", "register:40f0:8", ["const:86d5a4:8", "const:4:8"]]
+ 0086d5a4 ["CALL", null, ["callee:0047cd94:8"]]
- 0083b2b8 bytes 117bf097
+ 0086d5a4 bytes fc3df097
~~~


<a id="compare-a7564e827c85c37f93434393939885ab"></a>

### [`0083b3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b3f0.md) → [`0086d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md) FUN_0086d6dc

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0042c9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c9c0.md) [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`00433930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/00433930.md) [`004418c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004418c4.md) [`004419a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004419a0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0044f858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f858.md) [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md) [`00464838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464838.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.02% / 新版 86.02%

CFGの説明率　旧版 30.38% / 新版 32.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083b418"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083b41c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083b438"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083b418",
      "WRITE",
      [
        "storage",
        "Stack[-0x220]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083b41c",
      "WRITE",
      [
        "storage",
        "Stack[-0x160]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083b420",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086d990"
      ]
    ]
  ],
  "added": [
    [
      "0086d704",
      "WRITE",
      [
        "storage",
        "Stack[-0x220]",
        null,
        null
      ]
    ],
    [
      "0086d708",
      "WRITE",
      [
        "storage",
        "Stack[-0x160]",
        null,
        null
      ]
    ],
    [
      "0086d70c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086d990"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b3f0.md#insn-0083b418) · [`0083b41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b3f0.md#insn-0083b41c) · [`0083b438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b3f0.md#insn-0083b438)

~~~diff
- 0083b418 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0083b418 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0083b418 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 0083b418 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0083b418 bytes ff430239
- 0083b41c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0083b41c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0083b41c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 0083b41c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0083b41c bytes ff430539
- 0083b438 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 0083b438 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0083b438 bytes e027803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e30af59b413bb87c1351c7f5088f90b8"></a>

### [`0083b938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b938.md) → [`0086dc24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc24.md) FUN_0086dc24

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`004418c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004418c4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md)

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
      "definition_site": "0086dc2c",
      "incomplete_value": false,
      "site": "0086dc30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b940",
      "incomplete_value": false,
      "site": "0083b944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "0086dc30",
      "DATA",
      [
        "storage",
        "00c01518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086dc30",
      "DATA",
      [
        "storage",
        "00c7f150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b938.md#insn-0083b93c) · [`0083b940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b938.md#insn-0083b940)
- 新版 `0086dc28`（命令位置の公開資料なし） · `0086dc2c`（命令位置の公開資料なし）

~~~diff
- 0083b93c ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 0086dc28 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0083b93c bytes 291e00d0
+ 0086dc28 bytes 892000d0
- 0083b940 ["COPY", "tmp:0:8", ["const:518:8"]]
- 0083b940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086dc2c ["COPY", "tmp:0:8", ["const:150:8"]]
+ 0086dc2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086dc2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086dc2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b940 bytes 29611491
+ 0086dc2c bytes 29410591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70dcd88434fd2b13734fac8ead0c05f0"></a>

### [`0083b958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b958.md) → [`0086dc44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc44.md) FUN_0086dc44

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`004418c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004418c4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0086dc4c",
      "incomplete_value": false,
      "site": "0086dc50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b960",
      "incomplete_value": false,
      "site": "0083b964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "0086dc50",
      "DATA",
      [
        "storage",
        "00c01518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086dc50",
      "DATA",
      [
        "storage",
        "00c7f150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b958.md#insn-0083b95c) · [`0083b960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b958.md#insn-0083b960) · [`0083b980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b958.md#insn-0083b980)
- 新版 `0086dc48`（命令位置の公開資料なし） · `0086dc4c`（命令位置の公開資料なし） · `0086dc6c`（命令位置の公開資料なし）

~~~diff
- 0083b95c ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 0086dc48 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0083b95c bytes 291e00d0
+ 0086dc48 bytes 892000d0
- 0083b960 ["COPY", "tmp:0:8", ["const:518:8"]]
- 0083b960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086dc4c ["COPY", "tmp:0:8", ["const:150:8"]]
+ 0086dc4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086dc4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086dc4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b960 bytes 29611491
+ 0086dc4c bytes 29410591
- 0083b980 ["INT_ADD", "register:40f0:8", ["const:83b980:8", "const:4:8"]]
- 0083b980 ["CALL", null, ["callee:0046475c:8"]]
+ 0086dc6c ["INT_ADD", "register:40f0:8", ["const:86dc6c:8", "const:4:8"]]
+ 0086dc6c ["CALL", null, ["callee:0046475c:8"]]
- 0083b980 bytes d117f097
+ 0086dc6c bytes bcdaef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16d9775912880ae3269cba025cc5f444"></a>

### [`0083b994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b994.md) → [`0086dc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dc80.md) FUN_0086dc80

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`004419a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004419a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00464838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464838.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083b9c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083b9c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083b9c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083b9c8",
      "DATA",
      [
        "storage",
        "00c01518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086dcb4",
      "DATA",
      [
        "storage",
        "00c7f150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b994.md#insn-0083b9c4) · [`0083b9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b994.md#insn-0083b9c8) · [`0083b9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b994.md#insn-0083b9d0)

~~~diff
- 0083b9c4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0083b9c4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0083b9c4 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:d0:8"]]
- 0083b9c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0083b9c4 bytes 1f400339
- 0083b9c8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0083b9c8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0083b9c8 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0083b9c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083b9c8 bytes 092000a9
- 0083b9d0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0083b9d0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0083b9d0 ["INT_ADD", "register:40a8:8", ["register:40a8:8", "const:10:8"]]
- 0083b9d0 ["STORE", null, ["const:1b1:8", "register:40a8:8", "tmp:1:1"]]
- 0083b9d0 bytes bf0e0138
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae6240c7d894803ba8f227b3e2da20cf"></a>

### [`0083ba94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083ba94.md) → [`0086dd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dd80.md) FUN_0086dd80

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`004418c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004418c4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083ba94.md#insn-0083ba98)
- 新版 `0086dd84`（命令位置の公開資料なし）

~~~diff
- 0083ba98 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 0083ba98 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0086dd84 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 0086dd84 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0083ba98 bytes 68000034
+ 0086dd84 bytes 68000034
~~~


<a id="compare-8ff8beab752679408dc76058f46931de"></a>

### [`0083baa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083baa8.md) → [`0086dd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086dd94.md) FUN_0086dd94

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0083b3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b3f0.md) · 呼出先 2件 [`004418c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00441/004418c4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0086d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md) · 呼出先 2件 [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083baac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083baa8.md#insn-0083baac) · [`0083bac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083baa8.md#insn-0083bac4)
- 新版 `0086dd98`（命令位置の公開資料なし） · `0086ddb0`（命令位置の公開資料なし）

~~~diff
- 0083baac ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 0083baac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0086dd98 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 0086dd98 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0083baac bytes 48010034
+ 0086dd98 bytes 48010034
- 0083bac4 ["INT_ADD", "register:40f0:8", ["const:83bac4:8", "const:4:8"]]
- 0083bac4 ["CALL", null, ["callee:0046475c:8"]]
+ 0086ddb0 ["INT_ADD", "register:40f0:8", ["const:86ddb0:8", "const:4:8"]]
+ 0086ddb0 ["CALL", null, ["callee:0046475c:8"]]
- 0083bac4 bytes 8017f097
+ 0086ddb0 bytes 6bdaef97
~~~


<a id="compare-6ba30a8198201b7854f8134b89b437d3"></a>

### [`0083bb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083bb78.md) → [`0086de64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086de64.md) FUN_0086de64

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00829340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829340.md) [`0083bb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083bb78.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0085b2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b2b8.md) [`0086de64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086de64.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.35% / 新版 77.35%

CFGの説明率　旧版 25.41% / 新版 27.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083bb7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083bb7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083bb80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083bb7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083bb80",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083bb84",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0086de68",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0086de6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0086de70",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083bb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083bb78.md#insn-0083bb7c) · [`0083bb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083bb78.md#insn-0083bb80) · [`0083bb84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083bb78.md#insn-0083bb84)

~~~diff
- 0083bb7c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0083bb7c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0083bb7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 0083bb7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083bb7c bytes fd7b0da9
- 0083bb80 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0083bb80 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0083bb80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 0083bb80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083bb80 bytes fc6f0ea9
- 0083bb84 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0083bb84 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0083bb84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 0083bb84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083bb84 bytes fa670fa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e11b100304f23aa278585e3d55dcf28"></a>

### [`0083c478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083c478.md) → [`0086e764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086e/0086e764.md) FUN_0086e764

採用 · 移動量 `+0x322ec` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0083bb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083bb78.md) [`0083c478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083c478.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0086de64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086de64.md) [`0086e764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086e/0086e764.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.41% / 新版 80.41%

CFGの説明率　旧版 25.46% / 新版 32.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 36件, `store_condition` 3件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083c558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083c5fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083c9e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083c4e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086e8f4"
      ]
    ],
    [
      "unmatched:0083c558",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083c55c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086e85c"
      ]
    ]
  ],
  "added": [
    [
      "0086e7d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086e8f4"
      ]
    ],
    [
      "0086e844",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "0086e848",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086e85c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083c4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083c478.md#insn-0083c4e4) · [`0083c544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083c478.md#insn-0083c544) · [`0083c558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083c478.md#insn-0083c558)

~~~diff
- 0083c4e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 0083c4e4 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 0083c4e4 bytes 2b090054
- 0083c544 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0083c544 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0083c544 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0083c544 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0083c544 bytes 1a31899a
- 0083c558 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0083c558 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe0:8"]]
- 0083c558 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0083c558 bytes a8031e38
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8534769729c0bedf2bbfeb87a72606e1"></a>

### [`0083cdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083cdb0.md) → [`0086f09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f09c.md) FUN_0086f09c

採用 · 移動量 `+0x322ec` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0083c478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083c478.md) [`0083cdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083cdb0.md) [`008648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00864/008648a8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`0086e764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086e/0086e764.md) [`0086f09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f09c.md) [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.53% / 新版 85.53%

CFGの説明率　旧版 32.73% / 新版 40.60%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083cde0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083ce88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083d140"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083cde0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083ce00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086f2c0"
      ]
    ],
    [
      "unmatched:0083ce48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086f110"
      ]
    ]
  ],
  "added": [
    [
      "0086f0cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "0086f0ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086f2c0"
      ]
    ],
    [
      "0086f134",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086f110"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083cde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083cdb0.md#insn-0083cde0) · [`0083ce00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083cdb0.md#insn-0083ce00) · [`0083ce48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083c/0083cdb0.md#insn-0083ce48)

~~~diff
- 0083cde0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0083cde0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0083cde0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0083cde0 bytes a9831ff8
- 0083ce00 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0083ce00 ["CBRANCH", null, ["local:b38:8", "tmp:0:1"]]
- 0083ce00 bytes a30e0054
- 0083ce48 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 0083ce48 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0083ce48 bytes eafeff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a4fd7ded9572aeb89a6ec60171dc345"></a>

### [`0083d5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083d5f0.md) → [`0086f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f8dc.md) FUN_0086f8dc

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`0042aea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042a/0042aea8.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f78.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0044dd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dd40.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.42% / 新版 83.42%

CFGの説明率　旧版 25.51% / 新版 32.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083d5f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083d5f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083d5f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083d5f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083d5f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083d5fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0086f8e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0086f8e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0086f8e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083d5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083d5f0.md#insn-0083d5f4) · [`0083d5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083d5f0.md#insn-0083d5f8) · [`0083d5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083d5f0.md#insn-0083d5fc)

~~~diff
- 0083d5f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0083d5f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0083d5f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 0083d5f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083d5f4 bytes fd7b0ea9
- 0083d5f8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0083d5f8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0083d5f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 0083d5f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083d5f8 bytes fc570fa9
- 0083d5fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0083d5fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0083d5fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 0083d5fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083d5fc bytes f44f10a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b89dfd36282f456bae8411cc0e07140"></a>

### [`0083daa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083daa8.md) → [`0086fd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fd94.md) FUN_0086fd94

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0086fda0",
      "incomplete_value": false,
      "site": "0086fda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083dab4",
      "incomplete_value": false,
      "site": "0083dab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:628:8"
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
      "0086fda0",
      "DATA",
      [
        "storage",
        "00c01628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086fda0",
      "DATA",
      [
        "storage",
        "00c7f260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083daac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083daa8.md#insn-0083daac) · [`0083dab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083daa8.md#insn-0083dab0)
- 新版 `0086fd98`（命令位置の公開資料なし） · `0086fd9c`（命令位置の公開資料なし）

~~~diff
- 0083daac ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 0086fd98 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0083daac bytes 291e0090
+ 0086fd98 bytes 89200090
- 0083dab0 ["COPY", "tmp:0:8", ["const:628:8"]]
- 0083dab0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083dab0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083dab0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086fd9c ["COPY", "tmp:0:8", ["const:260:8"]]
+ 0086fd9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086fd9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086fd9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083dab0 bytes 29a11891
+ 0086fd9c bytes 29810991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6caa49ae214de82cc8bf7a78725f89ea"></a>

### [`0083db90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083db90.md) → [`0086fe7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fe7c.md) FUN_0086fe7c

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0086fe80",
      "incomplete_value": false,
      "site": "0086fe84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083db94",
      "incomplete_value": false,
      "site": "0083db98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:708:8"
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
      "0086fe84",
      "DATA",
      [
        "storage",
        "00c01708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086fe84",
      "DATA",
      [
        "storage",
        "00c7f340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083db90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083db90.md#insn-0083db90) · [`0083db94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083db90.md#insn-0083db94)
- 新版 `0086fe7c`（命令位置の公開資料なし） · `0086fe80`（命令位置の公開資料なし）

~~~diff
- 0083db90 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 0086fe7c ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0083db90 bytes 281e0090
+ 0086fe7c bytes 88200090
- 0083db94 ["COPY", "tmp:0:8", ["const:708:8"]]
- 0083db94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083db94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083db94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0086fe80 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 0086fe80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0086fe80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0086fe80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083db94 bytes 08211c91
+ 0086fe80 bytes 08010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-024ba331fed6a04de26230b153e30575"></a>

### [`0083dbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dbdc.md) → [`0086fec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fec8.md) FUN_0086fec8

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0083dbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dbb0.md) [`0083df14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083df14.md) · 呼出先 7件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0052dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad8.md) [`0052dae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dae4.md) [`00574ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff0.md) [`00a28788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28788.md)
- 新版 呼出元 2件 [`0086fe9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086fe9c.md) [`00870200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870200.md) · 呼出先 7件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00550970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550970.md) [`0055097c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055097c.md) [`00597e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e88.md) [`00a86618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86618.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.69% / 新版 78.69%

CFGの説明率　旧版 60.87% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083dbe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083dbe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083dbe4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083dbe0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083dbe4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083dbf4",
      "PARAM",
      [
        "storage",
        "00c34440",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0086fecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0086fed0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0086fee0",
      "PARAM",
      [
        "storage",
        "00cb4178",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083dbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dbdc.md#insn-0083dbe0) · [`0083dbe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dbdc.md#insn-0083dbe4) · [`0083dbfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dbdc.md#insn-0083dbfc)

~~~diff
- 0083dbe0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0083dbe0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0083dbe0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 0083dbe0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083dbe0 bytes fd7b0ca9
- 0083dbe4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0083dbe4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0083dbe4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 0083dbe4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083dbe4 bytes f44f0da9
- 0083dbfc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0083dbfc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0083dbfc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0083dbfc bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fb908a36159e075e3d737bd54e8e45a"></a>

### [`0083debc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083debc.md) → [`008701a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/008701a8.md) FUN_008701a8

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008701c8",
      "incomplete_value": false,
      "site": "008701cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083dedc",
      "incomplete_value": false,
      "site": "0083dee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "008701cc",
      "DATA",
      [
        "storage",
        "00c01788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008701cc",
      "DATA",
      [
        "storage",
        "00c7f3c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083ded0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083debc.md#insn-0083ded0) · [`0083ded8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083debc.md#insn-0083ded8) · [`0083dedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083debc.md#insn-0083dedc)
- 新版 `008701bc`（命令位置の公開資料なし） · `008701c4`（命令位置の公開資料なし） · `008701c8`（命令位置の公開資料なし）

~~~diff
- 0083ded0 ["INT_ADD", "register:40f0:8", ["const:83ded0:8", "const:4:8"]]
- 0083ded0 ["CALL", null, ["callee:00c57a90:8"]]
+ 008701bc ["INT_ADD", "register:40f0:8", ["const:8701bc:8", "const:4:8"]]
+ 008701bc ["CALL", null, ["callee:00c57a90:8"]]
- 0083ded0 bytes 5c740e94
+ 008701bc bytes 359e0f94
- 0083ded8 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 008701c4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0083ded8 bytes 281e0090
+ 008701c4 bytes 682000f0
- 0083dedc ["COPY", "tmp:0:8", ["const:788:8"]]
- 0083dedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083dedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083dedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008701c8 ["COPY", "tmp:0:8", ["const:3c0:8"]]
+ 008701c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008701c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008701c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083dedc bytes 08211e91
+ 008701c8 bytes 08010f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-186236cb3bae550cbb902159cb71d759"></a>

### [`0083df44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083df44.md) → [`00870230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870230.md) FUN_00870230

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 35.71% / 新版 35.71%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083df44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083df44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083df48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083df44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083df48",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083df68",
      "DATA",
      [
        "storage",
        "00c01808",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00870230",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00870234",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00870254",
      "DATA",
      [
        "storage",
        "00c7f440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083df44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083df44.md#insn-0083df44) · [`0083df48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083df44.md#insn-0083df48) · [`0083df58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083df44.md#insn-0083df58)
- 新版 `00870244`（命令位置の公開資料なし）

~~~diff
- 0083df44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0083df44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0083df44 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0083df44 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0083df44 bytes fd7bbea9
- 0083df48 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0083df48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0083df48 bytes f30b00f9
- 0083df58 ["INT_ADD", "register:40f0:8", ["const:83df58:8", "const:4:8"]]
- 0083df58 ["CALL", null, ["callee:00c57a90:8"]]
+ 00870244 ["INT_ADD", "register:40f0:8", ["const:870244:8", "const:4:8"]]
+ 00870244 ["CALL", null, ["callee:00c57a90:8"]]
- 0083df58 bytes 3a740e94
+ 00870244 bytes 139e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39903a4f229ef40c5f19b8f84bde6360"></a>

### [`0083dfc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dfc8.md) → [`008702b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/008702b4.md) FUN_008702b4

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0083df9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083df9c.md) [`0083e950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e950.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`0052dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad8.md)
- 新版 呼出元 2件 [`00870288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870288.md) [`00870c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c3c.md) · 呼出先 16件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00550970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550970.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.92% / 新版 62.92%

CFGの説明率　旧版 28.18% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件, `unresolved_branch_alignment` 16件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 37件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083e008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083e00c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083e010"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083dff8",
      "READ",
      [
        "storage",
        "0029eb0a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0083dffc",
      "READ",
      [
        "storage",
        "0029eb11",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0083e008",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008702e4",
      "READ",
      [
        "storage",
        "002aee89",
        null,
        "string"
      ]
    ],
    [
      "008702e8",
      "READ",
      [
        "storage",
        "002aee90",
        null,
        "string"
      ]
    ],
    [
      "008702f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083e008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dfc8.md#insn-0083e008) · [`0083e00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dfc8.md#insn-0083e00c) · [`0083e010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dfc8.md#insn-0083e010)

~~~diff
- 0083e008 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0083e008 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 0083e008 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0083e008 bytes a8831ef8
- 0083e00c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0083e00c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd0:8"]]
- 0083e00c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0083e00c bytes aa031d38
- 0083e010 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0083e010 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "const:19:8"]]
- 0083e010 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0083e010 bytes f39201f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab24c5b91efcbe35cbe84e89b55f21e8"></a>

### [`0083e8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e8f8.md) → [`00870be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870be4.md) FUN_00870be4

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00870c04",
      "incomplete_value": false,
      "site": "00870c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083e918",
      "incomplete_value": false,
      "site": "0083e91c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:888:8"
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
      "00870c08",
      "DATA",
      [
        "storage",
        "00c01888",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00870c08",
      "DATA",
      [
        "storage",
        "00c7f4c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083e90c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e8f8.md#insn-0083e90c) · [`0083e914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e8f8.md#insn-0083e914) · [`0083e918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e8f8.md#insn-0083e918)
- 新版 `00870bf8`（命令位置の公開資料なし） · `00870c00`（命令位置の公開資料なし） · `00870c04`（命令位置の公開資料なし）

~~~diff
- 0083e90c ["INT_ADD", "register:40f0:8", ["const:83e90c:8", "const:4:8"]]
- 0083e90c ["CALL", null, ["callee:00c57a90:8"]]
+ 00870bf8 ["INT_ADD", "register:40f0:8", ["const:870bf8:8", "const:4:8"]]
+ 00870bf8 ["CALL", null, ["callee:00c57a90:8"]]
- 0083e90c bytes cd710e94
+ 00870bf8 bytes a69b0f94
- 0083e914 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 00870c00 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0083e914 bytes 081e00f0
+ 00870c00 bytes 682000f0
- 0083e918 ["COPY", "tmp:0:8", ["const:888:8"]]
- 0083e918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083e918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083e918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00870c04 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00870c04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00870c04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00870c04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083e918 bytes 08212291
+ 00870c04 bytes 08011391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89ed0e18d1b1167c10f0d785ff5b5953"></a>

### [`0083e930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e930.md) → [`00870c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c1c.md) FUN_00870c1c

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00870c20",
      "incomplete_value": false,
      "site": "00870c24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083e934",
      "incomplete_value": false,
      "site": "0083e938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:888:8"
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
      "00870c24",
      "DATA",
      [
        "storage",
        "00c01888",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00870c24",
      "DATA",
      [
        "storage",
        "00c7f4c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083e930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e930.md#insn-0083e930) · [`0083e934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e930.md#insn-0083e934)
- 新版 `00870c1c`（命令位置の公開資料なし） · `00870c20`（命令位置の公開資料なし）

~~~diff
- 0083e930 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 00870c1c ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0083e930 bytes 081e00f0
+ 00870c1c bytes 682000f0
- 0083e934 ["COPY", "tmp:0:8", ["const:888:8"]]
- 0083e934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083e934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083e934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00870c20 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00870c20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00870c20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00870c20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083e934 bytes 08212291
+ 00870c20 bytes 08011391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9be6874efe3069d46ec6b331f771ff37"></a>

### [`0083e97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e97c.md) → [`00870c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c68.md) FUN_00870c68

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0082b53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082b/0082b53c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0085d4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085d/0085d4b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00870c78",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0083e98c",
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
      "definition_site": "00870c74",
      "incomplete_value": false,
      "site": "00870c78",
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
      "definition_site": "0083e988",
      "incomplete_value": false,
      "site": "0083e98c",
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
      "00870c74",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00870c78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00870c74",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00870c78",
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

- 旧版 [`0083e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e97c.md#insn-0083e98c) · [`0083e984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e97c.md#insn-0083e984) · [`0083e988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e97c.md#insn-0083e988)
- 新版 `00870c78`（命令位置の公開資料なし） · `00870c70`（命令位置の公開資料なし） · `00870c74`（命令位置の公開資料なし）

~~~diff
- 0083e98c ["INT_ADD", "register:40f0:8", ["const:83e98c:8", "const:4:8"]]
- 0083e98c ["CALL", null, ["ram:418c38:8"]]
+ 00870c78 ["INT_ADD", "register:40f0:8", ["const:870c78:8", "const:4:8"]]
+ 00870c78 ["CALL", null, ["ram:43b738:8"]]
- 0083e98c bytes ab68ef97
+ 00870c78 bytes b02aef97
- 0083e984 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00870c70 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0083e984 bytes 40d3ffb0
+ 00870c70 bytes 20d2fff0
- 0083e988 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0083e988 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0083e988 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0083e988 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00870c74 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00870c74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00870c74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00870c74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0083e988 bytes 00740e91
+ 00870c74 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f715a42429766d05a346da9e136b747"></a>

### [`0083e990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e990.md) → [`00870c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md) FUN_00870c7c

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0082b53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082b/0082b53c.md) [`0083e990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e990.md) [`0083ec90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083ec90.md) · 呼出先 4件 [`0083e990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e990.md) [`0083ec90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083ec90.md) [`0083ef28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083ef28.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`0085d4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085d/0085d4b4.md) [`00870c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md) [`00870f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870f7c.md) · 呼出先 4件 [`00870c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md) [`00870f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870f7c.md) [`00871214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871214.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 31.34% / 新版 39.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083e9a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083e9a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083e9a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083e9a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083e9a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083e9a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00870c8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00870c90",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00870c94",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083e9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e990.md#insn-0083e9a0) · [`0083e9a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e990.md#insn-0083e9a4) · [`0083e9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e990.md#insn-0083e9a8)

~~~diff
- 0083e9a0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0083e9a0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0083e9a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 0083e9a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083e9a0 bytes f85f06a9
- 0083e9a4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0083e9a4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0083e9a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 0083e9a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083e9a4 bytes f65707a9
- 0083e9a8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0083e9a8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0083e9a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 0083e9a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083e9a8 bytes f44f08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b20b7c65773a95902d723be63dea7e7"></a>

### [`0083ec90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083ec90.md) → [`00870f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870f7c.md) FUN_00870f7c

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083e990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e990.md) · 呼出先 1件 [`0083e990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083e990.md)
- 新版 呼出元 1件 [`00870c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md) · 呼出先 1件 [`00870c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00870/00870c7c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.35% / 新版 87.35%

CFGの説明率　旧版 30.77% / 新版 38.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083ed08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083ed64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083eec8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00871034",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0083ed6c"
      ]
    ],
    [
      "unmatched:0083ed68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008711f8"
      ]
    ],
    [
      "unmatched:0083eddc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00871098"
      ]
    ]
  ],
  "added": [
    [
      "00871034",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00871058"
      ]
    ],
    [
      "00871054",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008711f8"
      ]
    ],
    [
      "008710c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00871098"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083ed08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083ec90.md#insn-0083ed08) · [`0083ed64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083ec90.md#insn-0083ed64) · [`0083ed68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083e/0083ec90.md#insn-0083ed68)

~~~diff
- 0083ed08 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0083ed08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0083ed08 bytes 690200f9
- 0083ed64 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0083ed64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0083ed64 bytes 490300f9
- 0083ed68 ["CBRANCH", null, ["local:b45:8", "register:101:1"]]
- 0083ed68 bytes 200d0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0eefc415bc298fc9d1c9bdbb373b04b0"></a>

### [`0083f88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083f88c.md) → [`00871b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871b78.md) FUN_00871b78

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0082f5a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082f/0082f5a4.md) [`008c8580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c8580.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) [`009dd9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dd/009dd9d4.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 4件 [`0086151c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00861/0086151c.md) [`008fc454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fc/008fc454.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) [`00a3a8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3a/00a3a8d0.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.92% / 新版 70.92%

CFGの説明率　旧版 21.43% / 新版 17.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 20件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083f88c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083f88c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083f890"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083f88c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083f890",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083f894",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00871b78",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00871b7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00871b80",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083f88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083f88c.md#insn-0083f88c) · [`0083f890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083f88c.md#insn-0083f890) · [`0083f894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083f88c.md#insn-0083f894)

~~~diff
- 0083f88c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0083f88c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0083f88c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 0083f88c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0083f88c bytes fd7bbba9
- 0083f890 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0083f890 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 0083f890 bytes f90b00f9
- 0083f894 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0083f894 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0083f894 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0083f894 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083f894 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af53126ec744cda02e8043359a4d1280"></a>

### [`0083fb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fb9c.md) → [`00871e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871e88.md) FUN_00871e88

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00871e90",
      "incomplete_value": false,
      "site": "00871e94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fba4",
      "incomplete_value": false,
      "site": "0083fba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a28:8"
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
      "00871e94",
      "DATA",
      [
        "storage",
        "00c01a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871e94",
      "DATA",
      [
        "storage",
        "00c7f660",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fb9c.md#insn-0083fba0) · [`0083fba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fb9c.md#insn-0083fba4)
- 新版 `00871e8c`（命令位置の公開資料なし） · `00871e90`（命令位置の公開資料なし）

~~~diff
- 0083fba0 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 00871e8c ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 0083fba0 bytes 091e00d0
+ 00871e8c bytes 692000d0
- 0083fba4 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 0083fba4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083fba4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083fba4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871e90 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 00871e90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871e90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871e90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083fba4 bytes 29a12891
+ 00871e90 bytes 29811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8f58cfd31d5352cde8a645b0da3da40"></a>

### [`0083fbbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fbbc.md) → [`00871ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871ea8.md) FUN_00871ea8

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 31.25% / 新版 31.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083fbc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083fbd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083fbd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083fbc8",
      "DATA",
      [
        "storage",
        "00c01a28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0083fbcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00871ee4"
      ]
    ],
    [
      "unmatched:0083fbd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00871eb4",
      "DATA",
      [
        "storage",
        "00c7f660",
        null,
        "undefined *"
      ]
    ],
    [
      "00871eb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00871ee4"
      ]
    ],
    [
      "00871ebc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fbbc.md#insn-0083fbc8) · [`0083fbcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fbbc.md#insn-0083fbcc) · [`0083fbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fbbc.md#insn-0083fbd0)

~~~diff
- 0083fbc8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0083fbc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0083fbc8 bytes 090000f9
- 0083fbcc ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 0083fbcc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0083fbcc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0083fbcc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0083fbcc bytes 68010036
- 0083fbd0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0083fbd0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0083fbd0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0083fbd0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0083fbd0 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50aeb35d41a8db580ae5ca509821766f"></a>

### [`0083fbfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fbfc.md) → [`00871ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871ee8.md) FUN_00871ee8

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083fc28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00871f14"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0083fc44",
      "incomplete_value": true,
      "site": "0083fc48",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
      "unmatched:0083fc28",
      "DATA",
      [
        "storage",
        "00c01a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871f14",
      "DATA",
      [
        "storage",
        "00c7f660",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fc28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fbfc.md#insn-0083fc28) · [`0083fc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fbfc.md#insn-0083fc48) · [`0083fc58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fbfc.md#insn-0083fc58)
- 新版 `00871f34`（命令位置の公開資料なし）

~~~diff
- 0083fc28 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 0083fc28 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 0083fc28 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 0083fc28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0083fc28 bytes 0a8400f8
- 0083fc48 ["INT_ADD", "register:40f0:8", ["const:83fc48:8", "const:4:8"]]
- 0083fc48 ["CALL", null, ["callee:0043bae0:8"]]
+ 00871f34 ["INT_ADD", "register:40f0:8", ["const:871f34:8", "const:4:8"]]
+ 00871f34 ["CALL", null, ["callee:0043bae0:8"]]
- 0083fc48 bytes e664ef97
+ 00871f34 bytes eb26ef97
- 0083fc58 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0083fc58 ["RETURN", null, ["register:0:8"]]
- 0083fc58 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f74f1c15f924719bfe1c14b431a01749"></a>

### [`0083fcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fcac.md) → [`00871f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871f98.md) FUN_00871f98

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083fcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fcac.md#insn-0083fcb0)
- 新版 `00871f9c`（命令位置の公開資料なし）

~~~diff
- 0083fcb0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 0083fcb0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0083fcb0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0083fcb0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00871f9c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00871f9c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00871f9c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00871f9c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 0083fcb0 bytes 48000037
+ 00871f9c bytes 48000037
~~~


<a id="compare-6d21abd7fc6b059f275f8db58e3474ce"></a>

### [`0083fcf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fcf4.md) → [`00871fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871fe0.md) FUN_00871fe0

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0083fd5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00872048"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0083fd18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083fd18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ],
    [
      "unmatched:0083fd1c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0048e7a0"
      ]
    ],
    [
      "unmatched:0083fd20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ]
  ],
  "added": [
    [
      "00872004",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00872008",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0048e7a0"
      ]
    ],
    [
      "0087200c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fcf4.md#insn-0083fd18) · [`0083fd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fcf4.md#insn-0083fd1c) · [`0083fd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fcf4.md#insn-0083fd20)

~~~diff
- 0083fd18 ["INT_ADD", "register:40f0:8", ["const:83fd18:8", "const:4:8"]]
- 0083fd18 ["CALL", null, ["ram:469e20:8"]]
- 0083fd18 bytes 42a8f097
- 0083fd1c ["INT_ADD", "register:40f0:8", ["const:83fd1c:8", "const:4:8"]]
- 0083fd1c ["CALL", null, ["callee:0048e7a0:8"]]
- 0083fd1c bytes fbaef097
- 0083fd20 ["INT_ADD", "register:40f0:8", ["const:83fd20:8", "const:4:8"]]
- 0083fd20 ["CALL", null, ["ram:469e20:8"]]
- 0083fd20 bytes 40a8f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b8c9207875a33917007936fcc912666"></a>

### [`0083fdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fdec.md) → [`008720d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008720d8.md) FUN_008720d8

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083fdf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008720e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0083fe14",
      "incomplete_value": true,
      "site": "0083fe18",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:18:8"
              ]
            ]
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
      "unmatched:0083fdf8",
      "DATA",
      [
        "storage",
        "00c01aa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008720e4",
      "DATA",
      [
        "storage",
        "00c7f6e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fdf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fdec.md#insn-0083fdf8) · [`0083fe18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fdec.md#insn-0083fe18)
- 新版 `00872104`（命令位置の公開資料なし） · `008720e4`（命令位置の公開資料なし）

~~~diff
- 0083fdf8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0083fdf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0083fdf8 bytes 090000f9
- 0083fe18 ["INT_ADD", "register:40f0:8", ["const:83fe18:8", "const:4:8"]]
- 0083fe18 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00872104 ["INT_ADD", "register:40f0:8", ["const:872104:8", "const:4:8"]]
+ 00872104 ["CALL", null, ["callee:00c57ab0:8"]]
- 0083fe18 bytes 926c0e94
+ 00872104 bytes 6b960f94
+ 008720e4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008720e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008720e4 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0915f1f59af58869ff73df5a3fab7279"></a>

### [`0083fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fe2c.md) → [`00872118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872118.md) FUN_00872118

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083fe2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083fe2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0083fe30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083fe2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083fe30",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0083fe58",
      "DATA",
      [
        "storage",
        "00c01aa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872118",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087211c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00872144",
      "DATA",
      [
        "storage",
        "00c7f6e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fe2c.md#insn-0083fe2c) · [`0083fe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fe2c.md#insn-0083fe30) · [`0083fe40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fe2c.md#insn-0083fe40)
- 新版 `0087212c`（命令位置の公開資料なし）

~~~diff
- 0083fe2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0083fe2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0083fe2c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0083fe2c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0083fe2c bytes fd7bbea9
- 0083fe30 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0083fe30 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0083fe30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0083fe30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0083fe30 bytes f44f01a9
- 0083fe40 ["INT_ADD", "register:40f0:8", ["const:83fe40:8", "const:4:8"]]
- 0083fe40 ["CALL", null, ["callee:00c57a90:8"]]
+ 0087212c ["INT_ADD", "register:40f0:8", ["const:87212c:8", "const:4:8"]]
+ 0087212c ["CALL", null, ["callee:00c57a90:8"]]
- 0083fe40 bytes 806c0e94
+ 0087212c bytes 59960f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4803057ded60c0826d53f281b9680ea"></a>

### [`0083fea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fea0.md) → [`0087218c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/0087218c.md) FUN_0087218c

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

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
      "definition_site": "00872194",
      "incomplete_value": false,
      "site": "00872194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fea8",
      "incomplete_value": false,
      "site": "0083fea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "00872194",
      "DATA",
      [
        "storage",
        "00c01aa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872194",
      "DATA",
      [
        "storage",
        "00c7f6e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fea0.md#insn-0083fea0) · [`0083fea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fea0.md#insn-0083fea4)
- 新版 `0087218c`（命令位置の公開資料なし） · `00872190`（命令位置の公開資料なし）

~~~diff
- 0083fea0 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 0087218c ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0083fea0 bytes 081e00d0
+ 0087218c bytes 682000b0
- 0083fea4 ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 0083fea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083fea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083fea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872190 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00872190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083fea4 bytes 08a12a91
+ 00872190 bytes 08811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a3db3ef69e761433a73586471cf10b7"></a>

### [`0083fedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fedc.md) → [`008721c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008721c8.md) FUN_008721c8

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0083feec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fedc.md#insn-0083feec)
- 新版 `008721d8`（命令位置の公開資料なし）

~~~diff
- 0083feec 5d6c0e14
+ 008721d8 36960f14
~~~


<a id="compare-6e1456719d5d75034aa5dcedd1b6c1e8"></a>

### [`0083ff24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083ff24.md) → [`00872210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872210.md) FUN_00872210

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0083ff8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00872278"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0083ff48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0083ff48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ],
    [
      "unmatched:0083ff4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0048e7a0"
      ]
    ],
    [
      "unmatched:0083ff50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ]
  ],
  "added": [
    [
      "00872234",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00872238",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0048e7a0"
      ]
    ],
    [
      "0087223c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083ff48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083ff24.md#insn-0083ff48) · [`0083ff4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083ff24.md#insn-0083ff4c) · [`0083ff50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083ff24.md#insn-0083ff50)

~~~diff
- 0083ff48 ["INT_ADD", "register:40f0:8", ["const:83ff48:8", "const:4:8"]]
- 0083ff48 ["CALL", null, ["ram:469e20:8"]]
- 0083ff48 bytes b6a7f097
- 0083ff4c ["INT_ADD", "register:40f0:8", ["const:83ff4c:8", "const:4:8"]]
- 0083ff4c ["CALL", null, ["callee:0048e7a0:8"]]
- 0083ff4c bytes 6faef097
- 0083ff50 ["INT_ADD", "register:40f0:8", ["const:83ff50:8", "const:4:8"]]
- 0083ff50 ["CALL", null, ["ram:469e20:8"]]
- 0083ff50 bytes b4a7f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c90c9f5069c417536d01ec91ff45f48a"></a>

### [`00840274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840274.md) → [`00872560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872560.md) FUN_00872560

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008406c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406c0.md) · 呼出先 5件 [`004618e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/004618e8.md) [`00470ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470ac0.md) [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`008729ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729ac.md) · 呼出先 5件 [`00484780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md) [`00493958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493958.md) [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 24.35% / 新版 24.35%

CFGの説明率　旧版 13.51% / 新版 12.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_destination` 1件, `unresolved_branch_alignment` 26件, `unresolved_call_alignment` 39件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00840278"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00840278"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084027c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00840278",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084027c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008402ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00872564",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00872568",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00872598",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00840278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840274.md#insn-00840278) · [`0084027c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840274.md#insn-0084027c) · [`008402ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840274.md#insn-008402ac)

~~~diff
- 00840278 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00840278 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00840278 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00840278 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00840278 bytes fd7b02a9
- 0084027c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 0084027c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 0084027c bytes f91b00f9
- 008402ac ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008402ac ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008402ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008402ac bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0b22161dbf170d96747bb0d6049f122"></a>

### [`008406e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406e4.md) → [`008729d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729d0.md) FUN_008729d0

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 17件 [`004215a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/004215a0.md) [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md)
- 新版 呼出元 0件  · 呼出先 17件 [`004440a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004440a0.md) [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.54% / 新版 64.54%

CFGの説明率　旧版 16.67% / 新版 17.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 2件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008406e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008406e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008406ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008406e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008406ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008406f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008729d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008729d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008729dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008406e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406e4.md#insn-008406e8) · [`008406ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406e4.md#insn-008406ec) · [`008406f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406e4.md#insn-008406f0)

~~~diff
- 008406e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008406e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008406e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 008406e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008406e8 bytes fd7b09a9
- 008406ec ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008406ec ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008406ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 008406ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008406ec bytes fc6f0aa9
- 008406f0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008406f0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008406f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 008406f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008406f0 bytes fa670ba9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f769acb8a0c9e56963e93699cbea5b69"></a>

### [`00840d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840d6c.md) → [`00873058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873058.md) FUN_00873058

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) [`008443c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443c8.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00574ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 2件 [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) [`008766b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008766b4.md) · 呼出先 12件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00597e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.78% / 新版 70.78%

CFGの説明率　旧版 31.03% / 新版 24.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00840db0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00840db0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00840e18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00840db0",
      "DATA",
      [
        "storage",
        "00c01c28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00840dd0",
      "PARAM",
      [
        "storage",
        "002dbf24",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00840dd8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57d90"
      ]
    ]
  ],
  "added": [
    [
      "0087309c",
      "DATA",
      [
        "storage",
        "00c7f860",
        null,
        "undefined *"
      ]
    ],
    [
      "008730bc",
      "PARAM",
      [
        "storage",
        "002eedf0",
        null,
        "string"
      ]
    ],
    [
      "008730c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57d90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00840db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840d6c.md#insn-00840db0) · [`00840e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840d6c.md#insn-00840e18) · [`00840e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840d6c.md#insn-00840e24)

~~~diff
- 00840db0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00840db0 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00840db0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00840db0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00840db0 bytes 080400a9
- 00840e18 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00840e18 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:19:8"]]
- 00840e18 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00840e18 bytes e89301f8
- 00840e24 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00840e24 ["COPY", "tmp:1:8", ["register:8:8"]]
- 00840e24 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00840e24 bytes e9030039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf34d2b1c545591d0dd883b042088faa"></a>

### [`00841168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841168.md) → [`00873454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873454.md) FUN_00873454

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.40% / 新版 81.40%

CFGの説明率　旧版 64.29% / 新版 56.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00841168"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00841168"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084116c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00841168",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084116c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00841184",
      "DATA",
      [
        "storage",
        "00c01c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873454",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00873458",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00873470",
      "DATA",
      [
        "storage",
        "00c7f860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00841168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841168.md#insn-00841168) · [`0084116c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841168.md#insn-0084116c) · [`00841184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841168.md#insn-00841184)

~~~diff
- 00841168 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00841168 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00841168 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00841168 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00841168 bytes fd7bbea9
- 0084116c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0084116c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0084116c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0084116c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084116c bytes f44f01a9
- 00841184 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00841184 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00841184 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00b98b791087d580d1c9320638d1dcab"></a>

### [`00841214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841214.md) → [`00873500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873500.md) FUN_00873500

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 84.62% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00873518",
      "incomplete_value": false,
      "site": "0087351c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084122c",
      "incomplete_value": false,
      "site": "00841230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "0087351c",
      "DATA",
      [
        "storage",
        "00c01c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087351c",
      "DATA",
      [
        "storage",
        "00c7f860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00841228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841214.md#insn-00841228) · [`0084122c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841214.md#insn-0084122c) · [`0084123c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841214.md#insn-0084123c)
- 新版 `00873514`（命令位置の公開資料なし） · `00873518`（命令位置の公開資料なし） · `00873528`（命令位置の公開資料なし）

~~~diff
- 00841228 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 00873514 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00841228 bytes 091e0090
+ 00873514 bytes 69200090
- 0084122c ["COPY", "tmp:0:8", ["const:c28:8"]]
- 0084122c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084122c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084122c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00873518 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 00873518 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00873518 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00873518 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084122c bytes 29a13091
+ 00873518 bytes 29812191
- 0084123c ["INT_ADD", "register:40f0:8", ["const:84123c:8", "const:4:8"]]
- 0084123c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00873528 ["INT_ADD", "register:40f0:8", ["const:873528:8", "const:4:8"]]
+ 00873528 ["CALL", null, ["callee:00c57ab0:8"]]
- 0084123c bytes 89670e94
+ 00873528 bytes 62910f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-657ea5ee63bce2b513a96b9714994630"></a>

### [`008412b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md) → [`0087359c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md) FUN_0087359c

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 17件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0053dc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dc30.md) [`0073ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073ab94.md)
- 新版 呼出元 0件  · 呼出先 17件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00560ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ac8.md) [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.97% / 新版 80.97%

CFGの説明率　旧版 54.76% / 新版 49.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00841308"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00841310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00841314"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008412d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073e08c"
      ]
    ],
    [
      "008735e0",
      "DATA",
      [
        "storage",
        "003c3718",
        "fde_003c3718",
        "dword"
      ]
    ],
    [
      "unmatched:00841304",
      "READ",
      [
        "storage",
        "002a42fd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008735c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768398"
      ]
    ],
    [
      "008735e0",
      "DATA",
      [
        "storage",
        "003c79f8",
        null,
        "byte[15]"
      ]
    ],
    [
      "008735f0",
      "READ",
      [
        "storage",
        "002b4b6a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00841308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md#insn-00841308) · [`00841310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md#insn-00841310) · [`00841314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md#insn-00841314)

~~~diff
- 00841308 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00841308 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00841308 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:64:8"]]
- 00841308 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00841308 bytes ff930139
- 00841310 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00841310 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00841310 bytes e96300b9
- 00841314 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:51:8"]]
- 00841314 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00841314 bytes e013853c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fd7fca62930d910b26b71bbb7b73312"></a>

### [`0084177c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/0084177c.md) → [`00873a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873a68.md) FUN_00873a68

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008412b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md) [`008427a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008427a8.md) · 呼出先 9件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`0042ca70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca70.md) [`0084224c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084224c.md) [`0084229c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084229c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 2件 [`0087359c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md) [`00874a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874a94.md) · 呼出先 9件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`0044f908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md) [`00874538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874538.md) [`00874588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874588.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.06% / 新版 95.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00873ad0",
      "incomplete_value": false,
      "site": "00873ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008417e4",
      "incomplete_value": false,
      "site": "008417e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "definition_site": "00873af0",
      "incomplete_value": false,
      "site": "00873af0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841804",
      "incomplete_value": false,
      "site": "00841804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "00873ad0",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ],
    [
      "00873af0",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ],
    [
      "00873b30",
      "READ",
      [
        "storage",
        "00c01ca8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00873ad0",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873af0",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873b30",
      "READ",
      [
        "storage",
        "00c7f8e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008417a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/0084177c.md#insn-008417a8) · [`008417cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/0084177c.md#insn-008417cc) · [`008417d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/0084177c.md#insn-008417d0)
- 新版 `00873a94`（命令位置の公開資料なし） · `00873ab8`（命令位置の公開資料なし） · `00873abc`（命令位置の公開資料なし）

~~~diff
- 008417a8 ["INT_ADD", "register:40f0:8", ["const:8417a8:8", "const:4:8"]]
- 008417a8 ["CALL", null, ["callee:0044f8a0:8"]]
+ 00873a94 ["INT_ADD", "register:40f0:8", ["const:873a94:8", "const:4:8"]]
+ 00873a94 ["CALL", null, ["callee:0044f8a0:8"]]
- 008417a8 bytes 98acef97
+ 00873a94 bytes 836fef97
- 008417cc ["INT_ADD", "register:40f0:8", ["const:8417cc:8", "const:4:8"]]
- 008417cc ["CALL", null, ["callee:00c538b0:8"]]
+ 00873ab8 ["INT_ADD", "register:40f0:8", ["const:873ab8:8", "const:4:8"]]
+ 00873ab8 ["CALL", null, ["callee:00c538b0:8"]]
- 008417cc bytes a5550e94
+ 00873ab8 bytes 7e7f0f94
- 008417d0 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 00873abc ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 008417d0 bytes 081e0090
+ 00873abc bytes 68200090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93fed73f5f9ace95532561568ebc2f65"></a>

### [`00841924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841924.md) → [`00873c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873c10.md) FUN_00873c10

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008412b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md) [`008423bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008423bc.md) · 呼出先 7件 [`0084297c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084297c.md) [`008429cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008429cc.md) [`0084d6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d6d0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 2件 [`0087359c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md) [`008746a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008746a8.md) · 呼出先 7件 [`00874c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874c68.md) [`00874cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874cb8.md) [`00880668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00873c70",
      "incomplete_value": false,
      "site": "00873c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841984",
      "incomplete_value": false,
      "site": "00841984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "definition_site": "00873c90",
      "incomplete_value": false,
      "site": "00873c90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008419a4",
      "incomplete_value": false,
      "site": "008419a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "definition_site": "00873ca8",
      "incomplete_value": true,
      "site": "00873cac",
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
                "register:40b0:8"
              ],
              "INT_LEFT"
            ]
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008419bc",
      "incomplete_value": true,
      "site": "008419c0",
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
                "register:40b0:8"
              ],
              "INT_LEFT"
            ]
          ],
          [
            "leaf",
            "const:60:8"
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
      "00873c70",
      "DATA",
      [
        "storage",
        "00c01d88",
        null,
        "undefined *"
      ]
    ],
    [
      "00873c90",
      "DATA",
      [
        "storage",
        "00c01d88",
        null,
        "undefined *"
      ]
    ],
    [
      "00873cd4",
      "READ",
      [
        "storage",
        "00c01da8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00873c70",
      "DATA",
      [
        "storage",
        "00c7f9c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873c90",
      "DATA",
      [
        "storage",
        "00c7f9c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873cd4",
      "READ",
      [
        "storage",
        "00c7f9e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008419c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841924.md#insn-008419c0) · [`0084196c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841924.md#insn-0084196c) · [`00841970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841924.md#insn-00841970)
- 新版 `00873cac`（命令位置の公開資料なし） · `00873c58`（命令位置の公開資料なし） · `00873c5c`（命令位置の公開資料なし）

~~~diff
- 008419c0 ["INT_ADD", "register:40f0:8", ["const:8419c0:8", "const:4:8"]]
- 008419c0 ["CALL", null, ["callee:00880668:8"]]
+ 00873cac ["INT_ADD", "register:40f0:8", ["const:873cac:8", "const:4:8"]]
+ 00873cac ["CALL", null, ["callee:00880668:8"]]
- 008419c0 bytes 442f0094
+ 00873cac bytes 6f320094
- 0084196c ["INT_ADD", "register:40f0:8", ["const:84196c:8", "const:4:8"]]
- 0084196c ["CALL", null, ["callee:00c538b0:8"]]
+ 00873c58 ["INT_ADD", "register:40f0:8", ["const:873c58:8", "const:4:8"]]
+ 00873c58 ["CALL", null, ["callee:00c538b0:8"]]
- 0084196c bytes 3d550e94
+ 00873c58 bytes 167f0f94
- 00841970 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 00873c5c ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00841970 bytes 081e0090
+ 00873c5c bytes 68200090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30ca506871eb287ce520766da83ea888"></a>

### [`00841a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841a9c.md) → [`00873d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873d88.md) FUN_00873d88

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008412b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md) · 呼出先 7件 [`00842db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842db4.md) [`00842e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e04.md) [`0084dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`0087359c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md) · 呼出先 7件 [`008750a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008750a0.md) [`008750f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008750f0.md) [`00880cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.82% / 新版 80.82%

CFGの説明率　旧版 63.16% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00841af8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00841af8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00841afc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00841af8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00841afc",
      "DATA",
      [
        "storage",
        "00c01e08",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00841afc",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00873de4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00873de8",
      "DATA",
      [
        "storage",
        "00c7fa40",
        null,
        "undefined *"
      ]
    ],
    [
      "00873de8",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00841af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841a9c.md#insn-00841af8) · [`00841afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841a9c.md#insn-00841afc) · [`00841b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841a9c.md#insn-00841b18)

~~~diff
- 00841af8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00841af8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00841af8 ["COPY", "tmp:2:8", ["tmp:0:8"]]
- 00841af8 ["INT_ADD", "tmp:3:8", ["register:8:8", "const:38:8"]]
- 00841af8 bytes f3ff03a9
- 00841afc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00841afc ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00841afc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00841afc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00841afc bytes e85302a9
- 00841b18 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00841b18 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00841b18 ["COPY", "tmp:2:8", ["tmp:0:8"]]
- 00841b18 ["INT_ADD", "tmp:3:8", ["register:8:8", "const:38:8"]]
- 00841b18 bytes f3ff03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c782e64cf766d86f6a12bd4526e38af5"></a>

### [`00841c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md) → [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) FUN_00873f00

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`008412b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/008412b0.md) [`00842a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842a50.md) [`00842e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e88.md) [`00843d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843d2c.md) · 呼出先 16件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`00430dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00430/00430dd8.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md) [`0073ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073ab94.md) [`008430b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008430b0.md)
- 新版 呼出元 4件 [`0087359c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/0087359c.md) [`00874d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874d3c.md) [`00875174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875174.md) [`00876018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876018.md) · 呼出先 16件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`00453c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453c70.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`0087539c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087539c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.81% / 新版 83.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00873f5c",
      "incomplete_value": true,
      "site": "00873f5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d4b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841c70",
      "incomplete_value": true,
      "site": "00841c70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:113:8"
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
      "definition_site": "00873f64",
      "incomplete_value": true,
      "site": "00873f64",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00841c78",
      "incomplete_value": true,
      "site": "00841c78",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00873fa8",
      "incomplete_value": true,
      "site": "00873fb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:59b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841cbc",
      "incomplete_value": true,
      "site": "00841ccc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d92:8"
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
      "00873f50",
      "READ",
      [
        "storage",
        "00298113",
        null,
        "string"
      ]
    ],
    [
      "00873f54",
      "READ",
      [
        "storage",
        "00298118",
        null,
        "string"
      ]
    ],
    [
      "00873fa8",
      "READ",
      [
        "storage",
        "00293d92",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00873f50",
      "READ",
      [
        "storage",
        "002a7d4b",
        null,
        "string"
      ]
    ],
    [
      "00873f54",
      "READ",
      [
        "storage",
        "002a7d50",
        null,
        "string"
      ]
    ],
    [
      "00873fa8",
      "READ",
      [
        "storage",
        "002a359b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00841c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md#insn-00841c88) · [`00841cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md#insn-00841cd8) · [`00841d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md#insn-00841d34)
- 新版 `00873f74`（命令位置の公開資料なし） · `00873fc4`（命令位置の公開資料なし） · `00874020`（命令位置の公開資料なし）

~~~diff
- 00841c88 ["INT_ADD", "register:40f0:8", ["const:841c88:8", "const:4:8"]]
- 00841c88 ["CALL", null, ["callee:00b3ba6c:8"]]
+ 00873f74 ["INT_ADD", "register:40f0:8", ["const:873f74:8", "const:4:8"]]
+ 00873f74 ["CALL", null, ["callee:00b3ba6c:8"]]
- 00841c88 bytes 03690a94
+ 00873f74 bytes be1e0b94
- 00841cd8 ["INT_ADD", "register:40f0:8", ["const:841cd8:8", "const:4:8"]]
- 00841cd8 ["CALL", null, ["callee:00b3ba6c:8"]]
+ 00873fc4 ["INT_ADD", "register:40f0:8", ["const:873fc4:8", "const:4:8"]]
+ 00873fc4 ["CALL", null, ["callee:00b3ba6c:8"]]
- 00841cd8 bytes ef680a94
+ 00873fc4 bytes aa1e0b94
- 00841d34 ["INT_ADD", "register:40f0:8", ["const:841d34:8", "const:4:8"]]
- 00841d34 ["CALL", null, ["callee:00b3ba6c:8"]]
+ 00874020 ["INT_ADD", "register:40f0:8", ["const:874020:8", "const:4:8"]]
+ 00874020 ["CALL", null, ["callee:00b3ba6c:8"]]
- 00841d34 bytes d8680a94
+ 00874020 bytes 931e0b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19a9942f87a762176cda82a2d49fdf21"></a>

### [`00842100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842100.md) → [`008743ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008743ec.md) FUN_008743ec

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "00874400",
      "incomplete_value": false,
      "site": "00874404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842114",
      "incomplete_value": false,
      "site": "00842118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "00874404",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874404",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842100.md#insn-00842110) · [`00842114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842100.md#insn-00842114) · [`00842128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842100.md#insn-00842128)
- 新版 `008743fc`（命令位置の公開資料なし） · `00874400`（命令位置の公開資料なし） · `00874414`（命令位置の公開資料なし）

~~~diff
- 00842110 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 008743fc ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00842110 bytes e81d00f0
+ 008743fc bytes 482000f0
- 00842114 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00842114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874400 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00874400 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874400 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874400 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842114 bytes 08213291
+ 00874400 bytes 08012391
- 00842128 ["INT_ADD", "register:40f0:8", ["const:842128:8", "const:4:8"]]
- 00842128 ["CALL", null, ["callee:00c538e0:8"]]
+ 00874414 ["INT_ADD", "register:40f0:8", ["const:874414:8", "const:4:8"]]
+ 00874414 ["CALL", null, ["callee:00c538e0:8"]]
- 00842128 bytes 5a530e94
+ 00874414 bytes 337d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bd7cd50429f94acb66602c66afb3810"></a>

### [`0084215c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084215c.md) → [`00874448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874448.md) FUN_00874448

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00874460",
      "incomplete_value": false,
      "site": "00874464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842174",
      "incomplete_value": false,
      "site": "00842178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "00874464",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874464",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084215c.md#insn-00842170) · [`00842174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084215c.md#insn-00842174) · [`00842188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084215c.md#insn-00842188)
- 新版 `0087445c`（命令位置の公開資料なし） · `00874460`（命令位置の公開資料なし） · `00874474`（命令位置の公開資料なし）

~~~diff
- 00842170 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 0087445c ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00842170 bytes e81d00f0
+ 0087445c bytes 482000f0
- 00842174 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00842174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874460 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00874460 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874460 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874460 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842174 bytes 08213291
+ 00874460 bytes 08012391
- 00842188 ["INT_ADD", "register:40f0:8", ["const:842188:8", "const:4:8"]]
- 00842188 ["CALL", null, ["callee:00c538e0:8"]]
+ 00874474 ["INT_ADD", "register:40f0:8", ["const:874474:8", "const:4:8"]]
+ 00874474 ["CALL", null, ["callee:00c538e0:8"]]
- 00842188 bytes 42530e94
+ 00874474 bytes 1b7d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d72387ec099789f38e1ff2295976d8c"></a>

### [`008421b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008421b8.md) → [`008744a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008744a4.md) FUN_008744a4

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "008744c8",
      "incomplete_value": false,
      "site": "008744cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008421dc",
      "incomplete_value": false,
      "site": "008421e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "008744cc",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008744cc",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008421cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008421b8.md#insn-008421cc) · [`008421d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008421b8.md#insn-008421d8) · [`008421dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008421b8.md#insn-008421dc)
- 新版 `008744b8`（命令位置の公開資料なし） · `008744c4`（命令位置の公開資料なし） · `008744c8`（命令位置の公開資料なし）

~~~diff
- 008421cc ["INT_ADD", "register:40f0:8", ["const:8421cc:8", "const:4:8"]]
- 008421cc ["CALL", null, ["callee:00c57a90:8"]]
+ 008744b8 ["INT_ADD", "register:40f0:8", ["const:8744b8:8", "const:4:8"]]
+ 008744b8 ["CALL", null, ["callee:00c57a90:8"]]
- 008421cc bytes 9d630e94
+ 008744b8 bytes 768d0f94
- 008421d8 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 008744c4 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 008421d8 bytes e91d00f0
+ 008744c4 bytes 492000f0
- 008421dc ["COPY", "tmp:0:8", ["const:c88:8"]]
- 008421dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008421dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008421dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008744c8 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 008744c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008744c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008744c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008421dc bytes 29213291
+ 008744c8 bytes 29012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43ae549dca6fdf5ec709a7f4dc1d8abc"></a>

### [`00842210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842210.md) → [`008744fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008744fc.md) FUN_008744fc

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "00874504",
      "incomplete_value": false,
      "site": "00874508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842218",
      "incomplete_value": false,
      "site": "0084221c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "00874508",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874508",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842210.md#insn-00842214) · [`00842218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842210.md#insn-00842218) · [`00842240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842210.md#insn-00842240)
- 新版 `00874500`（命令位置の公開資料なし） · `00874504`（命令位置の公開資料なし） · `0087452c`（命令位置の公開資料なし）

~~~diff
- 00842214 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 00874500 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00842214 bytes e91d00f0
+ 00874500 bytes 492000f0
- 00842218 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00842218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874504 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00874504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842218 bytes 29213291
+ 00874504 bytes 29012391
- 00842240 ["INT_ADD", "register:40f0:8", ["const:842240:8", "const:4:8"]]
- 00842240 ["CALL", null, ["callee:00c538b0:8"]]
+ 0087452c ["INT_ADD", "register:40f0:8", ["const:87452c:8", "const:4:8"]]
+ 0087452c ["CALL", null, ["callee:00c538b0:8"]]
- 00842240 bytes 08530e94
+ 0087452c bytes e17c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e60f9059a9b5d7aa3c2564fd6ad1644"></a>

### [`0084224c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084224c.md) → [`00874538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874538.md) FUN_00874538

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0084177c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/0084177c.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00873a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873a68.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 16.67% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084225c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084224c.md#insn-0084225c) · [`00842268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084224c.md#insn-00842268) · [`0084226c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084224c.md#insn-0084226c)
- 新版 `00874548`（命令位置の公開資料なし） · `00874554`（命令位置の公開資料なし） · `00874558`（命令位置の公開資料なし）

~~~diff
- 0084225c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 0084225c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00874548 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00874548 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0084225c bytes b30000b4
+ 00874548 bytes b30000b4
- 00842268 ["INT_ADD", "register:40f0:8", ["const:842268:8", "const:4:8"]]
- 00842268 ["CALL", null, ["callee:00c538e0:8"]]
+ 00874554 ["INT_ADD", "register:40f0:8", ["const:874554:8", "const:4:8"]]
+ 00874554 ["CALL", null, ["callee:00c538e0:8"]]
- 00842268 bytes 0a530e94
+ 00874554 bytes e37c0f94
- 0084226c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0084226c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00874558 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00874558 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0084226c bytes 800000b4
+ 00874558 bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cb373c1111eab251c546587728a4ac2"></a>

### [`008423bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008423bc.md) → [`008746a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008746a8.md) FUN_008746a8

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008422ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008422ec.md) · 呼出先 7件 [`00841924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841924.md) [`00842708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842708.md) [`00842758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842758.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`008745d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008745d8.md) · 呼出先 7件 [`00873c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873c10.md) [`008749f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008749f4.md) [`00874a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874a44.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00874744",
      "incomplete_value": false,
      "site": "00874744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842458",
      "incomplete_value": false,
      "site": "00842458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00874760",
      "incomplete_value": false,
      "site": "00874760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842474",
      "incomplete_value": false,
      "site": "00842474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "00874744",
      "DATA",
      [
        "storage",
        "00c01cf8",
        null,
        "undefined *"
      ]
    ],
    [
      "00874760",
      "DATA",
      [
        "storage",
        "00c01cf8",
        null,
        "undefined *"
      ]
    ],
    [
      "008747a8",
      "READ",
      [
        "storage",
        "00c01d18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00874744",
      "DATA",
      [
        "storage",
        "00c7f930",
        null,
        "undefined *"
      ]
    ],
    [
      "00874760",
      "DATA",
      [
        "storage",
        "00c7f930",
        null,
        "undefined *"
      ]
    ],
    [
      "008747a8",
      "READ",
      [
        "storage",
        "00c7f950",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008423bc.md#insn-00842440) · [`00842444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008423bc.md#insn-00842444) · [`00842448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008423bc.md#insn-00842448)
- 新版 `0087472c`（命令位置の公開資料なし） · `00874730`（命令位置の公開資料なし） · `00874734`（命令位置の公開資料なし）

~~~diff
- 00842440 ["INT_ADD", "register:40f0:8", ["const:842440:8", "const:4:8"]]
- 00842440 ["CALL", null, ["callee:00c538b0:8"]]
+ 0087472c ["INT_ADD", "register:40f0:8", ["const:87472c:8", "const:4:8"]]
+ 0087472c ["CALL", null, ["callee:00c538b0:8"]]
- 00842440 bytes 88520e94
+ 0087472c bytes 617c0f94
- 00842444 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 00874730 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00842444 bytes e81d00f0
+ 00874730 bytes 482000f0
- 00842448 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 00842448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874734 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 00874734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842448 bytes 08e13391
+ 00874734 bytes 08c12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27c35217e604c59c391b6956576305a7"></a>

### [`008425bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008425bc.md) → [`008748a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008748a8.md) FUN_008748a8

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "008748bc",
      "incomplete_value": false,
      "site": "008748c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008425d0",
      "incomplete_value": false,
      "site": "008425d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "008748c0",
      "DATA",
      [
        "storage",
        "00c01cf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008748c0",
      "DATA",
      [
        "storage",
        "00c7f930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008425cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008425bc.md#insn-008425cc) · [`008425d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008425bc.md#insn-008425d0) · [`008425e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008425bc.md#insn-008425e4)
- 新版 `008748b8`（命令位置の公開資料なし） · `008748bc`（命令位置の公開資料なし） · `008748d0`（命令位置の公開資料なし）

~~~diff
- 008425cc ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 008748b8 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 008425cc bytes e81d00f0
+ 008748b8 bytes 482000f0
- 008425d0 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 008425d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008425d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008425d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008748bc ["COPY", "tmp:0:8", ["const:930:8"]]
+ 008748bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008748bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008748bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008425d0 bytes 08e13391
+ 008748bc bytes 08c12491
- 008425e4 ["INT_ADD", "register:40f0:8", ["const:8425e4:8", "const:4:8"]]
- 008425e4 ["CALL", null, ["callee:00c538e0:8"]]
+ 008748d0 ["INT_ADD", "register:40f0:8", ["const:8748d0:8", "const:4:8"]]
+ 008748d0 ["CALL", null, ["callee:00c538e0:8"]]
- 008425e4 bytes 2b520e94
+ 008748d0 bytes 047c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-008fbfc252c2d532ab458f21b5f4379b"></a>

### [`00842618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842618.md) → [`00874904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874904.md) FUN_00874904

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0087491c",
      "incomplete_value": false,
      "site": "00874920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842630",
      "incomplete_value": false,
      "site": "00842634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "00874920",
      "DATA",
      [
        "storage",
        "00c01cf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874920",
      "DATA",
      [
        "storage",
        "00c7f930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084262c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842618.md#insn-0084262c) · [`00842630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842618.md#insn-00842630) · [`00842644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842618.md#insn-00842644)
- 新版 `00874918`（命令位置の公開資料なし） · `0087491c`（命令位置の公開資料なし） · `00874930`（命令位置の公開資料なし）

~~~diff
- 0084262c ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 00874918 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0084262c bytes e81d00f0
+ 00874918 bytes 482000f0
- 00842630 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 00842630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087491c ["COPY", "tmp:0:8", ["const:930:8"]]
+ 0087491c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087491c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087491c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842630 bytes 08e13391
+ 0087491c bytes 08c12491
- 00842644 ["INT_ADD", "register:40f0:8", ["const:842644:8", "const:4:8"]]
- 00842644 ["CALL", null, ["callee:00c538e0:8"]]
+ 00874930 ["INT_ADD", "register:40f0:8", ["const:874930:8", "const:4:8"]]
+ 00874930 ["CALL", null, ["callee:00c538e0:8"]]
- 00842644 bytes 13520e94
+ 00874930 bytes ec7b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d28a94c7d193ecd1160ddaf39f0bdcb7"></a>

### [`00842674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842674.md) → [`00874960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874960.md) FUN_00874960

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00874984",
      "incomplete_value": false,
      "site": "00874988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842698",
      "incomplete_value": false,
      "site": "0084269c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "00874988",
      "DATA",
      [
        "storage",
        "00c01cf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874988",
      "DATA",
      [
        "storage",
        "00c7f930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842674.md#insn-00842688) · [`00842694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842674.md#insn-00842694) · [`00842698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842674.md#insn-00842698)
- 新版 `00874974`（命令位置の公開資料なし） · `00874980`（命令位置の公開資料なし） · `00874984`（命令位置の公開資料なし）

~~~diff
- 00842688 ["INT_ADD", "register:40f0:8", ["const:842688:8", "const:4:8"]]
- 00842688 ["CALL", null, ["callee:00c57a90:8"]]
+ 00874974 ["INT_ADD", "register:40f0:8", ["const:874974:8", "const:4:8"]]
+ 00874974 ["CALL", null, ["callee:00c57a90:8"]]
- 00842688 bytes 6e620e94
+ 00874974 bytes 478c0f94
- 00842694 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 00874980 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00842694 bytes e91d00f0
+ 00874980 bytes 492000f0
- 00842698 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 00842698 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842698 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842698 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874984 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 00874984 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874984 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874984 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842698 bytes 29e13391
+ 00874984 bytes 29c12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d871149925545dc12499b2c3668ca1b2"></a>

### [`008426cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008426cc.md) → [`008749b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008749b8.md) FUN_008749b8

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "008749c0",
      "incomplete_value": false,
      "site": "008749c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008426d4",
      "incomplete_value": false,
      "site": "008426d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "008749c4",
      "DATA",
      [
        "storage",
        "00c01cf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008749c4",
      "DATA",
      [
        "storage",
        "00c7f930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008426d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008426cc.md#insn-008426d0) · [`008426d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008426cc.md#insn-008426d4) · [`008426fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008426cc.md#insn-008426fc)
- 新版 `008749bc`（命令位置の公開資料なし） · `008749c0`（命令位置の公開資料なし） · `008749e8`（命令位置の公開資料なし）

~~~diff
- 008426d0 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 008749bc ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 008426d0 bytes e91d00f0
+ 008749bc bytes 492000f0
- 008426d4 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 008426d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008426d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008426d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008749c0 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 008749c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008749c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008749c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008426d4 bytes 29e13391
+ 008749c0 bytes 29c12491
- 008426fc ["INT_ADD", "register:40f0:8", ["const:8426fc:8", "const:4:8"]]
- 008426fc ["CALL", null, ["callee:00c538b0:8"]]
+ 008749e8 ["INT_ADD", "register:40f0:8", ["const:8749e8:8", "const:4:8"]]
+ 008749e8 ["CALL", null, ["callee:00c538b0:8"]]
- 008426fc bytes d9510e94
+ 008749e8 bytes b27b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1fbeb1c49cb3142ca5edb37f825f09e"></a>

### [`00842830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842830.md) → [`00874b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874b1c.md) FUN_00874b1c

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "00874b30",
      "incomplete_value": false,
      "site": "00874b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842844",
      "incomplete_value": false,
      "site": "00842848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "00874b34",
      "DATA",
      [
        "storage",
        "00c01d88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874b34",
      "DATA",
      [
        "storage",
        "00c7f9c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842830.md#insn-00842840) · [`00842844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842830.md#insn-00842844) · [`00842858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842830.md#insn-00842858)
- 新版 `00874b2c`（命令位置の公開資料なし） · `00874b30`（命令位置の公開資料なし） · `00874b44`（命令位置の公開資料なし）

~~~diff
- 00842840 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 00874b2c ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00842840 bytes e81d00f0
+ 00874b2c bytes 482000f0
- 00842844 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 00842844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874b30 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00874b30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874b30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874b30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842844 bytes 08213691
+ 00874b30 bytes 08012791
- 00842858 ["INT_ADD", "register:40f0:8", ["const:842858:8", "const:4:8"]]
- 00842858 ["CALL", null, ["callee:00c538e0:8"]]
+ 00874b44 ["INT_ADD", "register:40f0:8", ["const:874b44:8", "const:4:8"]]
+ 00874b44 ["CALL", null, ["callee:00c538e0:8"]]
- 00842858 bytes 8e510e94
+ 00874b44 bytes 677b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c97d3785fb0239e479e7b91fb2ef170"></a>

### [`0084288c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084288c.md) → [`00874b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874b78.md) FUN_00874b78

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00874b90",
      "incomplete_value": false,
      "site": "00874b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008428a4",
      "incomplete_value": false,
      "site": "008428a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "00874b94",
      "DATA",
      [
        "storage",
        "00c01d88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874b94",
      "DATA",
      [
        "storage",
        "00c7f9c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008428a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084288c.md#insn-008428a0) · [`008428a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084288c.md#insn-008428a4) · [`008428b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/0084288c.md#insn-008428b8)
- 新版 `00874b8c`（命令位置の公開資料なし） · `00874b90`（命令位置の公開資料なし） · `00874ba4`（命令位置の公開資料なし）

~~~diff
- 008428a0 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 00874b8c ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 008428a0 bytes e81d00f0
+ 00874b8c bytes 482000f0
- 008428a4 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 008428a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008428a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008428a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874b90 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00874b90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874b90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874b90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008428a4 bytes 08213691
+ 00874b90 bytes 08012791
- 008428b8 ["INT_ADD", "register:40f0:8", ["const:8428b8:8", "const:4:8"]]
- 008428b8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00874ba4 ["INT_ADD", "register:40f0:8", ["const:874ba4:8", "const:4:8"]]
+ 00874ba4 ["CALL", null, ["callee:00c538e0:8"]]
- 008428b8 bytes 76510e94
+ 00874ba4 bytes 4f7b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d81f126407050642be54eadf9c62a570"></a>

### [`008428e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008428e8.md) → [`00874bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874bd4.md) FUN_00874bd4

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00874bf8",
      "incomplete_value": false,
      "site": "00874bfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084290c",
      "incomplete_value": false,
      "site": "00842910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "00874bfc",
      "DATA",
      [
        "storage",
        "00c01d88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874bfc",
      "DATA",
      [
        "storage",
        "00c7f9c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008428fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008428e8.md#insn-008428fc) · [`00842908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008428e8.md#insn-00842908) · [`0084290c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/008428e8.md#insn-0084290c)
- 新版 `00874be8`（命令位置の公開資料なし） · `00874bf4`（命令位置の公開資料なし） · `00874bf8`（命令位置の公開資料なし）

~~~diff
- 008428fc ["INT_ADD", "register:40f0:8", ["const:8428fc:8", "const:4:8"]]
- 008428fc ["CALL", null, ["callee:00c57a90:8"]]
+ 00874be8 ["INT_ADD", "register:40f0:8", ["const:874be8:8", "const:4:8"]]
+ 00874be8 ["CALL", null, ["callee:00c57a90:8"]]
- 008428fc bytes d1610e94
+ 00874be8 bytes aa8b0f94
- 00842908 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 00874bf4 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00842908 bytes e91d00f0
+ 00874bf4 bytes 492000f0
- 0084290c ["COPY", "tmp:0:8", ["const:d88:8"]]
- 0084290c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084290c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084290c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874bf8 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00874bf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874bf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874bf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084290c bytes 29213691
+ 00874bf8 bytes 29012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2e075d1b99ff112f0cd22bf511103c8"></a>

### [`00842940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842940.md) → [`00874c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874c2c.md) FUN_00874c2c

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "00874c34",
      "incomplete_value": false,
      "site": "00874c38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842948",
      "incomplete_value": false,
      "site": "0084294c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "00874c38",
      "DATA",
      [
        "storage",
        "00c01d88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874c38",
      "DATA",
      [
        "storage",
        "00c7f9c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842940.md#insn-00842944) · [`00842948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842940.md#insn-00842948) · [`00842970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842940.md#insn-00842970)
- 新版 `00874c30`（命令位置の公開資料なし） · `00874c34`（命令位置の公開資料なし） · `00874c5c`（命令位置の公開資料なし）

~~~diff
- 00842944 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 00874c30 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00842944 bytes e91d00f0
+ 00874c30 bytes 492000f0
- 00842948 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 00842948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874c34 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00874c34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874c34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874c34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842948 bytes 29213691
+ 00874c34 bytes 29012791
- 00842970 ["INT_ADD", "register:40f0:8", ["const:842970:8", "const:4:8"]]
- 00842970 ["CALL", null, ["callee:00c538b0:8"]]
+ 00874c5c ["INT_ADD", "register:40f0:8", ["const:874c5c:8", "const:4:8"]]
+ 00874c5c ["CALL", null, ["callee:00c538b0:8"]]
- 00842970 bytes 3c510e94
+ 00874c5c bytes 157b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-553e905a65af0bb765d07801eed3d458"></a>

### [`00842a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842a50.md) → [`00874d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874d3c.md) FUN_00874d3c

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00842a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842a1c.md) · 呼出先 6件 [`00574ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md) [`00841c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md) [`009bd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd618.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00874d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874d08.md) · 呼出先 6件 [`00597e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md) [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 71.29% / 新版 71.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874d90",
      "incomplete_value": true,
      "site": "00874d98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00842aa4",
      "incomplete_value": true,
      "site": "00842aac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a90:8"
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
      "definition_site": "00874d8c",
      "incomplete_value": true,
      "site": "00874d9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842aa0",
      "incomplete_value": true,
      "site": "00842ab0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:ec3:8"
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
      "definition_site": "00874d8c",
      "incomplete_value": true,
      "site": "00874d9c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00842aa0",
      "incomplete_value": true,
      "site": "00842ab0",
      "value": [
        "LOAD",
        "16",
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
      "00874d8c",
      "READ",
      [
        "storage",
        "00294ec3",
        null,
        "string"
      ]
    ],
    [
      "00874d8c",
      "READ",
      [
        "storage",
        "00294ed3",
        null,
        "string"
      ]
    ],
    [
      "00874d90",
      "READ",
      [
        "storage",
        "002b1a90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00874d8c",
      "READ",
      [
        "storage",
        "002a47df",
        null,
        "string"
      ]
    ],
    [
      "00874d8c",
      "READ",
      [
        "storage",
        "002a47ef",
        null,
        "string"
      ]
    ],
    [
      "00874d90",
      "READ",
      [
        "storage",
        "002c3160",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842a50.md#insn-00842b88) · [`00842a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842a50.md#insn-00842a90) · [`00842a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842a50.md#insn-00842a94)
- 新版 `00874e74`（命令位置の公開資料なし） · `00874d7c`（命令位置の公開資料なし） · `00874d80`（命令位置の公開資料なし）

~~~diff
- 00842b88 ["INT_ADD", "register:40f0:8", ["const:842b88:8", "const:4:8"]]
- 00842b88 ["CALL", null, ["callee:00a1a508:8"]]
+ 00874e74 ["INT_ADD", "register:40f0:8", ["const:874e74:8", "const:4:8"]]
+ 00874e74 ["CALL", null, ["callee:00a1a508:8"]]
- 00842b88 bytes a4ea0594
+ 00874e74 bytes a5950694
- 00842a90 ["INT_ADD", "register:40f0:8", ["const:842a90:8", "const:4:8"]]
- 00842a90 ["CALL", null, ["callee:00c57a90:8"]]
+ 00874d7c ["INT_ADD", "register:40f0:8", ["const:874d7c:8", "const:4:8"]]
+ 00874d7c ["CALL", null, ["callee:00c57a90:8"]]
- 00842a90 bytes 6c610e94
+ 00874d7c bytes 458b0f94
- 00842a94 ["COPY", "register:4040:8", ["const:294000:8"]]
+ 00874d80 ["COPY", "register:4040:8", ["const:2a4000:8"]]
- 00842a94 bytes 88d2ffd0
+ 00874d80 bytes 88d1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fa1b5df94edf9b8abef9d83a12febc9"></a>

### [`00842c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842c68.md) → [`00874f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874f54.md) FUN_00874f54

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "00874f68",
      "incomplete_value": false,
      "site": "00874f6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842c7c",
      "incomplete_value": false,
      "site": "00842c80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "00874f6c",
      "DATA",
      [
        "storage",
        "00c01e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874f6c",
      "DATA",
      [
        "storage",
        "00c7fa40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842c68.md#insn-00842c78) · [`00842c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842c68.md#insn-00842c7c) · [`00842c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842c68.md#insn-00842c90)
- 新版 `00874f64`（命令位置の公開資料なし） · `00874f68`（命令位置の公開資料なし） · `00874f7c`（命令位置の公開資料なし）

~~~diff
- 00842c78 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 00874f64 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00842c78 bytes e81d00f0
+ 00874f64 bytes 482000f0
- 00842c7c ["COPY", "tmp:0:8", ["const:e08:8"]]
- 00842c7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842c7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842c7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874f68 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00874f68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874f68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874f68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842c7c bytes 08213891
+ 00874f68 bytes 08012991
- 00842c90 ["INT_ADD", "register:40f0:8", ["const:842c90:8", "const:4:8"]]
- 00842c90 ["CALL", null, ["callee:00c538e0:8"]]
+ 00874f7c ["INT_ADD", "register:40f0:8", ["const:874f7c:8", "const:4:8"]]
+ 00874f7c ["CALL", null, ["callee:00c538e0:8"]]
- 00842c90 bytes 80500e94
+ 00874f7c bytes 597a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c86e9f894ff2552d2ace325cf19a9510"></a>

### [`00842cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842cc4.md) → [`00874fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874fb0.md) FUN_00874fb0

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00874fc8",
      "incomplete_value": false,
      "site": "00874fcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842cdc",
      "incomplete_value": false,
      "site": "00842ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "00874fcc",
      "DATA",
      [
        "storage",
        "00c01e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874fcc",
      "DATA",
      [
        "storage",
        "00c7fa40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842cc4.md#insn-00842cd8) · [`00842cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842cc4.md#insn-00842cdc) · [`00842cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842cc4.md#insn-00842cf0)
- 新版 `00874fc4`（命令位置の公開資料なし） · `00874fc8`（命令位置の公開資料なし） · `00874fdc`（命令位置の公開資料なし）

~~~diff
- 00842cd8 ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 00874fc4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00842cd8 bytes e81d00f0
+ 00874fc4 bytes 482000f0
- 00842cdc ["COPY", "tmp:0:8", ["const:e08:8"]]
- 00842cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874fc8 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00874fc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874fc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874fc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842cdc bytes 08213891
+ 00874fc8 bytes 08012991
- 00842cf0 ["INT_ADD", "register:40f0:8", ["const:842cf0:8", "const:4:8"]]
- 00842cf0 ["CALL", null, ["callee:00c538e0:8"]]
+ 00874fdc ["INT_ADD", "register:40f0:8", ["const:874fdc:8", "const:4:8"]]
+ 00874fdc ["CALL", null, ["callee:00c538e0:8"]]
- 00842cf0 bytes 68500e94
+ 00874fdc bytes 417a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdce277b32cf1f1b6637d50c6d624216"></a>

### [`00842d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842d20.md) → [`0087500c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087500c.md) FUN_0087500c

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00875030",
      "incomplete_value": false,
      "site": "00875034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842d44",
      "incomplete_value": false,
      "site": "00842d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "00875034",
      "DATA",
      [
        "storage",
        "00c01e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875034",
      "DATA",
      [
        "storage",
        "00c7fa40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842d20.md#insn-00842d34) · [`00842d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842d20.md#insn-00842d40) · [`00842d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842d20.md#insn-00842d44)
- 新版 `00875020`（命令位置の公開資料なし） · `0087502c`（命令位置の公開資料なし） · `00875030`（命令位置の公開資料なし）

~~~diff
- 00842d34 ["INT_ADD", "register:40f0:8", ["const:842d34:8", "const:4:8"]]
- 00842d34 ["CALL", null, ["callee:00c57a90:8"]]
+ 00875020 ["INT_ADD", "register:40f0:8", ["const:875020:8", "const:4:8"]]
+ 00875020 ["CALL", null, ["callee:00c57a90:8"]]
- 00842d34 bytes c3600e94
+ 00875020 bytes 9c8a0f94
- 00842d40 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 0087502c ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00842d40 bytes e91d00f0
+ 0087502c bytes 492000d0
- 00842d44 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 00842d44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842d44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842d44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875030 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00875030 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875030 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875030 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842d44 bytes 29213891
+ 00875030 bytes 29012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fc67a1f028dc2dd5d920e6c79615c48"></a>

### [`00842d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842d78.md) → [`00875064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875064.md) FUN_00875064

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "0087506c",
      "incomplete_value": false,
      "site": "00875070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842d80",
      "incomplete_value": false,
      "site": "00842d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "00875070",
      "DATA",
      [
        "storage",
        "00c01e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875070",
      "DATA",
      [
        "storage",
        "00c7fa40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842d78.md#insn-00842d7c) · [`00842d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842d78.md#insn-00842d80) · [`00842da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842d78.md#insn-00842da8)
- 新版 `00875068`（命令位置の公開資料なし） · `0087506c`（命令位置の公開資料なし） · `00875094`（命令位置の公開資料なし）

~~~diff
- 00842d7c ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 00875068 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00842d7c bytes e91d00f0
+ 00875068 bytes 492000d0
- 00842d80 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 00842d80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842d80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842d80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087506c ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0087506c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087506c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087506c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842d80 bytes 29213891
+ 0087506c bytes 29012991
- 00842da8 ["INT_ADD", "register:40f0:8", ["const:842da8:8", "const:4:8"]]
- 00842da8 ["CALL", null, ["callee:00c538b0:8"]]
+ 00875094 ["INT_ADD", "register:40f0:8", ["const:875094:8", "const:4:8"]]
+ 00875094 ["CALL", null, ["callee:00c538b0:8"]]
- 00842da8 bytes 2e500e94
+ 00875094 bytes 077a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c3d78675c340b25f6fad2011695d271"></a>

### [`00842e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e88.md) → [`00875174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875174.md) FUN_00875174

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00842e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e54.md) · 呼出先 6件 [`00574ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md) [`00841c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md) [`009bd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd618.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00875140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875140.md) · 呼出先 6件 [`00597e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md) [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 68.55% / 新版 68.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008751c8",
      "incomplete_value": true,
      "site": "008751d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842edc",
      "incomplete_value": true,
      "site": "00842ee4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8a0:8"
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
      "definition_site": "008751c4",
      "incomplete_value": true,
      "site": "008751d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:56d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842ed8",
      "incomplete_value": true,
      "site": "00842ee8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d64:8"
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
      "definition_site": "008751c4",
      "incomplete_value": true,
      "site": "008751d4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00842ed8",
      "incomplete_value": true,
      "site": "00842ee8",
      "value": [
        "LOAD",
        "16",
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
      "008751c4",
      "READ",
      [
        "storage",
        "00293d64",
        null,
        "string"
      ]
    ],
    [
      "008751c4",
      "READ",
      [
        "storage",
        "00293d74",
        null,
        "string"
      ]
    ],
    [
      "008751c8",
      "READ",
      [
        "storage",
        "002b18a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008751c4",
      "READ",
      [
        "storage",
        "002a356d",
        null,
        "string"
      ]
    ],
    [
      "008751c4",
      "READ",
      [
        "storage",
        "002a357d",
        null,
        "string"
      ]
    ],
    [
      "008751c8",
      "READ",
      [
        "storage",
        "002c2f30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e88.md#insn-00843048) · [`00842ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e88.md#insn-00842ec8) · [`00842ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00842/00842e88.md#insn-00842ecc)
- 新版 `00875334`（命令位置の公開資料なし） · `008751b4`（命令位置の公開資料なし） · `008751b8`（命令位置の公開資料なし）

~~~diff
- 00843048 ["INT_ADD", "register:40f0:8", ["const:843048:8", "const:4:8"]]
- 00843048 ["CALL", null, ["callee:00a1a508:8"]]
+ 00875334 ["INT_ADD", "register:40f0:8", ["const:875334:8", "const:4:8"]]
+ 00875334 ["CALL", null, ["callee:00a1a508:8"]]
- 00843048 bytes 74e90594
+ 00875334 bytes 75940694
- 00842ec8 ["INT_ADD", "register:40f0:8", ["const:842ec8:8", "const:4:8"]]
- 00842ec8 ["CALL", null, ["callee:00c57a90:8"]]
+ 008751b4 ["INT_ADD", "register:40f0:8", ["const:8751b4:8", "const:4:8"]]
+ 008751b4 ["CALL", null, ["callee:00c57a90:8"]]
- 00842ec8 bytes 5e600e94
+ 008751b4 bytes 378a0f94
- 00842ecc ["COPY", "register:4040:8", ["const:293000:8"]]
+ 008751b8 ["COPY", "register:4040:8", ["const:2a3000:8"]]
- 00842ecc bytes 88d2ffb0
+ 008751b8 bytes 68d1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7845a235f126d40e2ee79343a04be812"></a>

### [`008432a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008432a0.md) → [`0087558c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087558c.md) FUN_0087558c

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 16.67% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008755a0",
      "incomplete_value": true,
      "site": "008755a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008432bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008432a0.md#insn-008432bc) · [`008432b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008432a0.md#insn-008432b0) · [`008432c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008432a0.md#insn-008432c0)
- 新版 `008755a8`（命令位置の公開資料なし） · `0087559c`（命令位置の公開資料なし） · `008755ac`（命令位置の公開資料なし）

~~~diff
- 008432bc ["INT_ADD", "register:40f0:8", ["const:8432bc:8", "const:4:8"]]
- 008432bc ["CALL", null, ["callee:00c538e0:8"]]
+ 008755a8 ["INT_ADD", "register:40f0:8", ["const:8755a8:8", "const:4:8"]]
+ 008755a8 ["CALL", null, ["callee:00c538e0:8"]]
- 008432bc bytes f54e0e94
+ 008755a8 bytes ce780f94
- 008432b0 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 008432b0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0087559c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 0087559c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 008432b0 bytes b30000b4
+ 0087559c bytes b30000b4
- 008432c0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008432c0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 008755ac ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 008755ac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008432c0 bytes 800000b4
+ 008755ac bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9adf77dd3ae2d48b86a01db9d74d37a0"></a>

### [`008432f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008432f0.md) → [`008755dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008755dc.md) FUN_008755dc

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008430b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008430b0.md) · 呼出先 2件 [`0084358c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084358c.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`0087539c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087539c.md) · 呼出先 2件 [`00875878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875878.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.61% / 新版 94.61%

CFGの説明率　旧版 68.75% / 新版 76.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0084345c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00843464"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00843518"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008433cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008432f0.md#insn-008433cc) · [`0084345c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008432f0.md#insn-0084345c) · [`00843464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008432f0.md#insn-00843464)
- 新版 `008756b8`（命令位置の公開資料なし）

~~~diff
- 008433cc ["INT_ADD", "register:40f0:8", ["const:8433cc:8", "const:4:8"]]
- 008433cc ["CALL", null, ["callee:00c57c50:8"]]
+ 008756b8 ["INT_ADD", "register:40f0:8", ["const:8756b8:8", "const:4:8"]]
+ 008756b8 ["CALL", null, ["callee:00c57c50:8"]]
- 008433cc bytes 8d5f0e94
+ 008756b8 bytes 66890f94
- 0084345c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0084345c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0084345c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 0084345c ["COPY", "register:4000:8", ["tmp:0:8"]]
- 0084345c bytes 00018a9a
- 00843464 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00843464 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00843464 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00843464 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00843464 bytes 6232999a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73c6fc11377aee035e54ec3c6e1bc1a1"></a>

### [`0084372c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084372c.md) → [`00875a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875a18.md) FUN_00875a18

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "00875a2c",
      "incomplete_value": false,
      "site": "00875a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843740",
      "incomplete_value": false,
      "site": "00843744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "00875a30",
      "DATA",
      [
        "storage",
        "00c01f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875a30",
      "DATA",
      [
        "storage",
        "00c7fb40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084373c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084372c.md#insn-0084373c) · [`00843740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084372c.md#insn-00843740) · [`00843754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084372c.md#insn-00843754)
- 新版 `00875a28`（命令位置の公開資料なし） · `00875a2c`（命令位置の公開資料なし） · `00875a40`（命令位置の公開資料なし）

~~~diff
- 0084373c ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 00875a28 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0084373c bytes e81d00d0
+ 00875a28 bytes 482000d0
- 00843740 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00843740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00843740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00843740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875a2c ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 00875a2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875a2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875a2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00843740 bytes 08213c91
+ 00875a2c bytes 08012d91
- 00843754 ["INT_ADD", "register:40f0:8", ["const:843754:8", "const:4:8"]]
- 00843754 ["CALL", null, ["callee:00c538e0:8"]]
+ 00875a40 ["INT_ADD", "register:40f0:8", ["const:875a40:8", "const:4:8"]]
+ 00875a40 ["CALL", null, ["callee:00c538e0:8"]]
- 00843754 bytes cf4d0e94
+ 00875a40 bytes a8770f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a41c946c219c80460542165316babe55"></a>

### [`00843788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843788.md) → [`00875a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875a74.md) FUN_00875a74

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00875a8c",
      "incomplete_value": false,
      "site": "00875a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008437a0",
      "incomplete_value": false,
      "site": "008437a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "00875a90",
      "DATA",
      [
        "storage",
        "00c01f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875a90",
      "DATA",
      [
        "storage",
        "00c7fb40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084379c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843788.md#insn-0084379c) · [`008437a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843788.md#insn-008437a0) · [`008437b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843788.md#insn-008437b4)
- 新版 `00875a88`（命令位置の公開資料なし） · `00875a8c`（命令位置の公開資料なし） · `00875aa0`（命令位置の公開資料なし）

~~~diff
- 0084379c ["COPY", "register:4040:8", ["const:c01000:8"]]
+ 00875a88 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 0084379c bytes e81d00d0
+ 00875a88 bytes 482000d0
- 008437a0 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 008437a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008437a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008437a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875a8c ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 00875a8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875a8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875a8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008437a0 bytes 08213c91
+ 00875a8c bytes 08012d91
- 008437b4 ["INT_ADD", "register:40f0:8", ["const:8437b4:8", "const:4:8"]]
- 008437b4 ["CALL", null, ["callee:00c538e0:8"]]
+ 00875aa0 ["INT_ADD", "register:40f0:8", ["const:875aa0:8", "const:4:8"]]
+ 00875aa0 ["CALL", null, ["callee:00c538e0:8"]]
- 008437b4 bytes b74d0e94
+ 00875aa0 bytes 90770f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a3dacd21f1943c9c9111ae723d36a07"></a>

### [`008437e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008437e4.md) → [`00875ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ad0.md) FUN_00875ad0

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00875af4",
      "incomplete_value": false,
      "site": "00875af8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843808",
      "incomplete_value": false,
      "site": "0084380c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "00875af8",
      "DATA",
      [
        "storage",
        "00c01f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875af8",
      "DATA",
      [
        "storage",
        "00c7fb40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008437f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008437e4.md#insn-008437f8) · [`00843804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008437e4.md#insn-00843804) · [`00843808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008437e4.md#insn-00843808)
- 新版 `00875ae4`（命令位置の公開資料なし） · `00875af0`（命令位置の公開資料なし） · `00875af4`（命令位置の公開資料なし）

~~~diff
- 008437f8 ["INT_ADD", "register:40f0:8", ["const:8437f8:8", "const:4:8"]]
- 008437f8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00875ae4 ["INT_ADD", "register:40f0:8", ["const:875ae4:8", "const:4:8"]]
+ 00875ae4 ["CALL", null, ["callee:00c57a90:8"]]
- 008437f8 bytes 125e0e94
+ 00875ae4 bytes eb870f94
- 00843804 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 00875af0 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00843804 bytes e91d00d0
+ 00875af0 bytes 492000d0
- 00843808 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00843808 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00843808 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00843808 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875af4 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 00875af4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875af4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875af4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00843808 bytes 29213c91
+ 00875af4 bytes 29012d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0110fbf1c954ade6ee7682efc3b7b62a"></a>

### [`0084383c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084383c.md) → [`00875b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875b28.md) FUN_00875b28

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "00875b30",
      "incomplete_value": false,
      "site": "00875b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843844",
      "incomplete_value": false,
      "site": "00843848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "00875b34",
      "DATA",
      [
        "storage",
        "00c01f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875b34",
      "DATA",
      [
        "storage",
        "00c7fb40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084383c.md#insn-00843840) · [`00843844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084383c.md#insn-00843844) · [`0084386c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084383c.md#insn-0084386c)
- 新版 `00875b2c`（命令位置の公開資料なし） · `00875b30`（命令位置の公開資料なし） · `00875b58`（命令位置の公開資料なし）

~~~diff
- 00843840 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 00875b2c ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00843840 bytes e91d00d0
+ 00875b2c bytes 492000d0
- 00843844 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00843844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00843844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00843844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875b30 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 00875b30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875b30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875b30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00843844 bytes 29213c91
+ 00875b30 bytes 29012d91
- 0084386c ["INT_ADD", "register:40f0:8", ["const:84386c:8", "const:4:8"]]
- 0084386c ["CALL", null, ["callee:00c538b0:8"]]
+ 00875b58 ["INT_ADD", "register:40f0:8", ["const:875b58:8", "const:4:8"]]
+ 00875b58 ["CALL", null, ["callee:00c538b0:8"]]
- 0084386c bytes 7d4d0e94
+ 00875b58 bytes 56770f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ed735186b2252628a3d31880ca4228e"></a>

### [`00843878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843878.md) → [`00875b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875b64.md) FUN_00875b64

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00841c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0084388c",
      "incomplete_value": true,
      "site": "00843894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00843894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843878.md#insn-00843894) · [`00843888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843878.md#insn-00843888) · [`00843898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843878.md#insn-00843898)
- 新版 `00875b80`（命令位置の公開資料なし） · `00875b74`（命令位置の公開資料なし） · `00875b84`（命令位置の公開資料なし）

~~~diff
- 00843894 ["INT_ADD", "register:40f0:8", ["const:843894:8", "const:4:8"]]
- 00843894 ["CALL", null, ["callee:00c538e0:8"]]
+ 00875b80 ["INT_ADD", "register:40f0:8", ["const:875b80:8", "const:4:8"]]
+ 00875b80 ["CALL", null, ["callee:00c538e0:8"]]
- 00843894 bytes 7f4d0e94
+ 00875b80 bytes 58770f94
- 00843888 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00843888 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00875b74 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00875b74 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00843888 bytes b30000b4
+ 00875b74 bytes b30000b4
- 00843898 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00843898 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00875b84 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00875b84 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00843898 bytes 800000b4
+ 00875b84 bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad74092b7fd5f0591a5fc64e75645e51"></a>

### [`008438c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008438c8.md) → [`00875bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875bb4.md) FUN_00875bb4

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00841c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008438dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00875bc8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "008438e4",
      "incomplete_value": false,
      "site": "008438e8",
      "value": [
        "leaf",
        "const:ffffffffffffffff:8"
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
      "unmatched:008438dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00875bf4"
      ]
    ],
    [
      "unmatched:008438fc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00875bc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00875bf4"
      ]
    ],
    [
      "00875be8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008438dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008438c8.md#insn-008438dc) · [`008438e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008438c8.md#insn-008438e8) · [`008438fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/008438c8.md#insn-008438fc)
- 新版 `00875bd4`（命令位置の公開資料なし）

~~~diff
- 008438dc ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 008438dc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008438dc bytes 740100b4
- 008438e8 ["INT_ADD", "register:40f0:8", ["const:8438e8:8", "const:4:8"]]
- 008438e8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00875bd4 ["INT_ADD", "register:40f0:8", ["const:875bd4:8", "const:4:8"]]
+ 00875bd4 ["CALL", null, ["callee:00c538e0:8"]]
- 008438e8 bytes 6a4d0e94
+ 00875bd4 bytes 43770f94
- 008438fc ["COPY", "register:0:8", ["register:4040:8"]]
- 008438fc ["INT_ADD", "register:40f0:8", ["const:8438fc:8", "const:4:8"]]
- 008438fc ["CALLIND", null, ["register:0:8"]]
- 008438fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67f0daa0f10e3f15c7624bc4d808da87"></a>

### [`0084394c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084394c.md) → [`00875c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875c38.md) FUN_00875c38

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00843918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843918.md) · 呼出先 6件 [`00843c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843c8c.md) [`00843cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843cdc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00875c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875c04.md) · 呼出先 6件 [`00875f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875f78.md) [`00875fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875fc8.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 73.91% / 新版 70.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008439d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008439d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008439dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00875c78",
      "DATA",
      [
        "storage",
        "003c34a0",
        null,
        "byte[39]"
      ]
    ],
    [
      "unmatched:008439d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:008439dc",
      "DATA",
      [
        "storage",
        "00c01f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875c78",
      "DATA",
      [
        "storage",
        "003c7780",
        null,
        "byte[15]"
      ]
    ],
    [
      "00875cc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00875cc8",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008439d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084394c.md#insn-008439d8) · [`008439dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084394c.md#insn-008439dc) · [`008439f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084394c.md#insn-008439f4)

~~~diff
- 008439d8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 008439d8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008439d8 ["COPY", "tmp:2:8", ["tmp:0:8"]]
- 008439d8 ["INT_ADD", "tmp:3:8", ["register:8:8", "const:38:8"]]
- 008439d8 bytes f3ff03a9
- 008439dc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008439dc ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 008439dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008439dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008439dc bytes e85b02a9
- 008439f4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 008439f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008439f4 ["COPY", "tmp:2:8", ["tmp:0:8"]]
- 008439f4 ["INT_ADD", "tmp:3:8", ["register:8:8", "const:38:8"]]
- 008439f4 bytes f3ff03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b29f9318b8efcacf4b01d044fb2653d"></a>

### [`00843b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843b40.md) → [`00875e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875e2c.md) FUN_00875e2c

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.57% / 新版 69.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00843b58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00875e44"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00875e4c",
      "incomplete_value": true,
      "site": "00875e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00843b58",
      "DATA",
      [
        "storage",
        "00c01f78",
        null,
        "undefined *"
      ]
    ],
    [
      "00875e58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00843b7c"
      ]
    ],
    [
      "unmatched:00843b88",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00875e44",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ],
    [
      "00875e58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00875e68"
      ]
    ],
    [
      "00875e74",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843b40.md#insn-00843b58) · [`00843b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843b40.md#insn-00843b68) · [`00843b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843b40.md#insn-00843b78)
- 新版 `00875e54`（命令位置の公開資料なし）

~~~diff
- 00843b58 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00843b58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00843b58 bytes 080000f9
- 00843b68 ["INT_ADD", "register:40f0:8", ["const:843b68:8", "const:4:8"]]
- 00843b68 ["CALL", null, ["callee:00c538e0:8"]]
+ 00875e54 ["INT_ADD", "register:40f0:8", ["const:875e54:8", "const:4:8"]]
+ 00875e54 ["CALL", null, ["callee:00c538e0:8"]]
- 00843b68 bytes ca4c0e94
+ 00875e54 bytes a3760f94
- 00843b78 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00843b78 ["RETURN", null, ["register:0:8"]]
- 00843b78 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

