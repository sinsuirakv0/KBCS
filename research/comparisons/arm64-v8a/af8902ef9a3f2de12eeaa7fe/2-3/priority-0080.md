# v16.0.0 → v16.0.1 · 最優先の変更候補 (80)

[一覧の目次](README.md)

<a id="compare-d80ebe8153b11f327eb6a1985a108b08"></a>

### [`00bc1830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1830.md) → [`00bc1c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1c58.md) _ZN8firebase13remote_config8internal6config15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1cb0",
      "incomplete_value": true,
      "site": "00bc1cb0",
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
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1888",
      "incomplete_value": true,
      "site": "00bc1888",
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
            "const:80:8"
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
      "definition_site": "00bc1c8c",
      "incomplete_value": true,
      "site": "00bc1c98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:478:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1864",
      "incomplete_value": true,
      "site": "00bc1870",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:78:8"
              ]
            ]
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
      "00bc1c6c",
      "READ",
      [
        "storage",
        "01126080",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1c8c",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1cb0",
      "WRITE",
      [
        "storage",
        "01126080",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc1c6c",
      "READ",
      [
        "storage",
        "01126480",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1c8c",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1cb0",
      "WRITE",
      [
        "storage",
        "01126480",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1830.md#insn-00bc1870) · [`00bc1888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1830.md#insn-00bc1888) · [`00bc1844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1830.md#insn-00bc1844)
- 新版 `00bc1c98`（命令位置の公開資料なし） · `00bc1cb0`（命令位置の公開資料なし） · `00bc1c6c`（命令位置の公開資料なし）

~~~diff
- 00bc1870 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc1870 ["INT_ADD", "register:40f0:8", ["const:bc1870:8", "const:4:8"]]
- 00bc1870 ["CALLIND", null, ["register:0:8"]]
+ 00bc1c98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc1c98 ["INT_ADD", "register:40f0:8", ["const:bc1c98:8", "const:4:8"]]
+ 00bc1c98 ["CALLIND", null, ["register:0:8"]]
- 00bc1870 bytes 00013fd6
+ 00bc1c98 bytes 00013fd6
- 00bc1888 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc1888 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:80:8"]]
- 00bc1888 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc1cb0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc1cb0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:480:8"]]
+ 00bc1cb0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc1888 bytes a0020239
+ 00bc1cb0 bytes a0021239
- 00bc1844 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:80:8"]]
- 00bc1844 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bc1844 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bc1c6c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:480:8"]]
+ 00bc1c6c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1c6c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bc1844 bytes a8024239
+ 00bc1c6c bytes a8025239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a240a2a55798ac92f09e7e8c636df812"></a>

### [`00bc189c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc189c.md) → [`00bc1cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1cc4.md) _ZN8firebase13remote_config8internal6config12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1d00",
      "incomplete_value": true,
      "site": "00bc1d00",
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
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc18d8",
      "incomplete_value": true,
      "site": "00bc18d8",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1d20",
      "incomplete_value": true,
      "site": "00bc1d20",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc18f8",
      "incomplete_value": true,
      "site": "00bc18f8",
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
            "const:78:8"
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
      "definition_site": "00bc1cdc",
      "incomplete_value": true,
      "site": "00bc1cdc",
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
      "definition_site": "00bc18b4",
      "incomplete_value": true,
      "site": "00bc18b4",
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
      "00bc1cd8",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1ce4",
      "READ",
      [
        "storage",
        "01126080",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1d00",
      "WRITE",
      [
        "storage",
        "01126080",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc1cd8",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1ce4",
      "READ",
      [
        "storage",
        "01126480",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1d00",
      "WRITE",
      [
        "storage",
        "01126480",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc18d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc189c.md#insn-00bc18d8) · [`00bc18f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc189c.md#insn-00bc18f4) · [`00bc18f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc189c.md#insn-00bc18f8)
- 新版 `00bc1d00`（命令位置の公開資料なし） · `00bc1d1c`（命令位置の公開資料なし） · `00bc1d20`（命令位置の公開資料なし）

~~~diff
- 00bc18d8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc18d8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc18d8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:80:8"]]
- 00bc18d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bc1d00 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bc1d00 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bc1d00 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:480:8"]]
+ 00bc1d00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc18d8 bytes bf020239
+ 00bc1d00 bytes bf021239
- 00bc18f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc18f4 ["INT_ADD", "register:40f0:8", ["const:bc18f4:8", "const:4:8"]]
- 00bc18f4 ["CALLIND", null, ["register:0:8"]]
+ 00bc1d1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc1d1c ["INT_ADD", "register:40f0:8", ["const:bc1d1c:8", "const:4:8"]]
+ 00bc1d1c ["CALLIND", null, ["register:0:8"]]
- 00bc18f4 bytes 00013fd6
+ 00bc1d1c bytes 00013fd6
- 00bc18f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
- 00bc18f8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bc18f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bc1d20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:478:8"]]
+ 00bc1d20 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bc1d20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bc18f8 bytes 9f3e00f9
+ 00bc1d20 bytes 9f3e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3ca5b04b3e28d4051e33864cbbe2d21"></a>

### [`00bc190c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc190c.md) → [`00bc1d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1d34.md) _ZN8firebase13remote_config8internal6config14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc194c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc1d74"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1928"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1920",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc1928",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1d78"
      ]
    ],
    [
      "unmatched:00bc1930",
      "PARAM",
      [
        "storage",
        "002b1656",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc1d48",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1d50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1d78"
      ]
    ],
    [
      "00bc1d58",
      "PARAM",
      [
        "storage",
        "002b1696",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc190c.md#insn-00bc1928) · [`00bc1944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc190c.md#insn-00bc1944) · [`00bc194c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc190c.md#insn-00bc194c)
- 新版 `00bc1d6c`（命令位置の公開資料なし）

~~~diff
- 00bc1928 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc1928 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc1928 bytes 410100b5
- 00bc1944 ["INT_ADD", "register:40f0:8", ["const:bc1944:8", "const:4:8"]]
- 00bc1944 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc1d6c ["INT_ADD", "register:40f0:8", ["const:bc1d6c:8", "const:4:8"]]
+ 00bc1d6c ["CALL", null, ["callee:00c5af10:8"]]
- 00bc1944 bytes 73640294
+ 00bc1d6c bytes 69640294
- 00bc194c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
- 00bc194c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc194c bytes 803e00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bef1f1efc7b0be135950353ba029b74"></a>

### [`00bc197c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc197c.md) → [`00bc1da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1da4.md) _ZN8firebase13remote_config8internal6config11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc1dc0",
      "incomplete_value": false,
      "site": "00bc1dc4",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1998",
      "incomplete_value": false,
      "site": "00bc199c",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc1dd0",
      "incomplete_value": true,
      "site": "00bc1ddc",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc19a8",
      "incomplete_value": true,
      "site": "00bc19b4",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00bc1dc0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bc1dd0",
      "DATA",
      [
        "storage",
        "01126088",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1dc0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc1dd0",
      "DATA",
      [
        "storage",
        "01126488",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc199c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc197c.md#insn-00bc199c) · [`00bc1998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc197c.md#insn-00bc1998) · [`00bc19a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc197c.md#insn-00bc19a4)
- 新版 `00bc1dc4`（命令位置の公開資料なし） · `00bc1dc0`（命令位置の公開資料なし） · `00bc1dcc`（命令位置の公開資料なし）

~~~diff
- 00bc199c ["INT_ADD", "register:40f0:8", ["const:bc199c:8", "const:4:8"]]
- 00bc199c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc1dc4 ["INT_ADD", "register:40f0:8", ["const:bc1dc4:8", "const:4:8"]]
+ 00bc1dc4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc199c bytes 99640294
+ 00bc1dc4 bytes 8f640294
- 00bc1998 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bc1998 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1998 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1998 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc1dc0 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bc1dc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1dc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1dc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc1998 bytes 00680a91
+ 00bc1dc0 bytes 009c0d91
- 00bc19a4 ["COPY", "tmp:0:8", ["const:88:8"]]
- 00bc19a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc19a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc19a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc1dcc ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00bc1dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc19a4 bytes 08210291
+ 00bc1dcc bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36f89316373a8053938fc6e9c2e9119c"></a>

### [`00bc19b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc19b8.md) → [`00bc1de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1de0.md) _ZN8firebase13remote_config8internal6config13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1e20",
      "incomplete_value": true,
      "site": "00bc1e20",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc19f8",
      "incomplete_value": true,
      "site": "00bc19f8",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1dfc",
      "incomplete_value": true,
      "site": "00bc1dfc",
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
      "definition_site": "00bc19d4",
      "incomplete_value": true,
      "site": "00bc19d4",
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
      "definition_site": "00bc1e04",
      "incomplete_value": false,
      "site": "00bc1e18",
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
            "const:696:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc19dc",
      "incomplete_value": false,
      "site": "00bc19f0",
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
            "const:656:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc1df4",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1e04",
      "PARAM",
      [
        "storage",
        "002b1656",
        null,
        "string"
      ]
    ],
    [
      "00bc1e20",
      "WRITE",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1df4",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1e04",
      "PARAM",
      [
        "storage",
        "002b1696",
        null,
        "string"
      ]
    ],
    [
      "00bc1e20",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc19f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc19b8.md#insn-00bc19f0) · [`00bc19f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc19b8.md#insn-00bc19f8) · [`00bc19cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc19b8.md#insn-00bc19cc)
- 新版 `00bc1e18`（命令位置の公開資料なし） · `00bc1e20`（命令位置の公開資料なし） · `00bc1df4`（命令位置の公開資料なし）

~~~diff
- 00bc19f0 ["INT_ADD", "register:40f0:8", ["const:bc19f0:8", "const:4:8"]]
- 00bc19f0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc1e18 ["INT_ADD", "register:40f0:8", ["const:bc1e18:8", "const:4:8"]]
+ 00bc1e18 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc19f0 bytes 48640294
+ 00bc1e18 bytes 3e640294
- 00bc19f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
- 00bc19f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1e20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:478:8"]]
+ 00bc1e20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc19f8 bytes 803e00f9
+ 00bc1e20 bytes 803e02f9
- 00bc19cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
- 00bc19cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1df4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:478:8"]]
+ 00bc1df4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc19cc bytes 813e40f9
+ 00bc1df4 bytes 813e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a58cda33b1aecd47870586832a47062"></a>

### [`00bc1a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1a28.md) → [`00bc1e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1e50.md) _ZN8firebase13remote_config8internal6config10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc1e6c",
      "incomplete_value": false,
      "site": "00bc1e70",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1a44",
      "incomplete_value": false,
      "site": "00bc1a48",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc1e7c",
      "incomplete_value": true,
      "site": "00bc1e88",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1a54",
      "incomplete_value": true,
      "site": "00bc1a60",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00bc1e6c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bc1e7c",
      "DATA",
      [
        "storage",
        "01126118",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc1e6c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bc1e7c",
      "DATA",
      [
        "storage",
        "01126518",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1a28.md#insn-00bc1a48) · [`00bc1a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1a28.md#insn-00bc1a44) · [`00bc1a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1a28.md#insn-00bc1a50)
- 新版 `00bc1e70`（命令位置の公開資料なし） · `00bc1e6c`（命令位置の公開資料なし） · `00bc1e78`（命令位置の公開資料なし）

~~~diff
- 00bc1a48 ["INT_ADD", "register:40f0:8", ["const:bc1a48:8", "const:4:8"]]
- 00bc1a48 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc1e70 ["INT_ADD", "register:40f0:8", ["const:bc1e70:8", "const:4:8"]]
+ 00bc1e70 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc1a48 bytes 6e640294
+ 00bc1e70 bytes 64640294
- 00bc1a44 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bc1a44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1a44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1a44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc1e6c ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bc1e6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1e6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1e6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc1a44 bytes 00441191
+ 00bc1e6c bytes 00781491
- 00bc1a50 ["COPY", "tmp:0:8", ["const:118:8"]]
- 00bc1a50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1a50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1a50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc1e78 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00bc1e78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1e78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1e78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc1a50 bytes 08610491
+ 00bc1e78 bytes 08611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9a919d1d87cf524c93f76c792f31e86"></a>

### [`00bc1a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1a64.md) → [`00bc1e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1e8c.md) _ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1eb8",
      "incomplete_value": true,
      "site": "00bc1eb8",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1a90",
      "incomplete_value": true,
      "site": "00bc1a90",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1ea0",
      "incomplete_value": true,
      "site": "00bc1ea0",
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
      "definition_site": "00bc1a78",
      "incomplete_value": true,
      "site": "00bc1a78",
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
      "definition_site": "00bc1eac",
      "incomplete_value": false,
      "site": "00bc1eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:cca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1a84",
      "incomplete_value": false,
      "site": "00bc1a88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:c8a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc1e9c",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1eac",
      "PARAM",
      [
        "storage",
        "002c1c8a",
        null,
        "string"
      ]
    ],
    [
      "00bc1eb8",
      "WRITE",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1e9c",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1eac",
      "PARAM",
      [
        "storage",
        "002c1cca",
        null,
        "string"
      ]
    ],
    [
      "00bc1eb8",
      "WRITE",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1a64.md#insn-00bc1a88) · [`00bc1a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1a64.md#insn-00bc1a90) · [`00bc1a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1a64.md#insn-00bc1a74)
- 新版 `00bc1eb0`（命令位置の公開資料なし） · `00bc1eb8`（命令位置の公開資料なし） · `00bc1e9c`（命令位置の公開資料なし）

~~~diff
- 00bc1a88 ["INT_ADD", "register:40f0:8", ["const:bc1a88:8", "const:4:8"]]
- 00bc1a88 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc1eb0 ["INT_ADD", "register:40f0:8", ["const:bc1eb0:8", "const:4:8"]]
+ 00bc1eb0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc1a88 bytes 22640294
+ 00bc1eb0 bytes 18640294
- 00bc1a90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:120:8"]]
- 00bc1a90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1eb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:520:8"]]
+ 00bc1eb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1a90 bytes 609200f9
+ 00bc1eb8 bytes 609202f9
- 00bc1a74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:120:8"]]
- 00bc1a74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1e9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:520:8"]]
+ 00bc1e9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc1a74 bytes 689240f9
+ 00bc1e9c bytes 689242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3729b161c8bbad70fe4fc14cd7a3825"></a>

### [`00bc1aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1aa4.md) → [`00bc1ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1ecc.md) _ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1aa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1aa8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1aa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc1aa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc1edc",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1ecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc1ed0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc1edc",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1aa4.md#insn-00bc1aa4) · [`00bc1aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1aa4.md#insn-00bc1aa8) · [`00bc1ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1aa4.md#insn-00bc1ab8)
- 新版 `00bc1ee0`（命令位置の公開資料なし）

~~~diff
- 00bc1aa4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc1aa4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc1aa4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc1aa4 bytes f30f1ef8
- 00bc1aa8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc1aa8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc1aa8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc1aa8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc1aa8 bytes fd7b01a9
- 00bc1ab8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc1ab8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc1ee0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc1ee0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc1ab8 bytes e80000b5
+ 00bc1ee0 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7eadc58dd055e56119191a24ea20bf"></a>

### [`00bc1ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1ae4.md) → [`00bc1f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1f0c.md) _ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1b14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc1f3c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1f20",
      "incomplete_value": true,
      "site": "00bc1f20",
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
      "definition_site": "00bc1af8",
      "incomplete_value": true,
      "site": "00bc1af8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc1f1c",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc1b04",
      "PARAM",
      [
        "storage",
        "002c1c8a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc1b0c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bc1f1c",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1f2c",
      "PARAM",
      [
        "storage",
        "002c1cca",
        null,
        "string"
      ]
    ],
    [
      "00bc1f34",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1ae4.md#insn-00bc1af8) · [`00bc1b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1ae4.md#insn-00bc1b0c) · [`00bc1b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1ae4.md#insn-00bc1b14)
- 新版 `00bc1f20`（命令位置の公開資料なし）

~~~diff
- 00bc1af8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc1af8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc1f20 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc1f20 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc1af8 bytes 080100b5
+ 00bc1f20 bytes 080100b5
- 00bc1b0c ["INT_ADD", "register:40f0:8", ["const:bc1b0c:8", "const:4:8"]]
- 00bc1b0c ["CALL", null, ["callee:00c5af10:8"]]
- 00bc1b0c bytes 01640294
- 00bc1b14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:120:8"]]
- 00bc1b14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1b14 bytes 609200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2e321a151b68371641cb3087e96a104"></a>

### [`00bc1b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1b28.md) → [`00bc1f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1f50.md) _ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1b58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc1f80"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1f64",
      "incomplete_value": true,
      "site": "00bc1f64",
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
      "definition_site": "00bc1b3c",
      "incomplete_value": true,
      "site": "00bc1b3c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc1f60",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1f64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc1b5c"
      ]
    ],
    [
      "unmatched:00bc1b44",
      "PARAM",
      [
        "storage",
        "002c1c8a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc1f60",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1f64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1f84"
      ]
    ],
    [
      "00bc1f6c",
      "PARAM",
      [
        "storage",
        "002c1cca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1b28.md#insn-00bc1b3c) · [`00bc1b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1b28.md#insn-00bc1b50) · [`00bc1b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1b28.md#insn-00bc1b58)
- 新版 `00bc1f64`（命令位置の公開資料なし） · `00bc1f78`（命令位置の公開資料なし）

~~~diff
- 00bc1b3c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc1b3c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bc1f64 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc1f64 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc1b3c bytes 080100b5
+ 00bc1f64 bytes 080100b5
- 00bc1b50 ["INT_ADD", "register:40f0:8", ["const:bc1b50:8", "const:4:8"]]
- 00bc1b50 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc1f78 ["INT_ADD", "register:40f0:8", ["const:bc1f78:8", "const:4:8"]]
+ 00bc1f78 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc1b50 bytes f0630294
+ 00bc1f78 bytes e6630294
- 00bc1b58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:120:8"]]
- 00bc1b58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1b58 bytes 609200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d32a7fdc9f3863f2e827069fa90b4583"></a>

### [`00bc1be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1be4.md) → [`00bc200c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc200c.md) _ZN8firebase13remote_config8internal12config_value12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2048",
      "incomplete_value": true,
      "site": "00bc2048",
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
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1c20",
      "incomplete_value": true,
      "site": "00bc1c20",
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
            "const:128:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2068",
      "incomplete_value": true,
      "site": "00bc2068",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1c40",
      "incomplete_value": true,
      "site": "00bc1c40",
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
            "const:120:8"
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
      "definition_site": "00bc2024",
      "incomplete_value": true,
      "site": "00bc2024",
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
      "definition_site": "00bc1bfc",
      "incomplete_value": true,
      "site": "00bc1bfc",
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
      "00bc2020",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc202c",
      "READ",
      [
        "storage",
        "01126128",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2048",
      "WRITE",
      [
        "storage",
        "01126128",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2020",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc202c",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2048",
      "WRITE",
      [
        "storage",
        "01126528",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1be4.md#insn-00bc1c20) · [`00bc1c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1be4.md#insn-00bc1c3c) · [`00bc1c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1be4.md#insn-00bc1c40)
- 新版 `00bc2048`（命令位置の公開資料なし） · `00bc2064`（命令位置の公開資料なし） · `00bc2068`（命令位置の公開資料なし）

~~~diff
- 00bc1c20 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc1c20 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc1c20 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:128:8"]]
- 00bc1c20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bc2048 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bc2048 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bc2048 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:528:8"]]
+ 00bc2048 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc1c20 bytes bfa20439
+ 00bc2048 bytes bfa21439
- 00bc1c3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc1c3c ["INT_ADD", "register:40f0:8", ["const:bc1c3c:8", "const:4:8"]]
- 00bc1c3c ["CALLIND", null, ["register:0:8"]]
+ 00bc2064 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2064 ["INT_ADD", "register:40f0:8", ["const:bc2064:8", "const:4:8"]]
+ 00bc2064 ["CALLIND", null, ["register:0:8"]]
- 00bc1c3c bytes 00013fd6
+ 00bc2064 bytes 00013fd6
- 00bc1c40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:120:8"]]
- 00bc1c40 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bc1c40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bc2068 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:520:8"]]
+ 00bc2068 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bc2068 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bc1c40 bytes 9f9200f9
+ 00bc2068 bytes 9f9202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3be9a4290e12ff5592999d6cda8b778d"></a>

### [`00bc1c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1c54.md) → [`00bc207c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc207c.md) _ZN8firebase13remote_config8internal12config_value14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1c94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc20bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1c70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1c68",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc1c70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc20c0"
      ]
    ],
    [
      "unmatched:00bc1c78",
      "PARAM",
      [
        "storage",
        "002c1c8a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2090",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2098",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc20c0"
      ]
    ],
    [
      "00bc20a0",
      "PARAM",
      [
        "storage",
        "002c1cca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1c54.md#insn-00bc1c70) · [`00bc1c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1c54.md#insn-00bc1c8c) · [`00bc1c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1c54.md#insn-00bc1c94)
- 新版 `00bc20b4`（命令位置の公開資料なし）

~~~diff
- 00bc1c70 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc1c70 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc1c70 bytes 410100b5
- 00bc1c8c ["INT_ADD", "register:40f0:8", ["const:bc1c8c:8", "const:4:8"]]
- 00bc1c8c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc20b4 ["INT_ADD", "register:40f0:8", ["const:bc20b4:8", "const:4:8"]]
+ 00bc20b4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc1c8c bytes a1630294
+ 00bc20b4 bytes 97630294
- 00bc1c94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:120:8"]]
- 00bc1c94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1c94 bytes 809200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30d594999a094f61790e080a1500b863"></a>

### [`00bc1d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1d00.md) → [`00bc2128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2128.md) _ZN8firebase13remote_config8internal12config_value13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1d40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2168"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1d1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1d14",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc1d1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc216c"
      ]
    ],
    [
      "unmatched:00bc1d24",
      "PARAM",
      [
        "storage",
        "002c1c8a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc213c",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2144",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc216c"
      ]
    ],
    [
      "00bc214c",
      "PARAM",
      [
        "storage",
        "002c1cca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1d00.md#insn-00bc1d1c) · [`00bc1d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1d00.md#insn-00bc1d38) · [`00bc1d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1d00.md#insn-00bc1d40)
- 新版 `00bc2160`（命令位置の公開資料なし）

~~~diff
- 00bc1d1c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc1d1c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc1d1c bytes 410100b5
- 00bc1d38 ["INT_ADD", "register:40f0:8", ["const:bc1d38:8", "const:4:8"]]
- 00bc1d38 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc2160 ["INT_ADD", "register:40f0:8", ["const:bc2160:8", "const:4:8"]]
+ 00bc2160 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc1d38 bytes 76630294
+ 00bc2160 bytes 6c630294
- 00bc1d40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:120:8"]]
- 00bc1d40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1d40 bytes 809200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-073e96ea0c1cfe07ea9f5febf5bce565"></a>

### [`00bc1dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1dac.md) → [`00bc21d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc21d4.md) _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call, call_count, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1dac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1db0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1db0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1dac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc1db0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc21e4",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc21d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc21d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc21e4",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1dac.md#insn-00bc1dac) · [`00bc1db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1dac.md#insn-00bc1db0) · [`00bc1dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1dac.md#insn-00bc1dd0)

~~~diff
- 00bc1dac ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc1dac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc1dac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc1dac bytes f30f1ef8
- 00bc1db0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc1db0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc1db0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc1db0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc1db0 bytes fd7b01a9
- 00bc1dd0 ["INT_ADD", "register:40f0:8", ["const:bc1dd0:8", "const:4:8"]]
- 00bc1dd0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc1dd0 bytes 50630294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc335d230471f6618998ba5e75adfb47"></a>

### [`00bc1dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1dec.md) → [`00bc2214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2214.md) _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1dec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1df0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1df0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1dec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc1df0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2224",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2214",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc2218",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2224",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1dec.md#insn-00bc1dec) · [`00bc1df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1dec.md#insn-00bc1df0) · [`00bc1e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1dec.md#insn-00bc1e00)
- 新版 `00bc2228`（命令位置の公開資料なし）

~~~diff
- 00bc1dec ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc1dec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc1dec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc1dec bytes f30f1ef8
- 00bc1df0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc1df0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc1df0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc1df0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc1df0 bytes fd7b01a9
- 00bc1e00 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc1e00 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bc2228 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc2228 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc1e00 bytes e80000b5
+ 00bc2228 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b401a5890b83478272eeef4df0675c26"></a>

### [`00bc1e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1e2c.md) → [`00bc2254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2254.md) _ZN8firebase13remote_config8internal11config_info10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2284",
      "incomplete_value": true,
      "site": "00bc2284",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1e5c",
      "incomplete_value": true,
      "site": "00bc1e5c",
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
            "const:168:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2268",
      "incomplete_value": true,
      "site": "00bc2268",
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
      "definition_site": "00bc1e40",
      "incomplete_value": true,
      "site": "00bc1e40",
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
      "definition_site": "00bc2274",
      "incomplete_value": false,
      "site": "00bc227c",
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
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1e4c",
      "incomplete_value": false,
      "site": "00bc1e54",
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
            "const:30c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2264",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2274",
      "PARAM",
      [
        "storage",
        "002a730c",
        null,
        "string"
      ]
    ],
    [
      "00bc2284",
      "WRITE",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2264",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2274",
      "PARAM",
      [
        "storage",
        "002a73e8",
        null,
        "string"
      ]
    ],
    [
      "00bc2284",
      "WRITE",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1e2c.md#insn-00bc1e54) · [`00bc1e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1e2c.md#insn-00bc1e5c) · [`00bc1e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1e2c.md#insn-00bc1e3c)
- 新版 `00bc227c`（命令位置の公開資料なし） · `00bc2284`（命令位置の公開資料なし） · `00bc2264`（命令位置の公開資料なし）

~~~diff
- 00bc1e54 ["INT_ADD", "register:40f0:8", ["const:bc1e54:8", "const:4:8"]]
- 00bc1e54 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc227c ["INT_ADD", "register:40f0:8", ["const:bc227c:8", "const:4:8"]]
+ 00bc227c ["CALL", null, ["callee:00c5af10:8"]]
- 00bc1e54 bytes 2f630294
+ 00bc227c bytes 25630294
- 00bc1e5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:168:8"]]
- 00bc1e5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2284 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
+ 00bc2284 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1e5c bytes 60b600f9
+ 00bc2284 bytes 60b602f9
- 00bc1e3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:168:8"]]
- 00bc1e3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2264 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
+ 00bc2264 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc1e3c bytes 68b640f9
+ 00bc2264 bytes 68b642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fea8359091887ce26d81d2e01de89ef2"></a>

### [`00bc1e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1e70.md) → [`00bc2298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2298.md) _ZN8firebase13remote_config8internal11config_info10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc22c8",
      "incomplete_value": true,
      "site": "00bc22c8",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1ea0",
      "incomplete_value": true,
      "site": "00bc1ea0",
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
            "const:168:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc22ac",
      "incomplete_value": true,
      "site": "00bc22ac",
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
      "definition_site": "00bc1e84",
      "incomplete_value": true,
      "site": "00bc1e84",
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
      "definition_site": "00bc22b4",
      "incomplete_value": false,
      "site": "00bc22c0",
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
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1e8c",
      "incomplete_value": false,
      "site": "00bc1e98",
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
            "const:30c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc22a8",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc22b4",
      "PARAM",
      [
        "storage",
        "002a730c",
        null,
        "string"
      ]
    ],
    [
      "00bc22c8",
      "WRITE",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc22a8",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc22b4",
      "PARAM",
      [
        "storage",
        "002a73e8",
        null,
        "string"
      ]
    ],
    [
      "00bc22c8",
      "WRITE",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1e70.md#insn-00bc1e98) · [`00bc1ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1e70.md#insn-00bc1ea0) · [`00bc1e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1e70.md#insn-00bc1e80)
- 新版 `00bc22c0`（命令位置の公開資料なし） · `00bc22c8`（命令位置の公開資料なし） · `00bc22a8`（命令位置の公開資料なし）

~~~diff
- 00bc1e98 ["INT_ADD", "register:40f0:8", ["const:bc1e98:8", "const:4:8"]]
- 00bc1e98 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc22c0 ["INT_ADD", "register:40f0:8", ["const:bc22c0:8", "const:4:8"]]
+ 00bc22c0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc1e98 bytes 1e630294
+ 00bc22c0 bytes 14630294
- 00bc1ea0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:168:8"]]
- 00bc1ea0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc22c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
+ 00bc22c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1ea0 bytes 60b600f9
+ 00bc22c8 bytes 60b602f9
- 00bc1e80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:168:8"]]
- 00bc1e80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc22a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
+ 00bc22a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc1e80 bytes 68b640f9
+ 00bc22a8 bytes 68b642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70c5bb52f1f7bbfaf69def8f97895d0d"></a>

### [`00bc1ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1ec0.md) → [`00bc22e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc22e8.md) _ZN8firebase13remote_config8internal11config_info15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 14.29% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1f18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2340"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1f00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc22fc",
      "READ",
      [
        "storage",
        "01126170",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2308",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc1f1c"
      ]
    ],
    [
      "unmatched:00bc1ef4",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc22fc",
      "READ",
      [
        "storage",
        "01126570",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2308",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2344"
      ]
    ],
    [
      "00bc231c",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1ec0.md#insn-00bc1f00) · [`00bc1f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1ec0.md#insn-00bc1f0c) · [`00bc1f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1ec0.md#insn-00bc1f18)
- 新版 `00bc2334`（命令位置の公開資料なし）

~~~diff
- 00bc1f00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc1f00 ["INT_ADD", "register:40f0:8", ["const:bc1f00:8", "const:4:8"]]
- 00bc1f00 ["CALLIND", null, ["register:0:8"]]
- 00bc1f00 bytes 00013fd6
- 00bc1f0c ["INT_ADD", "register:40f0:8", ["const:bc1f0c:8", "const:4:8"]]
- 00bc1f0c ["CALL", null, ["callee:00c5af60:8"]]
+ 00bc2334 ["INT_ADD", "register:40f0:8", ["const:bc2334:8", "const:4:8"]]
+ 00bc2334 ["CALL", null, ["callee:00c5af60:8"]]
- 00bc1f0c bytes 15630294
+ 00bc2334 bytes 0b630294
- 00bc1f18 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc1f18 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:170:8"]]
- 00bc1f18 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc1f18 bytes a0c20539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0ef4b97dd2506b0d2cb8c7a17a9dab1"></a>

### [`00bc1f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1f2c.md) → [`00bc2354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2354.md) _ZN8firebase13remote_config8internal11config_info12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1f68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1f88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2390"
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
      "00bc2368",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc236c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc1f8c"
      ]
    ],
    [
      "00bc2374",
      "READ",
      [
        "storage",
        "01126170",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2368",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc236c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc23b4"
      ]
    ],
    [
      "00bc2374",
      "READ",
      [
        "storage",
        "01126570",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1f2c.md#insn-00bc1f44) · [`00bc1f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1f2c.md#insn-00bc1f68) · [`00bc1f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1f2c.md#insn-00bc1f70)
- 新版 `00bc236c`（命令位置の公開資料なし）

~~~diff
- 00bc1f44 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc1f44 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bc236c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc236c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bc1f44 bytes 410200b4
+ 00bc236c bytes 410200b4
- 00bc1f68 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc1f68 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc1f68 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:170:8"]]
- 00bc1f68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc1f68 bytes bfc20539
- 00bc1f70 ["INT_ADD", "register:40f0:8", ["const:bc1f70:8", "const:4:8"]]
- 00bc1f70 ["CALL", null, ["callee:00c5af60:8"]]
- 00bc1f70 bytes fc620294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f4ff2c24c9cac26bb8f770ac2e826ee"></a>

### [`00bc1f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1f9c.md) → [`00bc23c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc23c4.md) _ZN8firebase13remote_config8internal11config_info14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1fdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2404"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1fb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1fb0",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc1fb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2408"
      ]
    ],
    [
      "unmatched:00bc1fc0",
      "PARAM",
      [
        "storage",
        "002a730c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc23d8",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc23e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2408"
      ]
    ],
    [
      "00bc23e8",
      "PARAM",
      [
        "storage",
        "002a73e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1f9c.md#insn-00bc1fb8) · [`00bc1fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1f9c.md#insn-00bc1fd4) · [`00bc1fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1f9c.md#insn-00bc1fdc)
- 新版 `00bc23fc`（命令位置の公開資料なし）

~~~diff
- 00bc1fb8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc1fb8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bc1fb8 bytes 410100b5
- 00bc1fd4 ["INT_ADD", "register:40f0:8", ["const:bc1fd4:8", "const:4:8"]]
- 00bc1fd4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc23fc ["INT_ADD", "register:40f0:8", ["const:bc23fc:8", "const:4:8"]]
+ 00bc23fc ["CALL", null, ["callee:00c5af10:8"]]
- 00bc1fd4 bytes cf620294
+ 00bc23fc bytes c5620294
- 00bc1fdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:168:8"]]
- 00bc1fdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1fdc bytes 80b600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4eccacb37a4c714efde7afeae1ded087"></a>

### [`00bc200c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc200c.md) → [`00bc2434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2434.md) _ZN8firebase13remote_config8internal11config_info11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc2450",
      "incomplete_value": false,
      "site": "00bc2454",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2028",
      "incomplete_value": false,
      "site": "00bc202c",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc2460",
      "incomplete_value": true,
      "site": "00bc246c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2038",
      "incomplete_value": true,
      "site": "00bc2044",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00bc2450",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bc2460",
      "DATA",
      [
        "storage",
        "01126178",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2450",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc2460",
      "DATA",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc202c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc200c.md#insn-00bc202c) · [`00bc2028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc200c.md#insn-00bc2028) · [`00bc2034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc200c.md#insn-00bc2034)
- 新版 `00bc2454`（命令位置の公開資料なし） · `00bc2450`（命令位置の公開資料なし） · `00bc245c`（命令位置の公開資料なし）

~~~diff
- 00bc202c ["INT_ADD", "register:40f0:8", ["const:bc202c:8", "const:4:8"]]
- 00bc202c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc2454 ["INT_ADD", "register:40f0:8", ["const:bc2454:8", "const:4:8"]]
+ 00bc2454 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc202c bytes f5620294
+ 00bc2454 bytes eb620294
- 00bc2028 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bc2028 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2028 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2028 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc2450 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bc2450 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2450 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2450 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc2028 bytes 00680a91
+ 00bc2450 bytes 009c0d91
- 00bc2034 ["COPY", "tmp:0:8", ["const:178:8"]]
- 00bc2034 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2034 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2034 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc245c ["COPY", "tmp:0:8", ["const:578:8"]]
+ 00bc245c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc245c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc245c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc2034 bytes 08e10591
+ 00bc245c bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3707db7892f089ead25431970e8fb271"></a>

### [`00bc2048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2048.md) → [`00bc2470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2470.md) _ZN8firebase13remote_config8internal11config_info13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc24b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2064"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc205c",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc2064",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc24b4"
      ]
    ],
    [
      "unmatched:00bc206c",
      "PARAM",
      [
        "storage",
        "002a730c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2484",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc248c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc24b4"
      ]
    ],
    [
      "00bc2494",
      "PARAM",
      [
        "storage",
        "002a73e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2048.md#insn-00bc2064) · [`00bc2080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2048.md#insn-00bc2080) · [`00bc2088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2048.md#insn-00bc2088)
- 新版 `00bc24a8`（命令位置の公開資料なし）

~~~diff
- 00bc2064 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc2064 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc2064 bytes 410100b5
- 00bc2080 ["INT_ADD", "register:40f0:8", ["const:bc2080:8", "const:4:8"]]
- 00bc2080 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc24a8 ["INT_ADD", "register:40f0:8", ["const:bc24a8:8", "const:4:8"]]
+ 00bc24a8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2080 bytes a4620294
+ 00bc24a8 bytes 9a620294
- 00bc2088 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:168:8"]]
- 00bc2088 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2088 bytes 80b600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5413170babf9da2336d03e80e717d4e4"></a>

### [`00bc20f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc20f4.md) → [`00bc251c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc251c.md) _ZN8firebase13remote_config8internal15config_settings19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFile

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2548",
      "incomplete_value": true,
      "site": "00bc2548",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2120",
      "incomplete_value": true,
      "site": "00bc2120",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2530",
      "incomplete_value": true,
      "site": "00bc2530",
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
      "definition_site": "00bc2108",
      "incomplete_value": true,
      "site": "00bc2108",
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
      "definition_site": "00bc253c",
      "incomplete_value": false,
      "site": "00bc2540",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2114",
      "incomplete_value": false,
      "site": "00bc2118",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc252c",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc253c",
      "PARAM",
      [
        "storage",
        "002b8be0",
        null,
        "string"
      ]
    ],
    [
      "00bc2548",
      "WRITE",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc252c",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc253c",
      "PARAM",
      [
        "storage",
        "002b8c20",
        null,
        "string"
      ]
    ],
    [
      "00bc2548",
      "WRITE",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc20f4.md#insn-00bc2118) · [`00bc2120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc20f4.md#insn-00bc2120) · [`00bc2104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc20f4.md#insn-00bc2104)
- 新版 `00bc2540`（命令位置の公開資料なし） · `00bc2548`（命令位置の公開資料なし） · `00bc252c`（命令位置の公開資料なし）

~~~diff
- 00bc2118 ["INT_ADD", "register:40f0:8", ["const:bc2118:8", "const:4:8"]]
- 00bc2118 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc2540 ["INT_ADD", "register:40f0:8", ["const:bc2540:8", "const:4:8"]]
+ 00bc2540 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2118 bytes 7e620294
+ 00bc2540 bytes 74620294
- 00bc2120 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:198:8"]]
- 00bc2120 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2548 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
+ 00bc2548 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2120 bytes 60ce00f9
+ 00bc2548 bytes 60ce02f9
- 00bc2104 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:198:8"]]
- 00bc2104 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc252c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
+ 00bc252c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2104 bytes 68ce40f9
+ 00bc252c bytes 68ce42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b4935e27422dff822bb9b257150a604"></a>

### [`00bc2134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2134.md) → [`00bc255c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc255c.md) _ZN8firebase13remote_config8internal15config_settings19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFile

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2588",
      "incomplete_value": true,
      "site": "00bc2588",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2160",
      "incomplete_value": true,
      "site": "00bc2160",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2570",
      "incomplete_value": true,
      "site": "00bc2570",
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
      "definition_site": "00bc2148",
      "incomplete_value": true,
      "site": "00bc2148",
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
      "definition_site": "00bc2578",
      "incomplete_value": false,
      "site": "00bc2580",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2150",
      "incomplete_value": false,
      "site": "00bc2158",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc256c",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2578",
      "PARAM",
      [
        "storage",
        "002b8be0",
        null,
        "string"
      ]
    ],
    [
      "00bc2588",
      "WRITE",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc256c",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2578",
      "PARAM",
      [
        "storage",
        "002b8c20",
        null,
        "string"
      ]
    ],
    [
      "00bc2588",
      "WRITE",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2134.md#insn-00bc2158) · [`00bc2160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2134.md#insn-00bc2160) · [`00bc2144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2134.md#insn-00bc2144)
- 新版 `00bc2580`（命令位置の公開資料なし） · `00bc2588`（命令位置の公開資料なし） · `00bc256c`（命令位置の公開資料なし）

~~~diff
- 00bc2158 ["INT_ADD", "register:40f0:8", ["const:bc2158:8", "const:4:8"]]
- 00bc2158 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc2580 ["INT_ADD", "register:40f0:8", ["const:bc2580:8", "const:4:8"]]
+ 00bc2580 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2158 bytes 6e620294
+ 00bc2580 bytes 64620294
- 00bc2160 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:198:8"]]
- 00bc2160 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2588 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
+ 00bc2588 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2160 bytes 60ce00f9
+ 00bc2588 bytes 60ce02f9
- 00bc2144 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:198:8"]]
- 00bc2144 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc256c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
+ 00bc256c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2144 bytes 68ce40f9
+ 00bc256c bytes 68ce42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f76f7c1b467f62f0c7bdab5d7a2d27b0"></a>

### [`00bc2174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2174.md) → [`00bc259c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc259c.md) _ZN8firebase13remote_config8internal15config_settings10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc25cc",
      "incomplete_value": true,
      "site": "00bc25cc",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc21a4",
      "incomplete_value": true,
      "site": "00bc21a4",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc25b0",
      "incomplete_value": true,
      "site": "00bc25b0",
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
      "definition_site": "00bc2188",
      "incomplete_value": true,
      "site": "00bc2188",
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
      "definition_site": "00bc25bc",
      "incomplete_value": false,
      "site": "00bc25c4",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2194",
      "incomplete_value": false,
      "site": "00bc219c",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc25ac",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc25bc",
      "PARAM",
      [
        "storage",
        "002b8be0",
        null,
        "string"
      ]
    ],
    [
      "00bc25cc",
      "WRITE",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc25ac",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc25bc",
      "PARAM",
      [
        "storage",
        "002b8c20",
        null,
        "string"
      ]
    ],
    [
      "00bc25cc",
      "WRITE",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc219c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2174.md#insn-00bc219c) · [`00bc21a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2174.md#insn-00bc21a4) · [`00bc2184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2174.md#insn-00bc2184)
- 新版 `00bc25c4`（命令位置の公開資料なし） · `00bc25cc`（命令位置の公開資料なし） · `00bc25ac`（命令位置の公開資料なし）

~~~diff
- 00bc219c ["INT_ADD", "register:40f0:8", ["const:bc219c:8", "const:4:8"]]
- 00bc219c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc25c4 ["INT_ADD", "register:40f0:8", ["const:bc25c4:8", "const:4:8"]]
+ 00bc25c4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc219c bytes 5d620294
+ 00bc25c4 bytes 53620294
- 00bc21a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:198:8"]]
- 00bc21a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc25cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
+ 00bc25cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc21a4 bytes 60ce00f9
+ 00bc25cc bytes 60ce02f9
- 00bc2184 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:198:8"]]
- 00bc2184 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc25ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
+ 00bc25ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2184 bytes 68ce40f9
+ 00bc25ac bytes 68ce42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5a294234e1c25c3032235d8a4887299"></a>

### [`00bc21b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc21b8.md) → [`00bc25e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc25e0.md) _ZN8firebase13remote_config8internal15config_settings10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc21b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc21bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc21bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc21b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc21bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc25f0",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc25e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc25e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc25f0",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc21b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc21b8.md#insn-00bc21b8) · [`00bc21bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc21b8.md#insn-00bc21bc) · [`00bc21cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc21b8.md#insn-00bc21cc)
- 新版 `00bc25f4`（命令位置の公開資料なし）

~~~diff
- 00bc21b8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc21b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc21b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc21b8 bytes f30f1ef8
- 00bc21bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc21bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc21bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc21bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc21bc bytes fd7b01a9
- 00bc21cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc21cc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bc25f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc25f4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc21cc bytes 080100b5
+ 00bc25f4 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d6019a7c344079c2550e85c199f2445"></a>

### [`00bc2208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2208.md) → [`00bc2630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2630.md) _ZN8firebase13remote_config8internal15config_settings15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2688",
      "incomplete_value": true,
      "site": "00bc2688",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2260",
      "incomplete_value": true,
      "site": "00bc2260",
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
            "const:1a0:8"
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
      "definition_site": "00bc2664",
      "incomplete_value": true,
      "site": "00bc2670",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:598:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc223c",
      "incomplete_value": true,
      "site": "00bc2248",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:198:8"
              ]
            ]
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
      "00bc2644",
      "READ",
      [
        "storage",
        "011261a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2664",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2688",
      "WRITE",
      [
        "storage",
        "011261a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2644",
      "READ",
      [
        "storage",
        "011265a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2664",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2688",
      "WRITE",
      [
        "storage",
        "011265a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2208.md#insn-00bc2248) · [`00bc2260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2208.md#insn-00bc2260) · [`00bc221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2208.md#insn-00bc221c)
- 新版 `00bc2670`（命令位置の公開資料なし） · `00bc2688`（命令位置の公開資料なし） · `00bc2644`（命令位置の公開資料なし）

~~~diff
- 00bc2248 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2248 ["INT_ADD", "register:40f0:8", ["const:bc2248:8", "const:4:8"]]
- 00bc2248 ["CALLIND", null, ["register:0:8"]]
+ 00bc2670 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2670 ["INT_ADD", "register:40f0:8", ["const:bc2670:8", "const:4:8"]]
+ 00bc2670 ["CALLIND", null, ["register:0:8"]]
- 00bc2248 bytes 00013fd6
+ 00bc2670 bytes 00013fd6
- 00bc2260 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc2260 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1a0:8"]]
- 00bc2260 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc2688 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc2688 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5a0:8"]]
+ 00bc2688 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc2260 bytes a0820639
+ 00bc2688 bytes a0821639
- 00bc221c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:1a0:8"]]
- 00bc221c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bc221c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bc2644 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a0:8"]]
+ 00bc2644 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2644 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bc221c bytes a8824639
+ 00bc2644 bytes a8825639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f273d55f94694470f41d5d1093d6956e"></a>

### [`00bc2274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2274.md) → [`00bc269c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc269c.md) _ZN8firebase13remote_config8internal15config_settings12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 16.67% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc22b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc22d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc26d8"
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
      "00bc26b0",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc26b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc22d4"
      ]
    ],
    [
      "00bc26bc",
      "READ",
      [
        "storage",
        "011261a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc26b0",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc26b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc26fc"
      ]
    ],
    [
      "00bc26bc",
      "READ",
      [
        "storage",
        "011265a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc228c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2274.md#insn-00bc228c) · [`00bc22b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2274.md#insn-00bc22b0) · [`00bc22b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2274.md#insn-00bc22b8)
- 新版 `00bc26b4`（命令位置の公開資料なし）

~~~diff
- 00bc228c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc228c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bc26b4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc26b4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bc228c bytes 410200b4
+ 00bc26b4 bytes 410200b4
- 00bc22b0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc22b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc22b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:1a0:8"]]
- 00bc22b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc22b0 bytes bf820639
- 00bc22b8 ["INT_ADD", "register:40f0:8", ["const:bc22b8:8", "const:4:8"]]
- 00bc22b8 ["CALL", null, ["callee:00c5af60:8"]]
- 00bc22b8 bytes 2a620294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fc4f6bf7838cf0d4e9f15978077bb21"></a>

### [`00bc22e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc22e4.md) → [`00bc270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc270c.md) _ZN8firebase13remote_config8internal15config_settings14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc22e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc22e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc22e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc22e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc22e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc22f8",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc270c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc2710",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2720",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc22e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc22e4.md#insn-00bc22e4) · [`00bc22e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc22e4.md#insn-00bc22e8) · [`00bc2300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc22e4.md#insn-00bc2300)

~~~diff
- 00bc22e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc22e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc22e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc22e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc22e4 bytes f44fbea9
- 00bc22e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc22e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc22e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc22e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc22e8 bytes fd7b01a9
- 00bc2300 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc2300 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc2300 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-279b8119d62f563f58e2d83568eb1486"></a>

### [`00bc2354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2354.md) → [`00bc277c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc277c.md) _ZN8firebase13remote_config8internal15config_settings11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc2798",
      "incomplete_value": false,
      "site": "00bc279c",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2370",
      "incomplete_value": false,
      "site": "00bc2374",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc27a8",
      "incomplete_value": true,
      "site": "00bc27b4",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2380",
      "incomplete_value": true,
      "site": "00bc238c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00bc2798",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bc27a8",
      "DATA",
      [
        "storage",
        "011261a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2798",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc27a8",
      "DATA",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2354.md#insn-00bc2374) · [`00bc2370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2354.md#insn-00bc2370) · [`00bc237c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2354.md#insn-00bc237c)
- 新版 `00bc279c`（命令位置の公開資料なし） · `00bc2798`（命令位置の公開資料なし） · `00bc27a4`（命令位置の公開資料なし）

~~~diff
- 00bc2374 ["INT_ADD", "register:40f0:8", ["const:bc2374:8", "const:4:8"]]
- 00bc2374 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc279c ["INT_ADD", "register:40f0:8", ["const:bc279c:8", "const:4:8"]]
+ 00bc279c ["CALL", null, ["callee:00c5b000:8"]]
- 00bc2374 bytes 23620294
+ 00bc279c bytes 19620294
- 00bc2370 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bc2370 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2370 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2370 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc2798 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bc2798 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2798 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2798 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc2370 bytes 00680a91
+ 00bc2798 bytes 009c0d91
- 00bc237c ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 00bc237c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc237c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc237c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc27a4 ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 00bc27a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc27a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc27a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc237c bytes 08a10691
+ 00bc27a4 bytes 08a11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc2f3ef9c9ba3ab2fd418331b1b55803"></a>

### [`00bc2390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2390.md) → [`00bc27b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc27b8.md) _ZN8firebase13remote_config8internal15config_settings13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc27f8",
      "incomplete_value": true,
      "site": "00bc27f8",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc23d0",
      "incomplete_value": true,
      "site": "00bc23d0",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc27d4",
      "incomplete_value": true,
      "site": "00bc27d4",
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
      "definition_site": "00bc23ac",
      "incomplete_value": true,
      "site": "00bc23ac",
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
      "definition_site": "00bc27dc",
      "incomplete_value": false,
      "site": "00bc27f0",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc23b4",
      "incomplete_value": false,
      "site": "00bc23c8",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc27cc",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc27dc",
      "PARAM",
      [
        "storage",
        "002b8be0",
        null,
        "string"
      ]
    ],
    [
      "00bc27f8",
      "WRITE",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc27cc",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc27dc",
      "PARAM",
      [
        "storage",
        "002b8c20",
        null,
        "string"
      ]
    ],
    [
      "00bc27f8",
      "WRITE",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc23c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2390.md#insn-00bc23c8) · [`00bc23d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2390.md#insn-00bc23d0) · [`00bc23a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2390.md#insn-00bc23a4)
- 新版 `00bc27f0`（命令位置の公開資料なし） · `00bc27f8`（命令位置の公開資料なし） · `00bc27cc`（命令位置の公開資料なし）

~~~diff
- 00bc23c8 ["INT_ADD", "register:40f0:8", ["const:bc23c8:8", "const:4:8"]]
- 00bc23c8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc27f0 ["INT_ADD", "register:40f0:8", ["const:bc27f0:8", "const:4:8"]]
+ 00bc27f0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc23c8 bytes d2610294
+ 00bc27f0 bytes c8610294
- 00bc23d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:198:8"]]
- 00bc23d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc27f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:598:8"]]
+ 00bc27f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc23d0 bytes 80ce00f9
+ 00bc27f8 bytes 80ce02f9
- 00bc23a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:198:8"]]
- 00bc23a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc27cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:598:8"]]
+ 00bc27cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc23a4 bytes 81ce40f9
+ 00bc27cc bytes 81ce42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-939809f292e8d8e698e586442c70a77b"></a>

### [`00bc2400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2400.md) → [`00bc2828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2828.md) _ZN8firebase13remote_config8internal15config_settings10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc2844",
      "incomplete_value": false,
      "site": "00bc2848",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc241c",
      "incomplete_value": false,
      "site": "00bc2420",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc2854",
      "incomplete_value": true,
      "site": "00bc2860",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc242c",
      "incomplete_value": true,
      "site": "00bc2438",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00bc2844",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bc2854",
      "DATA",
      [
        "storage",
        "011261b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc2844",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bc2854",
      "DATA",
      [
        "storage",
        "011265b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2400.md#insn-00bc2420) · [`00bc241c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2400.md#insn-00bc241c) · [`00bc2428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2400.md#insn-00bc2428)
- 新版 `00bc2848`（命令位置の公開資料なし） · `00bc2844`（命令位置の公開資料なし） · `00bc2850`（命令位置の公開資料なし）

~~~diff
- 00bc2420 ["INT_ADD", "register:40f0:8", ["const:bc2420:8", "const:4:8"]]
- 00bc2420 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc2848 ["INT_ADD", "register:40f0:8", ["const:bc2848:8", "const:4:8"]]
+ 00bc2848 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc2420 bytes f8610294
+ 00bc2848 bytes ee610294
- 00bc241c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bc241c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc241c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc241c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc2844 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bc2844 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2844 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2844 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc241c bytes 00441191
+ 00bc2844 bytes 00781491
- 00bc2428 ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 00bc2428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc2850 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 00bc2850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc2428 bytes 08e10691
+ 00bc2850 bytes 08e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad802cd0a1bf9792235b721c115163c6"></a>

### [`00bc243c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc243c.md) → [`00bc2864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2864.md) _ZN8firebase13remote_config8internal23config_settings_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embe

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2468"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2890"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2878",
      "incomplete_value": true,
      "site": "00bc2878",
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
      "definition_site": "00bc2450",
      "incomplete_value": true,
      "site": "00bc2450",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2874",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2878",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc246c"
      ]
    ],
    [
      "unmatched:00bc245c",
      "PARAM",
      [
        "storage",
        "002b9b9e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2874",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2878",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2894"
      ]
    ],
    [
      "00bc2884",
      "PARAM",
      [
        "storage",
        "002b9bde",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc243c.md#insn-00bc2450) · [`00bc2460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc243c.md#insn-00bc2460) · [`00bc2468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc243c.md#insn-00bc2468)
- 新版 `00bc2878`（命令位置の公開資料なし）

~~~diff
- 00bc2450 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc2450 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc2878 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc2878 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc2450 bytes e80000b5
+ 00bc2878 bytes e80000b5
- 00bc2460 ["INT_ADD", "register:40f0:8", ["const:bc2460:8", "const:4:8"]]
- 00bc2460 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2460 bytes ac610294
- 00bc2468 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1c0:8"]]
- 00bc2468 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2468 bytes 60e200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47664b52e4e06fcd85daa022adeb92b4"></a>

### [`00bc247c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc247c.md) → [`00bc28a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc28a4.md) _ZN8firebase13remote_config8internal23config_settings_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embe

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc28d0",
      "incomplete_value": true,
      "site": "00bc28d0",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc24a8",
      "incomplete_value": true,
      "site": "00bc24a8",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc28b8",
      "incomplete_value": true,
      "site": "00bc28b8",
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
      "definition_site": "00bc2490",
      "incomplete_value": true,
      "site": "00bc2490",
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
      "definition_site": "00bc28c0",
      "incomplete_value": false,
      "site": "00bc28c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:bde:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2498",
      "incomplete_value": false,
      "site": "00bc24a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:b9e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc28b4",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc28c0",
      "PARAM",
      [
        "storage",
        "002b9b9e",
        null,
        "string"
      ]
    ],
    [
      "00bc28d0",
      "WRITE",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc28b4",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc28c0",
      "PARAM",
      [
        "storage",
        "002b9bde",
        null,
        "string"
      ]
    ],
    [
      "00bc28d0",
      "WRITE",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc24a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc247c.md#insn-00bc24a0) · [`00bc24a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc247c.md#insn-00bc24a8) · [`00bc248c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc247c.md#insn-00bc248c)
- 新版 `00bc28c8`（命令位置の公開資料なし） · `00bc28d0`（命令位置の公開資料なし） · `00bc28b4`（命令位置の公開資料なし）

~~~diff
- 00bc24a0 ["INT_ADD", "register:40f0:8", ["const:bc24a0:8", "const:4:8"]]
- 00bc24a0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc28c8 ["INT_ADD", "register:40f0:8", ["const:bc28c8:8", "const:4:8"]]
+ 00bc28c8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc24a0 bytes 9c610294
+ 00bc28c8 bytes 92610294
- 00bc24a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1c0:8"]]
- 00bc24a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc28d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00bc28d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc24a8 bytes 60e200f9
+ 00bc28d0 bytes 60e202f9
- 00bc248c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1c0:8"]]
- 00bc248c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc28b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00bc28b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc248c bytes 68e240f9
+ 00bc28b4 bytes 68e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a38e03e8cc63d0f6eb58a427123df09a"></a>

### [`00bc24bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc24bc.md) → [`00bc28e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc28e4.md) _ZN8firebase13remote_config8internal23config_settings_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc24ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2914"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc28f8",
      "incomplete_value": true,
      "site": "00bc28f8",
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
      "definition_site": "00bc24d0",
      "incomplete_value": true,
      "site": "00bc24d0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc28f4",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc28f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc24f0"
      ]
    ],
    [
      "unmatched:00bc24dc",
      "PARAM",
      [
        "storage",
        "002b9b9e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc28f4",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc28f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2918"
      ]
    ],
    [
      "00bc2904",
      "PARAM",
      [
        "storage",
        "002b9bde",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc24e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc24bc.md#insn-00bc24e4) · [`00bc24ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc24bc.md#insn-00bc24ec) · [`00bc24fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc24bc.md#insn-00bc24fc)

~~~diff
- 00bc24e4 ["INT_ADD", "register:40f0:8", ["const:bc24e4:8", "const:4:8"]]
- 00bc24e4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc24e4 bytes 8b610294
- 00bc24ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1c0:8"]]
- 00bc24ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc24ec bytes 60e200f9
- 00bc24fc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc24fc ["RETURN", null, ["register:0:8"]]
- 00bc24fc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-442bcad600062728ea297ced8eeb106d"></a>

### [`00bc2500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2500.md) → [`00bc2928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2928.md) _ZN8firebase13remote_config8internal23config_settings_builder10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2530"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2958"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc293c",
      "incomplete_value": true,
      "site": "00bc293c",
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
      "definition_site": "00bc2514",
      "incomplete_value": true,
      "site": "00bc2514",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2938",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc251c",
      "PARAM",
      [
        "storage",
        "002b9b9e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc2530",
      "WRITE",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2938",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2944",
      "PARAM",
      [
        "storage",
        "002b9bde",
        null,
        "string"
      ]
    ],
    [
      "00bc2958",
      "WRITE",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2500.md#insn-00bc2528) · [`00bc2530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2500.md#insn-00bc2530)
- 新版 `00bc2950`（命令位置の公開資料なし） · `00bc2958`（命令位置の公開資料なし）

~~~diff
- 00bc2528 ["INT_ADD", "register:40f0:8", ["const:bc2528:8", "const:4:8"]]
- 00bc2528 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc2950 ["INT_ADD", "register:40f0:8", ["const:bc2950:8", "const:4:8"]]
+ 00bc2950 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2528 bytes 7a610294
+ 00bc2950 bytes 70610294
- 00bc2530 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1c0:8"]]
- 00bc2530 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2530 bytes 60e200f9
+ 00bc2958 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00bc2958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2958 bytes 60e202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e53c9ce9d985ae8bc42ae34a9c6d1d9"></a>

### [`00bc2550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2550.md) → [`00bc2978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2978.md) _ZN8firebase13remote_config8internal23config_settings_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc29d0",
      "incomplete_value": true,
      "site": "00bc29d0",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc25a8",
      "incomplete_value": true,
      "site": "00bc25a8",
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
            "const:1c8:8"
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
      "definition_site": "00bc29ac",
      "incomplete_value": true,
      "site": "00bc29b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2584",
      "incomplete_value": true,
      "site": "00bc2590",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:1c0:8"
              ]
            ]
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
      "00bc298c",
      "READ",
      [
        "storage",
        "011261c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc29ac",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc29d0",
      "WRITE",
      [
        "storage",
        "011261c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc298c",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc29ac",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc29d0",
      "WRITE",
      [
        "storage",
        "011265c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2550.md#insn-00bc2590) · [`00bc25a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2550.md#insn-00bc25a8) · [`00bc2564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2550.md#insn-00bc2564)
- 新版 `00bc29b8`（命令位置の公開資料なし） · `00bc29d0`（命令位置の公開資料なし） · `00bc298c`（命令位置の公開資料なし）

~~~diff
- 00bc2590 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2590 ["INT_ADD", "register:40f0:8", ["const:bc2590:8", "const:4:8"]]
- 00bc2590 ["CALLIND", null, ["register:0:8"]]
+ 00bc29b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc29b8 ["INT_ADD", "register:40f0:8", ["const:bc29b8:8", "const:4:8"]]
+ 00bc29b8 ["CALLIND", null, ["register:0:8"]]
- 00bc2590 bytes 00013fd6
+ 00bc29b8 bytes 00013fd6
- 00bc25a8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc25a8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1c8:8"]]
- 00bc25a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc29d0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc29d0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5c8:8"]]
+ 00bc29d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc25a8 bytes a0220739
+ 00bc29d0 bytes a0221739
- 00bc2564 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:1c8:8"]]
- 00bc2564 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bc2564 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bc298c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5c8:8"]]
+ 00bc298c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bc298c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bc2564 bytes a8224739
+ 00bc298c bytes a8225739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94c34207b05dfe5f59b8fc8b80c774ae"></a>

### [`00bc25bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc25bc.md) → [`00bc29e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc29e4.md) _ZN8firebase13remote_config8internal23config_settings_builder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 12.50% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc25f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2a20"
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
      "00bc29f8",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc29fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc261c"
      ]
    ],
    [
      "00bc2a04",
      "READ",
      [
        "storage",
        "011261c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc29f8",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc29fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2a44"
      ]
    ],
    [
      "00bc2a04",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc25d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc25bc.md#insn-00bc25d4) · [`00bc25f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc25bc.md#insn-00bc25f8) · [`00bc2600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc25bc.md#insn-00bc2600)
- 新版 `00bc29fc`（命令位置の公開資料なし）

~~~diff
- 00bc25d4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc25d4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bc29fc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc29fc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bc25d4 bytes 410200b4
+ 00bc29fc bytes 410200b4
- 00bc25f8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc25f8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc25f8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:1c8:8"]]
- 00bc25f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc25f8 bytes bf220739
- 00bc2600 ["INT_ADD", "register:40f0:8", ["const:bc2600:8", "const:4:8"]]
- 00bc2600 ["CALL", null, ["callee:00c5af60:8"]]
- 00bc2600 bytes 58610294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88b2a23c5250c25b776c664d87c0cf61"></a>

### [`00bc262c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc262c.md) → [`00bc2a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2a54.md) _ZN8firebase13remote_config8internal23config_settings_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc266c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2a94"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2648"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2640",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc2648",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2a98"
      ]
    ],
    [
      "unmatched:00bc2650",
      "PARAM",
      [
        "storage",
        "002b9b9e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2a68",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2a70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2a98"
      ]
    ],
    [
      "00bc2a78",
      "PARAM",
      [
        "storage",
        "002b9bde",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc262c.md#insn-00bc2648) · [`00bc2664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc262c.md#insn-00bc2664) · [`00bc266c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc262c.md#insn-00bc266c)
- 新版 `00bc2a8c`（命令位置の公開資料なし）

~~~diff
- 00bc2648 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc2648 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc2648 bytes 410100b5
- 00bc2664 ["INT_ADD", "register:40f0:8", ["const:bc2664:8", "const:4:8"]]
- 00bc2664 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc2a8c ["INT_ADD", "register:40f0:8", ["const:bc2a8c:8", "const:4:8"]]
+ 00bc2a8c ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2664 bytes 2b610294
+ 00bc2a8c bytes 21610294
- 00bc266c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1c0:8"]]
- 00bc266c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc266c bytes 80e200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10ef5c1a0ea6f9c47e57a389774bc758"></a>

### [`00bc26d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc26d8.md) → [`00bc2b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2b00.md) _ZN8firebase13remote_config8internal23config_settings_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2b40",
      "incomplete_value": true,
      "site": "00bc2b40",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2718",
      "incomplete_value": true,
      "site": "00bc2718",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2b1c",
      "incomplete_value": true,
      "site": "00bc2b1c",
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
      "definition_site": "00bc26f4",
      "incomplete_value": true,
      "site": "00bc26f4",
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
      "definition_site": "00bc2b24",
      "incomplete_value": false,
      "site": "00bc2b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:bde:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc26fc",
      "incomplete_value": false,
      "site": "00bc2710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:b9e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2b14",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2b24",
      "PARAM",
      [
        "storage",
        "002b9b9e",
        null,
        "string"
      ]
    ],
    [
      "00bc2b40",
      "WRITE",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2b14",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2b24",
      "PARAM",
      [
        "storage",
        "002b9bde",
        null,
        "string"
      ]
    ],
    [
      "00bc2b40",
      "WRITE",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc26d8.md#insn-00bc2710) · [`00bc2718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc26d8.md#insn-00bc2718) · [`00bc26ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc26d8.md#insn-00bc26ec)
- 新版 `00bc2b38`（命令位置の公開資料なし） · `00bc2b40`（命令位置の公開資料なし） · `00bc2b14`（命令位置の公開資料なし）

~~~diff
- 00bc2710 ["INT_ADD", "register:40f0:8", ["const:bc2710:8", "const:4:8"]]
- 00bc2710 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc2b38 ["INT_ADD", "register:40f0:8", ["const:bc2b38:8", "const:4:8"]]
+ 00bc2b38 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2710 bytes 00610294
+ 00bc2b38 bytes f6600294
- 00bc2718 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1c0:8"]]
- 00bc2718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2b40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00bc2b40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2718 bytes 80e200f9
+ 00bc2b40 bytes 80e202f9
- 00bc26ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1c0:8"]]
- 00bc26ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2b14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00bc2b14 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc26ec bytes 81e240f9
+ 00bc2b14 bytes 81e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-997e2e03786830e0b8609809df5c7961"></a>

### [`00bc2784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2784.md) → [`00bc2bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2bac.md) _ZN8firebase13remote_config8internal22custom_signals_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embed

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2784"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2788"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2788"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2784",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc2788",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2bbc",
      "READ",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2bac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc2bb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2bbc",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2784.md#insn-00bc2784) · [`00bc2788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2784.md#insn-00bc2788) · [`00bc2798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2784.md#insn-00bc2798)
- 新版 `00bc2bc0`（命令位置の公開資料なし）

~~~diff
- 00bc2784 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc2784 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc2784 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc2784 bytes f30f1ef8
- 00bc2788 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc2788 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc2788 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc2788 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc2788 bytes fd7b01a9
- 00bc2798 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc2798 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc2bc0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc2bc0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc2798 bytes e80000b5
+ 00bc2bc0 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-337b797adef621c3b72fd8f84bc64130"></a>

### [`00bc27c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc27c4.md) → [`00bc2bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2bec.md) _ZN8firebase13remote_config8internal22custom_signals_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embed

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2c18",
      "incomplete_value": true,
      "site": "00bc2c18",
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
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc27f0",
      "incomplete_value": true,
      "site": "00bc27f0",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2c00",
      "incomplete_value": true,
      "site": "00bc2c00",
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
      "definition_site": "00bc27d8",
      "incomplete_value": true,
      "site": "00bc27d8",
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
      "definition_site": "00bc2c08",
      "incomplete_value": false,
      "site": "00bc2c10",
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
            "const:3eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc27e0",
      "incomplete_value": false,
      "site": "00bc27e8",
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
            "const:3ab:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2bfc",
      "READ",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2c08",
      "PARAM",
      [
        "storage",
        "002ae3ab",
        null,
        "string"
      ]
    ],
    [
      "00bc2c18",
      "WRITE",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2bfc",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2c08",
      "PARAM",
      [
        "storage",
        "002ae3eb",
        null,
        "string"
      ]
    ],
    [
      "00bc2c18",
      "WRITE",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc27e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc27c4.md#insn-00bc27e8) · [`00bc27f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc27c4.md#insn-00bc27f0) · [`00bc27d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc27c4.md#insn-00bc27d4)
- 新版 `00bc2c10`（命令位置の公開資料なし） · `00bc2c18`（命令位置の公開資料なし） · `00bc2bfc`（命令位置の公開資料なし）

~~~diff
- 00bc27e8 ["INT_ADD", "register:40f0:8", ["const:bc27e8:8", "const:4:8"]]
- 00bc27e8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc2c10 ["INT_ADD", "register:40f0:8", ["const:bc2c10:8", "const:4:8"]]
+ 00bc2c10 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc27e8 bytes ca600294
+ 00bc2c10 bytes c0600294
- 00bc27f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1f8:8"]]
- 00bc27f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2c18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5f8:8"]]
+ 00bc2c18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc27f0 bytes 60fe00f9
+ 00bc2c18 bytes 60fe02f9
- 00bc27d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1f8:8"]]
- 00bc27d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2bfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5f8:8"]]
+ 00bc2bfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc27d4 bytes 68fe40f9
+ 00bc2bfc bytes 68fe42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b7b4f4cf95990b7b1743708829a9247"></a>

### [`00bc2804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2804.md) → [`00bc2c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2c2c.md) _ZN8firebase13remote_config8internal22custom_signals_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2c5c",
      "incomplete_value": true,
      "site": "00bc2c5c",
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
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2834",
      "incomplete_value": true,
      "site": "00bc2834",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2c40",
      "incomplete_value": true,
      "site": "00bc2c40",
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
      "definition_site": "00bc2818",
      "incomplete_value": true,
      "site": "00bc2818",
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
      "definition_site": "00bc2c4c",
      "incomplete_value": false,
      "site": "00bc2c54",
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
            "const:3eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2824",
      "incomplete_value": false,
      "site": "00bc282c",
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
            "const:3ab:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2c3c",
      "READ",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2c4c",
      "PARAM",
      [
        "storage",
        "002ae3ab",
        null,
        "string"
      ]
    ],
    [
      "00bc2c5c",
      "WRITE",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2c3c",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2c4c",
      "PARAM",
      [
        "storage",
        "002ae3eb",
        null,
        "string"
      ]
    ],
    [
      "00bc2c5c",
      "WRITE",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc282c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2804.md#insn-00bc282c) · [`00bc2834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2804.md#insn-00bc2834) · [`00bc2814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2804.md#insn-00bc2814)
- 新版 `00bc2c54`（命令位置の公開資料なし） · `00bc2c5c`（命令位置の公開資料なし） · `00bc2c3c`（命令位置の公開資料なし）

~~~diff
- 00bc282c ["INT_ADD", "register:40f0:8", ["const:bc282c:8", "const:4:8"]]
- 00bc282c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc2c54 ["INT_ADD", "register:40f0:8", ["const:bc2c54:8", "const:4:8"]]
+ 00bc2c54 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc282c bytes b9600294
+ 00bc2c54 bytes af600294
- 00bc2834 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1f8:8"]]
- 00bc2834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2c5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5f8:8"]]
+ 00bc2c5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2834 bytes 60fe00f9
+ 00bc2c5c bytes 60fe02f9
- 00bc2814 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1f8:8"]]
- 00bc2814 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2c3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5f8:8"]]
+ 00bc2c3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2814 bytes 68fe40f9
+ 00bc2c3c bytes 68fe42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebf6f7fe65a19166dbb144f9f2da87f6"></a>

### [`00bc2848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2848.md) → [`00bc2c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2c70.md) _ZN8firebase13remote_config8internal22custom_signals_builder10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2ca0",
      "incomplete_value": true,
      "site": "00bc2ca0",
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
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2878",
      "incomplete_value": true,
      "site": "00bc2878",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2c84",
      "incomplete_value": true,
      "site": "00bc2c84",
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
      "definition_site": "00bc285c",
      "incomplete_value": true,
      "site": "00bc285c",
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
      "definition_site": "00bc2c8c",
      "incomplete_value": false,
      "site": "00bc2c98",
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
            "const:3eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2864",
      "incomplete_value": false,
      "site": "00bc2870",
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
            "const:3ab:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2c80",
      "READ",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2c8c",
      "PARAM",
      [
        "storage",
        "002ae3ab",
        null,
        "string"
      ]
    ],
    [
      "00bc2ca0",
      "WRITE",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2c80",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2c8c",
      "PARAM",
      [
        "storage",
        "002ae3eb",
        null,
        "string"
      ]
    ],
    [
      "00bc2ca0",
      "WRITE",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2848.md#insn-00bc2870) · [`00bc2878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2848.md#insn-00bc2878) · [`00bc2858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2848.md#insn-00bc2858)
- 新版 `00bc2c98`（命令位置の公開資料なし） · `00bc2ca0`（命令位置の公開資料なし） · `00bc2c80`（命令位置の公開資料なし）

~~~diff
- 00bc2870 ["INT_ADD", "register:40f0:8", ["const:bc2870:8", "const:4:8"]]
- 00bc2870 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc2c98 ["INT_ADD", "register:40f0:8", ["const:bc2c98:8", "const:4:8"]]
+ 00bc2c98 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2870 bytes a8600294
+ 00bc2c98 bytes 9e600294
- 00bc2878 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1f8:8"]]
- 00bc2878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2ca0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5f8:8"]]
+ 00bc2ca0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2878 bytes 60fe00f9
+ 00bc2ca0 bytes 60fe02f9
- 00bc2858 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1f8:8"]]
- 00bc2858 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2c80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5f8:8"]]
+ 00bc2c80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2858 bytes 68fe40f9
+ 00bc2c80 bytes 68fe42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e7978aaa9e8fd299381a6cf7c105389"></a>

### [`00bc2898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2898.md) → [`00bc2cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2cc0.md) _ZN8firebase13remote_config8internal22custom_signals_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2d18",
      "incomplete_value": true,
      "site": "00bc2d18",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc28f0",
      "incomplete_value": true,
      "site": "00bc28f0",
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
            "const:200:8"
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
      "definition_site": "00bc2cf4",
      "incomplete_value": true,
      "site": "00bc2d00",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:5f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc28cc",
      "incomplete_value": true,
      "site": "00bc28d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:1f8:8"
              ]
            ]
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
      "00bc2cd4",
      "READ",
      [
        "storage",
        "01126200",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2cf4",
      "READ",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2d18",
      "WRITE",
      [
        "storage",
        "01126200",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2cd4",
      "READ",
      [
        "storage",
        "01126600",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2cf4",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2d18",
      "WRITE",
      [
        "storage",
        "01126600",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc28d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2898.md#insn-00bc28d8) · [`00bc28f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2898.md#insn-00bc28f0) · [`00bc28ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2898.md#insn-00bc28ac)
- 新版 `00bc2d00`（命令位置の公開資料なし） · `00bc2d18`（命令位置の公開資料なし） · `00bc2cd4`（命令位置の公開資料なし）

~~~diff
- 00bc28d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc28d8 ["INT_ADD", "register:40f0:8", ["const:bc28d8:8", "const:4:8"]]
- 00bc28d8 ["CALLIND", null, ["register:0:8"]]
+ 00bc2d00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2d00 ["INT_ADD", "register:40f0:8", ["const:bc2d00:8", "const:4:8"]]
+ 00bc2d00 ["CALLIND", null, ["register:0:8"]]
- 00bc28d8 bytes 00013fd6
+ 00bc2d00 bytes 00013fd6
- 00bc28f0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc28f0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:200:8"]]
- 00bc28f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc2d18 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc2d18 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:600:8"]]
+ 00bc2d18 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc28f0 bytes a0020839
+ 00bc2d18 bytes a0021839
- 00bc28ac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:200:8"]]
- 00bc28ac ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bc28ac ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bc2cd4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:600:8"]]
+ 00bc2cd4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2cd4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bc28ac bytes a8024839
+ 00bc2cd4 bytes a8025839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-734468b3e04bbf383e9feb3f08a8bace"></a>

### [`00bc2904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2904.md) → [`00bc2d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2d2c.md) _ZN8firebase13remote_config8internal22custom_signals_builder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2d68",
      "incomplete_value": true,
      "site": "00bc2d68",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2940",
      "incomplete_value": true,
      "site": "00bc2940",
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
            "const:200:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2d88",
      "incomplete_value": true,
      "site": "00bc2d88",
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
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2960",
      "incomplete_value": true,
      "site": "00bc2960",
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
            "const:1f8:8"
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
      "definition_site": "00bc2d44",
      "incomplete_value": true,
      "site": "00bc2d44",
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
      "definition_site": "00bc291c",
      "incomplete_value": true,
      "site": "00bc291c",
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
      "00bc2d40",
      "READ",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2d4c",
      "READ",
      [
        "storage",
        "01126200",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2d68",
      "WRITE",
      [
        "storage",
        "01126200",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2d40",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2d4c",
      "READ",
      [
        "storage",
        "01126600",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2d68",
      "WRITE",
      [
        "storage",
        "01126600",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2904.md#insn-00bc2940) · [`00bc295c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2904.md#insn-00bc295c) · [`00bc2960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2904.md#insn-00bc2960)
- 新版 `00bc2d68`（命令位置の公開資料なし） · `00bc2d84`（命令位置の公開資料なし） · `00bc2d88`（命令位置の公開資料なし）

~~~diff
- 00bc2940 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc2940 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc2940 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:200:8"]]
- 00bc2940 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bc2d68 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bc2d68 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bc2d68 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:600:8"]]
+ 00bc2d68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc2940 bytes bf020839
+ 00bc2d68 bytes bf021839
- 00bc295c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc295c ["INT_ADD", "register:40f0:8", ["const:bc295c:8", "const:4:8"]]
- 00bc295c ["CALLIND", null, ["register:0:8"]]
+ 00bc2d84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2d84 ["INT_ADD", "register:40f0:8", ["const:bc2d84:8", "const:4:8"]]
+ 00bc2d84 ["CALLIND", null, ["register:0:8"]]
- 00bc295c bytes 00013fd6
+ 00bc2d84 bytes 00013fd6
- 00bc2960 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1f8:8"]]
- 00bc2960 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bc2960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bc2d88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5f8:8"]]
+ 00bc2d88 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bc2d88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bc2960 bytes 9ffe00f9
+ 00bc2d88 bytes 9ffe02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9c392abcc62105eed24d1f9ab1b944"></a>

### [`00bc2974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2974.md) → [`00bc2d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2d9c.md) _ZN8firebase13remote_config8internal22custom_signals_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc29b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2ddc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2990"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2988",
      "READ",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc2990",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2de0"
      ]
    ],
    [
      "unmatched:00bc2998",
      "PARAM",
      [
        "storage",
        "002ae3ab",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2db0",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2db8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2de0"
      ]
    ],
    [
      "00bc2dc0",
      "PARAM",
      [
        "storage",
        "002ae3eb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2974.md#insn-00bc2990) · [`00bc29ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2974.md#insn-00bc29ac) · [`00bc29b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2974.md#insn-00bc29b4)
- 新版 `00bc2dd4`（命令位置の公開資料なし）

~~~diff
- 00bc2990 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc2990 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc2990 bytes 410100b5
- 00bc29ac ["INT_ADD", "register:40f0:8", ["const:bc29ac:8", "const:4:8"]]
- 00bc29ac ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc2dd4 ["INT_ADD", "register:40f0:8", ["const:bc2dd4:8", "const:4:8"]]
+ 00bc2dd4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc29ac bytes 59600294
+ 00bc2dd4 bytes 4f600294
- 00bc29b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1f8:8"]]
- 00bc29b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc29b4 bytes 80fe00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e88c2510a35f3aae5660f6d1d43c6a1"></a>

### [`00bc29e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc29e4.md) → [`00bc2e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2e0c.md) _ZN8firebase13remote_config8internal22custom_signals_builder11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc2e28",
      "incomplete_value": false,
      "site": "00bc2e2c",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2a00",
      "incomplete_value": false,
      "site": "00bc2a04",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc2e38",
      "incomplete_value": true,
      "site": "00bc2e44",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2a10",
      "incomplete_value": true,
      "site": "00bc2a1c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00bc2e28",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bc2e38",
      "DATA",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2e28",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc2e38",
      "DATA",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc29e4.md#insn-00bc2a04) · [`00bc2a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc29e4.md#insn-00bc2a00) · [`00bc2a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc29e4.md#insn-00bc2a0c)
- 新版 `00bc2e2c`（命令位置の公開資料なし） · `00bc2e28`（命令位置の公開資料なし） · `00bc2e34`（命令位置の公開資料なし）

~~~diff
- 00bc2a04 ["INT_ADD", "register:40f0:8", ["const:bc2a04:8", "const:4:8"]]
- 00bc2a04 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc2e2c ["INT_ADD", "register:40f0:8", ["const:bc2e2c:8", "const:4:8"]]
+ 00bc2e2c ["CALL", null, ["callee:00c5b000:8"]]
- 00bc2a04 bytes 7f600294
+ 00bc2e2c bytes 75600294
- 00bc2a00 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bc2a00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2a00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2a00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc2e28 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bc2e28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2e28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2e28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc2a00 bytes 00680a91
+ 00bc2e28 bytes 009c0d91
- 00bc2a0c ["COPY", "tmp:0:8", ["const:208:8"]]
- 00bc2a0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2a0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2a0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc2e34 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 00bc2e34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2e34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2e34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc2a0c bytes 08210891
+ 00bc2e34 bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef11ac9a6d515b8d7181b9d62df2aabc"></a>

### [`00bc2a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2a20.md) → [`00bc2e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2e48.md) _ZN8firebase13remote_config8internal22custom_signals_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2e88",
      "incomplete_value": true,
      "site": "00bc2e88",
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
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2a60",
      "incomplete_value": true,
      "site": "00bc2a60",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2e64",
      "incomplete_value": true,
      "site": "00bc2e64",
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
      "definition_site": "00bc2a3c",
      "incomplete_value": true,
      "site": "00bc2a3c",
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
      "definition_site": "00bc2e6c",
      "incomplete_value": false,
      "site": "00bc2e80",
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
            "const:3eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2a44",
      "incomplete_value": false,
      "site": "00bc2a58",
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
            "const:3ab:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2e5c",
      "READ",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2e6c",
      "PARAM",
      [
        "storage",
        "002ae3ab",
        null,
        "string"
      ]
    ],
    [
      "00bc2e88",
      "WRITE",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2e5c",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2e6c",
      "PARAM",
      [
        "storage",
        "002ae3eb",
        null,
        "string"
      ]
    ],
    [
      "00bc2e88",
      "WRITE",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2a20.md#insn-00bc2a58) · [`00bc2a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2a20.md#insn-00bc2a60) · [`00bc2a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2a20.md#insn-00bc2a34)
- 新版 `00bc2e80`（命令位置の公開資料なし） · `00bc2e88`（命令位置の公開資料なし） · `00bc2e5c`（命令位置の公開資料なし）

~~~diff
- 00bc2a58 ["INT_ADD", "register:40f0:8", ["const:bc2a58:8", "const:4:8"]]
- 00bc2a58 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc2e80 ["INT_ADD", "register:40f0:8", ["const:bc2e80:8", "const:4:8"]]
+ 00bc2e80 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2a58 bytes 2e600294
+ 00bc2e80 bytes 24600294
- 00bc2a60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1f8:8"]]
- 00bc2a60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2e88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5f8:8"]]
+ 00bc2e88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2a60 bytes 80fe00f9
+ 00bc2e88 bytes 80fe02f9
- 00bc2a34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1f8:8"]]
- 00bc2a34 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2e5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5f8:8"]]
+ 00bc2e5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2a34 bytes 81fe40f9
+ 00bc2e5c bytes 81fe42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fbce2d2ba85bd1cec15f3d67e065705"></a>

### [`00bc2a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2a90.md) → [`00bc2eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2eb8.md) _ZN8firebase13remote_config8internal22custom_signals_builder10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc2ed4",
      "incomplete_value": false,
      "site": "00bc2ed8",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2aac",
      "incomplete_value": false,
      "site": "00bc2ab0",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc2ee4",
      "incomplete_value": true,
      "site": "00bc2ef0",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2abc",
      "incomplete_value": true,
      "site": "00bc2ac8",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00bc2ed4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bc2ee4",
      "DATA",
      [
        "storage",
        "01126230",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc2ed4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bc2ee4",
      "DATA",
      [
        "storage",
        "01126630",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2a90.md#insn-00bc2ab0) · [`00bc2aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2a90.md#insn-00bc2aac) · [`00bc2ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2a90.md#insn-00bc2ab8)
- 新版 `00bc2ed8`（命令位置の公開資料なし） · `00bc2ed4`（命令位置の公開資料なし） · `00bc2ee0`（命令位置の公開資料なし）

~~~diff
- 00bc2ab0 ["INT_ADD", "register:40f0:8", ["const:bc2ab0:8", "const:4:8"]]
- 00bc2ab0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc2ed8 ["INT_ADD", "register:40f0:8", ["const:bc2ed8:8", "const:4:8"]]
+ 00bc2ed8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc2ab0 bytes 54600294
+ 00bc2ed8 bytes 4a600294
- 00bc2aac ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bc2aac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2aac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2aac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc2ed4 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bc2ed4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2ed4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2ed4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc2aac bytes 00441191
+ 00bc2ed4 bytes 00781491
- 00bc2ab8 ["COPY", "tmp:0:8", ["const:230:8"]]
- 00bc2ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc2ee0 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00bc2ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc2ab8 bytes 08c10891
+ 00bc2ee0 bytes 08c11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-707808178157a1a2935557119ca39f71"></a>

### [`00bc2acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2acc.md) → [`00bc2ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2ef4.md) _ZN8firebase13remote_config8internal19throttled_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embedded

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2af8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2f20"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2f08",
      "incomplete_value": true,
      "site": "00bc2f08",
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
      "definition_site": "00bc2ae0",
      "incomplete_value": true,
      "site": "00bc2ae0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2f04",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2f08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc2afc"
      ]
    ],
    [
      "unmatched:00bc2aec",
      "PARAM",
      [
        "storage",
        "002b9be8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2f04",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2f08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2f24"
      ]
    ],
    [
      "00bc2f14",
      "PARAM",
      [
        "storage",
        "002b9c28",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2acc.md#insn-00bc2ae0) · [`00bc2af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2acc.md#insn-00bc2af0) · [`00bc2af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2acc.md#insn-00bc2af8)
- 新版 `00bc2f08`（命令位置の公開資料なし）

~~~diff
- 00bc2ae0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc2ae0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc2f08 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc2f08 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bc2ae0 bytes e80000b5
+ 00bc2f08 bytes e80000b5
- 00bc2af0 ["INT_ADD", "register:40f0:8", ["const:bc2af0:8", "const:4:8"]]
- 00bc2af0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2af0 bytes 08600294
- 00bc2af8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:238:8"]]
- 00bc2af8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2af8 bytes 601e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f160ebd897c145c0190da49b21656c98"></a>

### [`00bc2b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b0c.md) → [`00bc2f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2f34.md) _ZN8firebase13remote_config8internal19throttled_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embedded

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2b0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2b10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2b10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2b0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc2b10",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2f44",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2f34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc2f38",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2f44",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b0c.md#insn-00bc2b0c) · [`00bc2b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b0c.md#insn-00bc2b10) · [`00bc2b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b0c.md#insn-00bc2b20)
- 新版 `00bc2f48`（命令位置の公開資料なし）

~~~diff
- 00bc2b0c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc2b0c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc2b0c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc2b0c bytes f30f1ef8
- 00bc2b10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc2b10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc2b10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc2b10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc2b10 bytes fd7b01a9
- 00bc2b20 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc2b20 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc2f48 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc2f48 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bc2b20 bytes e80000b5
+ 00bc2f48 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b1a0ee3e2f31f3e377c7fb353ac6c19"></a>

### [`00bc2b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b4c.md) → [`00bc2f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2f74.md) _ZN8firebase13remote_config8internal19throttled_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2fa4",
      "incomplete_value": true,
      "site": "00bc2fa4",
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
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2b7c",
      "incomplete_value": true,
      "site": "00bc2b7c",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2f88",
      "incomplete_value": true,
      "site": "00bc2f88",
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
      "definition_site": "00bc2b60",
      "incomplete_value": true,
      "site": "00bc2b60",
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
      "definition_site": "00bc2f94",
      "incomplete_value": false,
      "site": "00bc2f9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2b6c",
      "incomplete_value": false,
      "site": "00bc2b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2f84",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2f94",
      "PARAM",
      [
        "storage",
        "002b9be8",
        null,
        "string"
      ]
    ],
    [
      "00bc2fa4",
      "WRITE",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2f84",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2f94",
      "PARAM",
      [
        "storage",
        "002b9c28",
        null,
        "string"
      ]
    ],
    [
      "00bc2fa4",
      "WRITE",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b4c.md#insn-00bc2b74) · [`00bc2b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b4c.md#insn-00bc2b7c) · [`00bc2b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b4c.md#insn-00bc2b5c)
- 新版 `00bc2f9c`（命令位置の公開資料なし） · `00bc2fa4`（命令位置の公開資料なし） · `00bc2f84`（命令位置の公開資料なし）

~~~diff
- 00bc2b74 ["INT_ADD", "register:40f0:8", ["const:bc2b74:8", "const:4:8"]]
- 00bc2b74 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc2f9c ["INT_ADD", "register:40f0:8", ["const:bc2f9c:8", "const:4:8"]]
+ 00bc2f9c ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2b74 bytes e75f0294
+ 00bc2f9c bytes dd5f0294
- 00bc2b7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:238:8"]]
- 00bc2b7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2fa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:638:8"]]
+ 00bc2fa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2b7c bytes 601e01f9
+ 00bc2fa4 bytes 601e03f9
- 00bc2b5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:238:8"]]
- 00bc2b5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2f84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:638:8"]]
+ 00bc2f84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2b5c bytes 681e41f9
+ 00bc2f84 bytes 681e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-637d663a692d86b11eccf6c9ea920d75"></a>

### [`00bc2b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b90.md) → [`00bc2fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2fb8.md) _ZN8firebase13remote_config8internal19throttled_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2fe8",
      "incomplete_value": true,
      "site": "00bc2fe8",
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
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2bc0",
      "incomplete_value": true,
      "site": "00bc2bc0",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2fcc",
      "incomplete_value": true,
      "site": "00bc2fcc",
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
      "definition_site": "00bc2ba4",
      "incomplete_value": true,
      "site": "00bc2ba4",
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
      "definition_site": "00bc2fd4",
      "incomplete_value": false,
      "site": "00bc2fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2bac",
      "incomplete_value": false,
      "site": "00bc2bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2fc8",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2fd4",
      "PARAM",
      [
        "storage",
        "002b9be8",
        null,
        "string"
      ]
    ],
    [
      "00bc2fe8",
      "WRITE",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2fc8",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2fd4",
      "PARAM",
      [
        "storage",
        "002b9c28",
        null,
        "string"
      ]
    ],
    [
      "00bc2fe8",
      "WRITE",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b90.md#insn-00bc2bb8) · [`00bc2bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b90.md#insn-00bc2bc0) · [`00bc2ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b90.md#insn-00bc2ba0)
- 新版 `00bc2fe0`（命令位置の公開資料なし） · `00bc2fe8`（命令位置の公開資料なし） · `00bc2fc8`（命令位置の公開資料なし）

~~~diff
- 00bc2bb8 ["INT_ADD", "register:40f0:8", ["const:bc2bb8:8", "const:4:8"]]
- 00bc2bb8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc2fe0 ["INT_ADD", "register:40f0:8", ["const:bc2fe0:8", "const:4:8"]]
+ 00bc2fe0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2bb8 bytes d65f0294
+ 00bc2fe0 bytes cc5f0294
- 00bc2bc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:238:8"]]
- 00bc2bc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2fe8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:638:8"]]
+ 00bc2fe8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2bc0 bytes 601e01f9
+ 00bc2fe8 bytes 601e03f9
- 00bc2ba0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:238:8"]]
- 00bc2ba0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2fc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:638:8"]]
+ 00bc2fc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2ba0 bytes 681e41f9
+ 00bc2fc8 bytes 681e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19daf642a1917ba5a033c0bbc6f65ae3"></a>

### [`00bc2be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2be0.md) → [`00bc3008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3008.md) _ZN8firebase13remote_config8internal19throttled_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc3060",
      "incomplete_value": true,
      "site": "00bc3060",
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
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2c38",
      "incomplete_value": true,
      "site": "00bc2c38",
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
            "const:240:8"
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
      "definition_site": "00bc303c",
      "incomplete_value": true,
      "site": "00bc3048",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:638:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2c14",
      "incomplete_value": true,
      "site": "00bc2c20",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:238:8"
              ]
            ]
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
      "00bc301c",
      "READ",
      [
        "storage",
        "01126240",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc303c",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3060",
      "WRITE",
      [
        "storage",
        "01126240",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc301c",
      "READ",
      [
        "storage",
        "01126640",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc303c",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3060",
      "WRITE",
      [
        "storage",
        "01126640",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2be0.md#insn-00bc2c20) · [`00bc2c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2be0.md#insn-00bc2c38) · [`00bc2bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2be0.md#insn-00bc2bf4)
- 新版 `00bc3048`（命令位置の公開資料なし） · `00bc3060`（命令位置の公開資料なし） · `00bc301c`（命令位置の公開資料なし）

~~~diff
- 00bc2c20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2c20 ["INT_ADD", "register:40f0:8", ["const:bc2c20:8", "const:4:8"]]
- 00bc2c20 ["CALLIND", null, ["register:0:8"]]
+ 00bc3048 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc3048 ["INT_ADD", "register:40f0:8", ["const:bc3048:8", "const:4:8"]]
+ 00bc3048 ["CALLIND", null, ["register:0:8"]]
- 00bc2c20 bytes 00013fd6
+ 00bc3048 bytes 00013fd6
- 00bc2c38 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc2c38 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:240:8"]]
- 00bc2c38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc3060 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc3060 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:640:8"]]
+ 00bc3060 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc2c38 bytes a0020939
+ 00bc3060 bytes a0021939
- 00bc2bf4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:240:8"]]
- 00bc2bf4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bc2bf4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bc301c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:640:8"]]
+ 00bc301c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bc301c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bc2bf4 bytes a8024939
+ 00bc301c bytes a8025939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6649b73799c80e73212d8b20a066f53"></a>

### [`00bc2c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2c4c.md) → [`00bc3074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3074.md) _ZN8firebase13remote_config8internal19throttled_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc30b0",
      "incomplete_value": true,
      "site": "00bc30b0",
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
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2c88",
      "incomplete_value": true,
      "site": "00bc2c88",
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
            "const:240:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc30d0",
      "incomplete_value": true,
      "site": "00bc30d0",
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
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2ca8",
      "incomplete_value": true,
      "site": "00bc2ca8",
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
            "const:238:8"
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
      "definition_site": "00bc308c",
      "incomplete_value": true,
      "site": "00bc308c",
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
      "definition_site": "00bc2c64",
      "incomplete_value": true,
      "site": "00bc2c64",
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
      "00bc3088",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3094",
      "READ",
      [
        "storage",
        "01126240",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc30b0",
      "WRITE",
      [
        "storage",
        "01126240",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc3088",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3094",
      "READ",
      [
        "storage",
        "01126640",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc30b0",
      "WRITE",
      [
        "storage",
        "01126640",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2c4c.md#insn-00bc2c88) · [`00bc2ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2c4c.md#insn-00bc2ca4) · [`00bc2ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2c4c.md#insn-00bc2ca8)
- 新版 `00bc30b0`（命令位置の公開資料なし） · `00bc30cc`（命令位置の公開資料なし） · `00bc30d0`（命令位置の公開資料なし）

~~~diff
- 00bc2c88 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc2c88 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc2c88 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:240:8"]]
- 00bc2c88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bc30b0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bc30b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bc30b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:640:8"]]
+ 00bc30b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc2c88 bytes bf020939
+ 00bc30b0 bytes bf021939
- 00bc2ca4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2ca4 ["INT_ADD", "register:40f0:8", ["const:bc2ca4:8", "const:4:8"]]
- 00bc2ca4 ["CALLIND", null, ["register:0:8"]]
+ 00bc30cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc30cc ["INT_ADD", "register:40f0:8", ["const:bc30cc:8", "const:4:8"]]
+ 00bc30cc ["CALLIND", null, ["register:0:8"]]
- 00bc2ca4 bytes 00013fd6
+ 00bc30cc bytes 00013fd6
- 00bc2ca8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:238:8"]]
- 00bc2ca8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bc2ca8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bc30d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:638:8"]]
+ 00bc30d0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bc30d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bc2ca8 bytes 9f1e01f9
+ 00bc30d0 bytes 9f1e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a00077019e23bbaeded8cc03fd033ea"></a>

### [`00bc2cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2cbc.md) → [`00bc30e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc30e4.md) _ZN8firebase13remote_config8internal19throttled_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2cfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3124"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2cd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2cd0",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc2cd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3128"
      ]
    ],
    [
      "unmatched:00bc2ce0",
      "PARAM",
      [
        "storage",
        "002b9be8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc30f8",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3100",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3128"
      ]
    ],
    [
      "00bc3108",
      "PARAM",
      [
        "storage",
        "002b9c28",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2cbc.md#insn-00bc2cd8) · [`00bc2cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2cbc.md#insn-00bc2cf4) · [`00bc2cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2cbc.md#insn-00bc2cfc)
- 新版 `00bc311c`（命令位置の公開資料なし）

~~~diff
- 00bc2cd8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc2cd8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc2cd8 bytes 410100b5
- 00bc2cf4 ["INT_ADD", "register:40f0:8", ["const:bc2cf4:8", "const:4:8"]]
- 00bc2cf4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc311c ["INT_ADD", "register:40f0:8", ["const:bc311c:8", "const:4:8"]]
+ 00bc311c ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2cf4 bytes 875f0294
+ 00bc311c bytes 7d5f0294
- 00bc2cfc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:238:8"]]
- 00bc2cfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2cfc bytes 801e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5c7e1293d163706f4d1eb310fb5e0fd"></a>

### [`00bc2d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2d68.md) → [`00bc3190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3190.md) _ZN8firebase13remote_config8internal19throttled_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc31d0",
      "incomplete_value": true,
      "site": "00bc31d0",
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
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2da8",
      "incomplete_value": true,
      "site": "00bc2da8",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc31ac",
      "incomplete_value": true,
      "site": "00bc31ac",
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
      "definition_site": "00bc2d84",
      "incomplete_value": true,
      "site": "00bc2d84",
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
      "definition_site": "00bc31b4",
      "incomplete_value": false,
      "site": "00bc31c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2d8c",
      "incomplete_value": false,
      "site": "00bc2da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc31a4",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc31b4",
      "PARAM",
      [
        "storage",
        "002b9be8",
        null,
        "string"
      ]
    ],
    [
      "00bc31d0",
      "WRITE",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc31a4",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc31b4",
      "PARAM",
      [
        "storage",
        "002b9c28",
        null,
        "string"
      ]
    ],
    [
      "00bc31d0",
      "WRITE",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2d68.md#insn-00bc2da0) · [`00bc2da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2d68.md#insn-00bc2da8) · [`00bc2d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2d68.md#insn-00bc2d7c)
- 新版 `00bc31c8`（命令位置の公開資料なし） · `00bc31d0`（命令位置の公開資料なし） · `00bc31a4`（命令位置の公開資料なし）

~~~diff
- 00bc2da0 ["INT_ADD", "register:40f0:8", ["const:bc2da0:8", "const:4:8"]]
- 00bc2da0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc31c8 ["INT_ADD", "register:40f0:8", ["const:bc31c8:8", "const:4:8"]]
+ 00bc31c8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2da0 bytes 5c5f0294
+ 00bc31c8 bytes 525f0294
- 00bc2da8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:238:8"]]
- 00bc2da8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc31d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:638:8"]]
+ 00bc31d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2da8 bytes 801e01f9
+ 00bc31d0 bytes 801e03f9
- 00bc2d7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:238:8"]]
- 00bc2d7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc31a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:638:8"]]
+ 00bc31a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2d7c bytes 811e41f9
+ 00bc31a4 bytes 811e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c79c1aa7240471d6670cea2f7dc4068e"></a>

### [`00bc2dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2dd8.md) → [`00bc3200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3200.md) _ZN8firebase13remote_config8internal19throttled_exception10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc321c",
      "incomplete_value": false,
      "site": "00bc3220",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2df4",
      "incomplete_value": false,
      "site": "00bc2df8",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc322c",
      "incomplete_value": true,
      "site": "00bc3238",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2e04",
      "incomplete_value": true,
      "site": "00bc2e10",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00bc321c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bc322c",
      "DATA",
      [
        "storage",
        "01126250",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc321c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bc322c",
      "DATA",
      [
        "storage",
        "01126650",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2dd8.md#insn-00bc2df8) · [`00bc2df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2dd8.md#insn-00bc2df4) · [`00bc2e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2dd8.md#insn-00bc2e00)
- 新版 `00bc3220`（命令位置の公開資料なし） · `00bc321c`（命令位置の公開資料なし） · `00bc3228`（命令位置の公開資料なし）

~~~diff
- 00bc2df8 ["INT_ADD", "register:40f0:8", ["const:bc2df8:8", "const:4:8"]]
- 00bc2df8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc3220 ["INT_ADD", "register:40f0:8", ["const:bc3220:8", "const:4:8"]]
+ 00bc3220 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc2df8 bytes 825f0294
+ 00bc3220 bytes 785f0294
- 00bc2df4 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bc2df4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2df4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2df4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc321c ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bc321c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc321c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc321c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc2df4 bytes 00441191
+ 00bc321c bytes 00781491
- 00bc2e00 ["COPY", "tmp:0:8", ["const:250:8"]]
- 00bc2e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc3228 ["COPY", "tmp:0:8", ["const:650:8"]]
+ 00bc3228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc3228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc3228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc2e00 bytes 08410991
+ 00bc3228 bytes 08411991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40cf9fc7a1d492ffc6b5b5281a082d1d"></a>

### [`00bc2e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e14.md) → [`00bc323c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc323c.md) _ZN8firebase13remote_config8internal26jni_config_update_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc3268",
      "incomplete_value": true,
      "site": "00bc3268",
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
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2e40",
      "incomplete_value": true,
      "site": "00bc2e40",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc3250",
      "incomplete_value": true,
      "site": "00bc3250",
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
      "definition_site": "00bc2e28",
      "incomplete_value": true,
      "site": "00bc2e28",
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
      "definition_site": "00bc325c",
      "incomplete_value": false,
      "site": "00bc3260",
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
            "const:e5e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2e34",
      "incomplete_value": false,
      "site": "00bc2e38",
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
            "const:e1e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc324c",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc325c",
      "PARAM",
      [
        "storage",
        "002b6e1e",
        null,
        "string"
      ]
    ],
    [
      "00bc3268",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc324c",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc325c",
      "PARAM",
      [
        "storage",
        "002b6e5e",
        null,
        "string"
      ]
    ],
    [
      "00bc3268",
      "WRITE",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e14.md#insn-00bc2e38) · [`00bc2e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e14.md#insn-00bc2e40) · [`00bc2e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e14.md#insn-00bc2e24)
- 新版 `00bc3260`（命令位置の公開資料なし） · `00bc3268`（命令位置の公開資料なし） · `00bc324c`（命令位置の公開資料なし）

~~~diff
- 00bc2e38 ["INT_ADD", "register:40f0:8", ["const:bc2e38:8", "const:4:8"]]
- 00bc2e38 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc3260 ["INT_ADD", "register:40f0:8", ["const:bc3260:8", "const:4:8"]]
+ 00bc3260 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2e38 bytes 365f0294
+ 00bc3260 bytes 2c5f0294
- 00bc2e40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00bc2e40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3268 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00bc3268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2e40 bytes 602e01f9
+ 00bc3268 bytes 602e03f9
- 00bc2e24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00bc2e24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc324c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00bc324c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2e24 bytes 682e41f9
+ 00bc324c bytes 682e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eec7bd8be4407b05bc644be4de67862"></a>

### [`00bc2e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e54.md) → [`00bc327c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc327c.md) _ZN8firebase13remote_config8internal26jni_config_update_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc32a8",
      "incomplete_value": true,
      "site": "00bc32a8",
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
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2e80",
      "incomplete_value": true,
      "site": "00bc2e80",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc3290",
      "incomplete_value": true,
      "site": "00bc3290",
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
      "definition_site": "00bc2e68",
      "incomplete_value": true,
      "site": "00bc2e68",
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
      "definition_site": "00bc3298",
      "incomplete_value": false,
      "site": "00bc32a0",
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
            "const:e5e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2e70",
      "incomplete_value": false,
      "site": "00bc2e78",
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
            "const:e1e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc328c",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3298",
      "PARAM",
      [
        "storage",
        "002b6e1e",
        null,
        "string"
      ]
    ],
    [
      "00bc32a8",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc328c",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3298",
      "PARAM",
      [
        "storage",
        "002b6e5e",
        null,
        "string"
      ]
    ],
    [
      "00bc32a8",
      "WRITE",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e54.md#insn-00bc2e78) · [`00bc2e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e54.md#insn-00bc2e80) · [`00bc2e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e54.md#insn-00bc2e64)
- 新版 `00bc32a0`（命令位置の公開資料なし） · `00bc32a8`（命令位置の公開資料なし） · `00bc328c`（命令位置の公開資料なし）

~~~diff
- 00bc2e78 ["INT_ADD", "register:40f0:8", ["const:bc2e78:8", "const:4:8"]]
- 00bc2e78 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc32a0 ["INT_ADD", "register:40f0:8", ["const:bc32a0:8", "const:4:8"]]
+ 00bc32a0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2e78 bytes 265f0294
+ 00bc32a0 bytes 1c5f0294
- 00bc2e80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00bc2e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc32a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00bc32a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2e80 bytes 602e01f9
+ 00bc32a8 bytes 602e03f9
- 00bc2e64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00bc2e64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc328c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00bc328c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2e64 bytes 682e41f9
+ 00bc328c bytes 682e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f187cc6017a72e1d0bda9ef95cda6181"></a>

### [`00bc2e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e94.md) → [`00bc32bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc32bc.md) _ZN8firebase13remote_config8internal26jni_config_update_listener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc32ec",
      "incomplete_value": true,
      "site": "00bc32ec",
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
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2ec4",
      "incomplete_value": true,
      "site": "00bc2ec4",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc32d0",
      "incomplete_value": true,
      "site": "00bc32d0",
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
      "definition_site": "00bc2ea8",
      "incomplete_value": true,
      "site": "00bc2ea8",
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
      "definition_site": "00bc32dc",
      "incomplete_value": false,
      "site": "00bc32e4",
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
            "const:e5e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2eb4",
      "incomplete_value": false,
      "site": "00bc2ebc",
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
            "const:e1e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc32cc",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc32dc",
      "PARAM",
      [
        "storage",
        "002b6e1e",
        null,
        "string"
      ]
    ],
    [
      "00bc32ec",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc32cc",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc32dc",
      "PARAM",
      [
        "storage",
        "002b6e5e",
        null,
        "string"
      ]
    ],
    [
      "00bc32ec",
      "WRITE",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e94.md#insn-00bc2ebc) · [`00bc2ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e94.md#insn-00bc2ec4) · [`00bc2ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e94.md#insn-00bc2ea4)
- 新版 `00bc32e4`（命令位置の公開資料なし） · `00bc32ec`（命令位置の公開資料なし） · `00bc32cc`（命令位置の公開資料なし）

~~~diff
- 00bc2ebc ["INT_ADD", "register:40f0:8", ["const:bc2ebc:8", "const:4:8"]]
- 00bc2ebc ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc32e4 ["INT_ADD", "register:40f0:8", ["const:bc32e4:8", "const:4:8"]]
+ 00bc32e4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2ebc bytes 155f0294
+ 00bc32e4 bytes 0b5f0294
- 00bc2ec4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00bc2ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc32ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00bc32ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2ec4 bytes 602e01f9
+ 00bc32ec bytes 602e03f9
- 00bc2ea4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00bc2ea4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc32cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00bc32cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2ea4 bytes 682e41f9
+ 00bc32cc bytes 682e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cbde8385d0f2c5c9efe7055b1ee146f"></a>

### [`00bc2ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2ed8.md) → [`00bc3300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3300.md) _ZN8firebase13remote_config8internal26jni_config_update_listener10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc3330",
      "incomplete_value": true,
      "site": "00bc3330",
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
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2f08",
      "incomplete_value": true,
      "site": "00bc2f08",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc3314",
      "incomplete_value": true,
      "site": "00bc3314",
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
      "definition_site": "00bc2eec",
      "incomplete_value": true,
      "site": "00bc2eec",
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
      "definition_site": "00bc331c",
      "incomplete_value": false,
      "site": "00bc3328",
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
            "const:e5e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2ef4",
      "incomplete_value": false,
      "site": "00bc2f00",
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
            "const:e1e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc3310",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc331c",
      "PARAM",
      [
        "storage",
        "002b6e1e",
        null,
        "string"
      ]
    ],
    [
      "00bc3330",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3310",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc331c",
      "PARAM",
      [
        "storage",
        "002b6e5e",
        null,
        "string"
      ]
    ],
    [
      "00bc3330",
      "WRITE",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2ed8.md#insn-00bc2f00) · [`00bc2f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2ed8.md#insn-00bc2f08) · [`00bc2ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2ed8.md#insn-00bc2ee8)
- 新版 `00bc3328`（命令位置の公開資料なし） · `00bc3330`（命令位置の公開資料なし） · `00bc3310`（命令位置の公開資料なし）

~~~diff
- 00bc2f00 ["INT_ADD", "register:40f0:8", ["const:bc2f00:8", "const:4:8"]]
- 00bc2f00 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc3328 ["INT_ADD", "register:40f0:8", ["const:bc3328:8", "const:4:8"]]
+ 00bc3328 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc2f00 bytes 045f0294
+ 00bc3328 bytes fa5e0294
- 00bc2f08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00bc2f08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3330 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00bc3330 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2f08 bytes 602e01f9
+ 00bc3330 bytes 602e03f9
- 00bc2ee8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00bc2ee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc3310 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00bc3310 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2ee8 bytes 682e41f9
+ 00bc3310 bytes 682e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76701d46efd482845a9fb9e28bd11169"></a>

### [`00bc2f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2f94.md) → [`00bc33bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc33bc.md) _ZN8firebase13remote_config8internal26jni_config_update_listener12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2fd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc3418",
      "incomplete_value": true,
      "site": "00bc3418",
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
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2ff0",
      "incomplete_value": true,
      "site": "00bc2ff0",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc33f8"
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
      "00bc33d0",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc33dc",
      "READ",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bc2fd0",
      "WRITE",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc33d0",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc33dc",
      "READ",
      [
        "storage",
        "01126660",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc33f8",
      "WRITE",
      [
        "storage",
        "01126660",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2f94.md#insn-00bc2fac) · [`00bc2fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2f94.md#insn-00bc2fcc) · [`00bc2fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2f94.md#insn-00bc2fd0)
- 新版 `00bc33d4`（命令位置の公開資料なし）

~~~diff
- 00bc2fac ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc2fac ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bc33d4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc33d4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bc2fac bytes 410200b4
+ 00bc33d4 bytes 410200b4
- 00bc2fcc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2fcc ["INT_ADD", "register:40f0:8", ["const:bc2fcc:8", "const:4:8"]]
- 00bc2fcc ["CALLIND", null, ["register:0:8"]]
- 00bc2fcc bytes 00013fd6
- 00bc2fd0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc2fd0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc2fd0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:260:8"]]
- 00bc2fd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc2fd0 bytes bf820939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5364959a367a008576cc2cd9ccb29feb"></a>

### [`00bc3004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3004.md) → [`00bc342c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc342c.md) _ZN8firebase13remote_config8internal26jni_config_update_listener14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc346c",
      "incomplete_value": true,
      "site": "00bc346c",
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
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3044",
      "incomplete_value": true,
      "site": "00bc3044",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc3448",
      "incomplete_value": true,
      "site": "00bc3448",
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
      "definition_site": "00bc3020",
      "incomplete_value": true,
      "site": "00bc3020",
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
      "definition_site": "00bc3450",
      "incomplete_value": false,
      "site": "00bc3464",
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
            "const:e5e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3028",
      "incomplete_value": false,
      "site": "00bc303c",
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
            "const:e1e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc3440",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3450",
      "PARAM",
      [
        "storage",
        "002b6e1e",
        null,
        "string"
      ]
    ],
    [
      "00bc346c",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3440",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3450",
      "PARAM",
      [
        "storage",
        "002b6e5e",
        null,
        "string"
      ]
    ],
    [
      "00bc346c",
      "WRITE",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc303c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3004.md#insn-00bc303c) · [`00bc3044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3004.md#insn-00bc3044) · [`00bc3018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3004.md#insn-00bc3018)
- 新版 `00bc3464`（命令位置の公開資料なし） · `00bc346c`（命令位置の公開資料なし） · `00bc3440`（命令位置の公開資料なし）

~~~diff
- 00bc303c ["INT_ADD", "register:40f0:8", ["const:bc303c:8", "const:4:8"]]
- 00bc303c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc3464 ["INT_ADD", "register:40f0:8", ["const:bc3464:8", "const:4:8"]]
+ 00bc3464 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc303c bytes b55e0294
+ 00bc3464 bytes ab5e0294
- 00bc3044 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
- 00bc3044 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc346c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:658:8"]]
+ 00bc346c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3044 bytes 802e01f9
+ 00bc346c bytes 802e03f9
- 00bc3018 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
- 00bc3018 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc3440 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:658:8"]]
+ 00bc3440 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc3018 bytes 812e41f9
+ 00bc3440 bytes 812e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d013709f552fb089e5a74e66996fd68"></a>

### [`00bc30b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc30b0.md) → [`00bc34d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc34d8.md) _ZN8firebase13remote_config8internal26jni_config_update_listener13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc30f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3518"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc30cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc30c4",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc30cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc351c"
      ]
    ],
    [
      "unmatched:00bc30d4",
      "PARAM",
      [
        "storage",
        "002b6e1e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc34ec",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc34f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc351c"
      ]
    ],
    [
      "00bc34fc",
      "PARAM",
      [
        "storage",
        "002b6e5e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc30cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc30b0.md#insn-00bc30cc) · [`00bc30e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc30b0.md#insn-00bc30e8) · [`00bc30f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc30b0.md#insn-00bc30f0)
- 新版 `00bc3510`（命令位置の公開資料なし）

~~~diff
- 00bc30cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc30cc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc30cc bytes 410100b5
- 00bc30e8 ["INT_ADD", "register:40f0:8", ["const:bc30e8:8", "const:4:8"]]
- 00bc30e8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc3510 ["INT_ADD", "register:40f0:8", ["const:bc3510:8", "const:4:8"]]
+ 00bc3510 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc30e8 bytes 8a5e0294
+ 00bc3510 bytes 805e0294
- 00bc30f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
- 00bc30f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc30f0 bytes 802e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05fe034dc52461042fecdb45c9155372"></a>

### [`00bc3120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3120.md) → [`00bc3548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3548.md) _ZN8firebase13remote_config8internal26jni_config_update_listener10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc3564",
      "incomplete_value": false,
      "site": "00bc3568",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc313c",
      "incomplete_value": false,
      "site": "00bc3140",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc3574",
      "incomplete_value": true,
      "site": "00bc3580",
      "value": [
        "LOAD",
        "8",
        [
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
              "INT_LEFT"
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
      "00bc3564",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc314c",
      "DATA",
      [
        "storage",
        "01126270",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc3150",
      "DATA",
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
      "00bc3564",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bc3574",
      "DATA",
      [
        "storage",
        "01126670",
        null,
        null
      ]
    ],
    [
      "00bc3578",
      "DATA",
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

- 旧版 [`00bc3140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3120.md#insn-00bc3140) · [`00bc313c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3120.md#insn-00bc313c) · [`00bc3148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3120.md#insn-00bc3148)
- 新版 `00bc3568`（命令位置の公開資料なし） · `00bc3564`（命令位置の公開資料なし）

~~~diff
- 00bc3140 ["INT_ADD", "register:40f0:8", ["const:bc3140:8", "const:4:8"]]
- 00bc3140 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc3568 ["INT_ADD", "register:40f0:8", ["const:bc3568:8", "const:4:8"]]
+ 00bc3568 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc3140 bytes b05e0294
+ 00bc3568 bytes a65e0294
- 00bc313c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bc313c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc313c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc313c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc3564 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bc3564 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3564 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3564 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc313c bytes 00441191
+ 00bc3564 bytes 00781491
- 00bc3148 ["COPY", "tmp:0:8", ["const:270:8"]]
- 00bc3148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc3148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc3148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc3148 bytes 08c10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09332ee3e37bf1a97fe5caf520417eb5"></a>

### [`00bc315c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc315c.md) → [`00bc3584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3584.md) _ZN8firebase13remote_config8internal13config_update19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3188"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc35b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc3598",
      "incomplete_value": true,
      "site": "00bc3598",
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
      "definition_site": "00bc3170",
      "incomplete_value": true,
      "site": "00bc3170",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc3594",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3598",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc318c"
      ]
    ],
    [
      "unmatched:00bc317c",
      "PARAM",
      [
        "storage",
        "002bc09c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc3594",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3598",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc35b4"
      ]
    ],
    [
      "00bc35a4",
      "PARAM",
      [
        "storage",
        "002bc0dc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc315c.md#insn-00bc3180) · [`00bc3188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc315c.md#insn-00bc3188) · [`00bc3198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc315c.md#insn-00bc3198)

~~~diff
- 00bc3180 ["INT_ADD", "register:40f0:8", ["const:bc3180:8", "const:4:8"]]
- 00bc3180 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc3180 bytes 645e0294
- 00bc3188 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:278:8"]]
- 00bc3188 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3188 bytes 603e01f9
- 00bc3198 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc3198 ["RETURN", null, ["register:0:8"]]
- 00bc3198 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9576dccf694d76a7cc1b30bcefa82ffb"></a>

### [`00bc319c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc319c.md) → [`00bc35c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc35c4.md) _ZN8firebase13remote_config8internal13config_update19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc319c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc31a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc31a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc319c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc31a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc35d4",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc35c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc35c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc35d4",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc319c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc319c.md#insn-00bc319c) · [`00bc31a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc319c.md#insn-00bc31a0) · [`00bc31b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc319c.md#insn-00bc31b0)
- 新版 `00bc35d8`（命令位置の公開資料なし）

~~~diff
- 00bc319c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc319c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc319c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc319c bytes f30f1ef8
- 00bc31a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc31a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc31a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc31a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc31a0 bytes fd7b01a9
- 00bc31b0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc31b0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bc35d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc35d8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc31b0 bytes e80000b5
+ 00bc35d8 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d4c1eaf387d7bf581d358a2b9f67242"></a>

### [`00bc31dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc31dc.md) → [`00bc3604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3604.md) _ZN8firebase13remote_config8internal13config_update10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc3634",
      "incomplete_value": true,
      "site": "00bc3634",
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
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc320c",
      "incomplete_value": true,
      "site": "00bc320c",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc3618",
      "incomplete_value": true,
      "site": "00bc3618",
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
      "definition_site": "00bc31f0",
      "incomplete_value": true,
      "site": "00bc31f0",
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
      "definition_site": "00bc3624",
      "incomplete_value": false,
      "site": "00bc362c",
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
            "const:dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc31fc",
      "incomplete_value": false,
      "site": "00bc3204",
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
            "const:9c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc3614",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3624",
      "PARAM",
      [
        "storage",
        "002bc09c",
        null,
        "string"
      ]
    ],
    [
      "00bc3634",
      "WRITE",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3614",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3624",
      "PARAM",
      [
        "storage",
        "002bc0dc",
        null,
        "string"
      ]
    ],
    [
      "00bc3634",
      "WRITE",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc31dc.md#insn-00bc3204) · [`00bc320c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc31dc.md#insn-00bc320c) · [`00bc31ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc31dc.md#insn-00bc31ec)
- 新版 `00bc362c`（命令位置の公開資料なし） · `00bc3634`（命令位置の公開資料なし） · `00bc3614`（命令位置の公開資料なし）

~~~diff
- 00bc3204 ["INT_ADD", "register:40f0:8", ["const:bc3204:8", "const:4:8"]]
- 00bc3204 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc362c ["INT_ADD", "register:40f0:8", ["const:bc362c:8", "const:4:8"]]
+ 00bc362c ["CALL", null, ["callee:00c5af10:8"]]
- 00bc3204 bytes 435e0294
+ 00bc362c bytes 395e0294
- 00bc320c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:278:8"]]
- 00bc320c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3634 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
+ 00bc3634 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc320c bytes 603e01f9
+ 00bc3634 bytes 603e03f9
- 00bc31ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:278:8"]]
- 00bc31ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc3614 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
+ 00bc3614 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc31ec bytes 683e41f9
+ 00bc3614 bytes 683e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acbe8c0ccc35bee3ae2b2dfc1cbf1d69"></a>

### [`00bc3220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3220.md) → [`00bc3648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3648.md) _ZN8firebase13remote_config8internal13config_update10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc3678",
      "incomplete_value": true,
      "site": "00bc3678",
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
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3250",
      "incomplete_value": true,
      "site": "00bc3250",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc365c",
      "incomplete_value": true,
      "site": "00bc365c",
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
      "definition_site": "00bc3234",
      "incomplete_value": true,
      "site": "00bc3234",
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
      "definition_site": "00bc3664",
      "incomplete_value": false,
      "site": "00bc3670",
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
            "const:dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc323c",
      "incomplete_value": false,
      "site": "00bc3248",
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
            "const:9c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc3658",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3664",
      "PARAM",
      [
        "storage",
        "002bc09c",
        null,
        "string"
      ]
    ],
    [
      "00bc3678",
      "WRITE",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3658",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3664",
      "PARAM",
      [
        "storage",
        "002bc0dc",
        null,
        "string"
      ]
    ],
    [
      "00bc3678",
      "WRITE",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3220.md#insn-00bc3248) · [`00bc3250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3220.md#insn-00bc3250) · [`00bc3230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3220.md#insn-00bc3230)
- 新版 `00bc3670`（命令位置の公開資料なし） · `00bc3678`（命令位置の公開資料なし） · `00bc3658`（命令位置の公開資料なし）

~~~diff
- 00bc3248 ["INT_ADD", "register:40f0:8", ["const:bc3248:8", "const:4:8"]]
- 00bc3248 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc3670 ["INT_ADD", "register:40f0:8", ["const:bc3670:8", "const:4:8"]]
+ 00bc3670 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc3248 bytes 325e0294
+ 00bc3670 bytes 285e0294
- 00bc3250 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:278:8"]]
- 00bc3250 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3678 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
+ 00bc3678 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3250 bytes 603e01f9
+ 00bc3678 bytes 603e03f9
- 00bc3230 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:278:8"]]
- 00bc3230 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc3658 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
+ 00bc3658 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc3230 bytes 683e41f9
+ 00bc3658 bytes 683e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-722e1db778e64205d7d0bb5536c75ba9"></a>

### [`00bc3270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3270.md) → [`00bc3698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3698.md) _ZN8firebase13remote_config8internal13config_update15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc32c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc36f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc36cc",
      "incomplete_value": true,
      "site": "00bc36d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc32a4",
      "incomplete_value": true,
      "site": "00bc32b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "00bc36ac",
      "READ",
      [
        "storage",
        "01126280",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bc32a4",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc32c8",
      "WRITE",
      [
        "storage",
        "01126280",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc36ac",
      "READ",
      [
        "storage",
        "01126680",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc36cc",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc36f0",
      "WRITE",
      [
        "storage",
        "01126680",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc32b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3270.md#insn-00bc32b0) · [`00bc32c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3270.md#insn-00bc32c8)
- 新版 `00bc36d8`（命令位置の公開資料なし） · `00bc36f0`（命令位置の公開資料なし）

~~~diff
- 00bc32b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc32b0 ["INT_ADD", "register:40f0:8", ["const:bc32b0:8", "const:4:8"]]
- 00bc32b0 ["CALLIND", null, ["register:0:8"]]
+ 00bc36d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc36d8 ["INT_ADD", "register:40f0:8", ["const:bc36d8:8", "const:4:8"]]
+ 00bc36d8 ["CALLIND", null, ["register:0:8"]]
- 00bc32b0 bytes 00013fd6
+ 00bc36d8 bytes 00013fd6
- 00bc32c8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc32c8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:280:8"]]
- 00bc32c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc32c8 bytes a0020a39
+ 00bc36f0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc36f0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:680:8"]]
+ 00bc36f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc36f0 bytes a0021a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e98751783fe382ff9e3dc65c9a9be54"></a>

### [`00bc32dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc32dc.md) → [`00bc3704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3704.md) _ZN8firebase13remote_config8internal13config_update12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 25.00% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3318"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc3760",
      "incomplete_value": true,
      "site": "00bc3760",
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
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3338",
      "incomplete_value": true,
      "site": "00bc3338",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3740"
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
      "00bc3718",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3724",
      "READ",
      [
        "storage",
        "01126280",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bc3318",
      "WRITE",
      [
        "storage",
        "01126280",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc3718",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3724",
      "READ",
      [
        "storage",
        "01126680",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc3740",
      "WRITE",
      [
        "storage",
        "01126680",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc32f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc32dc.md#insn-00bc32f4) · [`00bc3314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc32dc.md#insn-00bc3314) · [`00bc3318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc32dc.md#insn-00bc3318)
- 新版 `00bc371c`（命令位置の公開資料なし）

~~~diff
- 00bc32f4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc32f4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bc371c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc371c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bc32f4 bytes 410200b4
+ 00bc371c bytes 410200b4
- 00bc3314 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc3314 ["INT_ADD", "register:40f0:8", ["const:bc3314:8", "const:4:8"]]
- 00bc3314 ["CALLIND", null, ["register:0:8"]]
- 00bc3314 bytes 00013fd6
- 00bc3318 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc3318 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc3318 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:280:8"]]
- 00bc3318 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc3318 bytes bf020a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a4ef916fbf34e4fddf9cb3a8bc8a899"></a>

### [`00bc334c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc334c.md) → [`00bc3774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3774.md) _ZN8firebase13remote_config8internal13config_update14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc338c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc37b4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc3790",
      "incomplete_value": true,
      "site": "00bc3790",
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
      "definition_site": "00bc3368",
      "incomplete_value": true,
      "site": "00bc3368",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc3788",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3798",
      "PARAM",
      [
        "storage",
        "002bc09c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc338c",
      "WRITE",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3788",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3798",
      "PARAM",
      [
        "storage",
        "002bc0dc",
        null,
        "string"
      ]
    ],
    [
      "00bc37b4",
      "WRITE",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc334c.md#insn-00bc3384) · [`00bc338c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc334c.md#insn-00bc338c)
- 新版 `00bc37ac`（命令位置の公開資料なし） · `00bc37b4`（命令位置の公開資料なし）

~~~diff
- 00bc3384 ["INT_ADD", "register:40f0:8", ["const:bc3384:8", "const:4:8"]]
- 00bc3384 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc37ac ["INT_ADD", "register:40f0:8", ["const:bc37ac:8", "const:4:8"]]
+ 00bc37ac ["CALL", null, ["callee:00c5af10:8"]]
- 00bc3384 bytes e35d0294
+ 00bc37ac bytes d95d0294
- 00bc338c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:278:8"]]
- 00bc338c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc338c bytes 803e01f9
+ 00bc37b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:678:8"]]
+ 00bc37b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc37b4 bytes 803e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bfe2510ec6bc8190245ca37608fde70"></a>

### [`00bc33bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc33bc.md) → [`00bc37e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc37e4.md) _ZN8firebase13remote_config8internal13config_update11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc3800",
      "incomplete_value": false,
      "site": "00bc3804",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc33d8",
      "incomplete_value": false,
      "site": "00bc33dc",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc3810",
      "incomplete_value": true,
      "site": "00bc381c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc33e8",
      "incomplete_value": true,
      "site": "00bc33f4",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00bc3800",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bc3810",
      "DATA",
      [
        "storage",
        "01126288",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3800",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc3810",
      "DATA",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc33dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc33bc.md#insn-00bc33dc) · [`00bc33d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc33bc.md#insn-00bc33d8) · [`00bc33e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc33bc.md#insn-00bc33e4)
- 新版 `00bc3804`（命令位置の公開資料なし） · `00bc3800`（命令位置の公開資料なし） · `00bc380c`（命令位置の公開資料なし）

~~~diff
- 00bc33dc ["INT_ADD", "register:40f0:8", ["const:bc33dc:8", "const:4:8"]]
- 00bc33dc ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc3804 ["INT_ADD", "register:40f0:8", ["const:bc3804:8", "const:4:8"]]
+ 00bc3804 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc33dc bytes 095e0294
+ 00bc3804 bytes ff5d0294
- 00bc33d8 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bc33d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc33d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc33d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc3800 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bc3800 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3800 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3800 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc33d8 bytes 00680a91
+ 00bc3800 bytes 009c0d91
- 00bc33e4 ["COPY", "tmp:0:8", ["const:288:8"]]
- 00bc33e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc33e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc33e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc380c ["COPY", "tmp:0:8", ["const:688:8"]]
+ 00bc380c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc380c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc380c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc33e4 bytes 08210a91
+ 00bc380c bytes 08211a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af5b8fb380c5f36cc07488be3345888f"></a>

### [`00bc33f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc33f8.md) → [`00bc3820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3820.md) _ZN8firebase13remote_config8internal13config_update13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc3860",
      "incomplete_value": true,
      "site": "00bc3860",
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
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3438",
      "incomplete_value": true,
      "site": "00bc3438",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc383c",
      "incomplete_value": true,
      "site": "00bc383c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3414",
      "incomplete_value": true,
      "site": "00bc3414",
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
      "definition_site": "00bc3844",
      "incomplete_value": false,
      "site": "00bc3858",
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
            "const:dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc341c",
      "incomplete_value": false,
      "site": "00bc3430",
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
            "const:9c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc340c",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3844",
      "PARAM",
      [
        "storage",
        "002bc09c",
        null,
        "string"
      ]
    ],
    [
      "00bc3860",
      "WRITE",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3834",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3844",
      "PARAM",
      [
        "storage",
        "002bc0dc",
        null,
        "string"
      ]
    ],
    [
      "00bc3860",
      "WRITE",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc33f8.md#insn-00bc3430) · [`00bc3438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc33f8.md#insn-00bc3438) · [`00bc340c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc33f8.md#insn-00bc340c)
- 新版 `00bc3858`（命令位置の公開資料なし） · `00bc3860`（命令位置の公開資料なし）

~~~diff
- 00bc3430 ["INT_ADD", "register:40f0:8", ["const:bc3430:8", "const:4:8"]]
- 00bc3430 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc3858 ["INT_ADD", "register:40f0:8", ["const:bc3858:8", "const:4:8"]]
+ 00bc3858 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc3430 bytes b85d0294
+ 00bc3858 bytes ae5d0294
- 00bc3438 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:278:8"]]
- 00bc3438 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3860 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:678:8"]]
+ 00bc3860 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3438 bytes 803e01f9
+ 00bc3860 bytes 803e03f9
- 00bc340c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:278:8"]]
- 00bc340c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc340c bytes 813e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e788e8ace22695a6a6deaa64ada95ae"></a>

### [`00bc3468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3468.md) → [`00bc3890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3890.md) _ZN8firebase13remote_config8internal13config_update10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc38ac",
      "incomplete_value": false,
      "site": "00bc38b0",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3484",
      "incomplete_value": false,
      "site": "00bc3488",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc38bc",
      "incomplete_value": true,
      "site": "00bc38c8",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3494",
      "incomplete_value": true,
      "site": "00bc34a0",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00bc38ac",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bc38bc",
      "DATA",
      [
        "storage",
        "01126290",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc38ac",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bc38bc",
      "DATA",
      [
        "storage",
        "01126690",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3468.md#insn-00bc3488) · [`00bc3484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3468.md#insn-00bc3484) · [`00bc3490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3468.md#insn-00bc3490)
- 新版 `00bc38b0`（命令位置の公開資料なし） · `00bc38ac`（命令位置の公開資料なし） · `00bc38b8`（命令位置の公開資料なし）

~~~diff
- 00bc3488 ["INT_ADD", "register:40f0:8", ["const:bc3488:8", "const:4:8"]]
- 00bc3488 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc38b0 ["INT_ADD", "register:40f0:8", ["const:bc38b0:8", "const:4:8"]]
+ 00bc38b0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc3488 bytes de5d0294
+ 00bc38b0 bytes d45d0294
- 00bc3484 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bc3484 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc3484 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc3484 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc38ac ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bc38ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc38ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc38ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc3484 bytes 00441191
+ 00bc38ac bytes 00781491
- 00bc3490 ["COPY", "tmp:0:8", ["const:290:8"]]
- 00bc3490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc3490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc3490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc38b8 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00bc38b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc38b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc38b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc3490 bytes 08410a91
+ 00bc38b8 bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1428407994065ae757256110546fb791"></a>

### [`00bc34a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc34a4.md) → [`00bc38cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc38cc.md) _ZN8firebase13remote_config8internal35config_update_listener_registration19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8in

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc34d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc38f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc38e0",
      "incomplete_value": true,
      "site": "00bc38e0",
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
      "definition_site": "00bc34b8",
      "incomplete_value": true,
      "site": "00bc34b8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc38dc",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc34c4",
      "PARAM",
      [
        "storage",
        "002a9762",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc34c8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bc38dc",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc38ec",
      "PARAM",
      [
        "storage",
        "002a982f",
        null,
        "string"
      ]
    ],
    [
      "00bc38f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc34b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc34a4.md#insn-00bc34b8) · [`00bc34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc34a4.md#insn-00bc34c8) · [`00bc34d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc34a4.md#insn-00bc34d0)
- 新版 `00bc38e0`（命令位置の公開資料なし）

~~~diff
- 00bc34b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc34b8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc38e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc38e0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc34b8 bytes e80000b5
+ 00bc38e0 bytes e80000b5
- 00bc34c8 ["INT_ADD", "register:40f0:8", ["const:bc34c8:8", "const:4:8"]]
- 00bc34c8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc34c8 bytes 925d0294
- 00bc34d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:298:8"]]
- 00bc34d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc34d0 bytes 604e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca78cb5e5d68e3a2169a3e40c1fe7430"></a>

### [`00bc34e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc34e4.md) → [`00bc390c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc390c.md) _ZN8firebase13remote_config8internal35config_update_listener_registration19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8in

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3510"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3938"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc3920",
      "incomplete_value": true,
      "site": "00bc3920",
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
      "definition_site": "00bc34f8",
      "incomplete_value": true,
      "site": "00bc34f8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc391c",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc3500",
      "PARAM",
      [
        "storage",
        "002a9762",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc3508",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bc391c",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3928",
      "PARAM",
      [
        "storage",
        "002a982f",
        null,
        "string"
      ]
    ],
    [
      "00bc3930",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc34f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc34e4.md#insn-00bc34f8) · [`00bc3508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc34e4.md#insn-00bc3508) · [`00bc3510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc34e4.md#insn-00bc3510)
- 新版 `00bc3920`（命令位置の公開資料なし）

~~~diff
- 00bc34f8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc34f8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bc3920 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc3920 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc34f8 bytes e80000b5
+ 00bc3920 bytes e80000b5
- 00bc3508 ["INT_ADD", "register:40f0:8", ["const:bc3508:8", "const:4:8"]]
- 00bc3508 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc3508 bytes 825d0294
- 00bc3510 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:298:8"]]
- 00bc3510 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3510 bytes 604e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d07de7e4c633ecd4cb20cdc7ef6109a"></a>

### [`00bc3524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3524.md) → [`00bc394c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc394c.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3524"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3528"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc3524",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc3528",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc395c",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc394c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc3950",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc395c",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3524.md#insn-00bc3524) · [`00bc3528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3524.md#insn-00bc3528) · [`00bc3538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3524.md#insn-00bc3538)
- 新版 `00bc3960`（命令位置の公開資料なし）

~~~diff
- 00bc3524 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc3524 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc3524 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc3524 bytes f30f1ef8
- 00bc3528 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc3528 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc3528 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc3528 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc3528 bytes fd7b01a9
- 00bc3538 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc3538 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bc3960 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc3960 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc3538 bytes 080100b5
+ 00bc3960 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8a7eca5f281670e3a9489fbd35e9a8c"></a>

### [`00bc3568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3568.md) → [`00bc3990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3990.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc39c0",
      "incomplete_value": true,
      "site": "00bc39c0",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3598",
      "incomplete_value": true,
      "site": "00bc3598",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc39a4",
      "incomplete_value": true,
      "site": "00bc39a4",
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
      "definition_site": "00bc357c",
      "incomplete_value": true,
      "site": "00bc357c",
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
      "definition_site": "00bc39ac",
      "incomplete_value": false,
      "site": "00bc39b8",
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
            "const:82f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3584",
      "incomplete_value": false,
      "site": "00bc3590",
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
            "const:762:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc39a0",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc39ac",
      "PARAM",
      [
        "storage",
        "002a9762",
        null,
        "string"
      ]
    ],
    [
      "00bc39c0",
      "WRITE",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc39a0",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc39ac",
      "PARAM",
      [
        "storage",
        "002a982f",
        null,
        "string"
      ]
    ],
    [
      "00bc39c0",
      "WRITE",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3568.md#insn-00bc3590) · [`00bc3598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3568.md#insn-00bc3598) · [`00bc3578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3568.md#insn-00bc3578)
- 新版 `00bc39b8`（命令位置の公開資料なし） · `00bc39c0`（命令位置の公開資料なし） · `00bc39a0`（命令位置の公開資料なし）

~~~diff
- 00bc3590 ["INT_ADD", "register:40f0:8", ["const:bc3590:8", "const:4:8"]]
- 00bc3590 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc39b8 ["INT_ADD", "register:40f0:8", ["const:bc39b8:8", "const:4:8"]]
+ 00bc39b8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc3590 bytes 605d0294
+ 00bc39b8 bytes 565d0294
- 00bc3598 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:298:8"]]
- 00bc3598 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc39c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00bc39c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3598 bytes 604e01f9
+ 00bc39c0 bytes 604e03f9
- 00bc3578 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:298:8"]]
- 00bc3578 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc39a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00bc39a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc3578 bytes 684e41f9
+ 00bc39a0 bytes 684e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acd40168099e61333c702f1720d2f03f"></a>

### [`00bc35b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc35b8.md) → [`00bc39e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc39e0.md) _ZN8firebase13remote_config8internal35config_update_listener_registration15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc3a38",
      "incomplete_value": true,
      "site": "00bc3a38",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3610",
      "incomplete_value": true,
      "site": "00bc3610",
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
            "const:2a0:8"
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
      "definition_site": "00bc3a14",
      "incomplete_value": true,
      "site": "00bc3a20",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "definition_site": "00bc35ec",
      "incomplete_value": true,
      "site": "00bc35f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:298:8"
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
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3620"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc39f4",
      "READ",
      [
        "storage",
        "011262a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc3a00",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc3614"
      ]
    ],
    [
      "00bc3a14",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc39f4",
      "READ",
      [
        "storage",
        "011266a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc3a00",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3a3c"
      ]
    ],
    [
      "00bc3a14",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc35f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc35b8.md#insn-00bc35f8) · [`00bc3610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc35b8.md#insn-00bc3610) · [`00bc3620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc35b8.md#insn-00bc3620)
- 新版 `00bc3a20`（命令位置の公開資料なし） · `00bc3a38`（命令位置の公開資料なし）

~~~diff
- 00bc35f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc35f8 ["INT_ADD", "register:40f0:8", ["const:bc35f8:8", "const:4:8"]]
- 00bc35f8 ["CALLIND", null, ["register:0:8"]]
+ 00bc3a20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc3a20 ["INT_ADD", "register:40f0:8", ["const:bc3a20:8", "const:4:8"]]
+ 00bc3a20 ["CALLIND", null, ["register:0:8"]]
- 00bc35f8 bytes 00013fd6
+ 00bc3a20 bytes 00013fd6
- 00bc3610 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc3610 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:2a0:8"]]
- 00bc3610 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc3a38 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc3a38 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6a0:8"]]
+ 00bc3a38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc3610 bytes a0820a39
+ 00bc3a38 bytes a0821a39
- 00bc3620 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc3620 ["RETURN", null, ["register:0:8"]]
- 00bc3620 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-225f64f4e25b5e5ff885ff9f3b3241a2"></a>

### [`00bc3694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3694.md) → [`00bc3abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3abc.md) _ZN8firebase13remote_config8internal35config_update_listener_registration14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc36d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3afc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc36b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc36a8",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc36b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3b00"
      ]
    ],
    [
      "unmatched:00bc36b8",
      "PARAM",
      [
        "storage",
        "002a9762",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc3ad0",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3ad8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3b00"
      ]
    ],
    [
      "00bc3ae0",
      "PARAM",
      [
        "storage",
        "002a982f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc36b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3694.md#insn-00bc36b0) · [`00bc36cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3694.md#insn-00bc36cc) · [`00bc36d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3694.md#insn-00bc36d4)
- 新版 `00bc3af4`（命令位置の公開資料なし）

~~~diff
- 00bc36b0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc36b0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc36b0 bytes 410100b5
- 00bc36cc ["INT_ADD", "register:40f0:8", ["const:bc36cc:8", "const:4:8"]]
- 00bc36cc ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc3af4 ["INT_ADD", "register:40f0:8", ["const:bc3af4:8", "const:4:8"]]
+ 00bc3af4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc36cc bytes 115d0294
+ 00bc3af4 bytes 075d0294
- 00bc36d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:298:8"]]
- 00bc36d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc36d4 bytes 804e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ecf0955c3a2e5ed2a8ff20035070010"></a>

### [`00bc3704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3704.md) → [`00bc3b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3b2c.md) _ZN8firebase13remote_config8internal35config_update_listener_registration11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc3b48",
      "incomplete_value": false,
      "site": "00bc3b4c",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3720",
      "incomplete_value": false,
      "site": "00bc3724",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc3b58",
      "incomplete_value": true,
      "site": "00bc3b64",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3730",
      "incomplete_value": true,
      "site": "00bc373c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00bc3b48",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bc3b58",
      "DATA",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3b48",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc3b58",
      "DATA",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3704.md#insn-00bc3724) · [`00bc3720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3704.md#insn-00bc3720) · [`00bc372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3704.md#insn-00bc372c)
- 新版 `00bc3b4c`（命令位置の公開資料なし） · `00bc3b48`（命令位置の公開資料なし） · `00bc3b54`（命令位置の公開資料なし）

~~~diff
- 00bc3724 ["INT_ADD", "register:40f0:8", ["const:bc3724:8", "const:4:8"]]
- 00bc3724 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc3b4c ["INT_ADD", "register:40f0:8", ["const:bc3b4c:8", "const:4:8"]]
+ 00bc3b4c ["CALL", null, ["callee:00c5b000:8"]]
- 00bc3724 bytes 375d0294
+ 00bc3b4c bytes 2d5d0294
- 00bc3720 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bc3720 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc3720 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc3720 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc3b48 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bc3b48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3b48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3b48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc3720 bytes 00680a91
+ 00bc3b48 bytes 009c0d91
- 00bc372c ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00bc372c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc372c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc372c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc3b54 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 00bc3b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc3b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc3b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc372c bytes 08a10a91
+ 00bc3b54 bytes 08a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-694dc32c805dd2bdaa252d88a0bb94fb"></a>

### [`00bc3740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3740.md) → [`00bc3b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3b68.md) _ZN8firebase13remote_config8internal35config_update_listener_registration13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3780"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3ba8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc375c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc3754",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc375c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3bac"
      ]
    ],
    [
      "unmatched:00bc3764",
      "PARAM",
      [
        "storage",
        "002a9762",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc3b7c",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3b84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3bac"
      ]
    ],
    [
      "00bc3b8c",
      "PARAM",
      [
        "storage",
        "002a982f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc375c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3740.md#insn-00bc375c) · [`00bc3778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3740.md#insn-00bc3778) · [`00bc3780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3740.md#insn-00bc3780)
- 新版 `00bc3ba0`（命令位置の公開資料なし）

~~~diff
- 00bc375c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc375c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc375c bytes 410100b5
- 00bc3778 ["INT_ADD", "register:40f0:8", ["const:bc3778:8", "const:4:8"]]
- 00bc3778 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc3ba0 ["INT_ADD", "register:40f0:8", ["const:bc3ba0:8", "const:4:8"]]
+ 00bc3ba0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc3778 bytes e65c0294
+ 00bc3ba0 bytes dc5c0294
- 00bc3780 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:298:8"]]
- 00bc3780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3780 bytes 804e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c63a79c7259d0f3fd5c05dec78b3648"></a>

### [`00bc37b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc37b0.md) → [`00bc3bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3bd8.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc3bf4",
      "incomplete_value": false,
      "site": "00bc3bf8",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc37cc",
      "incomplete_value": false,
      "site": "00bc37d0",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc3c04",
      "incomplete_value": true,
      "site": "00bc3c10",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc37dc",
      "incomplete_value": true,
      "site": "00bc37e8",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00bc3bf4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bc3c04",
      "DATA",
      [
        "storage",
        "011262b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc3bf4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bc3c04",
      "DATA",
      [
        "storage",
        "011266b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc37d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc37b0.md#insn-00bc37d0) · [`00bc37cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc37b0.md#insn-00bc37cc) · [`00bc37d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc37b0.md#insn-00bc37d8)
- 新版 `00bc3bf8`（命令位置の公開資料なし） · `00bc3bf4`（命令位置の公開資料なし） · `00bc3c00`（命令位置の公開資料なし）

~~~diff
- 00bc37d0 ["INT_ADD", "register:40f0:8", ["const:bc37d0:8", "const:4:8"]]
- 00bc37d0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc3bf8 ["INT_ADD", "register:40f0:8", ["const:bc3bf8:8", "const:4:8"]]
+ 00bc3bf8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc37d0 bytes 0c5d0294
+ 00bc3bf8 bytes 025d0294
- 00bc37cc ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bc37cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc37cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc37cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc3bf4 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bc3bf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3bf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3bf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc37cc bytes 00441191
+ 00bc3bf4 bytes 00781491
- 00bc37d8 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 00bc37d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc37d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc37d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc3c00 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 00bc3c00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc3c00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc3c00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc37d8 bytes 08c10a91
+ 00bc3c00 bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d01e8361c4711050f740e6c8b4b1f8ad"></a>

### [`00bc37f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc37f4.md) → [`00bc3c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3c1c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternalC1ERKNS_3AppE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d470.md) · 呼出先 22件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5d870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d870.md) · 呼出先 22件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 43.76% / 新版 43.76%

CFGの説明率　旧版 21.43% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 33件, `unresolved_branch_alignment` 29件, `unresolved_call_alignment` 38件, `unresolved_store_alignment` 26件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 5件, `store_condition` 1件, `store_destination` 5件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc3ca4",
      "incomplete_value": true,
      "site": "00bc3ca4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc387c",
      "incomplete_value": true,
      "site": "00bc387c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:578:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00bc3ca4",
      "incomplete_value": true,
      "site": "00bc3ca4",
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
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc387c",
      "incomplete_value": true,
      "site": "00bc387c",
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
            "const:4:8"
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
      "definition_site": "00bc3da8",
      "incomplete_value": true,
      "site": "00bc3dc0",
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
      "definition_site": "00bc3980",
      "incomplete_value": true,
      "site": "00bc3998",
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
      "00bc3c84",
      "READ",
      [
        "storage",
        "00c9b578",
        null,
        "pointer"
      ]
    ],
    [
      "00bc3ca4",
      "DATA",
      [
        "storage",
        "011262b8",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ],
    [
      "00bc3ca4",
      "DATA",
      [
        "storage",
        "011262bc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc3c84",
      "READ",
      [
        "storage",
        "00c9b978",
        null,
        "pointer"
      ]
    ],
    [
      "00bc3ca4",
      "DATA",
      [
        "storage",
        "011266b8",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ],
    [
      "00bc3ca4",
      "DATA",
      [
        "storage",
        "011266bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc37f4.md#insn-00bc3908) · [`00bc3964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc37f4.md#insn-00bc3964) · [`00bc39fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc37f4.md#insn-00bc39fc)
- 新版 `00bc3d30`（命令位置の公開資料なし） · `00bc3d8c`（命令位置の公開資料なし） · `00bc3e24`（命令位置の公開資料なし）

~~~diff
- 00bc3908 ["INT_ADD", "register:40f0:8", ["const:bc3908:8", "const:4:8"]]
- 00bc3908 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bc3d30 ["INT_ADD", "register:40f0:8", ["const:bc3d30:8", "const:4:8"]]
+ 00bc3d30 ["CALL", null, ["callee:00c5b080:8"]]
- 00bc3908 bytes de5c0294
+ 00bc3d30 bytes d45c0294
- 00bc3964 ["INT_ADD", "register:40f0:8", ["const:bc3964:8", "const:4:8"]]
- 00bc3964 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bc3d8c ["INT_ADD", "register:40f0:8", ["const:bc3d8c:8", "const:4:8"]]
+ 00bc3d8c ["CALL", null, ["callee:00c57e90:8"]]
- 00bc3964 bytes 4b500294
+ 00bc3d8c bytes 41500294
- 00bc39fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:258:8"]]
- 00bc39fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
+ 00bc3e24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:658:8"]]
+ 00bc3e24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bc39fc bytes 012d01f9
+ 00bc3e24 bytes 012d03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d8ff6d20f69e59255c99a85bfd1a42e"></a>

### [`00bc43dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43dc.md) → [`00bc4804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4804.md) _ZNSt6__ndk16vectorIN8firebase8internal12EmbeddedFileENS_9allocatorIS3_EEEC2ERKS6_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d570.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5d970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d970.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 62.50% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4424"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc484c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bc4424"
      ],
      [
        "FALL_THROUGH",
        "00bc484c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bc4848",
      "incomplete_value": true,
      "site": "00bc4860",
      "value": [
        "INT_LESSEQUAL",
        "1",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:40b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4420",
      "incomplete_value": true,
      "site": "00bc4438",
      "value": [
        "INT_LESSEQUAL",
        "1",
        [
          [
            "INT_OR",
            "8",
            [
              "INT_AND",
              [
                "leaf",
                "const:aaa000000000000:8"
              ]
            ]
          ],
          [
            "INT_MULT",
            "8",
            [
              "INT_SRIGHT",
              "INT_OR"
            ]
          ]
        ]
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
      "unmatched:00bc4424",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc48b0"
      ]
    ]
  ],
  "added": [
    [
      "00bc484c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc48b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43dc.md#insn-00bc4424) · [`00bc4400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43dc.md#insn-00bc4400)
- 新版 `00bc484c`（命令位置の公開資料なし） · `00bc4828`（命令位置の公開資料なし）

~~~diff
- 00bc4424 ["CBRANCH", null, ["local:b6:8", "register:102:1"]]
- 00bc4424 bytes 22030054
+ 00bc484c ["CBRANCH", null, ["local:b8:8", "register:102:1"]]
+ 00bc484c bytes 22030054
- 00bc4400 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00bc4828 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00bc4400 bytes c0030054
+ 00bc4828 bytes c0030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80f5fe5deb999263c61668cc35976aec"></a>

### [`00bc4714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4714.md) → [`00bc4b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4b3c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal7CleanupEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d400.md) · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abd0.md)
- 新版 呼出元 1件 [`00c5d800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d800.md) · 呼出先 7件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5afd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afd0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 25.52% / 新版 25.52%

CFGの説明率　旧版 14.86% / 新版 14.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 2件, `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 27件, `unresolved_store_alignment` 19件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc4b70",
      "incomplete_value": true,
      "site": "00bc4b70",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4748",
      "incomplete_value": true,
      "site": "00bc4748",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:578:8"
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
      "definition_site": "00bc4b70",
      "incomplete_value": true,
      "site": "00bc4b70",
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
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4748",
      "incomplete_value": true,
      "site": "00bc4748",
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
            "const:4:8"
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
      "site": "00bc47c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc4b5c",
      "READ",
      [
        "storage",
        "00c9b578",
        null,
        "pointer"
      ]
    ],
    [
      "00bc4b6c",
      "PARAM",
      [
        "storage",
        "011262bc",
        null,
        null
      ]
    ],
    [
      "00bc4b70",
      "DATA",
      [
        "storage",
        "011262b8",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00bc4b5c",
      "READ",
      [
        "storage",
        "00c9b978",
        null,
        "pointer"
      ]
    ],
    [
      "00bc4b6c",
      "PARAM",
      [
        "storage",
        "011266bc",
        null,
        null
      ]
    ],
    [
      "00bc4b70",
      "DATA",
      [
        "storage",
        "011266b8",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc47c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4714.md#insn-00bc47c8) · [`00bc47e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4714.md#insn-00bc47e8) · [`00bc4814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4714.md#insn-00bc4814)

~~~diff
- 00bc47c8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc47c8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc47c8 ["INT_ADD", "tmp:2:8", ["register:40b0:8", "const:260:8"]]
- 00bc47c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc47c8 bytes df820939
- 00bc47e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
- 00bc47e8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bc47e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bc47e8 bytes 9f2e01f9
- 00bc4814 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc4814 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc4814 ["INT_ADD", "tmp:2:8", ["register:40b0:8", "const:80:8"]]
- 00bc4814 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc4814 bytes df020239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31a05f9205fd72178e982fae68802b3a"></a>

### [`00bc4c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4c34.md) → [`00bc505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc505c.md) FUN_00bc505c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bc4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4b04.md) [`00bc8d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8d4c.md) · 呼出先 4件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md) [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 2件 [`00bc4f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4f2c.md) [`00bc9174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9174.md) · 呼出先 4件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md) [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 69.39% / 新版 69.39%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4ca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc50d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5078",
      "incomplete_value": true,
      "site": "00bc5088",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4c50",
      "incomplete_value": true,
      "site": "00bc4c60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:168:8"
              ]
            ]
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
      "unmatched:00bc4c50",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc4c6c",
      "READ",
      [
        "storage",
        "01126178",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc50b4",
      "READ",
      [
        "storage",
        "01126180",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc5078",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc5094",
      "READ",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc50b4",
      "READ",
      [
        "storage",
        "01126580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4c34.md#insn-00bc4c60) · [`00bc4c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4c34.md#insn-00bc4c78) · [`00bc4ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4c34.md#insn-00bc4ca8)
- 新版 `00bc5088`（命令位置の公開資料なし） · `00bc50a0`（命令位置の公開資料なし）

~~~diff
- 00bc4c60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc4c60 ["INT_ADD", "register:40f0:8", ["const:bc4c60:8", "const:4:8"]]
- 00bc4c60 ["CALLIND", null, ["register:0:8"]]
+ 00bc5088 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc5088 ["INT_ADD", "register:40f0:8", ["const:bc5088:8", "const:4:8"]]
+ 00bc5088 ["CALLIND", null, ["register:0:8"]]
- 00bc4c60 bytes 00013fd6
+ 00bc5088 bytes 00013fd6
- 00bc4c78 ["INT_ADD", "register:40f0:8", ["const:bc4c78:8", "const:4:8"]]
- 00bc4c78 ["CALL", null, ["callee:0058f59c:8"]]
+ 00bc50a0 ["INT_ADD", "register:40f0:8", ["const:bc50a0:8", "const:4:8"]]
+ 00bc50a0 ["CALL", null, ["callee:0058f59c:8"]]
- 00bc4c78 bytes 392ae797
+ 00bc50a0 bytes 3f29e797
- 00bc4ca8 ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
- 00bc4ca8 bytes 22010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93f6f1c103e8e7618dcdf7bc6943dabb"></a>

### [`00bc4fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md) → [`00bc53d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc53d8.md) _ZN8firebase13remote_config8internal19SetDefaultsCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00bc5f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5f58.md) [`00bc61f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc61f0.md) [`00bc6904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6904.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5d4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4c0.md)
- 新版 呼出元 3件 [`00bc6380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6380.md) [`00bc6618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6618.md) [`00bc6d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6d2c.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5d8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 79.41% / 新版 71.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bc5080",
      "incomplete_value": true,
      "site": "00bc5084",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md#insn-00bc5084) · [`00bc4fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md#insn-00bc4fec) · [`00bc4ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md#insn-00bc4ffc)
- 新版 `00bc54ac`（命令位置の公開資料なし） · `00bc5414`（命令位置の公開資料なし） · `00bc5424`（命令位置の公開資料なし）

~~~diff
- 00bc5084 ["INT_ADD", "register:40f0:8", ["const:bc5084:8", "const:4:8"]]
- 00bc5084 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bc54ac ["INT_ADD", "register:40f0:8", ["const:bc54ac:8", "const:4:8"]]
+ 00bc54ac ["CALL", null, ["callee:00c57eb0:8"]]
- 00bc5084 bytes 8b4a0294
+ 00bc54ac bytes 814a0294
- 00bc4fec ["INT_ADD", "register:40f0:8", ["const:bc4fec:8", "const:4:8"]]
- 00bc4fec ["CALL", null, ["callee:00c5d8c0:8"]]
+ 00bc5414 ["INT_ADD", "register:40f0:8", ["const:bc5414:8", "const:4:8"]]
+ 00bc5414 ["CALL", null, ["callee:00c5d8c0:8"]]
- 00bc4fec bytes 35610294
+ 00bc5414 bytes 2b610294
- 00bc4ffc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc4ffc ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
+ 00bc5424 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00bc5424 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 00bc4ffc bytes 21090054
+ 00bc5424 bytes 21090054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecb37ab0bea8f860cca06747ed967d3c"></a>

### [`00bc52ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc52ac.md) → [`00bc56d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc56d4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17EnsureInitializedEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d340.md) · 呼出先 15件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4b04.md) [`00bc97ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc97ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5d740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d740.md) · 呼出先 15件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc4f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4f2c.md) [`00bc9c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9c14.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.94% / 新版 91.94%

CFGの説明率　旧版 75.86% / 新版 91.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc52b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc52b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc52b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc52b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc52b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc52b8",
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
      "00bc56d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bc56dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bc56e0",
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

- 旧版 [`00bc52b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc52ac.md#insn-00bc52b0) · [`00bc52b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc52ac.md#insn-00bc52b4) · [`00bc52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc52ac.md#insn-00bc52b8)

~~~diff
- 00bc52b0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00bc52b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00bc52b0 bytes fb2b00f9
- 00bc52b4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bc52b4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bc52b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00bc52b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc52b4 bytes fa6706a9
- 00bc52b8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bc52b8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bc52b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00bc52b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc52b8 bytes f85f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b6f180c45d62a623bcafccf0b727c09"></a>

### [`00bc55d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc55d8.md) → [`00bc5a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5a00.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal8ActivateEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d440.md) · 呼出先 15件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc4cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4cf8.md) [`00bc99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc99a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5d840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d840.md) · 呼出先 15件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc5120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5120.md) [`00bc9dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9dc8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5a44",
      "incomplete_value": true,
      "site": "00bc5a58",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc561c",
      "incomplete_value": true,
      "site": "00bc5630",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:590:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5a80",
      "incomplete_value": true,
      "site": "00bc5a88",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:498:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5658",
      "incomplete_value": true,
      "site": "00bc5660",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5aac",
      "incomplete_value": false,
      "site": "00bc5ac0",
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
            "const:e14:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5684",
      "incomplete_value": false,
      "site": "00bc5698",
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
            "const:dd4:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc5a44",
      "READ",
      [
        "storage",
        "00c9b590",
        null,
        "pointer"
      ]
    ],
    [
      "00bc5a44",
      "PARAM",
      [
        "storage",
        "00bc99a0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00bc5a80",
      "READ",
      [
        "storage",
        "01126098",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc5a44",
      "READ",
      [
        "storage",
        "00c9b990",
        null,
        "pointer"
      ]
    ],
    [
      "00bc5a44",
      "PARAM",
      [
        "storage",
        "00bc9dc8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00bc5a80",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc55d8.md#insn-00bc5630) · [`00bc5660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc55d8.md#insn-00bc5660) · [`00bc5698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc55d8.md#insn-00bc5698)
- 新版 `00bc5a58`（命令位置の公開資料なし） · `00bc5a88`（命令位置の公開資料なし） · `00bc5ac0`（命令位置の公開資料なし）

~~~diff
- 00bc5630 ["INT_ADD", "register:40f0:8", ["const:bc5630:8", "const:4:8"]]
- 00bc5630 ["CALL", null, ["callee:00c5ae40:8"]]
+ 00bc5a58 ["INT_ADD", "register:40f0:8", ["const:bc5a58:8", "const:4:8"]]
+ 00bc5a58 ["CALL", null, ["callee:00c5ae40:8"]]
- 00bc5630 bytes 04550294
+ 00bc5a58 bytes fa540294
- 00bc5660 ["INT_ADD", "register:40f0:8", ["const:bc5660:8", "const:4:8"]]
- 00bc5660 ["CALL", null, ["callee:00497834:8"]]
+ 00bc5a88 ["INT_ADD", "register:40f0:8", ["const:bc5a88:8", "const:4:8"]]
+ 00bc5a88 ["CALL", null, ["callee:00497834:8"]]
- 00bc5660 bytes 6548e397
+ 00bc5a88 bytes 6b47e397
- 00bc5698 ["INT_ADD", "register:40f0:8", ["const:bc5698:8", "const:4:8"]]
- 00bc5698 ["CALL", null, ["callee:00c5d900:8"]]
+ 00bc5ac0 ["INT_ADD", "register:40f0:8", ["const:bc5ac0:8", "const:4:8"]]
+ 00bc5ac0 ["CALL", null, ["callee:00c5d900:8"]]
- 00bc5698 bytes 9a5f0294
+ 00bc5ac0 bytes 905f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f65a40ad999e36b8eb9eef331a33095"></a>

### [`00bc5904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5904.md) → [`00bc5d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5d2c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal16FetchAndActivateEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d320.md) · 呼出先 15件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc4cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4cf8.md) [`00bc99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc99a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5d720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d720.md) · 呼出先 15件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc5120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5120.md) [`00bc9dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9dc8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5d70",
      "incomplete_value": true,
      "site": "00bc5d84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5948",
      "incomplete_value": true,
      "site": "00bc595c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:590:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5dac",
      "incomplete_value": true,
      "site": "00bc5db4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:4a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5984",
      "incomplete_value": true,
      "site": "00bc598c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5dd8",
      "incomplete_value": false,
      "site": "00bc5dec",
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
            "const:791:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc59b0",
      "incomplete_value": false,
      "site": "00bc59c4",
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
            "const:751:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc5d70",
      "READ",
      [
        "storage",
        "00c9b590",
        null,
        "pointer"
      ]
    ],
    [
      "00bc5d70",
      "PARAM",
      [
        "storage",
        "00bc99a0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00bc5dac",
      "READ",
      [
        "storage",
        "011260a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc5d70",
      "READ",
      [
        "storage",
        "00c9b990",
        null,
        "pointer"
      ]
    ],
    [
      "00bc5d70",
      "PARAM",
      [
        "storage",
        "00bc9dc8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00bc5dac",
      "READ",
      [
        "storage",
        "011264a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc595c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5904.md#insn-00bc595c) · [`00bc598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5904.md#insn-00bc598c) · [`00bc59c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5904.md#insn-00bc59c4)
- 新版 `00bc5d84`（命令位置の公開資料なし） · `00bc5db4`（命令位置の公開資料なし） · `00bc5dec`（命令位置の公開資料なし）

~~~diff
- 00bc595c ["INT_ADD", "register:40f0:8", ["const:bc595c:8", "const:4:8"]]
- 00bc595c ["CALL", null, ["callee:00c5ae40:8"]]
+ 00bc5d84 ["INT_ADD", "register:40f0:8", ["const:bc5d84:8", "const:4:8"]]
+ 00bc5d84 ["CALL", null, ["callee:00c5ae40:8"]]
- 00bc595c bytes 39540294
+ 00bc5d84 bytes 2f540294
- 00bc598c ["INT_ADD", "register:40f0:8", ["const:bc598c:8", "const:4:8"]]
- 00bc598c ["CALL", null, ["callee:00497834:8"]]
+ 00bc5db4 ["INT_ADD", "register:40f0:8", ["const:bc5db4:8", "const:4:8"]]
+ 00bc5db4 ["CALL", null, ["callee:00497834:8"]]
- 00bc598c bytes 9a47e397
+ 00bc5db4 bytes a046e397
- 00bc59c4 ["INT_ADD", "register:40f0:8", ["const:bc59c4:8", "const:4:8"]]
- 00bc59c4 ["CALL", null, ["callee:00c5d900:8"]]
+ 00bc5dec ["INT_ADD", "register:40f0:8", ["const:bc5dec:8", "const:4:8"]]
+ 00bc5dec ["CALL", null, ["callee:00c5d900:8"]]
- 00bc59c4 bytes cf5e0294
+ 00bc5dec bytes c55e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12eaa6dd04ccae1c78614be69232ab0f"></a>

### [`00bc5c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5c30.md) → [`00bc6058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6058.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal5FetchEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3e0.md) · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc4f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4f30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5d7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7e0.md) · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc5358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5358.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc60d0",
      "incomplete_value": true,
      "site": "00bc60dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5ca8",
      "incomplete_value": true,
      "site": "00bc5cb4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:108:8"
              ]
            ]
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
      "definition_site": "00bc6100",
      "incomplete_value": false,
      "site": "00bc6114",
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
            "const:3bf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5cd8",
      "incomplete_value": false,
      "site": "00bc5cec",
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
            "const:2e3:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc61d0",
      "incomplete_value": true,
      "site": "00bc61e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5da8",
      "incomplete_value": true,
      "site": "00bc5db8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:558:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc60d0",
      "READ",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc6100",
      "PARAM",
      [
        "storage",
        "002a72e3",
        null,
        "string"
      ]
    ],
    [
      "00bc61d0",
      "READ",
      [
        "storage",
        "00c9b558",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bc60d0",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc6100",
      "PARAM",
      [
        "storage",
        "002a73bf",
        null,
        "string"
      ]
    ],
    [
      "00bc61d0",
      "READ",
      [
        "storage",
        "00c9b958",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5c30.md#insn-00bc5cb4) · [`00bc5cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5c30.md#insn-00bc5cec) · [`00bc5db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5c30.md#insn-00bc5db8)
- 新版 `00bc60dc`（命令位置の公開資料なし） · `00bc6114`（命令位置の公開資料なし） · `00bc61e0`（命令位置の公開資料なし）

~~~diff
- 00bc5cb4 ["INT_ADD", "register:40f0:8", ["const:bc5cb4:8", "const:4:8"]]
- 00bc5cb4 ["CALL", null, ["callee:00497834:8"]]
+ 00bc60dc ["INT_ADD", "register:40f0:8", ["const:bc60dc:8", "const:4:8"]]
+ 00bc60dc ["CALL", null, ["callee:00497834:8"]]
- 00bc5cb4 bytes d046e397
+ 00bc60dc bytes d645e397
- 00bc5cec ["INT_ADD", "register:40f0:8", ["const:bc5cec:8", "const:4:8"]]
- 00bc5cec ["CALL", null, ["callee:00c5ada0:8"]]
+ 00bc6114 ["INT_ADD", "register:40f0:8", ["const:bc6114:8", "const:4:8"]]
+ 00bc6114 ["CALL", null, ["callee:00c5ada0:8"]]
- 00bc5cec bytes 2d530294
+ 00bc6114 bytes 23530294
- 00bc5db8 ["INT_ADD", "register:40f0:8", ["const:bc5db8:8", "const:4:8"]]
- 00bc5db8 ["CALL", null, ["callee:00c5af40:8"]]
+ 00bc61e0 ["INT_ADD", "register:40f0:8", ["const:bc61e0:8", "const:4:8"]]
+ 00bc61e0 ["CALL", null, ["callee:00c5af40:8"]]
- 00bc5db8 bytes 62530294
+ 00bc61e0 bytes 58530294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de9a7226fee7b9b20215c0cd85d36ae9"></a>

### [`00bc5f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5f58.md) → [`00bc6380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6380.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d2f0.md) · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc4fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5d6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d6f0.md) · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc53d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc53d8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc63f8",
      "incomplete_value": true,
      "site": "00bc6404",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:4a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5fd0",
      "incomplete_value": true,
      "site": "00bc5fdc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:a8:8"
              ]
            ]
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
      "definition_site": "00bc6428",
      "incomplete_value": false,
      "site": "00bc643c",
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
            "const:bbb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6000",
      "incomplete_value": false,
      "site": "00bc6014",
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
            "const:b7b:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc64f8",
      "incomplete_value": true,
      "site": "00bc6508",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:968:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc60d0",
      "incomplete_value": true,
      "site": "00bc60e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc63f8",
      "READ",
      [
        "storage",
        "011260a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc6428",
      "PARAM",
      [
        "storage",
        "002c0b7b",
        null,
        "string"
      ]
    ],
    [
      "00bc64f8",
      "READ",
      [
        "storage",
        "00c9b568",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bc63f8",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc6428",
      "PARAM",
      [
        "storage",
        "002c0bbb",
        null,
        "string"
      ]
    ],
    [
      "00bc64f8",
      "READ",
      [
        "storage",
        "00c9b968",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5f58.md#insn-00bc5fdc) · [`00bc6014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5f58.md#insn-00bc6014) · [`00bc60e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5f58.md#insn-00bc60e0)
- 新版 `00bc6404`（命令位置の公開資料なし） · `00bc643c`（命令位置の公開資料なし） · `00bc6508`（命令位置の公開資料なし）

~~~diff
- 00bc5fdc ["INT_ADD", "register:40f0:8", ["const:bc5fdc:8", "const:4:8"]]
- 00bc5fdc ["CALL", null, ["callee:00497834:8"]]
+ 00bc6404 ["INT_ADD", "register:40f0:8", ["const:bc6404:8", "const:4:8"]]
+ 00bc6404 ["CALL", null, ["callee:00497834:8"]]
- 00bc5fdc bytes 0646e397
+ 00bc6404 bytes 0c45e397
- 00bc6014 ["INT_ADD", "register:40f0:8", ["const:bc6014:8", "const:4:8"]]
- 00bc6014 ["CALL", null, ["callee:00c5ada0:8"]]
+ 00bc643c ["INT_ADD", "register:40f0:8", ["const:bc643c:8", "const:4:8"]]
+ 00bc643c ["CALL", null, ["callee:00c5ada0:8"]]
- 00bc6014 bytes 63520294
+ 00bc643c bytes 59520294
- 00bc60e0 ["INT_ADD", "register:40f0:8", ["const:bc60e0:8", "const:4:8"]]
- 00bc60e0 ["CALL", null, ["callee:00c5af40:8"]]
+ 00bc6508 ["INT_ADD", "register:40f0:8", ["const:bc6508:8", "const:4:8"]]
+ 00bc6508 ["CALL", null, ["callee:00c5af40:8"]]
- 00bc60e0 bytes 98520294
+ 00bc6508 bytes 8e520294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ea82e772199a476231db7cd95ef4a23"></a>

### [`00bc61f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc61f0.md) → [`00bc6618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6618.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEPKNS0_21ConfigKeyValueVariantEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5d2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d2e0.md) · 呼出先 33件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00bc4fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5d6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d6e0.md) · 呼出先 33件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00bc53d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc53d8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.38% / 新版 98.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc68ec",
      "incomplete_value": false,
      "site": "00bc68f0",
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
            "const:816:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc64c4",
      "incomplete_value": false,
      "site": "00bc64c8",
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
            "const:749:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc69f8",
      "incomplete_value": true,
      "site": "00bc6a04",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "definition_site": "00bc65d0",
      "incomplete_value": true,
      "site": "00bc65dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc6a2c",
      "incomplete_value": false,
      "site": "00bc6a40",
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
            "const:bbb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6604",
      "incomplete_value": false,
      "site": "00bc6618",
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
            "const:b7b:8"
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc6710",
      "DATA",
      [
        "storage",
        "0030e95a",
        "switchD_00bc62f0::switchdataD_0030e95a",
        "byte"
      ]
    ],
    [
      "00bc68ec",
      "PARAM",
      [
        "storage",
        "002a8749",
        null,
        "string"
      ]
    ],
    [
      "00bc69f8",
      "READ",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc6710",
      "DATA",
      [
        "storage",
        "0030e99a",
        "switchD_00bc6718::switchdataD_0030e99a",
        "byte"
      ]
    ],
    [
      "00bc68ec",
      "PARAM",
      [
        "storage",
        "002a8816",
        null,
        "string"
      ]
    ],
    [
      "00bc69f8",
      "READ",
      [
        "storage",
        "011264b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc62c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc61f0.md#insn-00bc62c0) · [`00bc64c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc61f0.md#insn-00bc64c8) · [`00bc65dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc61f0.md#insn-00bc65dc)
- 新版 `00bc66e8`（命令位置の公開資料なし） · `00bc68f0`（命令位置の公開資料なし） · `00bc6a04`（命令位置の公開資料なし）

~~~diff
- 00bc62c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc62c0 ["INT_ADD", "register:40f0:8", ["const:bc62c0:8", "const:4:8"]]
- 00bc62c0 ["CALLIND", null, ["register:0:8"]]
+ 00bc66e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc66e8 ["INT_ADD", "register:40f0:8", ["const:bc66e8:8", "const:4:8"]]
+ 00bc66e8 ["CALLIND", null, ["register:0:8"]]
- 00bc62c0 bytes 00013fd6
+ 00bc66e8 bytes 00013fd6
- 00bc64c8 ["INT_ADD", "register:40f0:8", ["const:bc64c8:8", "const:4:8"]]
- 00bc64c8 ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bc68f0 ["INT_ADD", "register:40f0:8", ["const:bc68f0:8", "const:4:8"]]
+ 00bc68f0 ["CALL", null, ["callee:00c5aca0:8"]]
- 00bc64c8 bytes f6500294
+ 00bc68f0 bytes ec500294
- 00bc65dc ["INT_ADD", "register:40f0:8", ["const:bc65dc:8", "const:4:8"]]
- 00bc65dc ["CALL", null, ["callee:00497834:8"]]
+ 00bc6a04 ["INT_ADD", "register:40f0:8", ["const:bc6a04:8", "const:4:8"]]
+ 00bc6a04 ["CALL", null, ["callee:00497834:8"]]
- 00bc65dc bytes 8644e397
+ 00bc6a04 bytes 8c43e397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0c4e7d11cf93a874015965cbec8d590"></a>

### [`00bc6904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6904.md) → [`00bc6d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6d2c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEPKNS0_14ConfigKeyValueEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d2d0.md) · 呼出先 21件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00bc4fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5d6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d6d0.md) · 呼出先 21件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00bc53d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc53d8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.60% / 新版 99.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc6f20",
      "incomplete_value": true,
      "site": "00bc6f2c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "definition_site": "00bc6af8",
      "incomplete_value": true,
      "site": "00bc6b04",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc6f54",
      "incomplete_value": false,
      "site": "00bc6f68",
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
            "const:bbb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6b2c",
      "incomplete_value": false,
      "site": "00bc6b40",
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
            "const:b7b:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7028",
      "incomplete_value": true,
      "site": "00bc7038",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:968:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6c00",
      "incomplete_value": true,
      "site": "00bc6c10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc6f20",
      "READ",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc6f54",
      "PARAM",
      [
        "storage",
        "002c0b7b",
        null,
        "string"
      ]
    ],
    [
      "00bc7028",
      "READ",
      [
        "storage",
        "00c9b568",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bc6f20",
      "READ",
      [
        "storage",
        "011264b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc6f54",
      "PARAM",
      [
        "storage",
        "002c0bbb",
        null,
        "string"
      ]
    ],
    [
      "00bc7028",
      "READ",
      [
        "storage",
        "00c9b968",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6904.md#insn-00bc6b04) · [`00bc6b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6904.md#insn-00bc6b40) · [`00bc6c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6904.md#insn-00bc6c10)
- 新版 `00bc6f2c`（命令位置の公開資料なし） · `00bc6f68`（命令位置の公開資料なし） · `00bc7038`（命令位置の公開資料なし）

~~~diff
- 00bc6b04 ["INT_ADD", "register:40f0:8", ["const:bc6b04:8", "const:4:8"]]
- 00bc6b04 ["CALL", null, ["callee:00497834:8"]]
+ 00bc6f2c ["INT_ADD", "register:40f0:8", ["const:bc6f2c:8", "const:4:8"]]
+ 00bc6f2c ["CALL", null, ["callee:00497834:8"]]
- 00bc6b04 bytes 3c43e397
+ 00bc6f2c bytes 4242e397
- 00bc6b40 ["INT_ADD", "register:40f0:8", ["const:bc6b40:8", "const:4:8"]]
- 00bc6b40 ["CALL", null, ["callee:00c5ada0:8"]]
+ 00bc6f68 ["INT_ADD", "register:40f0:8", ["const:bc6f68:8", "const:4:8"]]
+ 00bc6f68 ["CALL", null, ["callee:00c5ada0:8"]]
- 00bc6b40 bytes 984f0294
+ 00bc6f68 bytes 8e4f0294
- 00bc6c10 ["INT_ADD", "register:40f0:8", ["const:bc6c10:8", "const:4:8"]]
- 00bc6c10 ["CALL", null, ["callee:00c5af40:8"]]
+ 00bc7038 ["INT_ADD", "register:40f0:8", ["const:bc7038:8", "const:4:8"]]
+ 00bc7038 ["CALL", null, ["callee:00c5af40:8"]]
- 00bc6c10 bytes cc4f0294
+ 00bc7038 bytes c24f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c360afddf709fe926dcd1dcf4c5f9429"></a>

### [`00bc6ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6ec0.md) → [`00bc72e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc72e8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17SetConfigSettingsENS0_14ConfigSettingsE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d360.md) · 呼出先 15件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00bc4e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4e28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5d760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d760.md) · 呼出先 15件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00bc5250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5250.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.35% / 新版 97.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7364",
      "incomplete_value": true,
      "site": "00bc7370",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6f3c",
      "incomplete_value": true,
      "site": "00bc6f48",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:1c0:8"
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
      "definition_site": "00bc7368",
      "incomplete_value": true,
      "site": "00bc7370",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:5d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6f40",
      "incomplete_value": true,
      "site": "00bc6f48",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:1d0:8"
              ]
            ]
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
      "definition_site": "00bc7384",
      "incomplete_value": true,
      "site": "00bc73a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:5e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6f5c",
      "incomplete_value": true,
      "site": "00bc6f7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:1e0:8"
              ]
            ]
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
      "00bc7364",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7368",
      "READ",
      [
        "storage",
        "011261d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7384",
      "READ",
      [
        "storage",
        "011261e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc7364",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7368",
      "READ",
      [
        "storage",
        "011265d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7384",
      "READ",
      [
        "storage",
        "011265e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6ec0.md#insn-00bc6f48) · [`00bc6f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6ec0.md#insn-00bc6f7c) · [`00bc6fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6ec0.md#insn-00bc6fa4)
- 新版 `00bc7370`（命令位置の公開資料なし） · `00bc73a4`（命令位置の公開資料なし） · `00bc73cc`（命令位置の公開資料なし）

~~~diff
- 00bc6f48 ["INT_ADD", "register:40f0:8", ["const:bc6f48:8", "const:4:8"]]
- 00bc6f48 ["CALL", null, ["callee:005896f4:8"]]
+ 00bc7370 ["INT_ADD", "register:40f0:8", ["const:bc7370:8", "const:4:8"]]
+ 00bc7370 ["CALL", null, ["callee:005896f4:8"]]
- 00bc6f48 bytes db09e797
+ 00bc7370 bytes e108e797
- 00bc6f7c ["INT_ADD", "register:40f0:8", ["const:bc6f7c:8", "const:4:8"]]
- 00bc6f7c ["CALL", null, ["callee:00497834:8"]]
+ 00bc73a4 ["INT_ADD", "register:40f0:8", ["const:bc73a4:8", "const:4:8"]]
+ 00bc73a4 ["CALL", null, ["callee:00497834:8"]]
- 00bc6f7c bytes 1e42e397
+ 00bc73a4 bytes 2441e397
- 00bc6fa4 ["INT_ADD", "register:40f0:8", ["const:bc6fa4:8", "const:4:8"]]
- 00bc6fa4 ["CALL", null, ["callee:00497834:8"]]
+ 00bc73cc ["INT_ADD", "register:40f0:8", ["const:bc73cc:8", "const:4:8"]]
+ 00bc73cc ["CALL", null, ["callee:00497834:8"]]
- 00bc6fa4 bytes 1442e397
+ 00bc73cc bytes 1a41e397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-326186879e095a95f7e9c1e871ececb1"></a>

### [`00bc7314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7314.md) → [`00bc773c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc773c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal16SetCustomSignalsERKNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d330.md) · 呼出先 18件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00bc4e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4e28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5d730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d730.md) · 呼出先 18件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00bc5250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5250.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.49% / 新版 94.49%

CFGの説明率　旧版 69.52% / 新版 69.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc734c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc7774"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7780",
      "incomplete_value": true,
      "site": "00bc778c",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": {
      "definition_site": "00bc7358",
      "incomplete_value": true,
      "site": "00bc7364",
      "value": [
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
      "unmatched:00bc734c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc738c",
      "READ",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc7390",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc7774",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00bc77b4",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc77b8",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc734c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7314.md#insn-00bc734c) · [`00bc7364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7314.md#insn-00bc7364) · [`00bc7398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7314.md#insn-00bc7398)
- 新版 `00bc778c`（命令位置の公開資料なし） · `00bc77c0`（命令位置の公開資料なし）

~~~diff
- 00bc734c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc734c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa8:8"]]
- 00bc734c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bc734c bytes a8831af8
- 00bc7364 ["INT_ADD", "register:40f0:8", ["const:bc7364:8", "const:4:8"]]
- 00bc7364 ["CALL", null, ["callee:00c5ae40:8"]]
+ 00bc778c ["INT_ADD", "register:40f0:8", ["const:bc778c:8", "const:4:8"]]
+ 00bc778c ["CALL", null, ["callee:00c5ae40:8"]]
- 00bc7364 bytes b74d0294
+ 00bc778c bytes ad4d0294
- 00bc7398 ["INT_ADD", "register:40f0:8", ["const:bc7398:8", "const:4:8"]]
- 00bc7398 ["CALL", null, ["callee:005896f4:8"]]
+ 00bc77c0 ["INT_ADD", "register:40f0:8", ["const:bc77c0:8", "const:4:8"]]
+ 00bc77c0 ["CALL", null, ["callee:005896f4:8"]]
- 00bc7398 bytes c708e797
+ 00bc77c0 bytes cd07e797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

