# v15.7.3 → v15.7.4 · 最優先の変更候補 (54)

[一覧の目次](README.md)

<a id="compare-f89655f6520185a15c91cd2479b97268"></a>

### [`00a1fbb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fbb8.md) → [`00a1fbfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fbfc.md) FUN_00a1fbfc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a1fc20",
      "incomplete_value": false,
      "site": "00a1fc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a1fbdc",
      "incomplete_value": false,
      "site": "00a1fbdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "00a1fc20",
      "DATA",
      [
        "storage",
        "00c0c2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a1fc20",
      "DATA",
      [
        "storage",
        "00c0c300",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a1fbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fbb8.md#insn-00a1fbcc) · [`00a1fbd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fbb8.md#insn-00a1fbd8)
- 新版 `00a1fc10`（命令位置の公開資料なし） · `00a1fc1c`（命令位置の公開資料なし）

~~~diff
- 00a1fbcc ["INT_ADD", "register:40f0:8", ["const:a1fbcc:8", "const:4:8"]]
- 00a1fbcc ["CALL", null, ["callee:00bdb040:8"]]
+ 00a1fc10 ["INT_ADD", "register:40f0:8", ["const:a1fc10:8", "const:4:8"]]
+ 00a1fc10 ["CALL", null, ["callee:00bdb040:8"]]
- 00a1fbcc bytes 09ed0694
+ 00a1fc10 bytes 0ced0694
- 00a1fbd8 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 00a1fbd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a1fbd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a1fbd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a1fc1c ["COPY", "tmp:0:8", ["const:300:8"]]
+ 00a1fc1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a1fc1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a1fc1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a1fbd8 bytes 08c10a91
+ 00a1fc1c bytes 08010c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee69f64cc8003f8cd2faca4a2999b0c6"></a>

### [`00a1fbec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fbec.md) → [`00a1fc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fc30.md) FUN_00a1fc30

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a1fc3c",
      "incomplete_value": false,
      "site": "00a1fc3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a1fbf8",
      "incomplete_value": false,
      "site": "00a1fbf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "00a1fc3c",
      "DATA",
      [
        "storage",
        "00c0c2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a1fc3c",
      "DATA",
      [
        "storage",
        "00c0c300",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a1fbf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fbec.md#insn-00a1fbf4)
- 新版 `00a1fc38`（命令位置の公開資料なし）

~~~diff
- 00a1fbf4 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 00a1fbf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a1fbf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a1fbf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a1fc38 ["COPY", "tmp:0:8", ["const:300:8"]]
+ 00a1fc38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a1fc38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a1fc38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a1fbf4 bytes 29c10a91
+ 00a1fc38 bytes 29010c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c239a511f2b39d6259fc9e274b47387"></a>

### [`00a1fc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fc08.md) → [`00a1fc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fc4c.md) FUN_00a1fc4c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00ade5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade5cc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00ade610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 25.00% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a1fc98",
      "incomplete_value": true,
      "site": "00a1fc9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "live",
            "register:4040:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a1fc54",
      "incomplete_value": true,
      "site": "00a1fc58",
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
            "const:2260:8"
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
    "new": null,
    "old": {
      "definition_site": "00a1fc50",
      "incomplete_value": false,
      "site": "00a1fc58",
      "value": [
        "leaf",
        "const:47:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a1fcd8",
      "incomplete_value": true,
      "site": "00a1fcdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "live",
            "register:4040:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a1fc58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fc08.md#insn-00a1fc58) · [`00a1fc98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fc08.md#insn-00a1fc98) · [`00a1fc9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fc08.md#insn-00a1fc9c)
- 新版 `00a1fc9c`（命令位置の公開資料なし） · `00a1fcdc`（命令位置の公開資料なし） · `00a1fce0`（命令位置の公開資料なし）

~~~diff
- 00a1fc58 ["INT_ADD", "register:40f0:8", ["const:a1fc58:8", "const:4:8"]]
- 00a1fc58 ["CALL", null, ["callee:00ade610:8"]]
+ 00a1fc9c ["INT_ADD", "register:40f0:8", ["const:a1fc9c:8", "const:4:8"]]
+ 00a1fc9c ["CALL", null, ["callee:00ade610:8"]]
- 00a1fc58 bytes 5dfa0294
+ 00a1fc9c bytes 5dfa0294
- 00a1fc98 ["INT_ADD", "register:40f0:8", ["const:a1fc98:8", "const:4:8"]]
- 00a1fc98 ["CALL", null, ["callee:00ade610:8"]]
+ 00a1fcdc ["INT_ADD", "register:40f0:8", ["const:a1fcdc:8", "const:4:8"]]
+ 00a1fcdc ["CALL", null, ["callee:00ade610:8"]]
- 00a1fc98 bytes 4dfa0294
+ 00a1fcdc bytes 4dfa0294
- 00a1fc9c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00a1fc9c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00a1fc9c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00a1fc9c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00a1fce0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00a1fce0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00a1fce0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00a1fce0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00a1fc9c bytes e0000036
+ 00a1fce0 bytes e0000036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9ba8c78aa2434e7002792d132ed6c85"></a>

### [`00a1fcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fcc8.md) → [`00a1fd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fd0c.md) FUN_00a1fd0c

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-031d594525274d6f5686654d8d59df17"></a>

### [`00a1fd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fd28.md) → [`00a1fd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fd6c.md) FUN_00a1fd6c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a1fd78",
      "incomplete_value": false,
      "site": "00a1fd78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a1fd34",
      "incomplete_value": false,
      "site": "00a1fd34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:330:8"
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
      "00a1fd78",
      "DATA",
      [
        "storage",
        "00c0c330",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a1fd78",
      "DATA",
      [
        "storage",
        "00c0c380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a1fd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fd28.md#insn-00a1fd30)
- 新版 `00a1fd74`（命令位置の公開資料なし）

~~~diff
- 00a1fd30 ["COPY", "tmp:0:8", ["const:330:8"]]
- 00a1fd30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a1fd30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a1fd30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a1fd74 ["COPY", "tmp:0:8", ["const:380:8"]]
+ 00a1fd74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a1fd74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a1fd74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a1fd30 bytes 29c10c91
+ 00a1fd74 bytes 29010e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e1d2372f321184cfa3091db2f48e071"></a>

### [`00a1fd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fd44.md) → [`00a1fd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fd88.md) FUN_00a1fd88

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00829bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829bb8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00829bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829bb8.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1fd6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a1fdb0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a1fd9c",
      "incomplete_value": true,
      "site": "00a1fda0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a1fd58",
      "incomplete_value": true,
      "site": "00a1fd5c",
      "value": [
        "live",
        "register:4098:8"
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
      "unmatched:00a1fd6c",
      "DATA",
      [
        "storage",
        "0032ff14",
        "fde_0032ff14",
        "dword"
      ]
    ],
    [
      "unmatched:00a1fd70",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a1fd74",
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
      "00a1fdb0",
      "DATA",
      [
        "storage",
        "0032ff14",
        "fde_0032ff14",
        "dword"
      ]
    ],
    [
      "00a1fdb4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a1fdb8",
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

- 旧版 [`00a1fd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fd44.md#insn-00a1fd5c) · [`00a1fd6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fd44.md#insn-00a1fd6c) · [`00a1fd78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fd44.md#insn-00a1fd78)
- 新版 `00a1fda0`（命令位置の公開資料なし）

~~~diff
- 00a1fd5c ["INT_ADD", "register:40f0:8", ["const:a1fd5c:8", "const:4:8"]]
- 00a1fd5c ["CALL", null, ["callee:00829bb8:8"]]
+ 00a1fda0 ["INT_ADD", "register:40f0:8", ["const:a1fda0:8", "const:4:8"]]
+ 00a1fda0 ["CALL", null, ["callee:00829bb8:8"]]
- 00a1fd5c bytes 9727f897
+ 00a1fda0 bytes 8627f897
- 00a1fd6c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00a1fd6c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a1fd6c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a1fd6c ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00a1fd6c bytes 696a28b8
- 00a1fd78 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a1fd78 ["RETURN", null, ["register:0:8"]]
- 00a1fd78 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-633d3ca1e4956239872d8f57c6b420e3"></a>

### [`00a1fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fd7c.md) → [`00a1fdc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fdc0.md) FUN_00a1fdc0

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-19280397d70f3acd3866484c744771fb"></a>

### [`00a1fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fddc.md) → [`00a1fe20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fe20.md) FUN_00a1fe20

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a1fe2c",
      "incomplete_value": false,
      "site": "00a1fe2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a1fde8",
      "incomplete_value": false,
      "site": "00a1fde8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "00a1fe2c",
      "DATA",
      [
        "storage",
        "00c0c3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a1fe2c",
      "DATA",
      [
        "storage",
        "00c0c400",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a1fde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fddc.md#insn-00a1fde4)
- 新版 `00a1fe28`（命令位置の公開資料なし）

~~~diff
- 00a1fde4 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 00a1fde4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a1fde4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a1fde4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a1fe28 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 00a1fe28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a1fe28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a1fe28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a1fde4 bytes 29c10e91
+ 00a1fe28 bytes 29011091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c39ec3b46ca9c2c606bded09b2f883c1"></a>

### [`00a1fdf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fdf8.md) → [`00a1fe3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fe3c.md) FUN_00a1fe3c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0088482c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/0088482c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0088482c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/0088482c.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.07% / 新版 84.07%

CFGの説明率　旧版 63.89% / 新版 69.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1fdfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1fdfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a1fe00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a1fdfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a1fe00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a1fe04",
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
      "00a1fe40",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a1fe44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a1fe48",
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

- 旧版 [`00a1fdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fdf8.md#insn-00a1fdfc) · [`00a1fe00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fdf8.md#insn-00a1fe00) · [`00a1fe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fdf8.md#insn-00a1fe04)

~~~diff
- 00a1fdfc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a1fdfc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a1fdfc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00a1fdfc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a1fdfc bytes fd7b07a9
- 00a1fe00 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:80:8"]]
- 00a1fe00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00a1fe00 bytes f54300f9
- 00a1fe04 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a1fe04 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a1fe04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00a1fe04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a1fe04 bytes f44f09a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-444cb683d82ce8bdb0c01568eb76a725"></a>

### [`00a20078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20078.md) → [`00a200bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a200bc.md) FUN_00a200bc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a200d0",
      "incomplete_value": false,
      "site": "00a200d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2008c",
      "incomplete_value": false,
      "site": "00a20090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      "00a200d4",
      "DATA",
      [
        "storage",
        "00c0c420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a200d4",
      "DATA",
      [
        "storage",
        "00c0c470",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a20084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20078.md#insn-00a20084) · [`00a2008c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20078.md#insn-00a2008c)
- 新版 `00a200c8`（命令位置の公開資料なし） · `00a200d0`（命令位置の公開資料なし）

~~~diff
- 00a20084 ["INT_ADD", "register:40f0:8", ["const:a20084:8", "const:4:8"]]
- 00a20084 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a200c8 ["INT_ADD", "register:40f0:8", ["const:a200c8:8", "const:4:8"]]
+ 00a200c8 ["CALL", null, ["callee:00bdb040:8"]]
- 00a20084 bytes dbeb0694
+ 00a200c8 bytes deeb0694
- 00a2008c ["COPY", "tmp:0:8", ["const:420:8"]]
- 00a2008c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a2008c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a2008c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a200d0 ["COPY", "tmp:0:8", ["const:470:8"]]
+ 00a200d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a200d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a200d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a2008c bytes 08811091
+ 00a200d0 bytes 08c11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ece260abb2bd6f52100edefc37c3aafc"></a>

### [`00a2009c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a2009c.md) → [`00a200e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a200e0.md) FUN_00a200e0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a200e4",
      "incomplete_value": false,
      "site": "00a200e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a200a0",
      "incomplete_value": false,
      "site": "00a200a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      "00a200e8",
      "DATA",
      [
        "storage",
        "00c0c420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a200e8",
      "DATA",
      [
        "storage",
        "00c0c470",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a200a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a2009c.md#insn-00a200a0)
- 新版 `00a200e4`（命令位置の公開資料なし）

~~~diff
- 00a200a0 ["COPY", "tmp:0:8", ["const:420:8"]]
- 00a200a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a200a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a200a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a200e4 ["COPY", "tmp:0:8", ["const:470:8"]]
+ 00a200e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a200e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a200e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a200a0 bytes 08811091
+ 00a200e4 bytes 08c11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36466fba87ed0bdddb5c4d7009ada9f2"></a>

### [`00a200cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a200cc.md) → [`00a20110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20110.md) FUN_00a20110

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-65e29b59fae6d1240687eb8f16f82431"></a>

### [`00a200f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a200f8.md) → [`00a2013c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a2013c.md) FUN_00a2013c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 46.15% / 新版 46.15%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a200f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a200f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a200fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a200f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a200fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2011c",
      "DATA",
      [
        "storage",
        "00c0c4b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a2013c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a20140",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a20160",
      "DATA",
      [
        "storage",
        "00c0c500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a200f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a200f8.md#insn-00a200f8) · [`00a200fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a200f8.md#insn-00a200fc) · [`00a2010c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a200f8.md#insn-00a2010c)
- 新版 `00a20150`（命令位置の公開資料なし）

~~~diff
- 00a200f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a200f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a200f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a200f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a200f8 bytes fd7bbea9
- 00a200fc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a200fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a200fc bytes f30b00f9
- 00a2010c ["INT_ADD", "register:40f0:8", ["const:a2010c:8", "const:4:8"]]
- 00a2010c ["CALL", null, ["callee:00bdb040:8"]]
+ 00a20150 ["INT_ADD", "register:40f0:8", ["const:a20150:8", "const:4:8"]]
+ 00a20150 ["CALL", null, ["callee:00bdb040:8"]]
- 00a2010c bytes b9eb0694
+ 00a20150 bytes bceb0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f44d39c204612810bafbc34289024c4"></a>

### [`00a2012c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a2012c.md) → [`00a20170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20170.md) FUN_00a20170

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a2017c",
      "incomplete_value": false,
      "site": "00a2017c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a20138",
      "incomplete_value": false,
      "site": "00a20138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "00a2017c",
      "DATA",
      [
        "storage",
        "00c0c4b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a2017c",
      "DATA",
      [
        "storage",
        "00c0c500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a20134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a2012c.md#insn-00a20134)
- 新版 `00a20178`（命令位置の公開資料なし）

~~~diff
- 00a20134 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 00a20134 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a20134 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a20134 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a20178 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 00a20178 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a20178 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a20178 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a20134 bytes 29c11291
+ 00a20178 bytes 29011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bb28250515da2875d331b4fb01e9ed9"></a>

### [`00a20148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20148.md) → [`00a2018c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a2018c.md) FUN_00a2018c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0088482c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/0088482c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0088482c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/0088482c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.53% / 新版 80.53%

CFGの説明率　旧版 30.23% / 新版 30.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2014c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2014c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a20150"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a2014c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a20150",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a20154",
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
      "00a20190",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a20194",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a20198",
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

- 旧版 [`00a2014c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20148.md#insn-00a2014c) · [`00a20150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20148.md#insn-00a20150) · [`00a20154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20148.md#insn-00a20154)

~~~diff
- 00a2014c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a2014c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a2014c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00a2014c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a2014c bytes fd7b07a9
- 00a20150 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:80:8"]]
- 00a20150 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00a20150 bytes f54300f9
- 00a20154 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a20154 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a20154 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00a20154 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a20154 bytes f44f09a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9ce77f10cf66af6e3e30c8dbe60718e"></a>

### [`00a2039c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a2039c.md) → [`00a203e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a203e0.md) FUN_00a203e0

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-a682a980f6b51e5918eb47f4506ffffb"></a>

### [`00a203ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a203ec.md) → [`00a20430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20430.md) FUN_00a20430

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a20434",
      "incomplete_value": false,
      "site": "00a20438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a203f0",
      "incomplete_value": false,
      "site": "00a203f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:520:8"
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
      "00a20438",
      "DATA",
      [
        "storage",
        "00c0c520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a20438",
      "DATA",
      [
        "storage",
        "00c0c570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a203f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a203ec.md#insn-00a203f0)
- 新版 `00a20434`（命令位置の公開資料なし）

~~~diff
- 00a203f0 ["COPY", "tmp:0:8", ["const:520:8"]]
- 00a203f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a203f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a203f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a20434 ["COPY", "tmp:0:8", ["const:570:8"]]
+ 00a20434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a20434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a20434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a203f0 bytes 08811491
+ 00a20434 bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83f9858bd9bb0c9b2804ce35356fdcc6"></a>

### [`00a2041c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a2041c.md) → [`00a20460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20460.md) FUN_00a20460

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-c81be58154e3509d333264a2540f5fcc"></a>

### [`00a20498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20498.md) → [`00a204dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a204dc.md) FUN_00a204dc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883cc0.md) [`009e97a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e97a0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md) [`009e97e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e97e4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 10.00% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a20514"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a20558"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a204bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a204bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a20528"
      ]
    ],
    [
      "unmatched:00a20514",
      "DATA",
      [
        "storage",
        "0033a268",
        null,
        "byte[63]"
      ]
    ]
  ],
  "added": [
    [
      "00a20500",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a20528"
      ]
    ],
    [
      "00a20558",
      "DATA",
      [
        "storage",
        "0033a268",
        null,
        "byte[63]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a204bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20498.md#insn-00a204bc) · [`00a204fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20498.md#insn-00a204fc) · [`00a20500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20498.md#insn-00a20500)
- 新版 `00a20540`（命令位置の公開資料なし） · `00a20544`（命令位置の公開資料なし）

~~~diff
- 00a204bc ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00a204bc bytes 40010054
- 00a204fc ["INT_ADD", "register:40f0:8", ["const:a204fc:8", "const:4:8"]]
- 00a204fc ["CALL", null, ["callee:00459efc:8"]]
+ 00a20540 ["INT_ADD", "register:40f0:8", ["const:a20540:8", "const:4:8"]]
+ 00a20540 ["CALL", null, ["callee:00459efc:8"]]
- 00a204fc bytes 80e6e897
+ 00a20540 bytes 6fe6e897
- 00a20500 ["INT_ADD", "register:40f0:8", ["const:a20500:8", "const:4:8"]]
- 00a20500 ["CALL", null, ["callee:0081f580:8"]]
+ 00a20544 ["INT_ADD", "register:40f0:8", ["const:a20544:8", "const:4:8"]]
+ 00a20544 ["CALL", null, ["callee:0081f580:8"]]
- 00a20500 bytes 20fcf797
+ 00a20544 bytes 0ffcf797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-481ddf1ae9447d5c8cf57df5132deb4c"></a>

### [`00a20564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20564.md) → [`00a205a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a205a8.md) FUN_00a205a8

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-fdcc486c021dab733065151d8f00ccc9"></a>

### [`00a205c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a205c4.md) → [`00a20608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20608.md) FUN_00a20608

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a20614",
      "incomplete_value": false,
      "site": "00a20614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a205d0",
      "incomplete_value": false,
      "site": "00a205d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "00a20614",
      "DATA",
      [
        "storage",
        "00c0c630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a20614",
      "DATA",
      [
        "storage",
        "00c0c680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a205cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a205c4.md#insn-00a205cc)
- 新版 `00a20610`（命令位置の公開資料なし）

~~~diff
- 00a205cc ["COPY", "tmp:0:8", ["const:630:8"]]
- 00a205cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a205cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a205cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a20610 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 00a20610 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a20610 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a20610 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a205cc bytes 29c11891
+ 00a20610 bytes 29011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78fdc29c9f7df176c3ac28c847b22069"></a>

### [`00a205e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a205e0.md) → [`00a20624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20624.md) FUN_00a20624

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00664ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00664/00664ab8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a6aa88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6aa88.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00664ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/00664ab8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a6aacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6aacc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a206c8",
      "incomplete_value": true,
      "site": "00a206dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a20684",
      "incomplete_value": true,
      "site": "00a20698",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a206c4",
      "incomplete_value": false,
      "site": "00a206dc",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a20680",
      "incomplete_value": false,
      "site": "00a20698",
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
            "const:e48:8"
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
      "definition_site": "00a206d0",
      "incomplete_value": false,
      "site": "00a206dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2068c",
      "incomplete_value": false,
      "site": "00a20698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      "00a206c4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a206c8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a206d0",
      "PARAM",
      [
        "storage",
        "00bf7a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a206c4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a206c8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a206d0",
      "PARAM",
      [
        "storage",
        "00bf7ab0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a20698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a205e0.md#insn-00a20698) · [`00a20620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a205e0.md#insn-00a20620) · [`00a20658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a205e0.md#insn-00a20658)
- 新版 `00a206dc`（命令位置の公開資料なし） · `00a20664`（命令位置の公開資料なし） · `00a2069c`（命令位置の公開資料なし）

~~~diff
- 00a20698 ["INT_ADD", "register:40f0:8", ["const:a20698:8", "const:4:8"]]
- 00a20698 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00a206dc ["INT_ADD", "register:40f0:8", ["const:a206dc:8", "const:4:8"]]
+ 00a206dc ["CALL", null, ["callee:00bdb7c0:8"]]
- 00a20698 bytes 36ec0694
+ 00a206dc bytes 39ec0694
- 00a20620 ["INT_ADD", "register:40f0:8", ["const:a20620:8", "const:4:8"]]
- 00a20620 ["CALL", null, ["ram:457e1c:8"]]
+ 00a20664 ["INT_ADD", "register:40f0:8", ["const:a20664:8", "const:4:8"]]
+ 00a20664 ["CALL", null, ["ram:457e1c:8"]]
- 00a20620 bytes ffdde897
+ 00a20664 bytes eedde897
- 00a20658 ["INT_ADD", "register:40f0:8", ["const:a20658:8", "const:4:8"]]
- 00a20658 ["CALL", null, ["ram:457e1c:8"]]
+ 00a2069c ["INT_ADD", "register:40f0:8", ["const:a2069c:8", "const:4:8"]]
+ 00a2069c ["CALL", null, ["ram:457e1c:8"]]
- 00a20658 bytes f1dde897
+ 00a2069c bytes e0dde897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b383c6bdf818b774967c720a85ed0a3"></a>

### [`00a20958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20958.md) → [`00a2099c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a2099c.md) FUN_00a2099c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a209b0",
      "incomplete_value": false,
      "site": "00a209b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2096c",
      "incomplete_value": false,
      "site": "00a20970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "00a209b4",
      "DATA",
      [
        "storage",
        "00c0c6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a209b4",
      "DATA",
      [
        "storage",
        "00c0c700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a20964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20958.md#insn-00a20964) · [`00a2096c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20958.md#insn-00a2096c)
- 新版 `00a209a8`（命令位置の公開資料なし） · `00a209b0`（命令位置の公開資料なし）

~~~diff
- 00a20964 ["INT_ADD", "register:40f0:8", ["const:a20964:8", "const:4:8"]]
- 00a20964 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a209a8 ["INT_ADD", "register:40f0:8", ["const:a209a8:8", "const:4:8"]]
+ 00a209a8 ["CALL", null, ["callee:00bdb040:8"]]
- 00a20964 bytes a3e90694
+ 00a209a8 bytes a6e90694
- 00a2096c ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 00a2096c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a2096c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a2096c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a209b0 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 00a209b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a209b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a209b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a2096c bytes 08c11a91
+ 00a209b0 bytes 08011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bd598ebfebacecc68a6e9d0873d8068"></a>

### [`00a2097c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a2097c.md) → [`00a209c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a209c0.md) FUN_00a209c0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a209c4",
      "incomplete_value": false,
      "site": "00a209c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a20980",
      "incomplete_value": false,
      "site": "00a20984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "00a209c8",
      "DATA",
      [
        "storage",
        "00c0c6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a209c8",
      "DATA",
      [
        "storage",
        "00c0c700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a20980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a2097c.md#insn-00a20980)
- 新版 `00a209c4`（命令位置の公開資料なし）

~~~diff
- 00a20980 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 00a20980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a20980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a20980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a209c4 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 00a209c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a209c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a209c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a20980 bytes 08c11a91
+ 00a209c4 bytes 08011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06d265eec7a2fcb8bcfd190894b09a77"></a>

### [`00a209d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a209d8.md) → [`00a20a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20a1c.md) FUN_00a20a1c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a20a30",
      "incomplete_value": false,
      "site": "00a20a34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a209ec",
      "incomplete_value": false,
      "site": "00a209f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "00a20a34",
      "DATA",
      [
        "storage",
        "00c0c730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a20a34",
      "DATA",
      [
        "storage",
        "00c0c780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a209e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a209d8.md#insn-00a209e4) · [`00a209ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a209d8.md#insn-00a209ec)
- 新版 `00a20a28`（命令位置の公開資料なし） · `00a20a30`（命令位置の公開資料なし）

~~~diff
- 00a209e4 ["INT_ADD", "register:40f0:8", ["const:a209e4:8", "const:4:8"]]
- 00a209e4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a20a28 ["INT_ADD", "register:40f0:8", ["const:a20a28:8", "const:4:8"]]
+ 00a20a28 ["CALL", null, ["callee:00bdb040:8"]]
- 00a209e4 bytes 83e90694
+ 00a20a28 bytes 86e90694
- 00a209ec ["COPY", "tmp:0:8", ["const:730:8"]]
- 00a209ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a209ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a209ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a20a30 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 00a20a30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a20a30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a20a30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a209ec bytes 08c11c91
+ 00a20a30 bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73dbfd9e0556429c50dfab6b84479a7f"></a>

### [`00a209fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a209fc.md) → [`00a20a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20a40.md) FUN_00a20a40

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a20a44",
      "incomplete_value": false,
      "site": "00a20a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a20a00",
      "incomplete_value": false,
      "site": "00a20a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "00a20a48",
      "DATA",
      [
        "storage",
        "00c0c730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a20a48",
      "DATA",
      [
        "storage",
        "00c0c780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a20a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a209fc.md#insn-00a20a00)
- 新版 `00a20a44`（命令位置の公開資料なし）

~~~diff
- 00a20a00 ["COPY", "tmp:0:8", ["const:730:8"]]
- 00a20a00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a20a00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a20a00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a20a44 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 00a20a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a20a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a20a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a20a00 bytes 08c11c91
+ 00a20a44 bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-026867a5c96626dee2685aff53222566"></a>

### [`00a20d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20d94.md) → [`00a20dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20dd8.md) FUN_00a20dd8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a20a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20a54.md) · 呼出先 2件 [`007dcb28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dcb28.md) [`00a20a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20a54.md)
- 新版 呼出元 1件 [`00a20a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20a98.md) · 呼出先 2件 [`007dcb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dcb28.md) [`00a20a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20a98.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.79% / 新版 94.79%

CFGの説明率　旧版 48.65% / 新版 51.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a20e24"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a20f78"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a20ff0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a20e24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a20f20"
      ]
    ],
    [
      "unmatched:00a20f78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a20f6c"
      ]
    ],
    [
      "unmatched:00a20ff0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a20e48"
      ]
    ]
  ],
  "added": [
    [
      "00a20e68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a20f20"
      ]
    ],
    [
      "00a20fbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a20f6c"
      ]
    ],
    [
      "00a21034",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a20e48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a20e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20d94.md#insn-00a20e24) · [`00a20e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20d94.md#insn-00a20e6c)
- 新版 `00a20e68`（命令位置の公開資料なし） · `00a20eb0`（命令位置の公開資料なし）

~~~diff
- 00a20e24 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a20e24 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00a20e24 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00a20e24 ["CBRANCH", null, ["local:b24:8", "tmp:2:1"]]
- 00a20e24 bytes cc050054
+ 00a20e68 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a20e68 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00a20e68 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00a20e68 ["CBRANCH", null, ["local:b23:8", "tmp:2:1"]]
+ 00a20e68 bytes cc050054
- 00a20e6c ["INT_ADD", "register:40f0:8", ["const:a20e6c:8", "const:4:8"]]
- 00a20e6c ["CALL", null, ["callee:007dcb28:8"]]
+ 00a20eb0 ["INT_ADD", "register:40f0:8", ["const:a20eb0:8", "const:4:8"]]
+ 00a20eb0 ["CALL", null, ["callee:007dcb28:8"]]
- 00a20e6c bytes 2feff697
+ 00a20eb0 bytes 1eeff697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7bcc19b83133870a46bd35febe67892"></a>

### [`00a21094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21094.md) → [`00a210d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a210d8.md) FUN_00a210d8

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a20a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a20a54.md) [`00a21094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21094.md) · 呼出先 3件 [`007dcb28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007dc/007dcb28.md) [`00a21094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21094.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 2件 [`00a20a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20a98.md) [`00a210d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a210d8.md) · 呼出先 3件 [`007dcb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007dc/007dcb28.md) [`00a210d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a210d8.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 99.01% / 新版 99.01%

CFGの説明率　旧版 89.39% / 新版 88.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a214a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a214a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a214ec"
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
      "unmatched:00a214b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a214e0"
      ]
    ],
    [
      "unmatched:00a215c0",
      "READ",
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
      "00a214f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a214e0"
      ]
    ],
    [
      "00a21604",
      "READ",
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

- 旧版 [`00a21424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21094.md#insn-00a21424) · [`00a214a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21094.md#insn-00a214a8) · [`00a214b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21094.md#insn-00a214b0)
- 新版 `00a21468`（命令位置の公開資料なし）

~~~diff
- 00a21424 ["INT_ADD", "register:40f0:8", ["const:a21424:8", "const:4:8"]]
- 00a21424 ["CALL", null, ["local:b0:8"]]
+ 00a21468 ["INT_ADD", "register:40f0:8", ["const:a21468:8", "const:4:8"]]
+ 00a21468 ["CALL", null, ["local:b0:8"]]
- 00a21424 bytes 1cffff97
+ 00a21468 bytes 1cffff97
- 00a214a8 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:fffffffffffffff0:8"]]
- 00a214a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a214a8 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00a214a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00a214a8 bytes 80853fad
- 00a214b0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a214b0 ["CBRANCH", null, ["local:b52:8", "tmp:0:1"]]
- 00a214b0 bytes 61ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db89fa3aade7240ae2b9815690b45bce"></a>

### [`00a216ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a216ec.md) → [`00a21730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21730.md) FUN_00a21730

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a216ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a216ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a216f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a216ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a216f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a21710",
      "DATA",
      [
        "storage",
        "00c0c7b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a21730",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a21734",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a21754",
      "DATA",
      [
        "storage",
        "00c0c800",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a216ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a216ec.md#insn-00a216ec) · [`00a216f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a216ec.md#insn-00a216f0) · [`00a21700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a216ec.md#insn-00a21700)
- 新版 `00a21744`（命令位置の公開資料なし）

~~~diff
- 00a216ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a216ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a216ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a216ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a216ec bytes fd7bbea9
- 00a216f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a216f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a216f0 bytes f30b00f9
- 00a21700 ["INT_ADD", "register:40f0:8", ["const:a21700:8", "const:4:8"]]
- 00a21700 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a21744 ["INT_ADD", "register:40f0:8", ["const:a21744:8", "const:4:8"]]
+ 00a21744 ["CALL", null, ["callee:00bdb040:8"]]
- 00a21700 bytes 3ce60694
+ 00a21744 bytes 3fe60694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f39b6b5be6ee9c618ea77cd99d43bfee"></a>

### [`00a21740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21740.md) → [`00a21784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21784.md) FUN_00a21784

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-3978507894aecf6979668587ee720fae"></a>

### [`00a21768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21768.md) → [`00a217ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a217ac.md) FUN_00a217ac

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00a144c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a14/00a144c8.md) [`00a21768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21768.md) [`00a21bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21bc4.md) · 呼出先 5件 [`00a21768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21768.md) [`00a21ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21ae4.md) [`00a21bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21bc4.md) [`00a21eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21eb4.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`00a1450c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a14/00a1450c.md) [`00a217ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a217ac.md) [`00a21c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21c08.md) · 呼出先 5件 [`00a217ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a217ac.md) [`00a21b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21b28.md) [`00a21c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21c08.md) [`00a21ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21ef8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.30% / 新版 84.30%

CFGの説明率　旧版 39.74% / 新版 39.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 6件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a21780"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a21780"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a21794"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a21780",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a21794",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a21798",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a21810"
      ]
    ]
  ],
  "added": [
    [
      "00a217c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a217d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a217dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a21810"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a21780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21768.md#insn-00a21780) · [`00a21794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21768.md#insn-00a21794) · [`00a21798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21768.md#insn-00a21798)

~~~diff
- 00a21780 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a21780 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a21780 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00a21780 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a21780 bytes f44f06a9
- 00a21794 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00a21794 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a21794 bytes e80700f9
- 00a21798 ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
- 00a21798 bytes a2010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9eccc3409cdc8a31bfea3f851cbc89d8"></a>

### [`00a21ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21ae4.md) → [`00a21b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21b28.md) FUN_00a21b28

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00a21768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21768.md) [`00a21bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21bc4.md) [`00a21eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21eb4.md) · 呼出先 1件 [`006612f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006612f8.md)
- 新版 呼出元 3件 [`00a217ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a217ac.md) [`00a21c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21c08.md) [`00a21ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21ef8.md) · 呼出先 1件 [`006612f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006612f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 7.69% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a21b50",
      "incomplete_value": true,
      "site": "00a21b54",
      "value": [
        "INT_ADD",
        "8",
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
                "live",
                "register:4000:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:1560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a21b0c",
      "incomplete_value": true,
      "site": "00a21b10",
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
            "const:1560:8"
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
    "new": null,
    "old": {
      "definition_site": "00a21b24",
      "incomplete_value": true,
      "site": "00a21b30",
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
              [
                "live",
                "register:40a0:8"
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
    "new": null,
    "old": {
      "definition_site": "00a21b6c",
      "incomplete_value": true,
      "site": "00a21b70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "live",
            "register:40b0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a21b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21ae4.md#insn-00a21b10) · [`00a21b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21ae4.md#insn-00a21b30) · [`00a21b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21ae4.md#insn-00a21b70)
- 新版 `00a21b54`（命令位置の公開資料なし） · `00a21b74`（命令位置の公開資料なし） · `00a21bb4`（命令位置の公開資料なし）

~~~diff
- 00a21b10 ["INT_ADD", "register:40f0:8", ["const:a21b10:8", "const:4:8"]]
- 00a21b10 ["CALL", null, ["callee:006612f8:8"]]
+ 00a21b54 ["INT_ADD", "register:40f0:8", ["const:a21b54:8", "const:4:8"]]
+ 00a21b54 ["CALL", null, ["callee:006612f8:8"]]
- 00a21b10 bytes fafdf097
+ 00a21b54 bytes e9fdf097
- 00a21b30 ["INT_ADD", "register:40f0:8", ["const:a21b30:8", "const:4:8"]]
- 00a21b30 ["CALL", null, ["callee:006612f8:8"]]
+ 00a21b74 ["INT_ADD", "register:40f0:8", ["const:a21b74:8", "const:4:8"]]
+ 00a21b74 ["CALL", null, ["callee:006612f8:8"]]
- 00a21b30 bytes f2fdf097
+ 00a21b74 bytes e1fdf097
- 00a21b70 ["INT_ADD", "register:40f0:8", ["const:a21b70:8", "const:4:8"]]
- 00a21b70 ["CALL", null, ["callee:006612f8:8"]]
+ 00a21bb4 ["INT_ADD", "register:40f0:8", ["const:a21bb4:8", "const:4:8"]]
+ 00a21bb4 ["CALL", null, ["callee:006612f8:8"]]
- 00a21b70 bytes e2fdf097
+ 00a21bb4 bytes d1fdf097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7fc12fd0fc7b8ab46fc7da866248c0b"></a>

### [`00a21eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21eb4.md) → [`00a21ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21ef8.md) FUN_00a21ef8

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a21768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21768.md) [`00a21eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21eb4.md) · 呼出先 4件 [`00a21ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21ae4.md) [`00a21eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21eb4.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 2件 [`00a217ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a217ac.md) [`00a21ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21ef8.md) · 呼出先 4件 [`00a21b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21b28.md) [`00a21ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a21/00a21ef8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.57% / 新版 95.57%

CFGの説明率　旧版 78.42% / 新版 78.99%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 2件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a221c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a2220c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a220e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a220e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a22034"
      ]
    ],
    [
      "unmatched:00a22154",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a221c4"
      ]
    ],
    [
      "unmatched:00a2219c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a221d0"
      ]
    ]
  ],
  "added": [
    [
      "00a2212c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a22034"
      ]
    ],
    [
      "00a22198",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a221c4"
      ]
    ],
    [
      "00a221e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a221d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a220e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21eb4.md#insn-00a220e8) · [`00a2211c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a21/00a21eb4.md#insn-00a2211c)
- 新版 `00a22160`（命令位置の公開資料なし） · `00a2212c`（命令位置の公開資料なし）

~~~diff
- 00a220e8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a220e8 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00a220e8 bytes 41f8ff54
- 00a2211c ["INT_ADD", "register:40f0:8", ["const:a2211c:8", "const:4:8"]]
- 00a2211c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00a22160 ["INT_ADD", "register:40f0:8", ["const:a22160:8", "const:4:8"]]
+ 00a22160 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00a2211c bytes e1e30694
+ 00a22160 bytes e4e30694
+ 00a2212c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a2212c ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00a2212c bytes 41f8ff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32855b5b6fa7deee9ab86c9840c413b8"></a>

### [`00a22af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a22/00a22af0.md) → [`00a22b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a22/00a22b34.md) FUN_00a22b34

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a22568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a22/00a22568.md) [`00a22af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a22/00a22af0.md) · 呼出先 2件 [`00a22af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a22/00a22af0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 2件 [`00a225ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a22/00a225ac.md) [`00a22b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a22/00a22b34.md) · 呼出先 2件 [`00a22b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a22/00a22b34.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.87% / 新版 81.87%

CFGの説明率　旧版 48.94% / 新版 49.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 19件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a22af4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a22af4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a22af8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a22af4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a22af8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a22afc",
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
      "00a22b38",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a22b3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a22b40",
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

- 旧版 [`00a22af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a22/00a22af0.md#insn-00a22af4) · [`00a22af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a22/00a22af0.md#insn-00a22af8) · [`00a22afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a22/00a22af0.md#insn-00a22afc)

~~~diff
- 00a22af4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a22af4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a22af4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a22af4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a22af4 bytes fd7b02a9
- 00a22af8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a22af8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a22af8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00a22af8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a22af8 bytes fc6f03a9
- 00a22afc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a22afc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a22afc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a22afc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a22afc bytes fa6704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-417ebff8b241fb93378d669a4a8ce562"></a>

### [`00a23124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a23124.md) → [`00a23168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a23/00a23168.md) FUN_00a23168

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-4b5a5158e4fb53059370e0b729f9c701"></a>

### [`00a2314c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a2314c.md) → [`00a23190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a23/00a23190.md) _INIT_218

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.23% / 新版 80.23%

CFGの説明率　旧版 37.78% / 新版 38.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2317c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a231a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a231c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a2317c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a23188",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a231a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a231c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a231cc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00a231e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2317c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a2314c.md#insn-00a2317c) · [`00a231a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a2314c.md#insn-00a231a4)
- 新版 `00a231c0`（命令位置の公開資料なし）

~~~diff
- 00a2317c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a2317c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a2317c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a2317c bytes a9831ff8
- 00a231a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00a231a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a231a4 bytes e013813c
+ 00a231c0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a231c0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 00a231c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00a231c0 bytes a9831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2db8e4ad3036ae7d6c92a83d142e98f2"></a>

### [`00a234dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a234dc.md) → [`00a23520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a23/00a23520.md) _INIT_219

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00a2355c",
      "incomplete_value": true,
      "site": "00a23578",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a23518",
      "incomplete_value": true,
      "site": "00a23534",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a23580",
      "incomplete_value": true,
      "site": "00a2359c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a2353c",
      "incomplete_value": true,
      "site": "00a23558",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a235a0",
      "incomplete_value": true,
      "site": "00a235bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a2355c",
      "incomplete_value": true,
      "site": "00a23578",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a2355c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a23580",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a235a0",
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
      "00a2355c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00a23580",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00a235a0",
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

- 旧版 [`00a23514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a234dc.md#insn-00a23514) · [`00a2363c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a234dc.md#insn-00a2363c) · [`00a23710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a234dc.md#insn-00a23710)
- 新版 `00a23558`（命令位置の公開資料なし） · `00a23680`（命令位置の公開資料なし） · `00a23754`（命令位置の公開資料なし）

~~~diff
- 00a23514 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00a23514 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a23514 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a23514 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a23558 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00a23558 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a23558 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a23558 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a23514 bytes 29750b91
+ 00a23558 bytes 29dd0d91
- 00a2363c ["INT_ADD", "register:40f0:8", ["const:a2363c:8", "const:4:8"]]
- 00a2363c ["CALL", null, ["callee:00418cb8:8"]]
+ 00a23680 ["INT_ADD", "register:40f0:8", ["const:a23680:8", "const:4:8"]]
+ 00a23680 ["CALL", null, ["callee:00418cb8:8"]]
- 00a2363c bytes 9fd5e797
+ 00a23680 bytes 8ed5e797
- 00a23710 ["INT_ADD", "register:40f0:8", ["const:a23710:8", "const:4:8"]]
- 00a23710 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00a23754 ["INT_ADD", "register:40f0:8", ["const:a23754:8", "const:4:8"]]
+ 00a23754 ["CALL", null, ["callee:00bdafe0:8"]]
- 00a23710 bytes 20de0694
+ 00a23754 bytes 23de0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02c19020b0e5a096b01404a5b6464ce2"></a>

### [`00a2386c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a2386c.md) → [`00a238b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a23/00a238b0.md) FUN_00a238b0

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a25380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25380.md) · 呼出先 18件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md)
- 新版 呼出元 1件 [`00a253c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a253c4.md) · 呼出先 18件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.06% / 新版 87.06%

CFGの説明率　旧版 49.41% / 新版 48.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 22件, `unresolved_store_alignment` 24件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a23870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a23870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a23874"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a23870",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a23874",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a23878",
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
      "00a238b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a238b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a238bc",
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

- 旧版 [`00a23870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a2386c.md#insn-00a23870) · [`00a23874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a2386c.md#insn-00a23874) · [`00a23878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a2386c.md#insn-00a23878)

~~~diff
- 00a23870 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a23870 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a23870 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00a23870 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a23870 bytes fd7b13a9
- 00a23874 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a23874 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a23874 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00a23874 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a23874 bytes fc6f14a9
- 00a23878 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a23878 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a23878 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00a23878 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a23878 bytes fa6715a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2df70f9c197838b4f9a363ec809aad99"></a>

### [`00a243c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a243c0.md) → [`00a24404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a24/00a24404.md) FUN_00a24404

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2386c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a23/00a2386c.md) · 呼出先 10件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00467c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c68.md) [`008887f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00888/008887f0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00a238b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a23/00a238b0.md) · 呼出先 10件 [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00467c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c68.md) [`008887f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/008887f0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.99% / 新版 60.99%

CFGの説明率　旧版 15.62% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 7件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a24404"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a24410"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a24414"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a24404",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a24410",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a24414",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a24448",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a24454",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00a24458",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a24404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a243c0.md#insn-00a24404) · [`00a24410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a243c0.md#insn-00a24410) · [`00a24414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a243c0.md#insn-00a24414)

~~~diff
- 00a24404 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a24404 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a24404 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a24404 bytes a8831ff8
- 00a24410 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00a24410 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a24410 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00a24410 bytes ff1300f9
- 00a24414 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00a24414 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a24414 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00a24414 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00a24414 bytes e00300ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36ea8c4a80f12f3c4aea62e5e6f56c65"></a>

### [`00a24618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a24618.md) → [`00a2465c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a24/00a2465c.md) FUN_00a2465c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a254bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a254bc.md) · 呼出先 5件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00447a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md) [`00467c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c68.md) [`00467c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c70.md)
- 新版 呼出元 1件 [`00a25500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a25500.md) · 呼出先 5件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00447a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447a10.md) [`00467c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c68.md) [`00467c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.49% / 新版 84.49%

CFGの説明率　旧版 53.19% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a24658"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a2469c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2465c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a2465c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a24920"
      ]
    ],
    [
      "unmatched:00a246a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a24920"
      ]
    ],
    [
      "unmatched:00a2473c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00467c68"
      ]
    ]
  ],
  "added": [
    [
      "00a246a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a24920"
      ]
    ],
    [
      "00a246ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a24920"
      ]
    ],
    [
      "00a24780",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00467c68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a24658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a24618.md#insn-00a24658) · [`00a2465c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a24618.md#insn-00a2465c) · [`00a2469c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a24618.md#insn-00a2469c)

~~~diff
- 00a24658 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:1c:8"]]
- 00a24658 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:4"]]
- 00a24658 bytes 0a1c00b9
- 00a2465c ["CBRANCH", null, ["local:b35:8", "register:101:1"]]
- 00a2465c bytes 00140054
- 00a2469c ["INT_AND", "register:4058:8", ["register:4058:8", "const:ffffffffffff0000:8"]]
- 00a2469c ["INT_OR", "register:4058:8", ["register:4058:8", "const:cccd:8"]]
- 00a2469c bytes ab9999f2
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e5c9abaa4db60669151273ac3be4ac3"></a>

### [`00a24e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a24e60.md) → [`00a24ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a24/00a24ea4.md) FUN_00a24ea4

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`00658d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/00658d14.md) [`006d5524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d5524.md) [`007f7288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f7/007f7288.md) [`00896c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00896/00896c7c.md) [`008a90c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a9/008a90c0.md) · 呼出先 6件 [`008379d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00837/008379d0.md) [`00a25060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25060.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 9件 [`00658d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/00658d14.md) [`006d5524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5524.md) [`007f7288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7288.md) [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) [`008a90c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a90c0.md) · 呼出先 6件 [`008379d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/008379d0.md) [`00a250a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a250a4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 78.12% / 新版 78.12%

CFGの説明率　旧版 36.36% / 新版 35.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a24f04"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a24f30"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a24f58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a24f04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a24f78"
      ]
    ],
    [
      "unmatched:00a24f30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a24fd4"
      ]
    ],
    [
      "00a24f48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a24f5c"
      ]
    ]
  ],
  "added": [
    [
      "00a24f48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a24f78"
      ]
    ],
    [
      "00a24f74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a24fd4"
      ]
    ],
    [
      "00a24f8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a24fa0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a24ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a24e60.md#insn-00a24ec0) · [`00a24f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a24e60.md#insn-00a24f04) · [`00a24f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a24e60.md#insn-00a24f14)
- 新版 `00a24f04`（命令位置の公開資料なし） · `00a24f58`（命令位置の公開資料なし）

~~~diff
- 00a24ec0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a24ec0 ["CBRANCH", null, ["local:b44:8", "tmp:0:1"]]
+ 00a24f04 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a24f04 ["CBRANCH", null, ["local:b45:8", "tmp:0:1"]]
- 00a24ec0 bytes e10c0054
+ 00a24f04 bytes e10c0054
- 00a24f04 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a24f04 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00a24f04 bytes 81010054
- 00a24f14 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00a24f14 ["CBRANCH", null, ["local:b39:8", "tmp:0:1"]]
+ 00a24f58 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00a24f58 ["CBRANCH", null, ["local:b41:8", "tmp:0:1"]]
- 00a24f14 bytes 090900b5
+ 00a24f58 bytes 090900b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59fde4486bfeda1f2496d27de40079a5"></a>

### [`00a25060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25060.md) → [`00a250a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a250a4.md) FUN_00a250a4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a24e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a24e60.md) · 呼出先 6件 [`00888f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00888/00888f58.md) [`00a26320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26320.md) [`00a26574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26574.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00a24ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a24/00a24ea4.md) · 呼出先 6件 [`00888f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00888/00888f58.md) [`00a26364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26364.md) [`00a265b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a265b8.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 56.58% / 新版 56.58%

CFGの説明率　旧版 31.58% / 新版 31.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_condition` 3件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a25064"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a25064"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a25068"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a25064",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a25068",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2506c",
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
      "00a250a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a250ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a250b0",
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

- 旧版 [`00a25064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25060.md#insn-00a25064) · [`00a25068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25060.md#insn-00a25068) · [`00a2506c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a25060.md#insn-00a2506c)

~~~diff
- 00a25064 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a25064 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a25064 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a25064 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a25064 bytes fd7b02a9
- 00a25068 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a25068 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a25068 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00a25068 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a25068 bytes fa6703a9
- 00a2506c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a2506c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a2506c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a2506c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a2506c bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adb863b9c56babd7cfad68674c3c73be"></a>

### [`00a254bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a254bc.md) → [`00a25500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a25/00a25500.md) FUN_00a25500

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 46件 [`005a33f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a33f8.md) [`005cf984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005cf/005cf984.md) [`005e97d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e9/005e97d8.md) [`006059a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/006059a0.md) [`00609748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/00609748.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00a24618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a24/00a24618.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 46件 [`005a33f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a33f8.md) [`005cf984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cf/005cf984.md) [`005e97d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e9/005e97d8.md) [`006059a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/006059a0.md) [`00609748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/00609748.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00a2465c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a24/00a2465c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 39.29% / 新版 37.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a254bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a254c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a254c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a254bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a254c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a254c4",
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
      "00a25500",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a25504",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a25508",
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

- 旧版 [`00a254bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a254bc.md#insn-00a254bc) · [`00a254c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a254bc.md#insn-00a254c0) · [`00a254c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a25/00a254bc.md#insn-00a254c4)

~~~diff
- 00a254bc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00a254bc ["STORE", null, ["const:1b1:8", "register:8:8", "register:5100:8"]]
- 00a254bc bytes e80f1afc
- 00a254c0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a254c0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a254c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a254c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a254c0 bytes fd7b01a9
- 00a254c4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a254c4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a254c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a254c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a254c4 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f344d15b7ddcc2e257c236269a344216"></a>

### [`00a26794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26794.md) → [`00a267d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a267d8.md) _INIT_220

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00a26814",
      "incomplete_value": true,
      "site": "00a26830",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a267d0",
      "incomplete_value": true,
      "site": "00a267ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a26838",
      "incomplete_value": true,
      "site": "00a26854",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a267f4",
      "incomplete_value": true,
      "site": "00a26810",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a26858",
      "incomplete_value": true,
      "site": "00a26874",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a26814",
      "incomplete_value": true,
      "site": "00a26830",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a26814",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a26838",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a26858",
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
      "00a26814",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00a26838",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00a26858",
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

- 旧版 [`00a267cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26794.md#insn-00a267cc) · [`00a268f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26794.md#insn-00a268f4) · [`00a269c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26794.md#insn-00a269c8)
- 新版 `00a26810`（命令位置の公開資料なし） · `00a26938`（命令位置の公開資料なし） · `00a26a0c`（命令位置の公開資料なし）

~~~diff
- 00a267cc ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00a267cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a267cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a267cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a26810 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00a26810 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a26810 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a26810 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a267cc bytes 29750b91
+ 00a26810 bytes 29dd0d91
- 00a268f4 ["INT_ADD", "register:40f0:8", ["const:a268f4:8", "const:4:8"]]
- 00a268f4 ["CALL", null, ["callee:00418cb8:8"]]
+ 00a26938 ["INT_ADD", "register:40f0:8", ["const:a26938:8", "const:4:8"]]
+ 00a26938 ["CALL", null, ["callee:00418cb8:8"]]
- 00a268f4 bytes f1c8e797
+ 00a26938 bytes e0c8e797
- 00a269c8 ["INT_ADD", "register:40f0:8", ["const:a269c8:8", "const:4:8"]]
- 00a269c8 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00a26a0c ["INT_ADD", "register:40f0:8", ["const:a26a0c:8", "const:4:8"]]
+ 00a26a0c ["CALL", null, ["callee:00bdafe0:8"]]
- 00a269c8 bytes 72d10694
+ 00a26a0c bytes 75d10694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42141c052a6b7f42cd7bf5beeb9945a1"></a>

### [`00a26ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26ddc.md) → [`00a26e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26e20.md) FUN_00a26e20

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00821cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cbc.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`0084c390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c390.md) [`00a290ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a290ac.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004289f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004289f4.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`0053ee5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) [`00650798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00650/00650798.md)
- 新版 呼出元 4件 [`00821cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cbc.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`0084c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) [`00a290f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a290f0.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004289f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289f4.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`0053ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md) [`00650798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650798.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.43% / 新版 84.43%

CFGの説明率　旧版 40.00% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a26de0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a26de0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a26de4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a26de0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a26de4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a26de8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a26e24",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00a26e28",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a26e2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a26de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26ddc.md#insn-00a26de0) · [`00a26de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26ddc.md#insn-00a26de4) · [`00a26de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a26/00a26ddc.md#insn-00a26de8)

~~~diff
- 00a26de0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:70:8"]]
- 00a26de0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5120:8"]]
- 00a26de0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:8:8"]]
- 00a26de0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5100:8"]]
- 00a26de0 bytes e923076d
- 00a26de4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a26de4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a26de4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00a26de4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a26de4 bytes fd7b08a9
- 00a26de8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00a26de8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00a26de8 bytes fb4b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66646b9e3f6b1f7a54f1f8ac62834521"></a>

### [`00a271c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a27/00a271c8.md) → [`00a2720c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a27/00a2720c.md) FUN_00a2720c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 25件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`005c3468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c3468.md) [`0064e810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064e/0064e810.md) [`0064f68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064f/0064f68c.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 25件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`005c3468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c3/005c3468.md) [`0064e810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064e/0064e810.md) [`0064f68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064f/0064f68c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 50.31% / 新版 50.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 38件, `unresolved_call_alignment` 20件, `unresolved_store_alignment` 62件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a271cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a271d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a271d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a271cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a271d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a271d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a27210",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "00a27214",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00a27218",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a271cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a27/00a271c8.md#insn-00a271cc) · [`00a271d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a27/00a271c8.md#insn-00a271d0) · [`00a271d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a27/00a271c8.md#insn-00a271d4)

~~~diff
- 00a271cc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00a271cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5140:8"]]
- 00a271cc bytes ea2b00fd
- 00a271d0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00a271d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5120:8"]]
- 00a271d0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:8:8"]]
- 00a271d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5100:8"]]
- 00a271d0 bytes e923066d
- 00a271d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a271d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a271d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00a271d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a271d4 bytes fd7b07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58a7f05e17f82ac9df3f602fec9d6aa4"></a>

### [`00a28744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28744.md) → [`00a28788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28788.md) FUN_00a28788

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`008220d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/008220d0.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`00827acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827acc.md) [`0083dbdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083dbdc.md) · 呼出先 7件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a28640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28640.md) [`00a5b084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5b/00a5b084.md) [`00a5cd84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a5c/00a5cd84.md) [`00acfa94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa94.md)
- 新版 呼出元 4件 [`008220d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/008220d0.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00827acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827acc.md) [`0083dbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083dbdc.md) · 呼出先 7件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a28684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a28/00a28684.md) [`00a5b0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b0c8.md) [`00a5cdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cdc8.md) [`00acfad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfad8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 36.36% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a287ac",
      "incomplete_value": true,
      "site": "00a287b0",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a28768",
      "incomplete_value": true,
      "site": "00a2876c",
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
            "const:1f8:8"
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
      "definition_site": "00a287a8",
      "incomplete_value": false,
      "site": "00a287b0",
      "value": [
        "leaf",
        "const:8:8"
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a287c8",
      "incomplete_value": true,
      "site": "00a287cc",
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
            "const:54c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a28784",
      "incomplete_value": true,
      "site": "00a28788",
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
            "const:54c:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a2876c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28744.md#insn-00a2876c) · [`00a28788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28744.md#insn-00a28788) · [`00a287b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28744.md#insn-00a287b0)
- 新版 `00a287b0`（命令位置の公開資料なし） · `00a287cc`（命令位置の公開資料なし）

~~~diff
- 00a2876c ["INT_ADD", "register:40f0:8", ["const:a2876c:8", "const:4:8"]]
- 00a2876c ["CALL", null, ["callee:00a5b0c8:8"]]
+ 00a287b0 ["INT_ADD", "register:40f0:8", ["const:a287b0:8", "const:4:8"]]
+ 00a287b0 ["CALL", null, ["callee:00a5b0c8:8"]]
- 00a2876c bytes 46ca0094
+ 00a287b0 bytes 46ca0094
- 00a28788 ["INT_ADD", "register:40f0:8", ["const:a28788:8", "const:4:8"]]
- 00a28788 ["CALL", null, ["callee:00acfad8:8"]]
+ 00a287cc ["INT_ADD", "register:40f0:8", ["const:a287cc:8", "const:4:8"]]
+ 00a287cc ["CALL", null, ["callee:00acfad8:8"]]
- 00a28788 bytes c39c0294
+ 00a287cc bytes c39c0294
- 00a287b0 ["INT_MULT", "tmp:0:4", ["register:40b0:4", "register:4060:4"]]
- 00a287b0 ["INT_CARRY", "register:105:1", ["register:4070:4", "tmp:0:4"]]
- 00a287b0 ["INT_SCARRY", "register:106:1", ["register:4070:4", "tmp:0:4"]]
- 00a287b0 ["INT_ADD", "tmp:1:4", ["register:4070:4", "tmp:0:4"]]
- 00a287b0 bytes cc3a0c1b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf69f589ec83a0e03a9a13dbb796c72f"></a>

### [`00a294f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a294f0.md) → [`00a29534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29534.md) FUN_00a29534

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a29514"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a29514"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a29558"
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
      "unmatched:00a29514",
      "DATA",
      [
        "storage",
        "00c0c8b0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a29518",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2951c",
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
      "00a29558",
      "DATA",
      [
        "storage",
        "00c0c900",
        null,
        "undefined *"
      ]
    ],
    [
      "00a2955c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a29560",
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

- 旧版 [`00a29504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a294f0.md#insn-00a29504) · [`00a29514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a294f0.md#insn-00a29514)
- 新版 `00a29548`（命令位置の公開資料なし） · `00a29558`（命令位置の公開資料なし）

~~~diff
- 00a29504 ["INT_ADD", "register:40f0:8", ["const:a29504:8", "const:4:8"]]
- 00a29504 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a29548 ["INT_ADD", "register:40f0:8", ["const:a29548:8", "const:4:8"]]
+ 00a29548 ["CALL", null, ["callee:00bdb040:8"]]
- 00a29504 bytes bbc60694
+ 00a29548 bytes bec60694
- 00a29514 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a29514 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a29514 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a29514 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a29514 bytes 082400a9
+ 00a29558 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a29558 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a29558 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a29558 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a29558 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5f442fbe6a58423e8539e28549d9054"></a>

### [`00a29674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a29674.md) → [`00a296b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a296b8.md) _INIT_221

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.32% / 新版 72.32%

CFGの説明率　旧版 3.57% / 新版 3.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a29678"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a29678"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2967c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a29678",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2967c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a29680",
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
      "00a296bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a296c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a296c4",
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

- 旧版 [`00a29678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a29674.md#insn-00a29678) · [`00a2967c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a29674.md#insn-00a2967c) · [`00a29680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a29674.md#insn-00a29680)

~~~diff
- 00a29678 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a29678 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a29678 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00a29678 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a29678 bytes fd7b0fa9
- 00a2967c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a2967c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a2967c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00a2967c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a2967c bytes fc5710a9
- 00a29680 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a29680 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a29680 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00a29680 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a29680 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ec7bcb4a208d7a533f7a36c70394507"></a>

### [`00a29a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a29a04.md) → [`00a29a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a29a48.md) FUN_00a29a48

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`0099a654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0099a/0099a654.md) [`0099dc74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0099d/0099dc74.md) [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) · 呼出先 32件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md)
- 新版 呼出元 4件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`0099a654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099a/0099a654.md) [`0099dc74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099d/0099dc74.md) [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) · 呼出先 32件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.73% / 新版 79.73%

CFGの説明率　旧版 19.14% / 新版 19.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 40件, `return_value_candidate` 1件, `store_condition` 53件, `unresolved_branch_alignment` 67件, `unresolved_call_alignment` 17件, `unresolved_store_alignment` 104件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a29a08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a29a0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a29a0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a29a08",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a29a0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a29a10",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a29a4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00a29a50",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a29a54",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a29a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a29a04.md#insn-00a29a08) · [`00a29a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a29a04.md#insn-00a29a0c) · [`00a29a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a29a04.md#insn-00a29a10)

~~~diff
- 00a29a08 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:120:8"]]
- 00a29a08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 00a29a08 bytes e89300fd
- 00a29a0c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a29a0c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a29a0c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00a29a0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a29a0c bytes fd7b13a9
- 00a29a10 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a29a10 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a29a10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00a29a10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a29a10 bytes fc6f14a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8a48a61b5eaad267a20eb07f9429c20"></a>

### [`00a2b694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2b694.md) → [`00a2b6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2b/00a2b6d8.md) _INIT_222

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 65.12% / 新版 68.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2b6c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2b6ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2b710"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a2b6c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2b6d0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a2b6ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a2b708",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a2b714",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00a2b730",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2b6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2b694.md#insn-00a2b6c4) · [`00a2b6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2b694.md#insn-00a2b6ec)
- 新版 `00a2b708`（命令位置の公開資料なし）

~~~diff
- 00a2b6c4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a2b6c4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a2b6c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a2b6c4 bytes a9831ff8
- 00a2b6ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00a2b6ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a2b6ec bytes e013813c
+ 00a2b708 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a2b708 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 00a2b708 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00a2b708 bytes a9831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c74b77f23fdab7d63e227acac42bbad"></a>

### [`00a2ba24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2ba24.md) → [`00a2ba68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2b/00a2ba68.md) FUN_00a2ba68

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) · 呼出先 7件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041cddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cddc.md) [`0067417c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00674/0067417c.md) [`00678894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678894.md) [`0080816c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00808/0080816c.md)
- 新版 呼出元 2件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) · 呼出先 7件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) [`00678894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678894.md) [`0080816c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/0080816c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a2baa4",
      "incomplete_value": true,
      "site": "00a2baac",
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
            "const:1d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2ba60",
      "incomplete_value": true,
      "site": "00a2ba68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "live",
            "register:40a8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a2ba9c",
      "incomplete_value": false,
      "site": "00a2baac",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a2baa0",
      "incomplete_value": false,
      "site": "00a2baac",
      "value": [
        "leaf",
        "const:1:8"
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a2ba68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2ba24.md#insn-00a2ba68) · [`00a2ba40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2ba24.md#insn-00a2ba40) · [`00a2ba44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2ba24.md#insn-00a2ba44)
- 新版 `00a2baac`（命令位置の公開資料なし） · `00a2ba84`（命令位置の公開資料なし） · `00a2ba88`（命令位置の公開資料なし）

~~~diff
- 00a2ba68 ["INT_ADD", "register:40f0:8", ["const:a2ba68:8", "const:4:8"]]
- 00a2ba68 ["CALL", null, ["callee:00678894:8"]]
+ 00a2baac ["INT_ADD", "register:40f0:8", ["const:a2baac:8", "const:4:8"]]
+ 00a2baac ["CALL", null, ["callee:00678894:8"]]
- 00a2ba68 bytes 8b33f197
+ 00a2baac bytes 7a33f197
- 00a2ba40 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00a2ba40 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00a2ba84 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00a2ba84 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00a2ba40 bytes 48020034
+ 00a2ba84 bytes 48020034
- 00a2ba44 ["INT_ADD", "register:40f0:8", ["const:a2ba44:8", "const:4:8"]]
- 00a2ba44 ["CALL", null, ["callee:009d8aa4:8"]]
+ 00a2ba88 ["INT_ADD", "register:40f0:8", ["const:a2ba88:8", "const:4:8"]]
+ 00a2ba88 ["CALL", null, ["callee:009d8aa4:8"]]
- 00a2ba44 bytes 07b4fe97
+ 00a2ba88 bytes 07b4fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a42c35cb770552bbd539d07cfa84b406"></a>

### [`00a2bab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2bab0.md) → [`00a2baf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2b/00a2baf4.md) FUN_00a2baf4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) [`00a3b108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b108.md) [`00a3c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c8f8.md) · 呼出先 17件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c84.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00883d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d2c.md)
- 新版 呼出元 3件 [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) [`00a3b14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b14c.md) [`00a3c93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c93c.md) · 呼出先 17件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c84.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`00883d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d2c.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.19% / 新版 65.19%

CFGの説明率　旧版 37.86% / 新版 37.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 3件, `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 28件, `unresolved_store_alignment` 21件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2baf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2bc48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2bc5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a2baf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a2bb40",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00a2bb08",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a2bb34",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a2bb40",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a2bb4c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2baf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2bab0.md#insn-00a2baf0) · [`00a2bc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2bab0.md#insn-00a2bc30)
- 新版 `00a2bb34`（命令位置の公開資料なし） · `00a2bc74`（命令位置の公開資料なし）

~~~diff
- 00a2baf0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a2baf0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a2baf0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a2baf0 bytes a8831ff8
+ 00a2bb34 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a2bb34 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 00a2bb34 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00a2bb34 bytes a8831ff8
- 00a2bc30 ["INT_ADD", "register:40f0:8", ["const:a2bc30:8", "const:4:8"]]
- 00a2bc30 ["CALL", null, ["callee:009e9690:8"]]
+ 00a2bc74 ["INT_ADD", "register:40f0:8", ["const:a2bc74:8", "const:4:8"]]
+ 00a2bc74 ["CALL", null, ["callee:009e9690:8"]]
- 00a2bc30 bytes 87f6fe97
+ 00a2bc74 bytes 87f6fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54a8a255bf98211d316281d9baa42bdd"></a>

### [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) → [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) FUN_00a2c3b0

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`0084c390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c390.md) · 呼出先 109件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) [`0041c8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8ec.md)
- 新版 呼出元 2件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`0084c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) · 呼出先 109件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041c8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8ec.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 57.44% / 新版 57.44%

CFGの説明率　旧版 28.55% / 新版 28.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 24件, `store_destination` 3件, `store_value` 15件, `unresolved_branch_alignment` 169件, `unresolved_call_alignment` 188件, `unresolved_store_alignment` 266件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2c8b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2c8b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2c8c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a2c528",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a2c4f0"
      ]
    ],
    [
      "unmatched:00a2c4f0",
      "READ",
      [
        "storage",
        "Stack[-0x240]",
        null,
        null
      ]
    ],
    [
      "00a2c71c",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00a2c528",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2c534"
      ]
    ],
    [
      "00a2c534",
      "READ",
      [
        "storage",
        "Stack[-0x240]",
        null,
        null
      ]
    ],
    [
      "00a2c71c",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2c8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md#insn-00a2c8b4) · [`00a2c8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md#insn-00a2c8b8) · [`00a2c8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md#insn-00a2c8c4)

~~~diff
- 00a2c8b4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 00a2c8b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:4"]]
- 00a2c8b4 bytes 192000b9
- 00a2c8b8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:158:8"]]
- 00a2c8b8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a2c8b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00a2c8b8 bytes 1fac00f9
- 00a2c8c4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a2c8c4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a2c8c4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a2c8c4 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00a2c8c4 bytes 1f7c00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01f2ccda7ad10dc2a88691199a329054"></a>

### [`00a2fc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2f/00a2fc5c.md) → [`00a2fca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2f/00a2fca0.md) FUN_00a2fca0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) · 呼出先 7件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0073e08c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e08c.md) [`00a33a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33a60.md) [`00a33d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33d6c.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 2件 [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) · 呼出先 7件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0073e08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e08c.md) [`00a33aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33aa4.md) [`00a33db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33db0.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 34.04% / 新版 34.04%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2fc5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2fc5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2fc60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a2fc5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2fc60",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2fc84",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00a2fca0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a2fca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a2fcc8",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2fc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2f/00a2fc5c.md#insn-00a2fc5c) · [`00a2fc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2f/00a2fc5c.md#insn-00a2fc60) · [`00a2fc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2f/00a2fc5c.md#insn-00a2fc88)

~~~diff
- 00a2fc5c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a2fc5c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a2fc5c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a2fc5c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a2fc5c bytes fd7bbea9
- 00a2fc60 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a2fc60 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a2fc60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a2fc60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a2fc60 bytes f44f01a9
- 00a2fc88 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00a2fc88 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00a2fc88 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00a2fc88 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00a2fc88 bytes c8010036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35a1562a899314a6f17ac3bb716901ce"></a>

### [`00a2fd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2f/00a2fd18.md) → [`00a2fd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2f/00a2fd5c.md) FUN_00a2fd5c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00449c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c34.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00467c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c58.md)
- 新版 呼出元 1件 [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00449c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00467c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c58.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.84% / 新版 75.84%

CFGの説明率　旧版 29.52% / 新版 30.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_value` 1件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2fd2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2fd2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2fd30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a2fd2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2fd30",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2fd44",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a2fd70",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a2fd74",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a2fd88",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2fd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2f/00a2fd18.md#insn-00a2fd2c) · [`00a2fd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2f/00a2fd18.md#insn-00a2fd30) · [`00a2fd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2f/00a2fd18.md#insn-00a2fd44)

~~~diff
- 00a2fd2c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a2fd2c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a2fd2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00a2fd2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a2fd2c bytes f65710a9
- 00a2fd30 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a2fd30 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a2fd30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00a2fd30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a2fd30 bytes f44f11a9
- 00a2fd44 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a2fd44 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00a2fd44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a2fd44 bytes a8031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da8283a3c1194b1e62dc57368590f6ae"></a>

### [`00a30514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a30514.md) → [`00a30558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30558.md) FUN_00a30558

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 75件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 75件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.57% / 新版 83.57%

CFGの説明率　旧版 62.53% / 新版 62.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 29件, `store_condition` 15件, `store_value` 5件, `unresolved_branch_alignment` 49件, `unresolved_call_alignment` 61件, `unresolved_store_alignment` 26件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a30870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a30968"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a30b1c",
      "incomplete_value": false,
      "site": "00a30b1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a30ad8",
      "incomplete_value": false,
      "site": "00a30ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a30594",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a305a8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a305b0",
      "PARAM",
      [
        "storage",
        "00c0c920",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a30594",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a305a8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a305b0",
      "PARAM",
      [
        "storage",
        "00c0c970",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a30870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a30514.md#insn-00a30870) · [`00a30968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a30514.md#insn-00a30968)
- 新版 `00a308b4`（命令位置の公開資料なし）

~~~diff
- 00a30870 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:2c0:8"]]
- 00a30870 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00a30870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 00a30870 bytes 5fc302b9
+ 00a308b4 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:2c0:8"]]
+ 00a308b4 ["COPY", "tmp:1:4", ["const:0:4"]]
+ 00a308b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
+ 00a308b4 bytes 5fc302b9
- 00a30968 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:9f4:8"]]
- 00a30968 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00a30968 bytes 28f709b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34e7a0c7d8638a178726b1a7d7d0e490"></a>

### [`00a33510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33510.md) → [`00a33554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33554.md) FUN_00a33554

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a30514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a30514.md) · 呼出先 10件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`004707b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/004707b8.md) [`0071a0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a0f8.md) [`0071b838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071b838.md)
- 新版 呼出元 1件 [`00a30558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30558.md) · 呼出先 10件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`004707b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/004707b8.md) [`0071a0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071a/0071a0f8.md) [`0071b838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071b838.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 97.00% / 新版 97.00%

CFGの説明率　旧版 95.65% / 新版 91.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a33614",
      "incomplete_value": false,
      "site": "00a33614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a335d0",
      "incomplete_value": false,
      "site": "00a335d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a33698"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00a336dc"
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
      "00a33614",
      "DATA",
      [
        "storage",
        "00c0d578",
        null,
        "undefined *"
      ]
    ],
    [
      "00a336b0",
      "READ",
      [
        "storage",
        "00c0d598",
        null,
        "pointer"
      ]
    ],
    [
      "00a336b0",
      "READ",
      [
        "storage",
        "00c0d5a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a33614",
      "DATA",
      [
        "storage",
        "00c0d5c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a336b0",
      "READ",
      [
        "storage",
        "00c0d5e8",
        null,
        "pointer"
      ]
    ],
    [
      "00a336b0",
      "READ",
      [
        "storage",
        "00c0d5f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a33698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33510.md#insn-00a33698) · [`00a3355c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33510.md#insn-00a3355c)
- 新版 `00a336dc`（命令位置の公開資料なし） · `00a335a0`（命令位置の公開資料なし）

~~~diff
- 00a33698 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a33698 ["RETURN", null, ["register:0:8"]]
- 00a33698 bytes c0035fd6
+ 00a336dc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00a336dc ["RETURN", null, ["register:0:8"]]
+ 00a336dc bytes c0035fd6
- 00a3355c ["INT_ADD", "register:40f0:8", ["const:a3355c:8", "const:4:8"]]
- 00a3355c ["CALL", null, ["ram:469e20:8"]]
+ 00a335a0 ["INT_ADD", "register:40f0:8", ["const:a335a0:8", "const:4:8"]]
+ 00a335a0 ["CALL", null, ["ram:469e20:8"]]
- 00a3355c bytes 31dae897
+ 00a335a0 bytes 20dae897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81bdc2673fd2f33d75ba93e73087f69c"></a>

### [`00a3371c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a3371c.md) → [`00a33760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33760.md) FUN_00a33760

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a30514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a30/00a30514.md) · 呼出先 10件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`004707b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/004707b8.md) [`00646dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646dc4.md) [`009785f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/009785f0.md)
- 新版 呼出元 1件 [`00a30558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30558.md) · 呼出先 10件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`004707b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/004707b8.md) [`00646dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646dc4.md) [`009785f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/009785f0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 76.00% / 新版 76.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a33820",
      "incomplete_value": false,
      "site": "00a33820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a337dc",
      "incomplete_value": false,
      "site": "00a337dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
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
    "new": null,
    "old": {
      "definition_site": "00a3381c",
      "incomplete_value": false,
      "site": "00a33838",
      "value": [
        "leaf",
        "const:e:8"
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a33890",
      "incomplete_value": true,
      "site": "00a3389c",
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
            "const:22b0:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a33820",
      "DATA",
      [
        "storage",
        "00c0d4f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a338d4",
      "READ",
      [
        "storage",
        "00c0d518",
        null,
        "pointer"
      ]
    ],
    [
      "00a338d4",
      "READ",
      [
        "storage",
        "00c0d520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a33820",
      "DATA",
      [
        "storage",
        "00c0d548",
        null,
        "undefined *"
      ]
    ],
    [
      "00a338d4",
      "READ",
      [
        "storage",
        "00c0d568",
        null,
        "pointer"
      ]
    ],
    [
      "00a338d4",
      "READ",
      [
        "storage",
        "00c0d570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a33838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a3371c.md#insn-00a33838) · [`00a33858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a3371c.md#insn-00a33858) · [`00a3376c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a3371c.md#insn-00a3376c)
- 新版 `00a3387c`（命令位置の公開資料なし） · `00a3389c`（命令位置の公開資料なし） · `00a337b0`（命令位置の公開資料なし）

~~~diff
- 00a33838 ["INT_ADD", "register:40f0:8", ["const:a33838:8", "const:4:8"]]
- 00a33838 ["CALL", null, ["callee:00646dc4:8"]]
+ 00a3387c ["INT_ADD", "register:40f0:8", ["const:a3387c:8", "const:4:8"]]
+ 00a3387c ["CALL", null, ["callee:00646dc4:8"]]
- 00a33838 bytes 634df097
+ 00a3387c bytes 524df097
- 00a33858 ["INT_ADD", "register:40f0:8", ["const:a33858:8", "const:4:8"]]
- 00a33858 ["CALL", null, ["callee:00a02dd4:8"]]
+ 00a3389c ["INT_ADD", "register:40f0:8", ["const:a3389c:8", "const:4:8"]]
+ 00a3389c ["CALL", null, ["callee:00a02dd4:8"]]
- 00a33858 bytes 4e3dff97
+ 00a3389c bytes 4e3dff97
- 00a3376c ["INT_ADD", "register:40f0:8", ["const:a3376c:8", "const:4:8"]]
- 00a3376c ["CALL", null, ["ram:469e20:8"]]
+ 00a337b0 ["INT_ADD", "register:40f0:8", ["const:a337b0:8", "const:4:8"]]
+ 00a337b0 ["CALL", null, ["ram:469e20:8"]]
- 00a3376c bytes add9e897
+ 00a337b0 bytes 9cd9e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12f1192989285515a1025cfb81429c6c"></a>

### [`00a33944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33944.md) → [`00a33988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33988.md) FUN_00a33988

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`009a1cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a1/009a1cd4.md) · 呼出先 4件 [`00a3cc9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cc9c.md) [`00a3cca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cca0.md) [`00a3cca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cca4.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`009a1cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a1/009a1cd4.md) · 呼出先 4件 [`00a3cce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cce0.md) [`00a3cce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cce4.md) [`00a3cce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cce8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 78.57% / 新版 73.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a339c4",
      "incomplete_value": false,
      "site": "00a339c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a33980",
      "incomplete_value": false,
      "site": "00a33980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
    "new": null,
    "old": {
      "definition_site": "00a339a0",
      "incomplete_value": true,
      "site": "00a339ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:10:8"
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
    "new": null,
    "old": {
      "definition_site": "00a339a4",
      "incomplete_value": true,
      "site": "00a339ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:c:8"
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
      "00a339c4",
      "DATA",
      [
        "storage",
        "00c0d478",
        null,
        "undefined *"
      ]
    ],
    [
      "00a33a28",
      "READ",
      [
        "storage",
        "00c0d498",
        null,
        "pointer"
      ]
    ],
    [
      "00a33a28",
      "READ",
      [
        "storage",
        "00c0d4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a339c4",
      "DATA",
      [
        "storage",
        "00c0d4c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a33a28",
      "READ",
      [
        "storage",
        "00c0d4e8",
        null,
        "pointer"
      ]
    ],
    [
      "00a33a28",
      "READ",
      [
        "storage",
        "00c0d4f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a339ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33944.md#insn-00a339ac) · [`00a339c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33944.md#insn-00a339c4) · [`00a33970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33944.md#insn-00a33970)
- 新版 `00a339f0`（命令位置の公開資料なし） · `00a33a08`（命令位置の公開資料なし） · `00a339b4`（命令位置の公開資料なし）

~~~diff
- 00a339ac ["INT_ADD", "register:40f0:8", ["const:a339ac:8", "const:4:8"]]
- 00a339ac ["CALL", null, ["callee:00a3cce8:8"]]
+ 00a339f0 ["INT_ADD", "register:40f0:8", ["const:a339f0:8", "const:4:8"]]
+ 00a339f0 ["CALL", null, ["callee:00a3cce8:8"]]
- 00a339ac bytes be240094
+ 00a339f0 bytes be240094
- 00a339c4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00a339c4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00a33a08 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00a33a08 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00a339c4 bytes 400100b4
+ 00a33a08 bytes 400100b4
- 00a33970 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00a33970 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00a33970 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00a33970 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00a339b4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00a339b4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00a339b4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00a339b4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00a33970 bytes e8030037
+ 00a339b4 bytes e8030037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98052172d207df0916388c3e698cb512"></a>

### [`00a33a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33a60.md) → [`00a33aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33aa4.md) FUN_00a33aa4

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a2fc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2f/00a2fc5c.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`00574ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`00a2fca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2f/00a2fca0.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`00574ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.94% / 新版 92.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a33ae8",
      "incomplete_value": true,
      "site": "00a33ae8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b49:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a33aa4",
      "incomplete_value": true,
      "site": "00a33aa4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:abe:8"
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
      "definition_site": "00a33aec",
      "incomplete_value": true,
      "site": "00a33aec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00a33aa8",
      "incomplete_value": true,
      "site": "00a33aa8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a33bf4",
      "incomplete_value": true,
      "site": "00a33bf4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a33bb0",
      "incomplete_value": true,
      "site": "00a33bb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cee:8"
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
      "00a33acc",
      "READ",
      [
        "storage",
        "002a2abe",
        null,
        "string"
      ]
    ],
    [
      "00a33ae0",
      "READ",
      [
        "storage",
        "002a2ac3",
        null,
        "string"
      ]
    ],
    [
      "00a33b18",
      "READ",
      [
        "storage",
        "00c250d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00a33acc",
      "READ",
      [
        "storage",
        "002a2b49",
        null,
        "string"
      ]
    ],
    [
      "00a33ae0",
      "READ",
      [
        "storage",
        "002a2b4e",
        null,
        "string"
      ]
    ],
    [
      "00a33b18",
      "READ",
      [
        "storage",
        "00c25118",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a33bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33a60.md#insn-00a33bf8) · [`00a33a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33a60.md#insn-00a33a80) · [`00a33ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33a60.md#insn-00a33ab8)
- 新版 `00a33c3c`（命令位置の公開資料なし） · `00a33ac4`（命令位置の公開資料なし） · `00a33afc`（命令位置の公開資料なし）

~~~diff
- 00a33bf8 ["INT_ADD", "register:40f0:8", ["const:a33bf8:8", "const:4:8"]]
- 00a33bf8 ["CALL", null, ["callee:00418fe0:8"]]
+ 00a33c3c ["INT_ADD", "register:40f0:8", ["const:a33c3c:8", "const:4:8"]]
+ 00a33c3c ["CALL", null, ["callee:00418fe0:8"]]
- 00a33bf8 bytes fa94e797
+ 00a33c3c bytes e994e797
- 00a33a80 ["COPY", "tmp:0:8", ["const:abe:8"]]
- 00a33a80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a33a80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a33a80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a33ac4 ["COPY", "tmp:0:8", ["const:b49:8"]]
+ 00a33ac4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a33ac4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a33ac4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a33a80 bytes 29f92a91
+ 00a33ac4 bytes 29252d91
- 00a33ab8 ["INT_ADD", "register:40f0:8", ["const:a33ab8:8", "const:4:8"]]
- 00a33ab8 ["CALL", null, ["callee:00574ff0:8"]]
+ 00a33afc ["INT_ADD", "register:40f0:8", ["const:a33afc:8", "const:4:8"]]
+ 00a33afc ["CALL", null, ["callee:00574ff0:8"]]
- 00a33ab8 bytes 4e05ed97
+ 00a33afc bytes 3d05ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3307b18acbf61cc80d377420621c9e91"></a>

### [`00a33d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33d6c.md) → [`00a33db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33db0.md) FUN_00a33db0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2fc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2f/00a2fc5c.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00449c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c34.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`00467c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c58.md) [`00467c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c60.md)
- 新版 呼出元 1件 [`00a2fca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2f/00a2fca0.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00449c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`00467c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c58.md) [`00467c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.45% / 新版 94.45%

CFGの説明率　旧版 84.78% / 新版 84.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a33e00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a33e04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a33f1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a33e30",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "00a33e34",
      "READ",
      [
        "storage",
        "00c250d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00a33e3c",
      "READ",
      [
        "storage",
        "00c250d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00a33e30",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "00a33e34",
      "READ",
      [
        "storage",
        "00c25118",
        null,
        "undefined1"
      ]
    ],
    [
      "00a33e3c",
      "READ",
      [
        "storage",
        "00c25118",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a33e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33d6c.md#insn-00a33e00) · [`00a33e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a33d6c.md#insn-00a33e04)
- 新版 `00a33e44`（命令位置の公開資料なし）

~~~diff
- 00a33e00 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00a33e00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a33e00 bytes a0039a3c
- 00a33e04 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a33e04 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb0:8"]]
- 00a33e04 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a33e04 bytes a8031bf8
+ 00a33e44 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
+ 00a33e44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00a33e44 bytes a0039a3c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe449ba97a118daf2601b2ee40a37e2b"></a>

### [`00a34758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34758.md) → [`00a3479c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a3479c.md) FUN_00a3479c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 2件 [`00a3d0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3d0f0.md) [`00a3d1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3d1f8.md) · 呼出先 10件 [`00821cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cb4.md) [`00883cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883cc0.md) [`008847e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/008847e4.md) [`009e97a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e97a8.md) [`009e97b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e97b8.md)
- 新版 呼出元 2件 [`00a3d134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d134.md) [`00a3d23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3d/00a3d23c.md) · 呼出先 10件 [`00821cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cb4.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md) [`008847e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/008847e4.md) [`009e97ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e97ec.md) [`009e97fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e97fc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 91.67% / 新版 88.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a348a0",
      "incomplete_value": true,
      "site": "00a348a4",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 17,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a348a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34758.md#insn-00a348a4) · [`00a3479c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34758.md#insn-00a3479c) · [`00a347a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34758.md#insn-00a347a0)
- 新版 `00a348e8`（命令位置の公開資料なし） · `00a347e0`（命令位置の公開資料なし） · `00a347e4`（命令位置の公開資料なし）

~~~diff
- 00a348a4 ["INT_ADD", "register:40f0:8", ["const:a348a4:8", "const:4:8"]]
- 00a348a4 ["CALL", null, ["callee:00bdb030:8"]]
+ 00a348e8 ["INT_ADD", "register:40f0:8", ["const:a348e8:8", "const:4:8"]]
+ 00a348e8 ["CALL", null, ["callee:00bdb030:8"]]
- 00a348a4 bytes cf990694
+ 00a348e8 bytes d2990694
- 00a3479c ["INT_ADD", "register:40f0:8", ["const:a3479c:8", "const:4:8"]]
- 00a3479c ["CALL", null, ["callee:008847e4:8"]]
+ 00a347e0 ["INT_ADD", "register:40f0:8", ["const:a347e0:8", "const:4:8"]]
+ 00a347e0 ["CALL", null, ["callee:008847e4:8"]]
- 00a3479c bytes 1240f997
+ 00a347e0 bytes 0140f997
- 00a347a0 ["INT_ADD", "register:40f0:8", ["const:a347a0:8", "const:4:8"]]
- 00a347a0 ["CALL", null, ["callee:00883cc0:8"]]
+ 00a347e4 ["INT_ADD", "register:40f0:8", ["const:a347e4:8", "const:4:8"]]
+ 00a347e4 ["CALL", null, ["callee:00883cc0:8"]]
- 00a347a0 bytes 483df997
+ 00a347e4 bytes 373df997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af9a1c7d0410751e3b651332980eb4ce"></a>

### [`00a34a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34a8c.md) → [`00a34ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34ad0.md) FUN_00a34ad0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) [`00a34c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34c84.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00449c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c34.md) [`00467c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c58.md) [`00467c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467c60.md) [`0073e07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e07c.md)
- 新版 呼出元 2件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) [`00a34cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34cc8.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00449c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md) [`00467c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c58.md) [`00467c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c60.md) [`0073e07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e07c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.33% / 新版 98.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a34b44",
      "incomplete_value": false,
      "site": "00a34b48",
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
    "old": {
      "definition_site": "00a34b00",
      "incomplete_value": false,
      "site": "00a34b04",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a34b44",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00a34b44",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a34b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34a8c.md#insn-00a34b04) · [`00a34aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34a8c.md#insn-00a34aa0) · [`00a34ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34a8c.md#insn-00a34ab4)
- 新版 `00a34b48`（命令位置の公開資料なし） · `00a34ae4`（命令位置の公開資料なし） · `00a34af8`（命令位置の公開資料なし）

~~~diff
- 00a34b04 ["INT_ADD", "register:40f0:8", ["const:a34b04:8", "const:4:8"]]
- 00a34b04 ["CALL", null, ["callee:00449c34:8"]]
+ 00a34b48 ["INT_ADD", "register:40f0:8", ["const:a34b48:8", "const:4:8"]]
+ 00a34b48 ["CALL", null, ["callee:00449c34:8"]]
- 00a34b04 bytes 4c54e897
+ 00a34b48 bytes 3b54e897
- 00a34aa0 ["INT_ADD", "register:40f0:8", ["const:a34aa0:8", "const:4:8"]]
- 00a34aa0 ["CALL", null, ["callee:0073e07c:8"]]
+ 00a34ae4 ["INT_ADD", "register:40f0:8", ["const:a34ae4:8", "const:4:8"]]
+ 00a34ae4 ["CALL", null, ["callee:0073e07c:8"]]
- 00a34aa0 bytes 7725f497
+ 00a34ae4 bytes 6625f497
- 00a34ab4 ["INT_ADD", "register:40f0:8", ["const:a34ab4:8", "const:4:8"]]
- 00a34ab4 ["CALL", null, ["callee:008847e4:8"]]
+ 00a34af8 ["INT_ADD", "register:40f0:8", ["const:a34af8:8", "const:4:8"]]
+ 00a34af8 ["CALL", null, ["callee:008847e4:8"]]
- 00a34ab4 bytes 4c3ff997
+ 00a34af8 bytes 3b3ff997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20d4b81e4dd2254ff8de3012ab613c2e"></a>

### [`00a34c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34c84.md) → [`00a34cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34cc8.md) FUN_00a34cc8

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 56件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444fcc.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 56件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fcc.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.64% / 新版 85.64%

CFGの説明率　旧版 63.25% / 新版 63.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 26件, `store_value` 3件, `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 21件, `unresolved_store_alignment` 19件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a34d98",
      "incomplete_value": true,
      "site": "00a34dac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fcb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a34d54",
      "incomplete_value": true,
      "site": "00a34d68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:58:8"
              ]
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
    "kind": "store_value",
    "new": {
      "definition_site": "00a34df8",
      "incomplete_value": true,
      "site": "00a34e04",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00a34db4",
      "incomplete_value": true,
      "site": "00a34dc0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a34df4",
      "incomplete_value": true,
      "site": "00a34e10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fb9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a34db0",
      "incomplete_value": true,
      "site": "00a34dcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f1f:8"
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
      "00a34d08",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a34d1c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a34d24",
      "PARAM",
      [
        "storage",
        "00c0c920",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a34d08",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a34d1c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a34d24",
      "PARAM",
      [
        "storage",
        "00c0c970",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a34d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34c84.md#insn-00a34d7c) · [`00a34dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34c84.md#insn-00a34dac) · [`00a3516c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a34/00a34c84.md#insn-00a3516c)
- 新版 `00a34dc0`（命令位置の公開資料なし） · `00a351b0`（命令位置の公開資料なし）

~~~diff
- 00a34d7c ["INT_ADD", "register:40f0:8", ["const:a34d7c:8", "const:4:8"]]
- 00a34d7c ["CALL", null, ["callee:009019f4:8"]]
+ 00a34dc0 ["INT_ADD", "register:40f0:8", ["const:a34dc0:8", "const:4:8"]]
+ 00a34dc0 ["CALL", null, ["callee:009019f4:8"]]
- 00a34d7c bytes 1e33fb97
+ 00a34dc0 bytes 0d33fb97
- 00a34dac ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00a34dac bytes e9c3ff90
- 00a3516c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a3516c ["CBRANCH", null, ["local:b251:8", "tmp:0:1"]]
+ 00a351b0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a351b0 ["CBRANCH", null, ["local:b246:8", "tmp:0:1"]]
- 00a3516c bytes 81d10054
+ 00a351b0 bytes 81d10054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c63ff8f7e7fdda7d468b4fec7dade72b"></a>

### [`00a37688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37688.md) → [`00a376cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a376cc.md) FUN_00a376cc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a3c280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c280.md) [`00a3c358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c358.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) [`0041cc4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cc4c.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 2件 [`00a3c2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c2c4.md) [`00a3c39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c39c.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041cc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cc4c.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.75% / 新版 99.75%

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
      "site": "00a37c54",
      "value": [
        "leaf",
        "ram:a26d00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a37c10",
      "value": [
        "leaf",
        "ram:a26cbc:8"
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
      "00a37c54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a26cbc"
      ]
    ]
  ],
  "added": [
    [
      "00a37c54",
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

- 旧版 [`00a37bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37688.md#insn-00a37bcc) · [`00a37c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37688.md#insn-00a37c10) · [`00a376e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37688.md#insn-00a376e0)
- 新版 `00a37c10`（命令位置の公開資料なし） · `00a37c54`（命令位置の公開資料なし） · `00a37724`（命令位置の公開資料なし）

~~~diff
- 00a37bcc ["INT_ADD", "register:40f0:8", ["const:a37bcc:8", "const:4:8"]]
- 00a37bcc ["CALL", null, ["callee:0041c120:8"]]
+ 00a37c10 ["INT_ADD", "register:40f0:8", ["const:a37c10:8", "const:4:8"]]
+ 00a37c10 ["CALL", null, ["callee:0041c120:8"]]
- 00a37bcc bytes 5591e797
+ 00a37c10 bytes 4491e797
- 00a37c10 ["INT_ADD", "register:40f0:8", ["const:a37c10:8", "const:4:8"]]
- 00a37c10 ["CALL", null, ["ram:a26cbc:8"]]
+ 00a37c54 ["INT_ADD", "register:40f0:8", ["const:a37c54:8", "const:4:8"]]
+ 00a37c54 ["CALL", null, ["ram:a26d00:8"]]
- 00a37c10 bytes 2bbcff97
+ 00a37c54 bytes 2bbcff97
- 00a376e0 ["INT_ADD", "register:40f0:8", ["const:a376e0:8", "const:4:8"]]
- 00a376e0 ["CALL", null, ["callee:00bdb5e0:8"]]
+ 00a37724 ["INT_ADD", "register:40f0:8", ["const:a37724:8", "const:4:8"]]
+ 00a37724 ["CALL", null, ["callee:00bdb5e0:8"]]
- 00a376e0 bytes ac8f0694
+ 00a37724 bytes af8f0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc51bd7a44d8091a638faa8a1a0b0b09"></a>

### [`00a37ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37ddc.md) → [`00a37e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a37e20.md) FUN_00a37e20

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a37e44",
      "incomplete_value": false,
      "site": "00a37e44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a37e00",
      "incomplete_value": false,
      "site": "00a37e00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "00a37e44",
      "DATA",
      [
        "storage",
        "00c0c948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a37e44",
      "DATA",
      [
        "storage",
        "00c0c998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a37df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37ddc.md#insn-00a37df0) · [`00a37dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37ddc.md#insn-00a37dfc)
- 新版 `00a37e34`（命令位置の公開資料なし） · `00a37e40`（命令位置の公開資料なし）

~~~diff
- 00a37df0 ["INT_ADD", "register:40f0:8", ["const:a37df0:8", "const:4:8"]]
- 00a37df0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a37e34 ["INT_ADD", "register:40f0:8", ["const:a37e34:8", "const:4:8"]]
+ 00a37e34 ["CALL", null, ["callee:00bdb040:8"]]
- 00a37df0 bytes 808c0694
+ 00a37e34 bytes 838c0694
- 00a37dfc ["COPY", "tmp:0:8", ["const:948:8"]]
- 00a37dfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a37dfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a37dfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a37e40 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00a37e40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a37e40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a37e40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a37dfc bytes 08212591
+ 00a37e40 bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-164c48d80e87b44de1fcbbf0b87068ad"></a>

### [`00a37e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37e10.md) → [`00a37e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a37e54.md) FUN_00a37e54

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a37e60",
      "incomplete_value": false,
      "site": "00a37e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a37e1c",
      "incomplete_value": false,
      "site": "00a37e1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "00a37e60",
      "DATA",
      [
        "storage",
        "00c0c948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a37e60",
      "DATA",
      [
        "storage",
        "00c0c998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a37e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37e10.md#insn-00a37e18)
- 新版 `00a37e5c`（命令位置の公開資料なし）

~~~diff
- 00a37e18 ["COPY", "tmp:0:8", ["const:948:8"]]
- 00a37e18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a37e18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a37e18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a37e5c ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00a37e5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a37e5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a37e5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a37e18 bytes 29212591
+ 00a37e5c bytes 29612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b508e9939bd659c9616082914e1e606"></a>

### [`00a37ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37ecc.md) → [`00a37f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a37/00a37f10.md) FUN_00a37f10

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) · 呼出先 22件 [`0044b8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8ec.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c020.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md) [`0044c794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c794.md)
- 新版 呼出元 1件 [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) · 呼出先 22件 [`0044b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0044c020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c020.md) [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) [`0044c794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c794.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 35.54% / 新版 35.54%

CFGの説明率　旧版 13.27% / 新版 13.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `store_value` 5件, `unresolved_branch_alignment` 138件, `unresolved_call_alignment` 154件, `unresolved_store_alignment` 239件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a37efc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a37f10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a37fa8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a37efc",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a37f00",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0089d9f4"
      ]
    ],
    [
      "unmatched:00a37f10",
      "DATA",
      [
        "storage",
        "00c0c9c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a37f40",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00a37f44",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0089d9f4"
      ]
    ],
    [
      "00a37f54",
      "DATA",
      [
        "storage",
        "00c0ca18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a37efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37ecc.md#insn-00a37efc) · [`00a37f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37ecc.md#insn-00a37f10) · [`00a37fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a37/00a37ecc.md#insn-00a37fa8)

~~~diff
- 00a37efc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a37efc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00a37efc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a37efc bytes a8831ef8
- 00a37f10 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a37f10 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00a37f10 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:b8:8"]]
- 00a37f10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a37f10 bytes 88860bf8
- 00a37fa8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00a37fa8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00a37fa8 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffbe:8"]]
- 00a37fa8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00a37fa8 bytes bfe31b38
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-116589e567ee2a86368843796b6a383d"></a>

### [`00a3a11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a11c.md) → [`00a3a160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a160.md) FUN_00a3a160

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a3a2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a2e4.md) · 呼出先 6件 [`0044b9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c104.md) [`0064c828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c828.md) [`006582c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006582c8.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00a3a328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a328.md) · 呼出先 6件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md) [`0064c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c828.md) [`006582c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006582c8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a3a170",
      "incomplete_value": false,
      "site": "00a3a178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3a12c",
      "incomplete_value": false,
      "site": "00a3a134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
      "definition_site": "00a3a2e4",
      "incomplete_value": false,
      "site": "00a3a2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3a2a0",
      "incomplete_value": false,
      "site": "00a3a2a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "00a3a178",
      "DATA",
      [
        "storage",
        "00c0c9c8",
        null,
        "pointer"
      ]
    ],
    [
      "00a3a2e8",
      "DATA",
      [
        "storage",
        "00c063e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a3a178",
      "DATA",
      [
        "storage",
        "00c0ca18",
        null,
        "pointer"
      ]
    ],
    [
      "00a3a2e8",
      "DATA",
      [
        "storage",
        "00c06430",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3a12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a11c.md#insn-00a3a12c) · [`00a3a13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a11c.md#insn-00a3a13c) · [`00a3a144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a11c.md#insn-00a3a144)
- 新版 `00a3a170`（命令位置の公開資料なし） · `00a3a180`（命令位置の公開資料なし） · `00a3a188`（命令位置の公開資料なし）

~~~diff
- 00a3a12c ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 00a3a12c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3a12c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3a12c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3a170 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 00a3a170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3a170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3a170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3a12c bytes 08212791
+ 00a3a170 bytes 08612891
- 00a3a13c ["INT_ADD", "register:40f0:8", ["const:a3a13c:8", "const:4:8"]]
- 00a3a13c ["CALL", null, ["callee:0044b9cc:8"]]
+ 00a3a180 ["INT_ADD", "register:40f0:8", ["const:a3a180:8", "const:4:8"]]
+ 00a3a180 ["CALL", null, ["callee:0044b9cc:8"]]
- 00a3a13c bytes 2446e897
+ 00a3a180 bytes 1346e897
- 00a3a144 ["INT_ADD", "register:40f0:8", ["const:a3a144:8", "const:4:8"]]
- 00a3a144 ["CALL", null, ["callee:0044b9cc:8"]]
+ 00a3a188 ["INT_ADD", "register:40f0:8", ["const:a3a188:8", "const:4:8"]]
+ 00a3a188 ["CALL", null, ["callee:0044b9cc:8"]]
- 00a3a144 bytes 2246e897
+ 00a3a188 bytes 1146e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fc9d29225bd8f7e6902fa8faf610a18"></a>

### [`00a3a30c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a30c.md) → [`00a3a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a350.md) FUN_00a3a350

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3a364",
      "incomplete_value": false,
      "site": "00a3a368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3a320",
      "incomplete_value": false,
      "site": "00a3a324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "00a3a368",
      "DATA",
      [
        "storage",
        "00c0c9e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3a368",
      "DATA",
      [
        "storage",
        "00c0ca38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3a318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a30c.md#insn-00a3a318) · [`00a3a320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a30c.md#insn-00a3a320)
- 新版 `00a3a35c`（命令位置の公開資料なし） · `00a3a364`（命令位置の公開資料なし）

~~~diff
- 00a3a318 ["INT_ADD", "register:40f0:8", ["const:a3a318:8", "const:4:8"]]
- 00a3a318 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a3a35c ["INT_ADD", "register:40f0:8", ["const:a3a35c:8", "const:4:8"]]
+ 00a3a35c ["CALL", null, ["callee:00bdb040:8"]]
- 00a3a318 bytes 36830694
+ 00a3a35c bytes 39830694
- 00a3a320 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00a3a320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3a320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3a320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3a364 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 00a3a364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3a364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3a364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3a320 bytes 08a12791
+ 00a3a364 bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c52b81cb1b75d1007350be900859e804"></a>

### [`00a3a330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a330.md) → [`00a3a374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3a374.md) FUN_00a3a374

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3a378",
      "incomplete_value": false,
      "site": "00a3a37c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3a334",
      "incomplete_value": false,
      "site": "00a3a338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "00a3a37c",
      "DATA",
      [
        "storage",
        "00c0c9e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3a37c",
      "DATA",
      [
        "storage",
        "00c0ca38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3a334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a330.md#insn-00a3a334)
- 新版 `00a3a378`（命令位置の公開資料なし）

~~~diff
- 00a3a334 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00a3a334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3a334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3a334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3a378 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 00a3a378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3a378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3a378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3a334 bytes 08a12791
+ 00a3a378 bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ea5fd767f2033397768766a778072b2"></a>

### [`00a3a9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a9d0.md) → [`00a3aa14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3aa14.md) FUN_00a3aa14

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-6c02ae9e786f49039b727123c6996f2a"></a>

### [`00a3a9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a9fc.md) → [`00a3aa40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3aa40.md) FUN_00a3aa40

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3aa54",
      "incomplete_value": false,
      "site": "00a3aa58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3aa10",
      "incomplete_value": false,
      "site": "00a3aa14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
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
      "00a3aa58",
      "DATA",
      [
        "storage",
        "00c0ca58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3aa58",
      "DATA",
      [
        "storage",
        "00c0caa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3aa08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a9fc.md#insn-00a3aa08) · [`00a3aa10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3a9fc.md#insn-00a3aa10)
- 新版 `00a3aa4c`（命令位置の公開資料なし） · `00a3aa54`（命令位置の公開資料なし）

~~~diff
- 00a3aa08 ["INT_ADD", "register:40f0:8", ["const:a3aa08:8", "const:4:8"]]
- 00a3aa08 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a3aa4c ["INT_ADD", "register:40f0:8", ["const:a3aa4c:8", "const:4:8"]]
+ 00a3aa4c ["CALL", null, ["callee:00bdb040:8"]]
- 00a3aa08 bytes 7a810694
+ 00a3aa4c bytes 7d810694
- 00a3aa10 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 00a3aa10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3aa10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3aa10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3aa54 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 00a3aa54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3aa54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3aa54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3aa10 bytes 08612991
+ 00a3aa54 bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-052431edff91a85217070fc38b3bd644"></a>

### [`00a3aa20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3aa20.md) → [`00a3aa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3aa64.md) FUN_00a3aa64

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3aa68",
      "incomplete_value": false,
      "site": "00a3aa6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3aa24",
      "incomplete_value": false,
      "site": "00a3aa28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
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
      "00a3aa6c",
      "DATA",
      [
        "storage",
        "00c0ca58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3aa6c",
      "DATA",
      [
        "storage",
        "00c0caa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3aa24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3aa20.md#insn-00a3aa24)
- 新版 `00a3aa68`（命令位置の公開資料なし）

~~~diff
- 00a3aa24 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 00a3aa24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3aa24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3aa24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3aa68 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 00a3aa68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3aa68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3aa68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3aa24 bytes 08612991
+ 00a3aa68 bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c96897d660a31c29c71a9db337edf8c2"></a>

### [`00a3ab04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3ab04.md) → [`00a3ab48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3ab48.md) FUN_00a3ab48

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3ab4c",
      "incomplete_value": false,
      "site": "00a3ab50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3ab08",
      "incomplete_value": false,
      "site": "00a3ab0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
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
      "00a3ab50",
      "DATA",
      [
        "storage",
        "00c0cad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3ab50",
      "DATA",
      [
        "storage",
        "00c0cb28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3ab08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3ab04.md#insn-00a3ab08)
- 新版 `00a3ab4c`（命令位置の公開資料なし）

~~~diff
- 00a3ab08 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 00a3ab08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3ab08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3ab08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3ab4c ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 00a3ab4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3ab4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3ab4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3ab08 bytes 08612b91
+ 00a3ab4c bytes 08a12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-320ff191dca92aa7bba44895a14f7bb2"></a>

### [`00a3ab98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3ab98.md) → [`00a3abdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3abdc.md) FUN_00a3abdc

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-dec22fa0373ab09cfcdff7e64b626a74"></a>

### [`00a3abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3abfc.md) → [`00a3ac40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3ac40.md) FUN_00a3ac40

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3ac44",
      "incomplete_value": false,
      "site": "00a3ac48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3ac00",
      "incomplete_value": false,
      "site": "00a3ac04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "00a3ac48",
      "DATA",
      [
        "storage",
        "00c0cb68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3ac48",
      "DATA",
      [
        "storage",
        "00c0cbb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3ac00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3abfc.md#insn-00a3ac00)
- 新版 `00a3ac44`（命令位置の公開資料なし）

~~~diff
- 00a3ac00 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 00a3ac00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3ac00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3ac00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3ac44 ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 00a3ac44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3ac44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3ac44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3ac00 bytes 08a12d91
+ 00a3ac44 bytes 08e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-095709cafcd2a278681c70c43ddc31b2"></a>

### [`00a3ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3ac1c.md) → [`00a3ac60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3ac60.md) FUN_00a3ac60

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0045a2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a2e4.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0045a2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a2e4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.16% / 新版 88.16%

CFGの説明率　旧版 42.86% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3ac1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3ac1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3ac20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a3ac1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a3ac20",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a3ac24",
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
      "00a3ac60",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a3ac64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a3ac68",
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

- 旧版 [`00a3ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3ac1c.md#insn-00a3ac1c) · [`00a3ac20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3ac1c.md#insn-00a3ac20) · [`00a3ac24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3ac1c.md#insn-00a3ac24)

~~~diff
- 00a3ac1c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a3ac1c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a3ac1c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00a3ac1c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a3ac1c bytes fd7bbda9
- 00a3ac20 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a3ac20 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a3ac20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a3ac20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a3ac20 bytes f65701a9
- 00a3ac24 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a3ac24 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a3ac24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a3ac24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a3ac24 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0fc2c8ac70214e85e6184bef5be94fd"></a>

### [`00a3ad4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3ad4c.md) → [`00a3ad90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3ad90.md) FUN_00a3ad90

採用 · 移動量 `+0x44` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-b0cb105d9f207063b6b39a39bc7fcd0b"></a>

### [`00a3adb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3adb0.md) → [`00a3adf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3adf4.md) FUN_00a3adf4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3adf8",
      "incomplete_value": false,
      "site": "00a3adfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3adb4",
      "incomplete_value": false,
      "site": "00a3adb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "00a3adfc",
      "DATA",
      [
        "storage",
        "00c0cbe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3adfc",
      "DATA",
      [
        "storage",
        "00c0cc38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3adb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3adb0.md#insn-00a3adb4)
- 新版 `00a3adf8`（命令位置の公開資料なし）

~~~diff
- 00a3adb4 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 00a3adb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3adb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3adb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3adf8 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00a3adf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3adf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3adf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3adb4 bytes 08a12f91
+ 00a3adf8 bytes 08e13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c358a6b8c955fabe669e4d71c3577f9b"></a>

### [`00a3add0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3add0.md) → [`00a3ae14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3ae14.md) FUN_00a3ae14

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0045a2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a2e4.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0045a2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a2e4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.21% / 新版 92.21%

CFGの説明率　旧版 21.43% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3add0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3add0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3add4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a3add0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a3add4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a3add8",
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
      "00a3ae14",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a3ae18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a3ae1c",
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

- 旧版 [`00a3add0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3add0.md#insn-00a3add0) · [`00a3add4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3add0.md#insn-00a3add4) · [`00a3add8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3add0.md#insn-00a3add8)

~~~diff
- 00a3add0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a3add0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a3add0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00a3add0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a3add0 bytes fd7bbda9
- 00a3add4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a3add4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a3add4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a3add4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a3add4 bytes f65701a9
- 00a3add8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a3add8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a3add8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a3add8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a3add8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0343f46dada4b60fd9cfeab7cf90463a"></a>

### [`00a3af30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3af30.md) → [`00a3af74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3af74.md) FUN_00a3af74

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3af94",
      "incomplete_value": false,
      "site": "00a3af98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3af50",
      "incomplete_value": false,
      "site": "00a3af54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "00a3af98",
      "DATA",
      [
        "storage",
        "00c0cc68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3af98",
      "DATA",
      [
        "storage",
        "00c0ccb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3af44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3af30.md#insn-00a3af44) · [`00a3af50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3af30.md#insn-00a3af50)
- 新版 `00a3af88`（命令位置の公開資料なし） · `00a3af94`（命令位置の公開資料なし）

~~~diff
- 00a3af44 ["INT_ADD", "register:40f0:8", ["const:a3af44:8", "const:4:8"]]
- 00a3af44 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a3af88 ["INT_ADD", "register:40f0:8", ["const:a3af88:8", "const:4:8"]]
+ 00a3af88 ["CALL", null, ["callee:00bdb040:8"]]
- 00a3af44 bytes 2b800694
+ 00a3af88 bytes 2e800694
- 00a3af50 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 00a3af50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3af50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3af50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3af94 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 00a3af94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3af94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3af94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3af50 bytes 08a13191
+ 00a3af94 bytes 08e13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbb17cd51139cd90b93d9e011a577df0"></a>

### [`00a3af68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3af68.md) → [`00a3afac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3a/00a3afac.md) FUN_00a3afac

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3afb0",
      "incomplete_value": false,
      "site": "00a3afb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3af6c",
      "incomplete_value": false,
      "site": "00a3af70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "00a3afb4",
      "DATA",
      [
        "storage",
        "00c0cc68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3afb4",
      "DATA",
      [
        "storage",
        "00c0ccb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3af6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3af68.md#insn-00a3af6c)
- 新版 `00a3afb0`（命令位置の公開資料なし）

~~~diff
- 00a3af6c ["COPY", "tmp:0:8", ["const:c68:8"]]
- 00a3af6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3af6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3af6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3afb0 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 00a3afb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3afb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3afb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3af6c bytes 08a13191
+ 00a3afb0 bytes 08e13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d59e2e886cc7705c4065eb4ce517ac43"></a>

### [`00a3b0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b0b8.md) → [`00a3b0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b0fc.md) FUN_00a3b0fc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a3b120",
      "incomplete_value": false,
      "site": "00a3b120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3b0dc",
      "incomplete_value": false,
      "site": "00a3b0dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "00a3b120",
      "DATA",
      [
        "storage",
        "00c0cce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3b120",
      "DATA",
      [
        "storage",
        "00c0cd38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3b0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b0b8.md#insn-00a3b0cc) · [`00a3b0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b0b8.md#insn-00a3b0d8)
- 新版 `00a3b110`（命令位置の公開資料なし） · `00a3b11c`（命令位置の公開資料なし）

~~~diff
- 00a3b0cc ["INT_ADD", "register:40f0:8", ["const:a3b0cc:8", "const:4:8"]]
- 00a3b0cc ["CALL", null, ["callee:00bdb040:8"]]
+ 00a3b110 ["INT_ADD", "register:40f0:8", ["const:a3b110:8", "const:4:8"]]
+ 00a3b110 ["CALL", null, ["callee:00bdb040:8"]]
- 00a3b0cc bytes c97f0694
+ 00a3b110 bytes cc7f0694
- 00a3b0d8 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 00a3b0d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3b0d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3b0d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3b11c ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00a3b11c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3b11c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3b11c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3b0d8 bytes 08a13391
+ 00a3b11c bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-383033c26c45c0f4d30b43823b2eaeb7"></a>

### [`00a3b0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b0ec.md) → [`00a3b130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b130.md) FUN_00a3b130

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3b13c",
      "incomplete_value": false,
      "site": "00a3b13c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3b0f8",
      "incomplete_value": false,
      "site": "00a3b0f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "00a3b13c",
      "DATA",
      [
        "storage",
        "00c0cce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3b13c",
      "DATA",
      [
        "storage",
        "00c0cd38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3b0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b0ec.md#insn-00a3b0f4)
- 新版 `00a3b138`（命令位置の公開資料なし）

~~~diff
- 00a3b0f4 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 00a3b0f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a3b0f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a3b0f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a3b138 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00a3b138 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a3b138 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a3b138 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a3b0f4 bytes 29a13391
+ 00a3b138 bytes 29e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fe090c7ba0c49dc039ba87a7733bd21"></a>

### [`00a3b1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b1c0.md) → [`00a3b204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b204.md) FUN_00a3b204

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a3b228",
      "incomplete_value": false,
      "site": "00a3b228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3b1e4",
      "incomplete_value": false,
      "site": "00a3b1e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "00a3b228",
      "DATA",
      [
        "storage",
        "00c0cd78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3b228",
      "DATA",
      [
        "storage",
        "00c0cdc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3b1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b1c0.md#insn-00a3b1d4) · [`00a3b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b1c0.md#insn-00a3b1e0)
- 新版 `00a3b218`（命令位置の公開資料なし） · `00a3b224`（命令位置の公開資料なし）

~~~diff
- 00a3b1d4 ["INT_ADD", "register:40f0:8", ["const:a3b1d4:8", "const:4:8"]]
- 00a3b1d4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a3b218 ["INT_ADD", "register:40f0:8", ["const:a3b218:8", "const:4:8"]]
+ 00a3b218 ["CALL", null, ["callee:00bdb040:8"]]
- 00a3b1d4 bytes 877f0694
+ 00a3b218 bytes 8a7f0694
- 00a3b1e0 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00a3b1e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3b1e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3b1e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3b224 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00a3b224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3b224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3b224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3b1e0 bytes 08e13591
+ 00a3b224 bytes 08213791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6e2ab8b57c2d7e65ef2c9d88a16fe89"></a>

### [`00a3b1f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b1f4.md) → [`00a3b238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b238.md) FUN_00a3b238

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3b244",
      "incomplete_value": false,
      "site": "00a3b244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3b200",
      "incomplete_value": false,
      "site": "00a3b200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "00a3b244",
      "DATA",
      [
        "storage",
        "00c0cd78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3b244",
      "DATA",
      [
        "storage",
        "00c0cdc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3b1fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b1f4.md#insn-00a3b1fc)
- 新版 `00a3b240`（命令位置の公開資料なし）

~~~diff
- 00a3b1fc ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00a3b1fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a3b1fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a3b1fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a3b240 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00a3b240 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a3b240 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a3b240 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a3b1fc bytes 29e13591
+ 00a3b240 bytes 29213791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-066a6a0f3f321df38bfaa6fef7f15bd5"></a>

### [`00a3b31c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b31c.md) → [`00a3b360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b360.md) FUN_00a3b360

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3b380",
      "incomplete_value": false,
      "site": "00a3b384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3b33c",
      "incomplete_value": false,
      "site": "00a3b340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "00a3b384",
      "DATA",
      [
        "storage",
        "00c0cdf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3b384",
      "DATA",
      [
        "storage",
        "00c0ce48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3b330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b31c.md#insn-00a3b330) · [`00a3b33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b31c.md#insn-00a3b33c)
- 新版 `00a3b374`（命令位置の公開資料なし） · `00a3b380`（命令位置の公開資料なし）

~~~diff
- 00a3b330 ["INT_ADD", "register:40f0:8", ["const:a3b330:8", "const:4:8"]]
- 00a3b330 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a3b374 ["INT_ADD", "register:40f0:8", ["const:a3b374:8", "const:4:8"]]
+ 00a3b374 ["CALL", null, ["callee:00bdb040:8"]]
- 00a3b330 bytes 307f0694
+ 00a3b374 bytes 337f0694
- 00a3b33c ["COPY", "tmp:0:8", ["const:df8:8"]]
- 00a3b33c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3b33c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3b33c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3b380 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a3b380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3b380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3b380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3b33c bytes 08e13791
+ 00a3b380 bytes 08213991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dcb495f163a9907a361b1e70b801913"></a>

### [`00a3b354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b354.md) → [`00a3b398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b398.md) FUN_00a3b398

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3b39c",
      "incomplete_value": false,
      "site": "00a3b3a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3b358",
      "incomplete_value": false,
      "site": "00a3b35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "00a3b3a0",
      "DATA",
      [
        "storage",
        "00c0cdf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3b3a0",
      "DATA",
      [
        "storage",
        "00c0ce48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3b358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b354.md#insn-00a3b358)
- 新版 `00a3b39c`（命令位置の公開資料なし）

~~~diff
- 00a3b358 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 00a3b358 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3b358 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3b358 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3b39c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a3b39c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3b39c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3b39c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3b358 bytes 08e13791
+ 00a3b39c bytes 08213991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-629a52f3799fe12df97fcf4c9e5fbe1b"></a>

### [`00a3b374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b374.md) → [`00a3b3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b3b8.md) FUN_00a3b3b8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 23件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00466290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00466/00466290.md)
- 新版 呼出元 0件  · 呼出先 23件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00466290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/00466290.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.75% / 新版 52.75%

CFGの説明率　旧版 44.89% / 新版 45.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_branch_alignment` 32件, `unresolved_call_alignment` 43件, `unresolved_store_alignment` 45件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a3b57c",
      "incomplete_value": false,
      "site": "00a3b588",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3b538",
      "incomplete_value": false,
      "site": "00a3b544",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3b5f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3b708"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a3b564",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00a3b588",
      "DATA",
      [
        "storage",
        "00be8498",
        null,
        "pointer"
      ]
    ],
    [
      "00a3b614",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00a3b564",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00a3b588",
      "DATA",
      [
        "storage",
        "00be84e8",
        null,
        "pointer"
      ]
    ],
    [
      "00a3b614",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3b5f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b374.md#insn-00a3b5f8) · [`00a3b708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b374.md#insn-00a3b708)
- 新版 `00a3b708`（命令位置の公開資料なし）

~~~diff
- 00a3b5f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:9:8"]]
- 00a3b5f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a3b5f8 bytes e093803c
- 00a3b708 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00a3b708 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:8:8"]]
- 00a3b708 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00a3b708 bytes e8230039
+ 00a3b708 ["COPY", "register:4000:8", ["register:40a8:8"]]
+ 00a3b708 bytes e00315aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fa1f26c5de8d22c4de0967114a08fa4"></a>

### [`00a3be90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3be90.md) → [`00a3bed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3bed4.md) FUN_00a3bed4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3bee8",
      "incomplete_value": false,
      "site": "00a3beec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3bea4",
      "incomplete_value": false,
      "site": "00a3bea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:e78:8"
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
      "00a3beec",
      "DATA",
      [
        "storage",
        "00c0ce78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3beec",
      "DATA",
      [
        "storage",
        "00c0cec8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3be9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3be90.md#insn-00a3be9c) · [`00a3bea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3be90.md#insn-00a3bea4)
- 新版 `00a3bee0`（命令位置の公開資料なし） · `00a3bee8`（命令位置の公開資料なし）

~~~diff
- 00a3be9c ["INT_ADD", "register:40f0:8", ["const:a3be9c:8", "const:4:8"]]
- 00a3be9c ["CALL", null, ["callee:00bdb040:8"]]
+ 00a3bee0 ["INT_ADD", "register:40f0:8", ["const:a3bee0:8", "const:4:8"]]
+ 00a3bee0 ["CALL", null, ["callee:00bdb040:8"]]
- 00a3be9c bytes 557c0694
+ 00a3bee0 bytes 587c0694
- 00a3bea4 ["COPY", "tmp:0:8", ["const:e78:8"]]
- 00a3bea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3bea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3bea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3bee8 ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00a3bee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3bee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3bee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3bea4 bytes 08e13991
+ 00a3bee8 bytes 08213b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d1c36c13f1aacfa2cd8538f0dcac42d"></a>

### [`00a3beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3beb4.md) → [`00a3bef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3bef8.md) FUN_00a3bef8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3befc",
      "incomplete_value": false,
      "site": "00a3bf00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3beb8",
      "incomplete_value": false,
      "site": "00a3bebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:e78:8"
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
      "00a3bf00",
      "DATA",
      [
        "storage",
        "00c0ce78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3bf00",
      "DATA",
      [
        "storage",
        "00c0cec8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3beb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3beb4.md#insn-00a3beb8)
- 新版 `00a3befc`（命令位置の公開資料なし）

~~~diff
- 00a3beb8 ["COPY", "tmp:0:8", ["const:e78:8"]]
- 00a3beb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3beb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3beb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3befc ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00a3befc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3befc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3befc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3beb8 bytes 08e13991
+ 00a3befc bytes 08213b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f3b6fd1524a6eb5946e0dab25b8e468"></a>

### [`00a3bf64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bf64.md) → [`00a3bfa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3bfa8.md) FUN_00a3bfa8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3bfbc",
      "incomplete_value": false,
      "site": "00a3bfc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:f48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3bf78",
      "incomplete_value": false,
      "site": "00a3bf7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "00a3bfc0",
      "DATA",
      [
        "storage",
        "00c0cef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3bfc0",
      "DATA",
      [
        "storage",
        "00c0cf48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3bf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bf64.md#insn-00a3bf70) · [`00a3bf78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bf64.md#insn-00a3bf78)
- 新版 `00a3bfb4`（命令位置の公開資料なし） · `00a3bfbc`（命令位置の公開資料なし）

~~~diff
- 00a3bf70 ["INT_ADD", "register:40f0:8", ["const:a3bf70:8", "const:4:8"]]
- 00a3bf70 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a3bfb4 ["INT_ADD", "register:40f0:8", ["const:a3bfb4:8", "const:4:8"]]
+ 00a3bfb4 ["CALL", null, ["callee:00bdb040:8"]]
- 00a3bf70 bytes 207c0694
+ 00a3bfb4 bytes 237c0694
- 00a3bf78 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 00a3bf78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3bf78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3bf78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3bfbc ["COPY", "tmp:0:8", ["const:f48:8"]]
+ 00a3bfbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3bfbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3bfbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3bf78 bytes 08e13b91
+ 00a3bfbc bytes 08213d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ad44ca37b1e559eb4b22f6c53be9caf"></a>

### [`00a3bf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bf88.md) → [`00a3bfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3bfcc.md) FUN_00a3bfcc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3bfd0",
      "incomplete_value": false,
      "site": "00a3bfd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:f48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3bf8c",
      "incomplete_value": false,
      "site": "00a3bf90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "00a3bfd4",
      "DATA",
      [
        "storage",
        "00c0cef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3bfd4",
      "DATA",
      [
        "storage",
        "00c0cf48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3bf8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3bf88.md#insn-00a3bf8c)
- 新版 `00a3bfd0`（命令位置の公開資料なし）

~~~diff
- 00a3bf8c ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 00a3bf8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3bf8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3bf8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3bfd0 ["COPY", "tmp:0:8", ["const:f48:8"]]
+ 00a3bfd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3bfd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3bfd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3bf8c bytes 08e13b91
+ 00a3bfd0 bytes 08213d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aae2df1e0849b4baea2b727505801a56"></a>

### [`00a3c108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c108.md) → [`00a3c14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c14c.md) FUN_00a3c14c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3c160",
      "incomplete_value": false,
      "site": "00a3c164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3c11c",
      "incomplete_value": false,
      "site": "00a3c120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "00a3c164",
      "DATA",
      [
        "storage",
        "00c0cf78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3c164",
      "DATA",
      [
        "storage",
        "00c0cfc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3c114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c108.md#insn-00a3c114) · [`00a3c11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c108.md#insn-00a3c11c)
- 新版 `00a3c158`（命令位置の公開資料なし） · `00a3c160`（命令位置の公開資料なし）

~~~diff
- 00a3c114 ["INT_ADD", "register:40f0:8", ["const:a3c114:8", "const:4:8"]]
- 00a3c114 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a3c158 ["INT_ADD", "register:40f0:8", ["const:a3c158:8", "const:4:8"]]
+ 00a3c158 ["CALL", null, ["callee:00bdb040:8"]]
- 00a3c114 bytes b77b0694
+ 00a3c158 bytes ba7b0694
- 00a3c11c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00a3c11c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3c11c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3c11c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3c160 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00a3c160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3c160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3c160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3c11c bytes 08e13d91
+ 00a3c160 bytes 08213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ee0a7f89b35a6fbe05ebd0fa90f9c9e"></a>

### [`00a3c12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c12c.md) → [`00a3c170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c170.md) FUN_00a3c170

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3c174",
      "incomplete_value": false,
      "site": "00a3c178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3c130",
      "incomplete_value": false,
      "site": "00a3c134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "00a3c178",
      "DATA",
      [
        "storage",
        "00c0cf78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3c178",
      "DATA",
      [
        "storage",
        "00c0cfc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3c130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c12c.md#insn-00a3c130)
- 新版 `00a3c174`（命令位置の公開資料なし）

~~~diff
- 00a3c130 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00a3c130 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3c130 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3c130 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3c174 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00a3c174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3c174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3c174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3c130 bytes 08e13d91
+ 00a3c174 bytes 08213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8377b41390834dba29e80bb5a8c76a1f"></a>

### [`00a3c1a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c1a8.md) → [`00a3c1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c1ec.md) FUN_00a3c1ec

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3c1f8",
      "incomplete_value": false,
      "site": "00a3c1f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3c1b4",
      "incomplete_value": false,
      "site": "00a3c1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0c000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
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
      "00a3c1f8",
      "DATA",
      [
        "storage",
        "00c0cff8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3c1f8",
      "DATA",
      [
        "storage",
        "00c0d048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3c1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c1a8.md#insn-00a3c1ac) · [`00a3c1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c1a8.md#insn-00a3c1b0)
- 新版 `00a3c1f0`（命令位置の公開資料なし） · `00a3c1f4`（命令位置の公開資料なし）

~~~diff
- 00a3c1ac ["COPY", "register:4048:8", ["const:c0c000:8"]]
+ 00a3c1f0 ["COPY", "register:4048:8", ["const:c0d000:8"]]
- 00a3c1ac bytes 890e0090
+ 00a3c1f0 bytes 890e00b0
- 00a3c1b0 ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 00a3c1b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a3c1b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a3c1b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a3c1f4 ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00a3c1f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a3c1f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a3c1f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a3c1b0 bytes 29e13f91
+ 00a3c1f4 bytes 29210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28b2a4336a4092f46e8c067d73b7b1b0"></a>

### [`00a3c1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c1c4.md) → [`00a3c208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c208.md) FUN_00a3c208

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 75.00% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a3c1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c1c4.md#insn-00a3c1d0) · [`00a3c1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c1c4.md#insn-00a3c1d8) · [`00a3c1e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c1c4.md#insn-00a3c1e8)
- 新版 `00a3c214`（命令位置の公開資料なし） · `00a3c21c`（命令位置の公開資料なし） · `00a3c22c`（命令位置の公開資料なし）

~~~diff
- 00a3c1d0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a3c1d0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00a3c214 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a3c214 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00a3c1d0 bytes a1000054
+ 00a3c214 bytes a1000054
- 00a3c1d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:4", "const:0:4"]]
- 00a3c1d8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00a3c21c ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:4", "const:0:4"]]
+ 00a3c21c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00a3c1d8 bytes 6a000035
+ 00a3c21c bytes 6a000035
- 00a3c1e8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a3c1e8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00a3c22c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a3c22c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00a3c1e8 bytes c1000054
+ 00a3c22c bytes c1000054
~~~


<a id="compare-ed148b79f446ec85206cc827965ca8fd"></a>

### [`00a3c230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c230.md) → [`00a3c274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3c274.md) FUN_00a3c274

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a3c298",
      "incomplete_value": false,
      "site": "00a3c298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a3c254",
      "incomplete_value": false,
      "site": "00a3c254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
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
      "00a3c298",
      "DATA",
      [
        "storage",
        "00c0d078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3c298",
      "DATA",
      [
        "storage",
        "00c0d0c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3c244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c230.md#insn-00a3c244) · [`00a3c250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3c230.md#insn-00a3c250)
- 新版 `00a3c288`（命令位置の公開資料なし） · `00a3c294`（命令位置の公開資料なし）

~~~diff
- 00a3c244 ["INT_ADD", "register:40f0:8", ["const:a3c244:8", "const:4:8"]]
- 00a3c244 ["CALL", null, ["callee:00bdb040:8"]]
+ 00a3c288 ["INT_ADD", "register:40f0:8", ["const:a3c288:8", "const:4:8"]]
+ 00a3c288 ["CALL", null, ["callee:00bdb040:8"]]
- 00a3c244 bytes 6b7b0694
+ 00a3c288 bytes 6e7b0694
- 00a3c250 ["COPY", "tmp:0:8", ["const:78:8"]]
- 00a3c250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3c250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3c250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3c294 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00a3c294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3c294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3c294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3c250 bytes 08e10191
+ 00a3c294 bytes 08210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

