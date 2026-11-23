# v16.0.0 → v16.0.1 · 最優先の変更候補 (83)

[一覧の目次](README.md)

<a id="compare-99b26054188c3487e740c135b0872b9d"></a>

### [`00bd2488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2488.md) → [`00bd28b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd28b0.md) _ZN8firebase4auth21android_web_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd2908",
      "incomplete_value": true,
      "site": "00bd2908",
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
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd24e0",
      "incomplete_value": true,
      "site": "00bd24e0",
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
            "const:5b0:8"
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
      "definition_site": "00bd28e4",
      "incomplete_value": true,
      "site": "00bd28f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd24bc",
      "incomplete_value": true,
      "site": "00bd24c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5a8:8"
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
      "00bd28c4",
      "READ",
      [
        "storage",
        "011265b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd28e4",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2908",
      "WRITE",
      [
        "storage",
        "011265b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd28c4",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd28e4",
      "READ",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2908",
      "WRITE",
      [
        "storage",
        "011269b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd24c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2488.md#insn-00bd24c8) · [`00bd24e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2488.md#insn-00bd24e0) · [`00bd249c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2488.md#insn-00bd249c)
- 新版 `00bd28f0`（命令位置の公開資料なし） · `00bd2908`（命令位置の公開資料なし） · `00bd28c4`（命令位置の公開資料なし）

~~~diff
- 00bd24c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd24c8 ["INT_ADD", "register:40f0:8", ["const:bd24c8:8", "const:4:8"]]
- 00bd24c8 ["CALLIND", null, ["register:0:8"]]
+ 00bd28f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd28f0 ["INT_ADD", "register:40f0:8", ["const:bd28f0:8", "const:4:8"]]
+ 00bd28f0 ["CALLIND", null, ["register:0:8"]]
- 00bd24c8 bytes 00013fd6
+ 00bd28f0 bytes 00013fd6
- 00bd24e0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd24e0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5b0:8"]]
- 00bd24e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd2908 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd2908 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9b0:8"]]
+ 00bd2908 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd24e0 bytes a0c21639
+ 00bd2908 bytes a0c22639
- 00bd249c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5b0:8"]]
- 00bd249c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd249c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd28c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b0:8"]]
+ 00bd28c4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd28c4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd249c bytes a8c25639
+ 00bd28c4 bytes a8c26639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a8eeb585a12fc0d8c33e03896f9d7b2"></a>

### [`00bd24f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd24f4.md) → [`00bd291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd291c.md) _ZN8firebase4auth21android_web_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd2958",
      "incomplete_value": true,
      "site": "00bd2958",
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
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2530",
      "incomplete_value": true,
      "site": "00bd2530",
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
            "const:5b0:8"
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
      "definition_site": "00bd2978",
      "incomplete_value": true,
      "site": "00bd2978",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2550",
      "incomplete_value": true,
      "site": "00bd2550",
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
            "const:5a8:8"
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
      "definition_site": "00bd2934",
      "incomplete_value": true,
      "site": "00bd2934",
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
      "definition_site": "00bd250c",
      "incomplete_value": true,
      "site": "00bd250c",
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
      "00bd2930",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd293c",
      "READ",
      [
        "storage",
        "011265b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2958",
      "WRITE",
      [
        "storage",
        "011265b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd2930",
      "READ",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd293c",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2958",
      "WRITE",
      [
        "storage",
        "011269b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd24f4.md#insn-00bd2530) · [`00bd254c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd24f4.md#insn-00bd254c) · [`00bd2550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd24f4.md#insn-00bd2550)
- 新版 `00bd2958`（命令位置の公開資料なし） · `00bd2974`（命令位置の公開資料なし） · `00bd2978`（命令位置の公開資料なし）

~~~diff
- 00bd2530 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd2530 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd2530 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5b0:8"]]
- 00bd2530 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd2958 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd2958 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd2958 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9b0:8"]]
+ 00bd2958 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd2530 bytes bfc21639
+ 00bd2958 bytes bfc22639
- 00bd254c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd254c ["INT_ADD", "register:40f0:8", ["const:bd254c:8", "const:4:8"]]
- 00bd254c ["CALLIND", null, ["register:0:8"]]
+ 00bd2974 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2974 ["INT_ADD", "register:40f0:8", ["const:bd2974:8", "const:4:8"]]
+ 00bd2974 ["CALLIND", null, ["register:0:8"]]
- 00bd254c bytes 00013fd6
+ 00bd2974 bytes 00013fd6
- 00bd2550 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00bd2550 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bd2550 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd2978 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00bd2978 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd2978 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bd2550 bytes 9fd602f9
+ 00bd2978 bytes 9fd604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a3e757f5924f6abd7b8e1d9a439f987"></a>

### [`00bd2564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2564.md) → [`00bd298c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd298c.md) _ZN8firebase4auth21android_web_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd29cc",
      "incomplete_value": true,
      "site": "00bd29cc",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd25a4",
      "incomplete_value": true,
      "site": "00bd25a4",
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
            "const:5a8:8"
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
      "definition_site": "00bd29a8",
      "incomplete_value": true,
      "site": "00bd29a8",
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
      "definition_site": "00bd2580",
      "incomplete_value": true,
      "site": "00bd2580",
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
      "definition_site": "00bd29b0",
      "incomplete_value": false,
      "site": "00bd29c4",
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
            "const:d55:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2588",
      "incomplete_value": false,
      "site": "00bd259c",
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
            "const:c88:8"
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
      "00bd29a0",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd29b0",
      "PARAM",
      [
        "storage",
        "002a0c88",
        null,
        "string"
      ]
    ],
    [
      "00bd29cc",
      "WRITE",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd29a0",
      "READ",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd29b0",
      "PARAM",
      [
        "storage",
        "002a0d55",
        null,
        "string"
      ]
    ],
    [
      "00bd29cc",
      "WRITE",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd259c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2564.md#insn-00bd259c) · [`00bd25a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2564.md#insn-00bd25a4) · [`00bd2578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2564.md#insn-00bd2578)
- 新版 `00bd29c4`（命令位置の公開資料なし） · `00bd29cc`（命令位置の公開資料なし） · `00bd29a0`（命令位置の公開資料なし）

~~~diff
- 00bd259c ["INT_ADD", "register:40f0:8", ["const:bd259c:8", "const:4:8"]]
- 00bd259c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd29c4 ["INT_ADD", "register:40f0:8", ["const:bd29c4:8", "const:4:8"]]
+ 00bd29c4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd259c bytes 5d210294
+ 00bd29c4 bytes 53210294
- 00bd25a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00bd25a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd29cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00bd29cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd25a4 bytes 80d602f9
+ 00bd29cc bytes 80d604f9
- 00bd2578 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00bd2578 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd29a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00bd29a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2578 bytes 81d642f9
+ 00bd29a0 bytes 81d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b491294f68c2898fa7fa8e522eed08ff"></a>

### [`00bd25d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd25d4.md) → [`00bd29fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd29fc.md) _ZN8firebase4auth21android_web_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd2a18",
      "incomplete_value": false,
      "site": "00bd2a1c",
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
      "definition_site": "00bd25f0",
      "incomplete_value": false,
      "site": "00bd25f4",
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
      "definition_site": "00bd2a28",
      "incomplete_value": true,
      "site": "00bd2a34",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd2600",
      "incomplete_value": true,
      "site": "00bd260c",
      "value": [
        "LOAD",
        "8",
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
      "00bd2a18",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd2a28",
      "DATA",
      [
        "storage",
        "011265b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd2a18",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd2a28",
      "DATA",
      [
        "storage",
        "011269b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd25f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd25d4.md#insn-00bd25f4) · [`00bd25f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd25d4.md#insn-00bd25f0) · [`00bd25fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd25d4.md#insn-00bd25fc)
- 新版 `00bd2a1c`（命令位置の公開資料なし） · `00bd2a18`（命令位置の公開資料なし） · `00bd2a24`（命令位置の公開資料なし）

~~~diff
- 00bd25f4 ["INT_ADD", "register:40f0:8", ["const:bd25f4:8", "const:4:8"]]
- 00bd25f4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd2a1c ["INT_ADD", "register:40f0:8", ["const:bd2a1c:8", "const:4:8"]]
+ 00bd2a1c ["CALL", null, ["callee:00c5b000:8"]]
- 00bd25f4 bytes 83210294
+ 00bd2a1c bytes 79210294
- 00bd25f0 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd25f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd25f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd25f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd2a18 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd2a18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2a18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2a18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd25f0 bytes 00680a91
+ 00bd2a18 bytes 009c0d91
- 00bd25fc ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 00bd25fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd25fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd25fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd2a24 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00bd2a24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2a24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2a24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd25fc bytes 08e11691
+ 00bd2a24 bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbf0f7544b7c4a14aa11258f7445365d"></a>

### [`00bd2610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2610.md) → [`00bd2a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2a38.md) _ZN8firebase4auth21android_web_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd2a78",
      "incomplete_value": true,
      "site": "00bd2a78",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2650",
      "incomplete_value": true,
      "site": "00bd2650",
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
            "const:5a8:8"
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
      "definition_site": "00bd2a54",
      "incomplete_value": true,
      "site": "00bd2a54",
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
      "definition_site": "00bd262c",
      "incomplete_value": true,
      "site": "00bd262c",
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
      "definition_site": "00bd2a5c",
      "incomplete_value": false,
      "site": "00bd2a70",
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
            "const:d55:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2634",
      "incomplete_value": false,
      "site": "00bd2648",
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
            "const:c88:8"
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
      "00bd2a4c",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2a5c",
      "PARAM",
      [
        "storage",
        "002a0c88",
        null,
        "string"
      ]
    ],
    [
      "00bd2a78",
      "WRITE",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2a4c",
      "READ",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2a5c",
      "PARAM",
      [
        "storage",
        "002a0d55",
        null,
        "string"
      ]
    ],
    [
      "00bd2a78",
      "WRITE",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2610.md#insn-00bd2648) · [`00bd2650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2610.md#insn-00bd2650) · [`00bd2624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2610.md#insn-00bd2624)
- 新版 `00bd2a70`（命令位置の公開資料なし） · `00bd2a78`（命令位置の公開資料なし） · `00bd2a4c`（命令位置の公開資料なし）

~~~diff
- 00bd2648 ["INT_ADD", "register:40f0:8", ["const:bd2648:8", "const:4:8"]]
- 00bd2648 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2a70 ["INT_ADD", "register:40f0:8", ["const:bd2a70:8", "const:4:8"]]
+ 00bd2a70 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2648 bytes 32210294
+ 00bd2a70 bytes 28210294
- 00bd2650 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00bd2650 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2a78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00bd2a78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2650 bytes 80d602f9
+ 00bd2a78 bytes 80d604f9
- 00bd2624 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00bd2624 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd2a4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00bd2a4c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2624 bytes 81d642f9
+ 00bd2a4c bytes 81d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad7a74c4f95c42c7a5020255b63f6fd0"></a>

### [`00bd2680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2680.md) → [`00bd2aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2aa8.md) _ZN8firebase4auth21android_web_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd2ac4",
      "incomplete_value": false,
      "site": "00bd2ac8",
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
      "definition_site": "00bd269c",
      "incomplete_value": false,
      "site": "00bd26a0",
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
      "definition_site": "00bd2ad4",
      "incomplete_value": true,
      "site": "00bd2ae0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd26ac",
      "incomplete_value": true,
      "site": "00bd26b8",
      "value": [
        "LOAD",
        "8",
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
      "00bd2ac4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd2ad4",
      "DATA",
      [
        "storage",
        "011265c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd2ac4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd2ad4",
      "DATA",
      [
        "storage",
        "011269c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd26a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2680.md#insn-00bd26a0) · [`00bd269c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2680.md#insn-00bd269c) · [`00bd26a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2680.md#insn-00bd26a8)
- 新版 `00bd2ac8`（命令位置の公開資料なし） · `00bd2ac4`（命令位置の公開資料なし） · `00bd2ad0`（命令位置の公開資料なし）

~~~diff
- 00bd26a0 ["INT_ADD", "register:40f0:8", ["const:bd26a0:8", "const:4:8"]]
- 00bd26a0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd2ac8 ["INT_ADD", "register:40f0:8", ["const:bd2ac8:8", "const:4:8"]]
+ 00bd2ac8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd26a0 bytes 58210294
+ 00bd2ac8 bytes 4e210294
- 00bd269c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd269c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd269c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd269c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd2ac4 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd2ac4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2ac4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2ac4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd269c bytes 00441191
+ 00bd2ac4 bytes 00781491
- 00bd26a8 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 00bd26a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd26a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd26a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd2ad0 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00bd2ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd26a8 bytes 08011791
+ 00bd2ad0 bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7676721c143150f445751a1258859fef"></a>

### [`00bd26bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd26bc.md) → [`00bd2ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2ae4.md) _ZN8firebase4auth23firebase_auth_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "site": "00bd26e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2b10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd2af8",
      "incomplete_value": true,
      "site": "00bd2af8",
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
      "definition_site": "00bd26d0",
      "incomplete_value": true,
      "site": "00bd26d0",
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
      "00bd2af4",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2af8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd26ec"
      ]
    ],
    [
      "unmatched:00bd26dc",
      "PARAM",
      [
        "storage",
        "002be88d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd2af4",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2af8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2b14"
      ]
    ],
    [
      "00bd2b04",
      "PARAM",
      [
        "storage",
        "002be8cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd26d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd26bc.md#insn-00bd26d0) · [`00bd26e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd26bc.md#insn-00bd26e0) · [`00bd26e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd26bc.md#insn-00bd26e8)
- 新版 `00bd2af8`（命令位置の公開資料なし）

~~~diff
- 00bd26d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd26d0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd2af8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd2af8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd26d0 bytes e80000b5
+ 00bd2af8 bytes e80000b5
- 00bd26e0 ["INT_ADD", "register:40f0:8", ["const:bd26e0:8", "const:4:8"]]
- 00bd26e0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd26e0 bytes 0c210294
- 00bd26e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c8:8"]]
- 00bd26e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd26e8 bytes 60e602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2468d471743d7b9ca452b12c97d01690"></a>

### [`00bd26fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd26fc.md) → [`00bd2b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2b24.md) _ZN8firebase4auth23firebase_auth_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00bd2b50",
      "incomplete_value": true,
      "site": "00bd2b50",
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
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2728",
      "incomplete_value": true,
      "site": "00bd2728",
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
            "const:5c8:8"
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
      "definition_site": "00bd2b38",
      "incomplete_value": true,
      "site": "00bd2b38",
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
      "definition_site": "00bd2710",
      "incomplete_value": true,
      "site": "00bd2710",
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
      "definition_site": "00bd2b40",
      "incomplete_value": false,
      "site": "00bd2b48",
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
            "const:8cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2718",
      "incomplete_value": false,
      "site": "00bd2720",
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
            "const:88d:8"
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
      "00bd2b34",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2b40",
      "PARAM",
      [
        "storage",
        "002be88d",
        null,
        "string"
      ]
    ],
    [
      "00bd2b50",
      "WRITE",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2b34",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2b40",
      "PARAM",
      [
        "storage",
        "002be8cd",
        null,
        "string"
      ]
    ],
    [
      "00bd2b50",
      "WRITE",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd26fc.md#insn-00bd2720) · [`00bd2728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd26fc.md#insn-00bd2728) · [`00bd270c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd26fc.md#insn-00bd270c)
- 新版 `00bd2b48`（命令位置の公開資料なし） · `00bd2b50`（命令位置の公開資料なし） · `00bd2b34`（命令位置の公開資料なし）

~~~diff
- 00bd2720 ["INT_ADD", "register:40f0:8", ["const:bd2720:8", "const:4:8"]]
- 00bd2720 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2b48 ["INT_ADD", "register:40f0:8", ["const:bd2b48:8", "const:4:8"]]
+ 00bd2b48 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2720 bytes fc200294
+ 00bd2b48 bytes f2200294
- 00bd2728 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c8:8"]]
- 00bd2728 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2b50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00bd2b50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2728 bytes 60e602f9
+ 00bd2b50 bytes 60e604f9
- 00bd270c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c8:8"]]
- 00bd270c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd2b34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00bd2b34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd270c bytes 68e642f9
+ 00bd2b34 bytes 68e644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f25a3757c922216a92f4a794968add61"></a>

### [`00bd273c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd273c.md) → [`00bd2b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2b64.md) _ZN8firebase4auth23firebase_auth_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd2b94",
      "incomplete_value": true,
      "site": "00bd2b94",
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
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd276c",
      "incomplete_value": true,
      "site": "00bd276c",
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
            "const:5c8:8"
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
      "definition_site": "00bd2b78",
      "incomplete_value": true,
      "site": "00bd2b78",
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
      "definition_site": "00bd2750",
      "incomplete_value": true,
      "site": "00bd2750",
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
      "definition_site": "00bd2b84",
      "incomplete_value": false,
      "site": "00bd2b8c",
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
            "const:8cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd275c",
      "incomplete_value": false,
      "site": "00bd2764",
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
            "const:88d:8"
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
      "00bd2b74",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2b84",
      "PARAM",
      [
        "storage",
        "002be88d",
        null,
        "string"
      ]
    ],
    [
      "00bd2b94",
      "WRITE",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2b74",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2b84",
      "PARAM",
      [
        "storage",
        "002be8cd",
        null,
        "string"
      ]
    ],
    [
      "00bd2b94",
      "WRITE",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd273c.md#insn-00bd2764) · [`00bd276c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd273c.md#insn-00bd276c) · [`00bd274c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd273c.md#insn-00bd274c)
- 新版 `00bd2b8c`（命令位置の公開資料なし） · `00bd2b94`（命令位置の公開資料なし） · `00bd2b74`（命令位置の公開資料なし）

~~~diff
- 00bd2764 ["INT_ADD", "register:40f0:8", ["const:bd2764:8", "const:4:8"]]
- 00bd2764 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2b8c ["INT_ADD", "register:40f0:8", ["const:bd2b8c:8", "const:4:8"]]
+ 00bd2b8c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2764 bytes eb200294
+ 00bd2b8c bytes e1200294
- 00bd276c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c8:8"]]
- 00bd276c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2b94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00bd2b94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd276c bytes 60e602f9
+ 00bd2b94 bytes 60e604f9
- 00bd274c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c8:8"]]
- 00bd274c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd2b74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00bd2b74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd274c bytes 68e642f9
+ 00bd2b74 bytes 68e644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-189da351dfb94f0e4899d6a89df253e7"></a>

### [`00bd2780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2780.md) → [`00bd2ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2ba8.md) _ZN8firebase4auth23firebase_auth_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

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
      "site": "00bd27b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2bd8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd2bbc",
      "incomplete_value": true,
      "site": "00bd2bbc",
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
      "definition_site": "00bd2794",
      "incomplete_value": true,
      "site": "00bd2794",
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
      "00bd2bb8",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd279c",
      "PARAM",
      [
        "storage",
        "002be88d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd27b0",
      "WRITE",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2bb8",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2bc4",
      "PARAM",
      [
        "storage",
        "002be8cd",
        null,
        "string"
      ]
    ],
    [
      "00bd2bd8",
      "WRITE",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2780.md#insn-00bd2794) · [`00bd27a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2780.md#insn-00bd27a8) · [`00bd27b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2780.md#insn-00bd27b0)
- 新版 `00bd2bbc`（命令位置の公開資料なし） · `00bd2bd0`（命令位置の公開資料なし）

~~~diff
- 00bd2794 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd2794 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd2bbc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd2bbc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd2794 bytes 080100b5
+ 00bd2bbc bytes 080100b5
- 00bd27a8 ["INT_ADD", "register:40f0:8", ["const:bd27a8:8", "const:4:8"]]
- 00bd27a8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2bd0 ["INT_ADD", "register:40f0:8", ["const:bd2bd0:8", "const:4:8"]]
+ 00bd2bd0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd27a8 bytes da200294
+ 00bd2bd0 bytes d0200294
- 00bd27b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c8:8"]]
- 00bd27b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd27b0 bytes 60e602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8499e387988dd7bc1ce61ec3ee32cb9"></a>

### [`00bd27d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd27d0.md) → [`00bd2bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2bf8.md) _ZN8firebase4auth23firebase_auth_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd2c50",
      "incomplete_value": true,
      "site": "00bd2c50",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2828",
      "incomplete_value": true,
      "site": "00bd2828",
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
            "const:5d0:8"
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
      "definition_site": "00bd2c2c",
      "incomplete_value": true,
      "site": "00bd2c38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2804",
      "incomplete_value": true,
      "site": "00bd2810",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c8:8"
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
      "00bd2c0c",
      "READ",
      [
        "storage",
        "011265d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2c2c",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2c50",
      "WRITE",
      [
        "storage",
        "011265d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd2c0c",
      "READ",
      [
        "storage",
        "011269d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2c2c",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2c50",
      "WRITE",
      [
        "storage",
        "011269d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd27d0.md#insn-00bd2810) · [`00bd2828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd27d0.md#insn-00bd2828) · [`00bd27e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd27d0.md#insn-00bd27e4)
- 新版 `00bd2c38`（命令位置の公開資料なし） · `00bd2c50`（命令位置の公開資料なし） · `00bd2c0c`（命令位置の公開資料なし）

~~~diff
- 00bd2810 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2810 ["INT_ADD", "register:40f0:8", ["const:bd2810:8", "const:4:8"]]
- 00bd2810 ["CALLIND", null, ["register:0:8"]]
+ 00bd2c38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2c38 ["INT_ADD", "register:40f0:8", ["const:bd2c38:8", "const:4:8"]]
+ 00bd2c38 ["CALLIND", null, ["register:0:8"]]
- 00bd2810 bytes 00013fd6
+ 00bd2c38 bytes 00013fd6
- 00bd2828 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd2828 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5d0:8"]]
- 00bd2828 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd2c50 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd2c50 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9d0:8"]]
+ 00bd2c50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd2828 bytes a0421739
+ 00bd2c50 bytes a0422739
- 00bd27e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5d0:8"]]
- 00bd27e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd27e4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd2c0c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9d0:8"]]
+ 00bd2c0c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd2c0c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd27e4 bytes a8425739
+ 00bd2c0c bytes a8426739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16daf6ee81584f9ef0eaa5f96f7398f2"></a>

### [`00bd283c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd283c.md) → [`00bd2c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2c64.md) _ZN8firebase4auth23firebase_auth_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd2ca0",
      "incomplete_value": true,
      "site": "00bd2ca0",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2878",
      "incomplete_value": true,
      "site": "00bd2878",
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
            "const:5d0:8"
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
      "definition_site": "00bd2cc0",
      "incomplete_value": true,
      "site": "00bd2cc0",
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
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2898",
      "incomplete_value": true,
      "site": "00bd2898",
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
            "const:5c8:8"
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
      "definition_site": "00bd2c7c",
      "incomplete_value": true,
      "site": "00bd2c7c",
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
      "definition_site": "00bd2854",
      "incomplete_value": true,
      "site": "00bd2854",
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
      "00bd2c78",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2c84",
      "READ",
      [
        "storage",
        "011265d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2ca0",
      "WRITE",
      [
        "storage",
        "011265d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd2c78",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2c84",
      "READ",
      [
        "storage",
        "011269d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2ca0",
      "WRITE",
      [
        "storage",
        "011269d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd283c.md#insn-00bd2878) · [`00bd2894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd283c.md#insn-00bd2894) · [`00bd2898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd283c.md#insn-00bd2898)
- 新版 `00bd2ca0`（命令位置の公開資料なし） · `00bd2cbc`（命令位置の公開資料なし） · `00bd2cc0`（命令位置の公開資料なし）

~~~diff
- 00bd2878 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd2878 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd2878 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5d0:8"]]
- 00bd2878 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd2ca0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd2ca0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd2ca0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9d0:8"]]
+ 00bd2ca0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd2878 bytes bf421739
+ 00bd2ca0 bytes bf422739
- 00bd2894 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2894 ["INT_ADD", "register:40f0:8", ["const:bd2894:8", "const:4:8"]]
- 00bd2894 ["CALLIND", null, ["register:0:8"]]
+ 00bd2cbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2cbc ["INT_ADD", "register:40f0:8", ["const:bd2cbc:8", "const:4:8"]]
+ 00bd2cbc ["CALLIND", null, ["register:0:8"]]
- 00bd2894 bytes 00013fd6
+ 00bd2cbc bytes 00013fd6
- 00bd2898 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c8:8"]]
- 00bd2898 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bd2898 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd2cc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9c8:8"]]
+ 00bd2cc0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd2cc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bd2898 bytes 9fe602f9
+ 00bd2cc0 bytes 9fe604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e3fb73298ea6e6f04d1a3873869d4f1"></a>

### [`00bd28ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd28ac.md) → [`00bd2cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2cd4.md) _ZN8firebase4auth23firebase_auth_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bd28ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2d14"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd28c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd28c0",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd28c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2d18"
      ]
    ],
    [
      "unmatched:00bd28d0",
      "PARAM",
      [
        "storage",
        "002be88d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd2ce8",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2cf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2d18"
      ]
    ],
    [
      "00bd2cf8",
      "PARAM",
      [
        "storage",
        "002be8cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd28c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd28ac.md#insn-00bd28c8) · [`00bd28e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd28ac.md#insn-00bd28e4) · [`00bd28ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd28ac.md#insn-00bd28ec)
- 新版 `00bd2d0c`（命令位置の公開資料なし）

~~~diff
- 00bd28c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd28c8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd28c8 bytes 410100b5
- 00bd28e4 ["INT_ADD", "register:40f0:8", ["const:bd28e4:8", "const:4:8"]]
- 00bd28e4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2d0c ["INT_ADD", "register:40f0:8", ["const:bd2d0c:8", "const:4:8"]]
+ 00bd2d0c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd28e4 bytes 8b200294
+ 00bd2d0c bytes 81200294
- 00bd28ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c8:8"]]
- 00bd28ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd28ec bytes 80e602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-328599d617150d949d3fbf3060f858bd"></a>

### [`00bd2958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2958.md) → [`00bd2d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2d80.md) _ZN8firebase4auth23firebase_auth_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bd2958"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2958"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd295c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd2958",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd295c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd296c",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2d80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd2d84",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd2d94",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2958.md#insn-00bd2958) · [`00bd295c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2958.md#insn-00bd295c) · [`00bd2974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2958.md#insn-00bd2974)

~~~diff
- 00bd2958 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd2958 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd2958 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd2958 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd2958 bytes f44fbea9
- 00bd295c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd295c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd295c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd295c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd295c bytes fd7b01a9
- 00bd2974 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd2974 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd2974 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d77a39b8cfd8535780de3e4ce7be407a"></a>

### [`00bd2a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a04.md) → [`00bd2e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2e2c.md) _ZN8firebase4auth26firebase_network_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "definition_site": "00bd2e58",
      "incomplete_value": true,
      "site": "00bd2e58",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2a30",
      "incomplete_value": true,
      "site": "00bd2a30",
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
            "const:5e8:8"
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
      "definition_site": "00bd2e40",
      "incomplete_value": true,
      "site": "00bd2e40",
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
      "definition_site": "00bd2a18",
      "incomplete_value": true,
      "site": "00bd2a18",
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
      "definition_site": "00bd2e4c",
      "incomplete_value": false,
      "site": "00bd2e50",
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
            "const:a57:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2a24",
      "incomplete_value": false,
      "site": "00bd2a28",
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
            "const:a17:8"
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
      "00bd2e3c",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2e4c",
      "PARAM",
      [
        "storage",
        "002bfa17",
        null,
        "string"
      ]
    ],
    [
      "00bd2e58",
      "WRITE",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2e3c",
      "READ",
      [
        "storage",
        "011269e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2e4c",
      "PARAM",
      [
        "storage",
        "002bfa57",
        null,
        "string"
      ]
    ],
    [
      "00bd2e58",
      "WRITE",
      [
        "storage",
        "011269e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a04.md#insn-00bd2a28) · [`00bd2a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a04.md#insn-00bd2a30) · [`00bd2a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a04.md#insn-00bd2a14)
- 新版 `00bd2e50`（命令位置の公開資料なし） · `00bd2e58`（命令位置の公開資料なし） · `00bd2e3c`（命令位置の公開資料なし）

~~~diff
- 00bd2a28 ["INT_ADD", "register:40f0:8", ["const:bd2a28:8", "const:4:8"]]
- 00bd2a28 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2e50 ["INT_ADD", "register:40f0:8", ["const:bd2e50:8", "const:4:8"]]
+ 00bd2e50 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2a28 bytes 3a200294
+ 00bd2e50 bytes 30200294
- 00bd2a30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00bd2a30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2e58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00bd2e58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2a30 bytes 60f602f9
+ 00bd2e58 bytes 60f604f9
- 00bd2a14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00bd2a14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd2e3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00bd2e3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2a14 bytes 68f642f9
+ 00bd2e3c bytes 68f644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5434d1eae260be721af0e4a0153cdac0"></a>

### [`00bd2a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a44.md) → [`00bd2e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2e6c.md) _ZN8firebase4auth26firebase_network_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "definition_site": "00bd2e98",
      "incomplete_value": true,
      "site": "00bd2e98",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2a70",
      "incomplete_value": true,
      "site": "00bd2a70",
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
            "const:5e8:8"
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
      "definition_site": "00bd2e80",
      "incomplete_value": true,
      "site": "00bd2e80",
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
      "definition_site": "00bd2a58",
      "incomplete_value": true,
      "site": "00bd2a58",
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
      "definition_site": "00bd2e88",
      "incomplete_value": false,
      "site": "00bd2e90",
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
            "const:a57:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2a60",
      "incomplete_value": false,
      "site": "00bd2a68",
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
            "const:a17:8"
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
      "00bd2e7c",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2e88",
      "PARAM",
      [
        "storage",
        "002bfa17",
        null,
        "string"
      ]
    ],
    [
      "00bd2e98",
      "WRITE",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2e7c",
      "READ",
      [
        "storage",
        "011269e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2e88",
      "PARAM",
      [
        "storage",
        "002bfa57",
        null,
        "string"
      ]
    ],
    [
      "00bd2e98",
      "WRITE",
      [
        "storage",
        "011269e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a44.md#insn-00bd2a68) · [`00bd2a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a44.md#insn-00bd2a70) · [`00bd2a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a44.md#insn-00bd2a54)
- 新版 `00bd2e90`（命令位置の公開資料なし） · `00bd2e98`（命令位置の公開資料なし） · `00bd2e7c`（命令位置の公開資料なし）

~~~diff
- 00bd2a68 ["INT_ADD", "register:40f0:8", ["const:bd2a68:8", "const:4:8"]]
- 00bd2a68 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2e90 ["INT_ADD", "register:40f0:8", ["const:bd2e90:8", "const:4:8"]]
+ 00bd2e90 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2a68 bytes 2a200294
+ 00bd2e90 bytes 20200294
- 00bd2a70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00bd2a70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2e98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00bd2e98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2a70 bytes 60f602f9
+ 00bd2e98 bytes 60f604f9
- 00bd2a54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00bd2a54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd2e7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00bd2e7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2a54 bytes 68f642f9
+ 00bd2e7c bytes 68f644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30ae11e1dc886b8ca45eafd0bb93a15a"></a>

### [`00bd2a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a84.md) → [`00bd2eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2eac.md) _ZN8firebase4auth26firebase_network_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd2edc",
      "incomplete_value": true,
      "site": "00bd2edc",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2ab4",
      "incomplete_value": true,
      "site": "00bd2ab4",
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
            "const:5e8:8"
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
      "definition_site": "00bd2ec0",
      "incomplete_value": true,
      "site": "00bd2ec0",
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
      "definition_site": "00bd2a98",
      "incomplete_value": true,
      "site": "00bd2a98",
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
      "definition_site": "00bd2ecc",
      "incomplete_value": false,
      "site": "00bd2ed4",
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
            "const:a57:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2aa4",
      "incomplete_value": false,
      "site": "00bd2aac",
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
            "const:a17:8"
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
      "00bd2ebc",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2ecc",
      "PARAM",
      [
        "storage",
        "002bfa17",
        null,
        "string"
      ]
    ],
    [
      "00bd2edc",
      "WRITE",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2ebc",
      "READ",
      [
        "storage",
        "011269e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2ecc",
      "PARAM",
      [
        "storage",
        "002bfa57",
        null,
        "string"
      ]
    ],
    [
      "00bd2edc",
      "WRITE",
      [
        "storage",
        "011269e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a84.md#insn-00bd2aac) · [`00bd2ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a84.md#insn-00bd2ab4) · [`00bd2a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a84.md#insn-00bd2a94)
- 新版 `00bd2ed4`（命令位置の公開資料なし） · `00bd2edc`（命令位置の公開資料なし） · `00bd2ebc`（命令位置の公開資料なし）

~~~diff
- 00bd2aac ["INT_ADD", "register:40f0:8", ["const:bd2aac:8", "const:4:8"]]
- 00bd2aac ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2ed4 ["INT_ADD", "register:40f0:8", ["const:bd2ed4:8", "const:4:8"]]
+ 00bd2ed4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2aac bytes 19200294
+ 00bd2ed4 bytes 0f200294
- 00bd2ab4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00bd2ab4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2edc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00bd2edc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2ab4 bytes 60f602f9
+ 00bd2edc bytes 60f604f9
- 00bd2a94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00bd2a94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd2ebc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00bd2ebc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2a94 bytes 68f642f9
+ 00bd2ebc bytes 68f644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e598bf412ee7799f10049d879278277"></a>

### [`00bd2ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ac8.md) → [`00bd2ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2ef0.md) _ZN8firebase4auth26firebase_network_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd2f20",
      "incomplete_value": true,
      "site": "00bd2f20",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2af8",
      "incomplete_value": true,
      "site": "00bd2af8",
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
            "const:5e8:8"
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
      "definition_site": "00bd2f04",
      "incomplete_value": true,
      "site": "00bd2f04",
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
      "definition_site": "00bd2adc",
      "incomplete_value": true,
      "site": "00bd2adc",
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
      "definition_site": "00bd2f0c",
      "incomplete_value": false,
      "site": "00bd2f18",
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
            "const:a57:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2ae4",
      "incomplete_value": false,
      "site": "00bd2af0",
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
            "const:a17:8"
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
      "00bd2f00",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2f0c",
      "PARAM",
      [
        "storage",
        "002bfa17",
        null,
        "string"
      ]
    ],
    [
      "00bd2f20",
      "WRITE",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2f00",
      "READ",
      [
        "storage",
        "011269e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2f0c",
      "PARAM",
      [
        "storage",
        "002bfa57",
        null,
        "string"
      ]
    ],
    [
      "00bd2f20",
      "WRITE",
      [
        "storage",
        "011269e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ac8.md#insn-00bd2af0) · [`00bd2af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ac8.md#insn-00bd2af8) · [`00bd2ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ac8.md#insn-00bd2ad8)
- 新版 `00bd2f18`（命令位置の公開資料なし） · `00bd2f20`（命令位置の公開資料なし） · `00bd2f00`（命令位置の公開資料なし）

~~~diff
- 00bd2af0 ["INT_ADD", "register:40f0:8", ["const:bd2af0:8", "const:4:8"]]
- 00bd2af0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd2f18 ["INT_ADD", "register:40f0:8", ["const:bd2f18:8", "const:4:8"]]
+ 00bd2f18 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2af0 bytes 08200294
+ 00bd2f18 bytes fe1f0294
- 00bd2af8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00bd2af8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2f20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00bd2f20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2af8 bytes 60f602f9
+ 00bd2f20 bytes 60f604f9
- 00bd2ad8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00bd2ad8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd2f00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9e8:8"]]
+ 00bd2f00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2ad8 bytes 68f642f9
+ 00bd2f00 bytes 68f644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35c7c0478fa9532295066d24804922b1"></a>

### [`00bd2b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2b18.md) → [`00bd2f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2f40.md) _ZN8firebase4auth26firebase_network_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd2f98",
      "incomplete_value": true,
      "site": "00bd2f98",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2b70",
      "incomplete_value": true,
      "site": "00bd2b70",
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
            "const:5f0:8"
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
      "definition_site": "00bd2f74",
      "incomplete_value": true,
      "site": "00bd2f80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2b4c",
      "incomplete_value": true,
      "site": "00bd2b58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5e8:8"
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
      "00bd2f54",
      "READ",
      [
        "storage",
        "011265f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2f74",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2f98",
      "WRITE",
      [
        "storage",
        "011265f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd2f54",
      "READ",
      [
        "storage",
        "011269f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2f74",
      "READ",
      [
        "storage",
        "011269e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2f98",
      "WRITE",
      [
        "storage",
        "011269f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2b18.md#insn-00bd2b58) · [`00bd2b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2b18.md#insn-00bd2b70) · [`00bd2b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2b18.md#insn-00bd2b2c)
- 新版 `00bd2f80`（命令位置の公開資料なし） · `00bd2f98`（命令位置の公開資料なし） · `00bd2f54`（命令位置の公開資料なし）

~~~diff
- 00bd2b58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2b58 ["INT_ADD", "register:40f0:8", ["const:bd2b58:8", "const:4:8"]]
- 00bd2b58 ["CALLIND", null, ["register:0:8"]]
+ 00bd2f80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2f80 ["INT_ADD", "register:40f0:8", ["const:bd2f80:8", "const:4:8"]]
+ 00bd2f80 ["CALLIND", null, ["register:0:8"]]
- 00bd2b58 bytes 00013fd6
+ 00bd2f80 bytes 00013fd6
- 00bd2b70 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd2b70 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5f0:8"]]
- 00bd2b70 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd2f98 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd2f98 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9f0:8"]]
+ 00bd2f98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd2b70 bytes a0c21739
+ 00bd2f98 bytes a0c22739
- 00bd2b2c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5f0:8"]]
- 00bd2b2c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd2b2c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd2f54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9f0:8"]]
+ 00bd2f54 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd2f54 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd2b2c bytes a8c25739
+ 00bd2f54 bytes a8c26739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea781ac4af985b6baf4be334f126f2fe"></a>

### [`00bd2b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2b84.md) → [`00bd2fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2fac.md) _ZN8firebase4auth26firebase_network_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2b84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2b88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2b88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd2b84",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd2b88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd2b8c",
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
      "00bd2fac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd2fb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd2fb4",
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

- 旧版 [`00bd2b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2b84.md#insn-00bd2b84) · [`00bd2b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2b84.md#insn-00bd2b88) · [`00bd2b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2b84.md#insn-00bd2b8c)

~~~diff
- 00bd2b84 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd2b84 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd2b84 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd2b84 bytes f50f1df8
- 00bd2b88 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd2b88 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd2b88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd2b88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd2b88 bytes f44f01a9
- 00bd2b8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd2b8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd2b8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd2b8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd2b8c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4cdb072bb016bfca47f6e669a146c16"></a>

### [`00bd2bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2bf4.md) → [`00bd301c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd301c.md) _ZN8firebase4auth26firebase_network_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd2c34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd305c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2c10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd2c08",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd2c10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd3060"
      ]
    ],
    [
      "unmatched:00bd2c18",
      "PARAM",
      [
        "storage",
        "002bfa17",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd3030",
      "READ",
      [
        "storage",
        "011269e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3038",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd3060"
      ]
    ],
    [
      "00bd3040",
      "PARAM",
      [
        "storage",
        "002bfa57",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2bf4.md#insn-00bd2c10) · [`00bd2c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2bf4.md#insn-00bd2c2c) · [`00bd2c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2bf4.md#insn-00bd2c34)
- 新版 `00bd3054`（命令位置の公開資料なし）

~~~diff
- 00bd2c10 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd2c10 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd2c10 bytes 410100b5
- 00bd2c2c ["INT_ADD", "register:40f0:8", ["const:bd2c2c:8", "const:4:8"]]
- 00bd2c2c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd3054 ["INT_ADD", "register:40f0:8", ["const:bd3054:8", "const:4:8"]]
+ 00bd3054 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2c2c bytes b91f0294
+ 00bd3054 bytes af1f0294
- 00bd2c34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
- 00bd2c34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2c34 bytes 80f602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8694dff4185c7507448f0aa062f03268"></a>

### [`00bd2c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2c64.md) → [`00bd308c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd308c.md) _ZN8firebase4auth26firebase_network_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd30a8",
      "incomplete_value": false,
      "site": "00bd30ac",
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
      "definition_site": "00bd2c80",
      "incomplete_value": false,
      "site": "00bd2c84",
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
      "definition_site": "00bd30b8",
      "incomplete_value": true,
      "site": "00bd30c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd2c90",
      "incomplete_value": true,
      "site": "00bd2c9c",
      "value": [
        "LOAD",
        "8",
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
      "00bd30a8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd30b8",
      "DATA",
      [
        "storage",
        "011265f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd30a8",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd30b8",
      "DATA",
      [
        "storage",
        "011269f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2c64.md#insn-00bd2c84) · [`00bd2c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2c64.md#insn-00bd2c80) · [`00bd2c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2c64.md#insn-00bd2c8c)
- 新版 `00bd30ac`（命令位置の公開資料なし） · `00bd30a8`（命令位置の公開資料なし） · `00bd30b4`（命令位置の公開資料なし）

~~~diff
- 00bd2c84 ["INT_ADD", "register:40f0:8", ["const:bd2c84:8", "const:4:8"]]
- 00bd2c84 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd30ac ["INT_ADD", "register:40f0:8", ["const:bd30ac:8", "const:4:8"]]
+ 00bd30ac ["CALL", null, ["callee:00c5b000:8"]]
- 00bd2c84 bytes df1f0294
+ 00bd30ac bytes d51f0294
- 00bd2c80 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd2c80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd2c80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd2c80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd30a8 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd30a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd30a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd30a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd2c80 bytes 00680a91
+ 00bd30a8 bytes 009c0d91
- 00bd2c8c ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00bd2c8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2c8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2c8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd30b4 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00bd30b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd30b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd30b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd2c8c bytes 08e11791
+ 00bd30b4 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4872fd72167ae9c5864d70ed0f2c45df"></a>

### [`00bd2ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ca0.md) → [`00bd30c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd30c8.md) _ZN8firebase4auth26firebase_network_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd3108",
      "incomplete_value": true,
      "site": "00bd3108",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2ce0",
      "incomplete_value": true,
      "site": "00bd2ce0",
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
            "const:5e8:8"
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
      "definition_site": "00bd30e4",
      "incomplete_value": true,
      "site": "00bd30e4",
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
      "definition_site": "00bd2cbc",
      "incomplete_value": true,
      "site": "00bd2cbc",
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
      "definition_site": "00bd30ec",
      "incomplete_value": false,
      "site": "00bd3100",
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
            "const:a57:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2cc4",
      "incomplete_value": false,
      "site": "00bd2cd8",
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
            "const:a17:8"
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
      "00bd30dc",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd30ec",
      "PARAM",
      [
        "storage",
        "002bfa17",
        null,
        "string"
      ]
    ],
    [
      "00bd3108",
      "WRITE",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd30dc",
      "READ",
      [
        "storage",
        "011269e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd30ec",
      "PARAM",
      [
        "storage",
        "002bfa57",
        null,
        "string"
      ]
    ],
    [
      "00bd3108",
      "WRITE",
      [
        "storage",
        "011269e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ca0.md#insn-00bd2cd8) · [`00bd2ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ca0.md#insn-00bd2ce0) · [`00bd2cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ca0.md#insn-00bd2cb4)
- 新版 `00bd3100`（命令位置の公開資料なし） · `00bd3108`（命令位置の公開資料なし） · `00bd30dc`（命令位置の公開資料なし）

~~~diff
- 00bd2cd8 ["INT_ADD", "register:40f0:8", ["const:bd2cd8:8", "const:4:8"]]
- 00bd2cd8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd3100 ["INT_ADD", "register:40f0:8", ["const:bd3100:8", "const:4:8"]]
+ 00bd3100 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2cd8 bytes 8e1f0294
+ 00bd3100 bytes 841f0294
- 00bd2ce0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
- 00bd2ce0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd3108 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9e8:8"]]
+ 00bd3108 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2ce0 bytes 80f602f9
+ 00bd3108 bytes 80f604f9
- 00bd2cb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
- 00bd2cb4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd30dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9e8:8"]]
+ 00bd30dc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2cb4 bytes 81f642f9
+ 00bd30dc bytes 81f644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2697eec46d220c96898366a6853a8b13"></a>

### [`00bd2d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d10.md) → [`00bd3138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd3138.md) _ZN8firebase4auth26firebase_network_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd3154",
      "incomplete_value": false,
      "site": "00bd3158",
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
      "definition_site": "00bd2d2c",
      "incomplete_value": false,
      "site": "00bd2d30",
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
      "definition_site": "00bd3164",
      "incomplete_value": true,
      "site": "00bd3170",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd2d3c",
      "incomplete_value": true,
      "site": "00bd2d48",
      "value": [
        "LOAD",
        "8",
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
      "00bd3154",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd3164",
      "DATA",
      [
        "storage",
        "01126600",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd3154",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd3164",
      "DATA",
      [
        "storage",
        "01126a00",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d10.md#insn-00bd2d30) · [`00bd2d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d10.md#insn-00bd2d2c) · [`00bd2d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d10.md#insn-00bd2d38)
- 新版 `00bd3158`（命令位置の公開資料なし） · `00bd3154`（命令位置の公開資料なし） · `00bd3160`（命令位置の公開資料なし）

~~~diff
- 00bd2d30 ["INT_ADD", "register:40f0:8", ["const:bd2d30:8", "const:4:8"]]
- 00bd2d30 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd3158 ["INT_ADD", "register:40f0:8", ["const:bd3158:8", "const:4:8"]]
+ 00bd3158 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd2d30 bytes b41f0294
+ 00bd3158 bytes aa1f0294
- 00bd2d2c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd2d2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd2d2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd2d2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd3154 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd3154 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd3154 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd3154 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd2d2c bytes 00441191
+ 00bd3154 bytes 00781491
- 00bd2d38 ["COPY", "tmp:0:8", ["const:600:8"]]
- 00bd2d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd3160 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00bd3160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd2d38 bytes 08011891
+ 00bd3160 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3b4251f026b0db466190d72e7f46e23"></a>

### [`00bd2d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d4c.md) → [`00bd3174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd3174.md) _ZN8firebase4auth27too_many_requests_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

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
      "definition_site": "00bd31a0",
      "incomplete_value": true,
      "site": "00bd31a0",
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
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2d78",
      "incomplete_value": true,
      "site": "00bd2d78",
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
            "const:608:8"
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
      "definition_site": "00bd3188",
      "incomplete_value": true,
      "site": "00bd3188",
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
      "definition_site": "00bd2d60",
      "incomplete_value": true,
      "site": "00bd2d60",
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
      "definition_site": "00bd3194",
      "incomplete_value": false,
      "site": "00bd3198",
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
            "const:c19:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2d6c",
      "incomplete_value": false,
      "site": "00bd2d70",
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
            "const:bd9:8"
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
      "00bd3184",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3194",
      "PARAM",
      [
        "storage",
        "002b5bd9",
        null,
        "string"
      ]
    ],
    [
      "00bd31a0",
      "WRITE",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd3184",
      "READ",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3194",
      "PARAM",
      [
        "storage",
        "002b5c19",
        null,
        "string"
      ]
    ],
    [
      "00bd31a0",
      "WRITE",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d4c.md#insn-00bd2d70) · [`00bd2d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d4c.md#insn-00bd2d78) · [`00bd2d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d4c.md#insn-00bd2d5c)
- 新版 `00bd3198`（命令位置の公開資料なし） · `00bd31a0`（命令位置の公開資料なし） · `00bd3184`（命令位置の公開資料なし）

~~~diff
- 00bd2d70 ["INT_ADD", "register:40f0:8", ["const:bd2d70:8", "const:4:8"]]
- 00bd2d70 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd3198 ["INT_ADD", "register:40f0:8", ["const:bd3198:8", "const:4:8"]]
+ 00bd3198 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2d70 bytes 681f0294
+ 00bd3198 bytes 5e1f0294
- 00bd2d78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00bd2d78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd31a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00bd31a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2d78 bytes 600603f9
+ 00bd31a0 bytes 600605f9
- 00bd2d5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00bd2d5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd3184 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00bd3184 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2d5c bytes 680643f9
+ 00bd3184 bytes 680645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6876552dbbea5fde743bbb23625c9c46"></a>

### [`00bd2d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d8c.md) → [`00bd31b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd31b4.md) _ZN8firebase4auth27too_many_requests_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

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
      "definition_site": "00bd31e0",
      "incomplete_value": true,
      "site": "00bd31e0",
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
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2db8",
      "incomplete_value": true,
      "site": "00bd2db8",
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
            "const:608:8"
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
      "definition_site": "00bd31c8",
      "incomplete_value": true,
      "site": "00bd31c8",
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
      "definition_site": "00bd2da0",
      "incomplete_value": true,
      "site": "00bd2da0",
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
      "definition_site": "00bd31d0",
      "incomplete_value": false,
      "site": "00bd31d8",
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
            "const:c19:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2da8",
      "incomplete_value": false,
      "site": "00bd2db0",
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
            "const:bd9:8"
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
      "00bd31c4",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd31d0",
      "PARAM",
      [
        "storage",
        "002b5bd9",
        null,
        "string"
      ]
    ],
    [
      "00bd31e0",
      "WRITE",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd31c4",
      "READ",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd31d0",
      "PARAM",
      [
        "storage",
        "002b5c19",
        null,
        "string"
      ]
    ],
    [
      "00bd31e0",
      "WRITE",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d8c.md#insn-00bd2db0) · [`00bd2db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d8c.md#insn-00bd2db8) · [`00bd2d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d8c.md#insn-00bd2d9c)
- 新版 `00bd31d8`（命令位置の公開資料なし） · `00bd31e0`（命令位置の公開資料なし） · `00bd31c4`（命令位置の公開資料なし）

~~~diff
- 00bd2db0 ["INT_ADD", "register:40f0:8", ["const:bd2db0:8", "const:4:8"]]
- 00bd2db0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd31d8 ["INT_ADD", "register:40f0:8", ["const:bd31d8:8", "const:4:8"]]
+ 00bd31d8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2db0 bytes 581f0294
+ 00bd31d8 bytes 4e1f0294
- 00bd2db8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00bd2db8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd31e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00bd31e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2db8 bytes 600603f9
+ 00bd31e0 bytes 600605f9
- 00bd2d9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00bd2d9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd31c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00bd31c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2d9c bytes 680643f9
+ 00bd31c4 bytes 680645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d8c8693944206a57cfb355f4173bf59"></a>

### [`00bd2dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2dcc.md) → [`00bd31f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd31f4.md) _ZN8firebase4auth27too_many_requests_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd3224",
      "incomplete_value": true,
      "site": "00bd3224",
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
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2dfc",
      "incomplete_value": true,
      "site": "00bd2dfc",
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
            "const:608:8"
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
      "definition_site": "00bd3208",
      "incomplete_value": true,
      "site": "00bd3208",
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
      "definition_site": "00bd2de0",
      "incomplete_value": true,
      "site": "00bd2de0",
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
      "definition_site": "00bd3214",
      "incomplete_value": false,
      "site": "00bd321c",
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
            "const:c19:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2dec",
      "incomplete_value": false,
      "site": "00bd2df4",
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
            "const:bd9:8"
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
      "00bd3204",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3214",
      "PARAM",
      [
        "storage",
        "002b5bd9",
        null,
        "string"
      ]
    ],
    [
      "00bd3224",
      "WRITE",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd3204",
      "READ",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3214",
      "PARAM",
      [
        "storage",
        "002b5c19",
        null,
        "string"
      ]
    ],
    [
      "00bd3224",
      "WRITE",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2dcc.md#insn-00bd2df4) · [`00bd2dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2dcc.md#insn-00bd2dfc) · [`00bd2ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2dcc.md#insn-00bd2ddc)
- 新版 `00bd321c`（命令位置の公開資料なし） · `00bd3224`（命令位置の公開資料なし） · `00bd3204`（命令位置の公開資料なし）

~~~diff
- 00bd2df4 ["INT_ADD", "register:40f0:8", ["const:bd2df4:8", "const:4:8"]]
- 00bd2df4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd321c ["INT_ADD", "register:40f0:8", ["const:bd321c:8", "const:4:8"]]
+ 00bd321c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2df4 bytes 471f0294
+ 00bd321c bytes 3d1f0294
- 00bd2dfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00bd2dfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd3224 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00bd3224 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2dfc bytes 600603f9
+ 00bd3224 bytes 600605f9
- 00bd2ddc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00bd2ddc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd3204 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00bd3204 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2ddc bytes 680643f9
+ 00bd3204 bytes 680645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6dd25f151ca32591a7101ed2f45a2c3"></a>

### [`00bd2e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2e10.md) → [`00bd3238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd3238.md) _ZN8firebase4auth27too_many_requests_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd3268",
      "incomplete_value": true,
      "site": "00bd3268",
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
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2e40",
      "incomplete_value": true,
      "site": "00bd2e40",
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
            "const:608:8"
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
      "definition_site": "00bd324c",
      "incomplete_value": true,
      "site": "00bd324c",
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
      "definition_site": "00bd2e24",
      "incomplete_value": true,
      "site": "00bd2e24",
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
      "definition_site": "00bd3254",
      "incomplete_value": false,
      "site": "00bd3260",
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
            "const:c19:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2e2c",
      "incomplete_value": false,
      "site": "00bd2e38",
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
            "const:bd9:8"
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
      "00bd3248",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3254",
      "PARAM",
      [
        "storage",
        "002b5bd9",
        null,
        "string"
      ]
    ],
    [
      "00bd3268",
      "WRITE",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd3248",
      "READ",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3254",
      "PARAM",
      [
        "storage",
        "002b5c19",
        null,
        "string"
      ]
    ],
    [
      "00bd3268",
      "WRITE",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2e10.md#insn-00bd2e38) · [`00bd2e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2e10.md#insn-00bd2e40) · [`00bd2e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2e10.md#insn-00bd2e20)
- 新版 `00bd3260`（命令位置の公開資料なし） · `00bd3268`（命令位置の公開資料なし） · `00bd3248`（命令位置の公開資料なし）

~~~diff
- 00bd2e38 ["INT_ADD", "register:40f0:8", ["const:bd2e38:8", "const:4:8"]]
- 00bd2e38 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd3260 ["INT_ADD", "register:40f0:8", ["const:bd3260:8", "const:4:8"]]
+ 00bd3260 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2e38 bytes 361f0294
+ 00bd3260 bytes 2c1f0294
- 00bd2e40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00bd2e40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd3268 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00bd3268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2e40 bytes 600603f9
+ 00bd3268 bytes 600605f9
- 00bd2e20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00bd2e20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd3248 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00bd3248 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2e20 bytes 680643f9
+ 00bd3248 bytes 680645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4cc1189917306a0c11145add9811fb4"></a>

### [`00bd2e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2e60.md) → [`00bd3288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd3288.md) _ZN8firebase4auth27too_many_requests_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd32e0",
      "incomplete_value": true,
      "site": "00bd32e0",
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
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2eb8",
      "incomplete_value": true,
      "site": "00bd2eb8",
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
            "const:610:8"
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
      "definition_site": "00bd32bc",
      "incomplete_value": true,
      "site": "00bd32c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2e94",
      "incomplete_value": true,
      "site": "00bd2ea0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:608:8"
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
      "00bd329c",
      "READ",
      [
        "storage",
        "01126610",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd32bc",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd32e0",
      "WRITE",
      [
        "storage",
        "01126610",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd329c",
      "READ",
      [
        "storage",
        "01126a10",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd32bc",
      "READ",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd32e0",
      "WRITE",
      [
        "storage",
        "01126a10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2e60.md#insn-00bd2ea0) · [`00bd2eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2e60.md#insn-00bd2eb8) · [`00bd2e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2e60.md#insn-00bd2e74)
- 新版 `00bd32c8`（命令位置の公開資料なし） · `00bd32e0`（命令位置の公開資料なし） · `00bd329c`（命令位置の公開資料なし）

~~~diff
- 00bd2ea0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2ea0 ["INT_ADD", "register:40f0:8", ["const:bd2ea0:8", "const:4:8"]]
- 00bd2ea0 ["CALLIND", null, ["register:0:8"]]
+ 00bd32c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd32c8 ["INT_ADD", "register:40f0:8", ["const:bd32c8:8", "const:4:8"]]
+ 00bd32c8 ["CALLIND", null, ["register:0:8"]]
- 00bd2ea0 bytes 00013fd6
+ 00bd32c8 bytes 00013fd6
- 00bd2eb8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd2eb8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:610:8"]]
- 00bd2eb8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd32e0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd32e0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a10:8"]]
+ 00bd32e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd2eb8 bytes a0421839
+ 00bd32e0 bytes a0422839
- 00bd2e74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:610:8"]]
- 00bd2e74 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd2e74 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd329c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a10:8"]]
+ 00bd329c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd329c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd2e74 bytes a8425839
+ 00bd329c bytes a8426839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d827bc61c11b5d3da9fa41eda3050106"></a>

### [`00bd2ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ecc.md) → [`00bd32f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd32f4.md) _ZN8firebase4auth27too_many_requests_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd3330",
      "incomplete_value": true,
      "site": "00bd3330",
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
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2f08",
      "incomplete_value": true,
      "site": "00bd2f08",
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
            "const:610:8"
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
      "definition_site": "00bd3350",
      "incomplete_value": true,
      "site": "00bd3350",
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
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2f28",
      "incomplete_value": true,
      "site": "00bd2f28",
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
            "const:608:8"
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
      "definition_site": "00bd330c",
      "incomplete_value": true,
      "site": "00bd330c",
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
      "definition_site": "00bd2ee4",
      "incomplete_value": true,
      "site": "00bd2ee4",
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
      "00bd3308",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3314",
      "READ",
      [
        "storage",
        "01126610",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd3330",
      "WRITE",
      [
        "storage",
        "01126610",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd3308",
      "READ",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3314",
      "READ",
      [
        "storage",
        "01126a10",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd3330",
      "WRITE",
      [
        "storage",
        "01126a10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ecc.md#insn-00bd2f08) · [`00bd2f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ecc.md#insn-00bd2f24) · [`00bd2f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ecc.md#insn-00bd2f28)
- 新版 `00bd3330`（命令位置の公開資料なし） · `00bd334c`（命令位置の公開資料なし） · `00bd3350`（命令位置の公開資料なし）

~~~diff
- 00bd2f08 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd2f08 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd2f08 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:610:8"]]
- 00bd2f08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd3330 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd3330 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd3330 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a10:8"]]
+ 00bd3330 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd2f08 bytes bf421839
+ 00bd3330 bytes bf422839
- 00bd2f24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2f24 ["INT_ADD", "register:40f0:8", ["const:bd2f24:8", "const:4:8"]]
- 00bd2f24 ["CALLIND", null, ["register:0:8"]]
+ 00bd334c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd334c ["INT_ADD", "register:40f0:8", ["const:bd334c:8", "const:4:8"]]
+ 00bd334c ["CALLIND", null, ["register:0:8"]]
- 00bd2f24 bytes 00013fd6
+ 00bd334c bytes 00013fd6
- 00bd2f28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
- 00bd2f28 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bd2f28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd3350 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a08:8"]]
+ 00bd3350 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd3350 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bd2f28 bytes 9f0603f9
+ 00bd3350 bytes 9f0605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca74bb1a07ed7860739247f30603aa60"></a>

### [`00bd2f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2f3c.md) → [`00bd3364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd3364.md) _ZN8firebase4auth27too_many_requests_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd33a4",
      "incomplete_value": true,
      "site": "00bd33a4",
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
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2f7c",
      "incomplete_value": true,
      "site": "00bd2f7c",
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
            "const:608:8"
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
      "definition_site": "00bd3380",
      "incomplete_value": true,
      "site": "00bd3380",
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
      "definition_site": "00bd2f58",
      "incomplete_value": true,
      "site": "00bd2f58",
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
      "definition_site": "00bd3388",
      "incomplete_value": false,
      "site": "00bd339c",
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
            "const:c19:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2f60",
      "incomplete_value": false,
      "site": "00bd2f74",
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
            "const:bd9:8"
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
      "00bd3378",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3388",
      "PARAM",
      [
        "storage",
        "002b5bd9",
        null,
        "string"
      ]
    ],
    [
      "00bd33a4",
      "WRITE",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd3378",
      "READ",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3388",
      "PARAM",
      [
        "storage",
        "002b5c19",
        null,
        "string"
      ]
    ],
    [
      "00bd33a4",
      "WRITE",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2f3c.md#insn-00bd2f74) · [`00bd2f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2f3c.md#insn-00bd2f7c) · [`00bd2f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2f3c.md#insn-00bd2f50)
- 新版 `00bd339c`（命令位置の公開資料なし） · `00bd33a4`（命令位置の公開資料なし） · `00bd3378`（命令位置の公開資料なし）

~~~diff
- 00bd2f74 ["INT_ADD", "register:40f0:8", ["const:bd2f74:8", "const:4:8"]]
- 00bd2f74 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd339c ["INT_ADD", "register:40f0:8", ["const:bd339c:8", "const:4:8"]]
+ 00bd339c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd2f74 bytes e71e0294
+ 00bd339c bytes dd1e0294
- 00bd2f7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
- 00bd2f7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd33a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a08:8"]]
+ 00bd33a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2f7c bytes 800603f9
+ 00bd33a4 bytes 800605f9
- 00bd2f50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
- 00bd2f50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd3378 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a08:8"]]
+ 00bd3378 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2f50 bytes 810643f9
+ 00bd3378 bytes 810645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88634a4930789add3185d6a631ad999d"></a>

### [`00bd2fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2fac.md) → [`00bd33d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd33d4.md) _ZN8firebase4auth27too_many_requests_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd33f0",
      "incomplete_value": false,
      "site": "00bd33f4",
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
      "definition_site": "00bd2fc8",
      "incomplete_value": false,
      "site": "00bd2fcc",
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
      "definition_site": "00bd3400",
      "incomplete_value": true,
      "site": "00bd340c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd2fd8",
      "incomplete_value": true,
      "site": "00bd2fe4",
      "value": [
        "LOAD",
        "8",
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
      "00bd33f0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd3400",
      "DATA",
      [
        "storage",
        "01126618",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd33f0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd3400",
      "DATA",
      [
        "storage",
        "01126a18",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2fac.md#insn-00bd2fcc) · [`00bd2fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2fac.md#insn-00bd2fc8) · [`00bd2fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2fac.md#insn-00bd2fd4)
- 新版 `00bd33f4`（命令位置の公開資料なし） · `00bd33f0`（命令位置の公開資料なし） · `00bd33fc`（命令位置の公開資料なし）

~~~diff
- 00bd2fcc ["INT_ADD", "register:40f0:8", ["const:bd2fcc:8", "const:4:8"]]
- 00bd2fcc ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd33f4 ["INT_ADD", "register:40f0:8", ["const:bd33f4:8", "const:4:8"]]
+ 00bd33f4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd2fcc bytes 0d1f0294
+ 00bd33f4 bytes 031f0294
- 00bd2fc8 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd2fc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd2fc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd2fc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd33f0 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd33f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd33f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd33f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd2fc8 bytes 00680a91
+ 00bd33f0 bytes 009c0d91
- 00bd2fd4 ["COPY", "tmp:0:8", ["const:618:8"]]
- 00bd2fd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2fd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2fd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd33fc ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 00bd33fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd33fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd33fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd2fd4 bytes 08611891
+ 00bd33fc bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a376bce67de793a7a70acb16f1bb1fe0"></a>

### [`00bd2fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2fe8.md) → [`00bd3410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd3410.md) _ZN8firebase4auth27too_many_requests_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd3450",
      "incomplete_value": true,
      "site": "00bd3450",
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
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3028",
      "incomplete_value": true,
      "site": "00bd3028",
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
            "const:608:8"
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
      "definition_site": "00bd342c",
      "incomplete_value": true,
      "site": "00bd342c",
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
      "definition_site": "00bd3004",
      "incomplete_value": true,
      "site": "00bd3004",
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
      "definition_site": "00bd3434",
      "incomplete_value": false,
      "site": "00bd3448",
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
            "const:c19:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd300c",
      "incomplete_value": false,
      "site": "00bd3020",
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
            "const:bd9:8"
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
      "00bd3424",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3434",
      "PARAM",
      [
        "storage",
        "002b5bd9",
        null,
        "string"
      ]
    ],
    [
      "00bd3450",
      "WRITE",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd3424",
      "READ",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3434",
      "PARAM",
      [
        "storage",
        "002b5c19",
        null,
        "string"
      ]
    ],
    [
      "00bd3450",
      "WRITE",
      [
        "storage",
        "01126a08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2fe8.md#insn-00bd3020) · [`00bd3028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2fe8.md#insn-00bd3028) · [`00bd2ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2fe8.md#insn-00bd2ffc)
- 新版 `00bd3448`（命令位置の公開資料なし） · `00bd3450`（命令位置の公開資料なし） · `00bd3424`（命令位置の公開資料なし）

~~~diff
- 00bd3020 ["INT_ADD", "register:40f0:8", ["const:bd3020:8", "const:4:8"]]
- 00bd3020 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd3448 ["INT_ADD", "register:40f0:8", ["const:bd3448:8", "const:4:8"]]
+ 00bd3448 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd3020 bytes bc1e0294
+ 00bd3448 bytes b21e0294
- 00bd3028 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
- 00bd3028 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd3450 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a08:8"]]
+ 00bd3450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd3028 bytes 800603f9
+ 00bd3450 bytes 800605f9
- 00bd2ffc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
- 00bd2ffc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd3424 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a08:8"]]
+ 00bd3424 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd2ffc bytes 810643f9
+ 00bd3424 bytes 810645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99ce126a5586531e21ddb0a633257ca9"></a>

### [`00bd3058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3058.md) → [`00bd3480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd3480.md) _ZN8firebase4auth27too_many_requests_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd349c",
      "incomplete_value": false,
      "site": "00bd34a0",
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
      "definition_site": "00bd3074",
      "incomplete_value": false,
      "site": "00bd3078",
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
      "definition_site": "00bd34ac",
      "incomplete_value": true,
      "site": "00bd34b8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd3084",
      "incomplete_value": true,
      "site": "00bd3090",
      "value": [
        "LOAD",
        "8",
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
      "00bd349c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd34ac",
      "DATA",
      [
        "storage",
        "01126620",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd349c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd34ac",
      "DATA",
      [
        "storage",
        "01126a20",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3058.md#insn-00bd3078) · [`00bd3074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3058.md#insn-00bd3074) · [`00bd3080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3058.md#insn-00bd3080)
- 新版 `00bd34a0`（命令位置の公開資料なし） · `00bd349c`（命令位置の公開資料なし） · `00bd34a8`（命令位置の公開資料なし）

~~~diff
- 00bd3078 ["INT_ADD", "register:40f0:8", ["const:bd3078:8", "const:4:8"]]
- 00bd3078 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd34a0 ["INT_ADD", "register:40f0:8", ["const:bd34a0:8", "const:4:8"]]
+ 00bd34a0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd3078 bytes e21e0294
+ 00bd34a0 bytes d81e0294
- 00bd3074 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd3074 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd3074 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd3074 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd349c ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd349c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd349c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd349c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd3074 bytes 00441191
+ 00bd349c bytes 00781491
- 00bd3080 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00bd3080 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd3080 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd3080 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd34a8 ["COPY", "tmp:0:8", ["const:a20:8"]]
+ 00bd34a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd34a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd34a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd3080 bytes 08811891
+ 00bd34a8 bytes 08812891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea0ffa3189a92a8c799c0ec5aef6e98b"></a>

### [`00bd3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3094.md) → [`00bd34bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd34bc.md) _ZN8firebase4auth18firebase_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "definition_site": "00bd34e8",
      "incomplete_value": true,
      "site": "00bd34e8",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd30c0",
      "incomplete_value": true,
      "site": "00bd30c0",
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
            "const:628:8"
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
      "definition_site": "00bd34d0",
      "incomplete_value": true,
      "site": "00bd34d0",
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
      "definition_site": "00bd30a8",
      "incomplete_value": true,
      "site": "00bd30a8",
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
      "definition_site": "00bd34dc",
      "incomplete_value": false,
      "site": "00bd34e0",
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
            "const:d37:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd30b4",
      "incomplete_value": false,
      "site": "00bd30b8",
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
            "const:c6a:8"
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
      "00bd34cc",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd34dc",
      "PARAM",
      [
        "storage",
        "002a2c6a",
        null,
        "string"
      ]
    ],
    [
      "00bd34e8",
      "WRITE",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd34cc",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd34dc",
      "PARAM",
      [
        "storage",
        "002a2d37",
        null,
        "string"
      ]
    ],
    [
      "00bd34e8",
      "WRITE",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd30b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3094.md#insn-00bd30b8) · [`00bd30c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3094.md#insn-00bd30c0) · [`00bd30a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3094.md#insn-00bd30a4)
- 新版 `00bd34e0`（命令位置の公開資料なし） · `00bd34e8`（命令位置の公開資料なし） · `00bd34cc`（命令位置の公開資料なし）

~~~diff
- 00bd30b8 ["INT_ADD", "register:40f0:8", ["const:bd30b8:8", "const:4:8"]]
- 00bd30b8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd34e0 ["INT_ADD", "register:40f0:8", ["const:bd34e0:8", "const:4:8"]]
+ 00bd34e0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd30b8 bytes 961e0294
+ 00bd34e0 bytes 8c1e0294
- 00bd30c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 00bd30c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd34e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
+ 00bd34e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd30c0 bytes 601603f9
+ 00bd34e8 bytes 601605f9
- 00bd30a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 00bd30a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd34cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
+ 00bd34cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd30a4 bytes 681643f9
+ 00bd34cc bytes 681645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd2a81b6d74a6073e66a2c8986e49c5d"></a>

### [`00bd30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd30d4.md) → [`00bd34fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd34fc.md) _ZN8firebase4auth18firebase_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "definition_site": "00bd3528",
      "incomplete_value": true,
      "site": "00bd3528",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3100",
      "incomplete_value": true,
      "site": "00bd3100",
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
            "const:628:8"
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
      "definition_site": "00bd3510",
      "incomplete_value": true,
      "site": "00bd3510",
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
      "definition_site": "00bd30e8",
      "incomplete_value": true,
      "site": "00bd30e8",
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
      "definition_site": "00bd3518",
      "incomplete_value": false,
      "site": "00bd3520",
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
            "const:d37:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd30f0",
      "incomplete_value": false,
      "site": "00bd30f8",
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
            "const:c6a:8"
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
      "00bd350c",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3518",
      "PARAM",
      [
        "storage",
        "002a2c6a",
        null,
        "string"
      ]
    ],
    [
      "00bd3528",
      "WRITE",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd350c",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3518",
      "PARAM",
      [
        "storage",
        "002a2d37",
        null,
        "string"
      ]
    ],
    [
      "00bd3528",
      "WRITE",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd30f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd30d4.md#insn-00bd30f8) · [`00bd3100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd30d4.md#insn-00bd3100) · [`00bd30e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd30d4.md#insn-00bd30e4)
- 新版 `00bd3520`（命令位置の公開資料なし） · `00bd3528`（命令位置の公開資料なし） · `00bd350c`（命令位置の公開資料なし）

~~~diff
- 00bd30f8 ["INT_ADD", "register:40f0:8", ["const:bd30f8:8", "const:4:8"]]
- 00bd30f8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd3520 ["INT_ADD", "register:40f0:8", ["const:bd3520:8", "const:4:8"]]
+ 00bd3520 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd30f8 bytes 861e0294
+ 00bd3520 bytes 7c1e0294
- 00bd3100 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 00bd3100 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd3528 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
+ 00bd3528 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd3100 bytes 601603f9
+ 00bd3528 bytes 601605f9
- 00bd30e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 00bd30e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd350c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
+ 00bd350c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd30e4 bytes 681643f9
+ 00bd350c bytes 681645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3102b0a28e849523bf2add8c7ca9efad"></a>

### [`00bd3158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3158.md) → [`00bd3580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd3580.md) _ZN8firebase4auth18firebase_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd35b0",
      "incomplete_value": true,
      "site": "00bd35b0",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3188",
      "incomplete_value": true,
      "site": "00bd3188",
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
            "const:628:8"
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
      "definition_site": "00bd3594",
      "incomplete_value": true,
      "site": "00bd3594",
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
      "definition_site": "00bd316c",
      "incomplete_value": true,
      "site": "00bd316c",
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
      "definition_site": "00bd359c",
      "incomplete_value": false,
      "site": "00bd35a8",
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
            "const:d37:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3174",
      "incomplete_value": false,
      "site": "00bd3180",
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
            "const:c6a:8"
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
      "00bd3590",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd359c",
      "PARAM",
      [
        "storage",
        "002a2c6a",
        null,
        "string"
      ]
    ],
    [
      "00bd35b0",
      "WRITE",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd3590",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd359c",
      "PARAM",
      [
        "storage",
        "002a2d37",
        null,
        "string"
      ]
    ],
    [
      "00bd35b0",
      "WRITE",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3158.md#insn-00bd3180) · [`00bd3188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3158.md#insn-00bd3188) · [`00bd3168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3158.md#insn-00bd3168)
- 新版 `00bd35a8`（命令位置の公開資料なし） · `00bd35b0`（命令位置の公開資料なし） · `00bd3590`（命令位置の公開資料なし）

~~~diff
- 00bd3180 ["INT_ADD", "register:40f0:8", ["const:bd3180:8", "const:4:8"]]
- 00bd3180 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd35a8 ["INT_ADD", "register:40f0:8", ["const:bd35a8:8", "const:4:8"]]
+ 00bd35a8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd3180 bytes 641e0294
+ 00bd35a8 bytes 5a1e0294
- 00bd3188 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 00bd3188 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd35b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
+ 00bd35b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd3188 bytes 601603f9
+ 00bd35b0 bytes 601605f9
- 00bd3168 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 00bd3168 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd3590 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
+ 00bd3590 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd3168 bytes 681643f9
+ 00bd3590 bytes 681645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5563939cd490127b54a8e563a615c06"></a>

### [`00bd31a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd31a8.md) → [`00bd35d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd35d0.md) _ZN8firebase4auth18firebase_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd3628",
      "incomplete_value": true,
      "site": "00bd3628",
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
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3200",
      "incomplete_value": true,
      "site": "00bd3200",
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
            "const:630:8"
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
      "definition_site": "00bd3604",
      "incomplete_value": true,
      "site": "00bd3610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd31dc",
      "incomplete_value": true,
      "site": "00bd31e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:628:8"
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
      "00bd35e4",
      "READ",
      [
        "storage",
        "01126630",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd3604",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3628",
      "WRITE",
      [
        "storage",
        "01126630",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd35e4",
      "READ",
      [
        "storage",
        "01126a30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd3604",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3628",
      "WRITE",
      [
        "storage",
        "01126a30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd31e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd31a8.md#insn-00bd31e8) · [`00bd3200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd31a8.md#insn-00bd3200) · [`00bd31bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd31a8.md#insn-00bd31bc)
- 新版 `00bd3610`（命令位置の公開資料なし） · `00bd3628`（命令位置の公開資料なし） · `00bd35e4`（命令位置の公開資料なし）

~~~diff
- 00bd31e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd31e8 ["INT_ADD", "register:40f0:8", ["const:bd31e8:8", "const:4:8"]]
- 00bd31e8 ["CALLIND", null, ["register:0:8"]]
+ 00bd3610 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd3610 ["INT_ADD", "register:40f0:8", ["const:bd3610:8", "const:4:8"]]
+ 00bd3610 ["CALLIND", null, ["register:0:8"]]
- 00bd31e8 bytes 00013fd6
+ 00bd3610 bytes 00013fd6
- 00bd3200 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd3200 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:630:8"]]
- 00bd3200 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd3628 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd3628 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a30:8"]]
+ 00bd3628 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd3200 bytes a0c21839
+ 00bd3628 bytes a0c22839
- 00bd31bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:630:8"]]
- 00bd31bc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd31bc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd35e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a30:8"]]
+ 00bd35e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd35e4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd31bc bytes a8c25839
+ 00bd35e4 bytes a8c26839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc9a01a79f5e376c212de9cd7442006a"></a>

### [`00bd3214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3214.md) → [`00bd363c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd363c.md) _ZN8firebase4auth18firebase_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 16.67% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3250"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3270"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd3678"
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
      "00bd3650",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd365c",
      "READ",
      [
        "storage",
        "01126630",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd3664",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd3254"
      ]
    ]
  ],
  "added": [
    [
      "00bd3650",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd365c",
      "READ",
      [
        "storage",
        "01126a30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd3664",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd367c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd322c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3214.md#insn-00bd322c) · [`00bd3250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3214.md#insn-00bd3250) · [`00bd3258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3214.md#insn-00bd3258)
- 新版 `00bd3654`（命令位置の公開資料なし）

~~~diff
- 00bd322c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd322c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd3654 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd3654 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bd322c bytes 410200b4
+ 00bd3654 bytes 410200b4
- 00bd3250 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd3250 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd3250 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:630:8"]]
- 00bd3250 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd3250 bytes bfc21839
- 00bd3258 ["INT_ADD", "register:40f0:8", ["const:bd3258:8", "const:4:8"]]
- 00bd3258 ["CALL", null, ["callee:00c5af60:8"]]
- 00bd3258 bytes 421e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb14ede4dab683ffc446aba23457e386"></a>

### [`00bd3284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3284.md) → [`00bd36ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd36ac.md) _ZN8firebase4auth18firebase_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd32c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd36ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd32a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd3298",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd32a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd36f0"
      ]
    ],
    [
      "unmatched:00bd32a8",
      "PARAM",
      [
        "storage",
        "002a2c6a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd36c0",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd36c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd36f0"
      ]
    ],
    [
      "00bd36d0",
      "PARAM",
      [
        "storage",
        "002a2d37",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd32a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3284.md#insn-00bd32a0) · [`00bd32bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3284.md#insn-00bd32bc) · [`00bd32c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3284.md#insn-00bd32c4)
- 新版 `00bd36e4`（命令位置の公開資料なし）

~~~diff
- 00bd32a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd32a0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd32a0 bytes 410100b5
- 00bd32bc ["INT_ADD", "register:40f0:8", ["const:bd32bc:8", "const:4:8"]]
- 00bd32bc ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd36e4 ["INT_ADD", "register:40f0:8", ["const:bd36e4:8", "const:4:8"]]
+ 00bd36e4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd32bc bytes 151e0294
+ 00bd36e4 bytes 0b1e0294
- 00bd32c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:628:8"]]
- 00bd32c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd32c4 bytes 801603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fba3ad68ba03b605e72ffa6aedb240cb"></a>

### [`00bd32f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd32f4.md) → [`00bd371c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd371c.md) _ZN8firebase4auth18firebase_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd3738",
      "incomplete_value": false,
      "site": "00bd373c",
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
      "definition_site": "00bd3310",
      "incomplete_value": false,
      "site": "00bd3314",
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
      "definition_site": "00bd3748",
      "incomplete_value": true,
      "site": "00bd3754",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd3320",
      "incomplete_value": true,
      "site": "00bd332c",
      "value": [
        "LOAD",
        "8",
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
      "00bd3738",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd3748",
      "DATA",
      [
        "storage",
        "01126638",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd3738",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd3748",
      "DATA",
      [
        "storage",
        "01126a38",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd32f4.md#insn-00bd3314) · [`00bd3310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd32f4.md#insn-00bd3310) · [`00bd331c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd32f4.md#insn-00bd331c)
- 新版 `00bd373c`（命令位置の公開資料なし） · `00bd3738`（命令位置の公開資料なし） · `00bd3744`（命令位置の公開資料なし）

~~~diff
- 00bd3314 ["INT_ADD", "register:40f0:8", ["const:bd3314:8", "const:4:8"]]
- 00bd3314 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd373c ["INT_ADD", "register:40f0:8", ["const:bd373c:8", "const:4:8"]]
+ 00bd373c ["CALL", null, ["callee:00c5b000:8"]]
- 00bd3314 bytes 3b1e0294
+ 00bd373c bytes 311e0294
- 00bd3310 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd3310 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd3310 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd3310 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd3738 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd3738 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd3738 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd3738 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd3310 bytes 00680a91
+ 00bd3738 bytes 009c0d91
- 00bd331c ["COPY", "tmp:0:8", ["const:638:8"]]
- 00bd331c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd331c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd331c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd3744 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 00bd3744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd331c bytes 08e11891
+ 00bd3744 bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09c898895b4c6c8d40b23f61e7223db2"></a>

### [`00bd3330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3330.md) → [`00bd3758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd3758.md) _ZN8firebase4auth18firebase_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd3370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd3798"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd334c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd3344",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd334c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd379c"
      ]
    ],
    [
      "unmatched:00bd3354",
      "PARAM",
      [
        "storage",
        "002a2c6a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd376c",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3774",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd379c"
      ]
    ],
    [
      "00bd377c",
      "PARAM",
      [
        "storage",
        "002a2d37",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd334c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3330.md#insn-00bd334c) · [`00bd3368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3330.md#insn-00bd3368) · [`00bd3370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3330.md#insn-00bd3370)
- 新版 `00bd3790`（命令位置の公開資料なし）

~~~diff
- 00bd334c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd334c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd334c bytes 410100b5
- 00bd3368 ["INT_ADD", "register:40f0:8", ["const:bd3368:8", "const:4:8"]]
- 00bd3368 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd3790 ["INT_ADD", "register:40f0:8", ["const:bd3790:8", "const:4:8"]]
+ 00bd3790 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd3368 bytes ea1d0294
+ 00bd3790 bytes e01d0294
- 00bd3370 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:628:8"]]
- 00bd3370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd3370 bytes 801603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2814dd345a7c24f1e84c3b5de29c7b21"></a>

### [`00bd33a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd33a0.md) → [`00bd37c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd37c8.md) _ZN8firebase4auth18firebase_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd37e4",
      "incomplete_value": false,
      "site": "00bd37e8",
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
      "definition_site": "00bd33bc",
      "incomplete_value": false,
      "site": "00bd33c0",
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
      "definition_site": "00bd37f4",
      "incomplete_value": true,
      "site": "00bd3800",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd33cc",
      "incomplete_value": true,
      "site": "00bd33d8",
      "value": [
        "LOAD",
        "8",
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
      "00bd37e4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd37f4",
      "DATA",
      [
        "storage",
        "01126640",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd37e4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd37f4",
      "DATA",
      [
        "storage",
        "01126a40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd33c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd33a0.md#insn-00bd33c0) · [`00bd33bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd33a0.md#insn-00bd33bc) · [`00bd33c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd33a0.md#insn-00bd33c8)
- 新版 `00bd37e8`（命令位置の公開資料なし） · `00bd37e4`（命令位置の公開資料なし） · `00bd37f0`（命令位置の公開資料なし）

~~~diff
- 00bd33c0 ["INT_ADD", "register:40f0:8", ["const:bd33c0:8", "const:4:8"]]
- 00bd33c0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd37e8 ["INT_ADD", "register:40f0:8", ["const:bd37e8:8", "const:4:8"]]
+ 00bd37e8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd33c0 bytes 101e0294
+ 00bd37e8 bytes 061e0294
- 00bd33bc ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd33bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd33bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd33bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd37e4 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd37e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd37e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd37e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd33bc bytes 00441191
+ 00bd37e4 bytes 00781491
- 00bd33c8 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00bd33c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd33c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd33c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd37f0 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00bd37f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd37f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd37f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd33c8 bytes 08011991
+ 00bd37f0 bytes 08012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c4de45f6e4e1d58be32ab260f35b713"></a>

### [`00bd33dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd33dc.md) → [`00bd3804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd3804.md) _ZN8firebase4auth20CacheCommonMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d890.md) · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 1件 [`00c5dc90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc90.md) · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 13.41% / 新版 13.41%

CFGの説明率　旧版 3.61% / 新版 3.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 25件, `unresolved_call_alignment` 26件, `unresolved_store_alignment` 15件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3420"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3478"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd34d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd33f4",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd33fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd3850"
      ]
    ],
    [
      "unmatched:00bd3404",
      "PARAM",
      [
        "storage",
        "002a0c88",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd381c",
      "READ",
      [
        "storage",
        "011269a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3824",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd3850"
      ]
    ],
    [
      "00bd382c",
      "PARAM",
      [
        "storage",
        "002a0d55",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd33fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd33dc.md#insn-00bd33fc) · [`00bd3418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd33dc.md#insn-00bd3418) · [`00bd3420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd33dc.md#insn-00bd3420)
- 新版 `00bd3840`（命令位置の公開資料なし）

~~~diff
- 00bd33fc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd33fc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd33fc bytes 610100b5
- 00bd3418 ["INT_ADD", "register:40f0:8", ["const:bd3418:8", "const:4:8"]]
- 00bd3418 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd3840 ["INT_ADD", "register:40f0:8", ["const:bd3840:8", "const:4:8"]]
+ 00bd3840 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd3418 bytes be1d0294
+ 00bd3840 bytes b41d0294
- 00bd3420 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a8:8"]]
- 00bd3420 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd3420 bytes a0d602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad76e4fe3cdd06332505cdc567485a66"></a>

### [`00bd3938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3938.md) → [`00bd3d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd3d60.md) _ZN8firebase4auth20ReleaseCommonClassesEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8a0.md) · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5dca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dca0.md) · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 6.80% / 新版 6.80%

CFGの説明率　旧版 1.00% / 新版 1.01%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_branch_alignment` 29件, `unresolved_call_alignment` 43件, `unresolved_store_alignment` 29件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3974"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3994"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd39c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd3d74",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3d7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd3998"
      ]
    ],
    [
      "00bd3d84",
      "READ",
      [
        "storage",
        "01126450",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd3d74",
      "READ",
      [
        "storage",
        "01126848",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3d7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd3dc0"
      ]
    ],
    [
      "00bd3d84",
      "READ",
      [
        "storage",
        "01126850",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3938.md#insn-00bd3974) · [`00bd3994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3938.md#insn-00bd3994) · [`00bd39c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3938.md#insn-00bd39c0)

~~~diff
- 00bd3974 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd3974 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd3974 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:450:8"]]
- 00bd3974 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd3974 bytes bf421139
- 00bd3994 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:448:8"]]
- 00bd3994 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bd3994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bd3994 bytes 9f2602f9
- 00bd39c0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd39c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd39c0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:480:8"]]
- 00bd39c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd39c0 bytes bf021239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9626cdb4a7c4c0991019da0adb28df11"></a>

### [`00bd3dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3dd0.md) → [`00bd41f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd41f8.md) _ZN8firebase4auth22ErrorCodeFromExceptionEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d980.md) · 呼出先 10件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5dd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd80.md) · 呼出先 10件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.43% / 新版 69.43%

CFGの説明率　旧版 39.53% / 新版 36.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 27件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3dd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3dd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3dd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd3dd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd3dd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd3ddc",
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
      "00bd41fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bd4200",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bd4204",
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

- 旧版 [`00bd3dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3dd0.md#insn-00bd3dd4) · [`00bd3dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3dd0.md#insn-00bd3dd8) · [`00bd3ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3dd0.md#insn-00bd3ddc)

~~~diff
- 00bd3dd4 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bd3dd4 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bd3dd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 00bd3dd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd3dd4 bytes fc6f18a9
- 00bd3dd8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bd3dd8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bd3dd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:190:8"]]
- 00bd3dd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd3dd8 bytes fa6719a9
- 00bd3ddc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bd3ddc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bd3ddc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 00bd3ddc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd3ddc bytes f85f1aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-608638837d6259bb42e81e0c95bc83fe"></a>

### [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) → [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) _ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 11件 [`00bcdca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdca0.md) [`00bce468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce468.md) [`00bce6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce6d8.md) [`00bce864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce864.md) [`00bceaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceaf0.md) · 呼出先 11件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5f0.md) [`00c5a630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a630.md) [`00c5a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a650.md)
- 新版 呼出元 11件 [`00bce0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce0c8.md) [`00bce890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce890.md) [`00bceb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bceb00.md) [`00bcec8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcec8c.md) [`00bcef18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcef18.md) · 呼出先 11件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a9f0.md) [`00c5aa30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 89.42% / 新版 89.42%

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
      "site": "00bd4580"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd49a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd4884",
      "incomplete_value": true,
      "site": "00bd488c",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": null,
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
      "00bd4880",
      "READ",
      [
        "storage",
        "01126458",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd44f4",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd4500",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00497834"
      ]
    ]
  ],
  "added": [
    [
      "00bd4880",
      "READ",
      [
        "storage",
        "01126858",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd491c",
      "READ",
      [
        "storage",
        "01126860",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4928",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00497834"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md#insn-00bd4464) · [`00bd448c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md#insn-00bd448c) · [`00bd44c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md#insn-00bd44c0)
- 新版 `00bd488c`（命令位置の公開資料なし）

~~~diff
- 00bd4464 ["INT_ADD", "register:40f0:8", ["const:bd4464:8", "const:4:8"]]
- 00bd4464 ["CALL", null, ["callee:00497834:8"]]
+ 00bd488c ["INT_ADD", "register:40f0:8", ["const:bd488c:8", "const:4:8"]]
+ 00bd488c ["CALL", null, ["callee:00497834:8"]]
- 00bd4464 bytes e40ce397
+ 00bd488c bytes ea0be397
- 00bd448c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd448c ["INT_ADD", "register:40f0:8", ["const:bd448c:8", "const:4:8"]]
- 00bd448c ["CALLIND", null, ["register:0:8"]]
- 00bd448c bytes 00013fd6
- 00bd44c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd44c0 ["INT_ADD", "register:40f0:8", ["const:bd44c0:8", "const:4:8"]]
- 00bd44c0 ["CALLIND", null, ["register:0:8"]]
- 00bd44c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0f57d128d2554ffd3261273be9cc806"></a>

### [`00bd45cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd45cc.md) → [`00bd49f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd49f4.md) _ZN8firebase4auth22ReadAdditionalUserInfoEP7_JNIEnvP8_jobjectPNS0_18AdditionalUserInfoE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d990.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5f0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5dd90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd90.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a9f0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 60.00% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd45d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd45d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd45d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd45d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd45d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd45d8",
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
      "00bd49f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bd49fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bd4a00",
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

- 旧版 [`00bd45d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd45cc.md#insn-00bd45d0) · [`00bd45d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd45cc.md#insn-00bd45d4) · [`00bd45d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd45cc.md#insn-00bd45d8)

~~~diff
- 00bd45d0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:80:8"]]
- 00bd45d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00bd45d0 bytes f94300f9
- 00bd45d4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bd45d4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bd45d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00bd45d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd45d4 bytes f85f09a9
- 00bd45d8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bd45d8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bd45d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00bd45d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd45d8 bytes f6570aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40267cb27191cc675928f40ed1910d65"></a>

### [`00bd4814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4814.md) → [`00bd4c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4c3c.md) _ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bce0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce0b4.md) [`00bdfddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfddc.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a630.md) [`00c5a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a650.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 2件 [`00bce4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce4dc.md) [`00be0204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0204.md) · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa50.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.57% / 新版 98.57%

CFGの説明率　旧版 91.67% / 新版 84.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd4c90",
      "incomplete_value": true,
      "site": "00bd4c9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:858:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4868",
      "incomplete_value": true,
      "site": "00bd4874",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:458:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4924"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bd4d4c"
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
      "00bd4c90",
      "READ",
      [
        "storage",
        "01126458",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd4c90",
      "READ",
      [
        "storage",
        "01126858",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4814.md#insn-00bd4874) · [`00bd4924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4814.md#insn-00bd4924)
- 新版 `00bd4c9c`（命令位置の公開資料なし） · `00bd4d4c`（命令位置の公開資料なし）

~~~diff
- 00bd4874 ["INT_ADD", "register:40f0:8", ["const:bd4874:8", "const:4:8"]]
- 00bd4874 ["CALL", null, ["callee:00497834:8"]]
+ 00bd4c9c ["INT_ADD", "register:40f0:8", ["const:bd4c9c:8", "const:4:8"]]
+ 00bd4c9c ["CALL", null, ["callee:00497834:8"]]
- 00bd4874 bytes e00be397
+ 00bd4c9c bytes e60ae397
- 00bd4924 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd4924 ["RETURN", null, ["register:0:8"]]
- 00bd4924 bytes c0035fd6
+ 00bd4d4c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bd4d4c ["RETURN", null, ["register:0:8"]]
+ 00bd4d4c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac6e8e74e49c6e654580ed5b3b8cb25f"></a>

### [`00bd4a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4a58.md) → [`00bd4e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4e80.md) _ZN8firebase4auth10credential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00bd4eac",
      "incomplete_value": true,
      "site": "00bd4eac",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4a84",
      "incomplete_value": true,
      "site": "00bd4a84",
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
            "const:648:8"
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
      "definition_site": "00bd4e94",
      "incomplete_value": true,
      "site": "00bd4e94",
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
      "definition_site": "00bd4a6c",
      "incomplete_value": true,
      "site": "00bd4a6c",
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
      "definition_site": "00bd4ea0",
      "incomplete_value": false,
      "site": "00bd4ea4",
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
            "const:d1c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4a78",
      "incomplete_value": false,
      "site": "00bd4a7c",
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
            "const:cdc:8"
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
      "00bd4e90",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4ea0",
      "PARAM",
      [
        "storage",
        "002b9cdc",
        null,
        "string"
      ]
    ],
    [
      "00bd4eac",
      "WRITE",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd4e90",
      "READ",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4ea0",
      "PARAM",
      [
        "storage",
        "002b9d1c",
        null,
        "string"
      ]
    ],
    [
      "00bd4eac",
      "WRITE",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4a58.md#insn-00bd4a7c) · [`00bd4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4a58.md#insn-00bd4a84) · [`00bd4a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4a58.md#insn-00bd4a68)
- 新版 `00bd4ea4`（命令位置の公開資料なし） · `00bd4eac`（命令位置の公開資料なし） · `00bd4e90`（命令位置の公開資料なし）

~~~diff
- 00bd4a7c ["INT_ADD", "register:40f0:8", ["const:bd4a7c:8", "const:4:8"]]
- 00bd4a7c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd4ea4 ["INT_ADD", "register:40f0:8", ["const:bd4ea4:8", "const:4:8"]]
+ 00bd4ea4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd4a7c bytes 25180294
+ 00bd4ea4 bytes 1b180294
- 00bd4a84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00bd4a84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd4eac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00bd4eac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd4a84 bytes 602603f9
+ 00bd4eac bytes 602605f9
- 00bd4a68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00bd4a68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd4e90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00bd4e90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd4a68 bytes 682643f9
+ 00bd4e90 bytes 682645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28326c928d608eda8d7062818fbcb710"></a>

### [`00bd4a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4a98.md) → [`00bd4ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4ec0.md) _ZN8firebase4auth10credential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bd4eec",
      "incomplete_value": true,
      "site": "00bd4eec",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4ac4",
      "incomplete_value": true,
      "site": "00bd4ac4",
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
            "const:648:8"
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
      "definition_site": "00bd4ed4",
      "incomplete_value": true,
      "site": "00bd4ed4",
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
      "definition_site": "00bd4aac",
      "incomplete_value": true,
      "site": "00bd4aac",
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
      "definition_site": "00bd4edc",
      "incomplete_value": false,
      "site": "00bd4ee4",
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
            "const:d1c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4ab4",
      "incomplete_value": false,
      "site": "00bd4abc",
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
            "const:cdc:8"
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
      "00bd4ed0",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4edc",
      "PARAM",
      [
        "storage",
        "002b9cdc",
        null,
        "string"
      ]
    ],
    [
      "00bd4eec",
      "WRITE",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd4ed0",
      "READ",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4edc",
      "PARAM",
      [
        "storage",
        "002b9d1c",
        null,
        "string"
      ]
    ],
    [
      "00bd4eec",
      "WRITE",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4a98.md#insn-00bd4abc) · [`00bd4ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4a98.md#insn-00bd4ac4) · [`00bd4aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4a98.md#insn-00bd4aa8)
- 新版 `00bd4ee4`（命令位置の公開資料なし） · `00bd4eec`（命令位置の公開資料なし） · `00bd4ed0`（命令位置の公開資料なし）

~~~diff
- 00bd4abc ["INT_ADD", "register:40f0:8", ["const:bd4abc:8", "const:4:8"]]
- 00bd4abc ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd4ee4 ["INT_ADD", "register:40f0:8", ["const:bd4ee4:8", "const:4:8"]]
+ 00bd4ee4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd4abc bytes 15180294
+ 00bd4ee4 bytes 0b180294
- 00bd4ac4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00bd4ac4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd4eec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00bd4eec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd4ac4 bytes 602603f9
+ 00bd4eec bytes 602605f9
- 00bd4aa8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00bd4aa8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd4ed0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00bd4ed0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd4aa8 bytes 682643f9
+ 00bd4ed0 bytes 682645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e37fcfb7521cbe60c9c74bb86f08c79"></a>

### [`00bd4ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4ad8.md) → [`00bd4f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4f00.md) _ZN8firebase4auth10credential10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd4f30",
      "incomplete_value": true,
      "site": "00bd4f30",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4b08",
      "incomplete_value": true,
      "site": "00bd4b08",
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
            "const:648:8"
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
      "definition_site": "00bd4f14",
      "incomplete_value": true,
      "site": "00bd4f14",
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
      "definition_site": "00bd4aec",
      "incomplete_value": true,
      "site": "00bd4aec",
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
      "definition_site": "00bd4f20",
      "incomplete_value": false,
      "site": "00bd4f28",
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
            "const:d1c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4af8",
      "incomplete_value": false,
      "site": "00bd4b00",
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
            "const:cdc:8"
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
      "00bd4f10",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4f20",
      "PARAM",
      [
        "storage",
        "002b9cdc",
        null,
        "string"
      ]
    ],
    [
      "00bd4f30",
      "WRITE",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd4f10",
      "READ",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4f20",
      "PARAM",
      [
        "storage",
        "002b9d1c",
        null,
        "string"
      ]
    ],
    [
      "00bd4f30",
      "WRITE",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4ad8.md#insn-00bd4b00) · [`00bd4b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4ad8.md#insn-00bd4b08) · [`00bd4ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4ad8.md#insn-00bd4ae8)
- 新版 `00bd4f28`（命令位置の公開資料なし） · `00bd4f30`（命令位置の公開資料なし） · `00bd4f10`（命令位置の公開資料なし）

~~~diff
- 00bd4b00 ["INT_ADD", "register:40f0:8", ["const:bd4b00:8", "const:4:8"]]
- 00bd4b00 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd4f28 ["INT_ADD", "register:40f0:8", ["const:bd4f28:8", "const:4:8"]]
+ 00bd4f28 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd4b00 bytes 04180294
+ 00bd4f28 bytes fa170294
- 00bd4b08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00bd4b08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd4f30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00bd4f30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd4b08 bytes 602603f9
+ 00bd4f30 bytes 602605f9
- 00bd4ae8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00bd4ae8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd4f10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00bd4f10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd4ae8 bytes 682643f9
+ 00bd4f10 bytes 682645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-117874467c2b298b34676a29eda13d4f"></a>

### [`00bd4b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4b1c.md) → [`00bd4f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4f44.md) _ZN8firebase4auth10credential10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00bd4b4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd4f74"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd4f58",
      "incomplete_value": true,
      "site": "00bd4f58",
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
      "definition_site": "00bd4b30",
      "incomplete_value": true,
      "site": "00bd4b30",
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
      "00bd4f54",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd4b38",
      "PARAM",
      [
        "storage",
        "002b9cdc",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd4b4c",
      "WRITE",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd4f54",
      "READ",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4f60",
      "PARAM",
      [
        "storage",
        "002b9d1c",
        null,
        "string"
      ]
    ],
    [
      "00bd4f74",
      "WRITE",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4b1c.md#insn-00bd4b30) · [`00bd4b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4b1c.md#insn-00bd4b44) · [`00bd4b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4b1c.md#insn-00bd4b4c)
- 新版 `00bd4f58`（命令位置の公開資料なし） · `00bd4f6c`（命令位置の公開資料なし）

~~~diff
- 00bd4b30 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd4b30 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd4f58 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd4f58 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd4b30 bytes 080100b5
+ 00bd4f58 bytes 080100b5
- 00bd4b44 ["INT_ADD", "register:40f0:8", ["const:bd4b44:8", "const:4:8"]]
- 00bd4b44 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd4f6c ["INT_ADD", "register:40f0:8", ["const:bd4f6c:8", "const:4:8"]]
+ 00bd4f6c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd4b44 bytes f3170294
+ 00bd4f6c bytes e9170294
- 00bd4b4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00bd4b4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd4b4c bytes 602603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8cf2ee6bf41344146d4cd9fb1b37d6c"></a>

### [`00bd4b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4b6c.md) → [`00bd4f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4f94.md) _ZN8firebase4auth10credential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bd4fec",
      "incomplete_value": true,
      "site": "00bd4fec",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4bc4",
      "incomplete_value": true,
      "site": "00bd4bc4",
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
            "const:650:8"
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
      "definition_site": "00bd4fc8",
      "incomplete_value": true,
      "site": "00bd4fd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4ba0",
      "incomplete_value": true,
      "site": "00bd4bac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:648:8"
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
      "00bd4fa8",
      "READ",
      [
        "storage",
        "01126650",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd4fc8",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4fec",
      "WRITE",
      [
        "storage",
        "01126650",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd4fa8",
      "READ",
      [
        "storage",
        "01126a50",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd4fc8",
      "READ",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4fec",
      "WRITE",
      [
        "storage",
        "01126a50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4b6c.md#insn-00bd4bac) · [`00bd4bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4b6c.md#insn-00bd4bc4) · [`00bd4b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4b6c.md#insn-00bd4b80)
- 新版 `00bd4fd4`（命令位置の公開資料なし） · `00bd4fec`（命令位置の公開資料なし） · `00bd4fa8`（命令位置の公開資料なし）

~~~diff
- 00bd4bac ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4bac ["INT_ADD", "register:40f0:8", ["const:bd4bac:8", "const:4:8"]]
- 00bd4bac ["CALLIND", null, ["register:0:8"]]
+ 00bd4fd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4fd4 ["INT_ADD", "register:40f0:8", ["const:bd4fd4:8", "const:4:8"]]
+ 00bd4fd4 ["CALLIND", null, ["register:0:8"]]
- 00bd4bac bytes 00013fd6
+ 00bd4fd4 bytes 00013fd6
- 00bd4bc4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd4bc4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:650:8"]]
- 00bd4bc4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd4fec ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd4fec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a50:8"]]
+ 00bd4fec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd4bc4 bytes a0421939
+ 00bd4fec bytes a0422939
- 00bd4b80 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:650:8"]]
- 00bd4b80 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd4b80 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd4fa8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a50:8"]]
+ 00bd4fa8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd4fa8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd4b80 bytes a8425939
+ 00bd4fa8 bytes a8426939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7963993373e790bf0f6a97f51fd4c9d1"></a>

### [`00bd4bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4bd8.md) → [`00bd5000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5000.md) _ZN8firebase4auth10credential12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 16.67% / 新版 14.29%

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
      "site": "00bd4c14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4c34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd503c"
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
      "00bd5014",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5018",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd4c38"
      ]
    ],
    [
      "00bd5020",
      "READ",
      [
        "storage",
        "01126650",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd5014",
      "READ",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5018",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5060"
      ]
    ],
    [
      "00bd5020",
      "READ",
      [
        "storage",
        "01126a50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4bd8.md#insn-00bd4c14) · [`00bd4c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4bd8.md#insn-00bd4c1c) · [`00bd4c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4bd8.md#insn-00bd4c30)

~~~diff
- 00bd4c14 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd4c14 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd4c14 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:650:8"]]
- 00bd4c14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd4c14 bytes bf421939
- 00bd4c1c ["INT_ADD", "register:40f0:8", ["const:bd4c1c:8", "const:4:8"]]
- 00bd4c1c ["CALL", null, ["callee:00c5af60:8"]]
- 00bd4c1c bytes d1170294
- 00bd4c30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4c30 ["INT_ADD", "register:40f0:8", ["const:bd4c30:8", "const:4:8"]]
- 00bd4c30 ["CALLIND", null, ["register:0:8"]]
- 00bd4c30 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80661b4b764600b860aac33f2ace1ac1"></a>

### [`00bd4c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4c48.md) → [`00bd5070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5070.md) _ZN8firebase4auth10credential14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bd4c88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd50b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4c64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd4c5c",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd4c64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd50b4"
      ]
    ],
    [
      "unmatched:00bd4c6c",
      "PARAM",
      [
        "storage",
        "002b9cdc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd5084",
      "READ",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd508c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd50b4"
      ]
    ],
    [
      "00bd5094",
      "PARAM",
      [
        "storage",
        "002b9d1c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4c48.md#insn-00bd4c64) · [`00bd4c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4c48.md#insn-00bd4c80) · [`00bd4c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4c48.md#insn-00bd4c88)
- 新版 `00bd50a8`（命令位置の公開資料なし）

~~~diff
- 00bd4c64 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd4c64 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd4c64 bytes 410100b5
- 00bd4c80 ["INT_ADD", "register:40f0:8", ["const:bd4c80:8", "const:4:8"]]
- 00bd4c80 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd50a8 ["INT_ADD", "register:40f0:8", ["const:bd50a8:8", "const:4:8"]]
+ 00bd50a8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd4c80 bytes a4170294
+ 00bd50a8 bytes 9a170294
- 00bd4c88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
- 00bd4c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd4c88 bytes 802603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c42a0214ade6bd28895b1e293b3e307d"></a>

### [`00bd4cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4cb8.md) → [`00bd50e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd50e0.md) _ZN8firebase4auth10credential11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd50fc",
      "incomplete_value": false,
      "site": "00bd5100",
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
      "definition_site": "00bd4cd4",
      "incomplete_value": false,
      "site": "00bd4cd8",
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
      "definition_site": "00bd510c",
      "incomplete_value": true,
      "site": "00bd5118",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd4ce4",
      "incomplete_value": true,
      "site": "00bd4cf0",
      "value": [
        "LOAD",
        "8",
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
      "00bd50fc",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd510c",
      "DATA",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd50fc",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd510c",
      "DATA",
      [
        "storage",
        "01126a58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4cb8.md#insn-00bd4cd8) · [`00bd4cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4cb8.md#insn-00bd4cd4) · [`00bd4ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4cb8.md#insn-00bd4ce0)
- 新版 `00bd5100`（命令位置の公開資料なし） · `00bd50fc`（命令位置の公開資料なし） · `00bd5108`（命令位置の公開資料なし）

~~~diff
- 00bd4cd8 ["INT_ADD", "register:40f0:8", ["const:bd4cd8:8", "const:4:8"]]
- 00bd4cd8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd5100 ["INT_ADD", "register:40f0:8", ["const:bd5100:8", "const:4:8"]]
+ 00bd5100 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd4cd8 bytes ca170294
+ 00bd5100 bytes c0170294
- 00bd4cd4 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd4cd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd4cd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd4cd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd50fc ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd50fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd50fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd50fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd4cd4 bytes 00680a91
+ 00bd50fc bytes 009c0d91
- 00bd4ce0 ["COPY", "tmp:0:8", ["const:658:8"]]
- 00bd4ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd4ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd4ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd5108 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 00bd5108 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd5108 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd5108 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd4ce0 bytes 08611991
+ 00bd5108 bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ef129a781e3f356a764cea9400d2cdf"></a>

### [`00bd4cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4cf4.md) → [`00bd511c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd511c.md) _ZN8firebase4auth10credential13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd515c",
      "incomplete_value": true,
      "site": "00bd515c",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4d34",
      "incomplete_value": true,
      "site": "00bd4d34",
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
            "const:648:8"
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
      "definition_site": "00bd5138",
      "incomplete_value": true,
      "site": "00bd5138",
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
      "definition_site": "00bd4d10",
      "incomplete_value": true,
      "site": "00bd4d10",
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
      "definition_site": "00bd5140",
      "incomplete_value": false,
      "site": "00bd5154",
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
            "const:d1c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4d18",
      "incomplete_value": false,
      "site": "00bd4d2c",
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
            "const:cdc:8"
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
      "00bd5130",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5140",
      "PARAM",
      [
        "storage",
        "002b9cdc",
        null,
        "string"
      ]
    ],
    [
      "00bd515c",
      "WRITE",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5130",
      "READ",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5140",
      "PARAM",
      [
        "storage",
        "002b9d1c",
        null,
        "string"
      ]
    ],
    [
      "00bd515c",
      "WRITE",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4cf4.md#insn-00bd4d2c) · [`00bd4d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4cf4.md#insn-00bd4d34) · [`00bd4d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4cf4.md#insn-00bd4d08)
- 新版 `00bd5154`（命令位置の公開資料なし） · `00bd515c`（命令位置の公開資料なし） · `00bd5130`（命令位置の公開資料なし）

~~~diff
- 00bd4d2c ["INT_ADD", "register:40f0:8", ["const:bd4d2c:8", "const:4:8"]]
- 00bd4d2c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd5154 ["INT_ADD", "register:40f0:8", ["const:bd5154:8", "const:4:8"]]
+ 00bd5154 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd4d2c bytes 79170294
+ 00bd5154 bytes 6f170294
- 00bd4d34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
- 00bd4d34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd515c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
+ 00bd515c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd4d34 bytes 802603f9
+ 00bd515c bytes 802605f9
- 00bd4d08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
- 00bd4d08 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd5130 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
+ 00bd5130 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd4d08 bytes 812643f9
+ 00bd5130 bytes 812645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4985b4dbdec58983fb85ff3852bd5e15"></a>

### [`00bd4d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4d64.md) → [`00bd518c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd518c.md) _ZN8firebase4auth10credential10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd51a8",
      "incomplete_value": false,
      "site": "00bd51ac",
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
      "definition_site": "00bd4d80",
      "incomplete_value": false,
      "site": "00bd4d84",
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
      "definition_site": "00bd51b8",
      "incomplete_value": true,
      "site": "00bd51c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd4d90",
      "incomplete_value": true,
      "site": "00bd4d9c",
      "value": [
        "LOAD",
        "8",
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
      "00bd51a8",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd51b8",
      "DATA",
      [
        "storage",
        "01126660",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd51a8",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd51b8",
      "DATA",
      [
        "storage",
        "01126a60",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4d64.md#insn-00bd4d84) · [`00bd4d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4d64.md#insn-00bd4d80) · [`00bd4d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4d64.md#insn-00bd4d8c)
- 新版 `00bd51ac`（命令位置の公開資料なし） · `00bd51a8`（命令位置の公開資料なし） · `00bd51b4`（命令位置の公開資料なし）

~~~diff
- 00bd4d84 ["INT_ADD", "register:40f0:8", ["const:bd4d84:8", "const:4:8"]]
- 00bd4d84 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd51ac ["INT_ADD", "register:40f0:8", ["const:bd51ac:8", "const:4:8"]]
+ 00bd51ac ["CALL", null, ["callee:00c5b000:8"]]
- 00bd4d84 bytes 9f170294
+ 00bd51ac bytes 95170294
- 00bd4d80 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd4d80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd4d80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd4d80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd51a8 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd51a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd51a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd51a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd4d80 bytes 00441191
+ 00bd51a8 bytes 00781491
- 00bd4d8c ["COPY", "tmp:0:8", ["const:660:8"]]
- 00bd4d8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd4d8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd4d8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd51b4 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 00bd51b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd51b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd51b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd4d8c bytes 08811991
+ 00bd51b4 bytes 08812991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-384d017513145e1ef05ec564c4364207"></a>

### [`00bd4da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4da0.md) → [`00bd51c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd51c8.md) _ZN8firebase4auth9emailcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_

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
      "definition_site": "00bd51f4",
      "incomplete_value": true,
      "site": "00bd51f4",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4dcc",
      "incomplete_value": true,
      "site": "00bd4dcc",
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
            "const:668:8"
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
      "definition_site": "00bd51dc",
      "incomplete_value": true,
      "site": "00bd51dc",
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
      "definition_site": "00bd4db4",
      "incomplete_value": true,
      "site": "00bd4db4",
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
      "definition_site": "00bd51e8",
      "incomplete_value": false,
      "site": "00bd51ec",
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
            "const:3f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4dc0",
      "incomplete_value": false,
      "site": "00bd4dc4",
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
            "const:3b3:8"
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
      "00bd51d8",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd51e8",
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ],
    [
      "00bd51f4",
      "WRITE",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd51d8",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd51e8",
      "PARAM",
      [
        "storage",
        "002ac3f3",
        null,
        "string"
      ]
    ],
    [
      "00bd51f4",
      "WRITE",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4da0.md#insn-00bd4dc4) · [`00bd4dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4da0.md#insn-00bd4dcc) · [`00bd4db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4da0.md#insn-00bd4db0)
- 新版 `00bd51ec`（命令位置の公開資料なし） · `00bd51f4`（命令位置の公開資料なし） · `00bd51d8`（命令位置の公開資料なし）

~~~diff
- 00bd4dc4 ["INT_ADD", "register:40f0:8", ["const:bd4dc4:8", "const:4:8"]]
- 00bd4dc4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd51ec ["INT_ADD", "register:40f0:8", ["const:bd51ec:8", "const:4:8"]]
+ 00bd51ec ["CALL", null, ["callee:00c5af10:8"]]
- 00bd4dc4 bytes 53170294
+ 00bd51ec bytes 49170294
- 00bd4dcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00bd4dcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd51f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00bd51f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd4dcc bytes 603603f9
+ 00bd51f4 bytes 603605f9
- 00bd4db0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00bd4db0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd51d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00bd51d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd4db0 bytes 683643f9
+ 00bd51d8 bytes 683645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-946ccc7143227fb9771adccb03d7b0d6"></a>

### [`00bd4de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4de0.md) → [`00bd5208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5208.md) _ZN8firebase4auth9emailcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00bd4e0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5234"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd521c",
      "incomplete_value": true,
      "site": "00bd521c",
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
      "definition_site": "00bd4df4",
      "incomplete_value": true,
      "site": "00bd4df4",
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
      "00bd5218",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd4dfc",
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd4e04",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bd5218",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5224",
      "PARAM",
      [
        "storage",
        "002ac3f3",
        null,
        "string"
      ]
    ],
    [
      "00bd522c",
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

- 旧版 [`00bd4df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4de0.md#insn-00bd4df4) · [`00bd4e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4de0.md#insn-00bd4e04) · [`00bd4e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4de0.md#insn-00bd4e0c)
- 新版 `00bd521c`（命令位置の公開資料なし）

~~~diff
- 00bd4df4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd4df4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd521c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd521c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd4df4 bytes e80000b5
+ 00bd521c bytes e80000b5
- 00bd4e04 ["INT_ADD", "register:40f0:8", ["const:bd4e04:8", "const:4:8"]]
- 00bd4e04 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd4e04 bytes 43170294
- 00bd4e0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00bd4e0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd4e0c bytes 603603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3141133c9318f000286a1e4dd61503e0"></a>

### [`00bd4e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4e64.md) → [`00bd528c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd528c.md) _ZN8firebase4auth9emailcred10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00bd4e94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd52bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd52a0",
      "incomplete_value": true,
      "site": "00bd52a0",
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
      "definition_site": "00bd4e78",
      "incomplete_value": true,
      "site": "00bd4e78",
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
      "00bd529c",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd52a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd4e98"
      ]
    ],
    [
      "unmatched:00bd4e80",
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd529c",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd52a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd52c0"
      ]
    ],
    [
      "00bd52a8",
      "PARAM",
      [
        "storage",
        "002ac3f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4e64.md#insn-00bd4e78) · [`00bd4e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4e64.md#insn-00bd4e8c) · [`00bd4e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4e64.md#insn-00bd4e94)
- 新版 `00bd52a0`（命令位置の公開資料なし） · `00bd52b4`（命令位置の公開資料なし）

~~~diff
- 00bd4e78 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd4e78 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd52a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd52a0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd4e78 bytes 080100b5
+ 00bd52a0 bytes 080100b5
- 00bd4e8c ["INT_ADD", "register:40f0:8", ["const:bd4e8c:8", "const:4:8"]]
- 00bd4e8c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd52b4 ["INT_ADD", "register:40f0:8", ["const:bd52b4:8", "const:4:8"]]
+ 00bd52b4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd4e8c bytes 21170294
+ 00bd52b4 bytes 17170294
- 00bd4e94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00bd4e94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd4e94 bytes 603603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e81ce8aceacc16baf6b1c7fda9f94b6"></a>

### [`00bd4eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4eb4.md) → [`00bd52dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd52dc.md) _ZN8firebase4auth9emailcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5334"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd5310",
      "incomplete_value": true,
      "site": "00bd531c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4ee8",
      "incomplete_value": true,
      "site": "00bd4ef4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:668:8"
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
      "00bd52f0",
      "READ",
      [
        "storage",
        "01126670",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd52fc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd4f10"
      ]
    ],
    [
      "unmatched:00bd4ee8",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd52f0",
      "READ",
      [
        "storage",
        "01126a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd52fc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5338"
      ]
    ],
    [
      "00bd5310",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4eb4.md#insn-00bd4ef4) · [`00bd4f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4eb4.md#insn-00bd4f0c) · [`00bd4f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4eb4.md#insn-00bd4f1c)
- 新版 `00bd531c`（命令位置の公開資料なし）

~~~diff
- 00bd4ef4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4ef4 ["INT_ADD", "register:40f0:8", ["const:bd4ef4:8", "const:4:8"]]
- 00bd4ef4 ["CALLIND", null, ["register:0:8"]]
+ 00bd531c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd531c ["INT_ADD", "register:40f0:8", ["const:bd531c:8", "const:4:8"]]
+ 00bd531c ["CALLIND", null, ["register:0:8"]]
- 00bd4ef4 bytes 00013fd6
+ 00bd531c bytes 00013fd6
- 00bd4f0c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd4f0c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:670:8"]]
- 00bd4f0c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd4f0c bytes a0c21939
- 00bd4f1c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd4f1c ["RETURN", null, ["register:0:8"]]
- 00bd4f1c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0394882fb8a4a4c1e8f6fb3e370cc323"></a>

### [`00bd4f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4f20.md) → [`00bd5348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5348.md) _ZN8firebase4auth9emailcred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 16.67% / 新版 14.29%

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
      "site": "00bd4f5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4f7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5384"
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
      "00bd535c",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5360",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd4f80"
      ]
    ],
    [
      "00bd5368",
      "READ",
      [
        "storage",
        "01126670",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd535c",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5360",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd53a8"
      ]
    ],
    [
      "00bd5368",
      "READ",
      [
        "storage",
        "01126a70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4f20.md#insn-00bd4f5c) · [`00bd4f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4f20.md#insn-00bd4f64) · [`00bd4f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4f20.md#insn-00bd4f78)

~~~diff
- 00bd4f5c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd4f5c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd4f5c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:670:8"]]
- 00bd4f5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd4f5c bytes bfc21939
- 00bd4f64 ["INT_ADD", "register:40f0:8", ["const:bd4f64:8", "const:4:8"]]
- 00bd4f64 ["CALL", null, ["callee:00c5af60:8"]]
- 00bd4f64 bytes ff160294
- 00bd4f78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4f78 ["INT_ADD", "register:40f0:8", ["const:bd4f78:8", "const:4:8"]]
- 00bd4f78 ["CALLIND", null, ["register:0:8"]]
- 00bd4f78 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b38c44ce94bda9a516faef473e8cc00a"></a>

### [`00bd4f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4f90.md) → [`00bd53b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd53b8.md) _ZN8firebase4auth9emailcred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bd4fd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd53f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4fac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd4fa4",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd4fac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd53fc"
      ]
    ],
    [
      "unmatched:00bd4fb4",
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd53cc",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd53d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd53fc"
      ]
    ],
    [
      "00bd53dc",
      "PARAM",
      [
        "storage",
        "002ac3f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4f90.md#insn-00bd4fac) · [`00bd4fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4f90.md#insn-00bd4fc8) · [`00bd4fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4f90.md#insn-00bd4fd0)
- 新版 `00bd53f0`（命令位置の公開資料なし）

~~~diff
- 00bd4fac ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd4fac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd4fac bytes 410100b5
- 00bd4fc8 ["INT_ADD", "register:40f0:8", ["const:bd4fc8:8", "const:4:8"]]
- 00bd4fc8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd53f0 ["INT_ADD", "register:40f0:8", ["const:bd53f0:8", "const:4:8"]]
+ 00bd53f0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd4fc8 bytes d2160294
+ 00bd53f0 bytes c8160294
- 00bd4fd0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
- 00bd4fd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd4fd0 bytes 803603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fe0842896eb920d74a97f60ea599218"></a>

### [`00bd503c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd503c.md) → [`00bd5464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5464.md) _ZN8firebase4auth9emailcred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bd507c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd54a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5058"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5050",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd5058",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd54a8"
      ]
    ],
    [
      "unmatched:00bd5060",
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd5478",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5480",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd54a8"
      ]
    ],
    [
      "00bd5488",
      "PARAM",
      [
        "storage",
        "002ac3f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd503c.md#insn-00bd5058) · [`00bd5074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd503c.md#insn-00bd5074) · [`00bd507c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd503c.md#insn-00bd507c)
- 新版 `00bd549c`（命令位置の公開資料なし）

~~~diff
- 00bd5058 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd5058 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd5058 bytes 410100b5
- 00bd5074 ["INT_ADD", "register:40f0:8", ["const:bd5074:8", "const:4:8"]]
- 00bd5074 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd549c ["INT_ADD", "register:40f0:8", ["const:bd549c:8", "const:4:8"]]
+ 00bd549c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5074 bytes a7160294
+ 00bd549c bytes 9d160294
- 00bd507c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
- 00bd507c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd507c bytes 803603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac4de190cd6d449692d02be5ff3f52e0"></a>

### [`00bd50e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd50e8.md) → [`00bd5510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5510.md) _ZN8firebase4auth12facebookcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "definition_site": "00bd553c",
      "incomplete_value": true,
      "site": "00bd553c",
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
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5114",
      "incomplete_value": true,
      "site": "00bd5114",
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
            "const:688:8"
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
      "definition_site": "00bd5524",
      "incomplete_value": true,
      "site": "00bd5524",
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
      "definition_site": "00bd50fc",
      "incomplete_value": true,
      "site": "00bd50fc",
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
      "definition_site": "00bd5530",
      "incomplete_value": false,
      "site": "00bd5534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:499:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5108",
      "incomplete_value": false,
      "site": "00bd510c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:459:8"
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
      "00bd5520",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5530",
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ],
    [
      "00bd553c",
      "WRITE",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5520",
      "READ",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5530",
      "PARAM",
      [
        "storage",
        "002bd499",
        null,
        "string"
      ]
    ],
    [
      "00bd553c",
      "WRITE",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd510c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd50e8.md#insn-00bd510c) · [`00bd5114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd50e8.md#insn-00bd5114) · [`00bd50f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd50e8.md#insn-00bd50f8)
- 新版 `00bd5534`（命令位置の公開資料なし） · `00bd553c`（命令位置の公開資料なし） · `00bd5520`（命令位置の公開資料なし）

~~~diff
- 00bd510c ["INT_ADD", "register:40f0:8", ["const:bd510c:8", "const:4:8"]]
- 00bd510c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd5534 ["INT_ADD", "register:40f0:8", ["const:bd5534:8", "const:4:8"]]
+ 00bd5534 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd510c bytes 81160294
+ 00bd5534 bytes 77160294
- 00bd5114 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:688:8"]]
- 00bd5114 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd553c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
+ 00bd553c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5114 bytes 604603f9
+ 00bd553c bytes 604605f9
- 00bd50f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:688:8"]]
- 00bd50f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd5520 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
+ 00bd5520 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd50f8 bytes 684643f9
+ 00bd5520 bytes 684645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11dee1232bd59e92242f09fc47f7c262"></a>

### [`00bd51ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51ac.md) → [`00bd55d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd55d4.md) _ZN8firebase4auth12facebookcred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd51ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd51b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd51b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd51ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd51b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd55e4",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd55d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd55d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd55e4",
      "READ",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd51ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51ac.md#insn-00bd51ac) · [`00bd51b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51ac.md#insn-00bd51b0) · [`00bd51c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51ac.md#insn-00bd51c0)
- 新版 `00bd55e8`（命令位置の公開資料なし）

~~~diff
- 00bd51ac ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd51ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd51ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd51ac bytes f30f1ef8
- 00bd51b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd51b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd51b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd51b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd51b0 bytes fd7b01a9
- 00bd51c0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd51c0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd55e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd55e8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd51c0 bytes 080100b5
+ 00bd55e8 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad8edc25c7404cdc4a6aa29f4844c7cf"></a>

### [`00bd51fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51fc.md) → [`00bd5624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5624.md) _ZN8firebase4auth12facebookcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 40.00% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd51fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5200"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5200"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd51fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5200",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5204",
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
      "00bd5624",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd5628",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd562c",
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

- 旧版 [`00bd51fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51fc.md#insn-00bd51fc) · [`00bd5200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51fc.md#insn-00bd5200) · [`00bd5204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51fc.md#insn-00bd5204)

~~~diff
- 00bd51fc ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd51fc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd51fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd51fc bytes f50f1df8
- 00bd5200 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd5200 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd5200 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd5200 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5200 bytes f44f01a9
- 00bd5204 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd5204 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd5204 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd5204 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5204 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79e4b05046f9ed76b445634a3c98ecb6"></a>

### [`00bd5268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5268.md) → [`00bd5690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5690.md) _ZN8firebase4auth12facebookcred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00bd52a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd52c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd56cc"
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
      "00bd56a4",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd56a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd52c8"
      ]
    ],
    [
      "00bd56b0",
      "READ",
      [
        "storage",
        "01126690",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd56a4",
      "READ",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd56a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd56f0"
      ]
    ],
    [
      "00bd56b0",
      "READ",
      [
        "storage",
        "01126a90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5268.md#insn-00bd5280) · [`00bd52a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5268.md#insn-00bd52a4) · [`00bd52ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5268.md#insn-00bd52ac)
- 新版 `00bd56a8`（命令位置の公開資料なし）

~~~diff
- 00bd5280 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd5280 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd56a8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd56a8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd5280 bytes 410200b4
+ 00bd56a8 bytes 410200b4
- 00bd52a4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd52a4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd52a4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:690:8"]]
- 00bd52a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd52a4 bytes bf421a39
- 00bd52ac ["INT_ADD", "register:40f0:8", ["const:bd52ac:8", "const:4:8"]]
- 00bd52ac ["CALL", null, ["callee:00c5af60:8"]]
- 00bd52ac bytes 2d160294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8607645cc06f1b4c19f868081331a98d"></a>

### [`00bd52d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd52d8.md) → [`00bd5700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5700.md) _ZN8firebase4auth12facebookcred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bd5318"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5740"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd52f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd52ec",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd52f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5744"
      ]
    ],
    [
      "unmatched:00bd52fc",
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd5714",
      "READ",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd571c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5744"
      ]
    ],
    [
      "00bd5724",
      "PARAM",
      [
        "storage",
        "002bd499",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd52f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd52d8.md#insn-00bd52f4) · [`00bd5310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd52d8.md#insn-00bd5310) · [`00bd5318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd52d8.md#insn-00bd5318)
- 新版 `00bd5738`（命令位置の公開資料なし）

~~~diff
- 00bd52f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd52f4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd52f4 bytes 410100b5
- 00bd5310 ["INT_ADD", "register:40f0:8", ["const:bd5310:8", "const:4:8"]]
- 00bd5310 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd5738 ["INT_ADD", "register:40f0:8", ["const:bd5738:8", "const:4:8"]]
+ 00bd5738 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5310 bytes 00160294
+ 00bd5738 bytes f6150294
- 00bd5318 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:688:8"]]
- 00bd5318 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5318 bytes 804603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24dc7e6b26d2606e62039322673d364c"></a>

### [`00bd5384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5384.md) → [`00bd57ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd57ac.md) _ZN8firebase4auth12facebookcred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd53c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd57ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd53a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5398",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd53a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd57f0"
      ]
    ],
    [
      "unmatched:00bd53a8",
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd57c0",
      "READ",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd57c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd57f0"
      ]
    ],
    [
      "00bd57d0",
      "PARAM",
      [
        "storage",
        "002bd499",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd53a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5384.md#insn-00bd53a0) · [`00bd53bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5384.md#insn-00bd53bc) · [`00bd53c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5384.md#insn-00bd53c4)
- 新版 `00bd57e4`（命令位置の公開資料なし）

~~~diff
- 00bd53a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd53a0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd53a0 bytes 410100b5
- 00bd53bc ["INT_ADD", "register:40f0:8", ["const:bd53bc:8", "const:4:8"]]
- 00bd53bc ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd57e4 ["INT_ADD", "register:40f0:8", ["const:bd57e4:8", "const:4:8"]]
+ 00bd57e4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd53bc bytes d5150294
+ 00bd57e4 bytes cb150294
- 00bd53c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:688:8"]]
- 00bd53c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd53c4 bytes 804603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3305b7ee4348833e6080761a2f4e80cb"></a>

### [`00bd5470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5470.md) → [`00bd5898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5898.md) _ZN8firebase4auth10githubcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

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
      "site": "00bd549c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd58c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd58ac",
      "incomplete_value": true,
      "site": "00bd58ac",
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
      "definition_site": "00bd5484",
      "incomplete_value": true,
      "site": "00bd5484",
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
      "00bd58a8",
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd548c",
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd5494",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bd58a8",
      "READ",
      [
        "storage",
        "01126aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd58b4",
      "PARAM",
      [
        "storage",
        "002c1de2",
        null,
        "string"
      ]
    ],
    [
      "00bd58bc",
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

- 旧版 [`00bd5484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5470.md#insn-00bd5484) · [`00bd5494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5470.md#insn-00bd5494) · [`00bd549c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5470.md#insn-00bd549c)
- 新版 `00bd58ac`（命令位置の公開資料なし）

~~~diff
- 00bd5484 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd5484 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd58ac ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd58ac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd5484 bytes e80000b5
+ 00bd58ac bytes e80000b5
- 00bd5494 ["INT_ADD", "register:40f0:8", ["const:bd5494:8", "const:4:8"]]
- 00bd5494 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5494 bytes 9f150294
- 00bd549c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00bd549c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd549c bytes 605603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2da121d96066131a52b0218ebc8174ff"></a>

### [`00bd54f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd54f4.md) → [`00bd591c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd591c.md) _ZN8firebase4auth10githubcred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5524"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd594c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd5930",
      "incomplete_value": true,
      "site": "00bd5930",
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
      "definition_site": "00bd5508",
      "incomplete_value": true,
      "site": "00bd5508",
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
      "00bd592c",
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5930",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd5528"
      ]
    ],
    [
      "unmatched:00bd5510",
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd592c",
      "READ",
      [
        "storage",
        "01126aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5930",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5950"
      ]
    ],
    [
      "00bd5938",
      "PARAM",
      [
        "storage",
        "002c1de2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd54f4.md#insn-00bd5508) · [`00bd551c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd54f4.md#insn-00bd551c) · [`00bd5524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd54f4.md#insn-00bd5524)
- 新版 `00bd5930`（命令位置の公開資料なし） · `00bd5944`（命令位置の公開資料なし）

~~~diff
- 00bd5508 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd5508 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd5930 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd5930 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd5508 bytes 080100b5
+ 00bd5930 bytes 080100b5
- 00bd551c ["INT_ADD", "register:40f0:8", ["const:bd551c:8", "const:4:8"]]
- 00bd551c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd5944 ["INT_ADD", "register:40f0:8", ["const:bd5944:8", "const:4:8"]]
+ 00bd5944 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd551c bytes 7d150294
+ 00bd5944 bytes 73150294
- 00bd5524 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00bd5524 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5524 bytes 605603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e62c871725499f059ce4163440e91c6"></a>

### [`00bd55b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd55b0.md) → [`00bd59d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd59d8.md) _ZN8firebase4auth10githubcred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 14.29% / 新版 14.29%

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
      "site": "00bd55ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd560c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5a14"
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
      "00bd59ec",
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd59f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd5610"
      ]
    ],
    [
      "00bd59f8",
      "READ",
      [
        "storage",
        "011266b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd59ec",
      "READ",
      [
        "storage",
        "01126aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd59f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5a38"
      ]
    ],
    [
      "00bd59f8",
      "READ",
      [
        "storage",
        "01126ab0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd55c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd55b0.md#insn-00bd55c8) · [`00bd55ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd55b0.md#insn-00bd55ec) · [`00bd55f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd55b0.md#insn-00bd55f4)
- 新版 `00bd59f0`（命令位置の公開資料なし）

~~~diff
- 00bd55c8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd55c8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd59f0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd59f0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd55c8 bytes 410200b4
+ 00bd59f0 bytes 410200b4
- 00bd55ec ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd55ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd55ec ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6b0:8"]]
- 00bd55ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd55ec bytes bfc21a39
- 00bd55f4 ["INT_ADD", "register:40f0:8", ["const:bd55f4:8", "const:4:8"]]
- 00bd55f4 ["CALL", null, ["callee:00c5af60:8"]]
- 00bd55f4 bytes 5b150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a1c448bacf1882c5736ac70c8f6e1d2"></a>

### [`00bd5620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5620.md) → [`00bd5a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5a48.md) _ZN8firebase4auth10githubcred14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd5620"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5620"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5624"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5620",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5624",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5634",
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5a48",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5a4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5a5c",
      "READ",
      [
        "storage",
        "01126aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5620.md#insn-00bd5620) · [`00bd5624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5620.md#insn-00bd5624) · [`00bd563c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5620.md#insn-00bd563c)

~~~diff
- 00bd5620 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd5620 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd5620 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd5620 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd5620 bytes f44fbea9
- 00bd5624 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd5624 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd5624 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd5624 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5624 bytes fd7b01a9
- 00bd563c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd563c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd563c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff181322b8fb28b799d3ee99bcbd72d3"></a>

### [`00bd56cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd56cc.md) → [`00bd5af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5af4.md) _ZN8firebase4auth10githubcred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bd56cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd56cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd56d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd56cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd56d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd56e0",
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5af4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5af8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5b08",
      "READ",
      [
        "storage",
        "01126aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd56cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd56cc.md#insn-00bd56cc) · [`00bd56d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd56cc.md#insn-00bd56d0) · [`00bd56e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd56cc.md#insn-00bd56e8)

~~~diff
- 00bd56cc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd56cc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd56cc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd56cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd56cc bytes f44fbea9
- 00bd56d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd56d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd56d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd56d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd56d0 bytes fd7b01a9
- 00bd56e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd56e8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd56e8 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2da75fde781eb80bd5224c129fd13c3e"></a>

### [`00bd5778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5778.md) → [`00bd5ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5ba0.md) _ZN8firebase4auth10googlecred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "site": "00bd57a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5bcc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd5bb4",
      "incomplete_value": true,
      "site": "00bd5bb4",
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
      "definition_site": "00bd578c",
      "incomplete_value": true,
      "site": "00bd578c",
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
      "00bd5bb0",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5bb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd57a8"
      ]
    ],
    [
      "unmatched:00bd5798",
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd5bb0",
      "READ",
      [
        "storage",
        "01126ac8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5bb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5bd0"
      ]
    ],
    [
      "00bd5bc0",
      "PARAM",
      [
        "storage",
        "002c1e12",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd578c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5778.md#insn-00bd578c) · [`00bd579c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5778.md#insn-00bd579c) · [`00bd57a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5778.md#insn-00bd57a4)
- 新版 `00bd5bb4`（命令位置の公開資料なし）

~~~diff
- 00bd578c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd578c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd5bb4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd5bb4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd578c bytes e80000b5
+ 00bd5bb4 bytes e80000b5
- 00bd579c ["INT_ADD", "register:40f0:8", ["const:bd579c:8", "const:4:8"]]
- 00bd579c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd579c bytes dd140294
- 00bd57a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c8:8"]]
- 00bd57a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd57a4 bytes 606603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6a84f39f51b50ac643f93ec0954f691"></a>

### [`00bd57b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd57b8.md) → [`00bd5be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5be0.md) _ZN8firebase4auth10googlecred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

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
      "site": "00bd57e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5c0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd5bf4",
      "incomplete_value": true,
      "site": "00bd5bf4",
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
      "definition_site": "00bd57cc",
      "incomplete_value": true,
      "site": "00bd57cc",
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
      "00bd5bf0",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd57d4",
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd57dc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bd5bf0",
      "READ",
      [
        "storage",
        "01126ac8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5bfc",
      "PARAM",
      [
        "storage",
        "002c1e12",
        null,
        "string"
      ]
    ],
    [
      "00bd5c04",
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

- 旧版 [`00bd57cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd57b8.md#insn-00bd57cc) · [`00bd57dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd57b8.md#insn-00bd57dc) · [`00bd57e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd57b8.md#insn-00bd57e4)
- 新版 `00bd5bf4`（命令位置の公開資料なし）

~~~diff
- 00bd57cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd57cc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd5bf4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd5bf4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd57cc bytes e80000b5
+ 00bd5bf4 bytes e80000b5
- 00bd57dc ["INT_ADD", "register:40f0:8", ["const:bd57dc:8", "const:4:8"]]
- 00bd57dc ["CALL", null, ["callee:00c5af10:8"]]
- 00bd57dc bytes cd140294
- 00bd57e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c8:8"]]
- 00bd57e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd57e4 bytes 606603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-526ebe268f2a694ba9b4aab85c781c93"></a>

### [`00bd57f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd57f8.md) → [`00bd5c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5c20.md) _ZN8firebase4auth10googlecred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00bd57f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd57fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd57fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd57f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd57fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5c30",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5c20",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5c24",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5c30",
      "READ",
      [
        "storage",
        "01126ac8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd57f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd57f8.md#insn-00bd57f8) · [`00bd57fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd57f8.md#insn-00bd57fc) · [`00bd580c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd57f8.md#insn-00bd580c)
- 新版 `00bd5c34`（命令位置の公開資料なし）

~~~diff
- 00bd57f8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd57f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd57f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd57f8 bytes f30f1ef8
- 00bd57fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd57fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd57fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd57fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd57fc bytes fd7b01a9
- 00bd580c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd580c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd5c34 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd5c34 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd580c bytes 080100b5
+ 00bd5c34 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-254f1da7be6d2d56b3616f568332e9ef"></a>

### [`00bd583c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd583c.md) → [`00bd5c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5c64.md) _ZN8firebase4auth10googlecred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 23.53% / 新版 23.53%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd583c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5840"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5840"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd583c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5840",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd584c",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5c64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5c68",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5c74",
      "READ",
      [
        "storage",
        "01126ac8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd583c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd583c.md#insn-00bd583c) · [`00bd5840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd583c.md#insn-00bd5840) · [`00bd5850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd583c.md#insn-00bd5850)

~~~diff
- 00bd583c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd583c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd583c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd583c bytes f30f1ef8
- 00bd5840 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd5840 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd5840 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd5840 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5840 bytes fd7b01a9
- 00bd5850 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd5850 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd5850 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-178c7339092cddb83a834f8ec727eb81"></a>

### [`00bd588c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd588c.md) → [`00bd5cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5cb4.md) _ZN8firebase4auth10googlecred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd588c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5890"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5890"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd588c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5890",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5894",
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
      "00bd5cb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd5cb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5cbc",
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

- 旧版 [`00bd588c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd588c.md#insn-00bd588c) · [`00bd5890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd588c.md#insn-00bd5890) · [`00bd5894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd588c.md#insn-00bd5894)

~~~diff
- 00bd588c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd588c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd588c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd588c bytes f50f1df8
- 00bd5890 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd5890 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd5890 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd5890 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5890 bytes f44f01a9
- 00bd5894 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd5894 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd5894 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd5894 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5894 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93d2481961735b260cbe47a7374997a8"></a>

### [`00bd58f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd58f8.md) → [`00bd5d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5d20.md) _ZN8firebase4auth10googlecred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd58f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd58fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd58fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd58f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd58fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5900",
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
      "00bd5d20",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd5d24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5d28",
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

- 旧版 [`00bd58f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd58f8.md#insn-00bd58f8) · [`00bd58fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd58f8.md#insn-00bd58fc) · [`00bd5900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd58f8.md#insn-00bd5900)

~~~diff
- 00bd58f8 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd58f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd58f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd58f8 bytes f50f1df8
- 00bd58fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd58fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd58fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd58fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd58fc bytes f44f01a9
- 00bd5900 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd5900 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd5900 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd5900 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5900 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24b5a28e6e0ee2e3dfa66ca0c8cfb0ab"></a>

### [`00bd5968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5968.md) → [`00bd5d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5d90.md) _ZN8firebase4auth10googlecred14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00bd59a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5dd0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5984"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd597c",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd5984",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5dd4"
      ]
    ],
    [
      "unmatched:00bd598c",
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd5da4",
      "READ",
      [
        "storage",
        "01126ac8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5dac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5dd4"
      ]
    ],
    [
      "00bd5db4",
      "PARAM",
      [
        "storage",
        "002c1e12",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5968.md#insn-00bd5984) · [`00bd59a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5968.md#insn-00bd59a0) · [`00bd59a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5968.md#insn-00bd59a8)
- 新版 `00bd5dc8`（命令位置の公開資料なし）

~~~diff
- 00bd5984 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd5984 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd5984 bytes 410100b5
- 00bd59a0 ["INT_ADD", "register:40f0:8", ["const:bd59a0:8", "const:4:8"]]
- 00bd59a0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd5dc8 ["INT_ADD", "register:40f0:8", ["const:bd5dc8:8", "const:4:8"]]
+ 00bd5dc8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd59a0 bytes 5c140294
+ 00bd5dc8 bytes 52140294
- 00bd59a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c8:8"]]
- 00bd59a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd59a8 bytes 806603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea0a53e4637261f5a48690cd6a283b5b"></a>

### [`00bd5a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5a14.md) → [`00bd5e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5e3c.md) _ZN8firebase4auth10googlecred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bd5a54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5e7c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5a30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5a28",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd5a30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5e80"
      ]
    ],
    [
      "unmatched:00bd5a38",
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd5e50",
      "READ",
      [
        "storage",
        "01126ac8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5e58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5e80"
      ]
    ],
    [
      "00bd5e60",
      "PARAM",
      [
        "storage",
        "002c1e12",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5a14.md#insn-00bd5a30) · [`00bd5a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5a14.md#insn-00bd5a4c) · [`00bd5a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5a14.md#insn-00bd5a54)
- 新版 `00bd5e74`（命令位置の公開資料なし）

~~~diff
- 00bd5a30 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd5a30 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd5a30 bytes 410100b5
- 00bd5a4c ["INT_ADD", "register:40f0:8", ["const:bd5a4c:8", "const:4:8"]]
- 00bd5a4c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd5e74 ["INT_ADD", "register:40f0:8", ["const:bd5e74:8", "const:4:8"]]
+ 00bd5e74 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5a4c bytes 31140294
+ 00bd5e74 bytes 27140294
- 00bd5a54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c8:8"]]
- 00bd5a54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5a54 bytes 806603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8475bd8ee0c03e34449151ba6ef13d5"></a>

### [`00bd5a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5a84.md) → [`00bd5eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5eac.md) _ZN8firebase4auth10googlecred10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd5ec8",
      "incomplete_value": false,
      "site": "00bd5ecc",
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
      "definition_site": "00bd5aa0",
      "incomplete_value": false,
      "site": "00bd5aa4",
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
      "definition_site": "00bd5ed8",
      "incomplete_value": true,
      "site": "00bd5ee4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd5ab0",
      "incomplete_value": true,
      "site": "00bd5abc",
      "value": [
        "LOAD",
        "8",
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
      "00bd5ec8",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd5ed8",
      "DATA",
      [
        "storage",
        "011266e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd5ec8",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd5ed8",
      "DATA",
      [
        "storage",
        "01126ae0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5a84.md#insn-00bd5aa4) · [`00bd5aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5a84.md#insn-00bd5aa0) · [`00bd5aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5a84.md#insn-00bd5aac)
- 新版 `00bd5ecc`（命令位置の公開資料なし） · `00bd5ec8`（命令位置の公開資料なし） · `00bd5ed4`（命令位置の公開資料なし）

~~~diff
- 00bd5aa4 ["INT_ADD", "register:40f0:8", ["const:bd5aa4:8", "const:4:8"]]
- 00bd5aa4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd5ecc ["INT_ADD", "register:40f0:8", ["const:bd5ecc:8", "const:4:8"]]
+ 00bd5ecc ["CALL", null, ["callee:00c5b000:8"]]
- 00bd5aa4 bytes 57140294
+ 00bd5ecc bytes 4d140294
- 00bd5aa0 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd5aa0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd5aa0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd5aa0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd5ec8 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd5ec8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd5ec8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd5ec8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd5aa0 bytes 00441191
+ 00bd5ec8 bytes 00781491
- 00bd5aac ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00bd5aac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd5aac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd5aac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd5ed4 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 00bd5ed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd5ed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd5ed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd5aac bytes 08811b91
+ 00bd5ed4 bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c66ab96c0cc3345d6efe95e4bcb8d44f"></a>

### [`00bd5ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ac0.md) → [`00bd5ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5ee8.md) _ZN8firebase4auth13playgamescred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 31.25% / 新版 31.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5ac0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5ac4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5ac4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5ac0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5ac4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5ef8",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5ee8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5eec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5ef8",
      "READ",
      [
        "storage",
        "01126ae8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ac0.md#insn-00bd5ac0) · [`00bd5ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ac0.md#insn-00bd5ac4) · [`00bd5ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ac0.md#insn-00bd5ad4)
- 新版 `00bd5efc`（命令位置の公開資料なし）

~~~diff
- 00bd5ac0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd5ac0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd5ac0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd5ac0 bytes f30f1ef8
- 00bd5ac4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd5ac4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd5ac4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd5ac4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5ac4 bytes fd7b01a9
- 00bd5ad4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd5ad4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd5efc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd5efc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd5ad4 bytes e80000b5
+ 00bd5efc bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3c4954cea63c485401c934186818d51"></a>

### [`00bd5b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b00.md) → [`00bd5f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5f28.md) _ZN8firebase4auth13playgamescred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00bd5f54",
      "incomplete_value": true,
      "site": "00bd5f54",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5b2c",
      "incomplete_value": true,
      "site": "00bd5b2c",
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
            "const:6e8:8"
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
      "definition_site": "00bd5f3c",
      "incomplete_value": true,
      "site": "00bd5f3c",
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
      "definition_site": "00bd5b14",
      "incomplete_value": true,
      "site": "00bd5b14",
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
      "definition_site": "00bd5f44",
      "incomplete_value": false,
      "site": "00bd5f4c",
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
            "const:797:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5b1c",
      "incomplete_value": false,
      "site": "00bd5b24",
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
            "const:757:8"
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
      "00bd5f38",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5f44",
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      "00bd5f54",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5f38",
      "READ",
      [
        "storage",
        "01126ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5f44",
      "PARAM",
      [
        "storage",
        "002b3797",
        null,
        "string"
      ]
    ],
    [
      "00bd5f54",
      "WRITE",
      [
        "storage",
        "01126ae8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b00.md#insn-00bd5b24) · [`00bd5b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b00.md#insn-00bd5b2c) · [`00bd5b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b00.md#insn-00bd5b10)
- 新版 `00bd5f4c`（命令位置の公開資料なし） · `00bd5f54`（命令位置の公開資料なし） · `00bd5f38`（命令位置の公開資料なし）

~~~diff
- 00bd5b24 ["INT_ADD", "register:40f0:8", ["const:bd5b24:8", "const:4:8"]]
- 00bd5b24 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd5f4c ["INT_ADD", "register:40f0:8", ["const:bd5f4c:8", "const:4:8"]]
+ 00bd5f4c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5b24 bytes fb130294
+ 00bd5f4c bytes f1130294
- 00bd5b2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00bd5b2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5f54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00bd5f54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5b2c bytes 607603f9
+ 00bd5f54 bytes 607605f9
- 00bd5b10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00bd5b10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd5f38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00bd5f38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd5b10 bytes 687643f9
+ 00bd5f38 bytes 687645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a90636647d8821caaddfdef5f1152a4"></a>

### [`00bd5b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b40.md) → [`00bd5f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5f68.md) _ZN8firebase4auth13playgamescred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd5f98",
      "incomplete_value": true,
      "site": "00bd5f98",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5b70",
      "incomplete_value": true,
      "site": "00bd5b70",
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
            "const:6e8:8"
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
      "definition_site": "00bd5f7c",
      "incomplete_value": true,
      "site": "00bd5f7c",
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
      "definition_site": "00bd5b54",
      "incomplete_value": true,
      "site": "00bd5b54",
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
      "definition_site": "00bd5f88",
      "incomplete_value": false,
      "site": "00bd5f90",
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
            "const:797:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5b60",
      "incomplete_value": false,
      "site": "00bd5b68",
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
            "const:757:8"
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
      "00bd5f78",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5f88",
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      "00bd5f98",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5f78",
      "READ",
      [
        "storage",
        "01126ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5f88",
      "PARAM",
      [
        "storage",
        "002b3797",
        null,
        "string"
      ]
    ],
    [
      "00bd5f98",
      "WRITE",
      [
        "storage",
        "01126ae8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b40.md#insn-00bd5b68) · [`00bd5b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b40.md#insn-00bd5b70) · [`00bd5b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b40.md#insn-00bd5b50)
- 新版 `00bd5f90`（命令位置の公開資料なし） · `00bd5f98`（命令位置の公開資料なし） · `00bd5f78`（命令位置の公開資料なし）

~~~diff
- 00bd5b68 ["INT_ADD", "register:40f0:8", ["const:bd5b68:8", "const:4:8"]]
- 00bd5b68 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd5f90 ["INT_ADD", "register:40f0:8", ["const:bd5f90:8", "const:4:8"]]
+ 00bd5f90 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5b68 bytes ea130294
+ 00bd5f90 bytes e0130294
- 00bd5b70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00bd5b70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5f98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00bd5f98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5b70 bytes 607603f9
+ 00bd5f98 bytes 607605f9
- 00bd5b50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00bd5b50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd5f78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00bd5f78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd5b50 bytes 687643f9
+ 00bd5f78 bytes 687645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73b3cd083446b57473e03a2cffc81dbc"></a>

### [`00bd5b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b84.md) → [`00bd5fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5fac.md) _ZN8firebase4auth13playgamescred10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd5fdc",
      "incomplete_value": true,
      "site": "00bd5fdc",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5bb4",
      "incomplete_value": true,
      "site": "00bd5bb4",
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
            "const:6e8:8"
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
      "definition_site": "00bd5fc0",
      "incomplete_value": true,
      "site": "00bd5fc0",
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
      "definition_site": "00bd5b98",
      "incomplete_value": true,
      "site": "00bd5b98",
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
      "definition_site": "00bd5fc8",
      "incomplete_value": false,
      "site": "00bd5fd4",
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
            "const:797:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5ba0",
      "incomplete_value": false,
      "site": "00bd5bac",
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
            "const:757:8"
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
      "00bd5fbc",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5fc8",
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      "00bd5fdc",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5fbc",
      "READ",
      [
        "storage",
        "01126ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5fc8",
      "PARAM",
      [
        "storage",
        "002b3797",
        null,
        "string"
      ]
    ],
    [
      "00bd5fdc",
      "WRITE",
      [
        "storage",
        "01126ae8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b84.md#insn-00bd5bac) · [`00bd5bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b84.md#insn-00bd5bb4) · [`00bd5b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5b84.md#insn-00bd5b94)
- 新版 `00bd5fd4`（命令位置の公開資料なし） · `00bd5fdc`（命令位置の公開資料なし） · `00bd5fbc`（命令位置の公開資料なし）

~~~diff
- 00bd5bac ["INT_ADD", "register:40f0:8", ["const:bd5bac:8", "const:4:8"]]
- 00bd5bac ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd5fd4 ["INT_ADD", "register:40f0:8", ["const:bd5fd4:8", "const:4:8"]]
+ 00bd5fd4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5bac bytes d9130294
+ 00bd5fd4 bytes cf130294
- 00bd5bb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00bd5bb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5fdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00bd5fdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5bb4 bytes 607603f9
+ 00bd5fdc bytes 607605f9
- 00bd5b94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00bd5b94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd5fbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00bd5fbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd5b94 bytes 687643f9
+ 00bd5fbc bytes 687645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b1ebd9310a91e6b29b6f7639ed574c1"></a>

### [`00bd5bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5bd4.md) → [`00bd5ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5ffc.md) _ZN8firebase4auth13playgamescred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 62.96% / 新版 62.96%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5bd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5bd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5bd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5bd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5bd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5bdc",
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
      "00bd5ffc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd6000",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6004",
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

- 旧版 [`00bd5bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5bd4.md#insn-00bd5bd4) · [`00bd5bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5bd4.md#insn-00bd5bd8) · [`00bd5bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5bd4.md#insn-00bd5bdc)

~~~diff
- 00bd5bd4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd5bd4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd5bd4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd5bd4 bytes f50f1df8
- 00bd5bd8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd5bd8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd5bd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd5bd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5bd8 bytes f44f01a9
- 00bd5bdc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd5bdc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd5bdc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd5bdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5bdc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-932c8d124efb841027083f47df21f115"></a>

### [`00bd5c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5c40.md) → [`00bd6068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6068.md) _ZN8firebase4auth13playgamescred12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bd60a4",
      "incomplete_value": true,
      "site": "00bd60a4",
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
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5c7c",
      "incomplete_value": true,
      "site": "00bd5c7c",
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
            "const:6f0:8"
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
      "definition_site": "00bd60c4",
      "incomplete_value": true,
      "site": "00bd60c4",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5c9c",
      "incomplete_value": true,
      "site": "00bd5c9c",
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
            "const:6e8:8"
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
      "definition_site": "00bd6080",
      "incomplete_value": true,
      "site": "00bd6080",
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
      "definition_site": "00bd5c58",
      "incomplete_value": true,
      "site": "00bd5c58",
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
      "00bd607c",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6088",
      "READ",
      [
        "storage",
        "011266f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd60a4",
      "WRITE",
      [
        "storage",
        "011266f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd607c",
      "READ",
      [
        "storage",
        "01126ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6088",
      "READ",
      [
        "storage",
        "01126af0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd60a4",
      "WRITE",
      [
        "storage",
        "01126af0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5c40.md#insn-00bd5c7c) · [`00bd5c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5c40.md#insn-00bd5c98) · [`00bd5c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5c40.md#insn-00bd5c9c)
- 新版 `00bd60a4`（命令位置の公開資料なし） · `00bd60c0`（命令位置の公開資料なし） · `00bd60c4`（命令位置の公開資料なし）

~~~diff
- 00bd5c7c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd5c7c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd5c7c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6f0:8"]]
- 00bd5c7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd60a4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd60a4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd60a4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:af0:8"]]
+ 00bd60a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd5c7c bytes bfc21b39
+ 00bd60a4 bytes bfc22b39
- 00bd5c98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd5c98 ["INT_ADD", "register:40f0:8", ["const:bd5c98:8", "const:4:8"]]
- 00bd5c98 ["CALLIND", null, ["register:0:8"]]
+ 00bd60c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd60c0 ["INT_ADD", "register:40f0:8", ["const:bd60c0:8", "const:4:8"]]
+ 00bd60c0 ["CALLIND", null, ["register:0:8"]]
- 00bd5c98 bytes 00013fd6
+ 00bd60c0 bytes 00013fd6
- 00bd5c9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00bd5c9c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bd5c9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd60c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
+ 00bd60c4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd60c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bd5c9c bytes 9f7603f9
+ 00bd60c4 bytes 9f7605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b89338370879e057c9104f72faf7dc1"></a>

### [`00bd5cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5cb0.md) → [`00bd60d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd60d8.md) _ZN8firebase4auth13playgamescred14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6118",
      "incomplete_value": true,
      "site": "00bd6118",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5cf0",
      "incomplete_value": true,
      "site": "00bd5cf0",
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
            "const:6e8:8"
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
      "definition_site": "00bd60f4",
      "incomplete_value": true,
      "site": "00bd60f4",
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
      "definition_site": "00bd5ccc",
      "incomplete_value": true,
      "site": "00bd5ccc",
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
      "definition_site": "00bd60fc",
      "incomplete_value": false,
      "site": "00bd6110",
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
            "const:797:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5cd4",
      "incomplete_value": false,
      "site": "00bd5ce8",
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
            "const:757:8"
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
      "00bd60ec",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd60fc",
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      "00bd6118",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd60ec",
      "READ",
      [
        "storage",
        "01126ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd60fc",
      "PARAM",
      [
        "storage",
        "002b3797",
        null,
        "string"
      ]
    ],
    [
      "00bd6118",
      "WRITE",
      [
        "storage",
        "01126ae8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5cb0.md#insn-00bd5ce8) · [`00bd5cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5cb0.md#insn-00bd5cf0) · [`00bd5cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5cb0.md#insn-00bd5cc4)
- 新版 `00bd6110`（命令位置の公開資料なし） · `00bd6118`（命令位置の公開資料なし） · `00bd60ec`（命令位置の公開資料なし）

~~~diff
- 00bd5ce8 ["INT_ADD", "register:40f0:8", ["const:bd5ce8:8", "const:4:8"]]
- 00bd5ce8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd6110 ["INT_ADD", "register:40f0:8", ["const:bd6110:8", "const:4:8"]]
+ 00bd6110 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5ce8 bytes 8a130294
+ 00bd6110 bytes 80130294
- 00bd5cf0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00bd5cf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6118 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
+ 00bd6118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5cf0 bytes 807603f9
+ 00bd6118 bytes 807605f9
- 00bd5cc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00bd5cc4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd60ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
+ 00bd60ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd5cc4 bytes 817643f9
+ 00bd60ec bytes 817645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b842449e1c181d4bb04f222aac4488"></a>

### [`00bd5d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5d20.md) → [`00bd6148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6148.md) _ZN8firebase4auth13playgamescred11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bd6164",
      "incomplete_value": false,
      "site": "00bd6168",
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
      "definition_site": "00bd5d3c",
      "incomplete_value": false,
      "site": "00bd5d40",
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
      "definition_site": "00bd6174",
      "incomplete_value": true,
      "site": "00bd6180",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd5d4c",
      "incomplete_value": true,
      "site": "00bd5d58",
      "value": [
        "LOAD",
        "8",
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
      "00bd6164",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd6174",
      "DATA",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6164",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd6174",
      "DATA",
      [
        "storage",
        "01126af8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5d20.md#insn-00bd5d40) · [`00bd5d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5d20.md#insn-00bd5d3c) · [`00bd5d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5d20.md#insn-00bd5d48)
- 新版 `00bd6168`（命令位置の公開資料なし） · `00bd6164`（命令位置の公開資料なし） · `00bd6170`（命令位置の公開資料なし）

~~~diff
- 00bd5d40 ["INT_ADD", "register:40f0:8", ["const:bd5d40:8", "const:4:8"]]
- 00bd5d40 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd6168 ["INT_ADD", "register:40f0:8", ["const:bd6168:8", "const:4:8"]]
+ 00bd6168 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd5d40 bytes b0130294
+ 00bd6168 bytes a6130294
- 00bd5d3c ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bd5d3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd5d3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd5d3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd6164 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bd6164 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6164 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6164 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd5d3c bytes 00680a91
+ 00bd6164 bytes 009c0d91
- 00bd5d48 ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 00bd5d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd5d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd5d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd6170 ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 00bd6170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd6170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd6170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd5d48 bytes 08e11b91
+ 00bd6170 bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e0c7fbb2d4c347d70e7b731d9538518"></a>

### [`00bd5d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5d5c.md) → [`00bd6184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6184.md) _ZN8firebase4auth13playgamescred13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd61c4",
      "incomplete_value": true,
      "site": "00bd61c4",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5d9c",
      "incomplete_value": true,
      "site": "00bd5d9c",
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
            "const:6e8:8"
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
      "definition_site": "00bd61a0",
      "incomplete_value": true,
      "site": "00bd61a0",
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
      "definition_site": "00bd5d78",
      "incomplete_value": true,
      "site": "00bd5d78",
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
      "definition_site": "00bd61a8",
      "incomplete_value": false,
      "site": "00bd61bc",
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
            "const:797:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5d80",
      "incomplete_value": false,
      "site": "00bd5d94",
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
            "const:757:8"
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
      "00bd6198",
      "READ",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd61a8",
      "PARAM",
      [
        "storage",
        "002b3757",
        null,
        "string"
      ]
    ],
    [
      "00bd61c4",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6198",
      "READ",
      [
        "storage",
        "01126ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd61a8",
      "PARAM",
      [
        "storage",
        "002b3797",
        null,
        "string"
      ]
    ],
    [
      "00bd61c4",
      "WRITE",
      [
        "storage",
        "01126ae8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5d5c.md#insn-00bd5d94) · [`00bd5d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5d5c.md#insn-00bd5d9c) · [`00bd5d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5d5c.md#insn-00bd5d70)
- 新版 `00bd61bc`（命令位置の公開資料なし） · `00bd61c4`（命令位置の公開資料なし） · `00bd6198`（命令位置の公開資料なし）

~~~diff
- 00bd5d94 ["INT_ADD", "register:40f0:8", ["const:bd5d94:8", "const:4:8"]]
- 00bd5d94 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd61bc ["INT_ADD", "register:40f0:8", ["const:bd61bc:8", "const:4:8"]]
+ 00bd61bc ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5d94 bytes 5f130294
+ 00bd61bc bytes 55130294
- 00bd5d9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00bd5d9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd61c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
+ 00bd61c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5d9c bytes 807603f9
+ 00bd61c4 bytes 807605f9
- 00bd5d70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00bd5d70 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6198 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
+ 00bd6198 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd5d70 bytes 817643f9
+ 00bd6198 bytes 817645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcce85906216e4fe6613a7ed5017c47d"></a>

### [`00bd5dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5dcc.md) → [`00bd61f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd61f4.md) _ZN8firebase4auth13playgamescred10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bd6210",
      "incomplete_value": false,
      "site": "00bd6214",
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
      "definition_site": "00bd5de8",
      "incomplete_value": false,
      "site": "00bd5dec",
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
      "definition_site": "00bd6220",
      "incomplete_value": true,
      "site": "00bd622c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd5df8",
      "incomplete_value": true,
      "site": "00bd5e04",
      "value": [
        "LOAD",
        "8",
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
      "00bd6210",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd6220",
      "DATA",
      [
        "storage",
        "01126700",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd6210",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd6220",
      "DATA",
      [
        "storage",
        "01126b00",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5dcc.md#insn-00bd5dec) · [`00bd5de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5dcc.md#insn-00bd5de8) · [`00bd5df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5dcc.md#insn-00bd5df4)
- 新版 `00bd6214`（命令位置の公開資料なし） · `00bd6210`（命令位置の公開資料なし） · `00bd621c`（命令位置の公開資料なし）

~~~diff
- 00bd5dec ["INT_ADD", "register:40f0:8", ["const:bd5dec:8", "const:4:8"]]
- 00bd5dec ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd6214 ["INT_ADD", "register:40f0:8", ["const:bd6214:8", "const:4:8"]]
+ 00bd6214 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd5dec bytes 85130294
+ 00bd6214 bytes 7b130294
- 00bd5de8 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bd5de8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd5de8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd5de8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd6210 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bd6210 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6210 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6210 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd5de8 bytes 00441191
+ 00bd6210 bytes 00781491
- 00bd5df4 ["COPY", "tmp:0:8", ["const:700:8"]]
- 00bd5df4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd5df4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd5df4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd621c ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 00bd621c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd621c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd621c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd5df4 bytes 08011c91
+ 00bd621c bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9157155815177f0b7b4ce54209bc5642"></a>

### [`00bd5e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e08.md) → [`00bd6230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6230.md) _ZN8firebase4auth11twittercred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 33.33% / 新版 20.00%

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
      "site": "00bd5e34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd625c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd6244",
      "incomplete_value": true,
      "site": "00bd6244",
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
      "definition_site": "00bd5e1c",
      "incomplete_value": true,
      "site": "00bd5e1c",
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
      "00bd6240",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd5e28",
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd5e2c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bd6240",
      "READ",
      [
        "storage",
        "01126b08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6250",
      "PARAM",
      [
        "storage",
        "002a1d18",
        null,
        "string"
      ]
    ],
    [
      "00bd6254",
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

- 旧版 [`00bd5e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e08.md#insn-00bd5e1c) · [`00bd5e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e08.md#insn-00bd5e2c) · [`00bd5e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e08.md#insn-00bd5e34)
- 新版 `00bd6244`（命令位置の公開資料なし）

~~~diff
- 00bd5e1c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd5e1c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd6244 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd6244 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd5e1c bytes e80000b5
+ 00bd6244 bytes e80000b5
- 00bd5e2c ["INT_ADD", "register:40f0:8", ["const:bd5e2c:8", "const:4:8"]]
- 00bd5e2c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5e2c bytes 39130294
- 00bd5e34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
- 00bd5e34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5e34 bytes 608603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-812d7f493a018e951b435aeab770ac42"></a>

### [`00bd5e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e48.md) → [`00bd6270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6270.md) _ZN8firebase4auth11twittercred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bd629c",
      "incomplete_value": true,
      "site": "00bd629c",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5e74",
      "incomplete_value": true,
      "site": "00bd5e74",
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
            "const:708:8"
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
      "definition_site": "00bd6284",
      "incomplete_value": true,
      "site": "00bd6284",
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
      "definition_site": "00bd5e5c",
      "incomplete_value": true,
      "site": "00bd5e5c",
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
      "definition_site": "00bd628c",
      "incomplete_value": false,
      "site": "00bd6294",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5e64",
      "incomplete_value": false,
      "site": "00bd5e6c",
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
            "const:c4b:8"
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
      "00bd6280",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd628c",
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      "00bd629c",
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6280",
      "READ",
      [
        "storage",
        "01126b08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd628c",
      "PARAM",
      [
        "storage",
        "002a1d18",
        null,
        "string"
      ]
    ],
    [
      "00bd629c",
      "WRITE",
      [
        "storage",
        "01126b08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e48.md#insn-00bd5e6c) · [`00bd5e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e48.md#insn-00bd5e74) · [`00bd5e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e48.md#insn-00bd5e58)
- 新版 `00bd6294`（命令位置の公開資料なし） · `00bd629c`（命令位置の公開資料なし） · `00bd6280`（命令位置の公開資料なし）

~~~diff
- 00bd5e6c ["INT_ADD", "register:40f0:8", ["const:bd5e6c:8", "const:4:8"]]
- 00bd5e6c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd6294 ["INT_ADD", "register:40f0:8", ["const:bd6294:8", "const:4:8"]]
+ 00bd6294 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5e6c bytes 29130294
+ 00bd6294 bytes 1f130294
- 00bd5e74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
- 00bd5e74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd629c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b08:8"]]
+ 00bd629c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5e74 bytes 608603f9
+ 00bd629c bytes 608605f9
- 00bd5e58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
- 00bd5e58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6280 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b08:8"]]
+ 00bd6280 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd5e58 bytes 688643f9
+ 00bd6280 bytes 688645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d1dfe831b36df5262f9026c862b7619"></a>

### [`00bd5e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e88.md) → [`00bd62b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd62b0.md) _ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bd62e0",
      "incomplete_value": true,
      "site": "00bd62e0",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5eb8",
      "incomplete_value": true,
      "site": "00bd5eb8",
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
            "const:708:8"
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
      "definition_site": "00bd62c4",
      "incomplete_value": true,
      "site": "00bd62c4",
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
      "definition_site": "00bd5e9c",
      "incomplete_value": true,
      "site": "00bd5e9c",
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
      "definition_site": "00bd62d0",
      "incomplete_value": false,
      "site": "00bd62d8",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5ea8",
      "incomplete_value": false,
      "site": "00bd5eb0",
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
            "const:c4b:8"
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
      "00bd62c0",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd62d0",
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      "00bd62e0",
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd62c0",
      "READ",
      [
        "storage",
        "01126b08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd62d0",
      "PARAM",
      [
        "storage",
        "002a1d18",
        null,
        "string"
      ]
    ],
    [
      "00bd62e0",
      "WRITE",
      [
        "storage",
        "01126b08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e88.md#insn-00bd5eb0) · [`00bd5eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e88.md#insn-00bd5eb8) · [`00bd5e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5e88.md#insn-00bd5e98)
- 新版 `00bd62d8`（命令位置の公開資料なし） · `00bd62e0`（命令位置の公開資料なし） · `00bd62c0`（命令位置の公開資料なし）

~~~diff
- 00bd5eb0 ["INT_ADD", "register:40f0:8", ["const:bd5eb0:8", "const:4:8"]]
- 00bd5eb0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd62d8 ["INT_ADD", "register:40f0:8", ["const:bd62d8:8", "const:4:8"]]
+ 00bd62d8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5eb0 bytes 18130294
+ 00bd62d8 bytes 0e130294
- 00bd5eb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
- 00bd5eb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd62e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b08:8"]]
+ 00bd62e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5eb8 bytes 608603f9
+ 00bd62e0 bytes 608605f9
- 00bd5e98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
- 00bd5e98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd62c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b08:8"]]
+ 00bd62c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd5e98 bytes 688643f9
+ 00bd62c0 bytes 688645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0328ebdc72c8a5f2dcfcf20522502839"></a>

### [`00bd5ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ecc.md) → [`00bd62f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd62f4.md) _ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bd6324",
      "incomplete_value": true,
      "site": "00bd6324",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5efc",
      "incomplete_value": true,
      "site": "00bd5efc",
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
            "const:708:8"
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
      "definition_site": "00bd6308",
      "incomplete_value": true,
      "site": "00bd6308",
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
      "definition_site": "00bd5ee0",
      "incomplete_value": true,
      "site": "00bd5ee0",
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
      "definition_site": "00bd6310",
      "incomplete_value": false,
      "site": "00bd631c",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5ee8",
      "incomplete_value": false,
      "site": "00bd5ef4",
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
            "const:c4b:8"
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
      "00bd6304",
      "READ",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6310",
      "PARAM",
      [
        "storage",
        "002a1c4b",
        null,
        "string"
      ]
    ],
    [
      "00bd6324",
      "WRITE",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6304",
      "READ",
      [
        "storage",
        "01126b08",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6310",
      "PARAM",
      [
        "storage",
        "002a1d18",
        null,
        "string"
      ]
    ],
    [
      "00bd6324",
      "WRITE",
      [
        "storage",
        "01126b08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ecc.md#insn-00bd5ef4) · [`00bd5efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ecc.md#insn-00bd5efc) · [`00bd5edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5ecc.md#insn-00bd5edc)
- 新版 `00bd631c`（命令位置の公開資料なし） · `00bd6324`（命令位置の公開資料なし） · `00bd6304`（命令位置の公開資料なし）

~~~diff
- 00bd5ef4 ["INT_ADD", "register:40f0:8", ["const:bd5ef4:8", "const:4:8"]]
- 00bd5ef4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bd631c ["INT_ADD", "register:40f0:8", ["const:bd631c:8", "const:4:8"]]
+ 00bd631c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5ef4 bytes 07130294
+ 00bd631c bytes fd120294
- 00bd5efc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
- 00bd5efc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd6324 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b08:8"]]
+ 00bd6324 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5efc bytes 608603f9
+ 00bd6324 bytes 608605f9
- 00bd5edc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:708:8"]]
- 00bd5edc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6304 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b08:8"]]
+ 00bd6304 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd5edc bytes 688643f9
+ 00bd6304 bytes 688645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

