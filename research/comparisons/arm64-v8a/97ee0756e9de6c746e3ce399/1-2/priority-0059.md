# v15.7.3 → v15.7.4 · 最優先の変更候補 (59)

[一覧の目次](README.md)

<a id="compare-5246fc42cb583a359988595f702a3566"></a>

### [`00aa427c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa427c.md) → [`00aa42c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa42c0.md) FUN_00aa42c0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa42a8",
      "incomplete_value": true,
      "site": "00aa42ac",
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
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
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
      "definition_site": "00aa4324",
      "incomplete_value": true,
      "site": "00aa4350",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa4328",
      "incomplete_value": true,
      "site": "00aa4350",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa42ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa427c.md#insn-00aa42ac) · [`00aa430c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa427c.md#insn-00aa430c) · [`00aa4298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa427c.md#insn-00aa4298)
- 新版 `00aa42f0`（命令位置の公開資料なし） · `00aa4350`（命令位置の公開資料なし） · `00aa42dc`（命令位置の公開資料なし）

~~~diff
- 00aa42ac ["INT_ADD", "register:40f0:8", ["const:aa42ac:8", "const:4:8"]]
- 00aa42ac ["CALL", null, ["callee:005c2710:8"]]
+ 00aa42f0 ["INT_ADD", "register:40f0:8", ["const:aa42f0:8", "const:4:8"]]
+ 00aa42f0 ["CALL", null, ["callee:005c2710:8"]]
- 00aa42ac bytes 1979ec97
+ 00aa42f0 bytes 0879ec97
- 00aa430c ["INT_ADD", "register:40f0:8", ["const:aa430c:8", "const:4:8"]]
- 00aa430c ["CALL", null, ["callee:00a9f124:8"]]
+ 00aa4350 ["INT_ADD", "register:40f0:8", ["const:aa4350:8", "const:4:8"]]
+ 00aa4350 ["CALL", null, ["callee:00a9f124:8"]]
- 00aa430c bytes 75ebff97
+ 00aa4350 bytes 75ebff97
- 00aa4298 ["INT_ADD", "register:40f0:8", ["const:aa4298:8", "const:4:8"]]
- 00aa4298 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa42dc ["INT_ADD", "register:40f0:8", ["const:aa42dc:8", "const:4:8"]]
+ 00aa42dc ["CALL", null, ["callee:0081f580:8"]]
- 00aa4298 bytes baecf597
+ 00aa42dc bytes a9ecf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3beea849552d3c60641e300ad4195e96"></a>

### [`00aa4324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4324.md) → [`00aa4368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4368.md) FUN_00aa4368

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 28.57% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa4340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4324.md#insn-00aa4340) · [`00aa4354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4324.md#insn-00aa4354) · [`00aa435c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4324.md#insn-00aa435c)
- 新版 `00aa4384`（命令位置の公開資料なし） · `00aa4398`（命令位置の公開資料なし） · `00aa43a0`（命令位置の公開資料なし）

~~~diff
- 00aa4340 ["INT_ADD", "register:40f0:8", ["const:aa4340:8", "const:4:8"]]
- 00aa4340 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa4384 ["INT_ADD", "register:40f0:8", ["const:aa4384:8", "const:4:8"]]
+ 00aa4384 ["CALL", null, ["callee:0081f580:8"]]
- 00aa4340 bytes 90ecf597
+ 00aa4384 bytes 7fecf597
- 00aa4354 ["INT_ADD", "register:40f0:8", ["const:aa4354:8", "const:4:8"]]
- 00aa4354 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa4398 ["INT_ADD", "register:40f0:8", ["const:aa4398:8", "const:4:8"]]
+ 00aa4398 ["CALL", null, ["callee:005c2710:8"]]
- 00aa4354 bytes ef78ec97
+ 00aa4398 bytes de78ec97
- 00aa435c ["INT_ADD", "register:40f0:8", ["const:aa435c:8", "const:4:8"]]
- 00aa435c ["CALL", null, ["callee:0081f580:8"]]
+ 00aa43a0 ["INT_ADD", "register:40f0:8", ["const:aa43a0:8", "const:4:8"]]
+ 00aa43a0 ["CALL", null, ["callee:0081f580:8"]]
- 00aa435c bytes 89ecf597
+ 00aa43a0 bytes 78ecf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-333871050128751b6c085362526153ae"></a>

### [`00aa4c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4c30.md) → [`00aa4c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4c74.md) FUN_00aa4c74

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069e/0069ef54.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a960ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa4fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md)
- 新版 呼出元 4件 [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069ef54.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a960f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a960f0.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa4ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4ff4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 57.14% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa4c30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa4c30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa4c34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa4c30",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa4c34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa4c38",
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
      "00aa4c74",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa4c78",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa4c7c",
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

- 旧版 [`00aa4c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4c30.md#insn-00aa4c30) · [`00aa4c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4c30.md#insn-00aa4c34) · [`00aa4c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4c30.md#insn-00aa4c38)

~~~diff
- 00aa4c30 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa4c30 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa4c30 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa4c30 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa4c30 bytes fd7bbda9
- 00aa4c34 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa4c34 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aa4c34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aa4c34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa4c34 bytes f65701a9
- 00aa4c38 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa4c38 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa4c38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa4c38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa4c38 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-293d12ac1cbae32ed55826873a770a68"></a>

### [`00aa4cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4cf0.md) → [`00aa4d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4d34.md) FUN_00aa4d34

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0069ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069e/0069ef54.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`0069ef54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069ef54.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa4d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4cf0.md#insn-00aa4d04) · [`00aa4d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4cf0.md#insn-00aa4d18) · [`00aa4d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4cf0.md#insn-00aa4d20)
- 新版 `00aa4d48`（命令位置の公開資料なし） · `00aa4d5c`（命令位置の公開資料なし） · `00aa4d64`（命令位置の公開資料なし）

~~~diff
- 00aa4d04 ["INT_ADD", "register:40f0:8", ["const:aa4d04:8", "const:4:8"]]
- 00aa4d04 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa4d48 ["INT_ADD", "register:40f0:8", ["const:aa4d48:8", "const:4:8"]]
+ 00aa4d48 ["CALL", null, ["callee:0081f580:8"]]
- 00aa4d04 bytes 1feaf597
+ 00aa4d48 bytes 0eeaf597
- 00aa4d18 ["INT_ADD", "register:40f0:8", ["const:aa4d18:8", "const:4:8"]]
- 00aa4d18 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa4d5c ["INT_ADD", "register:40f0:8", ["const:aa4d5c:8", "const:4:8"]]
+ 00aa4d5c ["CALL", null, ["callee:005c2710:8"]]
- 00aa4d18 bytes 7e76ec97
+ 00aa4d5c bytes 6d76ec97
- 00aa4d20 ["INT_ADD", "register:40f0:8", ["const:aa4d20:8", "const:4:8"]]
- 00aa4d20 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa4d64 ["INT_ADD", "register:40f0:8", ["const:aa4d64:8", "const:4:8"]]
+ 00aa4d64 ["CALL", null, ["callee:0081f580:8"]]
- 00aa4d20 bytes 18eaf597
+ 00aa4d64 bytes 07eaf597
~~~


<a id="compare-3118d4b9524987f4cc06730b085e8b80"></a>

### [`00aa4fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md) → [`00aa4ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4ff4.md) FUN_00aa4ff4

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 14件 [`006a0128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0128.md) [`00a9f838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f838.md) [`00aa30a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa30a8.md) [`00aa3168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3168.md) [`00aa3228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3228.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cb4.md) [`008cfcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cf/008cfcf0.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 14件 [`006a0128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0128.md) [`00a9f87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f87c.md) [`00aa30ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa30ec.md) [`00aa31ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa31ac.md) [`00aa326c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa326c.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cb4.md) [`008cfcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cf/008cfcf0.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 39.29% / 新版 39.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 1件, `unresolved_branch_alignment` 9件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa50a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa50a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa50ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa4ff4",
      "DATA",
      [
        "storage",
        "00239d50",
        null,
        "Elf64_Rela[1792]"
      ]
    ],
    [
      "unmatched:00aa4ff8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa504c"
      ]
    ],
    [
      "unmatched:00aa4ffc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa506c"
      ]
    ]
  ],
  "added": [
    [
      "00aa5038",
      "DATA",
      [
        "storage",
        "00239d50",
        null,
        "Elf64_Rela[1792]"
      ]
    ],
    [
      "00aa503c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa504c"
      ]
    ],
    [
      "00aa5040",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa506c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa4ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md#insn-00aa4ff8) · [`00aa5004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md#insn-00aa5004) · [`00aa5038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md#insn-00aa5038)

~~~diff
- 00aa4ff8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aa4ff8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00aa4ff8 bytes 880000b5
- 00aa5004 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aa5004 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00aa5004 bytes 280100b4
- 00aa5038 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00aa5038 ["CBRANCH", null, ["local:b116:8", "tmp:0:1"]]
- 00aa5038 bytes 81290054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb9dc7f98a8b4052f53baad2525a69aa"></a>

### [`00aa556c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa556c.md) → [`00aa55b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa55b0.md) FUN_00aa55b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.23% / 新版 87.23%

CFGの説明率　旧版 3.03% / 新版 3.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa556c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa556c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa5570"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa556c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa5570",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa5574",
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
      "00aa55b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00aa55b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa55b8",
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

- 旧版 [`00aa556c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa556c.md#insn-00aa556c) · [`00aa5570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa556c.md#insn-00aa5570) · [`00aa5574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa556c.md#insn-00aa5574)

~~~diff
- 00aa556c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa556c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa556c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00aa556c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa556c bytes fd7bbca9
- 00aa5570 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aa5570 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00aa5570 bytes f70b00f9
- 00aa5574 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa5574 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aa5574 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa5574 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa5574 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bf8ea50f6fa84d5f02b78639bda9805"></a>

### [`00aa56e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa56e4.md) → [`00aa5728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5728.md) FUN_00aa5728

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.45% / 新版 57.45%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa56e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa56e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa56e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa56e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa56e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa5770",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aa5754"
      ]
    ]
  ],
  "added": [
    [
      "00aa5728",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa572c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa5770",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa5798"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa56e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa56e4.md#insn-00aa56e4) · [`00aa56e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa56e4.md#insn-00aa56e8) · [`00aa5718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa56e4.md#insn-00aa5718)
- 新版 `00aa575c`（命令位置の公開資料なし）

~~~diff
- 00aa56e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa56e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa56e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa56e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa56e4 bytes fd7bbda9
- 00aa56e8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa56e8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aa56e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aa56e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa56e8 bytes f65701a9
- 00aa5718 ["INT_ADD", "register:40f0:8", ["const:aa5718:8", "const:4:8"]]
- 00aa5718 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa575c ["INT_ADD", "register:40f0:8", ["const:aa575c:8", "const:4:8"]]
+ 00aa575c ["CALL", null, ["callee:005c2710:8"]]
- 00aa5718 bytes fe73ec97
+ 00aa575c bytes ed73ec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d1f961b6d56af54278247c40252ef09"></a>

### [`00aa5904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5904.md) → [`00aa5948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5948.md) FUN_00aa5948

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 58.62% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa5904"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa5904"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa5908"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa5904",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa5908",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa590c",
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
      "00aa5948",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa594c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa5950",
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

- 旧版 [`00aa5904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5904.md#insn-00aa5904) · [`00aa5908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5904.md#insn-00aa5908) · [`00aa590c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5904.md#insn-00aa590c)

~~~diff
- 00aa5904 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa5904 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa5904 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa5904 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa5904 bytes fd7bbda9
- 00aa5908 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa5908 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aa5908 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aa5908 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa5908 bytes f65701a9
- 00aa590c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa590c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa590c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa590c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa590c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3357e9a2ed7e391cb8a4057545fa068"></a>

### [`00aa59ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa59ac.md) → [`00aa59f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa59f0.md) FUN_00aa59f0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 12.90% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa5a1c",
      "incomplete_value": true,
      "site": "00aa5a20",
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
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa5a50"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00aa5a94"
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
      "unmatched:00aa5a04",
      "DATA",
      [
        "storage",
        "00239eb8",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ],
  "added": [
    [
      "00aa5a48",
      "DATA",
      [
        "storage",
        "00239eb8",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa59dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa59ac.md#insn-00aa59dc) · [`00aa5a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa59ac.md#insn-00aa5a50)
- 新版 `00aa5a20`（命令位置の公開資料なし） · `00aa5a94`（命令位置の公開資料なし）

~~~diff
- 00aa59dc ["INT_ADD", "register:40f0:8", ["const:aa59dc:8", "const:4:8"]]
- 00aa59dc ["CALL", null, ["callee:005c2710:8"]]
+ 00aa5a20 ["INT_ADD", "register:40f0:8", ["const:aa5a20:8", "const:4:8"]]
+ 00aa5a20 ["CALL", null, ["callee:005c2710:8"]]
- 00aa59dc bytes 4d73ec97
+ 00aa5a20 bytes 3c73ec97
- 00aa5a50 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aa5a50 ["RETURN", null, ["register:0:8"]]
- 00aa5a50 bytes c0035fd6
+ 00aa5a94 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00aa5a94 ["RETURN", null, ["register:0:8"]]
+ 00aa5a94 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-186505418ad1368e62c013e7020c5140"></a>

### [`00aa5ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5ab0.md) → [`00aa5af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5af4.md) FUN_00aa5af4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa5ab0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa5ab0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa5ab4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa5ab0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa5ab4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa5ab8",
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
      "00aa5af4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00aa5af8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa5afc",
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

- 旧版 [`00aa5ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5ab0.md#insn-00aa5ab0) · [`00aa5ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5ab0.md#insn-00aa5ab4) · [`00aa5ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5ab0.md#insn-00aa5ab8)

~~~diff
- 00aa5ab0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa5ab0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa5ab0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00aa5ab0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa5ab0 bytes fd7bbca9
- 00aa5ab4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aa5ab4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00aa5ab4 bytes f70b00f9
- 00aa5ab8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa5ab8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aa5ab8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa5ab8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa5ab8 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7acfb470c2a598820f540250e0c1d2b2"></a>

### [`00aa5b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5b80.md) → [`00aa5bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5bc4.md) FUN_00aa5bc4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa5bf4",
      "incomplete_value": true,
      "site": "00aa5bf8",
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
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa5c1c",
      "incomplete_value": true,
      "site": "00aa5c30",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
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
    "new": null,
    "old": {
      "definition_site": "00aa5c20",
      "incomplete_value": true,
      "site": "00aa5c30",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
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
      "unmatched:00aa5bdc",
      "DATA",
      [
        "storage",
        "00239ef4",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ],
  "added": [
    [
      "00aa5c20",
      "DATA",
      [
        "storage",
        "00239ef4",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa5bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5b80.md#insn-00aa5bb4) · [`00aa5c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5b80.md#insn-00aa5c30) · [`00aa5b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5b80.md#insn-00aa5b90)
- 新版 `00aa5bf8`（命令位置の公開資料なし） · `00aa5c74`（命令位置の公開資料なし）

~~~diff
- 00aa5bb4 ["INT_ADD", "register:40f0:8", ["const:aa5bb4:8", "const:4:8"]]
- 00aa5bb4 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa5bf8 ["INT_ADD", "register:40f0:8", ["const:aa5bf8:8", "const:4:8"]]
+ 00aa5bf8 ["CALL", null, ["callee:005c2710:8"]]
- 00aa5bb4 bytes d772ec97
+ 00aa5bf8 bytes c672ec97
- 00aa5c30 ["INT_ADD", "register:40f0:8", ["const:aa5c30:8", "const:4:8"]]
- 00aa5c30 ["CALL", null, ["callee:00a9f124:8"]]
+ 00aa5c74 ["INT_ADD", "register:40f0:8", ["const:aa5c74:8", "const:4:8"]]
+ 00aa5c74 ["CALL", null, ["callee:00a9f124:8"]]
- 00aa5c30 bytes 2ce5ff97
+ 00aa5c74 bytes 2ce5ff97
- 00aa5b90 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00aa5b90 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2fc54a04b8cd3a15eb0844cd45c2fef"></a>

### [`00aa5c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5c50.md) → [`00aa5c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5c94.md) FUN_00aa5c94

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 14.29% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa5cc4",
      "incomplete_value": true,
      "site": "00aa5cc8",
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
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa5c80",
      "incomplete_value": true,
      "site": "00aa5c84",
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
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
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
    "new": null,
    "old": {
      "definition_site": "00aa5cc8",
      "incomplete_value": true,
      "site": "00aa5ce4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
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
    "new": null,
    "old": {
      "definition_site": "00aa5cb8",
      "incomplete_value": true,
      "site": "00aa5ce4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa5c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5c50.md#insn-00aa5c84) · [`00aa5ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5c50.md#insn-00aa5ce4) · [`00aa5c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5c50.md#insn-00aa5c70)
- 新版 `00aa5cc8`（命令位置の公開資料なし） · `00aa5d28`（命令位置の公開資料なし） · `00aa5cb4`（命令位置の公開資料なし）

~~~diff
- 00aa5c84 ["INT_ADD", "register:40f0:8", ["const:aa5c84:8", "const:4:8"]]
- 00aa5c84 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa5cc8 ["INT_ADD", "register:40f0:8", ["const:aa5cc8:8", "const:4:8"]]
+ 00aa5cc8 ["CALL", null, ["callee:005c2710:8"]]
- 00aa5c84 bytes a372ec97
+ 00aa5cc8 bytes 9272ec97
- 00aa5ce4 ["INT_ADD", "register:40f0:8", ["const:aa5ce4:8", "const:4:8"]]
- 00aa5ce4 ["CALL", null, ["callee:00a9f124:8"]]
+ 00aa5d28 ["INT_ADD", "register:40f0:8", ["const:aa5d28:8", "const:4:8"]]
+ 00aa5d28 ["CALL", null, ["callee:00a9f124:8"]]
- 00aa5ce4 bytes ffe4ff97
+ 00aa5d28 bytes ffe4ff97
- 00aa5c70 ["INT_ADD", "register:40f0:8", ["const:aa5c70:8", "const:4:8"]]
- 00aa5c70 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa5cb4 ["INT_ADD", "register:40f0:8", ["const:aa5cb4:8", "const:4:8"]]
+ 00aa5cb4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa5c70 bytes 44e6f597
+ 00aa5cb4 bytes 33e6f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61cd26f2128c9a49177386a27caf125e"></a>

### [`00aa5d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5d7c.md) → [`00aa5dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5dc0.md) FUN_00aa5dc0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa5d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5d7c.md#insn-00aa5d90) · [`00aa5da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5d7c.md#insn-00aa5da4) · [`00aa5da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa5/00aa5d7c.md#insn-00aa5da8)
- 新版 `00aa5dd4`（命令位置の公開資料なし） · `00aa5de8`（命令位置の公開資料なし） · `00aa5dec`（命令位置の公開資料なし）

~~~diff
- 00aa5d90 ["INT_ADD", "register:40f0:8", ["const:aa5d90:8", "const:4:8"]]
- 00aa5d90 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa5dd4 ["INT_ADD", "register:40f0:8", ["const:aa5dd4:8", "const:4:8"]]
+ 00aa5dd4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa5d90 bytes fce5f597
+ 00aa5dd4 bytes ebe5f597
- 00aa5da4 ["INT_ADD", "register:40f0:8", ["const:aa5da4:8", "const:4:8"]]
- 00aa5da4 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa5de8 ["INT_ADD", "register:40f0:8", ["const:aa5de8:8", "const:4:8"]]
+ 00aa5de8 ["CALL", null, ["callee:005c2710:8"]]
- 00aa5da4 bytes 5b72ec97
+ 00aa5de8 bytes 4a72ec97
- 00aa5da8 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00aa5da8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00aa5da8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00aa5da8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00aa5dec ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00aa5dec ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00aa5dec ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00aa5dec ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00aa5da8 bytes 00010037
+ 00aa5dec bytes 00010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35d02387e7969bcaff01163f000fbc5d"></a>

### [`00aa621c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa621c.md) → [`00aa6260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6260.md) FUN_00aa6260

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa62c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00aa6304"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa62c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa621c.md#insn-00aa62c0) · [`00aa6238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa621c.md#insn-00aa6238)
- 新版 `00aa6304`（命令位置の公開資料なし） · `00aa627c`（命令位置の公開資料なし）

~~~diff
- 00aa62c0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aa62c0 ["RETURN", null, ["register:0:8"]]
- 00aa62c0 bytes c0035fd6
+ 00aa6304 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00aa6304 ["RETURN", null, ["register:0:8"]]
+ 00aa6304 bytes c0035fd6
- 00aa6238 ["INT_ADD", "register:40f0:8", ["const:aa6238:8", "const:4:8"]]
- 00aa6238 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa627c ["INT_ADD", "register:40f0:8", ["const:aa627c:8", "const:4:8"]]
+ 00aa627c ["CALL", null, ["callee:0081f580:8"]]
- 00aa6238 bytes d2e4f597
+ 00aa627c bytes c1e4f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3781e60b53f2aee2acde033a775890a1"></a>

### [`00aa62c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa62c4.md) → [`00aa6308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6308.md) FUN_00aa6308

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 5件 [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 5件 [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 91.04% / 新版 91.04%

CFGの説明率　旧版 7.14% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 4件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa6384",
      "incomplete_value": true,
      "site": "00aa6390",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
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
    "new": null,
    "old": {
      "definition_site": "00aa6388",
      "incomplete_value": true,
      "site": "00aa6390",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa63dc",
      "incomplete_value": true,
      "site": "00aa63f0",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00aa6320",
      "DATA",
      [
        "storage",
        "00239e24",
        null,
        "Elf64_Rela[1792]"
      ]
    ],
    [
      "unmatched:00aa6324",
      "READ",
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
      "00aa6364",
      "DATA",
      [
        "storage",
        "00239e24",
        null,
        "Elf64_Rela[1792]"
      ]
    ],
    [
      "00aa6368",
      "READ",
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

- 旧版 [`00aa6390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa62c4.md#insn-00aa6390) · [`00aa63ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa62c4.md#insn-00aa63ac) · [`00aa62d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa62c4.md#insn-00aa62d4)
- 新版 `00aa63d4`（命令位置の公開資料なし） · `00aa63f0`（命令位置の公開資料なし）

~~~diff
- 00aa6390 ["INT_ADD", "register:40f0:8", ["const:aa6390:8", "const:4:8"]]
- 00aa6390 ["CALL", null, ["callee:00aa2c70:8"]]
+ 00aa63d4 ["INT_ADD", "register:40f0:8", ["const:aa63d4:8", "const:4:8"]]
+ 00aa63d4 ["CALL", null, ["callee:00aa2c70:8"]]
- 00aa6390 bytes 27f2ff97
+ 00aa63d4 bytes 27f2ff97
- 00aa63ac ["INT_ADD", "register:40f0:8", ["const:aa63ac:8", "const:4:8"]]
- 00aa63ac ["CALL", null, ["callee:00a9f124:8"]]
+ 00aa63f0 ["INT_ADD", "register:40f0:8", ["const:aa63f0:8", "const:4:8"]]
+ 00aa63f0 ["CALL", null, ["callee:00a9f124:8"]]
- 00aa63ac bytes 4de3ff97
+ 00aa63f0 bytes 4de3ff97
- 00aa62d4 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00aa62d4 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83fb4876bd6519aae1060f4fba1910f1"></a>

### [`00aa6478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6478.md) → [`00aa64bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa64bc.md) FUN_00aa64bc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 2件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa64ec",
      "incomplete_value": true,
      "site": "00aa6508",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
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
    "new": null,
    "old": {
      "definition_site": "00aa64dc",
      "incomplete_value": true,
      "site": "00aa6508",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
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
    "new": null,
    "old": {
      "definition_site": "00aa64e0",
      "incomplete_value": true,
      "site": "00aa6508",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa6508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6478.md#insn-00aa6508) · [`00aa651c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6478.md#insn-00aa651c)
- 新版 `00aa654c`（命令位置の公開資料なし） · `00aa6560`（命令位置の公開資料なし）

~~~diff
- 00aa6508 ["INT_ADD", "register:40f0:8", ["const:aa6508:8", "const:4:8"]]
- 00aa6508 ["CALL", null, ["callee:00a9f124:8"]]
+ 00aa654c ["INT_ADD", "register:40f0:8", ["const:aa654c:8", "const:4:8"]]
+ 00aa654c ["CALL", null, ["callee:00a9f124:8"]]
- 00aa6508 bytes f6e2ff97
+ 00aa654c bytes f6e2ff97
- 00aa651c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aa651c ["RETURN", null, ["register:0:8"]]
- 00aa651c bytes c0035fd6
+ 00aa6560 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00aa6560 ["RETURN", null, ["register:0:8"]]
+ 00aa6560 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6452f67353009a7ee0a8475c684f5f40"></a>

### [`00aa6520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6520.md) → [`00aa6564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6564.md) FUN_00aa6564

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 14.29% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa6590",
      "incomplete_value": true,
      "site": "00aa6594",
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
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa654c",
      "incomplete_value": true,
      "site": "00aa6550",
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
            "register:4048:8"
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
      "unmatched:00aa6578",
      "DATA",
      [
        "storage",
        "00239ed8",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ],
  "added": [
    [
      "00aa65bc",
      "DATA",
      [
        "storage",
        "00239ed8",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa6550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6520.md#insn-00aa6550) · [`00aa653c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6520.md#insn-00aa653c) · [`00aa654c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6520.md#insn-00aa654c)
- 新版 `00aa6594`（命令位置の公開資料なし） · `00aa6580`（命令位置の公開資料なし）

~~~diff
- 00aa6550 ["INT_ADD", "register:40f0:8", ["const:aa6550:8", "const:4:8"]]
- 00aa6550 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa6594 ["INT_ADD", "register:40f0:8", ["const:aa6594:8", "const:4:8"]]
+ 00aa6594 ["CALL", null, ["callee:005c2710:8"]]
- 00aa6550 bytes 7070ec97
+ 00aa6594 bytes 5f70ec97
- 00aa653c ["INT_ADD", "register:40f0:8", ["const:aa653c:8", "const:4:8"]]
- 00aa653c ["CALL", null, ["callee:0081f580:8"]]
+ 00aa6580 ["INT_ADD", "register:40f0:8", ["const:aa6580:8", "const:4:8"]]
+ 00aa6580 ["CALL", null, ["callee:0081f580:8"]]
- 00aa653c bytes 11e4f597
+ 00aa6580 bytes 00e4f597
- 00aa654c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aa654c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aa654c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aa654c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aa654c bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-251d4e30e30fd3e969a86e9e43c8f879"></a>

### [`00aa6654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6654.md) → [`00aa6698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6698.md) FUN_00aa6698

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa6680",
      "incomplete_value": true,
      "site": "00aa6684",
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
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
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
      "definition_site": "00aa66ec",
      "incomplete_value": true,
      "site": "00aa670c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa66e4",
      "incomplete_value": true,
      "site": "00aa670c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa6684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6654.md#insn-00aa6684) · [`00aa66c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6654.md#insn-00aa66c8) · [`00aa6670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6654.md#insn-00aa6670)
- 新版 `00aa66c8`（命令位置の公開資料なし） · `00aa670c`（命令位置の公開資料なし） · `00aa66b4`（命令位置の公開資料なし）

~~~diff
- 00aa6684 ["INT_ADD", "register:40f0:8", ["const:aa6684:8", "const:4:8"]]
- 00aa6684 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa66c8 ["INT_ADD", "register:40f0:8", ["const:aa66c8:8", "const:4:8"]]
+ 00aa66c8 ["CALL", null, ["callee:005c2710:8"]]
- 00aa6684 bytes 2370ec97
+ 00aa66c8 bytes 1270ec97
- 00aa66c8 ["INT_ADD", "register:40f0:8", ["const:aa66c8:8", "const:4:8"]]
- 00aa66c8 ["CALL", null, ["callee:00a9f124:8"]]
+ 00aa670c ["INT_ADD", "register:40f0:8", ["const:aa670c:8", "const:4:8"]]
+ 00aa670c ["CALL", null, ["callee:00a9f124:8"]]
- 00aa66c8 bytes 86e2ff97
+ 00aa670c bytes 86e2ff97
- 00aa6670 ["INT_ADD", "register:40f0:8", ["const:aa6670:8", "const:4:8"]]
- 00aa6670 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa66b4 ["INT_ADD", "register:40f0:8", ["const:aa66b4:8", "const:4:8"]]
+ 00aa66b4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa6670 bytes c4e3f597
+ 00aa66b4 bytes b3e3f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cb9775571ed06d3372414befd92faa9"></a>

### [`00aa6798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6798.md) → [`00aa67dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa67dc.md) FUN_00aa67dc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 7.69% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa6798"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa6798"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa679c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa6798",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa679c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa67a0",
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
      "00aa67dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa67e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa67e4",
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

- 旧版 [`00aa6798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6798.md#insn-00aa6798) · [`00aa679c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6798.md#insn-00aa679c) · [`00aa67a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6798.md#insn-00aa67a0)

~~~diff
- 00aa6798 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa6798 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa6798 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa6798 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa6798 bytes fd7bbda9
- 00aa679c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aa679c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00aa679c bytes f50b00f9
- 00aa67a0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa67a0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa67a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa67a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa67a0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bc03eb98c4d476494cd4b2f1b859958"></a>

### [`00aa6810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6810.md) → [`00aa6854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6854.md) FUN_00aa6854

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa6880",
      "incomplete_value": true,
      "site": "00aa6884",
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
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa683c",
      "incomplete_value": true,
      "site": "00aa6840",
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
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa6840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6810.md#insn-00aa6840) · [`00aa682c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6810.md#insn-00aa682c) · [`00aa683c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6810.md#insn-00aa683c)
- 新版 `00aa6884`（命令位置の公開資料なし） · `00aa6870`（命令位置の公開資料なし）

~~~diff
- 00aa6840 ["INT_ADD", "register:40f0:8", ["const:aa6840:8", "const:4:8"]]
- 00aa6840 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa6884 ["INT_ADD", "register:40f0:8", ["const:aa6884:8", "const:4:8"]]
+ 00aa6884 ["CALL", null, ["callee:005c2710:8"]]
- 00aa6840 bytes b46fec97
+ 00aa6884 bytes a36fec97
- 00aa682c ["INT_ADD", "register:40f0:8", ["const:aa682c:8", "const:4:8"]]
- 00aa682c ["CALL", null, ["callee:0081f580:8"]]
+ 00aa6870 ["INT_ADD", "register:40f0:8", ["const:aa6870:8", "const:4:8"]]
+ 00aa6870 ["CALL", null, ["callee:0081f580:8"]]
- 00aa682c bytes 55e3f597
+ 00aa6870 bytes 44e3f597
- 00aa683c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aa683c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aa683c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aa683c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aa683c bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-205a220c9f66deb5690dc5620d6cc23c"></a>

### [`00aa68ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa68ec.md) → [`00aa6930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6930.md) FUN_00aa6930

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 6件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`007cebc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ce/007cebc8.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 6件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`007cebc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ce/007cebc8.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`007cfcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 17.65% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa69bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aa6a00"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa695c",
      "incomplete_value": true,
      "site": "00aa6960",
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
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa6918",
      "incomplete_value": true,
      "site": "00aa691c",
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
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
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
      "unmatched:00aa695c",
      "DATA",
      [
        "storage",
        "0032f934",
        null,
        "byte[23]"
      ]
    ],
    [
      "unmatched:00aa6960",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0081f580"
      ]
    ],
    [
      "unmatched:00aa69bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa6aa8"
      ]
    ]
  ],
  "added": [
    [
      "00aa69a0",
      "DATA",
      [
        "storage",
        "0032f934",
        null,
        "byte[23]"
      ]
    ],
    [
      "00aa69a4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0081f580"
      ]
    ],
    [
      "00aa6a00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa6aa8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa691c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa68ec.md#insn-00aa691c) · [`00aa6960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa68ec.md#insn-00aa6960) · [`00aa6978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa68ec.md#insn-00aa6978)
- 新版 `00aa6960`（命令位置の公開資料なし） · `00aa69bc`（命令位置の公開資料なし）

~~~diff
- 00aa691c ["INT_ADD", "register:40f0:8", ["const:aa691c:8", "const:4:8"]]
- 00aa691c ["CALL", null, ["callee:005c2710:8"]]
+ 00aa6960 ["INT_ADD", "register:40f0:8", ["const:aa6960:8", "const:4:8"]]
+ 00aa6960 ["CALL", null, ["callee:005c2710:8"]]
- 00aa691c bytes 7d6fec97
+ 00aa6960 bytes 6c6fec97
- 00aa6960 ["INT_ADD", "register:40f0:8", ["const:aa6960:8", "const:4:8"]]
- 00aa6960 ["CALL", null, ["callee:0081f580:8"]]
- 00aa6960 bytes 08e3f597
- 00aa6978 ["INT_ADD", "register:40f0:8", ["const:aa6978:8", "const:4:8"]]
- 00aa6978 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa69bc ["INT_ADD", "register:40f0:8", ["const:aa69bc:8", "const:4:8"]]
+ 00aa69bc ["CALL", null, ["callee:0081f580:8"]]
- 00aa6978 bytes 02e3f597
+ 00aa69bc bytes f1e2f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-700da7ffa82248f1ada76c9d7d687ef2"></a>

### [`00aa6a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6a74.md) → [`00aa6ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6ab8.md) FUN_00aa6ab8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 14.29% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa6aa0",
      "incomplete_value": true,
      "site": "00aa6aa4",
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
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
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
      "definition_site": "00aa6b2c",
      "incomplete_value": true,
      "site": "00aa6b48",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa6b1c",
      "incomplete_value": true,
      "site": "00aa6b48",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa6aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6a74.md#insn-00aa6aa4) · [`00aa6b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6a74.md#insn-00aa6b04) · [`00aa6a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6a74.md#insn-00aa6a90)
- 新版 `00aa6ae8`（命令位置の公開資料なし） · `00aa6b48`（命令位置の公開資料なし） · `00aa6ad4`（命令位置の公開資料なし）

~~~diff
- 00aa6aa4 ["INT_ADD", "register:40f0:8", ["const:aa6aa4:8", "const:4:8"]]
- 00aa6aa4 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa6ae8 ["INT_ADD", "register:40f0:8", ["const:aa6ae8:8", "const:4:8"]]
+ 00aa6ae8 ["CALL", null, ["callee:005c2710:8"]]
- 00aa6aa4 bytes 1b6fec97
+ 00aa6ae8 bytes 0a6fec97
- 00aa6b04 ["INT_ADD", "register:40f0:8", ["const:aa6b04:8", "const:4:8"]]
- 00aa6b04 ["CALL", null, ["callee:00a9f124:8"]]
+ 00aa6b48 ["INT_ADD", "register:40f0:8", ["const:aa6b48:8", "const:4:8"]]
+ 00aa6b48 ["CALL", null, ["callee:00a9f124:8"]]
- 00aa6b04 bytes 77e1ff97
+ 00aa6b48 bytes 77e1ff97
- 00aa6a90 ["INT_ADD", "register:40f0:8", ["const:aa6a90:8", "const:4:8"]]
- 00aa6a90 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa6ad4 ["INT_ADD", "register:40f0:8", ["const:aa6ad4:8", "const:4:8"]]
+ 00aa6ad4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa6a90 bytes bce2f597
+ 00aa6ad4 bytes abe2f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-965eaabffbaa9e89fad5f23e2f06fce4"></a>

### [`00aa6b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6b1c.md) → [`00aa6b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa6/00aa6b60.md) FUN_00aa6b60

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`006a4d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a4/006a4d58.md) · 呼出先 6件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cb4.md) [`008cfcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cf/008cfcf0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 2件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`006a4d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a4/006a4d58.md) · 呼出先 6件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cb4.md) [`008cfcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cf/008cfcf0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 28.70% / 新版 28.70%

CFGの説明率　旧版 11.86% / 新版 12.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 48件, `unresolved_call_alignment` 22件, `unresolved_store_alignment` 56件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa6c5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa6c70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa6c70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa6bac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa6c10"
      ]
    ],
    [
      "unmatched:00aa6bf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa7234"
      ]
    ],
    [
      "unmatched:00aa6c0c",
      "DATA",
      [
        "storage",
        "00239d50",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ],
  "added": [
    [
      "00aa6bf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa6c10"
      ]
    ],
    [
      "00aa6c38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa7234"
      ]
    ],
    [
      "00aa6c50",
      "DATA",
      [
        "storage",
        "00239d50",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa6c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6b1c.md#insn-00aa6c5c) · [`00aa6c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa6/00aa6b1c.md#insn-00aa6c70)
- 新版 `00aa6c5c`（命令位置の公開資料なし）

~~~diff
- 00aa6c5c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:1c:8"]]
- 00aa6c5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00aa6c5c bytes 141c00b9
+ 00aa6c5c ["COPY", "register:40a8:8", ["register:40c8:8"]]
+ 00aa6c5c bytes f50319aa
- 00aa6c70 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00aa6c70 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aa6c70 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00aa6c70 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00aa6c70 bytes bf7e00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae79f0d107bfc19bd1595ab73893ef81"></a>

### [`00aa7314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7314.md) → [`00aa7358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa7358.md) FUN_00aa7358

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`005a2308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a2/005a2308.md) [`005a3cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a3cbc.md) [`005a3eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a3eb8.md) [`005a45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) [`006a4e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a4/006a4e9c.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 6件 [`005a2308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a2/005a2308.md) [`005a3cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a3cbc.md) [`005a3eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a3eb8.md) [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) [`006a4e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a4/006a4e9c.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.20% / 新版 95.20%

CFGの説明率　旧版 45.28% / 新版 43.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa7428"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa7434"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aa746c"
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
      "unmatched:00aa7428",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa7498"
      ]
    ],
    [
      "unmatched:00aa7434",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa73b8"
      ]
    ]
  ],
  "added": [
    [
      "00aa746c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa7498"
      ]
    ],
    [
      "00aa7478",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa73b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa73dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7314.md#insn-00aa73dc) · [`00aa7428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7314.md#insn-00aa7428) · [`00aa7434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7314.md#insn-00aa7434)
- 新版 `00aa7420`（命令位置の公開資料なし）

~~~diff
- 00aa73dc ["INT_ADD", "register:40f0:8", ["const:aa73dc:8", "const:4:8"]]
- 00aa73dc ["CALL", null, ["callee:00bdb240:8"]]
+ 00aa7420 ["INT_ADD", "register:40f0:8", ["const:aa7420:8", "const:4:8"]]
+ 00aa7420 ["CALL", null, ["callee:00bdb240:8"]]
- 00aa73dc bytes 85cf0494
+ 00aa7420 bytes 88cf0494
- 00aa7428 ["CBRANCH", null, ["local:b25:8", "register:101:1"]]
- 00aa7428 bytes 60010054
- 00aa7434 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00aa7434 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00aa7434 bytes 01faff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e918a41c0824c5ee601d7c850a41440"></a>

### [`00aa7508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7508.md) → [`00aa754c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa754c.md) FUN_00aa754c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00aa71f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa71f8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00aa723c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa723c.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 93.40% / 新版 93.40%

CFGの説明率　旧版 50.00% / 新版 52.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 3件

アドレスに依存する影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa7510"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa7530"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa7644"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa7510",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa7568"
      ]
    ],
    [
      "unmatched:00aa7530",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa75b8"
      ]
    ],
    [
      "unmatched:00aa7644",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa769c"
      ]
    ]
  ],
  "added": [
    [
      "00aa7554",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa7568"
      ]
    ],
    [
      "00aa7574",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa75b8"
      ]
    ],
    [
      "00aa7688",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa769c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa7510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7508.md#insn-00aa7510) · [`00aa7530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7508.md#insn-00aa7530)
- 新版 `00aa7554`（命令位置の公開資料なし）

~~~diff
- 00aa7510 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00aa7510 bytes a0000054
- 00aa7530 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00aa7530 bytes 20020054
+ 00aa7554 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 00aa7554 bytes a0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e4d5d2b162aea7a37ecfe86745021c5"></a>

### [`00aa76f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa76f4.md) → [`00aa7738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa7738.md) _INIT_244

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.58% / 新版 74.58%

CFGの説明率　旧版 8.93% / 新版 8.20%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa7724"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa7738"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa773c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa7724",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa7730",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aa7738",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aa7768",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00aa7774",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00aa777c",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa7724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa76f4.md#insn-00aa7724) · [`00aa7738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa76f4.md#insn-00aa7738) · [`00aa773c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa76f4.md#insn-00aa773c)

~~~diff
- 00aa7724 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aa7724 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00aa7724 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00aa7724 bytes a9831ff8
- 00aa7738 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00aa7738 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00aa7738 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00aa7738 bytes ea130278
- 00aa773c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00aa773c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00aa773c bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9ad1274bdd36f24a4ce6399b77fec7b"></a>

### [`00aa7ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7ae4.md) → [`00aa7b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa7b28.md) FUN_00aa7b28

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 25件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00424230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424230.md)
- 新版 呼出元 1件 [`00ac0004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac0/00ac0004.md) · 呼出先 25件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00424230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424230.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 36.73% / 新版 36.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 42件, `unresolved_call_alignment` 17件, `unresolved_store_alignment` 59件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa7b2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa7b30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa7b94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa7b2c",
      "WRITE",
      [
        "storage",
        "Stack[-0xc9]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa7b30",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00aa7b30",
      "WRITE",
      [
        "storage",
        "Stack[-0x228]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aa7b70",
      "WRITE",
      [
        "storage",
        "Stack[-0xc9]",
        null,
        null
      ]
    ],
    [
      "00aa7b74",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00aa7b74",
      "WRITE",
      [
        "storage",
        "Stack[-0x228]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa7b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7ae4.md#insn-00aa7b2c) · [`00aa7b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7ae4.md#insn-00aa7b30) · [`00aa7b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7ae4.md#insn-00aa7b94)

~~~diff
- 00aa7b2c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aa7b2c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aa7b2c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffff97:8"]]
- 00aa7b2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aa7b2c bytes bf731938
- 00aa7b30 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:98:8"]]
- 00aa7b30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aa7b30 bytes e84f00f9
- 00aa7b94 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aa7b94 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:41:8"]]
- 00aa7b94 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00aa7b94 bytes a81204f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e3456317b2f61b0cf5e328b7a0ceb4e"></a>

### [`00aa8e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa8/00aa8e38.md) → [`00aa8e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa8/00aa8e7c.md) FUN_00aa8e7c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 62.50% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa8e54"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aa8e98"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aa8e54"
      ],
      [
        "FALL_THROUGH",
        "00aa8e98"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aa8e98",
      "incomplete_value": true,
      "site": "00aa8e9c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa8e54",
      "incomplete_value": true,
      "site": "00aa8e58",
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
      "unmatched:00aa8e54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa8ea4"
      ]
    ]
  ],
  "added": [
    [
      "00aa8e98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa8ea4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa8e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa8/00aa8e38.md#insn-00aa8e54) · [`00aa8e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa8/00aa8e38.md#insn-00aa8e4c)
- 新版 `00aa8e98`（命令位置の公開資料なし） · `00aa8e90`（命令位置の公開資料なし）

~~~diff
- 00aa8e54 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00aa8e54 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aa8e54 bytes 600000b4
+ 00aa8e98 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00aa8e98 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00aa8e98 bytes 600000b4
- 00aa8e4c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00aa8e4c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00aa8e90 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00aa8e90 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00aa8e4c bytes b30100b4
+ 00aa8e90 bytes b30100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-222da991fc1bfb8f46c2d56a629b922e"></a>

### [`00aa8e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa8/00aa8e8c.md) → [`00aa8ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa8/00aa8ed0.md) FUN_00aa8ed0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) [`00add7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00add/00add7d4.md) · 呼出先 7件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa9238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9238.md)
- 新版 呼出元 2件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) [`00add818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add818.md) · 呼出先 7件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa927c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa927c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.13% / 新版 82.13%

CFGの説明率　旧版 38.74% / 新版 39.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa8e8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa8e8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa8e90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa8e8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa8e90",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa8e94",
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
      "00aa8ed0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00aa8ed4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00aa8ed8",
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

- 旧版 [`00aa8e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa8/00aa8e8c.md#insn-00aa8e8c) · [`00aa8e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa8/00aa8e8c.md#insn-00aa8e90) · [`00aa8e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa8/00aa8e8c.md#insn-00aa8e94)

~~~diff
- 00aa8e8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa8e8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa8e8c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00aa8e8c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa8e8c bytes fd7bbaa9
- 00aa8e90 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00aa8e90 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00aa8e90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aa8e90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa8e90 bytes fc6f01a9
- 00aa8e94 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00aa8e94 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00aa8e94 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa8e94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa8e94 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dba5172fcfde05c05b44ad35bbe273f"></a>

### [`00aa9390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9390.md) → [`00aa93d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa93d4.md) _INIT_245

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
      "definition_site": "00aa9410",
      "incomplete_value": true,
      "site": "00aa942c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aa93cc",
      "incomplete_value": true,
      "site": "00aa93e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aa9434",
      "incomplete_value": true,
      "site": "00aa9450",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aa93f0",
      "incomplete_value": true,
      "site": "00aa940c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aa9454",
      "incomplete_value": true,
      "site": "00aa9470",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aa9410",
      "incomplete_value": true,
      "site": "00aa942c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00aa9410",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00aa9434",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00aa9454",
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
      "00aa9410",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00aa9434",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00aa9454",
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

- 旧版 [`00aa93c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9390.md#insn-00aa93c8) · [`00aa94f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9390.md#insn-00aa94f0) · [`00aa95c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9390.md#insn-00aa95c4)
- 新版 `00aa940c`（命令位置の公開資料なし） · `00aa9534`（命令位置の公開資料なし） · `00aa9608`（命令位置の公開資料なし）

~~~diff
- 00aa93c8 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00aa93c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00aa93c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00aa93c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00aa940c ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00aa940c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00aa940c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00aa940c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00aa93c8 bytes 29750b91
+ 00aa940c bytes 29dd0d91
- 00aa94f0 ["INT_ADD", "register:40f0:8", ["const:aa94f0:8", "const:4:8"]]
- 00aa94f0 ["CALL", null, ["callee:00418cb8:8"]]
+ 00aa9534 ["INT_ADD", "register:40f0:8", ["const:aa9534:8", "const:4:8"]]
+ 00aa9534 ["CALL", null, ["callee:00418cb8:8"]]
- 00aa94f0 bytes f2bde597
+ 00aa9534 bytes e1bde597
- 00aa95c4 ["INT_ADD", "register:40f0:8", ["const:aa95c4:8", "const:4:8"]]
- 00aa95c4 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00aa9608 ["INT_ADD", "register:40f0:8", ["const:aa9608:8", "const:4:8"]]
+ 00aa9608 ["CALL", null, ["callee:00bdafe0:8"]]
- 00aa95c4 bytes 73c60494
+ 00aa9608 bytes 76c60494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-375c97af4c7156c5e2943ec6e9d86db7"></a>

### [`00aa980c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa980c.md) → [`00aa9850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9850.md) FUN_00aa9850

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009c9128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009c9/009c9128.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0045d240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d240.md) [`0045d2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d2a0.md) [`0045d300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d300.md)
- 新版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0045d240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d240.md) [`0045d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d2a0.md) [`0045d300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d300.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 89.07% / 新版 90.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa995c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa9960"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa9c58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa996c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa99bc"
      ]
    ],
    [
      "unmatched:00aa9c10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa9cb8"
      ]
    ],
    [
      "00aa9c98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aa9c60"
      ]
    ]
  ],
  "added": [
    [
      "00aa99b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa99bc"
      ]
    ],
    [
      "00aa9c54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa9cb8"
      ]
    ],
    [
      "00aa9c98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa9ca4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa995c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa980c.md#insn-00aa995c) · [`00aa9960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa980c.md#insn-00aa9960) · [`00aa996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa980c.md#insn-00aa996c)

~~~diff
- 00aa995c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:38:8"]]
- 00aa995c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00aa995c bytes 0080833c
- 00aa9960 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00aa9960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aa9960 bytes 600200f9
- 00aa996c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aa996c ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00aa996c bytes 680000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee9c99420a886dffbcedd56f746f37f9"></a>

### [`00aab744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab744.md) → [`00aab788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab788.md) FUN_00aab788

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`00a90740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90740.md) [`00aad1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad1d8.md) [`00aad2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad2f4.md) · 呼出先 32件 [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md)
- 新版 呼出元 4件 [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`00a90784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90784.md) [`00aad21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad21c.md) [`00aad338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad338.md) · 呼出先 32件 [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883e08.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00aab7ec",
      "incomplete_value": false,
      "site": "00aab7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aab7a8",
      "incomplete_value": false,
      "site": "00aab7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:288:8"
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
      "definition_site": "00aab824",
      "incomplete_value": false,
      "site": "00aab824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aab7e0",
      "incomplete_value": false,
      "site": "00aab7e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "definition_site": "00aab844",
      "incomplete_value": false,
      "site": "00aab844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aab800",
      "incomplete_value": false,
      "site": "00aab800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "00aab7ec",
      "DATA",
      [
        "storage",
        "00c0f288",
        null,
        "undefined *"
      ]
    ],
    [
      "00aab824",
      "DATA",
      [
        "storage",
        "00c0f408",
        null,
        "undefined *"
      ]
    ],
    [
      "00aab844",
      "DATA",
      [
        "storage",
        "00c0f488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aab7ec",
      "DATA",
      [
        "storage",
        "00c0f2d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00aab824",
      "DATA",
      [
        "storage",
        "00c0f458",
        null,
        "undefined *"
      ]
    ],
    [
      "00aab844",
      "DATA",
      [
        "storage",
        "00c0f4d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aab844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab744.md#insn-00aab844) · [`00aab790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab744.md#insn-00aab790) · [`00aab798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab744.md#insn-00aab798)
- 新版 `00aab888`（命令位置の公開資料なし） · `00aab7d4`（命令位置の公開資料なし） · `00aab7dc`（命令位置の公開資料なし）

~~~diff
- 00aab844 ["INT_ADD", "register:40f0:8", ["const:aab844:8", "const:4:8"]]
- 00aab844 ["CALL", null, ["callee:008864f8:8"]]
+ 00aab888 ["INT_ADD", "register:40f0:8", ["const:aab888:8", "const:4:8"]]
+ 00aab888 ["CALL", null, ["callee:008864f8:8"]]
- 00aab844 bytes 2d6bf797
+ 00aab888 bytes 1c6bf797
- 00aab790 ["INT_ADD", "register:40f0:8", ["const:aab790:8", "const:4:8"]]
- 00aab790 ["CALL", null, ["callee:00aab624:8"]]
+ 00aab7d4 ["INT_ADD", "register:40f0:8", ["const:aab7d4:8", "const:4:8"]]
+ 00aab7d4 ["CALL", null, ["callee:00aab624:8"]]
- 00aab790 bytes 94ffff97
+ 00aab7d4 bytes 94ffff97
- 00aab798 ["INT_ADD", "register:40f0:8", ["const:aab798:8", "const:4:8"]]
- 00aab798 ["CALL", null, ["callee:0081f580:8"]]
+ 00aab7dc ["INT_ADD", "register:40f0:8", ["const:aab7dc:8", "const:4:8"]]
+ 00aab7dc ["CALL", null, ["callee:0081f580:8"]]
- 00aab798 bytes 7acff597
+ 00aab7dc bytes 69cff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d76fdea535a5c787386cec5a9350a195"></a>

### [`00aabe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aabe04.md) → [`00aabe48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aabe48.md) FUN_00aabe48

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00aab744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab744.md) [`00aad9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad9a0.md) [`00aadadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadadc.md) · 呼出先 20件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 3件 [`00aab788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aab/00aab788.md) [`00aad9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad9e4.md) [`00aadb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadb20.md) · 呼出先 20件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.75% / 新版 91.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aac104",
      "incomplete_value": false,
      "site": "00aac104",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "00aac0c0",
      "incomplete_value": false,
      "site": "00aac0c0",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
    "ordinal": 30,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aac108",
      "incomplete_value": false,
      "site": "00aac108",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aac0c4",
      "incomplete_value": false,
      "site": "00aac0c4",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00aac104",
      "incomplete_value": false,
      "site": "00aac108",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "00aac0c0",
      "incomplete_value": false,
      "site": "00aac0c4",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "00aabfb8",
      "READ",
      [
        "storage",
        "002a7732",
        null,
        "string"
      ]
    ],
    [
      "00aabfe4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00aac028",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aabfb8",
      "READ",
      [
        "storage",
        "002a77cc",
        null,
        "string"
      ]
    ],
    [
      "00aabfe4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00aac028",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aabfec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aabe04.md#insn-00aabfec) · [`00aac07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aabe04.md#insn-00aac07c) · [`00aac08c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aabe04.md#insn-00aac08c)
- 新版 `00aac030`（命令位置の公開資料なし） · `00aac0c0`（命令位置の公開資料なし） · `00aac0d0`（命令位置の公開資料なし）

~~~diff
- 00aabfec ["INT_ADD", "register:40f0:8", ["const:aabfec:8", "const:4:8"]]
- 00aabfec ["CALL", null, ["callee:0045b734:8"]]
+ 00aac030 ["INT_ADD", "register:40f0:8", ["const:aac030:8", "const:4:8"]]
+ 00aac030 ["CALL", null, ["callee:0045b734:8"]]
- 00aabfec bytes d2bde697
+ 00aac030 bytes c1bde697
- 00aac07c ["INT_ADD", "register:40f0:8", ["const:aac07c:8", "const:4:8"]]
- 00aac07c ["CALL", null, ["callee:00bdb060:8"]]
+ 00aac0c0 ["INT_ADD", "register:40f0:8", ["const:aac0c0:8", "const:4:8"]]
+ 00aac0c0 ["CALL", null, ["callee:00bdb060:8"]]
- 00aac07c bytes e5bb0494
+ 00aac0c0 bytes e8bb0494
- 00aac08c ["INT_ADD", "register:40f0:8", ["const:aac08c:8", "const:4:8"]]
- 00aac08c ["CALL", null, ["callee:00bdb060:8"]]
+ 00aac0d0 ["INT_ADD", "register:40f0:8", ["const:aac0d0:8", "const:4:8"]]
+ 00aac0d0 ["CALL", null, ["callee:00bdb060:8"]]
- 00aac08c bytes e1bb0494
+ 00aac0d0 bytes e4bb0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cedc1826494ded224fb09c8877afceac"></a>

### [`00aacb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb2c.md) → [`00aacb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb70.md) FUN_00aacb70

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00aac920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac920.md) [`00aacb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb54.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00aac964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aac964.md) [`00aacb98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb98.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00aacb7c",
      "incomplete_value": false,
      "site": "00aacb80",
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
    "old": {
      "definition_site": "00aacb38",
      "incomplete_value": false,
      "site": "00aacb3c",
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
            "const:303:8"
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
      "00aacb7c",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aacb7c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aacb3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb2c.md#insn-00aacb3c) · [`00aacb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb2c.md#insn-00aacb38)
- 新版 `00aacb80`（命令位置の公開資料なし） · `00aacb7c`（命令位置の公開資料なし）

~~~diff
- 00aacb3c ["INT_ADD", "register:40f0:8", ["const:aacb3c:8", "const:4:8"]]
- 00aacb3c ["CALL", null, ["callee:00418c38:8"]]
+ 00aacb80 ["INT_ADD", "register:40f0:8", ["const:aacb80:8", "const:4:8"]]
+ 00aacb80 ["CALL", null, ["callee:00418c38:8"]]
- 00aacb3c bytes 3fb0e597
+ 00aacb80 bytes 2eb0e597
- 00aacb38 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00aacb38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aacb38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aacb38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aacb7c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00aacb7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aacb7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aacb7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aacb38 bytes 000c0c91
+ 00aacb7c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99d5915d2545182bcf9d6c4ccf0dedc1"></a>

### [`00aacb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb40.md) → [`00aacb84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb84.md) FUN_00aacb84

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00aa980c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa980c.md) [`00aaafa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00aa9850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa9/00aa9850.md) [`00aaafe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaafe8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00aacb90",
      "incomplete_value": false,
      "site": "00aacb94",
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
    "old": {
      "definition_site": "00aacb4c",
      "incomplete_value": false,
      "site": "00aacb50",
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
            "const:303:8"
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
      "00aacb90",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aacb90",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aacb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb40.md#insn-00aacb50) · [`00aacb4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb40.md#insn-00aacb4c)
- 新版 `00aacb94`（命令位置の公開資料なし） · `00aacb90`（命令位置の公開資料なし）

~~~diff
- 00aacb50 ["INT_ADD", "register:40f0:8", ["const:aacb50:8", "const:4:8"]]
- 00aacb50 ["CALL", null, ["callee:00418c38:8"]]
+ 00aacb94 ["INT_ADD", "register:40f0:8", ["const:aacb94:8", "const:4:8"]]
+ 00aacb94 ["CALL", null, ["callee:00418c38:8"]]
- 00aacb50 bytes 3ab0e597
+ 00aacb94 bytes 29b0e597
- 00aacb4c ["COPY", "tmp:0:8", ["const:303:8"]]
- 00aacb4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aacb4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aacb4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aacb90 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00aacb90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aacb90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aacb90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aacb4c bytes 000c0c91
+ 00aacb90 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-151fccb1d47173748fe7c4f69b249203"></a>

### [`00aacce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacce4.md) → [`00aacd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacd28.md) FUN_00aacd28

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00aacd4c",
      "incomplete_value": false,
      "site": "00aacd50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aacd08",
      "incomplete_value": false,
      "site": "00aacd0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:288:8"
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
      "00aacd50",
      "DATA",
      [
        "storage",
        "00c0f288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aacd50",
      "DATA",
      [
        "storage",
        "00c0f2d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aaccf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacce4.md#insn-00aaccf8) · [`00aacd08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacce4.md#insn-00aacd08)
- 新版 `00aacd3c`（命令位置の公開資料なし） · `00aacd4c`（命令位置の公開資料なし）

~~~diff
- 00aaccf8 ["INT_ADD", "register:40f0:8", ["const:aaccf8:8", "const:4:8"]]
- 00aaccf8 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aacd3c ["INT_ADD", "register:40f0:8", ["const:aacd3c:8", "const:4:8"]]
+ 00aacd3c ["CALL", null, ["callee:00bdb040:8"]]
- 00aaccf8 bytes beb80494
+ 00aacd3c bytes c1b80494
- 00aacd08 ["COPY", "tmp:0:8", ["const:288:8"]]
- 00aacd08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aacd08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aacd08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aacd4c ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 00aacd4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aacd4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aacd4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aacd08 bytes 08210a91
+ 00aacd4c bytes 08610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5abbee045b3e7325eca4e91fc4f91521"></a>

### [`00aacd24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacd24.md) → [`00aacd68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacd68.md) FUN_00aacd68

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aacd6c",
      "incomplete_value": false,
      "site": "00aacd70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aacd28",
      "incomplete_value": false,
      "site": "00aacd2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:288:8"
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
      "00aacd70",
      "DATA",
      [
        "storage",
        "00c0f288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aacd70",
      "DATA",
      [
        "storage",
        "00c0f2d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aacd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacd24.md#insn-00aacd28)
- 新版 `00aacd6c`（命令位置の公開資料なし）

~~~diff
- 00aacd28 ["COPY", "tmp:0:8", ["const:288:8"]]
- 00aacd28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aacd28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aacd28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aacd6c ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 00aacd6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aacd6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aacd6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aacd28 bytes 08210a91
+ 00aacd6c bytes 08610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28eb40b501444b2c8e47a37632630537"></a>

### [`00aacd4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacd4c.md) → [`00aacd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacd90.md) FUN_00aacd90

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 16件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.38% / 新版 94.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00aace78",
      "incomplete_value": true,
      "site": "00aace88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aace34",
      "incomplete_value": true,
      "site": "00aace44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:99:8"
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
      "definition_site": "00aacebc",
      "incomplete_value": false,
      "site": "00aacebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aace78",
      "incomplete_value": false,
      "site": "00aace78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "definition_site": "00aacf20",
      "incomplete_value": true,
      "site": "00aacf30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aacedc",
      "incomplete_value": true,
      "site": "00aaceec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:df5:8"
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
      "00aace78",
      "READ",
      [
        "storage",
        "00294099",
        null,
        "string"
      ]
    ],
    [
      "00aacebc",
      "DATA",
      [
        "storage",
        "00c0f2f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00aacf20",
      "READ",
      [
        "storage",
        "0029fdf5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aace78",
      "READ",
      [
        "storage",
        "0029400c",
        null,
        "string"
      ]
    ],
    [
      "00aacebc",
      "DATA",
      [
        "storage",
        "00c0f348",
        null,
        "undefined *"
      ]
    ],
    [
      "00aacf20",
      "READ",
      [
        "storage",
        "0029fe80",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aace00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacd4c.md#insn-00aace00) · [`00aacda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacd4c.md#insn-00aacda0) · [`00aacdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacd4c.md#insn-00aacdac)
- 新版 `00aace44`（命令位置の公開資料なし） · `00aacde4`（命令位置の公開資料なし） · `00aacdf0`（命令位置の公開資料なし）

~~~diff
- 00aace00 ["INT_ADD", "register:40f0:8", ["const:aace00:8", "const:4:8"]]
- 00aace00 ["CALL", null, ["callee:0081f580:8"]]
+ 00aace44 ["INT_ADD", "register:40f0:8", ["const:aace44:8", "const:4:8"]]
+ 00aace44 ["CALL", null, ["callee:0081f580:8"]]
- 00aace00 bytes e0c9f597
+ 00aace44 bytes cfc9f597
- 00aacda0 ["INT_ADD", "register:40f0:8", ["const:aacda0:8", "const:4:8"]]
- 00aacda0 ["CALL", null, ["ram:457e1c:8"]]
+ 00aacde4 ["INT_ADD", "register:40f0:8", ["const:aacde4:8", "const:4:8"]]
+ 00aacde4 ["CALL", null, ["ram:457e1c:8"]]
- 00aacda0 bytes 1face697
+ 00aacde4 bytes 0eace697
- 00aacdac ["INT_ADD", "register:40f0:8", ["const:aacdac:8", "const:4:8"]]
- 00aacdac ["CALL", null, ["callee:00459efc:8"]]
+ 00aacdf0 ["INT_ADD", "register:40f0:8", ["const:aacdf0:8", "const:4:8"]]
+ 00aacdf0 ["CALL", null, ["callee:00459efc:8"]]
- 00aacdac bytes 54b4e697
+ 00aacdf0 bytes 43b4e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1b18b0fbd4a05191ecbb220eba5ee10"></a>

### [`00aad170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad170.md) → [`00aad1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad1b4.md) FUN_00aad1b4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00aad1d8",
      "incomplete_value": false,
      "site": "00aad1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aad194",
      "incomplete_value": false,
      "site": "00aad198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "00aad1dc",
      "DATA",
      [
        "storage",
        "00c0f2f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aad1dc",
      "DATA",
      [
        "storage",
        "00c0f348",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aad184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad170.md#insn-00aad184) · [`00aad194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad170.md#insn-00aad194)
- 新版 `00aad1c8`（命令位置の公開資料なし） · `00aad1d8`（命令位置の公開資料なし）

~~~diff
- 00aad184 ["INT_ADD", "register:40f0:8", ["const:aad184:8", "const:4:8"]]
- 00aad184 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aad1c8 ["INT_ADD", "register:40f0:8", ["const:aad1c8:8", "const:4:8"]]
+ 00aad1c8 ["CALL", null, ["callee:00bdb040:8"]]
- 00aad184 bytes 9bb70494
+ 00aad1c8 bytes 9eb70494
- 00aad194 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 00aad194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aad194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aad194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aad1d8 ["COPY", "tmp:0:8", ["const:348:8"]]
+ 00aad1d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad1d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad1d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aad194 bytes 08e10b91
+ 00aad1d8 bytes 08210d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56df33d6b0e7f12382c10bb0fa997f37"></a>

### [`00aad1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad1b0.md) → [`00aad1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad1f4.md) FUN_00aad1f4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aad1f8",
      "incomplete_value": false,
      "site": "00aad1fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aad1b4",
      "incomplete_value": false,
      "site": "00aad1b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "00aad1fc",
      "DATA",
      [
        "storage",
        "00c0f2f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aad1fc",
      "DATA",
      [
        "storage",
        "00c0f348",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aad1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad1b0.md#insn-00aad1b4)
- 新版 `00aad1f8`（命令位置の公開資料なし）

~~~diff
- 00aad1b4 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 00aad1b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aad1b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aad1b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aad1f8 ["COPY", "tmp:0:8", ["const:348:8"]]
+ 00aad1f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad1f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad1f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aad1b4 bytes 08e10b91
+ 00aad1f8 bytes 08210d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbef69e6fd0d01140f5b9c346831097f"></a>

### [`00aad28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad28c.md) → [`00aad2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad2d0.md) FUN_00aad2d0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00aad2f4",
      "incomplete_value": false,
      "site": "00aad2f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aad2b0",
      "incomplete_value": false,
      "site": "00aad2b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "00aad2f8",
      "DATA",
      [
        "storage",
        "00c0f378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aad2f8",
      "DATA",
      [
        "storage",
        "00c0f3c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aad2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad28c.md#insn-00aad2a0) · [`00aad2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad28c.md#insn-00aad2b0)
- 新版 `00aad2e4`（命令位置の公開資料なし） · `00aad2f4`（命令位置の公開資料なし）

~~~diff
- 00aad2a0 ["INT_ADD", "register:40f0:8", ["const:aad2a0:8", "const:4:8"]]
- 00aad2a0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aad2e4 ["INT_ADD", "register:40f0:8", ["const:aad2e4:8", "const:4:8"]]
+ 00aad2e4 ["CALL", null, ["callee:00bdb040:8"]]
- 00aad2a0 bytes 54b70494
+ 00aad2e4 bytes 57b70494
- 00aad2b0 ["COPY", "tmp:0:8", ["const:378:8"]]
- 00aad2b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aad2b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aad2b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aad2f4 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 00aad2f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad2f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad2f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aad2b0 bytes 08e10d91
+ 00aad2f4 bytes 08210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b02ba3c1098e03c409e0b6073515b942"></a>

### [`00aad2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad2cc.md) → [`00aad310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad310.md) FUN_00aad310

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aad314",
      "incomplete_value": false,
      "site": "00aad318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aad2d0",
      "incomplete_value": false,
      "site": "00aad2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "00aad318",
      "DATA",
      [
        "storage",
        "00c0f378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aad318",
      "DATA",
      [
        "storage",
        "00c0f3c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aad2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad2cc.md#insn-00aad2d0)
- 新版 `00aad314`（命令位置の公開資料なし）

~~~diff
- 00aad2d0 ["COPY", "tmp:0:8", ["const:378:8"]]
- 00aad2d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aad2d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aad2d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aad314 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 00aad314 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad314 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad314 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aad2d0 bytes 08e10d91
+ 00aad314 bytes 08210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb86529d05f323e9a8b3fa50d0420175"></a>

### [`00aad3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad3a8.md) → [`00aad3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad3ec.md) FUN_00aad3ec

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
      "definition_site": "00aad410",
      "incomplete_value": false,
      "site": "00aad410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aad3cc",
      "incomplete_value": false,
      "site": "00aad3cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "00aad410",
      "DATA",
      [
        "storage",
        "00c0f408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aad410",
      "DATA",
      [
        "storage",
        "00c0f458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aad3bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad3a8.md#insn-00aad3bc) · [`00aad3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad3a8.md#insn-00aad3c8)
- 新版 `00aad400`（命令位置の公開資料なし） · `00aad40c`（命令位置の公開資料なし）

~~~diff
- 00aad3bc ["INT_ADD", "register:40f0:8", ["const:aad3bc:8", "const:4:8"]]
- 00aad3bc ["CALL", null, ["callee:00bdb040:8"]]
+ 00aad400 ["INT_ADD", "register:40f0:8", ["const:aad400:8", "const:4:8"]]
+ 00aad400 ["CALL", null, ["callee:00bdb040:8"]]
- 00aad3bc bytes 0db70494
+ 00aad400 bytes 10b70494
- 00aad3c8 ["COPY", "tmp:0:8", ["const:408:8"]]
- 00aad3c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aad3c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aad3c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aad40c ["COPY", "tmp:0:8", ["const:458:8"]]
+ 00aad40c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad40c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad40c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aad3c8 bytes 08211091
+ 00aad40c bytes 08611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2727fa4ab2d481d8e0ee66f1d41d39f"></a>

### [`00aad3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad3dc.md) → [`00aad420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad420.md) FUN_00aad420

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
      "definition_site": "00aad42c",
      "incomplete_value": false,
      "site": "00aad42c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aad3e8",
      "incomplete_value": false,
      "site": "00aad3e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "00aad42c",
      "DATA",
      [
        "storage",
        "00c0f408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aad42c",
      "DATA",
      [
        "storage",
        "00c0f458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aad3e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad3dc.md#insn-00aad3e4)
- 新版 `00aad428`（命令位置の公開資料なし）

~~~diff
- 00aad3e4 ["COPY", "tmp:0:8", ["const:408:8"]]
- 00aad3e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00aad3e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00aad3e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00aad428 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 00aad428 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00aad428 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00aad428 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00aad3e4 bytes 29211091
+ 00aad428 bytes 29611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f5cbe87ed709f738ac09d4ae69b65fc"></a>

### [`00aad46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad46c.md) → [`00aad4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad4b0.md) FUN_00aad4b0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00aad4d4",
      "incomplete_value": false,
      "site": "00aad4d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aad490",
      "incomplete_value": false,
      "site": "00aad494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "00aad4d8",
      "DATA",
      [
        "storage",
        "00c0f488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aad4d8",
      "DATA",
      [
        "storage",
        "00c0f4d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aad480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad46c.md#insn-00aad480) · [`00aad490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad46c.md#insn-00aad490)
- 新版 `00aad4c4`（命令位置の公開資料なし） · `00aad4d4`（命令位置の公開資料なし）

~~~diff
- 00aad480 ["INT_ADD", "register:40f0:8", ["const:aad480:8", "const:4:8"]]
- 00aad480 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aad4c4 ["INT_ADD", "register:40f0:8", ["const:aad4c4:8", "const:4:8"]]
+ 00aad4c4 ["CALL", null, ["callee:00bdb040:8"]]
- 00aad480 bytes dcb60494
+ 00aad4c4 bytes dfb60494
- 00aad490 ["COPY", "tmp:0:8", ["const:488:8"]]
- 00aad490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aad490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aad490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aad4d4 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 00aad4d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad4d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad4d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aad490 bytes 08211291
+ 00aad4d4 bytes 08611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccc4f7e2f033fc60cbe031778d03e9c7"></a>

### [`00aad4ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad4ac.md) → [`00aad4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad4f0.md) FUN_00aad4f0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aad4f4",
      "incomplete_value": false,
      "site": "00aad4f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aad4b0",
      "incomplete_value": false,
      "site": "00aad4b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "00aad4f8",
      "DATA",
      [
        "storage",
        "00c0f488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aad4f8",
      "DATA",
      [
        "storage",
        "00c0f4d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aad4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad4ac.md#insn-00aad4b0)
- 新版 `00aad4f4`（命令位置の公開資料なし）

~~~diff
- 00aad4b0 ["COPY", "tmp:0:8", ["const:488:8"]]
- 00aad4b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aad4b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aad4b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aad4f4 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 00aad4f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad4f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad4f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aad4b0 bytes 08211291
+ 00aad4f4 bytes 08611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fae1183187bd5ae9d5f4259850d8c24a"></a>

### [`00aad948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad948.md) → [`00aad98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad98c.md) FUN_00aad98c

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
      "definition_site": "00aad9ac",
      "incomplete_value": false,
      "site": "00aad9b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aad968",
      "incomplete_value": false,
      "site": "00aad96c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "00aad9b0",
      "DATA",
      [
        "storage",
        "00c0f508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aad9b0",
      "DATA",
      [
        "storage",
        "00c0f558",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aad95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad948.md#insn-00aad95c) · [`00aad968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad948.md#insn-00aad968)
- 新版 `00aad9a0`（命令位置の公開資料なし） · `00aad9ac`（命令位置の公開資料なし）

~~~diff
- 00aad95c ["INT_ADD", "register:40f0:8", ["const:aad95c:8", "const:4:8"]]
- 00aad95c ["CALL", null, ["callee:00bdb040:8"]]
+ 00aad9a0 ["INT_ADD", "register:40f0:8", ["const:aad9a0:8", "const:4:8"]]
+ 00aad9a0 ["CALL", null, ["callee:00bdb040:8"]]
- 00aad95c bytes a5b50494
+ 00aad9a0 bytes a8b50494
- 00aad968 ["COPY", "tmp:0:8", ["const:508:8"]]
- 00aad968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aad968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aad968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aad9ac ["COPY", "tmp:0:8", ["const:558:8"]]
+ 00aad9ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad9ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad9ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aad968 bytes 08211491
+ 00aad9ac bytes 08611591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eee512b2b77c1f1b93dcff36dc9b9e49"></a>

### [`00aad980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad980.md) → [`00aad9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aad9c4.md) FUN_00aad9c4

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
      "definition_site": "00aad9c8",
      "incomplete_value": false,
      "site": "00aad9cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aad984",
      "incomplete_value": false,
      "site": "00aad988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "00aad9cc",
      "DATA",
      [
        "storage",
        "00c0f508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aad9cc",
      "DATA",
      [
        "storage",
        "00c0f558",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aad984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad980.md#insn-00aad984)
- 新版 `00aad9c8`（命令位置の公開資料なし）

~~~diff
- 00aad984 ["COPY", "tmp:0:8", ["const:508:8"]]
- 00aad984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aad984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aad984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aad9c8 ["COPY", "tmp:0:8", ["const:558:8"]]
+ 00aad9c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad9c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aad9c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aad984 bytes 08211491
+ 00aad9c8 bytes 08611591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d77f5225252b787b3d5e86a5bd34b2bf"></a>

### [`00aada84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aada84.md) → [`00aadac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadac8.md) FUN_00aadac8

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
      "definition_site": "00aadae8",
      "incomplete_value": false,
      "site": "00aadaec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aadaa4",
      "incomplete_value": false,
      "site": "00aadaa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:588:8"
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
      "00aadaec",
      "DATA",
      [
        "storage",
        "00c0f588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aadaec",
      "DATA",
      [
        "storage",
        "00c0f5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aada98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aada84.md#insn-00aada98) · [`00aadaa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aada84.md#insn-00aadaa4)
- 新版 `00aadadc`（命令位置の公開資料なし） · `00aadae8`（命令位置の公開資料なし）

~~~diff
- 00aada98 ["INT_ADD", "register:40f0:8", ["const:aada98:8", "const:4:8"]]
- 00aada98 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aadadc ["INT_ADD", "register:40f0:8", ["const:aadadc:8", "const:4:8"]]
+ 00aadadc ["CALL", null, ["callee:00bdb040:8"]]
- 00aada98 bytes 56b50494
+ 00aadadc bytes 59b50494
- 00aadaa4 ["COPY", "tmp:0:8", ["const:588:8"]]
- 00aadaa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aadaa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aadaa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aadae8 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00aadae8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aadae8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aadae8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aadaa4 bytes 08211691
+ 00aadae8 bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91667cd1a58ee911ae537db645a8132a"></a>

### [`00aadabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadabc.md) → [`00aadb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadb00.md) FUN_00aadb00

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
      "definition_site": "00aadb04",
      "incomplete_value": false,
      "site": "00aadb08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aadac0",
      "incomplete_value": false,
      "site": "00aadac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:588:8"
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
      "00aadb08",
      "DATA",
      [
        "storage",
        "00c0f588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aadb08",
      "DATA",
      [
        "storage",
        "00c0f5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aadac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadabc.md#insn-00aadac0)
- 新版 `00aadb04`（命令位置の公開資料なし）

~~~diff
- 00aadac0 ["COPY", "tmp:0:8", ["const:588:8"]]
- 00aadac0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aadac0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aadac0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aadb04 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00aadb04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aadb04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aadb04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aadac0 bytes 08211691
+ 00aadb04 bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28bf7cd4a5d7ef20ce17d2edaeb9e78c"></a>

### [`00aadc78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadc78.md) → [`00aadcbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadcbc.md) _INIT_246

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
      "definition_site": "00aadcf8",
      "incomplete_value": true,
      "site": "00aadd14",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aadcb4",
      "incomplete_value": true,
      "site": "00aadcd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aadd1c",
      "incomplete_value": true,
      "site": "00aadd38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aadcd8",
      "incomplete_value": true,
      "site": "00aadcf4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aadd3c",
      "incomplete_value": true,
      "site": "00aadd58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aadcf8",
      "incomplete_value": true,
      "site": "00aadd14",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00aadcf8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00aadd1c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00aadd3c",
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
      "00aadcf8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00aadd1c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00aadd3c",
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

- 旧版 [`00aadcb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadc78.md#insn-00aadcb0) · [`00aaddd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadc78.md#insn-00aaddd8) · [`00aadeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadc78.md#insn-00aadeac)
- 新版 `00aadcf4`（命令位置の公開資料なし） · `00aade1c`（命令位置の公開資料なし） · `00aadef0`（命令位置の公開資料なし）

~~~diff
- 00aadcb0 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00aadcb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00aadcb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00aadcb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00aadcf4 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00aadcf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00aadcf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00aadcf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00aadcb0 bytes 29750b91
+ 00aadcf4 bytes 29dd0d91
- 00aaddd8 ["INT_ADD", "register:40f0:8", ["const:aaddd8:8", "const:4:8"]]
- 00aaddd8 ["CALL", null, ["callee:00418cb8:8"]]
+ 00aade1c ["INT_ADD", "register:40f0:8", ["const:aade1c:8", "const:4:8"]]
+ 00aade1c ["CALL", null, ["callee:00418cb8:8"]]
- 00aaddd8 bytes b8abe597
+ 00aade1c bytes a7abe597
- 00aadeac ["INT_ADD", "register:40f0:8", ["const:aadeac:8", "const:4:8"]]
- 00aadeac ["CALL", null, ["callee:00bdafe0:8"]]
+ 00aadef0 ["INT_ADD", "register:40f0:8", ["const:aadef0:8", "const:4:8"]]
+ 00aadef0 ["CALL", null, ["callee:00bdafe0:8"]]
- 00aadeac bytes 39b40494
+ 00aadef0 bytes 3cb40494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ba69c0c8993b916afbd3c7f6f892f16"></a>

### [`00aae008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aae008.md) → [`00aae04c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aae04c.md) FUN_00aae04c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0076e98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076e/0076e98c.md) [`00776270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00776/00776270.md) [`00aae008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aae008.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`005b5878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b5878.md) [`0065ec80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ec80.md)
- 新版 呼出元 3件 [`0076e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e98c.md) [`00776270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00776/00776270.md) [`00aae04c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aae04c.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`005b5878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5878.md) [`0065ec80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065ec80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.88% / 新版 94.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00aae2bc",
      "incomplete_value": true,
      "site": "00aae2cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aae278",
      "incomplete_value": true,
      "site": "00aae288",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e98:8"
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
      "definition_site": "00aae2c0",
      "incomplete_value": true,
      "site": "00aae2d0",
      "value": [
        "LOAD",
        "16",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aae27c",
      "incomplete_value": true,
      "site": "00aae28c",
      "value": [
        "LOAD",
        "16",
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
                "const:f:8"
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
      "definition_site": "00aae328",
      "incomplete_value": true,
      "site": "00aae338",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9bd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aae2e4",
      "incomplete_value": true,
      "site": "00aae2f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:932:8"
              ]
            ]
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
      "00aae260",
      "PARAM",
      [
        "storage",
        "0029c8c1",
        null,
        "string"
      ]
    ],
    [
      "00aae2bc",
      "READ",
      [
        "storage",
        "00293e98",
        null,
        "string"
      ]
    ],
    [
      "00aae2c0",
      "READ",
      [
        "storage",
        "00293ea7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aae260",
      "PARAM",
      [
        "storage",
        "0029c94c",
        null,
        "string"
      ]
    ],
    [
      "00aae2bc",
      "READ",
      [
        "storage",
        "00293e0b",
        null,
        "string"
      ]
    ],
    [
      "00aae2c0",
      "READ",
      [
        "storage",
        "00293e1a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aae338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aae008.md#insn-00aae338) · [`00aae06c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aae008.md#insn-00aae06c) · [`00aae0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aae008.md#insn-00aae0f4)
- 新版 `00aae37c`（命令位置の公開資料なし） · `00aae0b0`（命令位置の公開資料なし） · `00aae138`（命令位置の公開資料なし）

~~~diff
- 00aae338 ["COPY", "tmp:0:8", ["const:7a9:8"]]
- 00aae338 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00aae338 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00aae338 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00aae37c ["COPY", "tmp:0:8", ["const:834:8"]]
+ 00aae37c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00aae37c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00aae37c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00aae338 bytes 4aa51e91
+ 00aae37c bytes 4ad12091
- 00aae06c ["INT_ADD", "register:40f0:8", ["const:aae06c:8", "const:4:8"]]
- 00aae06c ["CALL", null, ["callee:0070db34:8"]]
+ 00aae0b0 ["INT_ADD", "register:40f0:8", ["const:aae0b0:8", "const:4:8"]]
+ 00aae0b0 ["CALL", null, ["callee:0070db34:8"]]
- 00aae06c bytes b27ef197
+ 00aae0b0 bytes a17ef197
- 00aae0f4 ["INT_ADD", "register:40f0:8", ["const:aae0f4:8", "const:4:8"]]
- 00aae0f4 ["CALL", null, ["callee:0081f580:8"]]
+ 00aae138 ["INT_ADD", "register:40f0:8", ["const:aae138:8", "const:4:8"]]
+ 00aae138 ["CALL", null, ["callee:0081f580:8"]]
- 00aae0f4 bytes 23c5f597
+ 00aae138 bytes 12c5f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e08938ae6e01feda0cfe7c7dd1f1d78"></a>

### [`00aae6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aae6a8.md) → [`00aae6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aae6ec.md) _INIT_247

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 70.97% / 新版 68.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00aae728",
      "incomplete_value": true,
      "site": "00aae744",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aae6e4",
      "incomplete_value": true,
      "site": "00aae700",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aae74c",
      "incomplete_value": true,
      "site": "00aae768",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aae708",
      "incomplete_value": true,
      "site": "00aae724",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aae76c",
      "incomplete_value": true,
      "site": "00aae788",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aae728",
      "incomplete_value": true,
      "site": "00aae744",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00aae728",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00aae74c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00aae76c",
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
      "00aae728",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00aae74c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00aae76c",
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

- 旧版 [`00aae6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aae6a8.md#insn-00aae6e0) · [`00aae808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aae6a8.md#insn-00aae808) · [`00aae8dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aae6a8.md#insn-00aae8dc)
- 新版 `00aae724`（命令位置の公開資料なし） · `00aae84c`（命令位置の公開資料なし） · `00aae920`（命令位置の公開資料なし）

~~~diff
- 00aae6e0 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00aae6e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00aae6e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00aae6e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00aae724 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00aae724 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00aae724 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00aae724 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00aae6e0 bytes 29750b91
+ 00aae724 bytes 29dd0d91
- 00aae808 ["INT_ADD", "register:40f0:8", ["const:aae808:8", "const:4:8"]]
- 00aae808 ["CALL", null, ["callee:00418cb8:8"]]
+ 00aae84c ["INT_ADD", "register:40f0:8", ["const:aae84c:8", "const:4:8"]]
+ 00aae84c ["CALL", null, ["callee:00418cb8:8"]]
- 00aae808 bytes 2ca9e597
+ 00aae84c bytes 1ba9e597
- 00aae8dc ["INT_ADD", "register:40f0:8", ["const:aae8dc:8", "const:4:8"]]
- 00aae8dc ["CALL", null, ["callee:00bdafe0:8"]]
+ 00aae920 ["INT_ADD", "register:40f0:8", ["const:aae920:8", "const:4:8"]]
+ 00aae920 ["CALL", null, ["callee:00bdafe0:8"]]
- 00aae8dc bytes adb10494
+ 00aae920 bytes b0b10494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f761f0f0575424f035f06f784ced42f0"></a>

### [`00aaea38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaea38.md) → [`00aaea7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaea7c.md) FUN_00aaea7c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0076e98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076e/0076e98c.md) [`00aaeb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeb80.md) · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046fdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fdf4.md) [`00971a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971a68.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 2件 [`0076e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e98c.md) [`00aaebc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaebc4.md) · 呼出先 7件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046fdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fdf4.md) [`00971a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/00971a68.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00aaeabc",
      "incomplete_value": true,
      "site": "00aaead0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e91:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aaea78",
      "incomplete_value": true,
      "site": "00aaea8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e06:8"
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
      "definition_site": "00aaeabc",
      "incomplete_value": true,
      "site": "00aaead0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00aaea78",
      "incomplete_value": true,
      "site": "00aaea8c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00aaead4",
      "incomplete_value": true,
      "site": "00aaead4",
      "value": [
        "LOAD",
        "8",
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
                "const:1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aaea90",
      "incomplete_value": true,
      "site": "00aaea90",
      "value": [
        "LOAD",
        "8",
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
                "const:1d:8"
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
      "00aaeabc",
      "READ",
      [
        "storage",
        "0029fe06",
        null,
        "string"
      ]
    ],
    [
      "00aaeabc",
      "READ",
      [
        "storage",
        "0029fe16",
        null,
        "string"
      ]
    ],
    [
      "00aaeac4",
      "READ",
      [
        "storage",
        "0029fe23",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aaeabc",
      "READ",
      [
        "storage",
        "0029fe91",
        null,
        "string"
      ]
    ],
    [
      "00aaeabc",
      "READ",
      [
        "storage",
        "0029fea1",
        null,
        "string"
      ]
    ],
    [
      "00aaeac4",
      "READ",
      [
        "storage",
        "0029feae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aaeaa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaea38.md#insn-00aaeaa8) · [`00aaea68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaea38.md#insn-00aaea68) · [`00aaea70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaea38.md#insn-00aaea70)
- 新版 `00aaeaec`（命令位置の公開資料なし） · `00aaeaac`（命令位置の公開資料なし） · `00aaeab4`（命令位置の公開資料なし）

~~~diff
- 00aaeaa8 ["INT_ADD", "register:40f0:8", ["const:aaeaa8:8", "const:4:8"]]
- 00aaeaa8 ["CALL", null, ["callee:00bdb340:8"]]
+ 00aaeaec ["INT_ADD", "register:40f0:8", ["const:aaeaec:8", "const:4:8"]]
+ 00aaeaec ["CALL", null, ["callee:00bdb340:8"]]
- 00aaeaa8 bytes 12b20494
+ 00aaeaec bytes 15b20494
- 00aaea68 ["INT_ADD", "register:40f0:8", ["const:aaea68:8", "const:4:8"]]
- 00aaea68 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aaeaac ["INT_ADD", "register:40f0:8", ["const:aaeaac:8", "const:4:8"]]
+ 00aaeaac ["CALL", null, ["callee:00bdb040:8"]]
- 00aaea68 bytes 62b10494
+ 00aaeaac bytes 65b10494
- 00aaea70 ["COPY", "tmp:0:8", ["const:e06:8"]]
- 00aaea70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aaea70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aaea70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aaeab4 ["COPY", "tmp:0:8", ["const:e91:8"]]
+ 00aaeab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aaeab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aaeab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aaea70 bytes 08193891
+ 00aaeab4 bytes 08453a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbc6bd0e6253d34e1668bc1fcafba5d5"></a>

### [`00aaeb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeb80.md) → [`00aaebc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaebc4.md) FUN_00aaebc4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0076dd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076d/0076dd00.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`00436518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436518.md) [`005742c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005742c4.md) [`0057462c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057462c.md)
- 新版 呼出元 1件 [`0076dd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076d/0076dd00.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`00436518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436518.md) [`005742c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005742c4.md) [`0057462c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057462c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00aaec08",
      "incomplete_value": false,
      "site": "00aaec14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aaebc4",
      "incomplete_value": false,
      "site": "00aaebd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "definition_site": "00aaecc4",
      "incomplete_value": true,
      "site": "00aaecc8",
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
      "definition_site": "00aaec80",
      "incomplete_value": true,
      "site": "00aaec84",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00aaecc0",
      "incomplete_value": true,
      "site": "00aaeccc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aaec7c",
      "incomplete_value": true,
      "site": "00aaec88",
      "value": [
        "LOAD",
        "8",
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
      "00aaec14",
      "DATA",
      [
        "storage",
        "00bf0668",
        null,
        "pointer"
      ]
    ],
    [
      "00aaec50",
      "DATA",
      [
        "storage",
        "00be6750",
        null,
        "pointer"
      ]
    ],
    [
      "00aaec9c",
      "READ",
      [
        "storage",
        "00be6758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aaec14",
      "DATA",
      [
        "storage",
        "00bf06b8",
        null,
        "pointer"
      ]
    ],
    [
      "00aaec50",
      "DATA",
      [
        "storage",
        "00be67a0",
        null,
        "pointer"
      ]
    ],
    [
      "00aaec9c",
      "READ",
      [
        "storage",
        "00be67a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aaec44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeb80.md#insn-00aaec44) · [`00aaecc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeb80.md#insn-00aaecc8) · [`00aaecd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeb80.md#insn-00aaecd4)
- 新版 `00aaec88`（命令位置の公開資料なし） · `00aaed0c`（命令位置の公開資料なし） · `00aaed18`（命令位置の公開資料なし）

~~~diff
- 00aaec44 ["INT_ADD", "register:40f0:8", ["const:aaec44:8", "const:4:8"]]
- 00aaec44 ["CALL", null, ["callee:0057462c:8"]]
+ 00aaec88 ["INT_ADD", "register:40f0:8", ["const:aaec88:8", "const:4:8"]]
+ 00aaec88 ["CALL", null, ["callee:0057462c:8"]]
- 00aaec44 bytes 7a16eb97
+ 00aaec88 bytes 6916eb97
- 00aaecc8 ["INT_ADD", "register:40f0:8", ["const:aaecc8:8", "const:4:8"]]
- 00aaecc8 ["CALL", null, ["callee:00bdb3a0:8"]]
+ 00aaed0c ["INT_ADD", "register:40f0:8", ["const:aaed0c:8", "const:4:8"]]
+ 00aaed0c ["CALL", null, ["callee:00bdb3a0:8"]]
- 00aaecc8 bytes a2b10494
+ 00aaed0c bytes a5b10494
- 00aaecd4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d80:8"]]
- 00aaecd4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aaed18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd0:8"]]
+ 00aaed18 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00aaecd4 bytes 94c246f9
+ 00aaed18 bytes 94ea46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cb5ce91c2bd8cbf54d36c0e09220b84"></a>

### [`00aaf180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf180.md) → [`00aaf1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf1c4.md) _INIT_248

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
      "definition_site": "00aaf200",
      "incomplete_value": true,
      "site": "00aaf21c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aaf1bc",
      "incomplete_value": true,
      "site": "00aaf1d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aaf224",
      "incomplete_value": true,
      "site": "00aaf240",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aaf1e0",
      "incomplete_value": true,
      "site": "00aaf1fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aaf244",
      "incomplete_value": true,
      "site": "00aaf260",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aaf200",
      "incomplete_value": true,
      "site": "00aaf21c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00aaf200",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00aaf224",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00aaf244",
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
      "00aaf200",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00aaf224",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00aaf244",
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

- 旧版 [`00aaf1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf180.md#insn-00aaf1b8) · [`00aaf2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf180.md#insn-00aaf2e0) · [`00aaf3b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf180.md#insn-00aaf3b4)
- 新版 `00aaf1fc`（命令位置の公開資料なし） · `00aaf324`（命令位置の公開資料なし） · `00aaf3f8`（命令位置の公開資料なし）

~~~diff
- 00aaf1b8 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00aaf1b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00aaf1b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00aaf1b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00aaf1fc ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00aaf1fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00aaf1fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00aaf1fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00aaf1b8 bytes 29750b91
+ 00aaf1fc bytes 29dd0d91
- 00aaf2e0 ["INT_ADD", "register:40f0:8", ["const:aaf2e0:8", "const:4:8"]]
- 00aaf2e0 ["CALL", null, ["callee:00418cb8:8"]]
+ 00aaf324 ["INT_ADD", "register:40f0:8", ["const:aaf324:8", "const:4:8"]]
+ 00aaf324 ["CALL", null, ["callee:00418cb8:8"]]
- 00aaf2e0 bytes 76a6e597
+ 00aaf324 bytes 65a6e597
- 00aaf3b4 ["INT_ADD", "register:40f0:8", ["const:aaf3b4:8", "const:4:8"]]
- 00aaf3b4 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00aaf3f8 ["INT_ADD", "register:40f0:8", ["const:aaf3f8:8", "const:4:8"]]
+ 00aaf3f8 ["CALL", null, ["callee:00bdafe0:8"]]
- 00aaf3b4 bytes f7ae0494
+ 00aaf3f8 bytes faae0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8864e656bc692672001fea61859dfb14"></a>

### [`00aaf6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf6f8.md) → [`00aaf73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf73c.md) FUN_00aaf73c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 90.73% / 新版 90.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00aaf774",
      "incomplete_value": false,
      "site": "00aaf77c",
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
    "old": {
      "definition_site": "00aaf730",
      "incomplete_value": false,
      "site": "00aaf738",
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
            "const:d28:8"
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
      "definition_site": "00aaf790",
      "incomplete_value": true,
      "site": "00aaf79c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b63:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aaf74c",
      "incomplete_value": true,
      "site": "00aaf758",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ac9:8"
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
      "definition_site": "00aaf8f4",
      "incomplete_value": true,
      "site": "00aaf8f8",
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
      "definition_site": "00aaf8b0",
      "incomplete_value": true,
      "site": "00aaf8b4",
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
      "00aaf77c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00aaf790",
      "READ",
      [
        "storage",
        "002a8ac9",
        null,
        "string"
      ]
    ],
    [
      "00aaf8e4",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00aaf77c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00aaf790",
      "READ",
      [
        "storage",
        "002a8b63",
        null,
        "string"
      ]
    ],
    [
      "00aaf8e4",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aaf8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf6f8.md#insn-00aaf8f8) · [`00aaf728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf6f8.md#insn-00aaf728) · [`00aaf730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf6f8.md#insn-00aaf730)
- 新版 `00aaf93c`（命令位置の公開資料なし） · `00aaf76c`（命令位置の公開資料なし） · `00aaf774`（命令位置の公開資料なし）

~~~diff
- 00aaf8f8 ["INT_ADD", "register:40f0:8", ["const:aaf8f8:8", "const:4:8"]]
- 00aaf8f8 ["CALL", null, ["callee:00bdb160:8"]]
+ 00aaf93c ["INT_ADD", "register:40f0:8", ["const:aaf93c:8", "const:4:8"]]
+ 00aaf93c ["CALL", null, ["callee:00bdb160:8"]]
- 00aaf8f8 bytes 06ae0494
+ 00aaf93c bytes 09ae0494
- 00aaf728 ["INT_ADD", "register:40f0:8", ["const:aaf728:8", "const:4:8"]]
- 00aaf728 ["CALL", null, ["callee:00464f48:8"]]
+ 00aaf76c ["INT_ADD", "register:40f0:8", ["const:aaf76c:8", "const:4:8"]]
+ 00aaf76c ["CALL", null, ["callee:00464f48:8"]]
- 00aaf728 bytes 08d6e697
+ 00aaf76c bytes f7d5e697
- 00aaf730 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00aaf730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aaf730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aaf730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aaf774 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00aaf774 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aaf774 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aaf774 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aaf730 bytes 08a13491
+ 00aaf774 bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0d3c5b475bfcb6661027c6aa5652565"></a>

### [`00ab0e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e38.md) → [`00ab0e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab0/00ab0e7c.md) FUN_00ab0e7c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00aaf510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf510.md) [`00aaf9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf9b8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00aaf554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf554.md) [`00aaf9fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf9fc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00ab0e88",
      "incomplete_value": false,
      "site": "00ab0e8c",
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
    "old": {
      "definition_site": "00ab0e44",
      "incomplete_value": false,
      "site": "00ab0e48",
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
            "const:303:8"
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
      "00ab0e88",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ab0e88",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ab0e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e38.md#insn-00ab0e48) · [`00ab0e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e38.md#insn-00ab0e44)
- 新版 `00ab0e8c`（命令位置の公開資料なし） · `00ab0e88`（命令位置の公開資料なし）

~~~diff
- 00ab0e48 ["INT_ADD", "register:40f0:8", ["const:ab0e48:8", "const:4:8"]]
- 00ab0e48 ["CALL", null, ["callee:00418c38:8"]]
+ 00ab0e8c ["INT_ADD", "register:40f0:8", ["const:ab0e8c:8", "const:4:8"]]
+ 00ab0e8c ["CALL", null, ["callee:00418c38:8"]]
- 00ab0e48 bytes 7c9fe597
+ 00ab0e8c bytes 6b9fe597
- 00ab0e44 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00ab0e44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ab0e44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ab0e44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ab0e88 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00ab0e88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ab0e88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ab0e88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ab0e44 bytes 000c0c91
+ 00ab0e88 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bea596bbc2c7068a535f487d6780888f"></a>

### [`00ab0e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e4c.md) → [`00ab0e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab0/00ab0e90.md) FUN_00ab0e90

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00aafb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aafb1c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`00aafb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aafb60.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "00ab0e9c",
      "incomplete_value": false,
      "site": "00ab0ea0",
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
    "old": {
      "definition_site": "00ab0e58",
      "incomplete_value": false,
      "site": "00ab0e5c",
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
            "const:303:8"
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
      "00ab0e9c",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ab0e9c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ab0e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e4c.md#insn-00ab0e5c) · [`00ab0e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e4c.md#insn-00ab0e58)
- 新版 `00ab0ea0`（命令位置の公開資料なし） · `00ab0e9c`（命令位置の公開資料なし）

~~~diff
- 00ab0e5c ["INT_ADD", "register:40f0:8", ["const:ab0e5c:8", "const:4:8"]]
- 00ab0e5c ["CALL", null, ["callee:0041fdf0:8"]]
+ 00ab0ea0 ["INT_ADD", "register:40f0:8", ["const:ab0ea0:8", "const:4:8"]]
+ 00ab0ea0 ["CALL", null, ["callee:0041fdf0:8"]]
- 00ab0e5c bytes e5bbe597
+ 00ab0ea0 bytes d4bbe597
- 00ab0e58 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00ab0e58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ab0e58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ab0e58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ab0e9c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00ab0e9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ab0e9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ab0e9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ab0e58 bytes 000c0c91
+ 00ab0e9c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db842b137a0fe49f5ecff4a9d0a2fa19"></a>

### [`00ab0e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e60.md) → [`00ab0ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab0/00ab0ea4.md) _INIT_249

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
      "definition_site": "00ab0ee0",
      "incomplete_value": true,
      "site": "00ab0efc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ab0e9c",
      "incomplete_value": true,
      "site": "00ab0eb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ab0f04",
      "incomplete_value": true,
      "site": "00ab0f20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ab0ec0",
      "incomplete_value": true,
      "site": "00ab0edc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ab0f24",
      "incomplete_value": true,
      "site": "00ab0f40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ab0ee0",
      "incomplete_value": true,
      "site": "00ab0efc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00ab0ee0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00ab0f04",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00ab0f24",
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
      "00ab0ee0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00ab0f04",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00ab0f24",
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

- 旧版 [`00ab0e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e60.md#insn-00ab0e98) · [`00ab0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e60.md#insn-00ab0fc0) · [`00ab1094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e60.md#insn-00ab1094)
- 新版 `00ab0edc`（命令位置の公開資料なし） · `00ab1004`（命令位置の公開資料なし） · `00ab10d8`（命令位置の公開資料なし）

~~~diff
- 00ab0e98 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00ab0e98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ab0e98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ab0e98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ab0edc ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00ab0edc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ab0edc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ab0edc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ab0e98 bytes 29750b91
+ 00ab0edc bytes 29dd0d91
- 00ab0fc0 ["INT_ADD", "register:40f0:8", ["const:ab0fc0:8", "const:4:8"]]
- 00ab0fc0 ["CALL", null, ["callee:00418cb8:8"]]
+ 00ab1004 ["INT_ADD", "register:40f0:8", ["const:ab1004:8", "const:4:8"]]
+ 00ab1004 ["CALL", null, ["callee:00418cb8:8"]]
- 00ab0fc0 bytes 3e9fe597
+ 00ab1004 bytes 2d9fe597
- 00ab1094 ["INT_ADD", "register:40f0:8", ["const:ab1094:8", "const:4:8"]]
- 00ab1094 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00ab10d8 ["INT_ADD", "register:40f0:8", ["const:ab10d8:8", "const:4:8"]]
+ 00ab10d8 ["CALL", null, ["callee:00bdafe0:8"]]
- 00ab1094 bytes bfa70494
+ 00ab10d8 bytes c2a70494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-068e1a585f47f37f21f95dea8ce05215"></a>

### [`00ab11f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab11f0.md) → [`00ab1234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1234.md) FUN_00ab1234

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 137件 [`0044a248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a248.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md) [`00458038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00458/00458038.md) [`004662ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00466/004662ec.md) · 呼出先 20件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0044df7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044df7c.md) [`0044e84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044e/0044e84c.md) [`0044ea58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044e/0044ea58.md) [`0045e558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e558.md)
- 新版 呼出元 138件 [`0044a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a248.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) [`00458038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458038.md) [`004662ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004662ec.md) · 呼出先 20件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0044df7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044df7c.md) [`0044e84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e84c.md) [`0044ea58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ea58.md) [`0045e558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.95% / 新版 73.95%

CFGの説明率　旧版 59.35% / 新版 59.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 15件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab11f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab11f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab11f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ab11f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ab11f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ab11fc",
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
      "00ab1238",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00ab123c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ab1240",
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

- 旧版 [`00ab11f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab11f0.md#insn-00ab11f4) · [`00ab11f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab11f0.md#insn-00ab11f8) · [`00ab11fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab11f0.md#insn-00ab11fc)

~~~diff
- 00ab11f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ab11f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ab11f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00ab11f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ab11f4 bytes fd7b10a9
- 00ab11f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:110:8"]]
- 00ab11f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 00ab11f8 bytes fc8b00f9
- 00ab11fc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00ab11fc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00ab11fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00ab11fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ab11fc bytes fa6712a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a25f9731e4fb7a00d58abe6a466a669d"></a>

### [`00ab198c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab198c.md) → [`00ab19d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab19d0.md) _INIT_250

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
      "definition_site": "00ab1a0c",
      "incomplete_value": true,
      "site": "00ab1a28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ab19c8",
      "incomplete_value": true,
      "site": "00ab19e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ab1a30",
      "incomplete_value": true,
      "site": "00ab1a4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ab19ec",
      "incomplete_value": true,
      "site": "00ab1a08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ab1a50",
      "incomplete_value": true,
      "site": "00ab1a6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ab1a0c",
      "incomplete_value": true,
      "site": "00ab1a28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00ab1a0c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00ab1a30",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00ab1a50",
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
      "00ab1a0c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00ab1a30",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00ab1a50",
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

- 旧版 [`00ab19c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab198c.md#insn-00ab19c4) · [`00ab1aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab198c.md#insn-00ab1aec) · [`00ab1bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab198c.md#insn-00ab1bc0)
- 新版 `00ab1a08`（命令位置の公開資料なし） · `00ab1b30`（命令位置の公開資料なし） · `00ab1c04`（命令位置の公開資料なし）

~~~diff
- 00ab19c4 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00ab19c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ab19c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ab19c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ab1a08 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00ab1a08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ab1a08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ab1a08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ab19c4 bytes 29750b91
+ 00ab1a08 bytes 29dd0d91
- 00ab1aec ["INT_ADD", "register:40f0:8", ["const:ab1aec:8", "const:4:8"]]
- 00ab1aec ["CALL", null, ["callee:00418cb8:8"]]
+ 00ab1b30 ["INT_ADD", "register:40f0:8", ["const:ab1b30:8", "const:4:8"]]
+ 00ab1b30 ["CALL", null, ["callee:00418cb8:8"]]
- 00ab1aec bytes 739ce597
+ 00ab1b30 bytes 629ce597
- 00ab1bc0 ["INT_ADD", "register:40f0:8", ["const:ab1bc0:8", "const:4:8"]]
- 00ab1bc0 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00ab1c04 ["INT_ADD", "register:40f0:8", ["const:ab1c04:8", "const:4:8"]]
+ 00ab1c04 ["CALL", null, ["callee:00bdafe0:8"]]
- 00ab1bc0 bytes f4a40494
+ 00ab1c04 bytes f7a40494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db55ad88bb2b561bb7447aa2bca134b8"></a>

### [`00ab1e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md) → [`00ab1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1ecc.md) FUN_00ab1ecc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 24件 [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 24件 [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.93% / 新版 93.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 26件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ab1f48",
      "incomplete_value": false,
      "site": "00ab1f50",
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
    "old": {
      "definition_site": "00ab1f04",
      "incomplete_value": false,
      "site": "00ab1f0c",
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
            "const:d28:8"
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
      "definition_site": "00ab1fc8",
      "incomplete_value": true,
      "site": "00ab1fe0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dfa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ab1f84",
      "incomplete_value": true,
      "site": "00ab1f9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d6f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ab1fc8",
      "incomplete_value": true,
      "site": "00ab1fe0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00ab1f84",
      "incomplete_value": true,
      "site": "00ab1f9c",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ab1f50",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00ab1fc8",
      "READ",
      [
        "storage",
        "0029ed6f",
        null,
        "string"
      ]
    ],
    [
      "00ab1fc8",
      "READ",
      [
        "storage",
        "0029ed7f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ab1f50",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00ab1fc8",
      "READ",
      [
        "storage",
        "0029edfa",
        null,
        "string"
      ]
    ],
    [
      "00ab1fc8",
      "READ",
      [
        "storage",
        "0029ee0a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ab20c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md#insn-00ab20c0) · [`00ab2148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md#insn-00ab2148) · [`00ab229c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md#insn-00ab229c)
- 新版 `00ab2104`（命令位置の公開資料なし） · `00ab218c`（命令位置の公開資料なし） · `00ab22e0`（命令位置の公開資料なし）

~~~diff
- 00ab20c0 ["INT_ADD", "register:40f0:8", ["const:ab20c0:8", "const:4:8"]]
- 00ab20c0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00ab2104 ["INT_ADD", "register:40f0:8", ["const:ab2104:8", "const:4:8"]]
+ 00ab2104 ["CALL", null, ["callee:00bdb060:8"]]
- 00ab20c0 bytes d4a30494
+ 00ab2104 bytes d7a30494
- 00ab2148 ["INT_ADD", "register:40f0:8", ["const:ab2148:8", "const:4:8"]]
- 00ab2148 ["CALL", null, ["callee:0046ff30:8"]]
+ 00ab218c ["INT_ADD", "register:40f0:8", ["const:ab218c:8", "const:4:8"]]
+ 00ab218c ["CALL", null, ["callee:0046ff30:8"]]
- 00ab2148 bytes 7af7e697
+ 00ab218c bytes 69f7e697
- 00ab229c ["INT_ADD", "register:40f0:8", ["const:ab229c:8", "const:4:8"]]
- 00ab229c ["CALL", null, ["callee:00465780:8"]]
+ 00ab22e0 ["INT_ADD", "register:40f0:8", ["const:ab22e0:8", "const:4:8"]]
+ 00ab22e0 ["CALL", null, ["callee:00465780:8"]]
- 00ab229c bytes 39cde697
+ 00ab22e0 bytes 28cde697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e482cbcf444b0f936920f7e7fe85e6b"></a>

### [`00ab3134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3134.md) → [`00ab3178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3178.md) FUN_00ab3178

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ab1e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00ab1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1ecc.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.87% / 新版 89.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ab31b8",
      "incomplete_value": false,
      "site": "00ab31c4",
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
    "old": {
      "definition_site": "00ab3174",
      "incomplete_value": false,
      "site": "00ab3180",
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
            "const:d28:8"
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
      "definition_site": "00ab31d8",
      "incomplete_value": true,
      "site": "00ab31f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e89:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ab3194",
      "incomplete_value": true,
      "site": "00ab31ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dfe:8"
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
      "definition_site": "00ab31f4",
      "incomplete_value": true,
      "site": "00ab31f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ab31b0",
      "incomplete_value": true,
      "site": "00ab31b0",
      "value": [
        "LOAD",
        "8",
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
      "00ab31c4",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00ab31d8",
      "READ",
      [
        "storage",
        "002a0dfe",
        null,
        "string"
      ]
    ],
    [
      "00ab31e0",
      "READ",
      [
        "storage",
        "002a0e0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ab31c4",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00ab31d8",
      "READ",
      [
        "storage",
        "002a0e89",
        null,
        "string"
      ]
    ],
    [
      "00ab31e0",
      "READ",
      [
        "storage",
        "002a0e97",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ab3168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3134.md#insn-00ab3168) · [`00ab31f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3134.md#insn-00ab31f4) · [`00ab32e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3134.md#insn-00ab32e4)
- 新版 `00ab31ac`（命令位置の公開資料なし） · `00ab3238`（命令位置の公開資料なし） · `00ab3328`（命令位置の公開資料なし）

~~~diff
- 00ab3168 ["INT_ADD", "register:40f0:8", ["const:ab3168:8", "const:4:8"]]
- 00ab3168 ["CALL", null, ["callee:00464f48:8"]]
+ 00ab31ac ["INT_ADD", "register:40f0:8", ["const:ab31ac:8", "const:4:8"]]
+ 00ab31ac ["CALL", null, ["callee:00464f48:8"]]
- 00ab3168 bytes 78c7e697
+ 00ab31ac bytes 67c7e697
- 00ab31f4 ["INT_ADD", "register:40f0:8", ["const:ab31f4:8", "const:4:8"]]
- 00ab31f4 ["CALL", null, ["callee:00419064:8"]]
+ 00ab3238 ["INT_ADD", "register:40f0:8", ["const:ab3238:8", "const:4:8"]]
+ 00ab3238 ["CALL", null, ["callee:00419064:8"]]
- 00ab31f4 bytes 9c97e597
+ 00ab3238 bytes 8b97e597
- 00ab32e4 ["INT_ADD", "register:40f0:8", ["const:ab32e4:8", "const:4:8"]]
- 00ab32e4 ["CALL", null, ["callee:00465780:8"]]
+ 00ab3328 ["INT_ADD", "register:40f0:8", ["const:ab3328:8", "const:4:8"]]
+ 00ab3328 ["CALL", null, ["callee:00465780:8"]]
- 00ab32e4 bytes 27c9e697
+ 00ab3328 bytes 16c9e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6754e223149caed8b9ef9868eab641b"></a>

### [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) → [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) FUN_00ab3444

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 49件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00449588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449588.md) [`0044d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d83c.md)
- 新版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 49件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00449588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449588.md) [`0044d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d83c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.88% / 新版 60.88%

CFGの説明率　旧版 32.73% / 新版 32.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 43件, `store_condition` 16件, `store_destination` 1件, `store_value` 14件, `unresolved_branch_alignment` 423件, `unresolved_call_alignment` 291件, `unresolved_store_alignment` 317件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab3448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab346c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab3470"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ab3448",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00ab3448",
      "WRITE",
      [
        "storage",
        "Stack[-0x1e0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ab3450",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb040"
      ]
    ]
  ],
  "added": [
    [
      "00ab348c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00ab348c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1e0]",
        null,
        null
      ]
    ],
    [
      "00ab3494",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ab3448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md#insn-00ab3448) · [`00ab346c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md#insn-00ab346c) · [`00ab3470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md#insn-00ab3470)

~~~diff
- 00ab3448 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:410:8"]]
- 00ab3448 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ab3448 bytes e80b02f9
- 00ab346c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:400:8"]]
- 00ab346c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ab346c bytes e00302f9
- 00ab3470 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00ab3470 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00ab3470 bytes 0000803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09dd76bef30b85280e613fce05ed3e46"></a>

### [`00abaf24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aba/00abaf24.md) → [`00abaf68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aba/00abaf68.md) FUN_00abaf68

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 13件 [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465394.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 13件 [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465394.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 13.29% / 新版 13.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 17件, `unresolved_store_alignment` 16件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abaf60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abb15c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abb1c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00abaf60",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00abaf60",
      "WRITE",
      [
        "storage",
        "Stack[-0x1b0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00abafd8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00ab1234"
      ]
    ]
  ],
  "added": [
    [
      "00abafa4",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00abafa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x1b0]",
        null,
        null
      ]
    ],
    [
      "00abb01c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00ab1234"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00abaf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aba/00abaf24.md#insn-00abaf60) · [`00abb15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aba/00abaf24.md#insn-00abb15c)
- 新版 `00abafa4`（命令位置の公開資料なし）

~~~diff
- 00abaf60 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:c0:8"]]
- 00abaf60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00abaf60 bytes e86300f9
+ 00abafa4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:c0:8"]]
+ 00abafa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00abafa4 bytes e86300f9
- 00abb15c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00abb15c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00abb15c bytes 0003803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24b06b12a283c71e513e0c6cda870aa1"></a>

### [`00abb8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abb/00abb8ec.md) → [`00abb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abb/00abb930.md) FUN_00abb930

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 25件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md)
- 新版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 25件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.89% / 新版 77.89%

CFGの説明率　旧版 34.09% / 新版 34.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `store_condition` 6件, `store_value` 2件, `unresolved_branch_alignment` 44件, `unresolved_call_alignment` 35件, `unresolved_store_alignment` 76件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abb8ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abb8ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abb8f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00abb8ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00abb8f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00abb8f4",
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
      "00abb930",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00abb934",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00abb938",
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

- 旧版 [`00abb8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abb/00abb8ec.md#insn-00abb8ec) · [`00abb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abb/00abb8ec.md#insn-00abb8f0) · [`00abb8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abb/00abb8ec.md#insn-00abb8f4)

~~~diff
- 00abb8ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00abb8ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00abb8ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00abb8ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00abb8ec bytes fd7bbaa9
- 00abb8f0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00abb8f0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00abb8f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00abb8f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00abb8f0 bytes fc6f01a9
- 00abb8f4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00abb8f4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00abb8f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00abb8f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00abb8f4 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b241121f9651c8536fc9504768b3ffc"></a>

### [`00abd420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abd/00abd420.md) → [`00abd464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abd/00abd464.md) FUN_00abd464

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 13件 [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465394.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 13件 [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465394.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.11% / 新版 73.11%

CFGの説明率　旧版 33.56% / 新版 34.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 24件, `unresolved_call_alignment` 27件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 34件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abd5bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abd5c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abd5f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00abd4b0",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00abd4f0",
      "READ",
      [
        "storage",
        "Stack[-0x200]",
        null,
        null
      ]
    ],
    [
      "unmatched:00abd4f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb060"
      ]
    ]
  ],
  "added": [
    [
      "00abd4b0",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00abd54c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb060"
      ]
    ],
    [
      "00abd550",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abd6b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00abd5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abd/00abd420.md#insn-00abd5b0) · [`00abd5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abd/00abd420.md#insn-00abd5bc) · [`00abd5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abd/00abd420.md#insn-00abd5c0)
- 新版 `00abd5f4`（命令位置の公開資料なし）

~~~diff
- 00abd5b0 ["INT_ADD", "register:40f0:8", ["const:abd5b0:8", "const:4:8"]]
- 00abd5b0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00abd5f4 ["INT_ADD", "register:40f0:8", ["const:abd5f4:8", "const:4:8"]]
+ 00abd5f4 ["CALL", null, ["callee:00bdb060:8"]]
- 00abd5b0 bytes 98760494
+ 00abd5f4 bytes 9b760494
- 00abd5bc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00abd5bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00abd5bc bytes 6002803d
- 00abd5c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00abd5c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00abd5c0 bytes 680a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-187862ec5362ae9d10687633186244af"></a>

### [`00abe18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abe/00abe18c.md) → [`00abe1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abe/00abe1d0.md) FUN_00abe1d0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 25件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 25件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.15% / 新版 81.15%

CFGの説明率　旧版 37.22% / 新版 37.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_condition` 1件, `store_destination` 1件, `store_value` 4件, `unresolved_branch_alignment` 16件, `unresolved_call_alignment` 15件, `unresolved_store_alignment` 26件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abe1d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abe1e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abe248"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00abe1d0",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00abe1d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00abe1e8",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00abe214",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00abe214",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "00abe22c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00abe1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abe/00abe18c.md#insn-00abe1d0) · [`00abe1e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abe/00abe18c.md#insn-00abe1e8) · [`00abe214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abe/00abe18c.md#insn-00abe214)
- 新版 `00abe258`（命令位置の公開資料なし）

~~~diff
- 00abe1d0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:208:8"]]
- 00abe1d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 00abe1d0 bytes f60701f9
- 00abe1e8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:b0:8"]]
- 00abe1e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 00abe1e8 bytes f65b00f9
- 00abe214 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00abe214 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00abe214 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00abe214 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00abe258 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
+ 00abe258 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00abe258 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00abe258 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00abe214 bytes 89ff0736
+ 00abe258 bytes 89ff0736
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3071e0c463af75ff9839498c8839aee9"></a>

### [`00abf09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf09c.md) → [`00abf0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf0e0.md) FUN_00abf0e0

採用 · 移動量 `+0x44` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00596128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596128.md) · 呼出先 14件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041cc4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cc4c.md) [`0053d984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d984.md) [`00574fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fe4.md) [`0084dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084dd1c.md)
- 新版 呼出元 1件 [`00596128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md) · 呼出先 14件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041cc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cc4c.md) [`0053d984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d984.md) [`00574fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fe4.md) [`0084dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.64% / 新版 69.64%

CFGの説明率　旧版 27.27% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abf0c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abf118"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abf168"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00abf0c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00abf130",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00abf0f8"
      ]
    ],
    [
      "unmatched:00abf104",
      "READ",
      [
        "storage",
        "0029faf1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00abf104",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00abf130",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abf13c"
      ]
    ],
    [
      "00abf148",
      "READ",
      [
        "storage",
        "0029fb7c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00abf0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf09c.md#insn-00abf0c0) · [`00abf0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf09c.md#insn-00abf0d4) · [`00abf104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf09c.md#insn-00abf104)
- 新版 `00abf118`（命令位置の公開資料なし）

~~~diff
- 00abf0c0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00abf0c0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00abf0c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00abf0c0 bytes a8831ff8
- 00abf0d4 ["INT_ADD", "register:40f0:8", ["const:abf0d4:8", "const:4:8"]]
- 00abf0d4 ["CALL", null, ["callee:009bd6c4:8"]]
+ 00abf118 ["INT_ADD", "register:40f0:8", ["const:abf118:8", "const:4:8"]]
+ 00abf118 ["CALL", null, ["callee:009bd6c4:8"]]
- 00abf0d4 bytes 79f9fb97
+ 00abf118 bytes 6bf9fb97
- 00abf104 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00abf104 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00abf104 ["COPY", "register:5010:8", ["const:0:8"]]
- 00abf104 ["COPY", "register:5018:8", ["const:0:8"]]
- 00abf104 bytes 2001c03d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5723e5a00a72166de505d5330c39fdb7"></a>

### [`00ac8ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac8/00ac8ff0.md) → [`00ac9034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9034.md) FUN_00ac9034

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 80.00% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ac9004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac8/00ac8ff0.md#insn-00ac9004) · [`00ac900c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac8/00ac8ff0.md#insn-00ac900c) · [`00ac9014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac8/00ac8ff0.md#insn-00ac9014)
- 新版 `00ac9048`（命令位置の公開資料なし） · `00ac9050`（命令位置の公開資料なし） · `00ac9058`（命令位置の公開資料なし）

~~~diff
- 00ac9004 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00ac9004 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ac9004 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ac9004 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00ac9048 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00ac9048 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00ac9048 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00ac9048 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00ac9004 bytes 28010037
+ 00ac9048 bytes 28010037
- 00ac900c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00ac900c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ac900c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ac900c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00ac9050 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00ac9050 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00ac9050 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00ac9050 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00ac900c bytes 68010037
+ 00ac9050 bytes 68010037
- 00ac9014 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00ac9014 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00ac9058 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00ac9058 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ac9014 bytes a00100b4
+ 00ac9058 bytes a00100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0fe1501758a7d101b8df7980498f75e"></a>

### [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) → [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) FUN_00ac9098

採用 · 移動量 `+0x44` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00596128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596128.md) · 呼出先 67件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00458038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00458/00458038.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00596128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md) · 呼出先 67件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00458038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458038.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.05% / 新版 92.05%

CFGの説明率　旧版 84.96% / 新版 86.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件, `store_value` 7件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 16件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9058"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9058"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac905c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac9058",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac905c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac9060",
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
      "00ac909c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ac90a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ac90a4",
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

- 旧版 [`00ac9058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md#insn-00ac9058) · [`00ac905c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md#insn-00ac905c) · [`00ac9060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md#insn-00ac9060)

~~~diff
- 00ac9058 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ac9058 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ac9058 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:190:8"]]
- 00ac9058 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac9058 bytes fd7b19a9
- 00ac905c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00ac905c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00ac905c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 00ac905c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac905c bytes fc671aa9
- 00ac9060 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ac9060 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ac9060 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1b0:8"]]
- 00ac9060 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac9060 bytes f85f1ba9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f9befe37119a21fb214f116254cdf83"></a>

### [`00ac9dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9dc8.md) → [`00ac9e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9e0c.md) FUN_00ac9e0c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9c18.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00ac9c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9c5c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00ac9e18",
      "incomplete_value": false,
      "site": "00ac9e1c",
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
    "old": {
      "definition_site": "00ac9dd4",
      "incomplete_value": false,
      "site": "00ac9dd8",
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
            "const:303:8"
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
      "00ac9e18",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ac9e18",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac9dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9dc8.md#insn-00ac9dd8) · [`00ac9dd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9dc8.md#insn-00ac9dd4)
- 新版 `00ac9e1c`（命令位置の公開資料なし） · `00ac9e18`（命令位置の公開資料なし）

~~~diff
- 00ac9dd8 ["INT_ADD", "register:40f0:8", ["const:ac9dd8:8", "const:4:8"]]
- 00ac9dd8 ["CALL", null, ["callee:00418c38:8"]]
+ 00ac9e1c ["INT_ADD", "register:40f0:8", ["const:ac9e1c:8", "const:4:8"]]
+ 00ac9e1c ["CALL", null, ["callee:00418c38:8"]]
- 00ac9dd8 bytes 983be597
+ 00ac9e1c bytes 873be597
- 00ac9dd4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00ac9dd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ac9dd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ac9dd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ac9e18 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00ac9e18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ac9e18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ac9e18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ac9dd4 bytes 000c0c91
+ 00ac9e18 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fe197c168db89923d551db5ab493f46"></a>

### [`00ac9f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f70.md) → [`00ac9fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9fb4.md) FUN_00ac9fb4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9ddc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00ac9e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9e20.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00ac9fc0",
      "incomplete_value": false,
      "site": "00ac9fc4",
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
    "old": {
      "definition_site": "00ac9f7c",
      "incomplete_value": false,
      "site": "00ac9f80",
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
            "const:303:8"
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
      "00ac9fc0",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ac9fc0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac9f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f70.md#insn-00ac9f80) · [`00ac9f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f70.md#insn-00ac9f7c)
- 新版 `00ac9fc4`（命令位置の公開資料なし） · `00ac9fc0`（命令位置の公開資料なし）

~~~diff
- 00ac9f80 ["INT_ADD", "register:40f0:8", ["const:ac9f80:8", "const:4:8"]]
- 00ac9f80 ["CALL", null, ["callee:00418c38:8"]]
+ 00ac9fc4 ["INT_ADD", "register:40f0:8", ["const:ac9fc4:8", "const:4:8"]]
+ 00ac9fc4 ["CALL", null, ["callee:00418c38:8"]]
- 00ac9f80 bytes 2e3be597
+ 00ac9fc4 bytes 1d3be597
- 00ac9f7c ["COPY", "tmp:0:8", ["const:303:8"]]
- 00ac9f7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ac9f7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ac9f7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ac9fc0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00ac9fc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ac9fc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ac9fc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ac9f7c bytes 000c0c91
+ 00ac9fc0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-334d407454e42f7446e1f7c24c524732"></a>

### [`00aca114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca114.md) → [`00aca158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca158.md) FUN_00aca158

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f84.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00ac9fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9fc8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00aca164",
      "incomplete_value": false,
      "site": "00aca168",
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
    "old": {
      "definition_site": "00aca120",
      "incomplete_value": false,
      "site": "00aca124",
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
            "const:303:8"
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
      "00aca164",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aca164",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca114.md#insn-00aca124) · [`00aca120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca114.md#insn-00aca120)
- 新版 `00aca168`（命令位置の公開資料なし） · `00aca164`（命令位置の公開資料なし）

~~~diff
- 00aca124 ["INT_ADD", "register:40f0:8", ["const:aca124:8", "const:4:8"]]
- 00aca124 ["CALL", null, ["callee:00418c38:8"]]
+ 00aca168 ["INT_ADD", "register:40f0:8", ["const:aca168:8", "const:4:8"]]
+ 00aca168 ["CALL", null, ["callee:00418c38:8"]]
- 00aca124 bytes c53ae597
+ 00aca168 bytes b43ae597
- 00aca120 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00aca120 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aca120 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aca120 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aca164 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00aca164 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca164 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca164 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aca120 bytes 000c0c91
+ 00aca164 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a173fcb1d81d3a685b62eb4136c5cfc"></a>

### [`00aca254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca254.md) → [`00aca298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca298.md) FUN_00aca298

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00aca128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca128.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00aca16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca16c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00aca2a4",
      "incomplete_value": false,
      "site": "00aca2a8",
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
    "old": {
      "definition_site": "00aca260",
      "incomplete_value": false,
      "site": "00aca264",
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
            "const:303:8"
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
      "00aca2a4",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aca2a4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca254.md#insn-00aca264) · [`00aca260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca254.md#insn-00aca260)
- 新版 `00aca2a8`（命令位置の公開資料なし） · `00aca2a4`（命令位置の公開資料なし）

~~~diff
- 00aca264 ["INT_ADD", "register:40f0:8", ["const:aca264:8", "const:4:8"]]
- 00aca264 ["CALL", null, ["callee:00418c38:8"]]
+ 00aca2a8 ["INT_ADD", "register:40f0:8", ["const:aca2a8:8", "const:4:8"]]
+ 00aca2a8 ["CALL", null, ["callee:00418c38:8"]]
- 00aca264 bytes 753ae597
+ 00aca2a8 bytes 643ae597
- 00aca260 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00aca260 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aca260 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aca260 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aca2a4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00aca2a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca2a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca2a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aca260 bytes 000c0c91
+ 00aca2a4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8eb2599ea1884e092979c68487a9381"></a>

### [`00aca3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca3fc.md) → [`00aca440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca440.md) FUN_00aca440

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00aca268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca268.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00aca2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca2ac.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00aca44c",
      "incomplete_value": false,
      "site": "00aca450",
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
    "old": {
      "definition_site": "00aca408",
      "incomplete_value": false,
      "site": "00aca40c",
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
            "const:303:8"
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
      "00aca44c",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aca44c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca3fc.md#insn-00aca40c) · [`00aca408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca3fc.md#insn-00aca408)
- 新版 `00aca450`（命令位置の公開資料なし） · `00aca44c`（命令位置の公開資料なし）

~~~diff
- 00aca40c ["INT_ADD", "register:40f0:8", ["const:aca40c:8", "const:4:8"]]
- 00aca40c ["CALL", null, ["callee:00418c38:8"]]
+ 00aca450 ["INT_ADD", "register:40f0:8", ["const:aca450:8", "const:4:8"]]
+ 00aca450 ["CALL", null, ["callee:00418c38:8"]]
- 00aca40c bytes 0b3ae597
+ 00aca450 bytes fa39e597
- 00aca408 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00aca408 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aca408 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aca408 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aca44c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00aca44c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca44c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca44c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aca408 bytes 000c0c91
+ 00aca44c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-539a6a0118697b8f4c6f534effad29d0"></a>

### [`00aca5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5a0.md) → [`00aca5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca5e4.md) FUN_00aca5e4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00aca410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca410.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00aca454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca454.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00aca5f0",
      "incomplete_value": false,
      "site": "00aca5f4",
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
    "old": {
      "definition_site": "00aca5ac",
      "incomplete_value": false,
      "site": "00aca5b0",
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
            "const:303:8"
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
      "00aca5f0",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aca5f0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5a0.md#insn-00aca5b0) · [`00aca5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5a0.md#insn-00aca5ac)
- 新版 `00aca5f4`（命令位置の公開資料なし） · `00aca5f0`（命令位置の公開資料なし）

~~~diff
- 00aca5b0 ["INT_ADD", "register:40f0:8", ["const:aca5b0:8", "const:4:8"]]
- 00aca5b0 ["CALL", null, ["callee:00418c38:8"]]
+ 00aca5f4 ["INT_ADD", "register:40f0:8", ["const:aca5f4:8", "const:4:8"]]
+ 00aca5f4 ["CALL", null, ["callee:00418c38:8"]]
- 00aca5b0 bytes a239e597
+ 00aca5f4 bytes 9139e597
- 00aca5ac ["COPY", "tmp:0:8", ["const:303:8"]]
- 00aca5ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aca5ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aca5ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aca5f0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00aca5f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca5f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca5f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aca5ac bytes 000c0c91
+ 00aca5f0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16ca4226c4a611b4946bb6abd38a1a74"></a>

### [`00aca5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5b4.md) → [`00aca5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca5f8.md) FUN_00aca5f8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00aca604",
      "incomplete_value": false,
      "site": "00aca608",
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
    "old": {
      "definition_site": "00aca5c0",
      "incomplete_value": false,
      "site": "00aca5c4",
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
            "const:303:8"
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
      "00aca604",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aca604",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca5c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5b4.md#insn-00aca5c4) · [`00aca5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5b4.md#insn-00aca5c0)
- 新版 `00aca608`（命令位置の公開資料なし） · `00aca604`（命令位置の公開資料なし）

~~~diff
- 00aca5c4 ["INT_ADD", "register:40f0:8", ["const:aca5c4:8", "const:4:8"]]
- 00aca5c4 ["CALL", null, ["callee:00418c38:8"]]
+ 00aca608 ["INT_ADD", "register:40f0:8", ["const:aca608:8", "const:4:8"]]
+ 00aca608 ["CALL", null, ["callee:00418c38:8"]]
- 00aca5c4 bytes 9d39e597
+ 00aca608 bytes 8c39e597
- 00aca5c0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00aca5c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aca5c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aca5c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aca604 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00aca604 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca604 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca604 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aca5c0 bytes 000c0c91
+ 00aca604 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79a1fd5aa56a8241a184a30ecc73e31b"></a>

### [`00aca6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca6f4.md) → [`00aca738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca738.md) FUN_00aca738

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00aca5c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5c8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00aca60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca60c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00aca744",
      "incomplete_value": false,
      "site": "00aca748",
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
    "old": {
      "definition_site": "00aca700",
      "incomplete_value": false,
      "site": "00aca704",
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
            "const:303:8"
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
      "00aca744",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aca744",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca6f4.md#insn-00aca704) · [`00aca700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca6f4.md#insn-00aca700)
- 新版 `00aca748`（命令位置の公開資料なし） · `00aca744`（命令位置の公開資料なし）

~~~diff
- 00aca704 ["INT_ADD", "register:40f0:8", ["const:aca704:8", "const:4:8"]]
- 00aca704 ["CALL", null, ["callee:00418c38:8"]]
+ 00aca748 ["INT_ADD", "register:40f0:8", ["const:aca748:8", "const:4:8"]]
+ 00aca748 ["CALL", null, ["callee:00418c38:8"]]
- 00aca704 bytes 4d39e597
+ 00aca748 bytes 3c39e597
- 00aca700 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00aca700 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aca700 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aca700 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aca744 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00aca744 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca744 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca744 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aca700 bytes 000c0c91
+ 00aca744 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6483515c1491e45c44c7d5eb4d615d1"></a>

### [`00aca708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca708.md) → [`00aca74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca74c.md) FUN_00aca74c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aca8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca8c0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aca904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca904.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.09% / 新版 89.09%

CFGの説明率　旧版 66.67% / 新版 63.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aca798"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aca7a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aca7dc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aca798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca708.md#insn-00aca798) · [`00aca7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca708.md#insn-00aca7a0) · [`00aca7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca708.md#insn-00aca7c4)
- 新版 `00aca808`（命令位置の公開資料なし）

~~~diff
- 00aca798 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00aca798 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00aca798 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00aca798 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00aca798 bytes 29818b9a
- 00aca7a0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00aca7a0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aca7a0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00aca7a0 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00aca7a0 bytes 37318a9a
- 00aca7c4 ["BRANCH", null, ["local:b10:8"]]
+ 00aca808 ["BRANCH", null, ["local:b11:8"]]
- 00aca7c4 bytes 16000014
+ 00aca808 bytes 16000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-348f2aa5303dd90a0e83d863cdaed309"></a>

### [`00aca8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca8c0.md) → [`00aca904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca904.md) FUN_00aca904

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00aca708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca708.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00aca74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca74c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00aca910",
      "incomplete_value": false,
      "site": "00aca914",
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
    "old": {
      "definition_site": "00aca8cc",
      "incomplete_value": false,
      "site": "00aca8d0",
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
            "const:303:8"
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
      "00aca910",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aca910",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca8c0.md#insn-00aca8d0) · [`00aca8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca8c0.md#insn-00aca8cc)
- 新版 `00aca914`（命令位置の公開資料なし） · `00aca910`（命令位置の公開資料なし）

~~~diff
- 00aca8d0 ["INT_ADD", "register:40f0:8", ["const:aca8d0:8", "const:4:8"]]
- 00aca8d0 ["CALL", null, ["callee:00418c38:8"]]
+ 00aca914 ["INT_ADD", "register:40f0:8", ["const:aca914:8", "const:4:8"]]
+ 00aca914 ["CALL", null, ["callee:00418c38:8"]]
- 00aca8d0 bytes da38e597
+ 00aca914 bytes c938e597
- 00aca8cc ["COPY", "tmp:0:8", ["const:303:8"]]
- 00aca8cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aca8cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aca8cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aca910 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00aca910 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca910 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aca910 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aca8cc bytes 000c0c91
+ 00aca910 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ecb65da2a4f11b8cc002f949b073f4b"></a>

### [`00aca8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca8d8.md) → [`00aca91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca91c.md) FUN_00aca91c

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
      "definition_site": "00aca930",
      "incomplete_value": false,
      "site": "00aca934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aca8ec",
      "incomplete_value": false,
      "site": "00aca8f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "00aca934",
      "DATA",
      [
        "storage",
        "00c0f678",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aca934",
      "DATA",
      [
        "storage",
        "00c0f6c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca8e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca8d8.md#insn-00aca8e4) · [`00aca8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca8d8.md#insn-00aca8ec)
- 新版 `00aca928`（命令位置の公開資料なし） · `00aca930`（命令位置の公開資料なし）

~~~diff
- 00aca8e4 ["INT_ADD", "register:40f0:8", ["const:aca8e4:8", "const:4:8"]]
- 00aca8e4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aca928 ["INT_ADD", "register:40f0:8", ["const:aca928:8", "const:4:8"]]
+ 00aca928 ["CALL", null, ["callee:00bdb040:8"]]
- 00aca8e4 bytes c3410494
+ 00aca928 bytes c6410494
- 00aca8ec ["COPY", "tmp:0:8", ["const:678:8"]]
- 00aca8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aca8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aca8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aca930 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00aca930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aca930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aca930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aca8ec bytes 08e11991
+ 00aca930 bytes 08211b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-824b0c6a542a342abb748a41bb3a00c6"></a>

### [`00aca8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca8fc.md) → [`00aca940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca940.md) FUN_00aca940

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
      "definition_site": "00aca944",
      "incomplete_value": false,
      "site": "00aca948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aca900",
      "incomplete_value": false,
      "site": "00aca904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "00aca948",
      "DATA",
      [
        "storage",
        "00c0f678",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aca948",
      "DATA",
      [
        "storage",
        "00c0f6c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca8fc.md#insn-00aca900)
- 新版 `00aca944`（命令位置の公開資料なし）

~~~diff
- 00aca900 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00aca900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aca900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aca900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aca944 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00aca944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aca944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aca944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aca900 bytes 08e11991
+ 00aca944 bytes 08211b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-628e9b7ffdb1151973caa211cda6abb2"></a>

### [`00acabb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabb4.md) → [`00acabf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acabf8.md) FUN_00acabf8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00aca940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca940.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00aca984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca984.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00acac04",
      "incomplete_value": false,
      "site": "00acac08",
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
    "old": {
      "definition_site": "00acabc0",
      "incomplete_value": false,
      "site": "00acabc4",
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
            "const:303:8"
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
      "00acac04",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acac04",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acabc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabb4.md#insn-00acabc4) · [`00acabc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabb4.md#insn-00acabc0)
- 新版 `00acac08`（命令位置の公開資料なし） · `00acac04`（命令位置の公開資料なし）

~~~diff
- 00acabc4 ["INT_ADD", "register:40f0:8", ["const:acabc4:8", "const:4:8"]]
- 00acabc4 ["CALL", null, ["callee:00418c38:8"]]
+ 00acac08 ["INT_ADD", "register:40f0:8", ["const:acac08:8", "const:4:8"]]
+ 00acac08 ["CALL", null, ["callee:00418c38:8"]]
- 00acabc4 bytes 1d38e597
+ 00acac08 bytes 0c38e597
- 00acabc0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00acabc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00acabc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00acabc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00acac04 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00acac04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00acac04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00acac04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00acabc0 bytes 000c0c91
+ 00acac04 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9f3d5a7fd7c7691b5bd272247144c45"></a>

### [`00acabc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabc8.md) → [`00acac0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acac0c.md) FUN_00acac0c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00aca940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca940.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00aca984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca984.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 86.36% / 新版 82.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acabcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabc8.md#insn-00acabcc) · [`00acac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabc8.md#insn-00acac64) · [`00acac6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabc8.md#insn-00acac6c)
- 新版 `00acac10`（命令位置の公開資料なし） · `00acaca8`（命令位置の公開資料なし） · `00acacb0`（命令位置の公開資料なし）

~~~diff
- 00acabcc ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
+ 00acac10 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00acabcc bytes 60070054
+ 00acac10 bytes 60070054
- 00acac64 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 00acaca8 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00acac64 bytes 60020054
+ 00acaca8 bytes 60020054
- 00acac6c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00acac6c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00acac6c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00acac6c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00acacb0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00acacb0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00acacb0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00acacb0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00acac6c bytes c8000037
+ 00acacb0 bytes c8000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37f85cd7951780c751dce0718f0789e7"></a>

### [`00acacbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acacbc.md) → [`00acad00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acad00.md) FUN_00acad00

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00acad0c",
      "incomplete_value": false,
      "site": "00acad10",
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
    "old": {
      "definition_site": "00acacc8",
      "incomplete_value": false,
      "site": "00acaccc",
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
            "const:303:8"
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
      "00acad0c",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acad0c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acaccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acacbc.md#insn-00acaccc) · [`00acacc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acacbc.md#insn-00acacc8)
- 新版 `00acad10`（命令位置の公開資料なし） · `00acad0c`（命令位置の公開資料なし）

~~~diff
- 00acaccc ["INT_ADD", "register:40f0:8", ["const:acaccc:8", "const:4:8"]]
- 00acaccc ["CALL", null, ["callee:00418c38:8"]]
+ 00acad10 ["INT_ADD", "register:40f0:8", ["const:acad10:8", "const:4:8"]]
+ 00acad10 ["CALL", null, ["callee:00418c38:8"]]
- 00acaccc bytes db37e597
+ 00acad10 bytes ca37e597
- 00acacc8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00acacc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00acacc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00acacc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00acad0c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00acad0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00acad0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00acad0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00acacc8 bytes 000c0c91
+ 00acad0c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0c5ddf79eadc04b8ba921d956db3326"></a>

### [`00acb5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb5d0.md) → [`00acb614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb614.md) FUN_00acb614

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00acb174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00acb1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb1b8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00acb620",
      "incomplete_value": false,
      "site": "00acb624",
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
    "old": {
      "definition_site": "00acb5dc",
      "incomplete_value": false,
      "site": "00acb5e0",
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
            "const:303:8"
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
      "00acb620",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acb620",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb5d0.md#insn-00acb5e0) · [`00acb5dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb5d0.md#insn-00acb5dc)
- 新版 `00acb624`（命令位置の公開資料なし） · `00acb620`（命令位置の公開資料なし）

~~~diff
- 00acb5e0 ["INT_ADD", "register:40f0:8", ["const:acb5e0:8", "const:4:8"]]
- 00acb5e0 ["CALL", null, ["callee:00418c38:8"]]
+ 00acb624 ["INT_ADD", "register:40f0:8", ["const:acb624:8", "const:4:8"]]
+ 00acb624 ["CALL", null, ["callee:00418c38:8"]]
- 00acb5e0 bytes 9635e597
+ 00acb624 bytes 8535e597
- 00acb5dc ["COPY", "tmp:0:8", ["const:303:8"]]
- 00acb5dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00acb5dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00acb5dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00acb620 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00acb620 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00acb620 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00acb620 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00acb5dc bytes 000c0c91
+ 00acb620 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edafd71e127563c4c75c94baf2fe2080"></a>

### [`00acb5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb5e4.md) → [`00acb628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb628.md) _INIT_251

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 76.44% / 新版 76.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 11件, `store_value` 8件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acb664",
      "incomplete_value": true,
      "site": "00acb680",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acb620",
      "incomplete_value": true,
      "site": "00acb63c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acb688",
      "incomplete_value": true,
      "site": "00acb6a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acb644",
      "incomplete_value": true,
      "site": "00acb660",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acb6a8",
      "incomplete_value": true,
      "site": "00acb6c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acb664",
      "incomplete_value": true,
      "site": "00acb680",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00acb664",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00acb688",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00acb6a8",
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
      "00acb664",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00acb688",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00acb6a8",
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

- 旧版 [`00acb61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb5e4.md#insn-00acb61c) · [`00acb744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb5e4.md#insn-00acb744) · [`00acb7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb5e4.md#insn-00acb7fc)
- 新版 `00acb660`（命令位置の公開資料なし） · `00acb788`（命令位置の公開資料なし） · `00acb840`（命令位置の公開資料なし）

~~~diff
- 00acb61c ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00acb61c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00acb61c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00acb61c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00acb660 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00acb660 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00acb660 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00acb660 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00acb61c bytes 29750b91
+ 00acb660 bytes 29dd0d91
- 00acb744 ["INT_ADD", "register:40f0:8", ["const:acb744:8", "const:4:8"]]
- 00acb744 ["CALL", null, ["callee:00418cb8:8"]]
+ 00acb788 ["INT_ADD", "register:40f0:8", ["const:acb788:8", "const:4:8"]]
+ 00acb788 ["CALL", null, ["callee:00418cb8:8"]]
- 00acb744 bytes 5d35e597
+ 00acb788 bytes 4c35e597
- 00acb7fc ["INT_ADD", "register:40f0:8", ["const:acb7fc:8", "const:4:8"]]
- 00acb7fc ["CALL", null, ["callee:00bdb060:8"]]
+ 00acb840 ["INT_ADD", "register:40f0:8", ["const:acb840:8", "const:4:8"]]
+ 00acb840 ["CALL", null, ["callee:00bdb060:8"]]
- 00acb7fc bytes 053e0494
+ 00acb840 bytes 083e0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a109c083c3e51c334ee8bee194ca518a"></a>

### [`00acb9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb9f8.md) → [`00acba3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acba3c.md) FUN_00acba3c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004184bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004184bc.md) · 呼出先 20件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c9e0.md) [`00449bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bb8.md) [`00449be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449be4.md) [`004723a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00472/004723a8.md)
- 新版 呼出元 1件 [`004184bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004184bc.md) · 呼出先 20件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c9e0.md) [`00449bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bb8.md) [`00449be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449be4.md) [`004723a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004723a8.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.08% / 新版 91.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00acbaf0",
      "incomplete_value": false,
      "site": "00acbb00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acbaac",
      "incomplete_value": false,
      "site": "00acbabc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "definition_site": "00acbc20",
      "incomplete_value": false,
      "site": "00acbc30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acbbdc",
      "incomplete_value": false,
      "site": "00acbbec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
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
      "definition_site": "00acbb1c",
      "incomplete_value": true,
      "site": "00acbb1c",
      "value": [
        "LOAD",
        "8",
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
                "const:e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acbad8",
      "incomplete_value": true,
      "site": "00acbad8",
      "value": [
        "LOAD",
        "8",
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
                "const:e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00acbaf4",
      "READ",
      [
        "storage",
        "00c1b400",
        null,
        "pointer"
      ]
    ],
    [
      "00acbb00",
      "DATA",
      [
        "storage",
        "00c0f778",
        null,
        "undefined *"
      ]
    ],
    [
      "00acbb04",
      "READ",
      [
        "storage",
        "00c26610",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00acbaf4",
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ],
    [
      "00acbb00",
      "DATA",
      [
        "storage",
        "00c0f7c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00acbb04",
      "READ",
      [
        "storage",
        "00c26650",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acba78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb9f8.md#insn-00acba78) · [`00acba94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb9f8.md#insn-00acba94) · [`00acbad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb9f8.md#insn-00acbad8)
- 新版 `00acbabc`（命令位置の公開資料なし） · `00acbad8`（命令位置の公開資料なし） · `00acbb1c`（命令位置の公開資料なし）

~~~diff
- 00acba78 ["INT_ADD", "register:40f0:8", ["const:acba78:8", "const:4:8"]]
- 00acba78 ["CALL", null, ["callee:00828e20:8"]]
+ 00acbabc ["INT_ADD", "register:40f0:8", ["const:acbabc:8", "const:4:8"]]
+ 00acbabc ["CALL", null, ["callee:00828e20:8"]]
- 00acba78 bytes ea74f597
+ 00acbabc bytes d974f597
- 00acba94 ["INT_ADD", "register:40f0:8", ["const:acba94:8", "const:4:8"]]
- 00acba94 ["CALL", null, ["callee:0081f580:8"]]
+ 00acbad8 ["INT_ADD", "register:40f0:8", ["const:acbad8:8", "const:4:8"]]
+ 00acbad8 ["CALL", null, ["callee:0081f580:8"]]
- 00acba94 bytes bb4ef597
+ 00acbad8 bytes aa4ef597
- 00acbad8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00acbad8 ["INT_ADD", "register:40f0:8", ["const:acbad8:8", "const:4:8"]]
- 00acbad8 ["CALLIND", null, ["register:0:8"]]
+ 00acbb1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acbb1c ["INT_ADD", "register:40f0:8", ["const:acbb1c:8", "const:4:8"]]
+ 00acbb1c ["CALLIND", null, ["register:0:8"]]
- 00acbad8 bytes 00013fd6
+ 00acbb1c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-717888041fb4b00d744fb48cbdfcc232"></a>

### [`00acbd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbd60.md) → [`00acbda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbda4.md) FUN_00acbda4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00accf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md) · 呼出先 8件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00accf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md) · 呼出先 8件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.42% / 新版 93.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acbdec",
      "incomplete_value": true,
      "site": "00acbdec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ac:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acbda8",
      "incomplete_value": true,
      "site": "00acbda8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:439:8"
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
      "definition_site": "00acbde4",
      "incomplete_value": true,
      "site": "00acbdf0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00acbda0",
      "incomplete_value": true,
      "site": "00acbdac",
      "value": [
        "LOAD",
        "8",
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
      "00acbddc",
      "READ",
      [
        "storage",
        "00296439",
        null,
        "string"
      ]
    ],
    [
      "00acbde4",
      "READ",
      [
        "storage",
        "00296440",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acbddc",
      "READ",
      [
        "storage",
        "002963ac",
        null,
        "string"
      ]
    ],
    [
      "00acbde4",
      "READ",
      [
        "storage",
        "002963b3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acbd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbd60.md#insn-00acbd80) · [`00acbd88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbd60.md#insn-00acbd88) · [`00acbd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbd60.md#insn-00acbd94)
- 新版 `00acbdc4`（命令位置の公開資料なし） · `00acbdcc`（命令位置の公開資料なし） · `00acbdd8`（命令位置の公開資料なし）

~~~diff
- 00acbd80 ["INT_ADD", "register:40f0:8", ["const:acbd80:8", "const:4:8"]]
- 00acbd80 ["CALL", null, ["callee:00565f94:8"]]
+ 00acbdc4 ["INT_ADD", "register:40f0:8", ["const:acbdc4:8", "const:4:8"]]
+ 00acbdc4 ["CALL", null, ["callee:00565f94:8"]]
- 00acbd80 bytes 8568ea97
+ 00acbdc4 bytes 7468ea97
- 00acbd88 ["INT_ADD", "register:40f0:8", ["const:acbd88:8", "const:4:8"]]
- 00acbd88 ["CALL", null, ["callee:00566284:8"]]
+ 00acbdcc ["INT_ADD", "register:40f0:8", ["const:acbdcc:8", "const:4:8"]]
+ 00acbdcc ["CALL", null, ["callee:00566284:8"]]
- 00acbd88 bytes 3f69ea97
+ 00acbdcc bytes 2e69ea97
- 00acbd94 ["COPY", "tmp:0:8", ["const:439:8"]]
- 00acbd94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00acbd94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00acbd94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00acbdd8 ["COPY", "tmp:0:8", ["const:3ac:8"]]
+ 00acbdd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00acbdd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00acbdd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00acbd94 bytes 29e51091
+ 00acbdd8 bytes 29b10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af8b491f78ade279d6c931987ff9d8be"></a>

### [`00acbecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbecc.md) → [`00acbf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbf10.md) FUN_00acbf10

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00accf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md) · 呼出先 8件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00accf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md) · 呼出先 8件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acbf50",
      "incomplete_value": true,
      "site": "00acbf68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cea:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acbf0c",
      "incomplete_value": true,
      "site": "00acbf24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cec:8"
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
      "00acbf50",
      "READ",
      [
        "storage",
        "0029bcec",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acbf50",
      "READ",
      [
        "storage",
        "0029bcea",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acbf68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbecc.md#insn-00acbf68) · [`00acbeec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbecc.md#insn-00acbeec) · [`00acbef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbecc.md#insn-00acbef4)
- 新版 `00acbfac`（命令位置の公開資料なし） · `00acbf30`（命令位置の公開資料なし） · `00acbf38`（命令位置の公開資料なし）

~~~diff
- 00acbf68 ["INT_ADD", "register:40f0:8", ["const:acbf68:8", "const:4:8"]]
- 00acbf68 ["CALL", null, ["callee:0056626c:8"]]
+ 00acbfac ["INT_ADD", "register:40f0:8", ["const:acbfac:8", "const:4:8"]]
+ 00acbfac ["CALL", null, ["callee:0056626c:8"]]
- 00acbf68 bytes c168ea97
+ 00acbfac bytes b068ea97
- 00acbeec ["INT_ADD", "register:40f0:8", ["const:acbeec:8", "const:4:8"]]
- 00acbeec ["CALL", null, ["callee:00565f94:8"]]
+ 00acbf30 ["INT_ADD", "register:40f0:8", ["const:acbf30:8", "const:4:8"]]
+ 00acbf30 ["CALL", null, ["callee:00565f94:8"]]
- 00acbeec bytes 2a68ea97
+ 00acbf30 bytes 1968ea97
- 00acbef4 ["INT_ADD", "register:40f0:8", ["const:acbef4:8", "const:4:8"]]
- 00acbef4 ["CALL", null, ["callee:00566284:8"]]
+ 00acbf38 ["INT_ADD", "register:40f0:8", ["const:acbf38:8", "const:4:8"]]
+ 00acbf38 ["CALL", null, ["callee:00566284:8"]]
- 00acbef4 bytes e468ea97
+ 00acbf38 bytes d368ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51c67e733f9cd2b106041dcda2365675"></a>

### [`00acc1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc1a0.md) → [`00acc1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc1e4.md) FUN_00acc1e4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00accf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md) · 呼出先 8件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00accf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md) · 呼出先 8件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.95% / 新版 95.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acc224",
      "incomplete_value": true,
      "site": "00acc238",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bde:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acc1e0",
      "incomplete_value": true,
      "site": "00acc1f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b44:8"
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
      "00acc224",
      "READ",
      [
        "storage",
        "002a8b44",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acc224",
      "READ",
      [
        "storage",
        "002a8bde",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acc1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc1a0.md#insn-00acc1c0) · [`00acc1c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc1a0.md#insn-00acc1c8) · [`00acc1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc1a0.md#insn-00acc1d4)
- 新版 `00acc204`（命令位置の公開資料なし） · `00acc20c`（命令位置の公開資料なし） · `00acc218`（命令位置の公開資料なし）

~~~diff
- 00acc1c0 ["INT_ADD", "register:40f0:8", ["const:acc1c0:8", "const:4:8"]]
- 00acc1c0 ["CALL", null, ["callee:00565f94:8"]]
+ 00acc204 ["INT_ADD", "register:40f0:8", ["const:acc204:8", "const:4:8"]]
+ 00acc204 ["CALL", null, ["callee:00565f94:8"]]
- 00acc1c0 bytes 7567ea97
+ 00acc204 bytes 6467ea97
- 00acc1c8 ["INT_ADD", "register:40f0:8", ["const:acc1c8:8", "const:4:8"]]
- 00acc1c8 ["CALL", null, ["callee:00566284:8"]]
+ 00acc20c ["INT_ADD", "register:40f0:8", ["const:acc20c:8", "const:4:8"]]
+ 00acc20c ["CALL", null, ["callee:00566284:8"]]
- 00acc1c8 bytes 2f68ea97
+ 00acc20c bytes 1e68ea97
- 00acc1d4 ["COPY", "tmp:0:8", ["const:b44:8"]]
- 00acc1d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00acc1d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00acc1d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00acc218 ["COPY", "tmp:0:8", ["const:bde:8"]]
+ 00acc218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00acc218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00acc218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00acc1d4 bytes 29112d91
+ 00acc218 bytes 29792f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af28b1c70f113803c60ef8f4acca1298"></a>

### [`00acc304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc304.md) → [`00acc348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc348.md) FUN_00acc348

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004183ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004183ec.md) · 呼出先 19件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444a94.md) [`0044aa90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa90.md) [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`004684b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00468/004684b8.md)
- 新版 呼出元 1件 [`004183ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004183ec.md) · 呼出先 19件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444a94.md) [`0044aa90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa90.md) [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`004684b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/004684b8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.04% / 新版 92.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acc394",
      "incomplete_value": true,
      "site": "00acc394",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00acc350",
      "incomplete_value": true,
      "site": "00acc350",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1:8"
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
      "definition_site": "00acc458",
      "incomplete_value": true,
      "site": "00acc458",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acc414",
      "incomplete_value": true,
      "site": "00acc414",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:952:8"
              ]
            ]
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
      "00acc380",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ],
    [
      "00acc434",
      "READ",
      [
        "storage",
        "00c24d94",
        null,
        "undefined4"
      ]
    ],
    [
      "00acc448",
      "READ",
      [
        "storage",
        "00297952",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acc380",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "00acc434",
      "READ",
      [
        "storage",
        "00c24dd4",
        null,
        "undefined4"
      ]
    ],
    [
      "00acc448",
      "READ",
      [
        "storage",
        "002978c5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acc3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc304.md#insn-00acc3d0) · [`00acc32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc304.md#insn-00acc32c) · [`00acc334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc304.md#insn-00acc334)
- 新版 `00acc414`（命令位置の公開資料なし） · `00acc370`（命令位置の公開資料なし） · `00acc378`（命令位置の公開資料なし）

~~~diff
- 00acc3d0 ["INT_ADD", "register:40f0:8", ["const:acc3d0:8", "const:4:8"]]
- 00acc3d0 ["CALL", null, ["callee:0044aa90:8"]]
+ 00acc414 ["INT_ADD", "register:40f0:8", ["const:acc414:8", "const:4:8"]]
+ 00acc414 ["CALL", null, ["callee:0044aa90:8"]]
- 00acc3d0 bytes b0f9e597
+ 00acc414 bytes 9ff9e597
- 00acc32c ["INT_ADD", "register:40f0:8", ["const:acc32c:8", "const:4:8"]]
- 00acc32c ["CALL", null, ["callee:00bddd10:8"]]
+ 00acc370 ["INT_ADD", "register:40f0:8", ["const:acc370:8", "const:4:8"]]
+ 00acc370 ["CALL", null, ["callee:00bddd10:8"]]
- 00acc32c bytes 65460494
+ 00acc370 bytes 68460494
- 00acc334 ["COPY", "tmp:0:8", ["const:a1:8"]]
- 00acc334 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00acc334 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00acc334 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00acc378 ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 00acc378 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00acc378 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00acc378 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00acc334 bytes 29850291
+ 00acc378 bytes 29ed0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b941c5da1487ce9fdcdd1ed563680038"></a>

### [`00acc554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc554.md) → [`00acc598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc598.md) FUN_00acc598

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00418a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418a7c.md) [`00acd934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd934.md) · 呼出先 24件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md)
- 新版 呼出元 2件 [`00418a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418a7c.md) [`00acd978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd978.md) · 呼出先 24件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 62.65% / 新版 63.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `store_value` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acc608"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acc608"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acc610"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00acc608",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00acc610",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "00acc65c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00acc67c"
      ]
    ]
  ],
  "added": [
    [
      "00acc64c",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ],
    [
      "00acc654",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "00acc65c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00acc6c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acc5c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc554.md#insn-00acc5c4) · [`00acc608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc554.md#insn-00acc608) · [`00acc610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc554.md#insn-00acc610)
- 新版 `00acc608`（命令位置の公開資料なし）

~~~diff
- 00acc5c4 ["INT_ADD", "register:40f0:8", ["const:acc5c4:8", "const:4:8"]]
- 00acc5c4 ["CALL", null, ["callee:00574ff0:8"]]
+ 00acc608 ["INT_ADD", "register:40f0:8", ["const:acc608:8", "const:4:8"]]
+ 00acc608 ["CALL", null, ["callee:00574ff0:8"]]
- 00acc5c4 bytes 8ba2ea97
+ 00acc608 bytes 7aa2ea97
- 00acc608 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00acc608 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00acc608 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00acc608 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00acc608 bytes ffff06a9
- 00acc610 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:78:8"]]
- 00acc610 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00acc610 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00acc610 bytes ff3f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-245370318a2a26f098bb307efb7d28a6"></a>

### [`00accf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md) → [`00accf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md) FUN_00accf90

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004183ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004183ec.md) [`0041876c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041876c.md) · 呼出先 23件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8e4.md) [`0041c8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8ec.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`00449b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449b7c.md)
- 新版 呼出元 2件 [`004183ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004183ec.md) [`0041876c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041876c.md) · 呼出先 23件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8e4.md) [`0041c8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8ec.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`00449b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449b7c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00accfd8",
      "incomplete_value": true,
      "site": "00accff4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5c1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00accf94",
      "incomplete_value": true,
      "site": "00accfb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:64e:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00acd09c",
      "incomplete_value": true,
      "site": "00acd09c",
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
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acd058",
      "incomplete_value": true,
      "site": "00acd058",
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
            "const:28:8"
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
      "definition_site": "00acd0a0",
      "incomplete_value": true,
      "site": "00acd0a0",
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
            "const:24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acd05c",
      "incomplete_value": true,
      "site": "00acd05c",
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
            "const:24:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00accfd8",
      "READ",
      [
        "storage",
        "0029964e",
        null,
        "string"
      ]
    ],
    [
      "00acd098",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "00acd09c",
      "WRITE",
      [
        "storage",
        "00c24d98",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00accfd8",
      "READ",
      [
        "storage",
        "002995c1",
        null,
        "string"
      ]
    ],
    [
      "00acd098",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00acd09c",
      "WRITE",
      [
        "storage",
        "00c24dd8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acd018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md#insn-00acd018) · [`00accf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md#insn-00accf70) · [`00accf78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md#insn-00accf78)
- 新版 `00acd05c`（命令位置の公開資料なし） · `00accfb4`（命令位置の公開資料なし） · `00accfbc`（命令位置の公開資料なし）

~~~diff
- 00acd018 ["COPY", "register:0:8", ["register:4040:8"]]
- 00acd018 ["INT_ADD", "register:40f0:8", ["const:acd018:8", "const:4:8"]]
- 00acd018 ["CALLIND", null, ["register:0:8"]]
+ 00acd05c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acd05c ["INT_ADD", "register:40f0:8", ["const:acd05c:8", "const:4:8"]]
+ 00acd05c ["CALLIND", null, ["register:0:8"]]
- 00acd018 bytes 00013fd6
+ 00acd05c bytes 00013fd6
- 00accf70 ["INT_ADD", "register:40f0:8", ["const:accf70:8", "const:4:8"]]
- 00accf70 ["CALL", null, ["callee:00565f94:8"]]
+ 00accfb4 ["INT_ADD", "register:40f0:8", ["const:accfb4:8", "const:4:8"]]
+ 00accfb4 ["CALL", null, ["callee:00565f94:8"]]
- 00accf70 bytes 0964ea97
+ 00accfb4 bytes f863ea97
- 00accf78 ["INT_ADD", "register:40f0:8", ["const:accf78:8", "const:4:8"]]
- 00accf78 ["CALL", null, ["callee:00566284:8"]]
+ 00accfbc ["INT_ADD", "register:40f0:8", ["const:accfbc:8", "const:4:8"]]
+ 00accfbc ["CALL", null, ["callee:00566284:8"]]
- 00accf78 bytes c364ea97
+ 00accfbc bytes b264ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-291a6ab62d694375431fbf3a0ef8b4cd"></a>

### [`00acd4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd4b4.md) → [`00acd4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd4f8.md) FUN_00acd4f8

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
      "definition_site": "00acd50c",
      "incomplete_value": false,
      "site": "00acd510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acd4c8",
      "incomplete_value": false,
      "site": "00acd4cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
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
      "00acd510",
      "DATA",
      [
        "storage",
        "00c0f6f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acd510",
      "DATA",
      [
        "storage",
        "00c0f748",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acd4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd4b4.md#insn-00acd4c0) · [`00acd4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd4b4.md#insn-00acd4c8)
- 新版 `00acd504`（命令位置の公開資料なし） · `00acd50c`（命令位置の公開資料なし）

~~~diff
- 00acd4c0 ["INT_ADD", "register:40f0:8", ["const:acd4c0:8", "const:4:8"]]
- 00acd4c0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00acd504 ["INT_ADD", "register:40f0:8", ["const:acd504:8", "const:4:8"]]
+ 00acd504 ["CALL", null, ["callee:00bdb040:8"]]
- 00acd4c0 bytes cc360494
+ 00acd504 bytes cf360494
- 00acd4c8 ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 00acd4c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acd4c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acd4c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acd50c ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00acd50c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acd50c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acd50c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acd4c8 bytes 08e11b91
+ 00acd50c bytes 08211d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-218d1c2db07701f549369a20d813b96b"></a>

### [`00acd4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd4d8.md) → [`00acd51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd51c.md) FUN_00acd51c

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
      "definition_site": "00acd520",
      "incomplete_value": false,
      "site": "00acd524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acd4dc",
      "incomplete_value": false,
      "site": "00acd4e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
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
      "00acd524",
      "DATA",
      [
        "storage",
        "00c0f6f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acd524",
      "DATA",
      [
        "storage",
        "00c0f748",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acd4dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd4d8.md#insn-00acd4dc)
- 新版 `00acd520`（命令位置の公開資料なし）

~~~diff
- 00acd4dc ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 00acd4dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acd4dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acd4dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acd520 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00acd520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acd520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acd520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acd4dc bytes 08e11b91
+ 00acd520 bytes 08211d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84827be85c5bba5b0797facbfdb0fb6c"></a>

### [`00acd538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd538.md) → [`00acd57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd57c.md) FUN_00acd57c

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
      "definition_site": "00acd590",
      "incomplete_value": false,
      "site": "00acd594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acd54c",
      "incomplete_value": false,
      "site": "00acd550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "00acd594",
      "DATA",
      [
        "storage",
        "00c0f778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acd594",
      "DATA",
      [
        "storage",
        "00c0f7c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acd544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd538.md#insn-00acd544) · [`00acd54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd538.md#insn-00acd54c)
- 新版 `00acd588`（命令位置の公開資料なし） · `00acd590`（命令位置の公開資料なし）

~~~diff
- 00acd544 ["INT_ADD", "register:40f0:8", ["const:acd544:8", "const:4:8"]]
- 00acd544 ["CALL", null, ["callee:00bdb040:8"]]
+ 00acd588 ["INT_ADD", "register:40f0:8", ["const:acd588:8", "const:4:8"]]
+ 00acd588 ["CALL", null, ["callee:00bdb040:8"]]
- 00acd544 bytes ab360494
+ 00acd588 bytes ae360494
- 00acd54c ["COPY", "tmp:0:8", ["const:778:8"]]
- 00acd54c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acd54c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acd54c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acd590 ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 00acd590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acd590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acd590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acd54c bytes 08e11d91
+ 00acd590 bytes 08211f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e86252598d07ebc4459f0c841cdeacf"></a>

### [`00acd55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd55c.md) → [`00acd5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd5a0.md) FUN_00acd5a0

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
      "definition_site": "00acd5a4",
      "incomplete_value": false,
      "site": "00acd5a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acd560",
      "incomplete_value": false,
      "site": "00acd564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "00acd5a8",
      "DATA",
      [
        "storage",
        "00c0f778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acd5a8",
      "DATA",
      [
        "storage",
        "00c0f7c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acd560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd55c.md#insn-00acd560)
- 新版 `00acd5a4`（命令位置の公開資料なし）

~~~diff
- 00acd560 ["COPY", "tmp:0:8", ["const:778:8"]]
- 00acd560 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acd560 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acd560 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acd5a4 ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 00acd5a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acd5a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acd5a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acd560 bytes 08e11d91
+ 00acd5a4 bytes 08211f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

