# v15.7.4 → v16.0.0 · 最優先の変更候補 (60)

[一覧の目次](README.md)

<a id="compare-b2a98bbdf9d704673955f28ee6bb3bc6"></a>

### [`00af49e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af49e0.md) → [`00b54764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54764.md) _ZN8firebase4util19JCharArrayToVariantEP7_JNIEnvP11_jcharArray

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bde560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde560.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5afe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afe0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 73.33% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54830",
      "incomplete_value": true,
      "site": "00b5483c",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54834",
      "incomplete_value": false,
      "site": "00b5483c",
      "value": [
        "leaf",
        "const:1:8"
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af49e0.md#insn-00af4ab8) · [`00af4a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af49e0.md#insn-00af4a20) · [`00af4a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af49e0.md#insn-00af4a3c)
- 新版 [`00b5483c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54764.md#insn-00b5483c) · [`00b547a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54764.md#insn-00b547a4) · [`00b547c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54764.md#insn-00b547c0)

~~~diff
- 00af4ab8 ["INT_ADD", "register:40f0:8", ["const:af4ab8:8", "const:4:8"]]
- 00af4ab8 ["CALL", null, ["callee:00c5a430:8"]]
+ 00b5483c ["INT_ADD", "register:40f0:8", ["const:b5483c:8", "const:4:8"]]
+ 00b5483c ["CALL", null, ["callee:00c5a430:8"]]
- 00af4ab8 bytes caa30394
+ 00b5483c bytes fd160494
- 00af4a20 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af4a20 ["INT_ADD", "register:40f0:8", ["const:af4a20:8", "const:4:8"]]
- 00af4a20 ["CALLIND", null, ["register:0:8"]]
+ 00b547a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b547a4 ["INT_ADD", "register:40f0:8", ["const:b547a4:8", "const:4:8"]]
+ 00b547a4 ["CALLIND", null, ["register:0:8"]]
- 00af4a20 bytes 20013fd6
+ 00b547a4 bytes 20013fd6
- 00af4a3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4a3c ["INT_ADD", "register:40f0:8", ["const:af4a3c:8", "const:4:8"]]
- 00af4a3c ["CALLIND", null, ["register:0:8"]]
+ 00b547c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b547c0 ["INT_ADD", "register:40f0:8", ["const:b547c0:8", "const:4:8"]]
+ 00b547c0 ["CALLIND", null, ["register:0:8"]]
- 00af4a3c bytes 00013fd6
+ 00b547c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51671379941eb25fc7c20636a8d30205"></a>

### [`00af4b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4b60.md) → [`00b548e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b548e4.md) _ZN8firebase4util20JShortArrayToVariantEP7_JNIEnvP12_jshortArray

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5e0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5b060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b060.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.79% / 新版 95.79%

CFGの説明率　旧版 28.57% / 新版 21.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b549c8",
      "incomplete_value": true,
      "site": "00b549cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:40c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af4c44",
      "incomplete_value": true,
      "site": "00af4c48",
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
                "register:40b8:8"
              ]
            ]
          ],
          [
            "live",
            "register:40c0:8"
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
    "new": null,
    "old": {
      "definition_site": "00af4c3c",
      "incomplete_value": true,
      "site": "00af4c48",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af4ca0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af4ca0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54a24",
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

- 旧版 [`00af4c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4b60.md#insn-00af4c48) · [`00af4ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4b60.md#insn-00af4ca0)
- 新版 [`00b549cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b548e4.md#insn-00b549cc) · [`00b54a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b548e4.md#insn-00b54a24)

~~~diff
- 00af4c48 ["INT_ADD", "register:40f0:8", ["const:af4c48:8", "const:4:8"]]
- 00af4c48 ["CALL", null, ["callee:00c5a440:8"]]
+ 00b549cc ["INT_ADD", "register:40f0:8", ["const:b549cc:8", "const:4:8"]]
+ 00b549cc ["CALL", null, ["callee:00c5a440:8"]]
- 00af4c48 bytes 6aa30394
+ 00b549cc bytes 9d160494
- 00af4ca0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4ca0 ["INT_ADD", "register:40f0:8", ["const:af4ca0:8", "const:4:8"]]
- 00af4ca0 ["CALLIND", null, ["register:0:8"]]
- 00af4ca0 bytes 00013fd6
+ 00b54a24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b54a24 ["INT_ADD", "register:40f0:8", ["const:b54a24:8", "const:4:8"]]
+ 00b54a24 ["CALLIND", null, ["register:0:8"]]
+ 00b54a24 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d095901584647395e53877242b2e711c"></a>

### [`00af4e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4e58.md) → [`00b54bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54bdc.md) _ZN8firebase4util19JLongArrayToVariantEP7_JNIEnvP11_jlongArray

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde570.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5aff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aff0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 97.89% / 新版 97.89%

CFGの説明率　旧版 37.50% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54ca4",
      "incomplete_value": true,
      "site": "00b54cb0",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54ca8",
      "incomplete_value": false,
      "site": "00b54cb0",
      "value": [
        "leaf",
        "const:1:8"
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af4f98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af4f98",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54d1c",
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

- 旧版 [`00af4f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4e58.md#insn-00af4f2c) · [`00af4f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4e58.md#insn-00af4f98) · [`00af4fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4e58.md#insn-00af4fc8)
- 新版 [`00b54cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54bdc.md#insn-00b54cb0)

~~~diff
- 00af4f2c ["INT_ADD", "register:40f0:8", ["const:af4f2c:8", "const:4:8"]]
- 00af4f2c ["CALL", null, ["callee:00c5a430:8"]]
+ 00b54cb0 ["INT_ADD", "register:40f0:8", ["const:b54cb0:8", "const:4:8"]]
+ 00b54cb0 ["CALL", null, ["callee:00c5a430:8"]]
- 00af4f2c bytes ada20394
+ 00b54cb0 bytes e0150494
- 00af4f98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4f98 ["INT_ADD", "register:40f0:8", ["const:af4f98:8", "const:4:8"]]
- 00af4f98 ["CALLIND", null, ["register:0:8"]]
- 00af4f98 bytes 00013fd6
- 00af4fc8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af4fc8 ["RETURN", null, ["register:0:8"]]
- 00af4fc8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76144587e4433539c542b6d3272a5e95"></a>

### [`00af4fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4fd4.md) → [`00b54d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54d58.md) _ZN8firebase4util20JFloatArrayToVariantEP7_JNIEnvP12_jfloatArray

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5d0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5b050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b050.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 96.94% / 新版 96.94%

CFGの説明率　旧版 64.29% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5074"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b54df8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5088"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5088",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54dfc"
      ]
    ]
  ],
  "added": [
    [
      "00b54e0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54dfc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af5074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4fd4.md#insn-00af5074) · [`00af5088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4fd4.md#insn-00af5088) · [`00af5150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af4/00af4fd4.md#insn-00af5150)

~~~diff
- 00af5074 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:10:8"]]
- 00af5074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af5074 bytes e80a00f9
- 00af5088 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af5088 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00af5088 bytes 81ffff54
- 00af5150 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af5150 ["RETURN", null, ["register:0:8"]]
- 00af5150 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12d35f08835c0c1ba11cdd48a7315e66"></a>

### [`00af515c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af515c.md) → [`00b54ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54ee0.md) _ZN8firebase4util21JDoubleArrayToVariantEP7_JNIEnvP13_jdoubleArray

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde600.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5b080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b080.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 64.29% / 新版 56.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5160"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5160"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5164"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5160",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5164",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5168",
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
      "00b54ee4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b54ee8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b54eec",
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

- 旧版 [`00af5160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af515c.md#insn-00af5160) · [`00af5164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af515c.md#insn-00af5164) · [`00af5168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af515c.md#insn-00af5168)

~~~diff
- 00af5160 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00af5160 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00af5160 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af5160 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5160 bytes fc6f02a9
- 00af5164 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00af5164 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00af5164 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00af5164 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5164 bytes fa6703a9
- 00af5168 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00af5168 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00af5168 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00af5168 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5168 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08839315ac42c9377046d41076bf6891"></a>

### [`00af5428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5428.md) → [`00b551ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b551ac.md) _ZN8firebase4util15JArrayToVariantEP7_JNIEnvP7_jarray

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde480.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde530.md) [`00bde550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde550.md) [`00bde560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde560.md)
- 新版 呼出元 1件 [`00c5af00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af00.md) · 呼出先 11件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5afb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afb0.md) [`00c5afd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afd0.md) [`00c5afe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 63.84% / 新版 63.84%

CFGの説明率　旧版 20.00% / 新版 20.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af55fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af566c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af56dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5458",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55244",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00af54d0"
      ]
    ],
    [
      "00b5524c",
      "PARAM",
      [
        "storage",
        "0029531a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b551dc",
      "READ",
      [
        "storage",
        "01125568",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55244",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55254"
      ]
    ],
    [
      "00b5524c",
      "PARAM",
      [
        "storage",
        "002a4cbf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af5468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5428.md#insn-00af5468) · [`00af54cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5428.md#insn-00af54cc) · [`00af54e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5428.md#insn-00af54e4)
- 新版 [`00b551ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b551ac.md#insn-00b551ec) · [`00b55250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b551ac.md#insn-00b55250) · [`00b55268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b551ac.md#insn-00b55268)

~~~diff
- 00af5468 ["INT_ADD", "register:40f0:8", ["const:af5468:8", "const:4:8"]]
- 00af5468 ["CALL", null, ["callee:00497a08:8"]]
+ 00b551ec ["INT_ADD", "register:40f0:8", ["const:b551ec:8", "const:4:8"]]
+ 00b551ec ["CALL", null, ["callee:00497a08:8"]]
- 00af5468 bytes c2fde597
+ 00b551ec bytes 070ae597
- 00af54cc ["INT_ADD", "register:40f0:8", ["const:af54cc:8", "const:4:8"]]
- 00af54cc ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b55250 ["INT_ADD", "register:40f0:8", ["const:b55250:8", "const:4:8"]]
+ 00b55250 ["CALL", null, ["callee:00c5ac00:8"]]
- 00af54cc bytes 2da30394
+ 00b55250 bytes 6c160494
- 00af54e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af54e4 ["INT_ADD", "register:40f0:8", ["const:af54e4:8", "const:4:8"]]
- 00af54e4 ["CALLIND", null, ["register:0:8"]]
+ 00b55268 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55268 ["INT_ADD", "register:40f0:8", ["const:b55268:8", "const:4:8"]]
+ 00b55268 ["CALLIND", null, ["register:0:8"]]
- 00af54e4 bytes 00013fd6
+ 00b55268 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46db20c3a9f58710b5b974fd88daf567"></a>

### [`00af58c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af58c8.md) → [`00b5564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b5564c.md) _ZN8firebase4util14JniUriToStringEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde470.md) · 呼出先 3件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md) [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md)
- 新版 呼出元 1件 [`00c5aef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aef0.md) · 呼出先 3件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 62.00% / 新版 62.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b55668",
      "incomplete_value": true,
      "site": "00b55674",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
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
    "old": null,
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5904"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af591c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b55668",
      "READ",
      [
        "storage",
        "010a0a70",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55690",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00af5930"
      ]
    ],
    [
      "unmatched:00af5984",
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
      "00b55668",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55690",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b556b4"
      ]
    ],
    [
      "00b55708",
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

- 旧版 [`00af58f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af58c8.md#insn-00af58f0) · [`00af5904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af58c8.md#insn-00af5904) · [`00af591c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af58c8.md#insn-00af591c)
- 新版 [`00b55674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b5564c.md#insn-00b55674)

~~~diff
- 00af58f0 ["INT_ADD", "register:40f0:8", ["const:af58f0:8", "const:4:8"]]
- 00af58f0 ["CALL", null, ["callee:004977f4:8"]]
+ 00b55674 ["INT_ADD", "register:40f0:8", ["const:b55674:8", "const:4:8"]]
+ 00b55674 ["CALL", null, ["callee:004977f4:8"]]
- 00af58f0 bytes 1bfce597
+ 00b55674 bytes 6008e597
- 00af5904 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af5904 ["INT_ADD", "register:40f0:8", ["const:af5904:8", "const:4:8"]]
- 00af5904 ["CALLIND", null, ["register:0:8"]]
- 00af5904 bytes 00013fd6
- 00af591c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af591c ["INT_ADD", "register:40f0:8", ["const:af591c:8", "const:4:8"]]
- 00af591c ["CALLIND", null, ["register:0:8"]]
- 00af591c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51fbb40d4f9a0c17bb1f6b13194a3540"></a>

### [`00af5990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5990.md) → [`00b55714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55714.md) _ZN8firebase4util13CharsToJniUriEP7_JNIEnvPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde430.md) · 呼出先 2件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md)
- 新版 呼出元 1件 [`00c5aeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aeb0.md) · 呼出先 2件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 31.88% / 新版 31.88%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5990"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5994"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5994"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5990",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5994",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5998",
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
      "00b55714",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b55718",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5571c",
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

- 旧版 [`00af5990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5990.md#insn-00af5990) · [`00af5994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5990.md#insn-00af5994) · [`00af5998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5990.md#insn-00af5998)

~~~diff
- 00af5990 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00af5990 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00af5990 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5990 bytes f70f1cf8
- 00af5994 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af5994 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af5994 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5994 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5994 bytes f65701a9
- 00af5998 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af5998 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af5998 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af5998 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5998 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abf850d869279bd86a22aa35b2c36e4a"></a>

### [`00af5aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5aa4.md) → [`00b55828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55828.md) _ZN8firebase4util14ParseUriStringEP7_JNIEnvPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 63.41% / 新版 63.41%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5aa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5aa8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5aa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5aa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5aac",
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
      "00b55828",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5582c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b55830",
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

- 旧版 [`00af5aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5aa4.md#insn-00af5aa4) · [`00af5aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5aa4.md#insn-00af5aa8) · [`00af5aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5aa4.md#insn-00af5aac)

~~~diff
- 00af5aa4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00af5aa4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af5aa4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5aa4 bytes f50f1df8
- 00af5aa8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af5aa8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af5aa8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5aa8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5aa8 bytes f44f01a9
- 00af5aac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af5aac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af5aac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af5aac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5aac bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f047160f864833ea8658b4c73e8f4fd"></a>

### [`00af5b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5b48.md) → [`00b558cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b558cc.md) _ZN8firebase4util10CharsToURLEP7_JNIEnvPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.73% / 新版 70.73%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5b48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5b4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5b4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5b48",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5b4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5b50",
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
      "00b558cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b558d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b558d4",
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

- 旧版 [`00af5b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5b48.md#insn-00af5b48) · [`00af5b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5b48.md#insn-00af5b4c) · [`00af5b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5b48.md#insn-00af5b50)

~~~diff
- 00af5b48 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00af5b48 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af5b48 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5b48 bytes f50f1df8
- 00af5b4c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af5b4c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af5b4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5b4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5b4c bytes f44f01a9
- 00af5b50 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af5b50 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af5b50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af5b50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5b50 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db266d613b66f669afe32c5a06d398bd"></a>

### [`00af5bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5bec.md) → [`00b55970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55970.md) _ZN8firebase4util20JniByteArrayToVectorEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde5f0.md) · 呼出先 1件 [`00bde7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7e0.md)
- 新版 呼出元 1件 [`00c5b070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b070.md) · 呼出先 1件 [`00c5b260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b260.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.70% / 新版 69.70%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5bec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5bec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5bf0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5bec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5bf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5bf4",
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
      "00b55970",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b55974",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b55978",
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

- 旧版 [`00af5bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5bec.md#insn-00af5bec) · [`00af5bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5bec.md#insn-00af5bf0) · [`00af5bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5bec.md#insn-00af5bf4)

~~~diff
- 00af5bec ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af5bec ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af5bec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af5bec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5bec bytes f657bda9
- 00af5bf0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af5bf0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af5bf0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5bf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5bf0 bytes f44f01a9
- 00af5bf4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af5bf4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af5bf4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af5bf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5bf4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c889f45a53556c7e95317d865277e5db"></a>

### [`00af5cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5cf8.md) → [`00b55a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55a7c.md) _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0c0.md) · 呼出先 6件 [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md)
- 新版 呼出元 1件 [`00c5ab40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab40.md) · 呼出先 6件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.69% / 新版 77.69%

CFGの説明率　旧版 21.62% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5cf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5cfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5cfc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5cf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5cfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5d1c",
      "PARAM",
      [
        "storage",
        "010a0ac8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b55a7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b55a80",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b55aa0",
      "PARAM",
      [
        "storage",
        "01125988",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af5cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5cf8.md#insn-00af5cf8) · [`00af5cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5cf8.md#insn-00af5cfc) · [`00af5d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5cf8.md#insn-00af5d30)
- 新版 [`00b55ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55a7c.md#insn-00b55ab4)

~~~diff
- 00af5cf8 ["COPY", "tmp:0:8", ["register:40d8:8"]]
- 00af5cf8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00af5cf8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5cf8 bytes fb0f1af8
- 00af5cfc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00af5cfc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00af5cfc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5cfc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5cfc bytes fa6701a9
- 00af5d30 ["INT_ADD", "register:40f0:8", ["const:af5d30:8", "const:4:8"]]
- 00af5d30 ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00b55ab4 ["INT_ADD", "register:40f0:8", ["const:b55ab4:8", "const:4:8"]]
+ 00b55ab4 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00af5d30 bytes bca20394
+ 00b55ab4 bytes fb150494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdf032113719560e6cd4875862f6292c"></a>

### [`00af5f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5f00.md) → [`00b55c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55c84.md) _ZN8firebase4util32JniResultCallback_nativeOnResultEP7_JNIEnvP8_jobjectS4_hhP8_jstringll

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.16% / 新版 88.16%

CFGの説明率　旧版 22.22% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5f14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5f14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5f18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5f14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5f18",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5f30",
      "PARAM",
      [
        "storage",
        "010a0ac8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b55c98",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b55c9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b55cb4",
      "PARAM",
      [
        "storage",
        "01125988",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af5f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5f00.md#insn-00af5f14) · [`00af5f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5f00.md#insn-00af5f18) · [`00af5f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5f00.md#insn-00af5f50)
- 新版 [`00b55cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55c84.md#insn-00b55cd4)

~~~diff
- 00af5f14 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af5f14 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af5f14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00af5f14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5f14 bytes f44f06a9
- 00af5f18 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af5f18 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af5f18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00af5f18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5f18 bytes fd7b07a9
- 00af5f50 ["INT_ADD", "register:40f0:8", ["const:af5f50:8", "const:4:8"]]
- 00af5f50 ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00b55cd4 ["INT_ADD", "register:40f0:8", ["const:b55cd4:8", "const:4:8"]]
+ 00b55cd4 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00af5f50 bytes 34a20394
+ 00b55cd4 bytes 73150494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d23f1d7bd0d73ca47e5ac93470cc410"></a>

### [`00af6030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6030.md) → [`00b55db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55db4.md) _ZN8firebase4util41CppThreadDispatcherContext_nativeFunctionEP7_JNIEnvP8_jobjectll

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-20b7a5db5facb53a9754609acb7e9afe"></a>

### [`00af6040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6040.md) → [`00b55dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55dc4.md) _ZN8firebase4util17JavaThreadContext6CancelEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ade0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ade0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 30.00% / 新版 30.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6040"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6044"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6044"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af6040",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6044",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6050",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ade0"
      ]
    ]
  ],
  "added": [
    [
      "00b55dc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b55dc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b55dd4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ade0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af6040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6040.md#insn-00af6040) · [`00af6044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6040.md#insn-00af6044) · [`00af6050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6040.md#insn-00af6050)

~~~diff
- 00af6040 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00af6040 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af6040 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af6040 bytes f30f1ef8
- 00af6044 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af6044 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af6044 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af6044 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af6044 bytes fd7b01a9
- 00af6050 ["INT_ADD", "register:40f0:8", ["const:af6050:8", "const:4:8"]]
- 00af6050 ["CALL", null, ["callee:00c5ade0:8"]]
- 00af6050 bytes c4a00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-376995c2c262ba09b7c0c6d57504c6fd"></a>

### [`00af60b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af60b8.md) → [`00b55e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55e3c.md) _ZN8firebase4util17JavaThreadContext24ReleaseExecuteCancelLockEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ade0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ade0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.67% / 新版 76.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af60b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af60bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af60bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af60b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af60bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af60d8",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b55e3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b55e40",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b55e5c",
      "READ",
      [
        "storage",
        "01125298",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af60b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af60b8.md#insn-00af60b8) · [`00af60bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af60b8.md#insn-00af60bc) · [`00af60e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af60b8.md#insn-00af60e0)
- 新版 [`00b55e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55e3c.md#insn-00b55e64)

~~~diff
- 00af60b8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00af60b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af60b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af60b8 bytes f30f1ef8
- 00af60bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af60bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af60bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af60bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af60bc bytes fd7b01a9
- 00af60e0 ["INT_ADD", "register:40f0:8", ["const:af60e0:8", "const:4:8"]]
- 00af60e0 ["CALL", null, ["callee:00574cac:8"]]
+ 00b55e64 ["INT_ADD", "register:40f0:8", ["const:b55e64:8", "const:4:8"]]
+ 00b55e64 ["CALL", null, ["callee:00574cac:8"]]
- 00af60e0 bytes 4d6fe997
+ 00b55e64 bytes 927be897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15b834cd3dd5b516feae0f167875bf42"></a>

### [`00af6130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6130.md) → [`00b55eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55eb4.md) _ZN8firebase4util17JavaThreadContext24AcquireExecuteCancelLockEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00bde360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c5ade0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ade0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.76% / 新版 75.76%

CFGの説明率　旧版 12.50% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6130"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6130"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6134"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af6130",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6134",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b55ed4",
      "READ",
      [
        "storage",
        "010a03e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b55eb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b55eb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b55ed4",
      "READ",
      [
        "storage",
        "011252a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af6130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6130.md#insn-00af6130) · [`00af6134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6130.md#insn-00af6134) · [`00af6158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6130.md#insn-00af6158)
- 新版 [`00b55edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55eb4.md#insn-00b55edc)

~~~diff
- 00af6130 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af6130 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af6130 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af6130 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af6130 bytes f44fbea9
- 00af6134 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af6134 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af6134 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af6134 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af6134 bytes fd7b01a9
- 00af6158 ["INT_ADD", "register:40f0:8", ["const:af6158:8", "const:4:8"]]
- 00af6158 ["CALL", null, ["callee:00497a08:8"]]
+ 00b55edc ["INT_ADD", "register:40f0:8", ["const:b55edc:8", "const:4:8"]]
+ 00b55edc ["CALL", null, ["callee:00497a08:8"]]
- 00af6158 bytes 86fae597
+ 00b55edc bytes cb06e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f596b3af2c5c1f6e79bdcced7b2695e7"></a>

### [`00af61b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af61b4.md) → [`00b55f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55f38.md) _ZN8firebase4util17JavaThreadContext9TerminateEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde500.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5af80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af80.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 7.04% / 新版 7.04%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af61b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af61b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af61b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af61b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af61b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af61bc",
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
      "00b55f38",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b55f3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b55f40",
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

- 旧版 [`00af61b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af61b4.md#insn-00af61b4) · [`00af61b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af61b4.md#insn-00af61b8) · [`00af61bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af61b4.md#insn-00af61bc)

~~~diff
- 00af61b4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00af61b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af61b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af61b4 bytes f50f1df8
- 00af61b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af61b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af61b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af61b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af61b8 bytes f44f01a9
- 00af61bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af61bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af61bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af61bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af61bc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3a962092ae6fc24e9df2ee12c732363"></a>

### [`00af62d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af62d0.md) → [`00b56054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56054.md) _ZN8firebase4util17JavaThreadContext13SetupInstanceEP7_JNIEnvPFvPvES4_S6_PS1_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bde300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5ad80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 57.14% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5607c",
      "incomplete_value": true,
      "site": "00b56088",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:278:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af62f8",
      "incomplete_value": true,
      "site": "00af6304",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56080",
      "incomplete_value": true,
      "site": "00b56088",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:288:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af62fc",
      "incomplete_value": true,
      "site": "00af6304",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af62f0",
      "incomplete_value": true,
      "site": "00af6304",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "ordinal": 0,
    "slot": 5
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af62f8",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af62fc",
      "READ",
      [
        "storage",
        "010a03c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af6318",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5607c",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56080",
      "READ",
      [
        "storage",
        "01125288",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5609c",
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

- 旧版 [`00af6304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af62d0.md#insn-00af6304) · [`00af6318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af62d0.md#insn-00af6318)
- 新版 [`00b56088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56054.md#insn-00b56088) · [`00b5609c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56054.md#insn-00b5609c)

~~~diff
- 00af6304 ["INT_ADD", "register:40f0:8", ["const:af6304:8", "const:4:8"]]
- 00af6304 ["CALL", null, ["callee:005896b4:8"]]
+ 00b56088 ["INT_ADD", "register:40f0:8", ["const:b56088:8", "const:4:8"]]
+ 00b56088 ["CALL", null, ["callee:005896b4:8"]]
- 00af6304 bytes 46c1e997
+ 00b56088 bytes 8bcde897
- 00af6318 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af6318 ["INT_ADD", "register:40f0:8", ["const:af6318:8", "const:4:8"]]
- 00af6318 ["CALLIND", null, ["register:0:8"]]
- 00af6318 bytes 00013fd6
+ 00b5609c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5609c ["INT_ADD", "register:40f0:8", ["const:b5609c:8", "const:4:8"]]
+ 00b5609c ["CALLIND", null, ["register:0:8"]]
+ 00b5609c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-456ad6dd8d6e19f65dae05b72d885f07"></a>

### [`00af6368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6368.md) → [`00b560ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b560ec.md) _ZN8firebase4util17JavaThreadContext15RunOnMainThreadEP7_JNIEnvP8_jobjectPFvPvES6_S8_PS1_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4e0.md) · 呼出先 3件 [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bde300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde300.md) [`00bde3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3c0.md)
- 新版 呼出元 1件 [`00c5af60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af60.md) · 呼出先 3件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5ad80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad80.md) [`00c5ae40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae40.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 76.56% / 新版 76.56%

CFGの説明率　旧版 54.55% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af63bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b56140"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56118",
      "incomplete_value": true,
      "site": "00b56124",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:278:8"
              ]
            ]
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
      "unmatched:00af6394",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af6398",
      "READ",
      [
        "storage",
        "010a03c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af63bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56164"
      ]
    ]
  ],
  "added": [
    [
      "00b56118",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5611c",
      "READ",
      [
        "storage",
        "01125288",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56140",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56164"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af63a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6368.md#insn-00af63a0) · [`00af63b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6368.md#insn-00af63b4) · [`00af63bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6368.md#insn-00af63bc)
- 新版 [`00b56124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b560ec.md#insn-00b56124)

~~~diff
- 00af63a0 ["INT_ADD", "register:40f0:8", ["const:af63a0:8", "const:4:8"]]
- 00af63a0 ["CALL", null, ["callee:005896b4:8"]]
+ 00b56124 ["INT_ADD", "register:40f0:8", ["const:b56124:8", "const:4:8"]]
+ 00b56124 ["CALL", null, ["callee:005896b4:8"]]
- 00af63a0 bytes 1fc1e997
+ 00b56124 bytes 64cde897
- 00af63b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af63b4 ["INT_ADD", "register:40f0:8", ["const:af63b4:8", "const:4:8"]]
- 00af63b4 ["CALLIND", null, ["register:0:8"]]
- 00af63b4 bytes 00013fd6
- 00af63bc ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00af63bc bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b49e167f058b657a76b868e6a1516828"></a>

### [`00af6468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6468.md) → [`00b561ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b561ec.md) _ZN8firebase4util17JavaThreadContext21RunOnBackgroundThreadEP7_JNIEnvPFvPvES4_S6_PS1_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4f0.md) · 呼出先 3件 [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bde300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde300.md) [`00bde3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3c0.md)
- 新版 呼出元 1件 [`00c5af70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af70.md) · 呼出先 3件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5ad80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad80.md) [`00c5ae40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae40.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.52% / 新版 64.52%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6468"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af646c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af646c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af6468",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af646c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6470",
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
      "00b561ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b561f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b561f4",
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

- 旧版 [`00af6468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6468.md#insn-00af6468) · [`00af646c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6468.md#insn-00af646c) · [`00af6470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6468.md#insn-00af6470)

~~~diff
- 00af6468 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00af6468 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af6468 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af6468 bytes f50f1df8
- 00af646c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af646c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af646c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af646c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af646c bytes f44f01a9
- 00af6470 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af6470 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af6470 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af6470 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af6470 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34e3f2c00b3440b5f38208e8db62b20a"></a>

### [`00af6568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6568.md) → [`00b562ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b562ec.md) _ZN8firebase4util9FindClassEP7_JNIEnvPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6f0.md) · 呼出先 1件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md)
- 新版 呼出元 1件 [`00c5b170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b170.md) · 呼出先 1件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.52% / 新版 50.52%

CFGの説明率　旧版 6.90% / 新版 6.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6568"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6568"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af656c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af6568",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af656c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6570",
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
      "00b562ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b562f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b562f4",
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

- 旧版 [`00af6568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6568.md#insn-00af6568) · [`00af656c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6568.md#insn-00af656c) · [`00af6570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6568.md#insn-00af6570)

~~~diff
- 00af6568 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00af6568 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00af6568 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00af6568 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af6568 bytes f85fbca9
- 00af656c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af656c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af656c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af656c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af656c bytes f65701a9
- 00af6570 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af6570 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af6570 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af6570 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af6570 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1623b668c45e66110f9ab70072ddf4c2"></a>

### [`00af66ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af66ec.md) → [`00b56470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56470.md) _ZN8firebase4util16FindClassInFilesEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4b0.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5af30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af30.md) · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.20% / 新版 69.20%

CFGの説明率　旧版 17.80% / 新版 17.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_condition` 6件, `unresolved_branch_alignment` 16件, `unresolved_call_alignment` 23件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af69d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af69d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6d38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af6720",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b564b0"
      ]
    ],
    [
      "unmatched:00af6734",
      "READ",
      [
        "storage",
        "010a0520",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af6760",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56508"
      ]
    ]
  ],
  "added": [
    [
      "00b564a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b564b0"
      ]
    ],
    [
      "00b564b8",
      "READ",
      [
        "storage",
        "011253e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b564e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56508"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af6720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af66ec.md#insn-00af6720) · [`00af6760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af66ec.md#insn-00af6760) · [`00af67b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af66ec.md#insn-00af67b0)

~~~diff
- 00af6720 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af6720 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00af6720 bytes 61000054
- 00af6760 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00af6760 bytes 20010054
- 00af67b0 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00af67b0 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aeaa2cea8c4858b36d707c558914771"></a>

### [`00af6dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6dec.md) → [`00b56b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56b70.md) _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_S6_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7f0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5b270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b270.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 16.00% / 新版 14.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6e1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6e24"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6e2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af6e2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56c9c"
      ]
    ]
  ],
  "added": [
    [
      "00b56bb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56c9c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af6e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6dec.md#insn-00af6e1c) · [`00af6e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6dec.md#insn-00af6e24) · [`00af6e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6dec.md#insn-00af6e2c)

~~~diff
- 00af6e1c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00af6e1c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00af6e1c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00af6e1c ["COPY", "register:40a8:8", ["tmp:0:8"]]
- 00af6e1c bytes 7501899a
- 00af6e24 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af6e24 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00af6e24 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00af6e24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00af6e24 bytes 5615809a
- 00af6e2c ["CBRANCH", null, ["local:b19:8", "register:102:1"]]
- 00af6e2c bytes 62070054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82137fc462c71988f59af5a291cae9cf"></a>

### [`00af6f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6f1c.md) → [`00b56ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56ca0.md) _ZN8firebase4util25GetResourceIdFromActivityEP7_JNIEnvP8_jobjectPKcNS0_12ResourceTypeE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 76.36% / 新版 76.36%

CFGの説明率　旧版 18.75% / 新版 15.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6f64"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7048"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b56ce8"
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
      "unmatched:00af6f38",
      "READ",
      [
        "storage",
        "010a0540",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af6f64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56d0c"
      ]
    ],
    [
      "00b56d10",
      "READ",
      [
        "storage",
        "010a0538",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b56cbc",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56ce8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56d0c"
      ]
    ],
    [
      "00b56d10",
      "READ",
      [
        "storage",
        "011253f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af6f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6f1c.md#insn-00af6f48) · [`00af6f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6f1c.md#insn-00af6f5c) · [`00af6f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6f1c.md#insn-00af6f64)
- 新版 [`00b56ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56ca0.md#insn-00b56ccc)

~~~diff
- 00af6f48 ["INT_ADD", "register:40f0:8", ["const:af6f48:8", "const:4:8"]]
- 00af6f48 ["CALL", null, ["callee:004977f4:8"]]
+ 00b56ccc ["INT_ADD", "register:40f0:8", ["const:b56ccc:8", "const:4:8"]]
+ 00b56ccc ["CALL", null, ["callee:004977f4:8"]]
- 00af6f48 bytes 85f6e597
+ 00b56ccc bytes ca02e597
- 00af6f5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af6f5c ["INT_ADD", "register:40f0:8", ["const:af6f5c:8", "const:4:8"]]
- 00af6f5c ["CALLIND", null, ["register:0:8"]]
- 00af6f5c bytes 00013fd6
- 00af6f64 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00af6f64 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40f06c9a283226edb47b0b7e07f15c81"></a>

### [`00af70d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af70d4.md) → [`00b56e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56e58.md) _ZN8firebase4util29GetResourceStringFromActivityEP7_JNIEnvP8_jobjecti

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.89% / 新版 68.89%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af70d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af70d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af70d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af70d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af70d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af70dc",
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
      "00b56e58",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b56e5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b56e60",
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

- 旧版 [`00af70d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af70d4.md#insn-00af70d4) · [`00af70d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af70d4.md#insn-00af70d8) · [`00af70dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af70d4.md#insn-00af70dc)

~~~diff
- 00af70d4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af70d4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af70d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af70d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af70d4 bytes f657bda9
- 00af70d8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af70d8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af70d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af70d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af70d8 bytes f44f01a9
- 00af70dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af70dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af70dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af70dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af70dc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9d3273d309f2eb56d1634f0334a08f7"></a>

### [`00af7188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7188.md) → [`00b56f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f0c.md) _ZN8firebase4util14GetPackageNameEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56f20",
      "incomplete_value": true,
      "site": "00b56f2c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:3f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af719c",
      "incomplete_value": true,
      "site": "00af71a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:538:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af71d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b56f58"
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
      "00b56f20",
      "READ",
      [
        "storage",
        "010a0538",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af71d4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b56f20",
      "READ",
      [
        "storage",
        "011253f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56f58",
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

- 旧版 [`00af71a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7188.md#insn-00af71a8) · [`00af71d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7188.md#insn-00af71d4)
- 新版 [`00b56f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f0c.md#insn-00b56f2c) · [`00b56f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f0c.md#insn-00b56f58)

~~~diff
- 00af71a8 ["INT_ADD", "register:40f0:8", ["const:af71a8:8", "const:4:8"]]
- 00af71a8 ["CALL", null, ["callee:004977f4:8"]]
+ 00b56f2c ["INT_ADD", "register:40f0:8", ["const:b56f2c:8", "const:4:8"]]
+ 00b56f2c ["CALL", null, ["callee:004977f4:8"]]
- 00af71a8 bytes edf5e597
+ 00b56f2c bytes 3202e597
- 00af71d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af71d4 ["INT_ADD", "register:40f0:8", ["const:af71d4:8", "const:4:8"]]
- 00af71d4 ["CALLIND", null, ["register:0:8"]]
- 00af71d4 bytes 00013fd6
+ 00b56f58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b56f58 ["INT_ADD", "register:40f0:8", ["const:b56f58:8", "const:4:8"]]
+ 00b56f58 ["CALLIND", null, ["register:0:8"]]
+ 00b56f58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a68d9095401b91c324844d53bf3f6b7"></a>

### [`00af7218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7218.md) → [`00b56f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f9c.md) _ZN8firebase4util27GetAndClearExceptionMessageEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0f0.md) · 呼出先 1件 [`00bde0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0d0.md)
- 新版 呼出元 1件 [`00c5ab70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab70.md) · 呼出先 1件 [`00c5ab50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 50.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7250"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af7258",
      "incomplete_value": true,
      "site": "00af7260",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b56fd4"
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
      "unmatched:00af7250",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b56fd4",
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

- 旧版 [`00af7250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7218.md#insn-00af7250) · [`00af7260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7218.md#insn-00af7260)
- 新版 [`00b56fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f9c.md#insn-00b56fe4) · [`00b56fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56f9c.md#insn-00b56fd4)

~~~diff
- 00af7250 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af7250 ["INT_ADD", "register:40f0:8", ["const:af7250:8", "const:4:8"]]
- 00af7250 ["CALLIND", null, ["register:0:8"]]
- 00af7250 bytes 00013fd6
- 00af7260 ["INT_ADD", "register:40f0:8", ["const:af7260:8", "const:4:8"]]
- 00af7260 ["CALL", null, ["callee:00c5ab50:8"]]
+ 00b56fe4 ["INT_ADD", "register:40f0:8", ["const:b56fe4:8", "const:4:8"]]
+ 00b56fe4 ["CALL", null, ["callee:00c5ab50:8"]]
- 00af7260 bytes 9c9b0394
+ 00b56fe4 bytes db0e0494
+ 00b56fd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b56fd4 ["INT_ADD", "register:40f0:8", ["const:b56fd4:8", "const:4:8"]]
+ 00b56fd4 ["CALLIND", null, ["register:0:8"]]
+ 00b56fd4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dbb7183888dd254b1f1b05fce9007bc"></a>

### [`00af729c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af729c.md) → [`00b57020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57020.md) _ZN8firebase4util23GetMessageFromExceptionEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0d0.md) · 呼出先 3件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md) [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md)
- 新版 呼出元 1件 [`00c5ab50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab50.md) · 呼出先 3件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 54.29% / 新版 54.29%

CFGの説明率　旧版 22.73% / 新版 18.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 9件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af72e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af73b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b57064"
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
      "00b5703c",
      "READ",
      [
        "storage",
        "010a0a40",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af72e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57088"
      ]
    ],
    [
      "00b57090",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5703c",
      "READ",
      [
        "storage",
        "01125900",
        null,
        "undefined8"
      ]
    ],
    [
      "00b57064",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57088"
      ]
    ],
    [
      "00b57090",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af72c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af729c.md#insn-00af72c4) · [`00af72d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af729c.md#insn-00af72d8) · [`00af72e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af729c.md#insn-00af72e0)
- 新版 [`00b57048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57020.md#insn-00b57048)

~~~diff
- 00af72c4 ["INT_ADD", "register:40f0:8", ["const:af72c4:8", "const:4:8"]]
- 00af72c4 ["CALL", null, ["callee:004977f4:8"]]
+ 00b57048 ["INT_ADD", "register:40f0:8", ["const:b57048:8", "const:4:8"]]
+ 00b57048 ["CALL", null, ["callee:004977f4:8"]]
- 00af72c4 bytes a6f5e597
+ 00b57048 bytes eb01e597
- 00af72d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af72d8 ["INT_ADD", "register:40f0:8", ["const:af72d8:8", "const:4:8"]]
- 00af72d8 ["CALLIND", null, ["register:0:8"]]
- 00af72d8 bytes 00013fd6
- 00af72e0 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00af72e0 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3dbc459a5f94ab77daa9dc442af800f"></a>

### [`00af7440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7440.md) → [`00b571c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b571c4.md) _ZN8firebase4util12LogExceptionEP7_JNIEnvNS_8LogLevelEPKcz

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde060.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md) [`00bde240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde240.md)
- 新版 呼出元 1件 [`00c5aae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aae0.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5acc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acc0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 45.09% / 新版 45.09%

CFGの説明率　旧版 9.38% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 15件, `unresolved_store_alignment` 28件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7444"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7444"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7448"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7444",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7448",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af744c",
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
      "00b571c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b571cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b571d0",
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

- 旧版 [`00af7444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7440.md#insn-00af7444) · [`00af7448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7440.md#insn-00af7448) · [`00af744c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7440.md#insn-00af744c)

~~~diff
- 00af7444 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00af7444 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00af7444 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00af7444 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af7444 bytes fc6711a9
- 00af7448 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00af7448 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00af7448 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00af7448 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af7448 bytes f85f12a9
- 00af744c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af744c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af744c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00af744c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af744c bytes f65713a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9cc7d226d8f15270dd99637a14c70d"></a>

### [`00af775c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af775c.md) → [`00b574e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b574e0.md) _ZN8firebase4util19AttachCurrentThreadEP7_JavaVMPP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-873deedafc7fc2120f1fed775830ff8c"></a>

### [`00af7780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7780.md) → [`00b57504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57504.md) _ZN8firebase4util19GetThreadsafeJNIEnvEP7_JavaVM

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde540.md) · 呼出先 4件 [`00af776c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af776c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00bde840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde840.md)
- 新版 呼出元 1件 [`00c5afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afc0.md) · 呼出先 4件 [`00b574f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b574f0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c5b2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2c0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af77a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b57528"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af77f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af77a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af77a8",
      "READ",
      [
        "storage",
        "00c1b938",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00af77a8",
      "PARAM",
      [
        "storage",
        "010a0cf8",
        "_ZN8firebase4util23pthread_key_initializedE",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b57528",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b5752c",
      "READ",
      [
        "storage",
        "00c9b338",
        null,
        "pointer"
      ]
    ],
    [
      "00b5752c",
      "PARAM",
      [
        "storage",
        "01125bb8",
        "_ZN8firebase4util23pthread_key_initializedE",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af77a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7780.md#insn-00af77a4) · [`00af77b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7780.md#insn-00af77b0) · [`00af77c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7780.md#insn-00af77c4)
- 新版 [`00b57534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57504.md#insn-00b57534) · [`00b57548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57504.md#insn-00b57548)

~~~diff
- 00af77a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00af77a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af77a4 bytes e80700f9
- 00af77b0 ["INT_ADD", "register:40f0:8", ["const:af77b0:8", "const:4:8"]]
- 00af77b0 ["CALL", null, ["callee:00c5b2c0:8"]]
+ 00b57534 ["INT_ADD", "register:40f0:8", ["const:b57534:8", "const:4:8"]]
+ 00b57534 ["CALL", null, ["callee:00c5b2c0:8"]]
- 00af77b0 bytes 249c0394
+ 00b57534 bytes 630f0494
- 00af77c4 ["INT_ADD", "register:40f0:8", ["const:af77c4:8", "const:4:8"]]
- 00af77c4 ["CALL", null, ["callee:00c57d40:8"]]
+ 00b57548 ["INT_ADD", "register:40f0:8", ["const:b57548:8", "const:4:8"]]
+ 00b57548 ["CALL", null, ["callee:00c57d40:8"]]
- 00af77c4 bytes cb8e0394
+ 00b57548 bytes fe010494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f85316f42aaa5adf71fa83845195bd25"></a>

### [`00af7810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7810.md) → [`00b57594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57594.md) _ZN8firebase4util16GetJNIEnvFromAppEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bde4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4c0.md) · 呼出先 3件 [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3d0.md) [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md)
- 新版 呼出元 1件 [`00c5af40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af40.md) · 呼出先 3件 [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 20.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af7818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7810.md#insn-00af7818) · [`00af781c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7810.md#insn-00af781c) · [`00af7820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7810.md#insn-00af7820)
- 新版 [`00b5759c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57594.md#insn-00b5759c) · [`00b575a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57594.md#insn-00b575a0) · [`00b575a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57594.md#insn-00b575a4)

~~~diff
- 00af7818 ["INT_ADD", "register:40f0:8", ["const:af7818:8", "const:4:8"]]
- 00af7818 ["CALL", null, ["callee:00c5ae50:8"]]
+ 00b5759c ["INT_ADD", "register:40f0:8", ["const:b5759c:8", "const:4:8"]]
+ 00b5759c ["CALL", null, ["callee:00c5ae50:8"]]
- 00af7818 bytes ee9a0394
+ 00b5759c bytes 2d0e0494
- 00af781c ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00af781c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b575a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b575a0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00af781c bytes 600000b5
+ 00b575a0 bytes 600000b5
- 00af7820 ["INT_ADD", "register:40f0:8", ["const:af7820:8", "const:4:8"]]
- 00af7820 ["CALL", null, ["callee:00c5ae60:8"]]
+ 00b575a4 ["INT_ADD", "register:40f0:8", ["const:b575a4:8", "const:4:8"]]
+ 00b575a4 ["CALL", null, ["callee:00c5ae60:8"]]
- 00af7820 bytes f09a0394
+ 00b575a4 bytes 2f0e0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f400967d2b4019094d7a16621ddb14a"></a>

### [`00af7838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7838.md) → [`00b575bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b575bc.md) _ZN8firebase7Variant18set_mutable_stringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde700.md) · 呼出先 3件 [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bddab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddab0.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)
- 新版 呼出元 1件 [`00c5b180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b180.md) · 呼出先 3件 [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a500.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 25.00% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af785c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af788c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7890"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af785c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7838.md#insn-00af785c) · [`00af7874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7838.md#insn-00af7874) · [`00af788c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7838.md#insn-00af788c)
- 新版 [`00b575f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b575bc.md#insn-00b575f8)

~~~diff
- 00af785c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00af785c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00af785c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00af785c ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00af785c bytes 4801899a
- 00af7874 ["INT_ADD", "register:40f0:8", ["const:af7874:8", "const:4:8"]]
- 00af7874 ["CALL", null, ["callee:00c5a430:8"]]
+ 00b575f8 ["INT_ADD", "register:40f0:8", ["const:b575f8:8", "const:4:8"]]
+ 00b575f8 ["CALL", null, ["callee:00c5a430:8"]]
- 00af7874 bytes 5b980394
+ 00b575f8 bytes 8e0b0494
- 00af788c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00af788c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00af788c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00af788c ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00af788c bytes 6801899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e16acd48b450234c4c5cbd8816f6f368"></a>

### [`00af78e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af78e0.md) → [`00b57664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57664.md) _ZNSt6__ndk16__treeINS_12__value_typeIPKcNS_4listIN8firebase4util12CallbackDataENS_9allocatorIS7_EEEEEENS_19__map_value_compareIS3_SB_NS_4le

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde790.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde790.md)
- 新版 呼出元 1件 [`00c5b210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b210.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 22.22% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af7908",
      "incomplete_value": true,
      "site": "00af790c",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af7904",
      "incomplete_value": true,
      "site": "00af790c",
      "value": [
        "LOAD",
        "8",
        [
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


#### 変更候補の命令位置

- 旧版 [`00af790c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af78e0.md#insn-00af790c) · [`00af78e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af78e0.md#insn-00af78e0) · [`00af78f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af78e0.md#insn-00af78f0)
- 新版 [`00b57690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57664.md#insn-00b57690) · [`00b57664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57664.md#insn-00b57664)

~~~diff
- 00af790c ["INT_ADD", "register:40f0:8", ["const:af790c:8", "const:4:8"]]
- 00af790c ["CALL", null, ["callee:00c5b210:8"]]
+ 00b57690 ["INT_ADD", "register:40f0:8", ["const:b57690:8", "const:4:8"]]
+ 00b57690 ["CALL", null, ["callee:00c5b210:8"]]
- 00af790c bytes a19b0394
+ 00b57690 bytes e00e0494
- 00af78e0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00af78e0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b57664 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b57664 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00af78e0 bytes 410400b4
+ 00b57664 bytes 410400b4
- 00af78f0 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00af78f0 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00af78f0 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00af78f0 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00af78f0 bytes fd830091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea3345e6e5d4f2356673165f0c633b99"></a>

### [`00af796c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af796c.md) → [`00b576f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b576f0.md) _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 46.15% / 新版 39.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7974"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7a9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7ab0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7978",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b577ac"
      ]
    ],
    [
      "unmatched:00af7a48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b577d8"
      ]
    ]
  ],
  "added": [
    [
      "00b576fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b577ac"
      ]
    ],
    [
      "00b577cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b577d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af7974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af796c.md#insn-00af7974) · [`00af7978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af796c.md#insn-00af7978) · [`00af7a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af796c.md#insn-00af7a48)

~~~diff
- 00af7974 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00af7974 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:18:8"]]
- 00af7974 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00af7974 bytes 28600039
- 00af7978 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00af7978 bytes 80050054
- 00af7a48 ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00af7a48 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00af7a48 bytes 6a0000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-409e4f8fd0899ac6eb6ad5e023cf2e20"></a>

### [`00af7bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7bb4.md) → [`00b57938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57938.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE25__emp

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde770.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde720.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md)
- 新版 呼出元 1件 [`00c5b1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1f0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5b1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1a0.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 46.15% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7c70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b579f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7c4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7c4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b579c0"
      ]
    ]
  ],
  "added": [
    [
      "00b579d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b579c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af7c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7bb4.md#insn-00af7c4c) · [`00af7c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7bb4.md#insn-00af7c64) · [`00af7c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7bb4.md#insn-00af7c70)
- 新版 [`00b579e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57938.md#insn-00b579e8)

~~~diff
- 00af7c4c ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00af7c4c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00af7c4c bytes 95ffffb5
- 00af7c64 ["INT_ADD", "register:40f0:8", ["const:af7c64:8", "const:4:8"]]
- 00af7c64 ["CALL", null, ["callee:00c5a440:8"]]
+ 00b579e8 ["INT_ADD", "register:40f0:8", ["const:b579e8:8", "const:4:8"]]
+ 00b579e8 ["CALL", null, ["callee:00c5a440:8"]]
- 00af7c64 bytes 63970394
+ 00b579e8 bytes 960a0494
- 00af7c70 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00af7c70 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00af7c70 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:38:8"]]
- 00af7c70 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:1:4"]]
- 00af7c70 bytes 1f8c03b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-372e58ecbe1421f847d109243317e60c"></a>

### [`00af7cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7cd0.md) → [`00b57a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57a54.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIRKS6_EEvOT_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7c0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md)
- 新版 呼出元 1件 [`00c5b240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b240.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 48.15% / 新版 41.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7d08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7d34"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7d78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7d08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57ba0"
      ]
    ],
    [
      "unmatched:00af7d34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57acc"
      ]
    ],
    [
      "unmatched:00af7d78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57b30"
      ]
    ]
  ],
  "added": [
    [
      "00b57a8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57ba0"
      ]
    ],
    [
      "00b57ab8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57acc"
      ]
    ],
    [
      "00b57afc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57b30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af7d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7cd0.md#insn-00af7d08) · [`00af7d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7cd0.md#insn-00af7d34) · [`00af7d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7cd0.md#insn-00af7d50)
- 新版 [`00b57ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57a54.md#insn-00b57ad4)

~~~diff
- 00af7d08 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af7d08 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00af7d08 ["CBRANCH", null, ["local:b19:8", "tmp:1:1"]]
- 00af7d08 bytes a8080054
- 00af7d34 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af7d34 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00af7d34 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 00af7d34 bytes a8000054
- 00af7d50 ["INT_ADD", "register:40f0:8", ["const:af7d50:8", "const:4:8"]]
- 00af7d50 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b57ad4 ["INT_ADD", "register:40f0:8", ["const:b57ad4:8", "const:4:8"]]
+ 00b57ad4 ["CALL", null, ["callee:00c57a90:8"]]
- 00af7d50 bytes bc8c0394
+ 00b57ad4 bytes efff0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13688a9814c759921d3b31c7b61a3eb4"></a>

### [`00af7e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7e20.md) → [`00b57ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57ba4.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIS6_EEvOT_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7d0.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5b250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b250.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.09% / 新版 84.09%

CFGの説明率　旧版 28.12% / 新版 29.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7ee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7ee8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b57c68"
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
      "unmatched:00af7e58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57d00"
      ]
    ],
    [
      "unmatched:00af7e84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57c1c"
      ]
    ],
    [
      "unmatched:00af7f00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57c60"
      ]
    ]
  ],
  "added": [
    [
      "00b57bdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57d00"
      ]
    ],
    [
      "00b57c08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57c1c"
      ]
    ],
    [
      "00b57c84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57c60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af7e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7e20.md#insn-00af7e58) · [`00af7e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7e20.md#insn-00af7e84) · [`00af7ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7e20.md#insn-00af7ea0)
- 新版 [`00b57c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57ba4.md#insn-00b57c24)

~~~diff
- 00af7e58 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af7e58 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00af7e58 ["CBRANCH", null, ["local:b24:8", "tmp:1:1"]]
- 00af7e58 bytes 28090054
- 00af7e84 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af7e84 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00af7e84 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00af7e84 bytes a8000054
- 00af7ea0 ["INT_ADD", "register:40f0:8", ["const:af7ea0:8", "const:4:8"]]
- 00af7ea0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b57c24 ["INT_ADD", "register:40f0:8", ["const:b57c24:8", "const:4:8"]]
+ 00b57c24 ["CALL", null, ["callee:00c57a90:8"]]
- 00af7ea0 bytes 688c0394
+ 00b57c24 bytes 9bff0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-684819239958353a08f45a948ea862b7"></a>

### [`00af7f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7f80.md) → [`00b57d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57d04.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE21__push_back_slow_pathIS2_EEvOT_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7a0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5b220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b220.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.79% / 新版 70.79%

CFGの説明率　旧版 31.82% / 新版 26.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8028"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b57dac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7fc0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7fc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57e64"
      ]
    ],
    [
      "unmatched:00af7fec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57d84"
      ]
    ],
    [
      "unmatched:00af7ffc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57e5c"
      ]
    ]
  ],
  "added": [
    [
      "00b57d44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57e64"
      ]
    ],
    [
      "00b57d70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57d84"
      ]
    ],
    [
      "00b57d80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57e5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af7fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7f80.md#insn-00af7fc0) · [`00af7fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7f80.md#insn-00af7fec) · [`00af7ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7f80.md#insn-00af7ff8)

~~~diff
- 00af7fc0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af7fc0 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00af7fc0 ["CBRANCH", null, ["local:b16:8", "tmp:1:1"]]
- 00af7fc0 bytes 08090054
- 00af7fec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af7fec ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00af7fec ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00af7fec bytes a8000054
- 00af7ff8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00af7ff8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00af7ff8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00af7ff8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af7ff8 bytes 1531899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de1a4c2aafd5b8a36a3592b25e864c7f"></a>

### [`00af80e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af80e4.md) → [`00b57e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57e68.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE8__appendEm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7e0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5b260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b260.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 45.00% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8124"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8134"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b57ea8"
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
      "unmatched:00af8124",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57f74"
      ]
    ],
    [
      "unmatched:00af8134",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57ef4"
      ]
    ]
  ],
  "added": [
    [
      "00b57ea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57f74"
      ]
    ],
    [
      "00b57eb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57ef4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af8124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af80e4.md#insn-00af8124) · [`00af8134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af80e4.md#insn-00af8134) · [`00af8194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af80e4.md#insn-00af8194)
- 新版 [`00b57f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57e68.md#insn-00b57f18)

~~~diff
- 00af8124 ["CBRANCH", null, ["local:b15:8", "register:100:1"]]
- 00af8124 bytes 64060054
- 00af8134 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af8134 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00af8134 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 00af8134 bytes e8010054
- 00af8194 ["INT_ADD", "register:40f0:8", ["const:af8194:8", "const:4:8"]]
- 00af8194 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b57f18 ["INT_ADD", "register:40f0:8", ["const:b57f18:8", "const:4:8"]]
+ 00b57f18 ["CALL", null, ["callee:00c57c90:8"]]
- 00af8194 bytes 2b8c0394
+ 00b57f18 bytes 5eff0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35e859f7e1ae87b92f452b1afc833596"></a>

### [`00af81f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af81f4.md) → [`00b57f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57f78.md) _ZNSt6__ndk16__treeINS_12__value_typeIPKcNS_4listIN8firebase4util12CallbackDataENS_9allocatorIS7_EEEEEENS_19__map_value_compareIS3_SB_NS_4le

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde780.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde750.md)
- 新版 呼出元 1件 [`00c5b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b200.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1d0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 42.11% / 新版 38.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8290"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8298"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b58014"
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
      "unmatched:00af8230",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57fd0"
      ]
    ],
    [
      "unmatched:00af8254",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57fe0"
      ]
    ]
  ],
  "added": [
    [
      "00b57fb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57fd0"
      ]
    ],
    [
      "00b57fd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57fe0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af8230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af81f4.md#insn-00af8230) · [`00af8254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af81f4.md#insn-00af8254) · [`00af8290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af81f4.md#insn-00af8290)

~~~diff
- 00af8230 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00af8230 bytes e0000054
- 00af8254 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af8254 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00af8254 bytes 41000054
- 00af8290 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:8:8"]]
- 00af8290 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00af8290 bytes 490500f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-885af93c2624ca9667896b96fe6f5f5e"></a>

### [`00af82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af82d4.md) → [`00b58058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58058.md) _ZNSt6__ndk113__tree_removeIPNS_16__tree_node_baseIPvEEEEvT_S5_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde750.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5b1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1d0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 85.59% / 新版 85.59%

CFGの説明率　旧版 49.17% / 新版 51.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 6件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8358"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af836c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af82dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58078"
      ]
    ],
    [
      "unmatched:00af82f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5808c"
      ]
    ],
    [
      "00b5814c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58150"
      ]
    ]
  ],
  "added": [
    [
      "00b58060",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58078"
      ]
    ],
    [
      "00b5807c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5808c"
      ]
    ],
    [
      "00b5814c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58188"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af82dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af82d4.md#insn-00af82dc) · [`00af82f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af82d4.md#insn-00af82f8) · [`00af8310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af82d4.md#insn-00af8310)

~~~diff
- 00af82dc ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00af82dc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00af82dc bytes c90000b4
- 00af82f8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00af82f8 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00af82f8 bytes 890000b5
- 00af8310 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:10:8"]]
- 00af8310 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af8310 bytes 280900f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bddba3e1c47734260cee076b1a325db"></a>

### [`00af8684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8684.md) → [`00b58408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58408.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde220.md)
- 新版 呼出元 1件 [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) · 呼出先 2件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5aca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aca0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 38.10% / 新版 38.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5845c",
      "incomplete_value": true,
      "site": "00b5846c",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b58460",
      "incomplete_value": true,
      "site": "00b5846c",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 5
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b58464",
      "incomplete_value": false,
      "site": "00b5846c",
      "value": [
        "leaf",
        "const:0:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 6
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af86e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8684.md#insn-00af86e8) · [`00af8710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8684.md#insn-00af8710) · [`00af8744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8684.md#insn-00af8744)
- 新版 [`00b5846c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58408.md#insn-00b5846c) · [`00b58494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58408.md#insn-00b58494)

~~~diff
- 00af86e8 ["INT_ADD", "register:40f0:8", ["const:af86e8:8", "const:4:8"]]
- 00af86e8 ["CALL", null, ["callee:00c5aca0:8"]]
+ 00b5846c ["INT_ADD", "register:40f0:8", ["const:b5846c:8", "const:4:8"]]
+ 00b5846c ["CALL", null, ["callee:00c5aca0:8"]]
- 00af86e8 bytes ce960394
+ 00b5846c bytes 0d0a0494
- 00af8710 ["INT_ADD", "register:40f0:8", ["const:af8710:8", "const:4:8"]]
- 00af8710 ["CALL", null, ["callee:00c57c00:8"]]
+ 00b58494 ["INT_ADD", "register:40f0:8", ["const:b58494:8", "const:4:8"]]
+ 00b58494 ["CALL", null, ["callee:00c57c00:8"]]
- 00af8710 bytes a88a0394
+ 00b58494 bytes dbfd0394
- 00af8744 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af8744 ["RETURN", null, ["register:0:8"]]
- 00af8744 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb0e53ffd9ef5e32980126416c6aef36"></a>

### [`00af8748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8748.md) → [`00b584cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b584cc.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 44.83% / 新版 52.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8770"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af87bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af87c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af8770",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b585dc"
      ]
    ],
    [
      "unmatched:00af87c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5855c"
      ]
    ]
  ],
  "added": [
    [
      "00b584f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b585dc"
      ]
    ],
    [
      "00b58548",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5855c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af8770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8748.md#insn-00af8770) · [`00af87bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8748.md#insn-00af87bc) · [`00af87c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8748.md#insn-00af87c4)

~~~diff
- 00af8770 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00af8770 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00af8770 bytes 43070054
- 00af87bc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00af87bc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af87bc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00af87bc ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00af87bc bytes 2831889a
- 00af87c4 ["CBRANCH", null, ["local:b12:8", "register:102:1"]]
- 00af87c4 bytes a2000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-547b31f5d47111d07a24a7af3236b128"></a>

### [`00af885c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af885c.md) → [`00b585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b585e0.md) Java_com_google_firebase_app_internal_cpp_Log_nativeLog

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md) [`00bde240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde240.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5acc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acc0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 14.29% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8888"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5860c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af88d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af8888",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af88c4",
      "READ",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af88c8",
      "DATA",
      [
        "storage",
        "002cfde0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5860c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b58648",
      "READ",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b5864c",
      "DATA",
      [
        "storage",
        "002e1998",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af8888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af885c.md#insn-00af8888) · [`00af8898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af885c.md#insn-00af8898) · [`00af88ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af885c.md#insn-00af88ac)
- 新版 [`00b5861c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b585e0.md#insn-00b5861c) · [`00b58630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b585e0.md#insn-00b58630)

~~~diff
- 00af8888 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00af8888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af8888 bytes e81f00f9
- 00af8898 ["INT_ADD", "register:40f0:8", ["const:af8898:8", "const:4:8"]]
- 00af8898 ["CALL", null, ["callee:00c5ab20:8"]]
+ 00b5861c ["INT_ADD", "register:40f0:8", ["const:b5861c:8", "const:4:8"]]
+ 00b5861c ["CALL", null, ["callee:00c5ab20:8"]]
- 00af8898 bytes 02960394
+ 00b5861c bytes 41090494
- 00af88ac ["INT_ADD", "register:40f0:8", ["const:af88ac:8", "const:4:8"]]
- 00af88ac ["CALL", null, ["callee:00c5ab20:8"]]
+ 00b58630 ["INT_ADD", "register:40f0:8", ["const:b58630:8", "const:4:8"]]
+ 00b58630 ["CALL", null, ["callee:00c5ab20:8"]]
- 00af88ac bytes fd950394
+ 00b58630 bytes 3c090494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5d6983ae78a229e85cc581d7af04951"></a>

### [`00af8b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8b3c.md) → [`00b588c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b588c0.md) _ZN8firebase8internal16JObjectReferenceC2EOS1_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-4d945d5244d1be9826a972227a887218"></a>

### [`00af8df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8df4.md) → [`00b58b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58b78.md) _ZN8firebase8internal16JObjectReference18FromLocalReferenceEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2f0.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5ad70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad70.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 37.50% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8e1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8e20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b58ba0"
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
      "unmatched:00af8e1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8e20",
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
      "00b58ba0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b58ba4",
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

- 旧版 [`00af8e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8df4.md#insn-00af8e1c) · [`00af8e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8df4.md#insn-00af8e20) · [`00af8e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8df4.md#insn-00af8e30)
- 新版 [`00b58bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58b78.md#insn-00b58bb4)

~~~diff
- 00af8e1c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00af8e1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00af8e1c bytes e90700f9
- 00af8e20 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00af8e20 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00af8e20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00af8e20 bytes ff0300f9
- 00af8e30 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af8e30 ["INT_ADD", "register:40f0:8", ["const:af8e30:8", "const:4:8"]]
- 00af8e30 ["CALLIND", null, ["register:0:8"]]
+ 00b58bb4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b58bb4 ["INT_ADD", "register:40f0:8", ["const:b58bb4:8", "const:4:8"]]
+ 00b58bb4 ["CALLIND", null, ["register:0:8"]]
- 00af8e30 bytes 20013fd6
+ 00b58bb4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db195c704f71bef2bc339a57df6caf82"></a>

### [`00af8e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8e94.md) → [`00b58c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58c18.md) _ZN8firebase10app_common6AddAppEPNS_3AppEPNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS_10InitResultENS3_4l

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8d0.md) · 呼出先 20件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c5b350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b350.md) · 呼出先 20件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.59% / 新版 89.59%

CFGの説明率　旧版 39.02% / 新版 37.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `return_value_candidate` 1件, `store_condition` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8eac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8eac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8ec8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af8eac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8ec8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8ee4",
      "PARAM",
      [
        "storage",
        "0029ce69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b58c30",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b58c4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b58c68",
      "PARAM",
      [
        "storage",
        "002ad0c9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af8eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8e94.md#insn-00af8eac) · [`00af8ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8e94.md#insn-00af8ec8) · [`00af8ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8e94.md#insn-00af8ee8)
- 新版 [`00b58c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58c18.md#insn-00b58c6c)

~~~diff
- 00af8eac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af8eac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af8eac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00af8eac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af8eac bytes fd7b09a9
- 00af8ec8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00af8ec8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af8ec8 bytes e81f00f9
- 00af8ee8 ["INT_ADD", "register:40f0:8", ["const:af8ee8:8", "const:4:8"]]
- 00af8ee8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b58c6c ["INT_ADD", "register:40f0:8", ["const:b58c6c:8", "const:4:8"]]
+ 00b58c6c ["CALL", null, ["callee:00c5ac00:8"]]
- 00af8ee8 bytes a6940394
+ 00b58c6c bytes e5070494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8d5d5f0fd721c275096bcfff69ff6ac"></a>

### [`00af9208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9208.md) → [`00b58f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58f8c.md) _ZN8firebase10app_common13FindAppByNameEPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde870.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c5b2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2f0.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 91.03% / 新版 91.03%

CFGの説明率　旧版 4.17% / 新版 3.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9230"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af92a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af92a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af9230",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b58fbc",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58fcc",
      "READ",
      [
        "storage",
        "010a0d18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b58fb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b58fbc",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58fcc",
      "READ",
      [
        "storage",
        "01125bd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af9230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9208.md#insn-00af9230) · [`00af9240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9208.md#insn-00af9240) · [`00af924c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9208.md#insn-00af924c)
- 新版 [`00b58fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58f8c.md#insn-00b58fc4) · [`00b58fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58f8c.md#insn-00b58fd0)

~~~diff
- 00af9230 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00af9230 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af9230 bytes e80f00f9
- 00af9240 ["INT_ADD", "register:40f0:8", ["const:af9240:8", "const:4:8"]]
- 00af9240 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b58fc4 ["INT_ADD", "register:40f0:8", ["const:b58fc4:8", "const:4:8"]]
+ 00b58fc4 ["CALL", null, ["callee:00c5a600:8"]]
- 00af9240 bytes 78920394
+ 00b58fc4 bytes 8f050494
- 00af924c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00af924c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00b58fd0 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00b58fd0 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00af924c bytes b40500b4
+ 00b58fd0 bytes b40500b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71e81a67e3f532212ab8762673b504f3"></a>

### [`00af9340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9340.md) → [`00b590c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590c4.md) _ZN8firebase10app_common16IsDefaultAppNameEPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bde8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8b0.md) · 呼出先 1件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)
- 新版 呼出元 1件 [`00c5b330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b330.md) · 呼出先 1件 [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b590d4",
      "incomplete_value": false,
      "site": "00b590d8",
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
            "const:8f2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af9350",
      "incomplete_value": false,
      "site": "00af9354",
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
            "const:f51:8"
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
      "definition_site": "00af9348",
      "incomplete_value": true,
      "site": "00af9354",
      "value": [
        "live",
        "register:4000:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b590e0",
      "incomplete_value": true,
      "site": "00b590e8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00af9350",
      "PARAM",
      [
        "storage",
        "002a4f51",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b590d4",
      "PARAM",
      [
        "storage",
        "002b58f2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af9354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9340.md#insn-00af9354) · [`00af934c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9340.md#insn-00af934c) · [`00af9350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9340.md#insn-00af9350)
- 新版 [`00b590d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590c4.md#insn-00b590d8) · [`00b590d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590c4.md#insn-00b590d0)

~~~diff
- 00af9354 ["INT_ADD", "register:40f0:8", ["const:af9354:8", "const:4:8"]]
- 00af9354 ["CALL", null, ["callee:00c5b450:8"]]
+ 00b590d8 ["INT_ADD", "register:40f0:8", ["const:b590d8:8", "const:4:8"]]
+ 00b590d8 ["CALL", null, ["callee:00c5b450:8"]]
- 00af9354 bytes 9f950394
+ 00b590d8 bytes de080494
- 00af934c ["COPY", "register:4000:8", ["const:2a4000:8"]]
+ 00b590d0 ["COPY", "register:4000:8", ["const:2b5000:8"]]
- 00af934c bytes 40bdfff0
+ 00b590d0 bytes e0baff90
- 00af9350 ["COPY", "tmp:0:8", ["const:f51:8"]]
- 00af9350 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00af9350 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00af9350 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00af9350 bytes 00443d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a635ac0bbaa097a101ec036bc7405538"></a>

### [`00af9374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9374.md) → [`00b590f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590f8.md) _ZN8firebase10app_common9GetAnyAppEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3e0.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 40.00% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9374"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9374"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9378"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af9374",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9378",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b59108",
      "READ",
      [
        "storage",
        "010a0d10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b590f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b590fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b59108",
      "READ",
      [
        "storage",
        "01125bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af9374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9374.md#insn-00af9374) · [`00af9378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9374.md#insn-00af9378) · [`00af9398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9374.md#insn-00af9398)
- 新版 [`00b5911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b590f8.md#insn-00b5911c)

~~~diff
- 00af9374 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af9374 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af9374 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af9374 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af9374 bytes f44fbea9
- 00af9378 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af9378 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af9378 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af9378 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af9378 bytes fd7b01a9
- 00af9398 ["INT_ADD", "register:40f0:8", ["const:af9398:8", "const:4:8"]]
- 00af9398 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5911c ["INT_ADD", "register:40f0:8", ["const:b5911c:8", "const:4:8"]]
+ 00b5911c ["CALL", null, ["callee:00c5a600:8"]]
- 00af9398 bytes 22920394
+ 00b5911c bytes 39050494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47a805e1c6809ccab9c1b38d1c0d5568"></a>

### [`00af93dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af93dc.md) → [`00b59160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59160.md) _ZN8firebase10app_common10GetAllAppsEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde850.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5b2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2d0.md) · 呼出先 7件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.09% / 新版 79.09%

CFGの説明率　旧版 34.62% / 新版 33.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9540"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b591cc"
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
      "00b59180",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5918c",
      "READ",
      [
        "storage",
        "010a0d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b591a4",
      "READ",
      [
        "storage",
        "010a0d18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b59180",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5918c",
      "READ",
      [
        "storage",
        "01125bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b591a4",
      "READ",
      [
        "storage",
        "01125bd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af9418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af93dc.md#insn-00af9418) · [`00af9424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af93dc.md#insn-00af9424) · [`00af9430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af93dc.md#insn-00af9430)
- 新版 [`00b5919c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59160.md#insn-00b5919c)

~~~diff
- 00af9418 ["INT_ADD", "register:40f0:8", ["const:af9418:8", "const:4:8"]]
- 00af9418 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5919c ["INT_ADD", "register:40f0:8", ["const:b5919c:8", "const:4:8"]]
+ 00b5919c ["CALL", null, ["callee:00c5a600:8"]]
- 00af9418 bytes 02920394
+ 00b5919c bytes 19050494
- 00af9424 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00af9424 ["CBRANCH", null, ["local:b34:8", "tmp:0:1"]]
- 00af9424 bytes 480a00b4
- 00af9430 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af9430 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00af9430 bytes a1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4c1239b029c53d7c14738ce484da6bd"></a>

### [`00af9594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9594.md) → [`00b59318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59318.md) _ZN8firebase10app_common9RemoveAppEPNS_3AppE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8e0.md) · 呼出先 16件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 1件 [`00c5b360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b360.md) · 呼出先 16件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 16.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 4件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 3件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af95c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af96ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9758"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af95c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b5934c",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5935c",
      "READ",
      [
        "storage",
        "010a0d18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b59344",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b5934c",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5935c",
      "READ",
      [
        "storage",
        "01125bd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af95c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9594.md#insn-00af95c0) · [`00af95d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9594.md#insn-00af95d0) · [`00af95dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9594.md#insn-00af95dc)
- 新版 [`00b59354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59318.md#insn-00b59354) · [`00b59360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59318.md#insn-00b59360)

~~~diff
- 00af95c0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00af95c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af95c0 bytes e80f00f9
- 00af95d0 ["INT_ADD", "register:40f0:8", ["const:af95d0:8", "const:4:8"]]
- 00af95d0 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b59354 ["INT_ADD", "register:40f0:8", ["const:b59354:8", "const:4:8"]]
+ 00b59354 ["CALL", null, ["callee:00c5a600:8"]]
- 00af95d0 bytes 94910394
+ 00b59354 bytes ab040494
- 00af95dc ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00af95dc ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
+ 00b59360 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00b59360 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 00af95dc bytes 550900b4
+ 00b59360 bytes 550900b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6556f1345f073469f1735dff1134e3e"></a>

### [`00af97a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af97a4.md) → [`00b59528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59528.md) _ZN8firebase10app_common14DestroyAllAppsEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.57% / 新版 84.57%

CFGの説明率　旧版 37.78% / 新版 38.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 9件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af97b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af97b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af97b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af97b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af97b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b59548",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b59538",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5953c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b59548",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af97b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af97a4.md#insn-00af97b4) · [`00af97b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af97a4.md#insn-00af97b8) · [`00af97d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af97a4.md#insn-00af97d4)
- 新版 [`00b59558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59528.md#insn-00b59558)

~~~diff
- 00af97b4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af97b4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af97b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00af97b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af97b4 bytes f44f04a9
- 00af97b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af97b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af97b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00af97b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af97b8 bytes fd7b05a9
- 00af97d4 ["INT_ADD", "register:40f0:8", ["const:af97d4:8", "const:4:8"]]
- 00af97d4 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b59558 ["INT_ADD", "register:40f0:8", ["const:b59558:8", "const:4:8"]]
+ 00b59558 ["CALL", null, ["callee:00c5a600:8"]]
- 00af97d4 bytes 13910394
+ 00b59558 bytes 2a040494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0075eb1ddff12499d30944310340af99"></a>

### [`00af9a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9a60.md) → [`00b597e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b597e4.md) _ZN8firebase10app_common15RegisterLibraryEPKcS2_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8a0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde880.md) [`00bde890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde890.md)
- 新版 呼出元 1件 [`00c5b320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b320.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5b300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b300.md) [`00c5b310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b310.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 8件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9a60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9a64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9a64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af9a60",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9a64",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9a68",
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
      "00b597e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b597e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b597ec",
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

- 旧版 [`00af9a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9a60.md#insn-00af9a60) · [`00af9a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9a60.md#insn-00af9a64) · [`00af9a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9a60.md#insn-00af9a68)

~~~diff
- 00af9a60 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00af9a60 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00af9a60 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af9a60 bytes f70f1cf8
- 00af9a64 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af9a64 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af9a64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af9a64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af9a64 bytes f65701a9
- 00af9a68 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af9a68 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af9a68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af9a68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af9a68 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29f2da410da0b657990edd2d463f8eed"></a>

### [`00af9af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9af8.md) → [`00b5987c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b5987c.md) _ZN8firebase10app_common15LibraryRegistry15RegisterLibraryEPKcS3_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde880.md) · 呼出先 12件 [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00470ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470ef0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5b300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b300.md) · 呼出先 12件 [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00493d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.57% / 新版 92.57%

CFGの説明率　旧版 41.28% / 新版 44.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 5件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9c48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b599cc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9b50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af9b50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b598f0"
      ]
    ],
    [
      "unmatched:00af9c48",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9cf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b59abc"
      ]
    ]
  ],
  "added": [
    [
      "00b598d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b598f0"
      ]
    ],
    [
      "00b599cc",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "00b59a74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b59abc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af9b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9af8.md#insn-00af9b50) · [`00af9b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9af8.md#insn-00af9b98) · [`00af9be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9af8.md#insn-00af9be8)
- 新版 [`00b5991c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b5987c.md#insn-00b5991c) · [`00b5996c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b5987c.md#insn-00b5996c)

~~~diff
- 00af9b50 ["CBRANCH", null, ["local:b6:8", "register:102:1"]]
- 00af9b50 bytes e2000054
- 00af9b98 ["INT_ADD", "register:40f0:8", ["const:af9b98:8", "const:4:8"]]
- 00af9b98 ["CALL", null, ["callee:00c57c00:8"]]
+ 00b5991c ["INT_ADD", "register:40f0:8", ["const:b5991c:8", "const:4:8"]]
+ 00b5991c ["CALL", null, ["callee:00c57c00:8"]]
- 00af9b98 bytes 86850394
+ 00b5991c bytes b9f80394
- 00af9be8 ["INT_ADD", "register:40f0:8", ["const:af9be8:8", "const:4:8"]]
- 00af9be8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b5996c ["INT_ADD", "register:40f0:8", ["const:b5996c:8", "const:4:8"]]
+ 00b5996c ["CALL", null, ["callee:00c57a90:8"]]
- 00af9be8 bytes 16850394
+ 00b5996c bytes 49f80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d9adba35a36e1bb5317ee0b9a0b86a1"></a>

### [`00af9f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9f2c.md) → [`00b59cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59cb0.md) _ZN8firebase10app_common15LibraryRegistry15UpdateUserAgentEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde890.md) · 呼出先 5件 [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bde970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde970.md)
- 新版 呼出元 1件 [`00c5b310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b310.md) · 呼出先 5件 [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c5b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 29.85% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9f40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af9f3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9f40",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9f58",
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
      "00b59cc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b59cc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b59cdc",
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

- 旧版 [`00af9f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9f2c.md#insn-00af9f3c) · [`00af9f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9f2c.md#insn-00af9f40) · [`00af9f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9f2c.md#insn-00af9f58)

~~~diff
- 00af9f3c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af9f3c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af9f3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00af9f3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af9f3c bytes f44f09a9
- 00af9f40 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af9f40 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af9f40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00af9f40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af9f40 bytes fd7b0aa9
- 00af9f58 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00af9f58 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00af9f58 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00af9f58 bytes a8831bf8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b965a5d048077ffcf5cbef70afb6943"></a>

### [`00afa18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa18c.md) → [`00b59f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59f10.md) _ZN8firebase10app_common30RegisterLibrariesFromUserAgentEPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.58% / 新版 75.58%

CFGの説明率　旧版 43.75% / 新版 46.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 15件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa190"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa194"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa190",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa194",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa198",
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
      "00b59f14",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b59f18",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b59f1c",
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

- 旧版 [`00afa190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa18c.md#insn-00afa190) · [`00afa194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa18c.md#insn-00afa194) · [`00afa198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa18c.md#insn-00afa198)

~~~diff
- 00afa190 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00afa190 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00afa190 bytes f91300f9
- 00afa194 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00afa194 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00afa194 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00afa194 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa194 bytes f85f03a9
- 00afa198 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00afa198 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afa198 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00afa198 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa198 bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9705ea5bb47f56f93b5ba3f071f0c40"></a>

### [`00afa2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa2e4.md) → [`00b5a068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a068.md) _ZN8firebase10app_common16RegisterSdkUsageEPv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8c0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde930.md)
- 新版 呼出元 1件 [`00c5b340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b340.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5b3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3b0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 54.41% / 新版 54.41%

CFGの説明率　旧版 7.69% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa2e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa2e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa2e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa2e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa2e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa2ec",
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
      "00b5a068",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5a06c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5a070",
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

- 旧版 [`00afa2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa2e4.md#insn-00afa2e4) · [`00afa2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa2e4.md#insn-00afa2e8) · [`00afa2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa2e4.md#insn-00afa2ec)

~~~diff
- 00afa2e4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00afa2e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afa2e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afa2e4 bytes f50f1df8
- 00afa2e8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afa2e8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afa2e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afa2e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa2e8 bytes f44f01a9
- 00afa2ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afa2ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afa2ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afa2ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa2ec bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-835547f51c89ab130e1e75a38ba14912"></a>

### [`00afa3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa3f4.md) → [`00b5a178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a178.md) _ZN8firebase10app_common12GetUserAgentEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde860.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5b2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2e0.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 20.00% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa43c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5a1c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5a1a0",
      "incomplete_value": true,
      "site": "00b5a1a0",
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
      "definition_site": "00afa41c",
      "incomplete_value": true,
      "site": "00afa41c",
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
      "00b5a188",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5a198",
      "READ",
      [
        "storage",
        "00c1b950",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a19c",
      "READ",
      [
        "storage",
        "010a0d08",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5a188",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5a198",
      "READ",
      [
        "storage",
        "00c9b350",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a19c",
      "READ",
      [
        "storage",
        "01125bc8",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afa40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa3f4.md#insn-00afa40c) · [`00afa41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa3f4.md#insn-00afa41c) · [`00afa43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa3f4.md#insn-00afa43c)
- 新版 [`00b5a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a178.md#insn-00b5a190) · [`00b5a1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a178.md#insn-00b5a1a0)

~~~diff
- 00afa40c ["INT_ADD", "register:40f0:8", ["const:afa40c:8", "const:4:8"]]
- 00afa40c ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5a190 ["INT_ADD", "register:40f0:8", ["const:b5a190:8", "const:4:8"]]
+ 00b5a190 ["CALL", null, ["callee:00c5a600:8"]]
- 00afa40c bytes 058e0394
+ 00b5a190 bytes 1c010494
- 00afa41c ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00afa41c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b5a1a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b5a1a0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00afa41c bytes 400100b5
+ 00b5a1a0 bytes 400100b5
- 00afa43c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00afa43c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00afa43c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7303ea85e9478b67d72183088c875827"></a>

### [`00afa474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa474.md) → [`00b5a1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a1f8.md) _ZN8firebase10app_common17GetLibraryVersionEPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00470ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470ef0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00493d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 94.51% / 新版 94.51%

CFGの説明率　旧版 13.79% / 新版 14.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa4a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5a224"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5a244",
      "incomplete_value": true,
      "site": "00b5a244",
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
      "definition_site": "00afa4c0",
      "incomplete_value": true,
      "site": "00afa4c0",
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
      "unmatched:00afa4a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b5a22c",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5a23c",
      "READ",
      [
        "storage",
        "00c1b950",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5a224",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b5a22c",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5a23c",
      "READ",
      [
        "storage",
        "00c9b350",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afa4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa474.md#insn-00afa4a0) · [`00afa4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa474.md#insn-00afa4b0) · [`00afa4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa474.md#insn-00afa4c8)
- 新版 [`00b5a234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a1f8.md#insn-00b5a234) · [`00b5a24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a1f8.md#insn-00b5a24c)

~~~diff
- 00afa4a0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00afa4a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00afa4a0 bytes e90f00f9
- 00afa4b0 ["INT_ADD", "register:40f0:8", ["const:afa4b0:8", "const:4:8"]]
- 00afa4b0 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5a234 ["INT_ADD", "register:40f0:8", ["const:b5a234:8", "const:4:8"]]
+ 00b5a234 ["CALL", null, ["callee:00c5a600:8"]]
- 00afa4b0 bytes dc8d0394
+ 00b5a234 bytes f3000494
- 00afa4c8 ["INT_ADD", "register:40f0:8", ["const:afa4c8:8", "const:4:8"]]
- 00afa4c8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b5a24c ["INT_ADD", "register:40f0:8", ["const:b5a24c:8", "const:4:8"]]
+ 00b5a24c ["CALL", null, ["callee:00c57a90:8"]]
- 00afa4c8 bytes de820394
+ 00b5a24c bytes 11f60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acfc536ec5f82712829b270c0feb7d0a"></a>

### [`00afa5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa5e0.md) → [`00b5a364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a364.md) _ZN8firebase10app_common25GetOuterMostSdkAndVersionEPNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00470ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470ef0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00493d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493d88.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 17.11% / 新版 17.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 5件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 27件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa5e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa5e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa5e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa5e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa5e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa5ec",
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
      "00b5a368",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b5a36c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5a370",
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

- 旧版 [`00afa5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa5e0.md#insn-00afa5e4) · [`00afa5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa5e0.md#insn-00afa5e8) · [`00afa5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa5e0.md#insn-00afa5ec)

~~~diff
- 00afa5e4 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00afa5e4 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00afa5e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00afa5e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa5e4 bytes fc6f06a9
- 00afa5e8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00afa5e8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00afa5e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00afa5e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa5e8 bytes fa6707a9
- 00afa5ec ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00afa5ec ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00afa5ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00afa5ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa5ec bytes f85f08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-554f233c26f082ce085fb05d06c1b1a9"></a>

### [`00afa8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa8d0.md) → [`00b5a654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a654.md) _ZN8firebase10app_common19FindAppLoggerByNameEPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 25.00% / 新版 26.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa8f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa96c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa96c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa8f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa900",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5a694",
      "READ",
      [
        "storage",
        "010a0d18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5a67c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b5a684",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5a694",
      "READ",
      [
        "storage",
        "01125bd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afa8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa8d0.md#insn-00afa8f8) · [`00afa908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa8d0.md#insn-00afa908) · [`00afa914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa8d0.md#insn-00afa914)
- 新版 [`00b5a68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a654.md#insn-00b5a68c) · [`00b5a698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a654.md#insn-00b5a698)

~~~diff
- 00afa8f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00afa8f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00afa8f8 bytes e80f00f9
- 00afa908 ["INT_ADD", "register:40f0:8", ["const:afa908:8", "const:4:8"]]
- 00afa908 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5a68c ["INT_ADD", "register:40f0:8", ["const:b5a68c:8", "const:4:8"]]
+ 00b5a68c ["CALL", null, ["callee:00c5a600:8"]]
- 00afa908 bytes c68c0394
+ 00b5a68c bytes ddff0394
- 00afa914 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00afa914 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00b5a698 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00b5a698 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00afa914 bytes b40500b4
+ 00b5a698 bytes b40500b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d763f767f5a11d40a16f9a2ed9654d8e"></a>

### [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) → [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) FUN_00b5a78c

採用 · 移動量 `+0x5fd84` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 8件 [`00af9f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9f2c.md) [`00afd48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd48c.md) [`00afd550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd550.md) [`00b116c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b116c8.md) [`00b12820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12820.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 9件 [`00b59cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59cb0.md) [`00b5d210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d210.md) [`00b5d2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d2d4.md) [`00b7198c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b7198c.md) [`00b72b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b72b34.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 18.75% / 新版 17.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00afaa3c",
      "incomplete_value": true,
      "site": "00afaa44",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00afaa44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md#insn-00afaa44) · [`00afaa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md#insn-00afaa38) · [`00afaa50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md#insn-00afaa50)
- 新版 [`00b5a7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md#insn-00b5a7c8) · [`00b5a7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md#insn-00b5a7bc) · [`00b5a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md#insn-00b5a7d4)

~~~diff
- 00afaa44 ["INT_ADD", "register:40f0:8", ["const:afaa44:8", "const:4:8"]]
- 00afaa44 ["CALL", null, ["callee:00c57be0:8"]]
+ 00b5a7c8 ["INT_ADD", "register:40f0:8", ["const:b5a7c8:8", "const:4:8"]]
+ 00b5a7c8 ["CALL", null, ["callee:00c57be0:8"]]
- 00afaa44 bytes d3810394
+ 00b5a7c8 bytes 06f50394
- 00afaa38 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00afaa38 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00afaa38 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00afaa38 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b5a7bc ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b5a7bc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b5a7bc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b5a7bc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00afaa38 bytes e8000037
+ 00b5a7bc bytes e8000037
- 00afaa50 ["BRANCH", null, ["local:b3:8"]]
+ 00b5a7d4 ["BRANCH", null, ["local:b5:8"]]
- 00afaa50 bytes 06000014
+ 00b5a7d4 bytes 06000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4c00a5390f736dac3ca2bced2021a39"></a>

### [`00afaaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaaf0.md) → [`00b5a874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a874.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde970.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3f0.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.58% / 新版 89.58%

CFGの説明率　旧版 30.77% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaaf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaaf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaaf4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afaaf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afaaf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afaaf8",
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
      "00b5a874",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5a878",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5a87c",
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

- 旧版 [`00afaaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaaf0.md#insn-00afaaf0) · [`00afaaf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaaf0.md#insn-00afaaf4) · [`00afaaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaaf0.md#insn-00afaaf8)

~~~diff
- 00afaaf0 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00afaaf0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00afaaf0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afaaf0 bytes f70f1cf8
- 00afaaf4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00afaaf4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afaaf4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afaaf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afaaf4 bytes f65701a9
- 00afaaf8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afaaf8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afaaf8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afaaf8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afaaf8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdaf96174836042373b82c87f844940b"></a>

### [`00afabb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afabb0.md) → [`00b5a934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a934.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde980.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5b400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b400.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 51.52% / 新版 53.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afabb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afabb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afabb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afabb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afabb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afabb8",
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
      "00b5a934",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b5a938",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5a93c",
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

- 旧版 [`00afabb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afabb0.md#insn-00afabb0) · [`00afabb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afabb0.md#insn-00afabb4) · [`00afabb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afabb0.md#insn-00afabb8)

~~~diff
- 00afabb0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00afabb0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00afabb0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00afabb0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afabb0 bytes fc6fbaa9
- 00afabb4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00afabb4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00afabb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afabb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afabb4 bytes fa6701a9
- 00afabb8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00afabb8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00afabb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afabb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afabb8 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98ceeaa6e9dce23666f9a2e85d2924a1"></a>

### [`00afaecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaecc.md) → [`00b5ac50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ac50.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9a0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdddd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddd0.md) [`00bde2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2e0.md) [`00bde750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde750.md)
- 新版 呼出元 1件 [`00c5b420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b420.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a830.md) [`00c5ad60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad60.md) [`00c5b1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1d0.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.69% / 新版 82.69%

CFGの説明率　旧版 47.62% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaecc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaed0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaed0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afaecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afaed0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afaed4",
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
      "00b5ac50",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5ac54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5ac58",
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

- 旧版 [`00afaecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaecc.md#insn-00afaecc) · [`00afaed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaecc.md#insn-00afaed0) · [`00afaed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaecc.md#insn-00afaed4)

~~~diff
- 00afaecc ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00afaecc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afaecc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afaecc bytes f50f1df8
- 00afaed0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afaed0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afaed0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afaed0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afaed0 bytes f44f01a9
- 00afaed4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afaed4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afaed4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afaed4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afaed4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d4e996d2768411864b39180dccecd20"></a>

### [`00afaf9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaf9c.md) → [`00b5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ad20.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9b0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdddd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddd0.md) [`00bde2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2e0.md) [`00bde9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9b0.md)
- 新版 呼出元 1件 [`00c5b430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b430.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a830.md) [`00c5ad60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad60.md) [`00c5b430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b430.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5ad44",
      "incomplete_value": true,
      "site": "00b5ad48",
      "value": [
        "live",
        "register:40a0:8"
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
      "definition_site": "00b5ad40",
      "incomplete_value": true,
      "site": "00b5ad48",
      "value": [
        "LOAD",
        "8",
        [
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
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00afafd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afafd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bde2e0"
      ]
    ],
    [
      "unmatched:00afafe0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdddd0"
      ]
    ]
  ],
  "added": [
    [
      "00b5ad5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5ad60"
      ]
    ],
    [
      "00b5ad64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a830"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afafc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaf9c.md#insn-00afafc4) · [`00afafd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaf9c.md#insn-00afafd8) · [`00afafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaf9c.md#insn-00afafe0)
- 新版 [`00b5ad48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ad20.md#insn-00b5ad48)

~~~diff
- 00afafc4 ["INT_ADD", "register:40f0:8", ["const:afafc4:8", "const:4:8"]]
- 00afafc4 ["CALL", null, ["callee:00c5b430:8"]]
+ 00b5ad48 ["INT_ADD", "register:40f0:8", ["const:b5ad48:8", "const:4:8"]]
+ 00b5ad48 ["CALL", null, ["callee:00c5b430:8"]]
- 00afafc4 bytes 7b8e0394
+ 00b5ad48 bytes ba010494
- 00afafd8 ["INT_ADD", "register:40f0:8", ["const:afafd8:8", "const:4:8"]]
- 00afafd8 ["CALL", null, ["ram:bde2e0:8"]]
- 00afafd8 bytes c28c0394
- 00afafe0 ["INT_ADD", "register:40f0:8", ["const:afafe0:8", "const:4:8"]]
- 00afafe0 ["CALL", null, ["ram:bdddd0:8"]]
- 00afafe0 bytes 7c8b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ea7bcc7573d85cbec553110b1daad33"></a>

### [`00afb068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb068.md) → [`00b5adec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5adec.md) _ZNK8firebase10LoggerBase8LogDebugEPKcz

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 44.23% / 新版 44.23%

CFGの説明率　旧版 10.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb06c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb06c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb070"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb06c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb070",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb074",
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
      "00b5adf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5adf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5adf8",
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

- 旧版 [`00afb06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb068.md#insn-00afb06c) · [`00afb070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb068.md#insn-00afb070) · [`00afb074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb068.md#insn-00afb074)

~~~diff
- 00afb06c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00afb06c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afb06c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00afb06c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb06c bytes fc5712a9
- 00afb070 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afb070 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afb070 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00afb070 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb070 bytes f44f13a9
- 00afb074 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afb074 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afb074 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00afb074 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb074 bytes fd7b14a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f45632808d6b17804b056c5e89700fc7"></a>

### [`00afb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb1d0.md) → [`00b5af54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5af54.md) _ZNK8firebase10LoggerBase7LogInfoEPKcz

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.85% / 新版 53.85%

CFGの説明率　旧版 10.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb1e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb1e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb1e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb1e4",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb1e8",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb1ec",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5af68",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ],
    [
      "00b5af6c",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "00b5af70",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb1d0.md#insn-00afb1e4) · [`00afb1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb1d0.md#insn-00afb1e8) · [`00afb1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb1d0.md#insn-00afb1ec)

~~~diff
- 00afb1e4 ["COPY", "tmp:0:8", ["register:4010:8"]]
- 00afb1e4 ["COPY", "tmp:1:8", ["register:4018:8"]]
- 00afb1e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00afb1e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb1e4 bytes e20f08a9
- 00afb1e8 ["COPY", "tmp:0:8", ["register:4020:8"]]
- 00afb1e8 ["COPY", "tmp:1:8", ["register:4028:8"]]
- 00afb1e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00afb1e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb1e8 bytes e41709a9
- 00afb1ec ["COPY", "tmp:0:8", ["register:4030:8"]]
- 00afb1ec ["COPY", "tmp:1:8", ["register:4038:8"]]
- 00afb1ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00afb1ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb1ec bytes e61f0aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c6f9e9934cd74704724d700c8dd15f6"></a>

### [`00afb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb2a0.md) → [`00b5b024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b024.md) _ZNK8firebase10LoggerBase10LogWarningEPKcz

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 57.69% / 新版 57.69%

CFGの説明率　旧版 22.22% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb2bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb2bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb2c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb2bc",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb2c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x150]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb2c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x130]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5b040",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "00b5b044",
      "WRITE",
      [
        "storage",
        "Stack[-0x150]",
        null,
        null
      ]
    ],
    [
      "00b5b048",
      "WRITE",
      [
        "storage",
        "Stack[-0x130]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb2a0.md#insn-00afb2bc) · [`00afb2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb2a0.md#insn-00afb2c0) · [`00afb2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb2a0.md#insn-00afb2c4)

~~~diff
- 00afb2bc ["COPY", "tmp:0:8", ["register:4030:8"]]
- 00afb2bc ["COPY", "tmp:1:8", ["register:4038:8"]]
- 00afb2bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00afb2bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb2bc bytes e61f0aa9
- 00afb2c0 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00afb2c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00afb2c0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00afb2c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00afb2c0 bytes e00700ad
- 00afb2c4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00afb2c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 00afb2c4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00afb2c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5060:16"]]
- 00afb2c4 bytes e20f01ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3033203aec8b85d20e0af51b1569ee36"></a>

### [`00afb370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb370.md) → [`00b5b0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b0f4.md) _ZNK8firebase10LoggerBase8LogErrorEPKcz

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.85% / 新版 78.85%

CFGの説明率　旧版 28.57% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb388"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb388"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb38c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb388",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb38c",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb390",
      "WRITE",
      [
        "storage",
        "Stack[-0x150]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5b10c",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "00b5b110",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "00b5b114",
      "WRITE",
      [
        "storage",
        "Stack[-0x150]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb370.md#insn-00afb388) · [`00afb38c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb370.md#insn-00afb38c) · [`00afb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb370.md#insn-00afb390)

~~~diff
- 00afb388 ["COPY", "tmp:0:8", ["register:4020:8"]]
- 00afb388 ["COPY", "tmp:1:8", ["register:4028:8"]]
- 00afb388 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00afb388 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb388 bytes e41709a9
- 00afb38c ["COPY", "tmp:0:8", ["register:4030:8"]]
- 00afb38c ["COPY", "tmp:1:8", ["register:4038:8"]]
- 00afb38c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00afb38c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb38c bytes e61f0aa9
- 00afb390 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00afb390 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00afb390 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00afb390 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00afb390 bytes e00700ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b813f21674f55f8b07f68980b6ba48f"></a>

### [`00afb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb440.md) → [`00b5b1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b1c4.md) _ZNK8firebase10LoggerBase9LogAssertEPKcz

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 12.50% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb458"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb458"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb45c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb458",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb45c",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb460",
      "WRITE",
      [
        "storage",
        "Stack[-0x150]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5b1dc",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "00b5b1e0",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "00b5b1e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x150]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb440.md#insn-00afb458) · [`00afb45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb440.md#insn-00afb45c) · [`00afb460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb440.md#insn-00afb460)

~~~diff
- 00afb458 ["COPY", "tmp:0:8", ["register:4020:8"]]
- 00afb458 ["COPY", "tmp:1:8", ["register:4028:8"]]
- 00afb458 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00afb458 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb458 bytes e41709a9
- 00afb45c ["COPY", "tmp:0:8", ["register:4030:8"]]
- 00afb45c ["COPY", "tmp:1:8", ["register:4038:8"]]
- 00afb45c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00afb45c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb45c bytes e61f0aa9
- 00afb460 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00afb460 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00afb460 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00afb460 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00afb460 bytes e00700ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caa76ad0ddb72f844e7c2e5127543a14"></a>

### [`00afb510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb510.md) → [`00b5b294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b294.md) _ZNK8firebase10LoggerBase10LogMessageENS_8LogLevelEPKcz

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 54.55% / 新版 54.55%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb52c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb528",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb52c",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb530",
      "WRITE",
      [
        "storage",
        "Stack[-0xb8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5b2ac",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ],
    [
      "00b5b2b0",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "00b5b2b4",
      "WRITE",
      [
        "storage",
        "Stack[-0xb8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb510.md#insn-00afb528) · [`00afb52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb510.md#insn-00afb52c) · [`00afb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb510.md#insn-00afb530)

~~~diff
- 00afb528 ["COPY", "tmp:0:8", ["register:4018:8"]]
- 00afb528 ["COPY", "tmp:1:8", ["register:4020:8"]]
- 00afb528 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:88:8"]]
- 00afb528 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb528 bytes e39308a9
- 00afb52c ["COPY", "tmp:0:8", ["register:4028:8"]]
- 00afb52c ["COPY", "tmp:1:8", ["register:4030:8"]]
- 00afb52c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:98:8"]]
- 00afb52c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb52c bytes e59b09a9
- 00afb530 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:a8:8"]]
- 00afb530 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4038:8"]]
- 00afb530 bytes e75700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dc0b2c26079ffd92dbaeacab58d3b6b"></a>

### [`00afb5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb5ec.md) → [`00b5b370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b370.md) _ZNK8firebase10LoggerBase11LogMessageVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 12.50% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb61c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb61c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5b3a0"
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
      "unmatched:00afb61c",
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
      "00b5b3a0",
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

- 旧版 [`00afb61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb5ec.md#insn-00afb61c) · [`00afb654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb5ec.md#insn-00afb654) · [`00afb678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb5ec.md#insn-00afb678)
- 新版 [`00b5b3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b370.md#insn-00b5b3d8)

~~~diff
- 00afb61c ["COPY", "tmp:0:8", ["register:8:8"]]
- 00afb61c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00afb61c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00afb61c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00afb61c bytes e10300ad
- 00afb654 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afb654 ["INT_ADD", "register:40f0:8", ["const:afb654:8", "const:4:8"]]
- 00afb654 ["CALLIND", null, ["register:0:8"]]
+ 00b5b3d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5b3d8 ["INT_ADD", "register:40f0:8", ["const:b5b3d8:8", "const:4:8"]]
+ 00b5b3d8 ["CALLIND", null, ["register:0:8"]]
- 00afb654 bytes 00013fd6
+ 00b5b3d8 bytes 00013fd6
- 00afb678 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afb678 ["RETURN", null, ["register:0:8"]]
- 00afb678 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70d6f4ebefc37b9e66684e846b2da46a"></a>

### [`00afb690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb690.md) → [`00b5b414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b414.md) _ZNK8firebase12SystemLogger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

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
      "site": "00afb6b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb6c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb6c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb6b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb6c0",
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
      "00b5b438",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b5b444",
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

- 旧版 [`00afb6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb690.md#insn-00afb6b4) · [`00afb6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb690.md#insn-00afb6c0) · [`00afb6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb690.md#insn-00afb6c4)
- 新版 [`00b5b448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b414.md#insn-00b5b448)

~~~diff
- 00afb6b4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00afb6b4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00afb6b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00afb6b4 bytes a9831ef8
- 00afb6c0 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00afb6c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00afb6c0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00afb6c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00afb6c0 bytes e10300ad
- 00afb6c4 ["INT_ADD", "register:40f0:8", ["const:afb6c4:8", "const:4:8"]]
- 00afb6c4 ["CALL", null, ["callee:00c5ad20:8"]]
+ 00b5b448 ["INT_ADD", "register:40f0:8", ["const:b5b448:8", "const:4:8"]]
+ 00b5b448 ["CALL", null, ["callee:00c5ad20:8"]]
- 00afb6c4 bytes f78a0394
+ 00b5b448 bytes 36fe0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb4ab56c2f3a5eb1f92a11651e41e1f2"></a>

### [`00afb700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb700.md) → [`00b5b484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b484.md) _ZNK8firebase6Logger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 63.16% / 新版 63.16%

CFGの説明率　旧版 11.11% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb704"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb704"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb708"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb704",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb708",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb70c",
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
      "00b5b488",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5b48c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5b490",
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

- 旧版 [`00afb704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb700.md#insn-00afb704) · [`00afb708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb700.md#insn-00afb708) · [`00afb70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb700.md#insn-00afb70c)

~~~diff
- 00afb704 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00afb704 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afb704 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00afb704 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb704 bytes f65705a9
- 00afb708 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afb708 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afb708 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00afb708 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb708 bytes f44f06a9
- 00afb70c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afb70c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afb70c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00afb70c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb70c bytes fd7b07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1467d0462f47e9b071e73c720303902"></a>

### [`00afb798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb798.md) → [`00b5b51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b51c.md) _ZN8firebase8callback10InitializeEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde950.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md)
- 新版 呼出元 1件 [`00c5b3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3d0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 59.38% / 新版 59.38%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb798"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb79c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb79c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb798",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb79c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb7a0",
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
      "00b5b51c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5b520",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5b524",
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

- 旧版 [`00afb798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb798.md#insn-00afb798) · [`00afb79c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb798.md#insn-00afb79c) · [`00afb7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb798.md#insn-00afb7a0)

~~~diff
- 00afb798 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00afb798 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afb798 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afb798 bytes f50f1df8
- 00afb79c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afb79c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afb79c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afb79c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb79c bytes f44f01a9
- 00afb7a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afb7a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afb7a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afb7a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb7a0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cfb48ec3dae736b566c1fe7f1597394"></a>

### [`00afb818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb818.md) → [`00b5b59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b59c.md) _ZN8firebase8callback13IsInitializedEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5b5a0",
      "READ",
      [
        "storage",
        "010a0d28",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b5b5a0",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb818.md#insn-00afb818) · [`00afb81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb818.md#insn-00afb81c)
- 新版 [`00b5b59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b59c.md#insn-00b5b59c) · [`00b5b5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b59c.md#insn-00b5b5a0)

~~~diff
- 00afb818 ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b5b59c ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00afb818 bytes 282d00b0
+ 00b5b59c bytes 482e00d0
- 00afb81c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d28:8"]]
- 00afb81c ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00afb81c ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
+ 00b5b5a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:be8:8"]]
+ 00b5b5a0 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00b5b5a0 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 00afb81c bytes 08294db9
+ 00b5b5a0 bytes 08e94bb9
~~~


<a id="compare-bf444b691b2d2ab0b667acd3e537b50d"></a>

### [`00afb82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb82c.md) → [`00b5b5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b5b0.md) _ZN8firebase8callback9TerminateEb

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde960.md) · 呼出先 4件 [`00afb988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb988.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdec60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec60.md)
- 新版 呼出元 1件 [`00c5b3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3e0.md) · 呼出先 4件 [`00b5b70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b70c.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5b720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b720.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5b5dc",
      "incomplete_value": true,
      "site": "00b5b5dc",
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
      "definition_site": "00afb858",
      "incomplete_value": true,
      "site": "00afb858",
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
      "definition_site": "00b5b5c8",
      "incomplete_value": true,
      "site": "00b5b5cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afb844",
      "incomplete_value": true,
      "site": "00afb848",
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
      "00b5b5c0",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5b5d4",
      "READ",
      [
        "storage",
        "010a0d30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5b5c0",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5b5d4",
      "READ",
      [
        "storage",
        "01125bf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb82c.md#insn-00afb848) · [`00afb858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb82c.md#insn-00afb858) · [`00afb838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb82c.md#insn-00afb838)
- 新版 [`00b5b5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b5b0.md#insn-00b5b5cc) · [`00b5b5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b5b0.md#insn-00b5b5dc) · [`00b5b5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b5b0.md#insn-00b5b5bc)

~~~diff
- 00afb848 ["INT_ADD", "register:40f0:8", ["const:afb848:8", "const:4:8"]]
- 00afb848 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5b5cc ["INT_ADD", "register:40f0:8", ["const:b5b5cc:8", "const:4:8"]]
+ 00b5b5cc ["CALL", null, ["callee:00c5a600:8"]]
- 00afb848 bytes f6880394
+ 00b5b5cc bytes 0dfc0394
- 00afb858 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00afb858 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b5b5dc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b5b5dc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00afb858 bytes a80000b4
+ 00b5b5dc bytes a80000b4
- 00afb838 ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b5b5bc ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00afb838 bytes 282d00b0
+ 00b5b5bc bytes 482e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a725d4d5f505603bbf5ac5cc3f98d98a"></a>

### [`00afb988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb988.md) → [`00b5b70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b70c.md) FUN_00b5b70c

採用 · 移動量 `+0x5fd84` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00afb82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb82c.md) [`00afbd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbd60.md) [`00afbe8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbe8c.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md)
- 新版 呼出元 3件 [`00b5b5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b5b0.md) [`00b5bae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bae4.md) [`00b5bc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bc10.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.08% / 新版 77.08%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb9bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb9dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb9f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5b720",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5b734",
      "READ",
      [
        "storage",
        "010a0d28",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00afb9bc",
      "WRITE",
      [
        "storage",
        "010a0d28",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b5b720",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5b734",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5b740",
      "WRITE",
      [
        "storage",
        "01125be8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb988.md#insn-00afb9a8) · [`00afb9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb988.md#insn-00afb9bc) · [`00afb9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb988.md#insn-00afb9c0)
- 新版 [`00b5b72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b70c.md#insn-00b5b72c)

~~~diff
- 00afb9a8 ["INT_ADD", "register:40f0:8", ["const:afb9a8:8", "const:4:8"]]
- 00afb9a8 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5b72c ["INT_ADD", "register:40f0:8", ["const:b5b72c:8", "const:4:8"]]
+ 00b5b72c ["CALL", null, ["callee:00c5a600:8"]]
- 00afb9a8 bytes 9e880394
+ 00b5b72c bytes b5fb0394
- 00afb9bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d28:8"]]
- 00afb9bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
- 00afb9bc bytes a12a0db9
- 00afb9c0 ["BOOL_NEGATE", "tmp:0:1", ["register:100:1"]]
- 00afb9c0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00afb9c0 bytes a5000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52f84de3ab3144ab43b8c2696346bbe9"></a>

### [`00afba48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afba48.md) → [`00b5b7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b7cc.md) _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdec30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec30.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md) [`00bdec50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec50.md)
- 新版 呼出元 1件 [`00c5b6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6f0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md) [`00c5b710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b710.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.74% / 新版 71.74%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbabc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbac8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5b840"
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
      "00b5b7e4",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00afba70",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5b804",
      "READ",
      [
        "storage",
        "010a0d28",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b5b7e4",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5b7f4",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5b804",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afba6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afba48.md#insn-00afba6c) · [`00afba78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afba48.md#insn-00afba78) · [`00afbaa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afba48.md#insn-00afbaa8)
- 新版 [`00b5b7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b7cc.md#insn-00b5b7f0) · [`00b5b7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b7cc.md#insn-00b5b7fc)

~~~diff
- 00afba6c ["INT_ADD", "register:40f0:8", ["const:afba6c:8", "const:4:8"]]
- 00afba6c ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5b7f0 ["INT_ADD", "register:40f0:8", ["const:b5b7f0:8", "const:4:8"]]
+ 00b5b7f0 ["CALL", null, ["callee:00c5a600:8"]]
- 00afba6c bytes 6d880394
+ 00b5b7f0 bytes 84fb0394
- 00afba78 ["INT_ADD", "register:40f0:8", ["const:afba78:8", "const:4:8"]]
- 00afba78 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5b7fc ["INT_ADD", "register:40f0:8", ["const:b5b7fc:8", "const:4:8"]]
+ 00b5b7fc ["CALL", null, ["callee:00c5a600:8"]]
- 00afba78 bytes 6a880394
+ 00b5b7fc bytes 81fb0394
- 00afbaa8 ["INT_ADD", "register:40f0:8", ["const:afbaa8:8", "const:4:8"]]
- 00afbaa8 ["CALL", null, ["ram:bdde20:8"]]
- 00afbaa8 bytes de880394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e06fc27eca71d0b86c6563807deed3e"></a>

### [`00afbb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbb00.md) → [`00b5b884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b884.md) _ZN8firebase8callback18CallbackDispatcher11AddCallbackEPNS0_8CallbackE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdec50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec50.md) · 呼出先 5件 [`00afc348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc348.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5b710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b710.md) · 呼出先 5件 [`00b5c0cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c0cc.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 21.43% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbb44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbb48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbb78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5b8b4",
      "READ",
      [
        "storage",
        "00c1b988",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00afbb44",
      "DATA",
      [
        "storage",
        "00c107f8",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00b5b944",
      "READ",
      [
        "storage",
        "00c10808",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00b5b8b4",
      "READ",
      [
        "storage",
        "00c9b388",
        null,
        "pointer"
      ]
    ],
    [
      "00b5b8c8",
      "DATA",
      [
        "storage",
        "00c8ff18",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00b5b944",
      "READ",
      [
        "storage",
        "00c8ff28",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afbb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbb00.md#insn-00afbb44) · [`00afbb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbb00.md#insn-00afbb48) · [`00afbb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbb00.md#insn-00afbb78)

~~~diff
- 00afbb44 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00afbb44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00afbb44 bytes 080000f9
- 00afbb48 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00afbb48 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:18:8"]]
- 00afbb48 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 00afbb48 bytes 968e01f8
- 00afbb78 ["COPY", "tmp:0:1", ["const:1:1"]]
- 00afbb78 ["CALLOTHER", "tmp:1:1", ["const:3f:4", "register:40b8:8", "const:10:1"]]
- 00afbb78 ["BOOL_NEGATE", "tmp:2:1", ["tmp:1:1"]]
- 00afbb78 ["CBRANCH", null, ["const:3:4", "tmp:2:1"]]
- 00afbb78 bytes e87e09c8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-545acc795f0f4ef2062a112960898ca4"></a>

### [`00afbc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbc70.md) → [`00b5b9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b9f4.md) _ZN8firebase8callback19AddBlockingCallbackEPNS0_8CallbackE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7d0.md) [`00bdec30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec30.md) [`00bdec90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58220.md) [`00c5b6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6f0.md) [`00c5b750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b750.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 55.56% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbd00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5baa4",
      "incomplete_value": true,
      "site": "00b5baa4",
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
      "definition_site": "00afbd20",
      "incomplete_value": true,
      "site": "00afbd20",
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
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5ba84"
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
      "00b5ba1c",
      "READ",
      [
        "storage",
        "010a0d38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5ba30",
      "READ",
      [
        "storage",
        "010a0d40",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00afbd00",
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
      "00b5ba1c",
      "READ",
      [
        "storage",
        "01125bf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5ba30",
      "READ",
      [
        "storage",
        "01125c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ba84",
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

- 旧版 [`00afbce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbc70.md#insn-00afbce0) · [`00afbd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbc70.md#insn-00afbd00) · [`00afbd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbc70.md#insn-00afbd04)
- 新版 [`00b5ba88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b9f4.md#insn-00b5ba88)

~~~diff
- 00afbce0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afbce0 ["INT_ADD", "register:40f0:8", ["const:afbce0:8", "const:4:8"]]
- 00afbce0 ["CALLIND", null, ["register:0:8"]]
- 00afbce0 bytes 00013fd6
- 00afbd00 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00afbd00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00afbd00 bytes e00300f9
- 00afbd04 ["INT_ADD", "register:40f0:8", ["const:afbd04:8", "const:4:8"]]
- 00afbd04 ["CALL", null, ["callee:00c5b770:8"]]
+ 00b5ba88 ["INT_ADD", "register:40f0:8", ["const:b5ba88:8", "const:4:8"]]
+ 00b5ba88 ["CALL", null, ["callee:00c5b770:8"]]
- 00afbd04 bytes eb8b0394
+ 00b5ba88 bytes 3aff0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-846b57083fe306b88db9bef4b8e335e7"></a>

### [`00afbd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbd60.md) → [`00b5bae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bae4.md) _ZN8firebase8callback14RemoveCallbackEPv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00afb988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb988.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b5b70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b70c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.33% / 新版 69.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbde4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbdf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5bb68"
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
      "00b5bb00",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bb14",
      "READ",
      [
        "storage",
        "010a0d28",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00afbd9c",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5bb00",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bb14",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5bb20",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afbd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbd60.md#insn-00afbd88) · [`00afbda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbd60.md#insn-00afbda4) · [`00afbdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbd60.md#insn-00afbdd0)
- 新版 [`00b5bb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bae4.md#insn-00b5bb0c)

~~~diff
- 00afbd88 ["INT_ADD", "register:40f0:8", ["const:afbd88:8", "const:4:8"]]
- 00afbd88 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5bb0c ["INT_ADD", "register:40f0:8", ["const:b5bb0c:8", "const:4:8"]]
+ 00b5bb0c ["CALL", null, ["callee:00c5a600:8"]]
- 00afbd88 bytes a6870394
+ 00b5bb0c bytes bdfa0394
- 00afbda4 ["INT_ADD", "register:40f0:8", ["const:afbda4:8", "const:4:8"]]
- 00afbda4 ["CALL", null, ["callee:00c5a600:8"]]
- 00afbda4 bytes 9f870394
- 00afbdd0 ["INT_ADD", "register:40f0:8", ["const:afbdd0:8", "const:4:8"]]
- 00afbdd0 ["CALL", null, ["ram:bdde20:8"]]
- 00afbdd0 bytes 14880394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1c8b7f0da1a184f84567c76cf585de7"></a>

### [`00afbe8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbe8c.md) → [`00b5bc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bc10.md) _ZN8firebase8callback13PollCallbacksEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00afb988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb988.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7d0.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00b5b70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b70c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58220.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.88% / 新版 72.88%

CFGの説明率　旧版 11.11% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbf08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbf14"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5bcb4",
      "incomplete_value": false,
      "site": "00b5bcb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1125000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afbf30",
      "incomplete_value": false,
      "site": "00afbf30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:d40:8"
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
      "00b5bc28",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bc38",
      "READ",
      [
        "storage",
        "010a0d28",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00afbec0",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5bc28",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bc38",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5bc44",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afbeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbe8c.md#insn-00afbeac) · [`00afbec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbe8c.md#insn-00afbec8) · [`00afbedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbe8c.md#insn-00afbedc)
- 新版 [`00b5bc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bc10.md#insn-00b5bc30) · [`00b5bc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bc10.md#insn-00b5bc60)

~~~diff
- 00afbeac ["INT_ADD", "register:40f0:8", ["const:afbeac:8", "const:4:8"]]
- 00afbeac ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5bc30 ["INT_ADD", "register:40f0:8", ["const:b5bc30:8", "const:4:8"]]
+ 00b5bc30 ["CALL", null, ["callee:00c5a600:8"]]
- 00afbeac bytes 5d870394
+ 00b5bc30 bytes 74fa0394
- 00afbec8 ["INT_ADD", "register:40f0:8", ["const:afbec8:8", "const:4:8"]]
- 00afbec8 ["CALL", null, ["callee:00c5a600:8"]]
- 00afbec8 bytes 56870394
- 00afbedc ["INT_ADD", "register:40f0:8", ["const:afbedc:8", "const:4:8"]]
- 00afbedc ["CALL", null, ["callee:00c57a90:8"]]
+ 00b5bc60 ["INT_ADD", "register:40f0:8", ["const:b5bc60:8", "const:4:8"]]
+ 00b5bc60 ["CALL", null, ["callee:00c57a90:8"]]
- 00afbedc bytes 597c0394
+ 00b5bc60 bytes 8cef0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eab0d8054203ad52dad8d8f0d877ce4d"></a>

### [`00afc0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc0b0.md) → [`00b5be34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5be34.md) _ZN8firebase8callback18CallbackDispatcherD2Ev

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdec80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec80.md) · 呼出先 6件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md)
- 新版 呼出元 1件 [`00c5b740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b740.md) · 呼出先 6件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.55% / 新版 72.55%

CFGの説明率　旧版 24.44% / 新版 28.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc11c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc1d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc1d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5be60",
      "PARAM",
      [
        "storage",
        "0029de08",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00afc120",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5be98"
      ]
    ],
    [
      "unmatched:00afc124",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bec4"
      ]
    ]
  ],
  "added": [
    [
      "00b5be60",
      "PARAM",
      [
        "storage",
        "002ae122",
        null,
        "string"
      ]
    ],
    [
      "00b5bea4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5be98"
      ]
    ],
    [
      "00b5bea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bec4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc0b0.md#insn-00afc0e0) · [`00afc11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc0b0.md#insn-00afc11c) · [`00afc120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc0b0.md#insn-00afc120)
- 新版 [`00b5be64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5be34.md#insn-00b5be64)

~~~diff
- 00afc0e0 ["INT_ADD", "register:40f0:8", ["const:afc0e0:8", "const:4:8"]]
- 00afc0e0 ["CALL", null, ["callee:00c5a9e0:8"]]
+ 00b5be64 ["INT_ADD", "register:40f0:8", ["const:b5be64:8", "const:4:8"]]
+ 00b5be64 ["CALL", null, ["callee:00c5a9e0:8"]]
- 00afc0e0 bytes a0870394
+ 00b5be64 bytes dffa0394
- 00afc11c ["COPY", "tmp:0:1", ["const:1:1"]]
- 00afc11c ["CALLOTHER", "tmp:1:1", ["const:3f:4", "register:4040:8", "const:10:1"]]
- 00afc11c ["BOOL_NEGATE", "tmp:2:1", ["tmp:1:1"]]
- 00afc11c ["CBRANCH", null, ["const:3:4", "tmp:2:1"]]
- 00afc11c bytes 0afd0bc8
- 00afc120 ["INT_NOTEQUAL", "tmp:0:1", ["register:4058:4", "const:0:4"]]
- 00afc120 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00afc120 bytes abffff35
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbb7df1617faa1973672c68165e0361d"></a>

### [`00afc248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc248.md) → [`00b5bfcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bfcc.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED2Ev

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.65% / 新版 80.65%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc26c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5bff0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5bff4",
      "incomplete_value": true,
      "site": "00b5bff8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afc270",
      "incomplete_value": true,
      "site": "00afc274",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:00afc260",
      "READ",
      [
        "storage",
        "00c1b988",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00afc26c",
      "DATA",
      [
        "storage",
        "00c107f8",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00b5c044",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb050"
      ]
    ]
  ],
  "added": [
    [
      "00b5bfe4",
      "READ",
      [
        "storage",
        "00c9b388",
        null,
        "pointer"
      ]
    ],
    [
      "00b5bff0",
      "DATA",
      [
        "storage",
        "00c8ff18",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00b5c044",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57aa0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc248.md#insn-00afc26c) · [`00afc274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc248.md#insn-00afc274)
- 新版 [`00b5bff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bfcc.md#insn-00b5bff8) · [`00b5bff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bfcc.md#insn-00b5bff0)

~~~diff
- 00afc26c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00afc26c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00afc26c bytes 080000f9
- 00afc274 ["INT_ADD", "register:40f0:8", ["const:afc274:8", "const:4:8"]]
- 00afc274 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5bff8 ["INT_ADD", "register:40f0:8", ["const:b5bff8:8", "const:4:8"]]
+ 00b5bff8 ["CALL", null, ["callee:00c5a600:8"]]
- 00afc274 bytes 6b860394
+ 00b5bff8 bytes 82f90394
+ 00b5bff0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00b5bff0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b5bff0 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-848a47b850033b13463b903ac1501867"></a>

### [`00afc2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc2c4.md) → [`00b5c048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c048.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED0Ev

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5c068",
      "incomplete_value": true,
      "site": "00b5c06c",
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
      "definition_site": "00afc2e4",
      "incomplete_value": true,
      "site": "00afc2e8",
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5c0b4",
      "value": [
        "leaf",
        "ram:c57aa0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00afc330",
      "value": [
        "leaf",
        "ram:bdb050:8"
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
      "00b5c060",
      "READ",
      [
        "storage",
        "00c1b988",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c06c",
      "DATA",
      [
        "storage",
        "00c107f8",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00b5c0b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb050"
      ]
    ]
  ],
  "added": [
    [
      "00b5c060",
      "READ",
      [
        "storage",
        "00c9b388",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c06c",
      "DATA",
      [
        "storage",
        "00c8ff18",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00b5c0b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57aa0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc2c4.md#insn-00afc330) · [`00afc2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc2c4.md#insn-00afc2d4) · [`00afc2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc2c4.md#insn-00afc2dc)
- 新版 [`00b5c0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c048.md#insn-00b5c0b4) · [`00b5c058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c048.md#insn-00b5c058) · [`00b5c060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c048.md#insn-00b5c060)

~~~diff
- 00afc330 ["INT_ADD", "register:40f0:8", ["const:afc330:8", "const:4:8"]]
- 00afc330 ["CALL", null, ["ram:bdb050:8"]]
+ 00b5c0b4 ["INT_ADD", "register:40f0:8", ["const:b5c0b4:8", "const:4:8"]]
+ 00b5c0b4 ["CALL", null, ["ram:c57aa0:8"]]
- 00afc330 bytes 487b0394
+ 00b5c0b4 bytes 7bee0394
- 00afc2d4 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00b5c058 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00afc2d4 bytes e80800f0
+ 00b5c058 bytes e80900f0
- 00afc2dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:988:8"]]
- 00afc2dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5c060 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:388:8"]]
+ 00b5c060 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00afc2dc bytes 08c544f9
+ 00b5c060 bytes 08c541f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78974649e0cb42fb826d6843016ec18e"></a>

### [`00afc3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc3b8.md) → [`00b5c13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c13c.md) _ZN8firebase8callback16BlockingCallbackD2Ev

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdecc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdecc0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b780.md)

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
      "definition_site": "00b5c158",
      "incomplete_value": true,
      "site": "00b5c15c",
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
      "definition_site": "00afc3d4",
      "incomplete_value": true,
      "site": "00afc3d8",
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
      "00b5c150",
      "READ",
      [
        "storage",
        "00c1b980",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c15c",
      "DATA",
      [
        "storage",
        "00c10848",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b5c150",
      "READ",
      [
        "storage",
        "00c9b380",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c15c",
      "DATA",
      [
        "storage",
        "00c8ff68",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc3b8.md#insn-00afc3c4) · [`00afc3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc3b8.md#insn-00afc3cc) · [`00afc3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc3b8.md#insn-00afc3e0)
- 新版 [`00b5c148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c13c.md#insn-00b5c148) · [`00b5c150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c13c.md#insn-00b5c150) · [`00b5c164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c13c.md#insn-00b5c164)

~~~diff
- 00afc3c4 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 00b5c148 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00afc3c4 bytes e90800f0
+ 00b5c148 bytes e90900f0
- 00afc3cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:980:8"]]
- 00afc3cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5c150 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:380:8"]]
+ 00b5c150 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00afc3cc bytes 29c144f9
+ 00b5c150 bytes 29c141f9
- 00afc3e0 ["INT_ADD", "register:40f0:8", ["const:afc3e0:8", "const:4:8"]]
- 00afc3e0 ["CALL", null, ["callee:00c5b780:8"]]
+ 00b5c164 ["INT_ADD", "register:40f0:8", ["const:b5c164:8", "const:4:8"]]
+ 00b5c164 ["CALL", null, ["callee:00c5b780:8"]]
- 00afc3e0 bytes 388a0394
+ 00b5c164 bytes 87fd0394
~~~


<a id="compare-cbc8c7f51e066566e511dd2f35f64d74"></a>

### [`00afc40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc40c.md) → [`00b5c190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c190.md) _ZN8firebase8callback16BlockingCallbackD0Ev

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdecc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdecc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b780.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5c1ac",
      "incomplete_value": true,
      "site": "00b5c1b0",
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
      "definition_site": "00afc428",
      "incomplete_value": true,
      "site": "00afc42c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc448"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b5c1cc"
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
      "00b5c1a4",
      "READ",
      [
        "storage",
        "00c1b980",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c1b0",
      "DATA",
      [
        "storage",
        "00c10848",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "unmatched:00afc448",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5c1a4",
      "READ",
      [
        "storage",
        "00c9b380",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c1b0",
      "DATA",
      [
        "storage",
        "00c8ff68",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00b5c1cc",
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

- 旧版 [`00afc448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc40c.md#insn-00afc448) · [`00afc418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc40c.md#insn-00afc418)
- 新版 [`00b5c1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c190.md#insn-00b5c1cc) · [`00b5c19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c190.md#insn-00b5c19c)

~~~diff
- 00afc448 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afc448 ["INT_ADD", "register:40f0:8", ["const:afc448:8", "const:4:8"]]
- 00afc448 ["CALLIND", null, ["register:0:8"]]
- 00afc448 bytes 00013fd6
+ 00b5c1cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c1cc ["INT_ADD", "register:40f0:8", ["const:b5c1cc:8", "const:4:8"]]
+ 00b5c1cc ["CALLIND", null, ["register:0:8"]]
+ 00b5c1cc bytes 00013fd6
- 00afc418 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 00b5c19c ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00afc418 bytes e90800f0
+ 00b5c19c bytes e90900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ba66c0b2a7ec581fd26097abce671a3"></a>

### [`00afc46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc46c.md) → [`00b5c1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c1f0.md) _ZN8firebase8callback13CallbackEntry7ExecuteEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdec40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec40.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5b700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b700.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc46c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc470"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc470"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc46c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc470",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc474",
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
      "00b5c1f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5c1f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5c1f8",
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

- 旧版 [`00afc46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc46c.md#insn-00afc46c) · [`00afc470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc46c.md#insn-00afc470) · [`00afc474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc46c.md#insn-00afc474)

~~~diff
- 00afc46c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00afc46c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afc46c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afc46c bytes f50f1df8
- 00afc470 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afc470 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afc470 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afc470 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afc470 bytes f44f01a9
- 00afc474 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afc474 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afc474 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afc474 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afc474 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-855768e12dd2568974d221fe598a4b97"></a>

### [`00afc570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc570.md) → [`00b5c2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c2f4.md) _ZN8firebase15CleanupNotifierC1Ev

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdddc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddc0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md)
- 新版 呼出元 1件 [`00c5a820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a820.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc574"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc570",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc574",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc584",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde20"
      ]
    ]
  ],
  "added": [
    [
      "00b5c2f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5c2f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5c308",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a880"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc570.md#insn-00afc570) · [`00afc574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc570.md#insn-00afc574) · [`00afc584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc570.md#insn-00afc584)

~~~diff
- 00afc570 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afc570 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afc570 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00afc570 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afc570 bytes f44fbea9
- 00afc574 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afc574 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afc574 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afc574 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afc574 bytes fd7b01a9
- 00afc584 ["INT_ADD", "register:40f0:8", ["const:afc584:8", "const:4:8"]]
- 00afc584 ["CALL", null, ["ram:bdde20:8"]]
- 00afc584 bytes 27860394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-391210f77fd2c4bca5134b310177cdfc"></a>

### [`00afc5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc5f0.md) → [`00b5c374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c374.md) _ZN8firebase15CleanupNotifierD1Ev

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdddd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddd0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00c5a830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a830.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6a0.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 5.26% / 新版 4.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc640"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5c400",
      "incomplete_value": true,
      "site": "00b5c400",
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
      "definition_site": "00afc67c",
      "incomplete_value": true,
      "site": "00afc67c",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc6ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc640",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5c3a4"
      ]
    ],
    [
      "unmatched:00afc660",
      "READ",
      [
        "storage",
        "00c1b998",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00afc664",
      "READ",
      [
        "storage",
        "010a0d48",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5c3c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5c3a4"
      ]
    ],
    [
      "00b5c3e4",
      "READ",
      [
        "storage",
        "00c9b398",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c3e8",
      "READ",
      [
        "storage",
        "01125c08",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc5f0.md#insn-00afc640) · [`00afc66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc5f0.md#insn-00afc66c) · [`00afc67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc5f0.md#insn-00afc67c)
- 新版 [`00b5c3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c374.md#insn-00b5c3f0) · [`00b5c400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c374.md#insn-00b5c400)

~~~diff
- 00afc640 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00afc640 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00afc640 bytes 01ffff54
- 00afc66c ["INT_ADD", "register:40f0:8", ["const:afc66c:8", "const:4:8"]]
- 00afc66c ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5c3f0 ["INT_ADD", "register:40f0:8", ["const:b5c3f0:8", "const:4:8"]]
+ 00b5c3f0 ["CALL", null, ["callee:00c5a600:8"]]
- 00afc66c bytes 6d850394
+ 00b5c3f0 bytes 84f80394
- 00afc67c ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00afc67c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00b5c400 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00b5c400 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00afc67c bytes 350100b4
+ 00b5c400 bytes 350100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d68628317761701265cb25b7b117449d"></a>

### [`00afc6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc6d8.md) → [`00b5c45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c45c.md) _ZN8firebase15CleanupNotifier10CleanupAllEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde910.md) · 呼出先 3件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00c5b390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b390.md) · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 10.00% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc6d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc6dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc6dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc6d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc6dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc6e0",
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
      "00b5c45c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5c460",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5c464",
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

- 旧版 [`00afc6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc6d8.md#insn-00afc6d8) · [`00afc6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc6d8.md#insn-00afc6dc) · [`00afc6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc6d8.md#insn-00afc6e0)

~~~diff
- 00afc6d8 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00afc6d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afc6d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afc6d8 bytes f50f1df8
- 00afc6dc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afc6dc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afc6dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afc6dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afc6dc bytes f44f01a9
- 00afc6e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afc6e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afc6e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afc6e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afc6e0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8b00b4c00652ee5d95d0bf7e624d905"></a>

### [`00afc748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc748.md) → [`00b5c4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c4cc.md) _ZN8firebase15CleanupNotifier19UnregisterAllOwnersEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdecf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdecf0.md) · 呼出先 3件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdece0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdece0.md)
- 新版 呼出元 1件 [`00c5b7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7b0.md) · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5b7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 79.59% / 新版 79.59%

CFGの説明率　旧版 26.67% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc79c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc7b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc7cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5c4e4",
      "READ",
      [
        "storage",
        "00c1b998",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c4ec",
      "READ",
      [
        "storage",
        "010a0d48",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b5c508",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5c4e4",
      "READ",
      [
        "storage",
        "00c9b398",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c4ec",
      "READ",
      [
        "storage",
        "01125c08",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b5c508",
      "READ",
      [
        "storage",
        "00c9b390",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc748.md#insn-00afc770) · [`00afc79c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc748.md#insn-00afc79c) · [`00afc7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc748.md#insn-00afc7ac)
- 新版 [`00b5c4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c4cc.md#insn-00b5c4f4)

~~~diff
- 00afc770 ["INT_ADD", "register:40f0:8", ["const:afc770:8", "const:4:8"]]
- 00afc770 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5c4f4 ["INT_ADD", "register:40f0:8", ["const:b5c4f4:8", "const:4:8"]]
+ 00b5c4f4 ["CALL", null, ["callee:00c5a600:8"]]
- 00afc770 bytes 2c850394
+ 00b5c4f4 bytes 43f80394
- 00afc79c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00afc79c bytes c0020054
- 00afc7ac ["INT_ADD", "register:40f0:8", ["const:afc7ac:8", "const:4:8"]]
- 00afc7ac ["CALL", null, ["callee:00c5a600:8"]]
- 00afc7ac bytes 1d850394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45141c9a84f6901915cc9ea2093f5f98"></a>

### [`00afc80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc80c.md) → [`00b5c590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c590.md) _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md)
- 新版 呼出元 1件 [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 50.00% / 新版 44.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc920"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5c6a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc850"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc86c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5c648"
      ]
    ]
  ],
  "added": [
    [
      "00b5c5f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5c648"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc80c.md#insn-00afc850) · [`00afc86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc80c.md#insn-00afc86c) · [`00afc920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc80c.md#insn-00afc920)

~~~diff
- 00afc850 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00afc850 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00afc850 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00afc850 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00afc850 bytes 29318a9a
- 00afc86c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00afc86c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00afc86c ["CBRANCH", null, ["local:b16:8", "tmp:1:1"]]
- 00afc86c bytes c9020054
- 00afc920 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 00afc920 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00afc920 bytes 681e00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a2a69c5d0afe220445c7430272243fd"></a>

### [`00afca1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afca1c.md) → [`00b5c7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c7a0.md) _ZN8firebase15CleanupNotifier15UnregisterOwnerEPS0_Pv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdece0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdece0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5b7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 61.29% / 新版 61.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afca50"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afca64"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afca80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afca2c",
      "READ",
      [
        "storage",
        "00c1b998",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00afca34",
      "READ",
      [
        "storage",
        "010a0d48",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b5c7c8",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5c7b0",
      "READ",
      [
        "storage",
        "00c9b398",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c7b8",
      "READ",
      [
        "storage",
        "01125c08",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b5c7c8",
      "READ",
      [
        "storage",
        "00c9b390",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afca3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afca1c.md#insn-00afca3c) · [`00afca50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afca1c.md#insn-00afca50) · [`00afca64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afca1c.md#insn-00afca64)
- 新版 [`00b5c7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c7a0.md#insn-00b5c7c0)

~~~diff
- 00afca3c ["INT_ADD", "register:40f0:8", ["const:afca3c:8", "const:4:8"]]
- 00afca3c ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5c7c0 ["INT_ADD", "register:40f0:8", ["const:b5c7c0:8", "const:4:8"]]
+ 00b5c7c0 ["CALL", null, ["callee:00c5a600:8"]]
- 00afca3c bytes 79840394
+ 00b5c7c0 bytes 90f70394
- 00afca50 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00afca50 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00afca50 bytes c90100b4
- 00afca64 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00afca64 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00afca64 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00afca64 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00afca64 bytes 0030899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bad20f734c3eedee535de199a1b7ffd3"></a>

### [`00afca98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afca98.md) → [`00b5c81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c81c.md) _ZN8firebase15CleanupNotifier13RegisterOwnerEPS0_Pv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde920.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5b3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3a0.md) · 呼出先 8件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.61% / 新版 86.61%

CFGの説明率　旧版 37.50% / 新版 28.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 6件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afca98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afca9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afca9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afca98",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afca9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afcaa0",
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
      "00b5c81c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b5c820",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5c824",
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

- 旧版 [`00afca98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afca98.md#insn-00afca98) · [`00afca9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afca98.md#insn-00afca9c) · [`00afcaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afca98.md#insn-00afcaa0)

~~~diff
- 00afca98 ["COPY", "tmp:0:8", ["register:40d8:8"]]
- 00afca98 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00afca98 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afca98 bytes fb0f1af8
- 00afca9c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00afca9c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00afca9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afca9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afca9c bytes fa6701a9
- 00afcaa0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00afcaa0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00afcaa0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afcaa0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afcaa0 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

