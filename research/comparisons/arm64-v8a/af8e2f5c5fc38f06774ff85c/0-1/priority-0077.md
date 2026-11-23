# v15.7.2 → v15.7.3 · 最優先の変更候補 (77)

[一覧の目次](README.md)

<a id="compare-a0bc11357937516cf69da3522444c9ca"></a>

### [`00ba0720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba0720.md) → [`00ba07e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba07e8.md) FUN_00ba07e8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba2bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2bc8.md) · 呼出先 12件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba2c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2c90.md) · 呼出先 12件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 19.01% / 新版 19.01%

CFGの説明率　旧版 4.08% / 新版 4.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 15件, `store_condition` 4件, `store_destination` 9件, `store_value` 5件, `unresolved_branch_alignment` 163件, `unresolved_call_alignment` 126件, `unresolved_store_alignment` 178件

アドレスに依存する影響 `call_argument_candidate` 12件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba075c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba075c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba07d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba075c",
      "DATA",
      [
        "storage",
        "00c13818",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00ba07cc",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba07d4",
      "READ",
      [
        "storage",
        "00c1b480",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ba0824",
      "DATA",
      [
        "storage",
        "00c138c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00ba0894",
      "READ",
      [
        "storage",
        "00c1bd78",
        null,
        "pointer"
      ]
    ],
    [
      "00ba089c",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba075c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba0720.md#insn-00ba075c) · [`00ba07d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba0720.md#insn-00ba07d0) · [`00ba07dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba0720.md#insn-00ba07dc)

~~~diff
- 00ba075c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ba075c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ba075c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00ba075c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba075c bytes 092000a9
- 00ba07d0 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00ba07d0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ba07d0 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:18:8"]]
- 00ba07d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba07d0 bytes 19a001a9
- 00ba07dc ["COPY", "tmp:0:8", ["const:0:8"]]
- 00ba07dc ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ba07dc ["COPY", "tmp:2:8", ["tmp:0:8"]]
- 00ba07dc ["COPY", "tmp:3:8", ["register:40b0:8"]]
- 00ba07dc bytes c87e00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d575be569f5849b1df3fb5cf6da1078c"></a>

### [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) → [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) FUN_00ba25d8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba7f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7f80.md) [`00ba80b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba80b8.md) · 呼出先 43件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00ba0720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba0720.md) [`00ba2c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2c54.md) [`00ba2d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2d80.md) [`00ba2eac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2eac.md)
- 新版 呼出元 2件 [`00ba8048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8048.md) [`00ba8180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8180.md) · 呼出先 43件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00ba07e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba07e8.md) [`00ba2d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2d1c.md) [`00ba2e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2e48.md) [`00ba2f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2f74.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 13件

アドレスに依存する影響 `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba2608",
      "incomplete_value": false,
      "site": "00ba2608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2540",
      "incomplete_value": false,
      "site": "00ba2540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:818:8"
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
      "definition_site": "00ba27b4",
      "incomplete_value": true,
      "site": "00ba27b4",
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
      "definition_site": "00ba26ec",
      "incomplete_value": true,
      "site": "00ba26ec",
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
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba27f0",
      "incomplete_value": true,
      "site": "00ba27f4",
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
      "definition_site": "00ba2728",
      "incomplete_value": true,
      "site": "00ba272c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ba2608",
      "DATA",
      [
        "storage",
        "00c13818",
        null,
        "undefined *"
      ]
    ],
    [
      "00ba2698",
      "READ",
      [
        "storage",
        "010a29e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba26a0",
      "READ",
      [
        "storage",
        "010a29d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba2608",
      "DATA",
      [
        "storage",
        "00c138c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00ba2698",
      "READ",
      [
        "storage",
        "010a2aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba26a0",
      "READ",
      [
        "storage",
        "010a2a98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba26a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md#insn-00ba26a8) · [`00ba2820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md#insn-00ba2820) · [`00ba2868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md#insn-00ba2868)
- 新版 `00ba2770`（命令位置の公開資料なし） · `00ba28e8`（命令位置の公開資料なし） · `00ba2930`（命令位置の公開資料なし）

~~~diff
- 00ba26a8 ["INT_ADD", "register:40f0:8", ["const:ba26a8:8", "const:4:8"]]
- 00ba26a8 ["CALL", null, ["callee:00ba2f74:8"]]
+ 00ba2770 ["INT_ADD", "register:40f0:8", ["const:ba2770:8", "const:4:8"]]
+ 00ba2770 ["CALL", null, ["callee:00ba2f74:8"]]
- 00ba26a8 bytes 01020094
+ 00ba2770 bytes 01020094
- 00ba2820 ["INT_ADD", "register:40f0:8", ["const:ba2820:8", "const:4:8"]]
- 00ba2820 ["CALL", null, ["callee:00ba3a00:8"]]
+ 00ba28e8 ["INT_ADD", "register:40f0:8", ["const:ba28e8:8", "const:4:8"]]
+ 00ba28e8 ["CALL", null, ["callee:00ba3a00:8"]]
- 00ba2820 bytes 46040094
+ 00ba28e8 bytes 46040094
- 00ba2868 ["INT_ADD", "register:40f0:8", ["const:ba2868:8", "const:4:8"]]
- 00ba2868 ["CALL", null, ["callee:00ba3d3c:8"]]
+ 00ba2930 ["INT_ADD", "register:40f0:8", ["const:ba2930:8", "const:4:8"]]
+ 00ba2930 ["CALL", null, ["callee:00ba3d3c:8"]]
- 00ba2868 bytes 03050094
+ 00ba2930 bytes 03050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e18e39e885f79a05f9904f62cc8ef31"></a>

### [`00ba2bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2bc8.md) → [`00ba2c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2c90.md) _ZNSt6__ndk16locale7classicEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be17d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be17d0.md) · 呼出先 3件 [`00ba0720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba0720.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`00be1880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1880.md) · 呼出先 3件 [`00ba07e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba07e8.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 68.97% / 新版 68.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba2cf8",
      "incomplete_value": false,
      "site": "00ba2cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2c30",
      "incomplete_value": false,
      "site": "00ba2c30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "definition_site": "00ba2ccc",
      "incomplete_value": false,
      "site": "00ba2cd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2c04",
      "incomplete_value": false,
      "site": "00ba2c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "definition_site": "00ba2ce4",
      "incomplete_value": false,
      "site": "00ba2ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2c1c",
      "incomplete_value": false,
      "site": "00ba2c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "00ba2ca8",
      "READ",
      [
        "storage",
        "010a29e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba2cb4",
      "DATA",
      [
        "storage",
        "010a29d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba2ccc",
      "PARAM",
      [
        "storage",
        "010a29e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ba2ca8",
      "READ",
      [
        "storage",
        "010a2aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba2cb4",
      "DATA",
      [
        "storage",
        "010a2a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba2ccc",
      "PARAM",
      [
        "storage",
        "010a2aa0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2bc8.md#insn-00ba2c08) · [`00ba2c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2bc8.md#insn-00ba2c20) · [`00ba2c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2bc8.md#insn-00ba2c30)
- 新版 `00ba2cd0`（命令位置の公開資料なし） · `00ba2ce8`（命令位置の公開資料なし） · `00ba2cf8`（命令位置の公開資料なし）

~~~diff
- 00ba2c08 ["INT_ADD", "register:40f0:8", ["const:ba2c08:8", "const:4:8"]]
- 00ba2c08 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00ba2cd0 ["INT_ADD", "register:40f0:8", ["const:ba2cd0:8", "const:4:8"]]
+ 00ba2cd0 ["CALL", null, ["callee:00bdafb0:8"]]
- 00ba2c08 bytes bee00094
+ 00ba2cd0 bytes b8e00094
- 00ba2c20 ["INT_ADD", "register:40f0:8", ["const:ba2c20:8", "const:4:8"]]
- 00ba2c20 ["CALL", null, ["callee:00ba07e8:8"]]
+ 00ba2ce8 ["INT_ADD", "register:40f0:8", ["const:ba2ce8:8", "const:4:8"]]
+ 00ba2ce8 ["CALL", null, ["callee:00ba07e8:8"]]
- 00ba2c20 bytes c0f6ff97
+ 00ba2ce8 bytes c0f6ff97
- 00ba2c30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d8:8"]]
- 00ba2c30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00ba2cf8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a98:8"]]
+ 00ba2cf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00ba2c30 bytes 13ed04f9
+ 00ba2cf8 bytes 134d05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98fd05cbc9f98218a31701ddd561e36d"></a>

### [`00ba2c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2c54.md) → [`00ba2d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2d1c.md) FUN_00ba2d1c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba2d40",
      "incomplete_value": true,
      "site": "00ba2d44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2c78",
      "incomplete_value": true,
      "site": "00ba2c7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:480:8"
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
      "definition_site": "00ba2d4c",
      "incomplete_value": true,
      "site": "00ba2d50",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba2c84",
      "incomplete_value": true,
      "site": "00ba2c88",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba2d74",
      "incomplete_value": true,
      "site": "00ba2d78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2cac",
      "incomplete_value": true,
      "site": "00ba2cb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:480:8"
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
      "00ba2d40",
      "READ",
      [
        "storage",
        "00c1b480",
        null,
        "pointer"
      ]
    ],
    [
      "00ba2d44",
      "DATA",
      [
        "storage",
        "010a2750",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba2d48",
      "READ",
      [
        "storage",
        "010a2750",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba2d40",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ],
    [
      "00ba2d44",
      "DATA",
      [
        "storage",
        "010a2810",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba2d48",
      "READ",
      [
        "storage",
        "010a2810",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2cb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2c54.md#insn-00ba2cb0) · [`00ba2c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2c54.md#insn-00ba2c78) · [`00ba2ca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2c54.md#insn-00ba2ca0)
- 新版 `00ba2d78`（命令位置の公開資料なし） · `00ba2d40`（命令位置の公開資料なし） · `00ba2d68`（命令位置の公開資料なし）

~~~diff
- 00ba2cb0 ["INT_ADD", "register:40f0:8", ["const:ba2cb0:8", "const:4:8"]]
- 00ba2cb0 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba2d78 ["INT_ADD", "register:40f0:8", ["const:ba2d78:8", "const:4:8"]]
+ 00ba2d78 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba2cb0 bytes 4cf80094
+ 00ba2d78 bytes 46f80094
- 00ba2c78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00ba2c78 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba2d40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
+ 00ba2d40 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba2c78 bytes 944242f9
+ 00ba2d40 bytes 949a42f9
- 00ba2ca0 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba2d68 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba2ca0 bytes e21c0b10
+ 00ba2d68 bytes e21c0b10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11f7eb4773ffb781b8ee40ab02c5f523"></a>

### [`00ba2d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2d80.md) → [`00ba2e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2e48.md) FUN_00ba2e48

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba2e6c",
      "incomplete_value": true,
      "site": "00ba2e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2da4",
      "incomplete_value": true,
      "site": "00ba2da8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00ba2e78",
      "incomplete_value": true,
      "site": "00ba2e7c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba2db0",
      "incomplete_value": true,
      "site": "00ba2db4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba2ea0",
      "incomplete_value": true,
      "site": "00ba2ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2dd8",
      "incomplete_value": true,
      "site": "00ba2ddc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "00ba2e6c",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba2e70",
      "DATA",
      [
        "storage",
        "010a2760",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba2e74",
      "READ",
      [
        "storage",
        "010a2760",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba2e6c",
      "READ",
      [
        "storage",
        "00c1bd88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba2e70",
      "DATA",
      [
        "storage",
        "010a2820",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba2e74",
      "READ",
      [
        "storage",
        "010a2820",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2ddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2d80.md#insn-00ba2ddc) · [`00ba2da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2d80.md#insn-00ba2da4) · [`00ba2dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2d80.md#insn-00ba2dcc)
- 新版 `00ba2ea4`（命令位置の公開資料なし） · `00ba2e6c`（命令位置の公開資料なし） · `00ba2e94`（命令位置の公開資料なし）

~~~diff
- 00ba2ddc ["INT_ADD", "register:40f0:8", ["const:ba2ddc:8", "const:4:8"]]
- 00ba2ddc ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba2ea4 ["INT_ADD", "register:40f0:8", ["const:ba2ea4:8", "const:4:8"]]
+ 00ba2ea4 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba2ddc bytes 01f80094
+ 00ba2ea4 bytes fbf70094
- 00ba2da4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd8:8"]]
- 00ba2da4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba2e6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
+ 00ba2e6c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba2da4 bytes 946e46f9
+ 00ba2e6c bytes 94c646f9
- 00ba2dcc ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba2e94 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba2dcc bytes 82130b10
+ 00ba2e94 bytes 82130b10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53afb3afe88bb3061ad5549f4e93cad3"></a>

### [`00ba2eac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2eac.md) → [`00ba2f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2f74.md) FUN_00ba2f74

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba2f98",
      "incomplete_value": true,
      "site": "00ba2f9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2ed0",
      "incomplete_value": true,
      "site": "00ba2ed4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "definition_site": "00ba2fa4",
      "incomplete_value": true,
      "site": "00ba2fa8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba2edc",
      "incomplete_value": true,
      "site": "00ba2ee0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba2fcc",
      "incomplete_value": true,
      "site": "00ba2fd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2f04",
      "incomplete_value": true,
      "site": "00ba2f08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "00ba2f98",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00ba2f9c",
      "DATA",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba2fa0",
      "READ",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba2f98",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba2f9c",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba2fa0",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2f08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2eac.md#insn-00ba2f08) · [`00ba2ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2eac.md#insn-00ba2ed0) · [`00ba2ef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2eac.md#insn-00ba2ef8)
- 新版 `00ba2fd0`（命令位置の公開資料なし） · `00ba2f98`（命令位置の公開資料なし） · `00ba2fc0`（命令位置の公開資料なし）

~~~diff
- 00ba2f08 ["INT_ADD", "register:40f0:8", ["const:ba2f08:8", "const:4:8"]]
- 00ba2f08 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba2fd0 ["INT_ADD", "register:40f0:8", ["const:ba2fd0:8", "const:4:8"]]
+ 00ba2fd0 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba2f08 bytes b6f70094
+ 00ba2fd0 bytes b0f70094
- 00ba2ed0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d40:8"]]
- 00ba2ed0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba2f98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
+ 00ba2f98 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba2ed0 bytes 94a246f9
+ 00ba2f98 bytes 94fa46f9
- 00ba2ef8 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba2fc0 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba2ef8 bytes 220a0b10
+ 00ba2fc0 bytes 220a0b10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d818b0084dd8e96e4b225f68780ebab"></a>

### [`00ba2fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2fd8.md) → [`00ba30a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba30a0.md) FUN_00ba30a0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba30c4",
      "incomplete_value": true,
      "site": "00ba30c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba2ffc",
      "incomplete_value": true,
      "site": "00ba3000",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00ba30d0",
      "incomplete_value": true,
      "site": "00ba30d4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3008",
      "incomplete_value": true,
      "site": "00ba300c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba30f8",
      "incomplete_value": true,
      "site": "00ba30fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3030",
      "incomplete_value": true,
      "site": "00ba3034",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00ba30c4",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00ba30c8",
      "DATA",
      [
        "storage",
        "010a2a00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba30cc",
      "READ",
      [
        "storage",
        "010a2a00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba30c4",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba30c8",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba30cc",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2fd8.md#insn-00ba3034) · [`00ba2ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2fd8.md#insn-00ba2ffc) · [`00ba3024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2fd8.md#insn-00ba3024)
- 新版 `00ba30fc`（命令位置の公開資料なし） · `00ba30c4`（命令位置の公開資料なし） · `00ba30ec`（命令位置の公開資料なし）

~~~diff
- 00ba3034 ["INT_ADD", "register:40f0:8", ["const:ba3034:8", "const:4:8"]]
- 00ba3034 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba30fc ["INT_ADD", "register:40f0:8", ["const:ba30fc:8", "const:4:8"]]
+ 00ba30fc ["CALL", null, ["callee:00be0e90:8"]]
- 00ba3034 bytes 6bf70094
+ 00ba30fc bytes 65f70094
- 00ba2ffc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
- 00ba2ffc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba30c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc0:8"]]
+ 00ba30c4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba2ffc bytes 940a46f9
+ 00ba30c4 bytes 946246f9
- 00ba3024 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba30ec ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba3024 bytes c2000b10
+ 00ba30ec bytes c2000b10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91d780b53bf28a1e7113b345654c0fb3"></a>

### [`00ba3104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3104.md) → [`00ba31cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba31cc.md) FUN_00ba31cc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba31f0",
      "incomplete_value": true,
      "site": "00ba31f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3128",
      "incomplete_value": true,
      "site": "00ba312c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9b0:8"
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
      "definition_site": "00ba31fc",
      "incomplete_value": true,
      "site": "00ba3200",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3134",
      "incomplete_value": true,
      "site": "00ba3138",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3224",
      "incomplete_value": true,
      "site": "00ba3228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba315c",
      "incomplete_value": true,
      "site": "00ba3160",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9b0:8"
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
      "00ba31f0",
      "READ",
      [
        "storage",
        "00c1b9b0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba31f4",
      "DATA",
      [
        "storage",
        "010a2a20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba31f8",
      "READ",
      [
        "storage",
        "010a2a20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba31f0",
      "READ",
      [
        "storage",
        "00c1ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00ba31f4",
      "DATA",
      [
        "storage",
        "010a2ae0",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba31f8",
      "READ",
      [
        "storage",
        "010a2ae0",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3104.md#insn-00ba3160) · [`00ba3128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3104.md#insn-00ba3128) · [`00ba3150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3104.md#insn-00ba3150)
- 新版 `00ba3228`（命令位置の公開資料なし） · `00ba31f0`（命令位置の公開資料なし） · `00ba3218`（命令位置の公開資料なし）

~~~diff
- 00ba3160 ["INT_ADD", "register:40f0:8", ["const:ba3160:8", "const:4:8"]]
- 00ba3160 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba3228 ["INT_ADD", "register:40f0:8", ["const:ba3228:8", "const:4:8"]]
+ 00ba3228 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba3160 bytes 20f70094
+ 00ba3228 bytes 1af70094
- 00ba3128 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b0:8"]]
- 00ba3128 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba31f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a60:8"]]
+ 00ba31f0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3128 bytes 94da44f9
+ 00ba31f0 bytes 943245f9
- 00ba3150 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba3218 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba3150 bytes 62f70a10
+ 00ba3218 bytes 62f70a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7653e9d05d6202615ce4fedfa5692f8"></a>

### [`00ba3230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3230.md) → [`00ba32f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba32f8.md) FUN_00ba32f8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba331c",
      "incomplete_value": true,
      "site": "00ba3320",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3254",
      "incomplete_value": true,
      "site": "00ba3258",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
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
      "definition_site": "00ba3328",
      "incomplete_value": true,
      "site": "00ba332c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3260",
      "incomplete_value": true,
      "site": "00ba3264",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3350",
      "incomplete_value": true,
      "site": "00ba3354",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3288",
      "incomplete_value": true,
      "site": "00ba328c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
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
      "00ba331c",
      "READ",
      [
        "storage",
        "00c1bc78",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3320",
      "DATA",
      [
        "storage",
        "010a2a30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3324",
      "READ",
      [
        "storage",
        "010a2a30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba331c",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3320",
      "DATA",
      [
        "storage",
        "010a2af0",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3324",
      "READ",
      [
        "storage",
        "010a2af0",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba328c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3230.md#insn-00ba328c) · [`00ba3254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3230.md#insn-00ba3254) · [`00ba327c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3230.md#insn-00ba327c)
- 新版 `00ba3354`（命令位置の公開資料なし） · `00ba331c`（命令位置の公開資料なし） · `00ba3344`（命令位置の公開資料なし）

~~~diff
- 00ba328c ["INT_ADD", "register:40f0:8", ["const:ba328c:8", "const:4:8"]]
- 00ba328c ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba3354 ["INT_ADD", "register:40f0:8", ["const:ba3354:8", "const:4:8"]]
+ 00ba3354 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba328c bytes d5f60094
+ 00ba3354 bytes cff60094
- 00ba3254 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c78:8"]]
- 00ba3254 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba331c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
+ 00ba331c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3254 bytes 943e46f9
+ 00ba331c bytes 949646f9
- 00ba327c ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba3344 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba327c bytes 02ee0a10
+ 00ba3344 bytes 02ee0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c5025880969785d9a2ff9a8948902cd"></a>

### [`00ba335c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba335c.md) → [`00ba3424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3424.md) FUN_00ba3424

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3448",
      "incomplete_value": true,
      "site": "00ba344c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3380",
      "incomplete_value": true,
      "site": "00ba3384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf8:8"
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
      "definition_site": "00ba3454",
      "incomplete_value": true,
      "site": "00ba3458",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba338c",
      "incomplete_value": true,
      "site": "00ba3390",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba347c",
      "incomplete_value": true,
      "site": "00ba3480",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba33b4",
      "incomplete_value": true,
      "site": "00ba33b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf8:8"
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
      "00ba3448",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba344c",
      "DATA",
      [
        "storage",
        "010a2a40",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3450",
      "READ",
      [
        "storage",
        "010a2a40",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3448",
      "READ",
      [
        "storage",
        "00c1bda8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba344c",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3450",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba33b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba335c.md#insn-00ba33b8) · [`00ba3380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba335c.md#insn-00ba3380) · [`00ba33a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba335c.md#insn-00ba33a8)
- 新版 `00ba3480`（命令位置の公開資料なし） · `00ba3448`（命令位置の公開資料なし） · `00ba3470`（命令位置の公開資料なし）

~~~diff
- 00ba33b8 ["INT_ADD", "register:40f0:8", ["const:ba33b8:8", "const:4:8"]]
- 00ba33b8 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba3480 ["INT_ADD", "register:40f0:8", ["const:ba3480:8", "const:4:8"]]
+ 00ba3480 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba33b8 bytes 8af60094
+ 00ba3480 bytes 84f60094
- 00ba3380 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf8:8"]]
- 00ba3380 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3448 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:da8:8"]]
+ 00ba3448 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3380 bytes 947e46f9
+ 00ba3448 bytes 94d646f9
- 00ba33a8 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba3470 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba33a8 bytes a2e40a10
+ 00ba3470 bytes a2e40a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f87e45413538c04d61ff98b3096b81ea"></a>

### [`00ba3488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3488.md) → [`00ba3550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3550.md) FUN_00ba3550

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3574",
      "incomplete_value": true,
      "site": "00ba3578",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba34ac",
      "incomplete_value": true,
      "site": "00ba34b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
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
      "definition_site": "00ba3580",
      "incomplete_value": true,
      "site": "00ba3584",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba34b8",
      "incomplete_value": true,
      "site": "00ba34bc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba35a8",
      "incomplete_value": true,
      "site": "00ba35ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba34e0",
      "incomplete_value": true,
      "site": "00ba34e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
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
      "00ba3574",
      "READ",
      [
        "storage",
        "00c1bd08",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3578",
      "DATA",
      [
        "storage",
        "010a2a60",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba357c",
      "READ",
      [
        "storage",
        "010a2a60",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3574",
      "READ",
      [
        "storage",
        "00c1bdb8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3578",
      "DATA",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba357c",
      "READ",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba34e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3488.md#insn-00ba34e4) · [`00ba34ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3488.md#insn-00ba34ac) · [`00ba34d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3488.md#insn-00ba34d4)
- 新版 `00ba35ac`（命令位置の公開資料なし） · `00ba3574`（命令位置の公開資料なし） · `00ba359c`（命令位置の公開資料なし）

~~~diff
- 00ba34e4 ["INT_ADD", "register:40f0:8", ["const:ba34e4:8", "const:4:8"]]
- 00ba34e4 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba35ac ["INT_ADD", "register:40f0:8", ["const:ba35ac:8", "const:4:8"]]
+ 00ba35ac ["CALL", null, ["callee:00be0e90:8"]]
- 00ba34e4 bytes 3ff60094
+ 00ba35ac bytes 39f60094
- 00ba34ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d08:8"]]
- 00ba34ac ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3574 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db8:8"]]
+ 00ba3574 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba34ac bytes 948646f9
+ 00ba3574 bytes 94de46f9
- 00ba34d4 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba359c ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba34d4 bytes 42db0a10
+ 00ba359c bytes 42db0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c07dfbf83610e7e4c2786a7bab77566"></a>

### [`00ba35b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba35b4.md) → [`00ba367c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba367c.md) FUN_00ba367c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba36a0",
      "incomplete_value": true,
      "site": "00ba36a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba35d8",
      "incomplete_value": true,
      "site": "00ba35dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
      "definition_site": "00ba36ac",
      "incomplete_value": true,
      "site": "00ba36b0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba35e4",
      "incomplete_value": true,
      "site": "00ba35e8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba36d4",
      "incomplete_value": true,
      "site": "00ba36d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba360c",
      "incomplete_value": true,
      "site": "00ba3610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
      "00ba36a0",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00ba36a4",
      "DATA",
      [
        "storage",
        "010a2a50",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba36a8",
      "READ",
      [
        "storage",
        "010a2a50",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba36a0",
      "READ",
      [
        "storage",
        "00c1bdc8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba36a4",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba36a8",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba35b4.md#insn-00ba3610) · [`00ba35d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba35b4.md#insn-00ba35d8) · [`00ba3600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba35b4.md#insn-00ba3600)
- 新版 `00ba36d8`（命令位置の公開資料なし） · `00ba36a0`（命令位置の公開資料なし） · `00ba36c8`（命令位置の公開資料なし）

~~~diff
- 00ba3610 ["INT_ADD", "register:40f0:8", ["const:ba3610:8", "const:4:8"]]
- 00ba3610 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba36d8 ["INT_ADD", "register:40f0:8", ["const:ba36d8:8", "const:4:8"]]
+ 00ba36d8 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba3610 bytes f4f50094
+ 00ba36d8 bytes eef50094
- 00ba35d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d18:8"]]
- 00ba35d8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba36a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc8:8"]]
+ 00ba36a0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba35d8 bytes 948e46f9
+ 00ba36a0 bytes 94e646f9
- 00ba3600 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba36c8 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba3600 bytes e2d10a10
+ 00ba36c8 bytes e2d10a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bb67dce747c9aac89081597696098bf"></a>

### [`00ba36e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba36e0.md) → [`00ba37a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba37a8.md) FUN_00ba37a8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba37cc",
      "incomplete_value": true,
      "site": "00ba37d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3704",
      "incomplete_value": true,
      "site": "00ba3708",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
      "definition_site": "00ba37d8",
      "incomplete_value": true,
      "site": "00ba37dc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3710",
      "incomplete_value": true,
      "site": "00ba3714",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3800",
      "incomplete_value": true,
      "site": "00ba3804",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3738",
      "incomplete_value": true,
      "site": "00ba373c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
      "00ba37cc",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00ba37d0",
      "DATA",
      [
        "storage",
        "010a2a70",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba37d4",
      "READ",
      [
        "storage",
        "010a2a70",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba37cc",
      "READ",
      [
        "storage",
        "00c1bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba37d0",
      "DATA",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba37d4",
      "READ",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba373c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba36e0.md#insn-00ba373c) · [`00ba3704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba36e0.md#insn-00ba3704) · [`00ba372c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba36e0.md#insn-00ba372c)
- 新版 `00ba3804`（命令位置の公開資料なし） · `00ba37cc`（命令位置の公開資料なし） · `00ba37f4`（命令位置の公開資料なし）

~~~diff
- 00ba373c ["INT_ADD", "register:40f0:8", ["const:ba373c:8", "const:4:8"]]
- 00ba373c ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba3804 ["INT_ADD", "register:40f0:8", ["const:ba3804:8", "const:4:8"]]
+ 00ba3804 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba373c bytes a9f50094
+ 00ba3804 bytes a3f50094
- 00ba3704 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
- 00ba3704 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba37cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd8:8"]]
+ 00ba37cc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3704 bytes 949646f9
+ 00ba37cc bytes 94ee46f9
- 00ba372c ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba37f4 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba372c bytes 82c80a10
+ 00ba37f4 bytes 82c80a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c72dbb5d022dacba0af18019c7a477bc"></a>

### [`00ba380c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba380c.md) → [`00ba38d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba38d4.md) FUN_00ba38d4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba38f8",
      "incomplete_value": true,
      "site": "00ba38fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3830",
      "incomplete_value": true,
      "site": "00ba3834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "definition_site": "00ba3904",
      "incomplete_value": true,
      "site": "00ba3908",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba383c",
      "incomplete_value": true,
      "site": "00ba3840",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba392c",
      "incomplete_value": true,
      "site": "00ba3930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3864",
      "incomplete_value": true,
      "site": "00ba3868",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "00ba38f8",
      "READ",
      [
        "storage",
        "00c1bc88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba38fc",
      "DATA",
      [
        "storage",
        "010a2a80",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3900",
      "READ",
      [
        "storage",
        "010a2a80",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba38f8",
      "READ",
      [
        "storage",
        "00c1bd38",
        null,
        "pointer"
      ]
    ],
    [
      "00ba38fc",
      "DATA",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3900",
      "READ",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba380c.md#insn-00ba3868) · [`00ba3830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba380c.md#insn-00ba3830) · [`00ba3858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba380c.md#insn-00ba3858)
- 新版 `00ba3930`（命令位置の公開資料なし） · `00ba38f8`（命令位置の公開資料なし） · `00ba3920`（命令位置の公開資料なし）

~~~diff
- 00ba3868 ["INT_ADD", "register:40f0:8", ["const:ba3868:8", "const:4:8"]]
- 00ba3868 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba3930 ["INT_ADD", "register:40f0:8", ["const:ba3930:8", "const:4:8"]]
+ 00ba3930 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba3868 bytes 5ef50094
+ 00ba3930 bytes 58f50094
- 00ba3830 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
- 00ba3830 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba38f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d38:8"]]
+ 00ba38f8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3830 bytes 944646f9
+ 00ba38f8 bytes 949e46f9
- 00ba3858 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba3920 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba3858 bytes 22bf0a10
+ 00ba3920 bytes 22bf0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f843f8d968d5bdcd5f5888dc76290c43"></a>

### [`00ba3938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3938.md) → [`00ba3a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3a00.md) FUN_00ba3a00

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3a24",
      "incomplete_value": true,
      "site": "00ba3a28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba395c",
      "incomplete_value": true,
      "site": "00ba3960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
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
      "definition_site": "00ba3a30",
      "incomplete_value": true,
      "site": "00ba3a34",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3968",
      "incomplete_value": true,
      "site": "00ba396c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3a58",
      "incomplete_value": true,
      "site": "00ba3a5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3990",
      "incomplete_value": true,
      "site": "00ba3994",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
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
      "00ba3a24",
      "READ",
      [
        "storage",
        "00c1bc98",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3a28",
      "DATA",
      [
        "storage",
        "010a2a90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3a2c",
      "READ",
      [
        "storage",
        "010a2a90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3a24",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3a28",
      "DATA",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3a2c",
      "READ",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3938.md#insn-00ba3994) · [`00ba395c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3938.md#insn-00ba395c) · [`00ba3984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3938.md#insn-00ba3984)
- 新版 `00ba3a5c`（命令位置の公開資料なし） · `00ba3a24`（命令位置の公開資料なし） · `00ba3a4c`（命令位置の公開資料なし）

~~~diff
- 00ba3994 ["INT_ADD", "register:40f0:8", ["const:ba3994:8", "const:4:8"]]
- 00ba3994 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba3a5c ["INT_ADD", "register:40f0:8", ["const:ba3a5c:8", "const:4:8"]]
+ 00ba3a5c ["CALL", null, ["callee:00be0e90:8"]]
- 00ba3994 bytes 13f50094
+ 00ba3a5c bytes 0df50094
- 00ba395c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
- 00ba395c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3a24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d48:8"]]
+ 00ba3a24 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba395c bytes 944e46f9
+ 00ba3a24 bytes 94a646f9
- 00ba3984 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba3a4c ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba3984 bytes c2b50a10
+ 00ba3a4c bytes c2b50a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7aa9ca7ccd0bd8804e9b32212fe6b365"></a>

### [`00ba3a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3a64.md) → [`00ba3b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3b2c.md) FUN_00ba3b2c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3b50",
      "incomplete_value": true,
      "site": "00ba3b54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3a88",
      "incomplete_value": true,
      "site": "00ba3a8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb0:8"
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
      "definition_site": "00ba3b5c",
      "incomplete_value": true,
      "site": "00ba3b60",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3a94",
      "incomplete_value": true,
      "site": "00ba3a98",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3b84",
      "incomplete_value": true,
      "site": "00ba3b88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3abc",
      "incomplete_value": true,
      "site": "00ba3ac0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb0:8"
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
      "00ba3b50",
      "READ",
      [
        "storage",
        "00c1bcb0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3b54",
      "DATA",
      [
        "storage",
        "010a27f0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3b58",
      "READ",
      [
        "storage",
        "010a27f0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3b50",
      "READ",
      [
        "storage",
        "00c1bd60",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3b54",
      "DATA",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3b58",
      "READ",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3a64.md#insn-00ba3ac0) · [`00ba3a88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3a64.md#insn-00ba3a88) · [`00ba3ab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3a64.md#insn-00ba3ab0)
- 新版 `00ba3b88`（命令位置の公開資料なし） · `00ba3b50`（命令位置の公開資料なし） · `00ba3b78`（命令位置の公開資料なし）

~~~diff
- 00ba3ac0 ["INT_ADD", "register:40f0:8", ["const:ba3ac0:8", "const:4:8"]]
- 00ba3ac0 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba3b88 ["INT_ADD", "register:40f0:8", ["const:ba3b88:8", "const:4:8"]]
+ 00ba3b88 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba3ac0 bytes c8f40094
+ 00ba3b88 bytes c2f40094
- 00ba3a88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb0:8"]]
- 00ba3a88 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3b50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d60:8"]]
+ 00ba3b50 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3a88 bytes 945a46f9
+ 00ba3b50 bytes 94b246f9
- 00ba3ab0 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba3b78 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba3ab0 bytes 62ac0a10
+ 00ba3b78 bytes 62ac0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c967ab3625a6bf7e1b9e2d1c114525ec"></a>

### [`00ba3b90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3b90.md) → [`00ba3c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3c58.md) FUN_00ba3c58

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 1件 [`00be17e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be17e0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 1件 [`00be1890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1890.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3c88",
      "incomplete_value": true,
      "site": "00ba3c88",
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
      "definition_site": "00ba3bc0",
      "incomplete_value": true,
      "site": "00ba3bc0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ba3c78",
      "READ",
      [
        "storage",
        "00c1be68",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3c88",
      "DATA",
      [
        "storage",
        "00c15558",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00ba3c78",
      "READ",
      [
        "storage",
        "00c1bf18",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3c88",
      "DATA",
      [
        "storage",
        "00c15608",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3b90.md#insn-00ba3bb0) · [`00ba3bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3b90.md#insn-00ba3bb4) · [`00ba3bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3b90.md#insn-00ba3bb8)
- 新版 `00ba3c78`（命令位置の公開資料なし）

~~~diff
- 00ba3bb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e68:8"]]
- 00ba3bb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3c78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f18:8"]]
+ 00ba3c78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3bb0 bytes 083547f9
+ 00ba3c78 bytes 088d47f9
- 00ba3bb4 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00ba3bb4 bytes f50300aa
- 00ba3bb8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00ba3bb8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-330e035c6b9e338eb663aece75302b38"></a>

### [`00ba3c74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3c74.md) → [`00ba3d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3d3c.md) FUN_00ba3d3c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3d60",
      "incomplete_value": true,
      "site": "00ba3d64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3c98",
      "incomplete_value": true,
      "site": "00ba3c9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
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
      "definition_site": "00ba3d6c",
      "incomplete_value": true,
      "site": "00ba3d70",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3ca4",
      "incomplete_value": true,
      "site": "00ba3ca8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3d94",
      "incomplete_value": true,
      "site": "00ba3d98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3ccc",
      "incomplete_value": true,
      "site": "00ba3cd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
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
      "00ba3d60",
      "READ",
      [
        "storage",
        "00c1bca8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3d64",
      "DATA",
      [
        "storage",
        "010a2800",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3d68",
      "READ",
      [
        "storage",
        "010a2800",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3d60",
      "READ",
      [
        "storage",
        "00c1bd58",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3d64",
      "DATA",
      [
        "storage",
        "010a28c0",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3d68",
      "READ",
      [
        "storage",
        "010a28c0",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3cd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3c74.md#insn-00ba3cd0) · [`00ba3c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3c74.md#insn-00ba3c98) · [`00ba3cc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3c74.md#insn-00ba3cc0)
- 新版 `00ba3d98`（命令位置の公開資料なし） · `00ba3d60`（命令位置の公開資料なし） · `00ba3d88`（命令位置の公開資料なし）

~~~diff
- 00ba3cd0 ["INT_ADD", "register:40f0:8", ["const:ba3cd0:8", "const:4:8"]]
- 00ba3cd0 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba3d98 ["INT_ADD", "register:40f0:8", ["const:ba3d98:8", "const:4:8"]]
+ 00ba3d98 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba3cd0 bytes 44f40094
+ 00ba3d98 bytes 3ef40094
- 00ba3c98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
- 00ba3c98 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3d60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d58:8"]]
+ 00ba3d60 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3c98 bytes 945646f9
+ 00ba3d60 bytes 94ae46f9
- 00ba3cc0 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba3d88 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba3cc0 bytes e29b0a10
+ 00ba3d88 bytes e29b0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-752b1700d4eecd0d5e71dce0b2f21857"></a>

### [`00ba3da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3da0.md) → [`00ba3e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3e68.md) FUN_00ba3e68

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 1件 [`00be17f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be17f0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 1件 [`00be18a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3e98",
      "incomplete_value": true,
      "site": "00ba3e98",
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
      "definition_site": "00ba3dd0",
      "incomplete_value": true,
      "site": "00ba3dd0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ba3e88",
      "READ",
      [
        "storage",
        "00c1be70",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3e98",
      "DATA",
      [
        "storage",
        "00c155e0",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00ba3e88",
      "READ",
      [
        "storage",
        "00c1bf20",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3e98",
      "DATA",
      [
        "storage",
        "00c15690",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3da0.md#insn-00ba3dc0) · [`00ba3dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3da0.md#insn-00ba3dc4) · [`00ba3dc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3da0.md#insn-00ba3dc8)
- 新版 `00ba3e88`（命令位置の公開資料なし）

~~~diff
- 00ba3dc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 00ba3dc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3e88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
+ 00ba3e88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3dc0 bytes 083947f9
+ 00ba3e88 bytes 089147f9
- 00ba3dc4 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00ba3dc4 bytes f50300aa
- 00ba3dc8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00ba3dc8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c3e393ff28805ae2567019344dc901a"></a>

### [`00ba3e84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3e84.md) → [`00ba3f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3f4c.md) FUN_00ba3f4c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3f70",
      "incomplete_value": true,
      "site": "00ba3f74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3ea8",
      "incomplete_value": true,
      "site": "00ba3eac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "definition_site": "00ba3f7c",
      "incomplete_value": true,
      "site": "00ba3f80",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3eb4",
      "incomplete_value": true,
      "site": "00ba3eb8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3fa4",
      "incomplete_value": true,
      "site": "00ba3fa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3edc",
      "incomplete_value": true,
      "site": "00ba3ee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00ba3f70",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3f74",
      "DATA",
      [
        "storage",
        "010a2810",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3f78",
      "READ",
      [
        "storage",
        "010a2810",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3f70",
      "READ",
      [
        "storage",
        "00c1bd70",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3f74",
      "DATA",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3f78",
      "READ",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3e84.md#insn-00ba3ee0) · [`00ba3ea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3e84.md#insn-00ba3ea8) · [`00ba3ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3e84.md#insn-00ba3ed0)
- 新版 `00ba3fa8`（命令位置の公開資料なし） · `00ba3f70`（命令位置の公開資料なし） · `00ba3f98`（命令位置の公開資料なし）

~~~diff
- 00ba3ee0 ["INT_ADD", "register:40f0:8", ["const:ba3ee0:8", "const:4:8"]]
- 00ba3ee0 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba3fa8 ["INT_ADD", "register:40f0:8", ["const:ba3fa8:8", "const:4:8"]]
+ 00ba3fa8 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba3ee0 bytes c0f30094
+ 00ba3fa8 bytes baf30094
- 00ba3ea8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc0:8"]]
- 00ba3ea8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3f70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d70:8"]]
+ 00ba3f70 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3ea8 bytes 946246f9
+ 00ba3f70 bytes 94ba46f9
- 00ba3ed0 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba3f98 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba3ed0 bytes 628b0a10
+ 00ba3f98 bytes 628b0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7c074a7950eafa656a3969b17831838"></a>

### [`00ba3fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3fb0.md) → [`00ba4078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4078.md) FUN_00ba4078

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 1件 [`00be1800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1800.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 1件 [`00be18b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba40a8",
      "incomplete_value": true,
      "site": "00ba40a8",
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
      "definition_site": "00ba3fe0",
      "incomplete_value": true,
      "site": "00ba3fe0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ba4098",
      "READ",
      [
        "storage",
        "00c1be78",
        null,
        "pointer"
      ]
    ],
    [
      "00ba40a8",
      "DATA",
      [
        "storage",
        "00c15668",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00ba4098",
      "READ",
      [
        "storage",
        "00c1bf28",
        null,
        "pointer"
      ]
    ],
    [
      "00ba40a8",
      "DATA",
      [
        "storage",
        "00c15718",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3fb0.md#insn-00ba3fd0) · [`00ba3fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3fb0.md#insn-00ba3fd4) · [`00ba3fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3fb0.md#insn-00ba3fd8)
- 新版 `00ba4098`（命令位置の公開資料なし）

~~~diff
- 00ba3fd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e78:8"]]
- 00ba3fd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba4098 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f28:8"]]
+ 00ba4098 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3fd0 bytes 083d47f9
+ 00ba4098 bytes 089547f9
- 00ba3fd4 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00ba3fd4 bytes f50300aa
- 00ba3fd8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00ba3fd8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26ae85e91c1b1e742a183536bb0eb53b"></a>

### [`00ba4094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4094.md) → [`00ba415c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba415c.md) FUN_00ba415c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba4180",
      "incomplete_value": true,
      "site": "00ba4184",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba40b8",
      "incomplete_value": true,
      "site": "00ba40bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb8:8"
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
      "definition_site": "00ba418c",
      "incomplete_value": true,
      "site": "00ba4190",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba40c4",
      "incomplete_value": true,
      "site": "00ba40c8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba41b4",
      "incomplete_value": true,
      "site": "00ba41b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba40ec",
      "incomplete_value": true,
      "site": "00ba40f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb8:8"
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
      "00ba4180",
      "READ",
      [
        "storage",
        "00c1bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4184",
      "DATA",
      [
        "storage",
        "010a2820",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4188",
      "READ",
      [
        "storage",
        "010a2820",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba4180",
      "READ",
      [
        "storage",
        "00c1bd68",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4184",
      "DATA",
      [
        "storage",
        "010a28e0",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4188",
      "READ",
      [
        "storage",
        "010a28e0",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba40f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4094.md#insn-00ba40f0) · [`00ba40b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4094.md#insn-00ba40b8) · [`00ba40e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4094.md#insn-00ba40e0)
- 新版 `00ba41b8`（命令位置の公開資料なし） · `00ba4180`（命令位置の公開資料なし） · `00ba41a8`（命令位置の公開資料なし）

~~~diff
- 00ba40f0 ["INT_ADD", "register:40f0:8", ["const:ba40f0:8", "const:4:8"]]
- 00ba40f0 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba41b8 ["INT_ADD", "register:40f0:8", ["const:ba41b8:8", "const:4:8"]]
+ 00ba41b8 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba40f0 bytes 3cf30094
+ 00ba41b8 bytes 36f30094
- 00ba40b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb8:8"]]
- 00ba40b8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba4180 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
+ 00ba4180 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba40b8 bytes 945e46f9
+ 00ba4180 bytes 94b646f9
- 00ba40e0 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba41a8 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba40e0 bytes e27a0a10
+ 00ba41a8 bytes e27a0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43d481ab2ae7c79d3b57b6c7a840acd2"></a>

### [`00ba41c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba41c0.md) → [`00ba4288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4288.md) FUN_00ba4288

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 1件 [`00be1810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1810.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 1件 [`00be18c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18c0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba42b8",
      "incomplete_value": true,
      "site": "00ba42b8",
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
      "definition_site": "00ba41f0",
      "incomplete_value": true,
      "site": "00ba41f0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ba42a8",
      "READ",
      [
        "storage",
        "00c1be80",
        null,
        "pointer"
      ]
    ],
    [
      "00ba42b8",
      "DATA",
      [
        "storage",
        "00c156f0",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00ba42a8",
      "READ",
      [
        "storage",
        "00c1bf30",
        null,
        "pointer"
      ]
    ],
    [
      "00ba42b8",
      "DATA",
      [
        "storage",
        "00c157a0",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba41e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba41c0.md#insn-00ba41e0) · [`00ba41e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba41c0.md#insn-00ba41e4) · [`00ba41e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba41c0.md#insn-00ba41e8)
- 新版 `00ba42a8`（命令位置の公開資料なし）

~~~diff
- 00ba41e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e80:8"]]
- 00ba41e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba42a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f30:8"]]
+ 00ba42a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba41e0 bytes 084147f9
+ 00ba42a8 bytes 089947f9
- 00ba41e4 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00ba41e4 bytes f50300aa
- 00ba41e8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00ba41e8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3aaa9d782718f02d8228b3264ed78a77"></a>

### [`00ba42a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba42a4.md) → [`00ba436c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba436c.md) FUN_00ba436c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba4390",
      "incomplete_value": true,
      "site": "00ba4394",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba42c8",
      "incomplete_value": true,
      "site": "00ba42cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:400:8"
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
      "definition_site": "00ba439c",
      "incomplete_value": true,
      "site": "00ba43a0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba42d4",
      "incomplete_value": true,
      "site": "00ba42d8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba43c4",
      "incomplete_value": true,
      "site": "00ba43c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba42fc",
      "incomplete_value": true,
      "site": "00ba4300",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:400:8"
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
      "00ba4390",
      "READ",
      [
        "storage",
        "00c1b400",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4394",
      "DATA",
      [
        "storage",
        "010a27b0",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4398",
      "READ",
      [
        "storage",
        "010a27b0",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba4390",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4394",
      "DATA",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4398",
      "READ",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba4300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba42a4.md#insn-00ba4300) · [`00ba42c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba42a4.md#insn-00ba42c8) · [`00ba42f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba42a4.md#insn-00ba42f0)
- 新版 `00ba43c8`（命令位置の公開資料なし） · `00ba4390`（命令位置の公開資料なし） · `00ba43b8`（命令位置の公開資料なし）

~~~diff
- 00ba4300 ["INT_ADD", "register:40f0:8", ["const:ba4300:8", "const:4:8"]]
- 00ba4300 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba43c8 ["INT_ADD", "register:40f0:8", ["const:ba43c8:8", "const:4:8"]]
+ 00ba43c8 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba4300 bytes b8f20094
+ 00ba43c8 bytes b2f20094
- 00ba42c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:400:8"]]
- 00ba42c8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba4390 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4b0:8"]]
+ 00ba4390 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba42c8 bytes 940242f9
+ 00ba4390 bytes 945a42f9
- 00ba42f0 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba43b8 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba42f0 bytes 626a0a10
+ 00ba43b8 bytes 626a0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f03bc7cbeb3f74320ba4cb383b555720"></a>

### [`00ba43d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba43d0.md) → [`00ba4498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4498.md) FUN_00ba4498

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba44bc",
      "incomplete_value": true,
      "site": "00ba44c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba43f4",
      "incomplete_value": true,
      "site": "00ba43f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc0:8"
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
      "definition_site": "00ba44c8",
      "incomplete_value": true,
      "site": "00ba44cc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba4400",
      "incomplete_value": true,
      "site": "00ba4404",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba44f0",
      "incomplete_value": true,
      "site": "00ba44f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba4428",
      "incomplete_value": true,
      "site": "00ba442c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc0:8"
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
      "00ba44bc",
      "READ",
      [
        "storage",
        "00c1bdc0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba44c0",
      "DATA",
      [
        "storage",
        "010a27c0",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba44c4",
      "READ",
      [
        "storage",
        "010a27c0",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba44bc",
      "READ",
      [
        "storage",
        "00c1be70",
        null,
        "pointer"
      ]
    ],
    [
      "00ba44c0",
      "DATA",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba44c4",
      "READ",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba442c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba43d0.md#insn-00ba442c) · [`00ba43f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba43d0.md#insn-00ba43f4) · [`00ba441c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba43d0.md#insn-00ba441c)
- 新版 `00ba44f4`（命令位置の公開資料なし） · `00ba44bc`（命令位置の公開資料なし） · `00ba44e4`（命令位置の公開資料なし）

~~~diff
- 00ba442c ["INT_ADD", "register:40f0:8", ["const:ba442c:8", "const:4:8"]]
- 00ba442c ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba44f4 ["INT_ADD", "register:40f0:8", ["const:ba44f4:8", "const:4:8"]]
+ 00ba44f4 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba442c bytes 6df20094
+ 00ba44f4 bytes 67f20094
- 00ba43f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc0:8"]]
- 00ba43f4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba44bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e70:8"]]
+ 00ba44bc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba43f4 bytes 94e246f9
+ 00ba44bc bytes 943a47f9
- 00ba441c ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba44e4 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba441c bytes 02610a10
+ 00ba44e4 bytes 02610a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b457cddc476eea9e9681454fd38139ec"></a>

### [`00ba44fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba44fc.md) → [`00ba45c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba45c4.md) FUN_00ba45c4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba45e8",
      "incomplete_value": true,
      "site": "00ba45ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba4520",
      "incomplete_value": true,
      "site": "00ba4524",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:408:8"
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
      "definition_site": "00ba45f4",
      "incomplete_value": true,
      "site": "00ba45f8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba452c",
      "incomplete_value": true,
      "site": "00ba4530",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba461c",
      "incomplete_value": true,
      "site": "00ba4620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba4554",
      "incomplete_value": true,
      "site": "00ba4558",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:408:8"
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
      "00ba45e8",
      "READ",
      [
        "storage",
        "00c1b408",
        null,
        "pointer"
      ]
    ],
    [
      "00ba45ec",
      "DATA",
      [
        "storage",
        "010a27d0",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba45f0",
      "READ",
      [
        "storage",
        "010a27d0",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba45e8",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba45ec",
      "DATA",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba45f0",
      "READ",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba4558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba44fc.md#insn-00ba4558) · [`00ba4520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba44fc.md#insn-00ba4520) · [`00ba4548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba44fc.md#insn-00ba4548)
- 新版 `00ba4620`（命令位置の公開資料なし） · `00ba45e8`（命令位置の公開資料なし） · `00ba4610`（命令位置の公開資料なし）

~~~diff
- 00ba4558 ["INT_ADD", "register:40f0:8", ["const:ba4558:8", "const:4:8"]]
- 00ba4558 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba4620 ["INT_ADD", "register:40f0:8", ["const:ba4620:8", "const:4:8"]]
+ 00ba4620 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba4558 bytes 22f20094
+ 00ba4620 bytes 1cf20094
- 00ba4520 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:408:8"]]
- 00ba4520 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba45e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4b8:8"]]
+ 00ba45e8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba4520 bytes 940642f9
+ 00ba45e8 bytes 945e42f9
- 00ba4548 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba4610 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba4548 bytes a2570a10
+ 00ba4610 bytes a2570a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71b103ff4f56b5d3b05b1426b84b9c11"></a>

### [`00ba4628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4628.md) → [`00ba46f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba46f0.md) FUN_00ba46f0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba4714",
      "incomplete_value": true,
      "site": "00ba4718",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba464c",
      "incomplete_value": true,
      "site": "00ba4650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
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
      "definition_site": "00ba4720",
      "incomplete_value": true,
      "site": "00ba4724",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba4658",
      "incomplete_value": true,
      "site": "00ba465c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba4748",
      "incomplete_value": true,
      "site": "00ba474c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba4680",
      "incomplete_value": true,
      "site": "00ba4684",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
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
      "00ba4714",
      "READ",
      [
        "storage",
        "00c1bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4718",
      "DATA",
      [
        "storage",
        "010a27e0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba471c",
      "READ",
      [
        "storage",
        "010a27e0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba4714",
      "READ",
      [
        "storage",
        "00c1be90",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4718",
      "DATA",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba471c",
      "READ",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba4684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4628.md#insn-00ba4684) · [`00ba464c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4628.md#insn-00ba464c) · [`00ba4674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4628.md#insn-00ba4674)
- 新版 `00ba474c`（命令位置の公開資料なし） · `00ba4714`（命令位置の公開資料なし） · `00ba473c`（命令位置の公開資料なし）

~~~diff
- 00ba4684 ["INT_ADD", "register:40f0:8", ["const:ba4684:8", "const:4:8"]]
- 00ba4684 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba474c ["INT_ADD", "register:40f0:8", ["const:ba474c:8", "const:4:8"]]
+ 00ba474c ["CALL", null, ["callee:00be0e90:8"]]
- 00ba4684 bytes d7f10094
+ 00ba474c bytes d1f10094
- 00ba464c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:de0:8"]]
- 00ba464c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba4714 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e90:8"]]
+ 00ba4714 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba464c bytes 94f246f9
+ 00ba4714 bytes 944a47f9
- 00ba4674 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba473c ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba4674 bytes 424e0a10
+ 00ba473c bytes 424e0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b3fa48585f862e0cc4f6da3111ae62d"></a>

### [`00ba4754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4754.md) → [`00ba481c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba481c.md) FUN_00ba481c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba4840",
      "incomplete_value": true,
      "site": "00ba4844",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba4778",
      "incomplete_value": true,
      "site": "00ba477c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
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
      "definition_site": "00ba484c",
      "incomplete_value": true,
      "site": "00ba4850",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba4784",
      "incomplete_value": true,
      "site": "00ba4788",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba4874",
      "incomplete_value": true,
      "site": "00ba4878",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba47ac",
      "incomplete_value": true,
      "site": "00ba47b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
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
      "00ba4840",
      "READ",
      [
        "storage",
        "00c1bdf0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4844",
      "DATA",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4848",
      "READ",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba4840",
      "READ",
      [
        "storage",
        "00c1bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4844",
      "DATA",
      [
        "storage",
        "010a2930",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4848",
      "READ",
      [
        "storage",
        "010a2930",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba47b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4754.md#insn-00ba47b0) · [`00ba4778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4754.md#insn-00ba4778) · [`00ba47a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4754.md#insn-00ba47a0)
- 新版 `00ba4878`（命令位置の公開資料なし） · `00ba4840`（命令位置の公開資料なし） · `00ba4868`（命令位置の公開資料なし）

~~~diff
- 00ba47b0 ["INT_ADD", "register:40f0:8", ["const:ba47b0:8", "const:4:8"]]
- 00ba47b0 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba4878 ["INT_ADD", "register:40f0:8", ["const:ba4878:8", "const:4:8"]]
+ 00ba4878 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba47b0 bytes 8cf10094
+ 00ba4878 bytes 86f10094
- 00ba4778 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
- 00ba4778 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba4840 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ea0:8"]]
+ 00ba4840 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba4778 bytes 94fa46f9
+ 00ba4840 bytes 945247f9
- 00ba47a0 ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba4868 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba47a0 bytes e2440a10
+ 00ba4868 bytes e2440a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a70052888871371ed68e382404c2399"></a>

### [`00ba4880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4880.md) → [`00ba4948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4948.md) FUN_00ba4948

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) · 呼出先 5件 [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba496c",
      "incomplete_value": true,
      "site": "00ba4970",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba48a4",
      "incomplete_value": true,
      "site": "00ba48a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
      "definition_site": "00ba4978",
      "incomplete_value": true,
      "site": "00ba497c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba48b0",
      "incomplete_value": true,
      "site": "00ba48b4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba49a0",
      "incomplete_value": true,
      "site": "00ba49a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba48d8",
      "incomplete_value": true,
      "site": "00ba48dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
      "00ba496c",
      "READ",
      [
        "storage",
        "00c1be00",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4970",
      "DATA",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4974",
      "READ",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba496c",
      "READ",
      [
        "storage",
        "00c1beb0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4970",
      "DATA",
      [
        "storage",
        "010a2940",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4974",
      "READ",
      [
        "storage",
        "010a2940",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba48dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4880.md#insn-00ba48dc) · [`00ba48a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4880.md#insn-00ba48a4) · [`00ba48cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4880.md#insn-00ba48cc)
- 新版 `00ba49a4`（命令位置の公開資料なし） · `00ba496c`（命令位置の公開資料なし） · `00ba4994`（命令位置の公開資料なし）

~~~diff
- 00ba48dc ["INT_ADD", "register:40f0:8", ["const:ba48dc:8", "const:4:8"]]
- 00ba48dc ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba49a4 ["INT_ADD", "register:40f0:8", ["const:ba49a4:8", "const:4:8"]]
+ 00ba49a4 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba48dc bytes 41f10094
+ 00ba49a4 bytes 3bf10094
- 00ba48a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
- 00ba48a4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba496c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:eb0:8"]]
+ 00ba496c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba48a4 bytes 940247f9
+ 00ba496c bytes 945a47f9
- 00ba48cc ["COPY", "register:4010:8", ["const:bb903c:8"]]
+ 00ba4994 ["COPY", "register:4010:8", ["const:bb9104:8"]]
- 00ba48cc bytes 823b0a10
+ 00ba4994 bytes 823b0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-424545546bf4746544b17bcebaf055f3"></a>

### [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) → [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) FUN_00ba4a74

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00ba8124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8124.md) [`00ba8274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8274.md) · 呼出先 40件 [`00ba05e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba05e4.md) [`00ba2c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2c54.md) [`00ba2d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2d80.md) [`00ba2eac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2eac.md) [`00ba2fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2fd8.md)
- 新版 呼出元 2件 [`00ba81ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba81ec.md) [`00ba833c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba833c.md) · 呼出先 40件 [`00ba06ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba06ac.md) [`00ba2d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2d1c.md) [`00ba2e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2e48.md) [`00ba2f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2f74.md) [`00ba30a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba30a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 13件

アドレスに依存する影響 `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba4aa8",
      "incomplete_value": false,
      "site": "00ba4aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba49e0",
      "incomplete_value": false,
      "site": "00ba49e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:818:8"
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
      "definition_site": "00ba4c38",
      "incomplete_value": true,
      "site": "00ba4c38",
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
      "definition_site": "00ba4b70",
      "incomplete_value": true,
      "site": "00ba4b70",
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
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba4c70",
      "incomplete_value": true,
      "site": "00ba4c74",
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
      "definition_site": "00ba4ba8",
      "incomplete_value": true,
      "site": "00ba4bac",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ba4aa8",
      "DATA",
      [
        "storage",
        "00c13818",
        null,
        "undefined *"
      ]
    ],
    [
      "00ba4c30",
      "READ",
      [
        "storage",
        "00c1be08",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4c38",
      "DATA",
      [
        "storage",
        "00c15b28",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00ba4aa8",
      "DATA",
      [
        "storage",
        "00c138c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00ba4c30",
      "READ",
      [
        "storage",
        "00c1beb8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4c38",
      "DATA",
      [
        "storage",
        "00c15bd8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba4b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md#insn-00ba4b10) · [`00ba4c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md#insn-00ba4c38) · [`00ba4c74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md#insn-00ba4c74)
- 新版 `00ba4bd8`（命令位置の公開資料なし） · `00ba4d00`（命令位置の公開資料なし） · `00ba4d3c`（命令位置の公開資料なし）

~~~diff
- 00ba4b10 ["INT_ADD", "register:40f0:8", ["const:ba4b10:8", "const:4:8"]]
- 00ba4b10 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ba4bd8 ["INT_ADD", "register:40f0:8", ["const:ba4bd8:8", "const:4:8"]]
+ 00ba4bd8 ["CALL", null, ["callee:00bdaff0:8"]]
- 00ba4b10 bytes 0cd90094
+ 00ba4bd8 bytes 06d90094
- 00ba4c38 ["INT_ADD", "register:40f0:8", ["const:ba4c38:8", "const:4:8"]]
- 00ba4c38 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ba4d00 ["INT_ADD", "register:40f0:8", ["const:ba4d00:8", "const:4:8"]]
+ 00ba4d00 ["CALL", null, ["callee:00bdaff0:8"]]
- 00ba4c38 bytes c2d80094
+ 00ba4d00 bytes bcd80094
- 00ba4c74 ["INT_ADD", "register:40f0:8", ["const:ba4c74:8", "const:4:8"]]
- 00ba4c74 ["CALL", null, ["callee:00ba3c58:8"]]
+ 00ba4d3c ["INT_ADD", "register:40f0:8", ["const:ba4d3c:8", "const:4:8"]]
+ 00ba4d3c ["CALL", null, ["callee:00ba3c58:8"]]
- 00ba4c74 bytes c7fbff97
+ 00ba4d3c bytes c7fbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6af0ecd780bc0cd973fac14c68cb385"></a>

### [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) → [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) FUN_00ba50c4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba82ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba82ec.md) · 呼出先 33件 [`00ba05e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba0/00ba05e4.md) [`00ba5360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5360.md) [`00ba54a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba54a4.md) [`00ba55e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba55e8.md) [`00ba572c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba572c.md)
- 新版 呼出元 1件 [`00ba83b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba83b4.md) · 呼出先 33件 [`00ba06ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba06ac.md) [`00ba5428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5428.md) [`00ba556c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba556c.md) [`00ba56b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba56b0.md) [`00ba57f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba57f4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.27% / 新版 95.27%

CFGの説明率　旧版 42.42% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba502c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba502c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba5088"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba502c",
      "DATA",
      [
        "storage",
        "00c13818",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00ba50c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba51d0"
      ]
    ]
  ],
  "added": [
    [
      "00ba50f4",
      "DATA",
      [
        "storage",
        "00c138c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00ba5190",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba51d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba502c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md#insn-00ba502c) · [`00ba5088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md#insn-00ba5088) · [`00ba508c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md#insn-00ba508c)

~~~diff
- 00ba502c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ba502c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ba502c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00ba502c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba502c bytes 092000a9
- 00ba5088 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:e0:8"]]
- 00ba5088 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00ba5088 bytes 003b803d
- 00ba508c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba508c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ba508c ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:18:8"]]
- 00ba508c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba508c bytes 08a001a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07482f90e667a5810572c2440ddc3a7c"></a>

### [`00ba5360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5360.md) → [`00ba5428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5428.md) FUN_00ba5428

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 74.29% / 新版 74.29%

CFGの説明率　旧版 63.64% / 新版 58.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba5388"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba53a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba53b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba5384",
      "READ",
      [
        "storage",
        "00c1b480",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba5388",
      "DATA",
      [
        "storage",
        "010a2750",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba5388",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba544c",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5450",
      "DATA",
      [
        "storage",
        "010a2810",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5450",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5360.md#insn-00ba5388) · [`00ba5394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5360.md#insn-00ba5394) · [`00ba53a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5360.md#insn-00ba53a4)

~~~diff
- 00ba5388 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba5388 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba5388 bytes f40700f9
- 00ba5394 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba5394 bytes 60010054
- 00ba53a4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba53a4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00ba53a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ba53a4 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91a64e33519670cb8968b1f63f593696"></a>

### [`00ba54a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba54a4.md) → [`00ba556c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba556c.md) FUN_00ba556c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.29% / 新版 84.29%

CFGの説明率　旧版 56.00% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba54cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba5594"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba54d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba54c8",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba54cc",
      "DATA",
      [
        "storage",
        "010a2760",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba54cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba5590",
      "READ",
      [
        "storage",
        "00c1bd88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5594",
      "DATA",
      [
        "storage",
        "010a2820",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5594",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba54cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba54a4.md#insn-00ba54cc) · [`00ba54d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba54a4.md#insn-00ba54d8) · [`00ba5500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba54a4.md#insn-00ba5500)
- 新版 `00ba55c8`（命令位置の公開資料なし）

~~~diff
- 00ba54cc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba54cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba54cc bytes f40700f9
- 00ba54d8 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00ba54d8 bytes 60010054
- 00ba5500 ["INT_ADD", "register:40f0:8", ["const:ba5500:8", "const:4:8"]]
- 00ba5500 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba55c8 ["INT_ADD", "register:40f0:8", ["const:ba55c8:8", "const:4:8"]]
+ 00ba55c8 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba5500 bytes 38ee0094
+ 00ba55c8 bytes 32ee0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a985c9cedf52f33b821706248d73d2e"></a>

### [`00ba55e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba55e8.md) → [`00ba56b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba56b0.md) FUN_00ba56b0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba56d4",
      "incomplete_value": true,
      "site": "00ba56d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba560c",
      "incomplete_value": true,
      "site": "00ba5610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "definition_site": "00ba56e0",
      "incomplete_value": true,
      "site": "00ba56e4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5618",
      "incomplete_value": true,
      "site": "00ba561c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5708",
      "incomplete_value": true,
      "site": "00ba570c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5640",
      "incomplete_value": true,
      "site": "00ba5644",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "00ba56d4",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00ba56d8",
      "DATA",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba56dc",
      "READ",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba56d4",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba56d8",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba56dc",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba55e8.md#insn-00ba5644) · [`00ba56d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba55e8.md#insn-00ba56d8) · [`00ba560c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba55e8.md#insn-00ba560c)
- 新版 `00ba570c`（命令位置の公開資料なし） · `00ba57a0`（命令位置の公開資料なし） · `00ba56d4`（命令位置の公開資料なし）

~~~diff
- 00ba5644 ["INT_ADD", "register:40f0:8", ["const:ba5644:8", "const:4:8"]]
- 00ba5644 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba570c ["INT_ADD", "register:40f0:8", ["const:ba570c:8", "const:4:8"]]
+ 00ba570c ["CALL", null, ["callee:00be0e90:8"]]
- 00ba5644 bytes e7ed0094
+ 00ba570c bytes e1ed0094
- 00ba56d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba56d8 ["INT_ADD", "register:40f0:8", ["const:ba56d8:8", "const:4:8"]]
- 00ba56d8 ["CALLIND", null, ["register:0:8"]]
+ 00ba57a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba57a0 ["INT_ADD", "register:40f0:8", ["const:ba57a0:8", "const:4:8"]]
+ 00ba57a0 ["CALLIND", null, ["register:0:8"]]
- 00ba56d8 bytes 00013fd6
+ 00ba57a0 bytes 00013fd6
- 00ba560c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d40:8"]]
- 00ba560c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba56d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
+ 00ba56d4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba560c bytes 94a246f9
+ 00ba56d4 bytes 94fa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c7c4fd40059dd350025014349e16b76"></a>

### [`00ba572c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba572c.md) → [`00ba57f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba57f4.md) FUN_00ba57f4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5818",
      "incomplete_value": true,
      "site": "00ba581c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5750",
      "incomplete_value": true,
      "site": "00ba5754",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00ba5824",
      "incomplete_value": true,
      "site": "00ba5828",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba575c",
      "incomplete_value": true,
      "site": "00ba5760",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba584c",
      "incomplete_value": true,
      "site": "00ba5850",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5784",
      "incomplete_value": true,
      "site": "00ba5788",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00ba5818",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00ba581c",
      "DATA",
      [
        "storage",
        "010a2a00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5820",
      "READ",
      [
        "storage",
        "010a2a00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba5818",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba581c",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5820",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba572c.md#insn-00ba5788) · [`00ba581c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba572c.md#insn-00ba581c) · [`00ba5750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba572c.md#insn-00ba5750)
- 新版 `00ba5850`（命令位置の公開資料なし） · `00ba58e4`（命令位置の公開資料なし） · `00ba5818`（命令位置の公開資料なし）

~~~diff
- 00ba5788 ["INT_ADD", "register:40f0:8", ["const:ba5788:8", "const:4:8"]]
- 00ba5788 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba5850 ["INT_ADD", "register:40f0:8", ["const:ba5850:8", "const:4:8"]]
+ 00ba5850 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba5788 bytes 96ed0094
+ 00ba5850 bytes 90ed0094
- 00ba581c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba581c ["INT_ADD", "register:40f0:8", ["const:ba581c:8", "const:4:8"]]
- 00ba581c ["CALLIND", null, ["register:0:8"]]
+ 00ba58e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba58e4 ["INT_ADD", "register:40f0:8", ["const:ba58e4:8", "const:4:8"]]
+ 00ba58e4 ["CALLIND", null, ["register:0:8"]]
- 00ba581c bytes 00013fd6
+ 00ba58e4 bytes 00013fd6
- 00ba5750 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
- 00ba5750 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba5818 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc0:8"]]
+ 00ba5818 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba5750 bytes 940a46f9
+ 00ba5818 bytes 946246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8096b99fc479d4d3f5c7acd75d5c65b2"></a>

### [`00ba5870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5870.md) → [`00ba5938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5938.md) FUN_00ba5938

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba595c",
      "incomplete_value": true,
      "site": "00ba5960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5894",
      "incomplete_value": true,
      "site": "00ba5898",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9b0:8"
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
      "definition_site": "00ba5968",
      "incomplete_value": true,
      "site": "00ba596c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba58a0",
      "incomplete_value": true,
      "site": "00ba58a4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5990",
      "incomplete_value": true,
      "site": "00ba5994",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba58c8",
      "incomplete_value": true,
      "site": "00ba58cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9b0:8"
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
      "00ba595c",
      "READ",
      [
        "storage",
        "00c1b9b0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5960",
      "DATA",
      [
        "storage",
        "010a2a20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5964",
      "READ",
      [
        "storage",
        "010a2a20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba595c",
      "READ",
      [
        "storage",
        "00c1ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5960",
      "DATA",
      [
        "storage",
        "010a2ae0",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5964",
      "READ",
      [
        "storage",
        "010a2ae0",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba58cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5870.md#insn-00ba58cc) · [`00ba5960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5870.md#insn-00ba5960) · [`00ba5894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5870.md#insn-00ba5894)
- 新版 `00ba5994`（命令位置の公開資料なし） · `00ba5a28`（命令位置の公開資料なし） · `00ba595c`（命令位置の公開資料なし）

~~~diff
- 00ba58cc ["INT_ADD", "register:40f0:8", ["const:ba58cc:8", "const:4:8"]]
- 00ba58cc ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba5994 ["INT_ADD", "register:40f0:8", ["const:ba5994:8", "const:4:8"]]
+ 00ba5994 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba58cc bytes 45ed0094
+ 00ba5994 bytes 3fed0094
- 00ba5960 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba5960 ["INT_ADD", "register:40f0:8", ["const:ba5960:8", "const:4:8"]]
- 00ba5960 ["CALLIND", null, ["register:0:8"]]
+ 00ba5a28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba5a28 ["INT_ADD", "register:40f0:8", ["const:ba5a28:8", "const:4:8"]]
+ 00ba5a28 ["CALLIND", null, ["register:0:8"]]
- 00ba5960 bytes 00013fd6
+ 00ba5a28 bytes 00013fd6
- 00ba5894 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b0:8"]]
- 00ba5894 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba595c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a60:8"]]
+ 00ba595c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba5894 bytes 94da44f9
+ 00ba595c bytes 943245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30124ccbb5764542ccd578de80e7fa48"></a>

### [`00ba59b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba59b4.md) → [`00ba5a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5a7c.md) FUN_00ba5a7c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5aa0",
      "incomplete_value": true,
      "site": "00ba5aa4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba59d8",
      "incomplete_value": true,
      "site": "00ba59dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf8:8"
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
      "definition_site": "00ba5aac",
      "incomplete_value": true,
      "site": "00ba5ab0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba59e4",
      "incomplete_value": true,
      "site": "00ba59e8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5ad4",
      "incomplete_value": true,
      "site": "00ba5ad8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5a0c",
      "incomplete_value": true,
      "site": "00ba5a10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf8:8"
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
      "00ba5aa0",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5aa4",
      "DATA",
      [
        "storage",
        "010a2a40",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5aa8",
      "READ",
      [
        "storage",
        "010a2a40",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba5aa0",
      "READ",
      [
        "storage",
        "00c1bda8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5aa4",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5aa8",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba59b4.md#insn-00ba5a10) · [`00ba5aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba59b4.md#insn-00ba5aa4) · [`00ba59d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba59b4.md#insn-00ba59d8)
- 新版 `00ba5ad8`（命令位置の公開資料なし） · `00ba5b6c`（命令位置の公開資料なし） · `00ba5aa0`（命令位置の公開資料なし）

~~~diff
- 00ba5a10 ["INT_ADD", "register:40f0:8", ["const:ba5a10:8", "const:4:8"]]
- 00ba5a10 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba5ad8 ["INT_ADD", "register:40f0:8", ["const:ba5ad8:8", "const:4:8"]]
+ 00ba5ad8 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba5a10 bytes f4ec0094
+ 00ba5ad8 bytes eeec0094
- 00ba5aa4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba5aa4 ["INT_ADD", "register:40f0:8", ["const:ba5aa4:8", "const:4:8"]]
- 00ba5aa4 ["CALLIND", null, ["register:0:8"]]
+ 00ba5b6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba5b6c ["INT_ADD", "register:40f0:8", ["const:ba5b6c:8", "const:4:8"]]
+ 00ba5b6c ["CALLIND", null, ["register:0:8"]]
- 00ba5aa4 bytes 00013fd6
+ 00ba5b6c bytes 00013fd6
- 00ba59d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf8:8"]]
- 00ba59d8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba5aa0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:da8:8"]]
+ 00ba5aa0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba59d8 bytes 947e46f9
+ 00ba5aa0 bytes 94d646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9186d5780dbb832f9678a44816b71f90"></a>

### [`00ba5af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5af8.md) → [`00ba5bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5bc0.md) FUN_00ba5bc0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5be4",
      "incomplete_value": true,
      "site": "00ba5be8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5b1c",
      "incomplete_value": true,
      "site": "00ba5b20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
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
      "definition_site": "00ba5bf0",
      "incomplete_value": true,
      "site": "00ba5bf4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5b28",
      "incomplete_value": true,
      "site": "00ba5b2c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5c18",
      "incomplete_value": true,
      "site": "00ba5c1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5b50",
      "incomplete_value": true,
      "site": "00ba5b54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
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
      "00ba5be4",
      "READ",
      [
        "storage",
        "00c1bd08",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5be8",
      "DATA",
      [
        "storage",
        "010a2a60",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5bec",
      "READ",
      [
        "storage",
        "010a2a60",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba5be4",
      "READ",
      [
        "storage",
        "00c1bdb8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5be8",
      "DATA",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5bec",
      "READ",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5af8.md#insn-00ba5b54) · [`00ba5be8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5af8.md#insn-00ba5be8) · [`00ba5b1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5af8.md#insn-00ba5b1c)
- 新版 `00ba5c1c`（命令位置の公開資料なし） · `00ba5cb0`（命令位置の公開資料なし） · `00ba5be4`（命令位置の公開資料なし）

~~~diff
- 00ba5b54 ["INT_ADD", "register:40f0:8", ["const:ba5b54:8", "const:4:8"]]
- 00ba5b54 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba5c1c ["INT_ADD", "register:40f0:8", ["const:ba5c1c:8", "const:4:8"]]
+ 00ba5c1c ["CALL", null, ["callee:00be0e90:8"]]
- 00ba5b54 bytes a3ec0094
+ 00ba5c1c bytes 9dec0094
- 00ba5be8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba5be8 ["INT_ADD", "register:40f0:8", ["const:ba5be8:8", "const:4:8"]]
- 00ba5be8 ["CALLIND", null, ["register:0:8"]]
+ 00ba5cb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba5cb0 ["INT_ADD", "register:40f0:8", ["const:ba5cb0:8", "const:4:8"]]
+ 00ba5cb0 ["CALLIND", null, ["register:0:8"]]
- 00ba5be8 bytes 00013fd6
+ 00ba5cb0 bytes 00013fd6
- 00ba5b1c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d08:8"]]
- 00ba5b1c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba5be4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db8:8"]]
+ 00ba5be4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba5b1c bytes 948646f9
+ 00ba5be4 bytes 94de46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bcadcd6980aa3ff2c3c496b00e8889c"></a>

### [`00ba5c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5c3c.md) → [`00ba5d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5d04.md) FUN_00ba5d04

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5d28",
      "incomplete_value": true,
      "site": "00ba5d2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5c60",
      "incomplete_value": true,
      "site": "00ba5c64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
      "definition_site": "00ba5d34",
      "incomplete_value": true,
      "site": "00ba5d38",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5c6c",
      "incomplete_value": true,
      "site": "00ba5c70",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5d5c",
      "incomplete_value": true,
      "site": "00ba5d60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5c94",
      "incomplete_value": true,
      "site": "00ba5c98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
      "00ba5d28",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5d2c",
      "DATA",
      [
        "storage",
        "010a2a50",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5d30",
      "READ",
      [
        "storage",
        "010a2a50",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba5d28",
      "READ",
      [
        "storage",
        "00c1bdc8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5d2c",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5d30",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5c3c.md#insn-00ba5c98) · [`00ba5d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5c3c.md#insn-00ba5d2c) · [`00ba5c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5c3c.md#insn-00ba5c60)
- 新版 `00ba5d60`（命令位置の公開資料なし） · `00ba5df4`（命令位置の公開資料なし） · `00ba5d28`（命令位置の公開資料なし）

~~~diff
- 00ba5c98 ["INT_ADD", "register:40f0:8", ["const:ba5c98:8", "const:4:8"]]
- 00ba5c98 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba5d60 ["INT_ADD", "register:40f0:8", ["const:ba5d60:8", "const:4:8"]]
+ 00ba5d60 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba5c98 bytes 52ec0094
+ 00ba5d60 bytes 4cec0094
- 00ba5d2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba5d2c ["INT_ADD", "register:40f0:8", ["const:ba5d2c:8", "const:4:8"]]
- 00ba5d2c ["CALLIND", null, ["register:0:8"]]
+ 00ba5df4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba5df4 ["INT_ADD", "register:40f0:8", ["const:ba5df4:8", "const:4:8"]]
+ 00ba5df4 ["CALLIND", null, ["register:0:8"]]
- 00ba5d2c bytes 00013fd6
+ 00ba5df4 bytes 00013fd6
- 00ba5c60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d18:8"]]
- 00ba5c60 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba5d28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc8:8"]]
+ 00ba5d28 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba5c60 bytes 948e46f9
+ 00ba5d28 bytes 94e646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-962ba8a286d87ad12301739e99c05c2f"></a>

### [`00ba5d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5d80.md) → [`00ba5e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5e48.md) FUN_00ba5e48

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5e6c",
      "incomplete_value": true,
      "site": "00ba5e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5da4",
      "incomplete_value": true,
      "site": "00ba5da8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
      "definition_site": "00ba5e78",
      "incomplete_value": true,
      "site": "00ba5e7c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5db0",
      "incomplete_value": true,
      "site": "00ba5db4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5ea0",
      "incomplete_value": true,
      "site": "00ba5ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5dd8",
      "incomplete_value": true,
      "site": "00ba5ddc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
      "00ba5e6c",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5e70",
      "DATA",
      [
        "storage",
        "010a2a70",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5e74",
      "READ",
      [
        "storage",
        "010a2a70",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba5e6c",
      "READ",
      [
        "storage",
        "00c1bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5e70",
      "DATA",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5e74",
      "READ",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5ddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5d80.md#insn-00ba5ddc) · [`00ba5e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5d80.md#insn-00ba5e70) · [`00ba5da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5d80.md#insn-00ba5da4)
- 新版 `00ba5ea4`（命令位置の公開資料なし） · `00ba5f38`（命令位置の公開資料なし） · `00ba5e6c`（命令位置の公開資料なし）

~~~diff
- 00ba5ddc ["INT_ADD", "register:40f0:8", ["const:ba5ddc:8", "const:4:8"]]
- 00ba5ddc ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba5ea4 ["INT_ADD", "register:40f0:8", ["const:ba5ea4:8", "const:4:8"]]
+ 00ba5ea4 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba5ddc bytes 01ec0094
+ 00ba5ea4 bytes fbeb0094
- 00ba5e70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba5e70 ["INT_ADD", "register:40f0:8", ["const:ba5e70:8", "const:4:8"]]
- 00ba5e70 ["CALLIND", null, ["register:0:8"]]
+ 00ba5f38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba5f38 ["INT_ADD", "register:40f0:8", ["const:ba5f38:8", "const:4:8"]]
+ 00ba5f38 ["CALLIND", null, ["register:0:8"]]
- 00ba5e70 bytes 00013fd6
+ 00ba5f38 bytes 00013fd6
- 00ba5da4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
- 00ba5da4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba5e6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd8:8"]]
+ 00ba5e6c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba5da4 bytes 949646f9
+ 00ba5e6c bytes 94ee46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f6c2847258efa85a911b3ad5357de4c"></a>

### [`00ba5ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5ec4.md) → [`00ba5f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5f8c.md) FUN_00ba5f8c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5fb0",
      "incomplete_value": true,
      "site": "00ba5fb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5ee8",
      "incomplete_value": true,
      "site": "00ba5eec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
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
      "definition_site": "00ba5fbc",
      "incomplete_value": true,
      "site": "00ba5fc0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5ef4",
      "incomplete_value": true,
      "site": "00ba5ef8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5fe4",
      "incomplete_value": true,
      "site": "00ba5fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5f1c",
      "incomplete_value": true,
      "site": "00ba5f20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
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
      "00ba5fb0",
      "READ",
      [
        "storage",
        "00c1bc78",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5fb4",
      "DATA",
      [
        "storage",
        "010a2a30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5fb8",
      "READ",
      [
        "storage",
        "010a2a30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba5fb0",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5fb4",
      "DATA",
      [
        "storage",
        "010a2af0",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5fb8",
      "READ",
      [
        "storage",
        "010a2af0",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5ec4.md#insn-00ba5f20) · [`00ba5fb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5ec4.md#insn-00ba5fb4) · [`00ba5ee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba5/00ba5ec4.md#insn-00ba5ee8)
- 新版 `00ba5fe8`（命令位置の公開資料なし） · `00ba607c`（命令位置の公開資料なし） · `00ba5fb0`（命令位置の公開資料なし）

~~~diff
- 00ba5f20 ["INT_ADD", "register:40f0:8", ["const:ba5f20:8", "const:4:8"]]
- 00ba5f20 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba5fe8 ["INT_ADD", "register:40f0:8", ["const:ba5fe8:8", "const:4:8"]]
+ 00ba5fe8 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba5f20 bytes b0eb0094
+ 00ba5fe8 bytes aaeb0094
- 00ba5fb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba5fb4 ["INT_ADD", "register:40f0:8", ["const:ba5fb4:8", "const:4:8"]]
- 00ba5fb4 ["CALLIND", null, ["register:0:8"]]
+ 00ba607c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba607c ["INT_ADD", "register:40f0:8", ["const:ba607c:8", "const:4:8"]]
+ 00ba607c ["CALLIND", null, ["register:0:8"]]
- 00ba5fb4 bytes 00013fd6
+ 00ba607c bytes 00013fd6
- 00ba5ee8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c78:8"]]
- 00ba5ee8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba5fb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
+ 00ba5fb0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba5ee8 bytes 943e46f9
+ 00ba5fb0 bytes 949646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7b2c4f7dc490263fb796fb3f5e97057"></a>

### [`00ba6008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6008.md) → [`00ba60d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba60d0.md) FUN_00ba60d0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba60f4",
      "incomplete_value": true,
      "site": "00ba60f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba602c",
      "incomplete_value": true,
      "site": "00ba6030",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb0:8"
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
      "definition_site": "00ba6100",
      "incomplete_value": true,
      "site": "00ba6104",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6038",
      "incomplete_value": true,
      "site": "00ba603c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6128",
      "incomplete_value": true,
      "site": "00ba612c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6060",
      "incomplete_value": true,
      "site": "00ba6064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb0:8"
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
      "00ba60f4",
      "READ",
      [
        "storage",
        "00c1bcb0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba60f8",
      "DATA",
      [
        "storage",
        "010a27f0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba60fc",
      "READ",
      [
        "storage",
        "010a27f0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba60f4",
      "READ",
      [
        "storage",
        "00c1bd60",
        null,
        "pointer"
      ]
    ],
    [
      "00ba60f8",
      "DATA",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba60fc",
      "READ",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6008.md#insn-00ba6064) · [`00ba60f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6008.md#insn-00ba60f8) · [`00ba602c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6008.md#insn-00ba602c)
- 新版 `00ba612c`（命令位置の公開資料なし） · `00ba61c0`（命令位置の公開資料なし） · `00ba60f4`（命令位置の公開資料なし）

~~~diff
- 00ba6064 ["INT_ADD", "register:40f0:8", ["const:ba6064:8", "const:4:8"]]
- 00ba6064 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba612c ["INT_ADD", "register:40f0:8", ["const:ba612c:8", "const:4:8"]]
+ 00ba612c ["CALL", null, ["callee:00be0e90:8"]]
- 00ba6064 bytes 5feb0094
+ 00ba612c bytes 59eb0094
- 00ba60f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba60f8 ["INT_ADD", "register:40f0:8", ["const:ba60f8:8", "const:4:8"]]
- 00ba60f8 ["CALLIND", null, ["register:0:8"]]
+ 00ba61c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba61c0 ["INT_ADD", "register:40f0:8", ["const:ba61c0:8", "const:4:8"]]
+ 00ba61c0 ["CALLIND", null, ["register:0:8"]]
- 00ba60f8 bytes 00013fd6
+ 00ba61c0 bytes 00013fd6
- 00ba602c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb0:8"]]
- 00ba602c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba60f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d60:8"]]
+ 00ba60f4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba602c bytes 945a46f9
+ 00ba60f4 bytes 94b246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be447fe89dff41234637e78f512a5311"></a>

### [`00ba614c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba614c.md) → [`00ba6214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6214.md) FUN_00ba6214

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6238",
      "incomplete_value": true,
      "site": "00ba623c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6170",
      "incomplete_value": true,
      "site": "00ba6174",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
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
      "definition_site": "00ba6244",
      "incomplete_value": true,
      "site": "00ba6248",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba617c",
      "incomplete_value": true,
      "site": "00ba6180",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba626c",
      "incomplete_value": true,
      "site": "00ba6270",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba61a4",
      "incomplete_value": true,
      "site": "00ba61a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
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
      "00ba6238",
      "READ",
      [
        "storage",
        "00c1bca8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba623c",
      "DATA",
      [
        "storage",
        "010a2800",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6240",
      "READ",
      [
        "storage",
        "010a2800",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6238",
      "READ",
      [
        "storage",
        "00c1bd58",
        null,
        "pointer"
      ]
    ],
    [
      "00ba623c",
      "DATA",
      [
        "storage",
        "010a28c0",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6240",
      "READ",
      [
        "storage",
        "010a28c0",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba61a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba614c.md#insn-00ba61a8) · [`00ba623c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba614c.md#insn-00ba623c) · [`00ba6170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba614c.md#insn-00ba6170)
- 新版 `00ba6270`（命令位置の公開資料なし） · `00ba6304`（命令位置の公開資料なし） · `00ba6238`（命令位置の公開資料なし）

~~~diff
- 00ba61a8 ["INT_ADD", "register:40f0:8", ["const:ba61a8:8", "const:4:8"]]
- 00ba61a8 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba6270 ["INT_ADD", "register:40f0:8", ["const:ba6270:8", "const:4:8"]]
+ 00ba6270 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba61a8 bytes 0eeb0094
+ 00ba6270 bytes 08eb0094
- 00ba623c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba623c ["INT_ADD", "register:40f0:8", ["const:ba623c:8", "const:4:8"]]
- 00ba623c ["CALLIND", null, ["register:0:8"]]
+ 00ba6304 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba6304 ["INT_ADD", "register:40f0:8", ["const:ba6304:8", "const:4:8"]]
+ 00ba6304 ["CALLIND", null, ["register:0:8"]]
- 00ba623c bytes 00013fd6
+ 00ba6304 bytes 00013fd6
- 00ba6170 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
- 00ba6170 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6238 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d58:8"]]
+ 00ba6238 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6170 bytes 945646f9
+ 00ba6238 bytes 94ae46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01ab5e0d0166a51752ec45170db8770f"></a>

### [`00ba6290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6290.md) → [`00ba6358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6358.md) FUN_00ba6358

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba637c",
      "incomplete_value": true,
      "site": "00ba6380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba62b4",
      "incomplete_value": true,
      "site": "00ba62b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "definition_site": "00ba6388",
      "incomplete_value": true,
      "site": "00ba638c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba62c0",
      "incomplete_value": true,
      "site": "00ba62c4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba63b0",
      "incomplete_value": true,
      "site": "00ba63b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba62e8",
      "incomplete_value": true,
      "site": "00ba62ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00ba637c",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6380",
      "DATA",
      [
        "storage",
        "010a2810",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6384",
      "READ",
      [
        "storage",
        "010a2810",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba637c",
      "READ",
      [
        "storage",
        "00c1bd70",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6380",
      "DATA",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6384",
      "READ",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba62ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6290.md#insn-00ba62ec) · [`00ba6380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6290.md#insn-00ba6380) · [`00ba62b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6290.md#insn-00ba62b4)
- 新版 `00ba63b4`（命令位置の公開資料なし） · `00ba6448`（命令位置の公開資料なし） · `00ba637c`（命令位置の公開資料なし）

~~~diff
- 00ba62ec ["INT_ADD", "register:40f0:8", ["const:ba62ec:8", "const:4:8"]]
- 00ba62ec ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba63b4 ["INT_ADD", "register:40f0:8", ["const:ba63b4:8", "const:4:8"]]
+ 00ba63b4 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba62ec bytes bdea0094
+ 00ba63b4 bytes b7ea0094
- 00ba6380 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba6380 ["INT_ADD", "register:40f0:8", ["const:ba6380:8", "const:4:8"]]
- 00ba6380 ["CALLIND", null, ["register:0:8"]]
+ 00ba6448 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba6448 ["INT_ADD", "register:40f0:8", ["const:ba6448:8", "const:4:8"]]
+ 00ba6448 ["CALLIND", null, ["register:0:8"]]
- 00ba6380 bytes 00013fd6
+ 00ba6448 bytes 00013fd6
- 00ba62b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc0:8"]]
- 00ba62b4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba637c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d70:8"]]
+ 00ba637c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba62b4 bytes 946246f9
+ 00ba637c bytes 94ba46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ffb923a80ec0dfc51771d2b838d5db3"></a>

### [`00ba63d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba63d4.md) → [`00ba649c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba649c.md) FUN_00ba649c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba64c0",
      "incomplete_value": true,
      "site": "00ba64c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba63f8",
      "incomplete_value": true,
      "site": "00ba63fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb8:8"
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
      "definition_site": "00ba64cc",
      "incomplete_value": true,
      "site": "00ba64d0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6404",
      "incomplete_value": true,
      "site": "00ba6408",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba64f4",
      "incomplete_value": true,
      "site": "00ba64f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba642c",
      "incomplete_value": true,
      "site": "00ba6430",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb8:8"
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
      "00ba64c0",
      "READ",
      [
        "storage",
        "00c1bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba64c4",
      "DATA",
      [
        "storage",
        "010a2820",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba64c8",
      "READ",
      [
        "storage",
        "010a2820",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba64c0",
      "READ",
      [
        "storage",
        "00c1bd68",
        null,
        "pointer"
      ]
    ],
    [
      "00ba64c4",
      "DATA",
      [
        "storage",
        "010a28e0",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba64c8",
      "READ",
      [
        "storage",
        "010a28e0",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba63d4.md#insn-00ba6430) · [`00ba64c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba63d4.md#insn-00ba64c4) · [`00ba63f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba63d4.md#insn-00ba63f8)
- 新版 `00ba64f8`（命令位置の公開資料なし） · `00ba658c`（命令位置の公開資料なし） · `00ba64c0`（命令位置の公開資料なし）

~~~diff
- 00ba6430 ["INT_ADD", "register:40f0:8", ["const:ba6430:8", "const:4:8"]]
- 00ba6430 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba64f8 ["INT_ADD", "register:40f0:8", ["const:ba64f8:8", "const:4:8"]]
+ 00ba64f8 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba6430 bytes 6cea0094
+ 00ba64f8 bytes 66ea0094
- 00ba64c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba64c4 ["INT_ADD", "register:40f0:8", ["const:ba64c4:8", "const:4:8"]]
- 00ba64c4 ["CALLIND", null, ["register:0:8"]]
+ 00ba658c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba658c ["INT_ADD", "register:40f0:8", ["const:ba658c:8", "const:4:8"]]
+ 00ba658c ["CALLIND", null, ["register:0:8"]]
- 00ba64c4 bytes 00013fd6
+ 00ba658c bytes 00013fd6
- 00ba63f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb8:8"]]
- 00ba63f8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba64c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
+ 00ba64c0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba63f8 bytes 945e46f9
+ 00ba64c0 bytes 94b646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b54485b620227b44e35bacb78803ee1"></a>

### [`00ba6518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6518.md) → [`00ba65e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba65e0.md) FUN_00ba65e0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6604",
      "incomplete_value": true,
      "site": "00ba6608",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba653c",
      "incomplete_value": true,
      "site": "00ba6540",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
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
      "definition_site": "00ba6610",
      "incomplete_value": true,
      "site": "00ba6614",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6548",
      "incomplete_value": true,
      "site": "00ba654c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6638",
      "incomplete_value": true,
      "site": "00ba663c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6570",
      "incomplete_value": true,
      "site": "00ba6574",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
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
      "00ba6604",
      "READ",
      [
        "storage",
        "00c1bd78",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6608",
      "DATA",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba660c",
      "READ",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6604",
      "READ",
      [
        "storage",
        "00c1be28",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6608",
      "DATA",
      [
        "storage",
        "010a28f0",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba660c",
      "READ",
      [
        "storage",
        "010a28f0",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6518.md#insn-00ba6574) · [`00ba6608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6518.md#insn-00ba6608) · [`00ba653c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6518.md#insn-00ba653c)
- 新版 `00ba663c`（命令位置の公開資料なし） · `00ba66d0`（命令位置の公開資料なし） · `00ba6604`（命令位置の公開資料なし）

~~~diff
- 00ba6574 ["INT_ADD", "register:40f0:8", ["const:ba6574:8", "const:4:8"]]
- 00ba6574 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba663c ["INT_ADD", "register:40f0:8", ["const:ba663c:8", "const:4:8"]]
+ 00ba663c ["CALL", null, ["callee:00be0e90:8"]]
- 00ba6574 bytes 1bea0094
+ 00ba663c bytes 15ea0094
- 00ba6608 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba6608 ["INT_ADD", "register:40f0:8", ["const:ba6608:8", "const:4:8"]]
- 00ba6608 ["CALLIND", null, ["register:0:8"]]
+ 00ba66d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba66d0 ["INT_ADD", "register:40f0:8", ["const:ba66d0:8", "const:4:8"]]
+ 00ba66d0 ["CALLIND", null, ["register:0:8"]]
- 00ba6608 bytes 00013fd6
+ 00ba66d0 bytes 00013fd6
- 00ba653c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d78:8"]]
- 00ba653c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6604 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e28:8"]]
+ 00ba6604 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba653c bytes 94be46f9
+ 00ba6604 bytes 941647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee1e49a1235cf3fe2aab82447dbf1cb4"></a>

### [`00ba665c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba665c.md) → [`00ba6724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6724.md) FUN_00ba6724

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6748",
      "incomplete_value": true,
      "site": "00ba674c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6680",
      "incomplete_value": true,
      "site": "00ba6684",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
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
      "definition_site": "00ba6754",
      "incomplete_value": true,
      "site": "00ba6758",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba668c",
      "incomplete_value": true,
      "site": "00ba6690",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba677c",
      "incomplete_value": true,
      "site": "00ba6780",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba66b4",
      "incomplete_value": true,
      "site": "00ba66b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
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
      "00ba6748",
      "READ",
      [
        "storage",
        "00c1bd88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba674c",
      "DATA",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6750",
      "READ",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6748",
      "READ",
      [
        "storage",
        "00c1be38",
        null,
        "pointer"
      ]
    ],
    [
      "00ba674c",
      "DATA",
      [
        "storage",
        "010a2900",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6750",
      "READ",
      [
        "storage",
        "010a2900",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba66b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba665c.md#insn-00ba66b8) · [`00ba674c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba665c.md#insn-00ba674c) · [`00ba6680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba665c.md#insn-00ba6680)
- 新版 `00ba6780`（命令位置の公開資料なし） · `00ba6814`（命令位置の公開資料なし） · `00ba6748`（命令位置の公開資料なし）

~~~diff
- 00ba66b8 ["INT_ADD", "register:40f0:8", ["const:ba66b8:8", "const:4:8"]]
- 00ba66b8 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba6780 ["INT_ADD", "register:40f0:8", ["const:ba6780:8", "const:4:8"]]
+ 00ba6780 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba66b8 bytes cae90094
+ 00ba6780 bytes c4e90094
- 00ba674c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba674c ["INT_ADD", "register:40f0:8", ["const:ba674c:8", "const:4:8"]]
- 00ba674c ["CALLIND", null, ["register:0:8"]]
+ 00ba6814 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba6814 ["INT_ADD", "register:40f0:8", ["const:ba6814:8", "const:4:8"]]
+ 00ba6814 ["CALLIND", null, ["register:0:8"]]
- 00ba674c bytes 00013fd6
+ 00ba6814 bytes 00013fd6
- 00ba6680 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
- 00ba6680 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6748 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e38:8"]]
+ 00ba6748 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6680 bytes 94c646f9
+ 00ba6748 bytes 941e47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c092f0f29ddfe3f0cc7e8e8ec48bf55"></a>

### [`00ba67a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba67a0.md) → [`00ba6868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6868.md) FUN_00ba6868

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba688c",
      "incomplete_value": true,
      "site": "00ba6890",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba67c4",
      "incomplete_value": true,
      "site": "00ba67c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
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
      "definition_site": "00ba6898",
      "incomplete_value": true,
      "site": "00ba689c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba67d0",
      "incomplete_value": true,
      "site": "00ba67d4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba68c0",
      "incomplete_value": true,
      "site": "00ba68c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba67f8",
      "incomplete_value": true,
      "site": "00ba67fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
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
      "00ba688c",
      "READ",
      [
        "storage",
        "00c1bd98",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6890",
      "DATA",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6894",
      "READ",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba688c",
      "READ",
      [
        "storage",
        "00c1be48",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6890",
      "DATA",
      [
        "storage",
        "010a2910",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6894",
      "READ",
      [
        "storage",
        "010a2910",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba67fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba67a0.md#insn-00ba67fc) · [`00ba6890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba67a0.md#insn-00ba6890) · [`00ba67c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba67a0.md#insn-00ba67c4)
- 新版 `00ba68c4`（命令位置の公開資料なし） · `00ba6958`（命令位置の公開資料なし） · `00ba688c`（命令位置の公開資料なし）

~~~diff
- 00ba67fc ["INT_ADD", "register:40f0:8", ["const:ba67fc:8", "const:4:8"]]
- 00ba67fc ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba68c4 ["INT_ADD", "register:40f0:8", ["const:ba68c4:8", "const:4:8"]]
+ 00ba68c4 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba67fc bytes 79e90094
+ 00ba68c4 bytes 73e90094
- 00ba6890 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba6890 ["INT_ADD", "register:40f0:8", ["const:ba6890:8", "const:4:8"]]
- 00ba6890 ["CALLIND", null, ["register:0:8"]]
+ 00ba6958 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba6958 ["INT_ADD", "register:40f0:8", ["const:ba6958:8", "const:4:8"]]
+ 00ba6958 ["CALLIND", null, ["register:0:8"]]
- 00ba6890 bytes 00013fd6
+ 00ba6958 bytes 00013fd6
- 00ba67c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
- 00ba67c4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba688c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e48:8"]]
+ 00ba688c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba67c4 bytes 94ce46f9
+ 00ba688c bytes 942647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b534a82ae115203beec557283a52151"></a>

### [`00ba68e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba68e4.md) → [`00ba69ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba69ac.md) FUN_00ba69ac

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba69d0",
      "incomplete_value": true,
      "site": "00ba69d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6908",
      "incomplete_value": true,
      "site": "00ba690c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
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
      "definition_site": "00ba69dc",
      "incomplete_value": true,
      "site": "00ba69e0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6914",
      "incomplete_value": true,
      "site": "00ba6918",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6a04",
      "incomplete_value": true,
      "site": "00ba6a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba693c",
      "incomplete_value": true,
      "site": "00ba6940",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
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
      "00ba69d0",
      "READ",
      [
        "storage",
        "00c1bda8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba69d4",
      "DATA",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba69d8",
      "READ",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba69d0",
      "READ",
      [
        "storage",
        "00c1be58",
        null,
        "pointer"
      ]
    ],
    [
      "00ba69d4",
      "DATA",
      [
        "storage",
        "010a2920",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba69d8",
      "READ",
      [
        "storage",
        "010a2920",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba68e4.md#insn-00ba6940) · [`00ba69d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba68e4.md#insn-00ba69d4) · [`00ba6908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba68e4.md#insn-00ba6908)
- 新版 `00ba6a08`（命令位置の公開資料なし） · `00ba6a9c`（命令位置の公開資料なし） · `00ba69d0`（命令位置の公開資料なし）

~~~diff
- 00ba6940 ["INT_ADD", "register:40f0:8", ["const:ba6940:8", "const:4:8"]]
- 00ba6940 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba6a08 ["INT_ADD", "register:40f0:8", ["const:ba6a08:8", "const:4:8"]]
+ 00ba6a08 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba6940 bytes 28e90094
+ 00ba6a08 bytes 22e90094
- 00ba69d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba69d4 ["INT_ADD", "register:40f0:8", ["const:ba69d4:8", "const:4:8"]]
- 00ba69d4 ["CALLIND", null, ["register:0:8"]]
+ 00ba6a9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba6a9c ["INT_ADD", "register:40f0:8", ["const:ba6a9c:8", "const:4:8"]]
+ 00ba6a9c ["CALLIND", null, ["register:0:8"]]
- 00ba69d4 bytes 00013fd6
+ 00ba6a9c bytes 00013fd6
- 00ba6908 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:da8:8"]]
- 00ba6908 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba69d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e58:8"]]
+ 00ba69d0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6908 bytes 94d646f9
+ 00ba69d0 bytes 942e47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7f14cca43122d1d16fb186b5ded8d09"></a>

### [`00ba6a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6a28.md) → [`00ba6af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6af0.md) FUN_00ba6af0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6b14",
      "incomplete_value": true,
      "site": "00ba6b18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6a4c",
      "incomplete_value": true,
      "site": "00ba6a50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "definition_site": "00ba6b20",
      "incomplete_value": true,
      "site": "00ba6b24",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6a58",
      "incomplete_value": true,
      "site": "00ba6a5c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6b48",
      "incomplete_value": true,
      "site": "00ba6b4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6a80",
      "incomplete_value": true,
      "site": "00ba6a84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "00ba6b14",
      "READ",
      [
        "storage",
        "00c1bc88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6b18",
      "DATA",
      [
        "storage",
        "010a2a80",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6b1c",
      "READ",
      [
        "storage",
        "010a2a80",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6b14",
      "READ",
      [
        "storage",
        "00c1bd38",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6b18",
      "DATA",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6b1c",
      "READ",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6a84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6a28.md#insn-00ba6a84) · [`00ba6b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6a28.md#insn-00ba6b18) · [`00ba6a4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6a28.md#insn-00ba6a4c)
- 新版 `00ba6b4c`（命令位置の公開資料なし） · `00ba6be0`（命令位置の公開資料なし） · `00ba6b14`（命令位置の公開資料なし）

~~~diff
- 00ba6a84 ["INT_ADD", "register:40f0:8", ["const:ba6a84:8", "const:4:8"]]
- 00ba6a84 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba6b4c ["INT_ADD", "register:40f0:8", ["const:ba6b4c:8", "const:4:8"]]
+ 00ba6b4c ["CALL", null, ["callee:00be0e90:8"]]
- 00ba6a84 bytes d7e80094
+ 00ba6b4c bytes d1e80094
- 00ba6b18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba6b18 ["INT_ADD", "register:40f0:8", ["const:ba6b18:8", "const:4:8"]]
- 00ba6b18 ["CALLIND", null, ["register:0:8"]]
+ 00ba6be0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba6be0 ["INT_ADD", "register:40f0:8", ["const:ba6be0:8", "const:4:8"]]
+ 00ba6be0 ["CALLIND", null, ["register:0:8"]]
- 00ba6b18 bytes 00013fd6
+ 00ba6be0 bytes 00013fd6
- 00ba6a4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
- 00ba6a4c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6b14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d38:8"]]
+ 00ba6b14 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6a4c bytes 944646f9
+ 00ba6b14 bytes 949e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5d843b14be54d5f79a5d863ed8f2162"></a>

### [`00ba6b6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6b6c.md) → [`00ba6c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6c34.md) FUN_00ba6c34

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6c58",
      "incomplete_value": true,
      "site": "00ba6c5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6b90",
      "incomplete_value": true,
      "site": "00ba6b94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
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
      "definition_site": "00ba6c64",
      "incomplete_value": true,
      "site": "00ba6c68",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6b9c",
      "incomplete_value": true,
      "site": "00ba6ba0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6c8c",
      "incomplete_value": true,
      "site": "00ba6c90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6bc4",
      "incomplete_value": true,
      "site": "00ba6bc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
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
      "00ba6c58",
      "READ",
      [
        "storage",
        "00c1bc98",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6c5c",
      "DATA",
      [
        "storage",
        "010a2a90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6c60",
      "READ",
      [
        "storage",
        "010a2a90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6c58",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6c5c",
      "DATA",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6c60",
      "READ",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6b6c.md#insn-00ba6bc8) · [`00ba6c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6b6c.md#insn-00ba6c5c) · [`00ba6b90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6b6c.md#insn-00ba6b90)
- 新版 `00ba6c90`（命令位置の公開資料なし） · `00ba6d24`（命令位置の公開資料なし） · `00ba6c58`（命令位置の公開資料なし）

~~~diff
- 00ba6bc8 ["INT_ADD", "register:40f0:8", ["const:ba6bc8:8", "const:4:8"]]
- 00ba6bc8 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba6c90 ["INT_ADD", "register:40f0:8", ["const:ba6c90:8", "const:4:8"]]
+ 00ba6c90 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba6bc8 bytes 86e80094
+ 00ba6c90 bytes 80e80094
- 00ba6c5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba6c5c ["INT_ADD", "register:40f0:8", ["const:ba6c5c:8", "const:4:8"]]
- 00ba6c5c ["CALLIND", null, ["register:0:8"]]
+ 00ba6d24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba6d24 ["INT_ADD", "register:40f0:8", ["const:ba6d24:8", "const:4:8"]]
+ 00ba6d24 ["CALLIND", null, ["register:0:8"]]
- 00ba6c5c bytes 00013fd6
+ 00ba6d24 bytes 00013fd6
- 00ba6b90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
- 00ba6b90 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6c58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d48:8"]]
+ 00ba6c58 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6b90 bytes 944e46f9
+ 00ba6c58 bytes 94a646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff33d08248fe1fc550416a7b30768733"></a>

### [`00ba6cb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6cb0.md) → [`00ba6d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6d78.md) FUN_00ba6d78

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6d9c",
      "incomplete_value": true,
      "site": "00ba6da0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6cd4",
      "incomplete_value": true,
      "site": "00ba6cd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
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
      "definition_site": "00ba6da8",
      "incomplete_value": true,
      "site": "00ba6dac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6ce0",
      "incomplete_value": true,
      "site": "00ba6ce4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6dd0",
      "incomplete_value": true,
      "site": "00ba6dd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6d08",
      "incomplete_value": true,
      "site": "00ba6d0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
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
      "00ba6d9c",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6da0",
      "DATA",
      [
        "storage",
        "010a2770",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6da4",
      "READ",
      [
        "storage",
        "010a2770",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6d9c",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6da0",
      "DATA",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6da4",
      "READ",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6d0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6cb0.md#insn-00ba6d0c) · [`00ba6da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6cb0.md#insn-00ba6da0) · [`00ba6cd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6cb0.md#insn-00ba6cd4)
- 新版 `00ba6dd4`（命令位置の公開資料なし） · `00ba6e68`（命令位置の公開資料なし） · `00ba6d9c`（命令位置の公開資料なし）

~~~diff
- 00ba6d0c ["INT_ADD", "register:40f0:8", ["const:ba6d0c:8", "const:4:8"]]
- 00ba6d0c ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba6dd4 ["INT_ADD", "register:40f0:8", ["const:ba6dd4:8", "const:4:8"]]
+ 00ba6dd4 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba6d0c bytes 35e80094
+ 00ba6dd4 bytes 2fe80094
- 00ba6da0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba6da0 ["INT_ADD", "register:40f0:8", ["const:ba6da0:8", "const:4:8"]]
- 00ba6da0 ["CALLIND", null, ["register:0:8"]]
+ 00ba6e68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba6e68 ["INT_ADD", "register:40f0:8", ["const:ba6e68:8", "const:4:8"]]
+ 00ba6e68 ["CALLIND", null, ["register:0:8"]]
- 00ba6da0 bytes 00013fd6
+ 00ba6e68 bytes 00013fd6
- 00ba6cd4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
- 00ba6cd4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6d9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c90:8"]]
+ 00ba6d9c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6cd4 bytes 94f245f9
+ 00ba6d9c bytes 944a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd62dbbe3461d92717fad220505d3437"></a>

### [`00ba6df4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6df4.md) → [`00ba6ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6ebc.md) FUN_00ba6ebc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6ee0",
      "incomplete_value": true,
      "site": "00ba6ee4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6e18",
      "incomplete_value": true,
      "site": "00ba6e1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "definition_site": "00ba6eec",
      "incomplete_value": true,
      "site": "00ba6ef0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6e24",
      "incomplete_value": true,
      "site": "00ba6e28",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6f14",
      "incomplete_value": true,
      "site": "00ba6f18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6e4c",
      "incomplete_value": true,
      "site": "00ba6e50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00ba6ee0",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6ee4",
      "DATA",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6ee8",
      "READ",
      [
        "storage",
        "010a2780",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6ee0",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6ee4",
      "DATA",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6ee8",
      "READ",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6df4.md#insn-00ba6e50) · [`00ba6ee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6df4.md#insn-00ba6ee4) · [`00ba6e18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6df4.md#insn-00ba6e18)
- 新版 `00ba6f18`（命令位置の公開資料なし） · `00ba6fac`（命令位置の公開資料なし） · `00ba6ee0`（命令位置の公開資料なし）

~~~diff
- 00ba6e50 ["INT_ADD", "register:40f0:8", ["const:ba6e50:8", "const:4:8"]]
- 00ba6e50 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba6f18 ["INT_ADD", "register:40f0:8", ["const:ba6f18:8", "const:4:8"]]
+ 00ba6f18 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba6e50 bytes e4e70094
+ 00ba6f18 bytes dee70094
- 00ba6ee4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba6ee4 ["INT_ADD", "register:40f0:8", ["const:ba6ee4:8", "const:4:8"]]
- 00ba6ee4 ["CALLIND", null, ["register:0:8"]]
+ 00ba6fac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba6fac ["INT_ADD", "register:40f0:8", ["const:ba6fac:8", "const:4:8"]]
+ 00ba6fac ["CALLIND", null, ["register:0:8"]]
- 00ba6ee4 bytes 00013fd6
+ 00ba6fac bytes 00013fd6
- 00ba6e18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c18:8"]]
- 00ba6e18 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6ee0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc8:8"]]
+ 00ba6ee0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6e18 bytes 940e46f9
+ 00ba6ee0 bytes 946646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9ef1a92dcaf804df55df3c2cdf3cb3b"></a>

### [`00ba6f38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6f38.md) → [`00ba7000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7000.md) FUN_00ba7000

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba7024",
      "incomplete_value": true,
      "site": "00ba7028",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6f5c",
      "incomplete_value": true,
      "site": "00ba6f60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
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
      "definition_site": "00ba7030",
      "incomplete_value": true,
      "site": "00ba7034",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6f68",
      "incomplete_value": true,
      "site": "00ba6f6c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba7058",
      "incomplete_value": true,
      "site": "00ba705c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6f90",
      "incomplete_value": true,
      "site": "00ba6f94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
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
      "00ba7024",
      "READ",
      [
        "storage",
        "00c1b940",
        null,
        "pointer"
      ]
    ],
    [
      "00ba7028",
      "DATA",
      [
        "storage",
        "010a2790",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba702c",
      "READ",
      [
        "storage",
        "010a2790",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba7024",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba7028",
      "DATA",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba702c",
      "READ",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6f38.md#insn-00ba6f94) · [`00ba7028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6f38.md#insn-00ba7028) · [`00ba6f5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6f38.md#insn-00ba6f5c)
- 新版 `00ba705c`（命令位置の公開資料なし） · `00ba70f0`（命令位置の公開資料なし） · `00ba7024`（命令位置の公開資料なし）

~~~diff
- 00ba6f94 ["INT_ADD", "register:40f0:8", ["const:ba6f94:8", "const:4:8"]]
- 00ba6f94 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba705c ["INT_ADD", "register:40f0:8", ["const:ba705c:8", "const:4:8"]]
+ 00ba705c ["CALL", null, ["callee:00be0e90:8"]]
- 00ba6f94 bytes 93e70094
+ 00ba705c bytes 8de70094
- 00ba7028 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba7028 ["INT_ADD", "register:40f0:8", ["const:ba7028:8", "const:4:8"]]
- 00ba7028 ["CALLIND", null, ["register:0:8"]]
+ 00ba70f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba70f0 ["INT_ADD", "register:40f0:8", ["const:ba70f0:8", "const:4:8"]]
+ 00ba70f0 ["CALLIND", null, ["register:0:8"]]
- 00ba7028 bytes 00013fd6
+ 00ba70f0 bytes 00013fd6
- 00ba6f5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
- 00ba6f5c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba7024 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
+ 00ba7024 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6f5c bytes 94a244f9
+ 00ba7024 bytes 94fa44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcbe48842e048b8623dbc83163c03c59"></a>

### [`00ba707c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba707c.md) → [`00ba7144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7144.md) FUN_00ba7144

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 75.00% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba70a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba716c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba70b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba70a0",
      "READ",
      [
        "storage",
        "00c1bc28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba70a4",
      "DATA",
      [
        "storage",
        "010a27a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba70a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba7168",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba716c",
      "DATA",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba716c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba70a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba707c.md#insn-00ba70a4) · [`00ba70b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba707c.md#insn-00ba70b0) · [`00ba70d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba707c.md#insn-00ba70d8)
- 新版 `00ba71a0`（命令位置の公開資料なし）

~~~diff
- 00ba70a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba70a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba70a4 bytes f40700f9
- 00ba70b0 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba70b0 bytes 60010054
- 00ba70d8 ["INT_ADD", "register:40f0:8", ["const:ba70d8:8", "const:4:8"]]
- 00ba70d8 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba71a0 ["INT_ADD", "register:40f0:8", ["const:ba71a0:8", "const:4:8"]]
+ 00ba71a0 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba70d8 bytes 42e70094
+ 00ba71a0 bytes 3ce70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-705615e8b8c6016ead5c2d69f2e14a98"></a>

### [`00ba71c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba71c0.md) → [`00ba7288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7288.md) FUN_00ba7288

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.71% / 新版 75.71%

CFGの説明率　旧版 40.91% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba71c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba71c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba71cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba71c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba71cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba71d0",
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
      "00ba7290",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ba7294",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ba7298",
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

- 旧版 [`00ba71c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba71c0.md#insn-00ba71c8) · [`00ba71cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba71c0.md#insn-00ba71cc) · [`00ba71d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba71c0.md#insn-00ba71d0)

~~~diff
- 00ba71c8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ba71c8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ba71c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ba71c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba71c8 bytes fd7b02a9
- 00ba71cc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ba71cc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ba71cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00ba71cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba71cc bytes f65703a9
- 00ba71d0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ba71d0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ba71d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00ba71d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba71d0 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9167fe5dcf538d136cfa3ac9bcf4b7b"></a>

### [`00ba7304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7304.md) → [`00ba73cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba73cc.md) FUN_00ba73cc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba73f0",
      "incomplete_value": true,
      "site": "00ba73f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7328",
      "incomplete_value": true,
      "site": "00ba732c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc0:8"
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
      "definition_site": "00ba73fc",
      "incomplete_value": true,
      "site": "00ba7400",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba7334",
      "incomplete_value": true,
      "site": "00ba7338",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba7424",
      "incomplete_value": true,
      "site": "00ba7428",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba735c",
      "incomplete_value": true,
      "site": "00ba7360",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc0:8"
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
      "00ba73f0",
      "READ",
      [
        "storage",
        "00c1bdc0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba73f4",
      "DATA",
      [
        "storage",
        "010a27c0",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba73f8",
      "READ",
      [
        "storage",
        "010a27c0",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba73f0",
      "READ",
      [
        "storage",
        "00c1be70",
        null,
        "pointer"
      ]
    ],
    [
      "00ba73f4",
      "DATA",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba73f8",
      "READ",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7304.md#insn-00ba7360) · [`00ba73f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7304.md#insn-00ba73f4) · [`00ba7328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7304.md#insn-00ba7328)
- 新版 `00ba7428`（命令位置の公開資料なし） · `00ba74bc`（命令位置の公開資料なし） · `00ba73f0`（命令位置の公開資料なし）

~~~diff
- 00ba7360 ["INT_ADD", "register:40f0:8", ["const:ba7360:8", "const:4:8"]]
- 00ba7360 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba7428 ["INT_ADD", "register:40f0:8", ["const:ba7428:8", "const:4:8"]]
+ 00ba7428 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba7360 bytes a0e60094
+ 00ba7428 bytes 9ae60094
- 00ba73f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba73f4 ["INT_ADD", "register:40f0:8", ["const:ba73f4:8", "const:4:8"]]
- 00ba73f4 ["CALLIND", null, ["register:0:8"]]
+ 00ba74bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba74bc ["INT_ADD", "register:40f0:8", ["const:ba74bc:8", "const:4:8"]]
+ 00ba74bc ["CALLIND", null, ["register:0:8"]]
- 00ba73f4 bytes 00013fd6
+ 00ba74bc bytes 00013fd6
- 00ba7328 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc0:8"]]
- 00ba7328 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba73f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e70:8"]]
+ 00ba73f0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba7328 bytes 94e246f9
+ 00ba73f0 bytes 943a47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24980f19d3bc8c9b108e5fe7da8ceb3f"></a>

### [`00ba7448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7448.md) → [`00ba7510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7510.md) FUN_00ba7510

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba7534",
      "incomplete_value": true,
      "site": "00ba7538",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba746c",
      "incomplete_value": true,
      "site": "00ba7470",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:408:8"
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
      "definition_site": "00ba7540",
      "incomplete_value": true,
      "site": "00ba7544",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba7478",
      "incomplete_value": true,
      "site": "00ba747c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba7568",
      "incomplete_value": true,
      "site": "00ba756c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba74a0",
      "incomplete_value": true,
      "site": "00ba74a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:408:8"
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
      "00ba7534",
      "READ",
      [
        "storage",
        "00c1b408",
        null,
        "pointer"
      ]
    ],
    [
      "00ba7538",
      "DATA",
      [
        "storage",
        "010a27d0",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba753c",
      "READ",
      [
        "storage",
        "010a27d0",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba7534",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba7538",
      "DATA",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba753c",
      "READ",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba74a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7448.md#insn-00ba74a4) · [`00ba7538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7448.md#insn-00ba7538) · [`00ba746c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7448.md#insn-00ba746c)
- 新版 `00ba756c`（命令位置の公開資料なし） · `00ba7600`（命令位置の公開資料なし） · `00ba7534`（命令位置の公開資料なし）

~~~diff
- 00ba74a4 ["INT_ADD", "register:40f0:8", ["const:ba74a4:8", "const:4:8"]]
- 00ba74a4 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba756c ["INT_ADD", "register:40f0:8", ["const:ba756c:8", "const:4:8"]]
+ 00ba756c ["CALL", null, ["callee:00be0e90:8"]]
- 00ba74a4 bytes 4fe60094
+ 00ba756c bytes 49e60094
- 00ba7538 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba7538 ["INT_ADD", "register:40f0:8", ["const:ba7538:8", "const:4:8"]]
- 00ba7538 ["CALLIND", null, ["register:0:8"]]
+ 00ba7600 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba7600 ["INT_ADD", "register:40f0:8", ["const:ba7600:8", "const:4:8"]]
+ 00ba7600 ["CALLIND", null, ["register:0:8"]]
- 00ba7538 bytes 00013fd6
+ 00ba7600 bytes 00013fd6
- 00ba746c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:408:8"]]
- 00ba746c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba7534 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4b8:8"]]
+ 00ba7534 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba746c bytes 940642f9
+ 00ba7534 bytes 945e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f1fc0f4a3ab2f452465a44957b8e18d"></a>

### [`00ba758c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba758c.md) → [`00ba7654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7654.md) FUN_00ba7654

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 70.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba75b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba767c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba75c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba75b0",
      "READ",
      [
        "storage",
        "00c1bde0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba75b4",
      "DATA",
      [
        "storage",
        "010a27e0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba75b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba7678",
      "READ",
      [
        "storage",
        "00c1be90",
        null,
        "pointer"
      ]
    ],
    [
      "00ba767c",
      "DATA",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba767c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba75b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba758c.md#insn-00ba75b4) · [`00ba75c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba758c.md#insn-00ba75c0) · [`00ba75e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba758c.md#insn-00ba75e8)
- 新版 `00ba76b0`（命令位置の公開資料なし）

~~~diff
- 00ba75b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba75b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba75b4 bytes f40700f9
- 00ba75c0 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba75c0 bytes 60010054
- 00ba75e8 ["INT_ADD", "register:40f0:8", ["const:ba75e8:8", "const:4:8"]]
- 00ba75e8 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba76b0 ["INT_ADD", "register:40f0:8", ["const:ba76b0:8", "const:4:8"]]
+ 00ba76b0 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba75e8 bytes fee50094
+ 00ba76b0 bytes f8e50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-650b9cd0993bc8ec550c9bb5d83ea58e"></a>

### [`00ba76d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba76d0.md) → [`00ba7798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7798.md) FUN_00ba7798

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 80.95% / 新版 85.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba76f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba77c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7704"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba76f4",
      "READ",
      [
        "storage",
        "00c1bdf0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba76f8",
      "DATA",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba76f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba77bc",
      "READ",
      [
        "storage",
        "00c1bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba77c0",
      "DATA",
      [
        "storage",
        "010a2930",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba77c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba76f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba76d0.md#insn-00ba76f8) · [`00ba7704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba76d0.md#insn-00ba7704) · [`00ba772c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba76d0.md#insn-00ba772c)
- 新版 `00ba77f4`（命令位置の公開資料なし）

~~~diff
- 00ba76f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba76f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba76f8 bytes f40700f9
- 00ba7704 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00ba7704 bytes 60010054
- 00ba772c ["INT_ADD", "register:40f0:8", ["const:ba772c:8", "const:4:8"]]
- 00ba772c ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba77f4 ["INT_ADD", "register:40f0:8", ["const:ba77f4:8", "const:4:8"]]
+ 00ba77f4 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba772c bytes ade50094
+ 00ba77f4 bytes a7e50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7036ca1546b914d058a34052ac9a71c"></a>

### [`00ba7814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7814.md) → [`00ba78dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba78dc.md) FUN_00ba78dc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) · 呼出先 6件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 54.55% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba783c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba7904"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7848"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba7838",
      "READ",
      [
        "storage",
        "00c1be00",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba783c",
      "DATA",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba783c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba7900",
      "READ",
      [
        "storage",
        "00c1beb0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba7904",
      "DATA",
      [
        "storage",
        "010a2940",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba7904",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba783c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7814.md#insn-00ba783c) · [`00ba7848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7814.md#insn-00ba7848) · [`00ba7870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7814.md#insn-00ba7870)
- 新版 `00ba7938`（命令位置の公開資料なし）

~~~diff
- 00ba783c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba783c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba783c bytes f40700f9
- 00ba7848 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00ba7848 bytes 60010054
- 00ba7870 ["INT_ADD", "register:40f0:8", ["const:ba7870:8", "const:4:8"]]
- 00ba7870 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba7938 ["INT_ADD", "register:40f0:8", ["const:ba7938:8", "const:4:8"]]
+ 00ba7938 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba7870 bytes 5ce50094
+ 00ba7938 bytes 56e50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cacc02da02d6880ea1a65ea937f1945"></a>

### [`00ba7958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7958.md) → [`00ba7a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7a20.md) FUN_00ba7a20

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba8394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8394.md) · 呼出先 10件 [`00bb8954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8954.md) [`00bb896c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb896c.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00ba845c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba845c.md) · 呼出先 10件 [`00bb8a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a1c.md) [`00bb8a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a34.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.64% / 新版 90.64%

CFGの説明率　旧版 59.26% / 新版 56.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7988"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7988"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7a20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba7988",
      "DATA",
      [
        "storage",
        "00c13818",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00ba79b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7c30"
      ]
    ],
    [
      "unmatched:00ba7ae4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7bd0"
      ]
    ]
  ],
  "added": [
    [
      "00ba7a50",
      "DATA",
      [
        "storage",
        "00c138c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00ba7a80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7c30"
      ]
    ],
    [
      "00ba7bac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7bd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7958.md#insn-00ba7988) · [`00ba79b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7958.md#insn-00ba79b4) · [`00ba79b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7958.md#insn-00ba79b8)

~~~diff
- 00ba7988 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00ba7988 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00ba7988 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00ba7988 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba7988 bytes 0b2800a9
- 00ba79b4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ba79b4 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00ba79b4 ["COPY", "tmp:2:8", ["register:4058:8"]]
- 00ba79b4 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00ba79b4 bytes 7a95899a
- 00ba79b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00ba79b8 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
- 00ba79b8 bytes 8a0d00b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a9fa21349bbcadede91577d25bee1c2"></a>

### [`00ba7c2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7c2c.md) → [`00ba7cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7cf4.md) FUN_00ba7cf4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba7d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7d00.md) · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 1件 [`00ba7dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7dc8.md) · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.91% / 新版 84.91%

CFGの説明率　旧版 40.91% / 新版 45.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7c54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba7d1c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7c5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba7c54",
      "DATA",
      [
        "storage",
        "00c13818",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00ba7c5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7d7c"
      ]
    ],
    [
      "unmatched:00ba7c84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7d7c"
      ]
    ]
  ],
  "added": [
    [
      "00ba7d1c",
      "DATA",
      [
        "storage",
        "00c138c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00ba7d24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7d7c"
      ]
    ],
    [
      "00ba7d4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7d7c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7c2c.md#insn-00ba7c54) · [`00ba7c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7c2c.md#insn-00ba7c5c) · [`00ba7c84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7c2c.md#insn-00ba7c84)

~~~diff
- 00ba7c54 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ba7c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ba7c54 bytes 680200f9
- 00ba7c5c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00ba7c5c bytes c0020054
- 00ba7c84 ["CBRANCH", null, ["local:b9:8", "register:102:1"]]
- 00ba7c84 bytes 82010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55382ba121fce0caab1cd80530f2e329"></a>

### [`00ba7d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7d00.md) → [`00ba7dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7dc8.md) FUN_00ba7dc8

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00ba7c2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7c2c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00ba7cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7cf4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba7d14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7d00.md#insn-00ba7d14)
- 新版 `00ba7ddc`（命令位置の公開資料なし）

~~~diff
- 00ba7d14 ["INT_ADD", "register:40f0:8", ["const:ba7d14:8", "const:4:8"]]
- 00ba7d14 ["CALL", null, ["callee:00ba7cf4:8"]]
+ 00ba7ddc ["INT_ADD", "register:40f0:8", ["const:ba7ddc:8", "const:4:8"]]
+ 00ba7ddc ["CALL", null, ["callee:00ba7cf4:8"]]
- 00ba7d14 bytes c6ffff97
+ 00ba7ddc bytes c6ffff97
~~~


<a id="compare-3d909e325217ddf3133ca1a9a27601cb"></a>

### [`00ba7d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7d2c.md) → [`00ba7df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7df4.md) _ZNSt6__ndk16locale8__globalEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md) [`00be17d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be17d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1880.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7d48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ba7e10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba7e30",
      "incomplete_value": false,
      "site": "00ba7e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7d68",
      "incomplete_value": false,
      "site": "00ba7d6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "unmatched:00ba7d44",
      "READ",
      [
        "storage",
        "010a29f0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ba7d48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7e2c"
      ]
    ],
    [
      "unmatched:00ba7d50",
      "DATA",
      [
        "storage",
        "010a29e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba7e0c",
      "READ",
      [
        "storage",
        "010a2ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba7e10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7e2c"
      ]
    ],
    [
      "00ba7e18",
      "DATA",
      [
        "storage",
        "010a2aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7d2c.md#insn-00ba7d48) · [`00ba7d6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7d2c.md#insn-00ba7d6c) · [`00ba7d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7d2c.md#insn-00ba7d84)
- 新版 `00ba7e34`（命令位置の公開資料なし）

~~~diff
- 00ba7d48 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00ba7d48 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ba7d48 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ba7d48 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00ba7d48 bytes e8000036
- 00ba7d6c ["INT_ADD", "register:40f0:8", ["const:ba7d6c:8", "const:4:8"]]
- 00ba7d6c ["CALL", null, ["callee:00bdafb0:8"]]
+ 00ba7e34 ["INT_ADD", "register:40f0:8", ["const:ba7e34:8", "const:4:8"]]
+ 00ba7e34 ["CALL", null, ["callee:00bdafb0:8"]]
- 00ba7d6c bytes 65cc0094
+ 00ba7e34 bytes 5fcc0094
- 00ba7d84 ["INT_ADD", "register:40f0:8", ["const:ba7d84:8", "const:4:8"]]
- 00ba7d84 ["CALL", null, ["callee:00bdd930:8"]]
- 00ba7d84 bytes bfd60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7ee66de07e7cbb41629c227743076f1"></a>

### [`00ba7db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7db0.md) → [`00ba7e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7e78.md) _ZNSt6__ndk16localeC1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd850.md) · 呼出先 5件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md) [`00be17d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be17d0.md)
- 新版 呼出元 1件 [`00bdd900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd900.md) · 呼出先 5件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1880.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 12.50% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7de8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba7eb0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7dd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba7dcc",
      "READ",
      [
        "storage",
        "010a29f0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ba7dd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7ed4"
      ]
    ],
    [
      "unmatched:00ba7de0",
      "READ",
      [
        "storage",
        "010a29e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba7e94",
      "READ",
      [
        "storage",
        "010a2ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba7e98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7ed4"
      ]
    ],
    [
      "00ba7ea8",
      "READ",
      [
        "storage",
        "010a2aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7db0.md#insn-00ba7dd0) · [`00ba7de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7db0.md#insn-00ba7de8) · [`00ba7dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7db0.md#insn-00ba7dec)

~~~diff
- 00ba7dd0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00ba7dd0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ba7dd0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ba7dd0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00ba7dd0 bytes e8010036
- 00ba7de8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ba7de8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ba7de8 bytes 680200f9
- 00ba7dec ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00ba7dec bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cf7e0a15345a17980cce45192346608"></a>

### [`00ba7e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7e58.md) → [`00ba7f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7f20.md) _ZNSt6__ndk16localeC1ERKS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md) · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 1件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7e6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba7f34"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7e70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba7e70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7f5c"
      ]
    ]
  ],
  "added": [
    [
      "00ba7f38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7f5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7e6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7e58.md#insn-00ba7e6c) · [`00ba7e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7e58.md#insn-00ba7e70)
- 新版 `00ba7f34`（命令位置の公開資料なし）

~~~diff
- 00ba7e6c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00ba7e6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ba7e6c bytes 080000f9
- 00ba7e70 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba7e70 bytes 20010054
+ 00ba7f34 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00ba7f34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00ba7f34 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f99b4b7fe61aef28dc23160c1944a26"></a>

### [`00ba7f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7f80.md) → [`00ba8048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8048.md) _ZNSt6__ndk16localeC1EPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 47.06% / 新版 47.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8014"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba80dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ba7fb4",
      "incomplete_value": true,
      "site": "00ba7fb8",
      "value": [
        "live",
        "register:40a8:8"
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
      "unmatched:00ba8014",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba807c",
      "PARAM",
      [
        "storage",
        "002a526b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ba8080",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0f60"
      ]
    ]
  ],
  "added": [
    [
      "00ba80dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00ba8144",
      "PARAM",
      [
        "storage",
        "002a5264",
        null,
        "string"
      ]
    ],
    [
      "00ba8148",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0f60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7fb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7f80.md#insn-00ba7fb8) · [`00ba8004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7f80.md#insn-00ba8004) · [`00ba8014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7f80.md#insn-00ba8014)
- 新版 `00ba8080`（命令位置の公開資料なし） · `00ba80cc`（命令位置の公開資料なし）

~~~diff
- 00ba7fb8 ["INT_ADD", "register:40f0:8", ["const:ba7fb8:8", "const:4:8"]]
- 00ba7fb8 ["CALL", null, ["callee:00bdb140:8"]]
+ 00ba8080 ["INT_ADD", "register:40f0:8", ["const:ba8080:8", "const:4:8"]]
+ 00ba8080 ["CALL", null, ["callee:00bdb140:8"]]
- 00ba7fb8 bytes 36cc0094
+ 00ba8080 bytes 30cc0094
- 00ba8004 ["INT_ADD", "register:40f0:8", ["const:ba8004:8", "const:4:8"]]
- 00ba8004 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ba80cc ["INT_ADD", "register:40f0:8", ["const:ba80cc:8", "const:4:8"]]
+ 00ba80cc ["CALL", null, ["callee:00bdaff0:8"]]
- 00ba8004 bytes cfcb0094
+ 00ba80cc bytes c9cb0094
- 00ba8014 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba8014 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ba8014 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6752bb3c2ef0d3b5a392d548d69db1c"></a>

### [`00ba80b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba80b8.md) → [`00ba8180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8180.md) _ZNSt6__ndk16localeC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ba2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba2/00ba2510.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba8198",
      "incomplete_value": false,
      "site": "00ba81a0",
      "value": [
        "leaf",
        "const:138:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba80d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba80b8.md#insn-00ba80d8) · [`00ba80e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba80b8.md#insn-00ba80e8) · [`00ba80f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba80b8.md#insn-00ba80f8)
- 新版 `00ba81a0`（命令位置の公開資料なし） · `00ba81b0`（命令位置の公開資料なし） · `00ba81c0`（命令位置の公開資料なし）

~~~diff
- 00ba80d8 ["INT_ADD", "register:40f0:8", ["const:ba80d8:8", "const:4:8"]]
- 00ba80d8 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ba81a0 ["INT_ADD", "register:40f0:8", ["const:ba81a0:8", "const:4:8"]]
+ 00ba81a0 ["CALL", null, ["callee:00bdaff0:8"]]
- 00ba80d8 bytes 9acb0094
+ 00ba81a0 bytes 94cb0094
- 00ba80e8 ["INT_ADD", "register:40f0:8", ["const:ba80e8:8", "const:4:8"]]
- 00ba80e8 ["CALL", null, ["callee:00ba25d8:8"]]
+ 00ba81b0 ["INT_ADD", "register:40f0:8", ["const:ba81b0:8", "const:4:8"]]
+ 00ba81b0 ["CALL", null, ["callee:00ba25d8:8"]]
- 00ba80e8 bytes 0ae9ff97
+ 00ba81b0 bytes 0ae9ff97
- 00ba80f8 ["INT_ADD", "register:40f0:8", ["const:ba80f8:8", "const:4:8"]]
- 00ba80f8 ["CALL", null, ["callee:00bd6e20:8"]]
+ 00ba81c0 ["INT_ADD", "register:40f0:8", ["const:ba81c0:8", "const:4:8"]]
+ 00ba81c0 ["CALL", null, ["callee:00bd6e20:8"]]
- 00ba80f8 bytes 1abb0094
+ 00ba81c0 bytes 18bb0094
~~~


<a id="compare-16f5afb6a2038e1306b330be6cf01892"></a>

### [`00ba8124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8124.md) → [`00ba81ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba81ec.md) _ZNSt6__ndk16localeC2ERKS0_PKci

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 35.29% / 新版 35.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba81ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ba8274"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba82cc",
      "incomplete_value": true,
      "site": "00ba82d8",
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
      "unmatched:00ba8238",
      "PARAM",
      [
        "storage",
        "002a526b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ba823c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0f60"
      ]
    ]
  ],
  "added": [
    [
      "00ba8300",
      "PARAM",
      [
        "storage",
        "002a5264",
        null,
        "string"
      ]
    ],
    [
      "00ba8304",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0f60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba81ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8124.md#insn-00ba81ac) · [`00ba8210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8124.md#insn-00ba8210) · [`00ba823c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8124.md#insn-00ba823c)
- 新版 `00ba82d8`（命令位置の公開資料なし）

~~~diff
- 00ba81ac ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba81ac ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00ba81ac ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ba81ac ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00ba81ac bytes 0801899a
- 00ba8210 ["INT_ADD", "register:40f0:8", ["const:ba8210:8", "const:4:8"]]
- 00ba8210 ["CALL", null, ["callee:00bd6e20:8"]]
+ 00ba82d8 ["INT_ADD", "register:40f0:8", ["const:ba82d8:8", "const:4:8"]]
+ 00ba82d8 ["CALL", null, ["callee:00bd6e20:8"]]
- 00ba8210 bytes d4ba0094
+ 00ba82d8 bytes d2ba0094
- 00ba823c ["INT_ADD", "register:40f0:8", ["const:ba823c:8", "const:4:8"]]
- 00ba823c ["CALL", null, ["callee:00be0f60:8"]]
- 00ba823c bytes 1de30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-522c9f25b4731b98c8e402845c2b6340"></a>

### [`00ba8274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8274.md) → [`00ba833c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba833c.md) _ZNSt6__ndk16localeC1ERKS0_RKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ba49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba49ac.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ba82b8",
      "incomplete_value": false,
      "site": "00ba82c0",
      "value": [
        "leaf",
        "const:1:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ba82b4",
      "incomplete_value": true,
      "site": "00ba82c0",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba82c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8274.md#insn-00ba82c0) · [`00ba829c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8274.md#insn-00ba829c) · [`00ba82b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8274.md#insn-00ba82b0)
- 新版 `00ba8388`（命令位置の公開資料なし） · `00ba8364`（命令位置の公開資料なし） · `00ba8378`（命令位置の公開資料なし）

~~~diff
- 00ba82c0 ["INT_ADD", "register:40f0:8", ["const:ba82c0:8", "const:4:8"]]
- 00ba82c0 ["CALL", null, ["callee:00bd6e20:8"]]
+ 00ba8388 ["INT_ADD", "register:40f0:8", ["const:ba8388:8", "const:4:8"]]
+ 00ba8388 ["CALL", null, ["callee:00bd6e20:8"]]
- 00ba82c0 bytes a8ba0094
+ 00ba8388 bytes a6ba0094
- 00ba829c ["INT_ADD", "register:40f0:8", ["const:ba829c:8", "const:4:8"]]
- 00ba829c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ba8364 ["INT_ADD", "register:40f0:8", ["const:ba8364:8", "const:4:8"]]
+ 00ba8364 ["CALL", null, ["callee:00bdaff0:8"]]
- 00ba829c bytes 29cb0094
+ 00ba8364 bytes 23cb0094
- 00ba82b0 ["INT_ADD", "register:40f0:8", ["const:ba82b0:8", "const:4:8"]]
- 00ba82b0 ["CALL", null, ["callee:00ba4a74:8"]]
+ 00ba8378 ["INT_ADD", "register:40f0:8", ["const:ba8378:8", "const:4:8"]]
+ 00ba8378 ["CALL", null, ["callee:00ba4a74:8"]]
- 00ba82b0 bytes bff1ff97
+ 00ba8378 bytes bff1ff97
~~~


<a id="compare-2561d7f945ee0a439c1f237b9c14c785"></a>

### [`00ba82ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba82ec.md) → [`00ba83b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba83b4.md) _ZNSt6__ndk16localeC2ERKS0_S2_i

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ba4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba4/00ba4ffc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ba832c",
      "incomplete_value": true,
      "site": "00ba8338",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba82ec.md#insn-00ba8338) · [`00ba8314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba82ec.md#insn-00ba8314) · [`00ba8328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba82ec.md#insn-00ba8328)
- 新版 `00ba8400`（命令位置の公開資料なし） · `00ba83dc`（命令位置の公開資料なし） · `00ba83f0`（命令位置の公開資料なし）

~~~diff
- 00ba8338 ["INT_ADD", "register:40f0:8", ["const:ba8338:8", "const:4:8"]]
- 00ba8338 ["CALL", null, ["callee:00bd6e20:8"]]
+ 00ba8400 ["INT_ADD", "register:40f0:8", ["const:ba8400:8", "const:4:8"]]
+ 00ba8400 ["CALL", null, ["callee:00bd6e20:8"]]
- 00ba8338 bytes 8aba0094
+ 00ba8400 bytes 88ba0094
- 00ba8314 ["INT_ADD", "register:40f0:8", ["const:ba8314:8", "const:4:8"]]
- 00ba8314 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ba83dc ["INT_ADD", "register:40f0:8", ["const:ba83dc:8", "const:4:8"]]
+ 00ba83dc ["CALL", null, ["callee:00bdaff0:8"]]
- 00ba8314 bytes 0bcb0094
+ 00ba83dc bytes 05cb0094
- 00ba8328 ["INT_ADD", "register:40f0:8", ["const:ba8328:8", "const:4:8"]]
- 00ba8328 ["CALL", null, ["callee:00ba50c4:8"]]
+ 00ba83f0 ["INT_ADD", "register:40f0:8", ["const:ba83f0:8", "const:4:8"]]
+ 00ba83f0 ["CALL", null, ["callee:00ba50c4:8"]]
- 00ba8328 bytes 35f3ff97
+ 00ba83f0 bytes 35f3ff97
~~~


<a id="compare-264a96d0ca7c431130b33e91c3780b0c"></a>

### [`00ba8394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8394.md) → [`00ba845c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba845c.md) _ZNSt6__ndk16locale14__install_ctorERKS0_PNS0_5facetEl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ba7958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7958.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00ba7a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7a20.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba84b4",
      "incomplete_value": true,
      "site": "00ba84bc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00ba83ec",
      "incomplete_value": true,
      "site": "00ba83f4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "ordinal": 1,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba83c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8394.md#insn-00ba83c0) · [`00ba83d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8394.md#insn-00ba83d4) · [`00ba83e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8394.md#insn-00ba83e8)
- 新版 `00ba8488`（命令位置の公開資料なし） · `00ba849c`（命令位置の公開資料なし） · `00ba84b0`（命令位置の公開資料なし）

~~~diff
- 00ba83c0 ["INT_ADD", "register:40f0:8", ["const:ba83c0:8", "const:4:8"]]
- 00ba83c0 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ba8488 ["INT_ADD", "register:40f0:8", ["const:ba8488:8", "const:4:8"]]
+ 00ba8488 ["CALL", null, ["callee:00bdaff0:8"]]
- 00ba83c0 bytes e0ca0094
+ 00ba8488 bytes daca0094
- 00ba83d4 ["INT_ADD", "register:40f0:8", ["const:ba83d4:8", "const:4:8"]]
- 00ba83d4 ["CALL", null, ["callee:00ba7a20:8"]]
+ 00ba849c ["INT_ADD", "register:40f0:8", ["const:ba849c:8", "const:4:8"]]
+ 00ba849c ["CALL", null, ["callee:00ba7a20:8"]]
- 00ba83d4 bytes 61fdff97
+ 00ba849c bytes 61fdff97
- 00ba83e8 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00ba83e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ba83e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ba83e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ba84b0 ["COPY", "tmp:0:8", ["const:960:8"]]
+ 00ba84b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ba84b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ba84b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ba83e8 bytes 08812291
+ 00ba84b0 bytes 08812591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb5187ff8bb8bf799a09a5aed790d092"></a>

### [`00ba842c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba842c.md) → [`00ba84f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba84f4.md) _ZNSt6__ndk16locale6globalERKS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.54% / 新版 70.54%

CFGの説明率　旧版 45.95% / 新版 48.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba84c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba84d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba84dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba8454",
      "READ",
      [
        "storage",
        "010a29f0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ba845c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8680"
      ]
    ],
    [
      "00ba852c",
      "PARAM",
      [
        "storage",
        "010a29e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba851c",
      "READ",
      [
        "storage",
        "010a2ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba8524",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8680"
      ]
    ],
    [
      "00ba852c",
      "PARAM",
      [
        "storage",
        "010a2aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba845c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba842c.md#insn-00ba845c) · [`00ba846c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba842c.md#insn-00ba846c) · [`00ba8480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba842c.md#insn-00ba8480)
- 新版 `00ba8534`（命令位置の公開資料なし） · `00ba8548`（命令位置の公開資料なし）

~~~diff
- 00ba845c ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00ba845c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ba845c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ba845c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00ba845c bytes e90a0036
- 00ba846c ["INT_ADD", "register:40f0:8", ["const:ba846c:8", "const:4:8"]]
- 00ba846c ["CALL", null, ["callee:00bdd930:8"]]
+ 00ba8534 ["INT_ADD", "register:40f0:8", ["const:ba8534:8", "const:4:8"]]
+ 00ba8534 ["CALL", null, ["callee:00bdd930:8"]]
- 00ba846c bytes 05d50094
+ 00ba8534 bytes ffd40094
- 00ba8480 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00ba8548 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00ba8480 bytes 80000054
+ 00ba8548 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e646e5ed5ac16fb36675714b4391e255"></a>

### [`00ba872c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba872c.md) → [`00ba87f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba87f4.md) _ZNKSt6__ndk16locale9use_facetERNS0_2idE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) · 呼出先 3件 [`00b88fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88fdc.md) [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 1件 [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) · 呼出先 3件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba882c",
      "incomplete_value": false,
      "site": "00ba8840",
      "value": [
        "leaf",
        "const:bb9104:8"
      ]
    },
    "old": {
      "definition_site": "00ba8764",
      "incomplete_value": false,
      "site": "00ba8778",
      "value": [
        "leaf",
        "const:bb903c:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba87ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00ba8874"
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
      "00ba882c",
      "PARAM",
      [
        "storage",
        "00bb903c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba882c",
      "PARAM",
      [
        "storage",
        "00bb9104",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba872c.md#insn-00ba8778) · [`00ba87ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba872c.md#insn-00ba87ac)
- 新版 `00ba8840`（命令位置の公開資料なし） · `00ba8874`（命令位置の公開資料なし）

~~~diff
- 00ba8778 ["INT_ADD", "register:40f0:8", ["const:ba8778:8", "const:4:8"]]
- 00ba8778 ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba8840 ["INT_ADD", "register:40f0:8", ["const:ba8840:8", "const:4:8"]]
+ 00ba8840 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba8778 bytes 9ae10094
+ 00ba8840 bytes 94e10094
- 00ba87ac ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ba87ac ["RETURN", null, ["register:0:8"]]
- 00ba87ac bytes c0035fd6
+ 00ba8874 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00ba8874 ["RETURN", null, ["register:0:8"]]
+ 00ba8874 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7b4730b000266f80c7a3c82d422d38e"></a>

### [`00ba87b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba87b4.md) → [`00ba887c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba887c.md) _ZNKSt6__ndk16localeeqERKS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 85.71% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba87c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba87b4.md#insn-00ba87c4) · [`00ba8838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba87b4.md#insn-00ba8838) · [`00ba8840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba87b4.md#insn-00ba8840)
- 新版 `00ba888c`（命令位置の公開資料なし） · `00ba8900`（命令位置の公開資料なし） · `00ba8908`（命令位置の公開資料なし）

~~~diff
- 00ba87c4 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
+ 00ba888c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00ba87c4 bytes 80040054
+ 00ba888c bytes 80040054
- 00ba8838 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 00ba8838 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ba8838 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ba8838 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00ba8900 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
+ 00ba8900 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00ba8900 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00ba8900 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00ba8838 bytes 2a010037
+ 00ba8900 bytes 2a010037
- 00ba8840 ["CBRANCH", null, ["local:b11:8", "register:102:1"]]
+ 00ba8908 ["CBRANCH", null, ["local:b12:8", "register:102:1"]]
- 00ba8840 bytes c2010054
+ 00ba8908 bytes c2010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7208040932646e35a477cc5707f1c515"></a>

### [`00ba88e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba88e0.md) → [`00ba89a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba89a8.md) _ZNSt6__ndk114collate_bynameIcEC1EPKcm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.20% / 新版 90.20%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba890c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba890c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba89d4"
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
      "unmatched:00ba8900",
      "READ",
      [
        "storage",
        "00c1be88",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba890c",
      "DATA",
      [
        "storage",
        "00c13840",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "unmatched:00ba8948",
      "PARAM",
      [
        "storage",
        "0029a994",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ba89c8",
      "READ",
      [
        "storage",
        "00c1bf38",
        null,
        "pointer"
      ]
    ],
    [
      "00ba89d4",
      "DATA",
      [
        "storage",
        "00c138f0",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00ba8a10",
      "PARAM",
      [
        "storage",
        "0029aa21",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba890c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba88e0.md#insn-00ba890c) · [`00ba8918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba88e0.md#insn-00ba8918) · [`00ba8958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba88e0.md#insn-00ba8958)
- 新版 `00ba89e0`（命令位置の公開資料なし） · `00ba8a20`（命令位置の公開資料なし）

~~~diff
- 00ba890c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba890c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ba890c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00ba890c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba890c bytes 082400a9
- 00ba8918 ["INT_ADD", "register:40f0:8", ["const:ba8918:8", "const:4:8"]]
- 00ba8918 ["CALL", null, ["callee:00be1520:8"]]
+ 00ba89e0 ["INT_ADD", "register:40f0:8", ["const:ba89e0:8", "const:4:8"]]
+ 00ba89e0 ["CALL", null, ["callee:00be1520:8"]]
- 00ba8918 bytes d6e20094
+ 00ba89e0 bytes d0e20094
- 00ba8958 ["INT_ADD", "register:40f0:8", ["const:ba8958:8", "const:4:8"]]
- 00ba8958 ["CALL", null, ["callee:00ba8a80:8"]]
+ 00ba8a20 ["INT_ADD", "register:40f0:8", ["const:ba8a20:8", "const:4:8"]]
+ 00ba8a20 ["CALL", null, ["callee:00ba8a80:8"]]
- 00ba8958 bytes 18000094
+ 00ba8a20 bytes 18000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bad80f42a11fdcbed7a9a93bed291b9d"></a>

### [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md) → [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) FUN_00ba8a80

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 13件 [`00ba88e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba88e0.md) [`00ba8f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8f24.md) [`00baa21c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa21c.md) [`00baa794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa794.md) [`00bab330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab330.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdc080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc080.md)
- 新版 呼出元 13件 [`00ba89a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba89a8.md) [`00ba8fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8fec.md) [`00baa2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa2e4.md) [`00baa85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa85c.md) [`00bab3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab3f8.md) · 呼出先 2件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ba89e0",
      "incomplete_value": true,
      "site": "00ba89ec",
      "value": [
        "live",
        "register:4098:8"
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
      "definition_site": "00ba89dc",
      "incomplete_value": true,
      "site": "00ba89ec",
      "value": [
        "live",
        "register:4000:8"
      ]
    },
    "ordinal": 1,
    "slot": 4
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba89ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md#insn-00ba89ec) · [`00ba89d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md#insn-00ba89d8)
- 新版 `00ba8ab4`（命令位置の公開資料なし） · `00ba8aa0`（命令位置の公開資料なし）

~~~diff
- 00ba89ec ["INT_ADD", "register:40f0:8", ["const:ba89ec:8", "const:4:8"]]
- 00ba89ec ["CALL", null, ["callee:00bdc130:8"]]
+ 00ba8ab4 ["INT_ADD", "register:40f0:8", ["const:ba8ab4:8", "const:4:8"]]
+ 00ba8ab4 ["CALL", null, ["callee:00bdc130:8"]]
- 00ba89ec bytes a5cd0094
+ 00ba8ab4 bytes 9fcd0094
- 00ba89d8 ["INT_ADD", "register:40f0:8", ["const:ba89d8:8", "const:4:8"]]
- 00ba89d8 ["CALL", null, ["callee:00bdb140:8"]]
+ 00ba8aa0 ["INT_ADD", "register:40f0:8", ["const:ba8aa0:8", "const:4:8"]]
+ 00ba8aa0 ["CALL", null, ["callee:00bdb140:8"]]
- 00ba89d8 bytes aec90094
+ 00ba8aa0 bytes a8c90094
~~~


<a id="compare-15c45527be7d86e9530a44e3a79f80b9"></a>

### [`00ba8a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8a1c.md) → [`00ba8ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8ae4.md) _ZNSt6__ndk114collate_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1730.md) · 呼出先 6件 [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md) [`00be0eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0eb0.md)
- 新版 呼出元 1件 [`00be17e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be17e0.md) · 呼出先 6件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba8b10",
      "incomplete_value": true,
      "site": "00ba8b10",
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
      "definition_site": "00ba8a48",
      "incomplete_value": true,
      "site": "00ba8a48",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ba8b70"
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
      "00ba8b04",
      "READ",
      [
        "storage",
        "00c1be88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba8b10",
      "DATA",
      [
        "storage",
        "00c13840",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "unmatched:00ba8a88",
      "PARAM",
      [
        "storage",
        "0029a994",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ba8b04",
      "READ",
      [
        "storage",
        "00c1bf38",
        null,
        "pointer"
      ]
    ],
    [
      "00ba8b10",
      "DATA",
      [
        "storage",
        "00c138f0",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00ba8b50",
      "PARAM",
      [
        "storage",
        "0029aa21",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8a1c.md#insn-00ba8a98) · [`00ba8aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8a1c.md#insn-00ba8aa8)
- 新版 `00ba8b60`（命令位置の公開資料なし） · `00ba8b70`（命令位置の公開資料なし）

~~~diff
- 00ba8a98 ["INT_ADD", "register:40f0:8", ["const:ba8a98:8", "const:4:8"]]
- 00ba8a98 ["CALL", null, ["callee:00bdb210:8"]]
+ 00ba8b60 ["INT_ADD", "register:40f0:8", ["const:ba8b60:8", "const:4:8"]]
+ 00ba8b60 ["CALL", null, ["callee:00bdb210:8"]]
- 00ba8a98 bytes b2c90094
+ 00ba8b60 bytes acc90094
- 00ba8aa8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ba8aa8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ba8aa8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00ba8aa8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:1:8"]]
- 00ba8aa8 bytes 2015949a
+ 00ba8b70 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00ba8b70 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00ba8b70 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00ba8b70 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:1:8"]]
+ 00ba8b70 bytes 2015949a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7f66a36c99ab156d6dbc1f9e10208b1"></a>

### [`00ba8ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8ae0.md) → [`00ba8ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8ba8.md) _ZNSt6__ndk114collate_bynameIcED1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1840.md) · 呼出先 2件 [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md) [`00be1830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1830.md)
- 新版 呼出元 1件 [`00be18f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18f0.md) · 呼出先 2件 [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8b04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba8bcc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ba8afc",
      "incomplete_value": true,
      "site": "00ba8b08",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:10:8"
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
      "unmatched:00ba8af8",
      "READ",
      [
        "storage",
        "00c1be88",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba8b04",
      "DATA",
      [
        "storage",
        "00c13840",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00ba8bc0",
      "READ",
      [
        "storage",
        "00c1bf38",
        null,
        "pointer"
      ]
    ],
    [
      "00ba8bcc",
      "DATA",
      [
        "storage",
        "00c138f0",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8b04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8ae0.md#insn-00ba8b04) · [`00ba8b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8ae0.md#insn-00ba8b08)
- 新版 `00ba8bd0`（命令位置の公開資料なし） · `00ba8bcc`（命令位置の公開資料なし）

~~~diff
- 00ba8b04 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ba8b04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ba8b04 bytes 680200f9
- 00ba8b08 ["INT_ADD", "register:40f0:8", ["const:ba8b08:8", "const:4:8"]]
- 00ba8b08 ["CALL", null, ["callee:00be18e0:8"]]
+ 00ba8bd0 ["INT_ADD", "register:40f0:8", ["const:ba8bd0:8", "const:4:8"]]
+ 00ba8bd0 ["CALL", null, ["callee:00be18e0:8"]]
- 00ba8b08 bytes 4ae30094
+ 00ba8bd0 bytes 44e30094
+ 00ba8bcc ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 00ba8bcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00ba8bcc bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b72f044c14de65db8f8b975adcd71258"></a>

### [`00ba8b24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8b24.md) → [`00ba8bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8bec.md) _ZNSt6__ndk114collate_bynameIcED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1840.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be18f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18f0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba8b38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8b24.md#insn-00ba8b38)
- 新版 `00ba8c00`（命令位置の公開資料なし）

~~~diff
- 00ba8b38 ["INT_ADD", "register:40f0:8", ["const:ba8b38:8", "const:4:8"]]
- 00ba8b38 ["CALL", null, ["callee:00be18f0:8"]]
+ 00ba8c00 ["INT_ADD", "register:40f0:8", ["const:ba8c00:8", "const:4:8"]]
+ 00ba8c00 ["CALL", null, ["callee:00be18f0:8"]]
- 00ba8b38 bytes 42e30094
+ 00ba8c00 bytes 3ce30094
~~~


<a id="compare-06d69793e9658c1e7013fa8d07604456"></a>

### [`00ba8b50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8b50.md) → [`00ba8c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8c18.md) _ZNKSt6__ndk114collate_bynameIcE10do_compareEPKcS3_S3_S3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00be1850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1850.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00be1900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1900.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.98% / 新版 81.98%

CFGの説明率　旧版 5.26% / 新版 3.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8b60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8b60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8b64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba8b60",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba8b64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba8b68",
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
      "00ba8c28",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ba8c2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ba8c30",
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

- 旧版 [`00ba8b60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8b50.md#insn-00ba8b60) · [`00ba8b64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8b50.md#insn-00ba8b64) · [`00ba8b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8b50.md#insn-00ba8b68)

~~~diff
- 00ba8b60 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ba8b60 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ba8b60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00ba8b60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba8b60 bytes f85f05a9
- 00ba8b64 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ba8b64 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ba8b64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00ba8b64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba8b64 bytes f65706a9
- 00ba8b68 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ba8b68 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ba8b68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00ba8b68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba8b68 bytes f44f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0793a0f198e71e520de56aef35d2a4f0"></a>

### [`00ba8f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8f24.md) → [`00ba8fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8fec.md) _ZNSt6__ndk114collate_bynameIwEC1EPKcm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba9018",
      "incomplete_value": true,
      "site": "00ba9018",
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
      "definition_site": "00ba8f50",
      "incomplete_value": true,
      "site": "00ba8f50",
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
      "00ba900c",
      "READ",
      [
        "storage",
        "00c1be90",
        null,
        "pointer"
      ]
    ],
    [
      "00ba9018",
      "DATA",
      [
        "storage",
        "00c13880",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00ba900c",
      "READ",
      [
        "storage",
        "00c1bf40",
        null,
        "pointer"
      ]
    ],
    [
      "00ba9018",
      "DATA",
      [
        "storage",
        "00c13930",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8f44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8f24.md#insn-00ba8f44) · [`00ba8f5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8f24.md#insn-00ba8f5c) · [`00ba8f84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8f24.md#insn-00ba8f84)
- 新版 `00ba900c`（命令位置の公開資料なし） · `00ba9024`（命令位置の公開資料なし） · `00ba904c`（命令位置の公開資料なし）

~~~diff
- 00ba8f44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
- 00ba8f44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba900c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 00ba900c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba8f44 bytes 084947f9
+ 00ba900c bytes 08a147f9
- 00ba8f5c ["INT_ADD", "register:40f0:8", ["const:ba8f5c:8", "const:4:8"]]
- 00ba8f5c ["CALL", null, ["callee:00be1520:8"]]
+ 00ba9024 ["INT_ADD", "register:40f0:8", ["const:ba9024:8", "const:4:8"]]
+ 00ba9024 ["CALL", null, ["callee:00be1520:8"]]
- 00ba8f5c bytes 45e10094
+ 00ba9024 bytes 3fe10094
- 00ba8f84 ["INT_ADD", "register:40f0:8", ["const:ba8f84:8", "const:4:8"]]
- 00ba8f84 ["CALL", null, ["callee:0041b298:8"]]
+ 00ba904c ["INT_ADD", "register:40f0:8", ["const:ba904c:8", "const:4:8"]]
+ 00ba904c ["CALL", null, ["callee:0041b298:8"]]
- 00ba8f84 bytes c5c8e197
+ 00ba904c bytes 93c8e197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33e9d6b83cecb020b7a3b9c605a3ad40"></a>

### [`00ba8ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8ffc.md) → [`00ba90c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba90c4.md) _ZNSt6__ndk114collate_bynameIwEC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1740.md) · 呼出先 6件 [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md) [`00be0eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0eb0.md)
- 新版 呼出元 1件 [`00be17f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be17f0.md) · 呼出先 6件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)

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
      "definition_site": "00ba90f0",
      "incomplete_value": true,
      "site": "00ba90f0",
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
      "definition_site": "00ba9028",
      "incomplete_value": true,
      "site": "00ba9028",
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
      "00ba90e4",
      "READ",
      [
        "storage",
        "00c1be90",
        null,
        "pointer"
      ]
    ],
    [
      "00ba90f0",
      "DATA",
      [
        "storage",
        "00c13880",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00ba90e4",
      "READ",
      [
        "storage",
        "00c1bf40",
        null,
        "pointer"
      ]
    ],
    [
      "00ba90f0",
      "DATA",
      [
        "storage",
        "00c13930",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba901c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8ffc.md#insn-00ba901c) · [`00ba9044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8ffc.md#insn-00ba9044) · [`00ba9078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8ffc.md#insn-00ba9078)
- 新版 `00ba90e4`（命令位置の公開資料なし） · `00ba910c`（命令位置の公開資料なし） · `00ba9140`（命令位置の公開資料なし）

~~~diff
- 00ba901c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
- 00ba901c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba90e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 00ba90e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba901c bytes 084947f9
+ 00ba90e4 bytes 08a147f9
- 00ba9044 ["INT_ADD", "register:40f0:8", ["const:ba9044:8", "const:4:8"]]
- 00ba9044 ["CALL", null, ["callee:00be1520:8"]]
+ 00ba910c ["INT_ADD", "register:40f0:8", ["const:ba910c:8", "const:4:8"]]
+ 00ba910c ["CALL", null, ["callee:00be1520:8"]]
- 00ba9044 bytes 0be10094
+ 00ba910c bytes 05e10094
- 00ba9078 ["INT_ADD", "register:40f0:8", ["const:ba9078:8", "const:4:8"]]
- 00ba9078 ["CALL", null, ["callee:00bdb210:8"]]
+ 00ba9140 ["INT_ADD", "register:40f0:8", ["const:ba9140:8", "const:4:8"]]
+ 00ba9140 ["CALL", null, ["callee:00bdb210:8"]]
- 00ba9078 bytes 3ac80094
+ 00ba9140 bytes 34c80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab941aa074c38dae42236146ef19ab0a"></a>

### [`00ba90c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba90c0.md) → [`00ba9188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9188.md) _ZNSt6__ndk114collate_bynameIwED1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1870.md) · 呼出先 2件 [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md) [`00be1830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1830.md)
- 新版 呼出元 1件 [`00be1920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1920.md) · 呼出先 2件 [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba91a8",
      "incomplete_value": true,
      "site": "00ba91ac",
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
      "definition_site": "00ba90e0",
      "incomplete_value": true,
      "site": "00ba90e4",
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
      "00ba91a0",
      "READ",
      [
        "storage",
        "00c1be90",
        null,
        "pointer"
      ]
    ],
    [
      "00ba91ac",
      "DATA",
      [
        "storage",
        "00c13880",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00ba91a0",
      "READ",
      [
        "storage",
        "00c1bf40",
        null,
        "pointer"
      ]
    ],
    [
      "00ba91ac",
      "DATA",
      [
        "storage",
        "00c13930",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba90d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba90c0.md#insn-00ba90d8) · [`00ba90e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba90c0.md#insn-00ba90e8)
- 新版 `00ba91a0`（命令位置の公開資料なし） · `00ba91b0`（命令位置の公開資料なし）

~~~diff
- 00ba90d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
- 00ba90d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba91a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 00ba91a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba90d8 bytes 084947f9
+ 00ba91a0 bytes 08a147f9
- 00ba90e8 ["INT_ADD", "register:40f0:8", ["const:ba90e8:8", "const:4:8"]]
- 00ba90e8 ["CALL", null, ["callee:00be18e0:8"]]
+ 00ba91b0 ["INT_ADD", "register:40f0:8", ["const:ba91b0:8", "const:4:8"]]
+ 00ba91b0 ["CALL", null, ["callee:00be18e0:8"]]
- 00ba90e8 bytes d2e10094
+ 00ba91b0 bytes cce10094
~~~


<a id="compare-618446efcc942a338b779344aaee93b1"></a>

### [`00ba9130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9130.md) → [`00ba91f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba91f8.md) _ZNKSt6__ndk114collate_bynameIwE10do_compareEPKwS3_S3_S3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 93.33% / 新版 90.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba9168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9130.md#insn-00ba9168) · [`00ba91c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9130.md#insn-00ba91c4) · [`00ba91f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9130.md#insn-00ba91f8)
- 新版 `00ba9230`（命令位置の公開資料なし） · `00ba928c`（命令位置の公開資料なし） · `00ba92c0`（命令位置の公開資料なし）

~~~diff
- 00ba9168 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ba9168 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00ba9168 ["CBRANCH", null, ["local:b17:8", "tmp:1:1"]]
+ 00ba9230 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00ba9230 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00ba9230 ["CBRANCH", null, ["local:b18:8", "tmp:1:1"]]
- 00ba9168 bytes a80d0054
+ 00ba9230 bytes a80d0054
- 00ba91c4 ["INT_ADD", "register:40f0:8", ["const:ba91c4:8", "const:4:8"]]
- 00ba91c4 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ba928c ["INT_ADD", "register:40f0:8", ["const:ba928c:8", "const:4:8"]]
+ 00ba928c ["CALL", null, ["callee:00bdaff0:8"]]
- 00ba91c4 bytes 5fc70094
+ 00ba928c bytes 59c70094
- 00ba91f8 ["INT_ADD", "register:40f0:8", ["const:ba91f8:8", "const:4:8"]]
- 00ba91f8 ["CALL", null, ["callee:00bdb160:8"]]
+ 00ba92c0 ["INT_ADD", "register:40f0:8", ["const:ba92c0:8", "const:4:8"]]
+ 00ba92c0 ["CALL", null, ["callee:00bdb160:8"]]
- 00ba91f8 bytes aec70094
+ 00ba92c0 bytes a8c70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95a499982a4d91ab4a6ca3b57fecbdf1"></a>

### [`00ba9348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9348.md) → [`00ba9410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9410.md) _ZNKSt6__ndk114collate_bynameIwE12do_transformEPKwS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 95.90% / 新版 95.90%

CFGの説明率　旧版 39.29% / 新版 39.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 4件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9390"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba942c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ba9458"
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
      "unmatched:00ba9390",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba947c"
      ]
    ]
  ],
  "added": [
    [
      "00ba9458",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba947c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9348.md#insn-00ba9390) · [`00ba942c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9348.md#insn-00ba942c)
- 新版 `00ba9458`（命令位置の公開資料なし）

~~~diff
- 00ba9390 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ba9390 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00ba9390 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00ba9390 bytes 28010054
- 00ba942c ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00ba942c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00ba942c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ba942c ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00ba942c bytes e102899a
+ 00ba9458 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00ba9458 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00ba9458 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 00ba9458 bytes 28010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82ccdf1fa5274a786574ce9d129ededd"></a>

### [`00ba96c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba96c0.md) → [`00ba9788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9788.md) _ZNKSt6__ndk15ctypeIwE10do_toupperEw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md) [`00be18b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be18b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1960.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 78.38% / 新版 78.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba9808",
      "incomplete_value": true,
      "site": "00ba9808",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9740",
      "incomplete_value": true,
      "site": "00ba9740",
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
            "const:890:8"
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
      "definition_site": "00ba97b8",
      "incomplete_value": true,
      "site": "00ba97c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba96f0",
      "incomplete_value": true,
      "site": "00ba96f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:890:8"
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
      "definition_site": "00ba97e8",
      "incomplete_value": false,
      "site": "00ba97ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9720",
      "incomplete_value": false,
      "site": "00ba9724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00ba97b0",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba97b8",
      "READ",
      [
        "storage",
        "010a2890",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba97e8",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ba97b0",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba97b8",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba97e8",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba96f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba96c0.md#insn-00ba96f8) · [`00ba9724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba96c0.md#insn-00ba9724) · [`00ba973c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba96c0.md#insn-00ba973c)
- 新版 `00ba97c0`（命令位置の公開資料なし） · `00ba97ec`（命令位置の公開資料なし） · `00ba9804`（命令位置の公開資料なし）

~~~diff
- 00ba96f8 ["INT_ADD", "register:40f0:8", ["const:ba96f8:8", "const:4:8"]]
- 00ba96f8 ["CALL", null, ["callee:00be1960:8"]]
+ 00ba97c0 ["INT_ADD", "register:40f0:8", ["const:ba97c0:8", "const:4:8"]]
+ 00ba97c0 ["CALL", null, ["callee:00be1960:8"]]
- 00ba96f8 bytes 6ee00094
+ 00ba97c0 bytes 68e00094
- 00ba9724 ["INT_ADD", "register:40f0:8", ["const:ba9724:8", "const:4:8"]]
- 00ba9724 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00ba97ec ["INT_ADD", "register:40f0:8", ["const:ba97ec:8", "const:4:8"]]
+ 00ba97ec ["CALL", null, ["callee:00bdafb0:8"]]
- 00ba9724 bytes f7c50094
+ 00ba97ec bytes f1c50094
- 00ba973c ["INT_ADD", "register:40f0:8", ["const:ba973c:8", "const:4:8"]]
- 00ba973c ["CALL", null, ["callee:00be1520:8"]]
+ 00ba9804 ["INT_ADD", "register:40f0:8", ["const:ba9804:8", "const:4:8"]]
+ 00ba9804 ["CALL", null, ["callee:00be1520:8"]]
- 00ba973c bytes 4ddf0094
+ 00ba9804 bytes 47df0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58333e35429d5f3e726a8c838e6d7c5b"></a>

### [`00ba976c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba976c.md) → [`00ba9834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9834.md) _ZNKSt6__ndk15ctypeIwE10do_toupperEPwPKw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba98c0",
      "incomplete_value": true,
      "site": "00ba98c0",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba97f8",
      "incomplete_value": true,
      "site": "00ba97f8",
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
            "const:890:8"
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
      "00ba9898",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba98a0",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba98ac",
      "PARAM",
      [
        "storage",
        "002a568a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba9898",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba98a0",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba98ac",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba97f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba976c.md#insn-00ba97f8) · [`00ba9798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba976c.md#insn-00ba9798) · [`00ba97dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba976c.md#insn-00ba97dc)
- 新版 `00ba98c0`（命令位置の公開資料なし） · `00ba9860`（命令位置の公開資料なし） · `00ba98a4`（命令位置の公開資料なし）

~~~diff
- 00ba97f8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:890:8"]]
- 00ba97f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ba98c0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:950:8"]]
+ 00ba98c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ba97f8 bytes c04a04f9
+ 00ba98c0 bytes c0aa04f9
- 00ba9798 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00ba9798 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba9798 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba9798 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00ba9860 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00ba9860 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00ba9860 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00ba9860 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00ba9798 bytes b5622291
+ 00ba9860 bytes b5622591
- 00ba97dc ["INT_ADD", "register:40f0:8", ["const:ba97dc:8", "const:4:8"]]
- 00ba97dc ["CALL", null, ["callee:00bdafb0:8"]]
+ 00ba98a4 ["INT_ADD", "register:40f0:8", ["const:ba98a4:8", "const:4:8"]]
+ 00ba98a4 ["CALL", null, ["callee:00bdafb0:8"]]
- 00ba97dc bytes c9c50094
+ 00ba98a4 bytes c3c50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7efe6d9598de0ff14340e3fba9967d29"></a>

### [`00ba9840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9840.md) → [`00ba9908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9908.md) _ZNKSt6__ndk15ctypeIwE10do_tolowerEw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba9980",
      "incomplete_value": false,
      "site": "00ba9980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba98b8",
      "incomplete_value": false,
      "site": "00ba98b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:890:8"
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
      "definition_site": "00ba995c",
      "incomplete_value": false,
      "site": "00ba9960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9894",
      "incomplete_value": false,
      "site": "00ba9898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00ba996c",
      "incomplete_value": false,
      "site": "00ba9978",
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
            "const:683:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba98a4",
      "incomplete_value": false,
      "site": "00ba98b0",
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
            "const:68a:8"
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
      "00ba992c",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba995c",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba996c",
      "PARAM",
      [
        "storage",
        "002a568a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba992c",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba995c",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba996c",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9840.md#insn-00ba9898) · [`00ba98b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9840.md#insn-00ba98b0) · [`00ba98b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9840.md#insn-00ba98b8)
- 新版 `00ba9960`（命令位置の公開資料なし） · `00ba9978`（命令位置の公開資料なし） · `00ba9980`（命令位置の公開資料なし）

~~~diff
- 00ba9898 ["INT_ADD", "register:40f0:8", ["const:ba9898:8", "const:4:8"]]
- 00ba9898 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00ba9960 ["INT_ADD", "register:40f0:8", ["const:ba9960:8", "const:4:8"]]
+ 00ba9960 ["CALL", null, ["callee:00bdafb0:8"]]
- 00ba9898 bytes 9ac50094
+ 00ba9960 bytes 94c50094
- 00ba98b0 ["INT_ADD", "register:40f0:8", ["const:ba98b0:8", "const:4:8"]]
- 00ba98b0 ["CALL", null, ["callee:00be1520:8"]]
+ 00ba9978 ["INT_ADD", "register:40f0:8", ["const:ba9978:8", "const:4:8"]]
+ 00ba9978 ["CALL", null, ["callee:00be1520:8"]]
- 00ba98b0 bytes f0de0094
+ 00ba9978 bytes eade0094
- 00ba98b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:890:8"]]
- 00ba98b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ba9980 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
+ 00ba9980 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ba98b8 bytes 004904f9
+ 00ba9980 bytes 00a904f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4402247d5eb0f65f0175db1f1e05c178"></a>

### [`00ba98e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba98e4.md) → [`00ba99ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba99ac.md) _ZNKSt6__ndk15ctypeIwE10do_tolowerEPwPKw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba9a38",
      "incomplete_value": true,
      "site": "00ba9a38",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9970",
      "incomplete_value": true,
      "site": "00ba9970",
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
            "const:890:8"
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
      "00ba9a10",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9a18",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9a24",
      "PARAM",
      [
        "storage",
        "002a568a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba9a10",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9a18",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9a24",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba98e4.md#insn-00ba9970) · [`00ba9910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba98e4.md#insn-00ba9910) · [`00ba9954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba98e4.md#insn-00ba9954)
- 新版 `00ba9a38`（命令位置の公開資料なし） · `00ba99d8`（命令位置の公開資料なし） · `00ba9a1c`（命令位置の公開資料なし）

~~~diff
- 00ba9970 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:890:8"]]
- 00ba9970 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ba9a38 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:950:8"]]
+ 00ba9a38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ba9970 bytes c04a04f9
+ 00ba9a38 bytes c0aa04f9
- 00ba9910 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00ba9910 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba9910 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba9910 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00ba99d8 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00ba99d8 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00ba99d8 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00ba99d8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00ba9910 bytes b5622291
+ 00ba99d8 bytes b5622591
- 00ba9954 ["INT_ADD", "register:40f0:8", ["const:ba9954:8", "const:4:8"]]
- 00ba9954 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00ba9a1c ["INT_ADD", "register:40f0:8", ["const:ba9a1c:8", "const:4:8"]]
+ 00ba9a1c ["CALL", null, ["callee:00bdafb0:8"]]
- 00ba9954 bytes 6bc50094
+ 00ba9a1c bytes 65c50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5154f9479ac3c1e64af04423408d42f"></a>

### [`00ba9c8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9c8c.md) → [`00ba9d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9d54.md) _ZNSt6__ndk15ctypeIcEC1EPKmbm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be16f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be16f0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be17a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be17a0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba9d6c",
      "incomplete_value": true,
      "site": "00ba9d70",
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
      "definition_site": "00ba9ca4",
      "incomplete_value": true,
      "site": "00ba9ca8",
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
      "00ba9d60",
      "READ",
      [
        "storage",
        "00c1be98",
        null,
        "pointer"
      ]
    ],
    [
      "00ba9d70",
      "DATA",
      [
        "storage",
        "00c138c0",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00ba9d60",
      "READ",
      [
        "storage",
        "00c1bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00ba9d70",
      "DATA",
      [
        "storage",
        "00c13970",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9c8c.md#insn-00ba9c98)
- 新版 `00ba9d60`（命令位置の公開資料なし）

~~~diff
- 00ba9c98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e98:8"]]
- 00ba9c98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba9d60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 00ba9d60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba9c98 bytes 084d47f9
+ 00ba9d60 bytes 08a547f9
~~~


<a id="compare-63be874143758d113e6d1ddded9ced9e"></a>

### [`00ba9d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9d44.md) → [`00ba9e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9e0c.md) _ZNKSt6__ndk15ctypeIcE10do_toupperEc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba9e84",
      "incomplete_value": false,
      "site": "00ba9e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9dbc",
      "incomplete_value": false,
      "site": "00ba9dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:890:8"
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
      "definition_site": "00ba9e60",
      "incomplete_value": false,
      "site": "00ba9e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9d98",
      "incomplete_value": false,
      "site": "00ba9d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00ba9e70",
      "incomplete_value": false,
      "site": "00ba9e7c",
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
            "const:683:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9da8",
      "incomplete_value": false,
      "site": "00ba9db4",
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
            "const:68a:8"
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
      "00ba9e2c",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9e60",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9e70",
      "PARAM",
      [
        "storage",
        "002a568a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba9e2c",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9e60",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9e70",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9d9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9d44.md#insn-00ba9d9c) · [`00ba9db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9d44.md#insn-00ba9db4) · [`00ba9dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9d44.md#insn-00ba9dbc)
- 新版 `00ba9e64`（命令位置の公開資料なし） · `00ba9e7c`（命令位置の公開資料なし） · `00ba9e84`（命令位置の公開資料なし）

~~~diff
- 00ba9d9c ["INT_ADD", "register:40f0:8", ["const:ba9d9c:8", "const:4:8"]]
- 00ba9d9c ["CALL", null, ["callee:00bdafb0:8"]]
+ 00ba9e64 ["INT_ADD", "register:40f0:8", ["const:ba9e64:8", "const:4:8"]]
+ 00ba9e64 ["CALL", null, ["callee:00bdafb0:8"]]
- 00ba9d9c bytes 59c40094
+ 00ba9e64 bytes 53c40094
- 00ba9db4 ["INT_ADD", "register:40f0:8", ["const:ba9db4:8", "const:4:8"]]
- 00ba9db4 ["CALL", null, ["callee:00be1520:8"]]
+ 00ba9e7c ["INT_ADD", "register:40f0:8", ["const:ba9e7c:8", "const:4:8"]]
+ 00ba9e7c ["CALL", null, ["callee:00be1520:8"]]
- 00ba9db4 bytes afdd0094
+ 00ba9e7c bytes a9dd0094
- 00ba9dbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:890:8"]]
- 00ba9dbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ba9e84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
+ 00ba9e84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ba9dbc bytes 004904f9
+ 00ba9e84 bytes 00a904f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d38094731801881d71de2911e034b96f"></a>

### [`00ba9de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9de8.md) → [`00ba9eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9eb0.md) _ZNKSt6__ndk15ctypeIcE10do_toupperEPcPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba9f3c",
      "incomplete_value": true,
      "site": "00ba9f3c",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9e74",
      "incomplete_value": true,
      "site": "00ba9e74",
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
            "const:890:8"
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
      "00ba9f14",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9f1c",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9f28",
      "PARAM",
      [
        "storage",
        "002a568a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba9f14",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9f1c",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9f28",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9e74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9de8.md#insn-00ba9e74) · [`00ba9e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9de8.md#insn-00ba9e14) · [`00ba9e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9de8.md#insn-00ba9e58)
- 新版 `00ba9f3c`（命令位置の公開資料なし） · `00ba9edc`（命令位置の公開資料なし） · `00ba9f20`（命令位置の公開資料なし）

~~~diff
- 00ba9e74 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:890:8"]]
- 00ba9e74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ba9f3c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:950:8"]]
+ 00ba9f3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ba9e74 bytes c04a04f9
+ 00ba9f3c bytes c0aa04f9
- 00ba9e14 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00ba9e14 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba9e14 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba9e14 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00ba9edc ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00ba9edc ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00ba9edc ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00ba9edc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00ba9e14 bytes b5622291
+ 00ba9edc bytes b5622591
- 00ba9e58 ["INT_ADD", "register:40f0:8", ["const:ba9e58:8", "const:4:8"]]
- 00ba9e58 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00ba9f20 ["INT_ADD", "register:40f0:8", ["const:ba9f20:8", "const:4:8"]]
+ 00ba9f20 ["CALL", null, ["callee:00bdafb0:8"]]
- 00ba9e58 bytes 2ac40094
+ 00ba9f20 bytes 24c40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02af8874af1519fa6303da0890f9bab6"></a>

### [`00ba9ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9ebc.md) → [`00ba9f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9f84.md) _ZNKSt6__ndk15ctypeIcE10do_tolowerEc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba9ffc",
      "incomplete_value": false,
      "site": "00ba9ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9f34",
      "incomplete_value": false,
      "site": "00ba9f34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:890:8"
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
      "definition_site": "00ba9fd8",
      "incomplete_value": false,
      "site": "00ba9fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9f10",
      "incomplete_value": false,
      "site": "00ba9f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00ba9fe8",
      "incomplete_value": false,
      "site": "00ba9ff4",
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
            "const:683:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9f20",
      "incomplete_value": false,
      "site": "00ba9f2c",
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
            "const:68a:8"
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
      "00ba9fa4",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9fd8",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9fe8",
      "PARAM",
      [
        "storage",
        "002a568a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba9fa4",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9fd8",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9fe8",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9ebc.md#insn-00ba9f14) · [`00ba9f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9ebc.md#insn-00ba9f2c) · [`00ba9f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9ebc.md#insn-00ba9f34)
- 新版 `00ba9fdc`（命令位置の公開資料なし） · `00ba9ff4`（命令位置の公開資料なし） · `00ba9ffc`（命令位置の公開資料なし）

~~~diff
- 00ba9f14 ["INT_ADD", "register:40f0:8", ["const:ba9f14:8", "const:4:8"]]
- 00ba9f14 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00ba9fdc ["INT_ADD", "register:40f0:8", ["const:ba9fdc:8", "const:4:8"]]
+ 00ba9fdc ["CALL", null, ["callee:00bdafb0:8"]]
- 00ba9f14 bytes fbc30094
+ 00ba9fdc bytes f5c30094
- 00ba9f2c ["INT_ADD", "register:40f0:8", ["const:ba9f2c:8", "const:4:8"]]
- 00ba9f2c ["CALL", null, ["callee:00be1520:8"]]
+ 00ba9ff4 ["INT_ADD", "register:40f0:8", ["const:ba9ff4:8", "const:4:8"]]
+ 00ba9ff4 ["CALL", null, ["callee:00be1520:8"]]
- 00ba9f2c bytes 51dd0094
+ 00ba9ff4 bytes 4bdd0094
- 00ba9f34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:890:8"]]
- 00ba9f34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ba9ffc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
+ 00ba9ffc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ba9f34 bytes 004904f9
+ 00ba9ffc bytes 00a904f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7395693aff69b0028f0c13930c679be9"></a>

### [`00ba9f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9f60.md) → [`00baa028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa028.md) _ZNKSt6__ndk15ctypeIcE10do_tolowerEPcPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00baa0b4",
      "incomplete_value": true,
      "site": "00baa0b4",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9fec",
      "incomplete_value": true,
      "site": "00ba9fec",
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
            "const:890:8"
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
      "00baa08c",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00baa094",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00baa0a0",
      "PARAM",
      [
        "storage",
        "002a568a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00baa08c",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00baa094",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00baa0a0",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9f60.md#insn-00ba9fec) · [`00ba9f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9f60.md#insn-00ba9f8c) · [`00ba9fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9f60.md#insn-00ba9fd0)
- 新版 `00baa0b4`（命令位置の公開資料なし） · `00baa054`（命令位置の公開資料なし） · `00baa098`（命令位置の公開資料なし）

~~~diff
- 00ba9fec ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:890:8"]]
- 00ba9fec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00baa0b4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:950:8"]]
+ 00baa0b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ba9fec bytes c04a04f9
+ 00baa0b4 bytes c0aa04f9
- 00ba9f8c ["COPY", "tmp:0:8", ["const:898:8"]]
- 00ba9f8c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba9f8c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba9f8c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00baa054 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00baa054 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00baa054 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00baa054 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00ba9f8c bytes b5622291
+ 00baa054 bytes b5622591
- 00ba9fd0 ["INT_ADD", "register:40f0:8", ["const:ba9fd0:8", "const:4:8"]]
- 00ba9fd0 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00baa098 ["INT_ADD", "register:40f0:8", ["const:baa098:8", "const:4:8"]]
+ 00baa098 ["CALL", null, ["callee:00bdafb0:8"]]
- 00ba9fd0 bytes ccc30094
+ 00baa098 bytes c6c30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e983d87c20c32139682fabc2db67b29"></a>

### [`00baa21c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa21c.md) → [`00baa2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa2e4.md) _ZNSt6__ndk112ctype_bynameIcEC1EPKcm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be18e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be18e0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0eb0.md)
- 新版 呼出元 1件 [`00be1990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1990.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00baa318",
      "incomplete_value": true,
      "site": "00baa320",
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
      "definition_site": "00baa250",
      "incomplete_value": true,
      "site": "00baa258",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00baa35c",
      "incomplete_value": false,
      "site": "00baa36c",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baa294",
      "incomplete_value": false,
      "site": "00baa2a4",
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
            "const:ef:8"
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
      "00baa304",
      "READ",
      [
        "storage",
        "00c1bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00baa320",
      "DATA",
      [
        "storage",
        "00c13928",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00baa35c",
      "PARAM",
      [
        "storage",
        "002a40ef",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00baa304",
      "READ",
      [
        "storage",
        "00c1bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00baa320",
      "DATA",
      [
        "storage",
        "00c139d8",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00baa35c",
      "PARAM",
      [
        "storage",
        "002a40e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa2a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa21c.md#insn-00baa2a4) · [`00baa23c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa21c.md#insn-00baa23c) · [`00baa264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa21c.md#insn-00baa264)
- 新版 `00baa36c`（命令位置の公開資料なし） · `00baa304`（命令位置の公開資料なし） · `00baa32c`（命令位置の公開資料なし）

~~~diff
- 00baa2a4 ["INT_ADD", "register:40f0:8", ["const:baa2a4:8", "const:4:8"]]
- 00baa2a4 ["CALL", null, ["callee:00ba8a80:8"]]
+ 00baa36c ["INT_ADD", "register:40f0:8", ["const:baa36c:8", "const:4:8"]]
+ 00baa36c ["CALL", null, ["callee:00ba8a80:8"]]
- 00baa2a4 bytes c5f9ff97
+ 00baa36c bytes c5f9ff97
- 00baa23c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ea0:8"]]
- 00baa23c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baa304 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f50:8"]]
+ 00baa304 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00baa23c bytes 295147f9
+ 00baa304 bytes 29a947f9
- 00baa264 ["INT_ADD", "register:40f0:8", ["const:baa264:8", "const:4:8"]]
- 00baa264 ["CALL", null, ["callee:00be1520:8"]]
+ 00baa32c ["INT_ADD", "register:40f0:8", ["const:baa32c:8", "const:4:8"]]
+ 00baa32c ["CALL", null, ["callee:00be1520:8"]]
- 00baa264 bytes 83dc0094
+ 00baa32c bytes 7ddc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-200e9e7226b9a28f79fcc96c81e9daec"></a>

### [`00baa304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa304.md) → [`00baa3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa3cc.md) _ZNSt6__ndk112ctype_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00be1750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1750.md) [`00be18f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be18f0.md) · 呼出先 6件 [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00be0eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0eb0.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md)
- 新版 呼出元 2件 [`00be1800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1800.md) [`00be19a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19a0.md) · 呼出先 6件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00baa408",
      "incomplete_value": true,
      "site": "00baa408",
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
      "definition_site": "00baa340",
      "incomplete_value": true,
      "site": "00baa340",
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
      "definition_site": "00baa448",
      "incomplete_value": false,
      "site": "00baa458",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baa380",
      "incomplete_value": false,
      "site": "00baa390",
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
            "const:ef:8"
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
      "00baa3f8",
      "READ",
      [
        "storage",
        "00c1bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00baa408",
      "DATA",
      [
        "storage",
        "00c13928",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00baa448",
      "PARAM",
      [
        "storage",
        "002a40ef",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00baa3f8",
      "READ",
      [
        "storage",
        "00c1bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00baa408",
      "DATA",
      [
        "storage",
        "00c139d8",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00baa448",
      "PARAM",
      [
        "storage",
        "002a40e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa304.md#insn-00baa390) · [`00baa330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa304.md#insn-00baa330) · [`00baa35c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa304.md#insn-00baa35c)
- 新版 `00baa458`（命令位置の公開資料なし） · `00baa3f8`（命令位置の公開資料なし） · `00baa424`（命令位置の公開資料なし）

~~~diff
- 00baa390 ["INT_ADD", "register:40f0:8", ["const:baa390:8", "const:4:8"]]
- 00baa390 ["CALL", null, ["callee:00bdb210:8"]]
+ 00baa458 ["INT_ADD", "register:40f0:8", ["const:baa458:8", "const:4:8"]]
+ 00baa458 ["CALL", null, ["callee:00bdb210:8"]]
- 00baa390 bytes 74c30094
+ 00baa458 bytes 6ec30094
- 00baa330 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00baa330 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baa3f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 00baa3f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00baa330 bytes 085147f9
+ 00baa3f8 bytes 08a947f9
- 00baa35c ["INT_ADD", "register:40f0:8", ["const:baa35c:8", "const:4:8"]]
- 00baa35c ["CALL", null, ["callee:00be1520:8"]]
+ 00baa424 ["INT_ADD", "register:40f0:8", ["const:baa424:8", "const:4:8"]]
+ 00baa424 ["CALL", null, ["callee:00be1520:8"]]
- 00baa35c bytes 45dc0094
+ 00baa424 bytes 3fdc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67e254799b486a89e4acefe1f91c804d"></a>

### [`00baa794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa794.md) → [`00baa85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa85c.md) _ZNSt6__ndk112ctype_bynameIwEC2EPKcm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1910.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0eb0.md)
- 新版 呼出元 1件 [`00be19c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19c0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00baa888",
      "incomplete_value": true,
      "site": "00baa888",
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
      "definition_site": "00baa7c0",
      "incomplete_value": true,
      "site": "00baa7c0",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00baa8c4",
      "incomplete_value": false,
      "site": "00baa8d4",
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
            "const:5bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baa7fc",
      "incomplete_value": false,
      "site": "00baa80c",
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
            "const:650:8"
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
      "00baa87c",
      "READ",
      [
        "storage",
        "00c1bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00baa888",
      "DATA",
      [
        "storage",
        "00c13990",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00baa8c4",
      "PARAM",
      [
        "storage",
        "002ae650",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00baa87c",
      "READ",
      [
        "storage",
        "00c1bf58",
        null,
        "pointer"
      ]
    ],
    [
      "00baa888",
      "DATA",
      [
        "storage",
        "00c13a40",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00baa8c4",
      "PARAM",
      [
        "storage",
        "002ae5bc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa80c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa794.md#insn-00baa80c) · [`00baa7b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa794.md#insn-00baa7b4) · [`00baa7cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa794.md#insn-00baa7cc)
- 新版 `00baa8d4`（命令位置の公開資料なし） · `00baa87c`（命令位置の公開資料なし） · `00baa894`（命令位置の公開資料なし）

~~~diff
- 00baa80c ["INT_ADD", "register:40f0:8", ["const:baa80c:8", "const:4:8"]]
- 00baa80c ["CALL", null, ["callee:00ba8a80:8"]]
+ 00baa8d4 ["INT_ADD", "register:40f0:8", ["const:baa8d4:8", "const:4:8"]]
+ 00baa8d4 ["CALL", null, ["callee:00ba8a80:8"]]
- 00baa80c bytes 6bf8ff97
+ 00baa8d4 bytes 6bf8ff97
- 00baa7b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
- 00baa7b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baa87c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f58:8"]]
+ 00baa87c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00baa7b4 bytes 085547f9
+ 00baa87c bytes 08ad47f9
- 00baa7cc ["INT_ADD", "register:40f0:8", ["const:baa7cc:8", "const:4:8"]]
- 00baa7cc ["CALL", null, ["callee:00be1520:8"]]
+ 00baa894 ["INT_ADD", "register:40f0:8", ["const:baa894:8", "const:4:8"]]
+ 00baa894 ["CALL", null, ["callee:00be1520:8"]]
- 00baa7cc bytes 29db0094
+ 00baa894 bytes 23db0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dc7b75ef647358fc520516f591b8b7e"></a>

### [`00baa86c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa86c.md) → [`00baa934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa934.md) _ZNSt6__ndk112ctype_bynameIwEC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00be1760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1760.md) [`00be1930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1930.md) · 呼出先 6件 [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00be0eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0eb0.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md)
- 新版 呼出元 2件 [`00be1810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1810.md) [`00be19e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19e0.md) · 呼出先 6件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00baa960",
      "incomplete_value": true,
      "site": "00baa960",
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
      "definition_site": "00baa898",
      "incomplete_value": true,
      "site": "00baa898",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00baa9a0",
      "incomplete_value": false,
      "site": "00baa9b0",
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
            "const:5bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baa8d8",
      "incomplete_value": false,
      "site": "00baa8e8",
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
            "const:650:8"
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
      "00baa954",
      "READ",
      [
        "storage",
        "00c1bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00baa960",
      "DATA",
      [
        "storage",
        "00c13990",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00baa9a0",
      "PARAM",
      [
        "storage",
        "002ae650",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00baa954",
      "READ",
      [
        "storage",
        "00c1bf58",
        null,
        "pointer"
      ]
    ],
    [
      "00baa960",
      "DATA",
      [
        "storage",
        "00c13a40",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00baa9a0",
      "PARAM",
      [
        "storage",
        "002ae5bc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa86c.md#insn-00baa8e8) · [`00baa88c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa86c.md#insn-00baa88c) · [`00baa8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa86c.md#insn-00baa8b4)
- 新版 `00baa9b0`（命令位置の公開資料なし） · `00baa954`（命令位置の公開資料なし） · `00baa97c`（命令位置の公開資料なし）

~~~diff
- 00baa8e8 ["INT_ADD", "register:40f0:8", ["const:baa8e8:8", "const:4:8"]]
- 00baa8e8 ["CALL", null, ["callee:00bdb210:8"]]
+ 00baa9b0 ["INT_ADD", "register:40f0:8", ["const:baa9b0:8", "const:4:8"]]
+ 00baa9b0 ["CALL", null, ["callee:00bdb210:8"]]
- 00baa8e8 bytes 1ec20094
+ 00baa9b0 bytes 18c20094
- 00baa88c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
- 00baa88c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baa954 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f58:8"]]
+ 00baa954 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00baa88c bytes 085547f9
+ 00baa954 bytes 08ad47f9
- 00baa8b4 ["INT_ADD", "register:40f0:8", ["const:baa8b4:8", "const:4:8"]]
- 00baa8b4 ["CALL", null, ["callee:00be1520:8"]]
+ 00baa97c ["INT_ADD", "register:40f0:8", ["const:baa97c:8", "const:4:8"]]
+ 00baa97c ["CALL", null, ["callee:00be1520:8"]]
- 00baa8b4 bytes efda0094
+ 00baa97c bytes e9da0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

