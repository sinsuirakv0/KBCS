# v16.0.1 → v16.0.2 · 最優先の変更候補 (74)

[一覧の目次](README.md)

<a id="compare-791f8b00a1fcaa83cbe569256e8887f1"></a>

### [`00b4d410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d410.md) → [`00b4d4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d4ac.md) _ZN8firebase4util11short_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4d534",
      "incomplete_value": true,
      "site": "00b4d534",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d498",
      "incomplete_value": true,
      "site": "00b4d498",
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
            "const:cb0:8"
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
      "definition_site": "00b4d4e0",
      "incomplete_value": true,
      "site": "00b4d4ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d444",
      "incomplete_value": true,
      "site": "00b4d450",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
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
      "00b4d4c0",
      "READ",
      [
        "storage",
        "01125cb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d4e0",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d534",
      "WRITE",
      [
        "storage",
        "01125cb0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d4c0",
      "READ",
      [
        "storage",
        "01125db0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d4e0",
      "READ",
      [
        "storage",
        "01125da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d534",
      "WRITE",
      [
        "storage",
        "01125db0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d410.md#insn-00b4d450) · [`00b4d498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d410.md#insn-00b4d498) · [`00b4d424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d410.md#insn-00b4d424)
- 新版 [`00b4d4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d4ac.md#insn-00b4d4ec) · [`00b4d534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d4ac.md#insn-00b4d534) · [`00b4d4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d4ac.md#insn-00b4d4c0)

~~~diff
- 00b4d450 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4d450 ["INT_ADD", "register:40f0:8", ["const:b4d450:8", "const:4:8"]]
- 00b4d450 ["CALLIND", null, ["register:0:8"]]
+ 00b4d4ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d4ec ["INT_ADD", "register:40f0:8", ["const:b4d4ec:8", "const:4:8"]]
+ 00b4d4ec ["CALLIND", null, ["register:0:8"]]
- 00b4d450 bytes 00013fd6
+ 00b4d4ec bytes 00013fd6
- 00b4d498 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4d498 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:cb0:8"]]
- 00b4d498 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4d534 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4d534 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:db0:8"]]
+ 00b4d534 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4d498 bytes a0c23239
+ 00b4d534 bytes a0c23639
- 00b4d424 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cb0:8"]]
- 00b4d424 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4d424 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4d4c0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:db0:8"]]
+ 00b4d4c0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d4c0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4d424 bytes a8c27239
+ 00b4d4c0 bytes a8c27639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be2b5f63f5ee437fab607fb018d68be5"></a>

### [`00b4d4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d4ac.md) → [`00b4d548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d548.md) _ZN8firebase4util11short_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00b4d584",
      "incomplete_value": true,
      "site": "00b4d584",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d4e8",
      "incomplete_value": true,
      "site": "00b4d4e8",
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
            "const:cb0:8"
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
      "definition_site": "00b4d5d4",
      "incomplete_value": true,
      "site": "00b4d5d4",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d538",
      "incomplete_value": true,
      "site": "00b4d538",
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
            "const:ca8:8"
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
      "definition_site": "00b4d560",
      "incomplete_value": true,
      "site": "00b4d560",
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
      "definition_site": "00b4d4c4",
      "incomplete_value": true,
      "site": "00b4d4c4",
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
      "00b4d55c",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d568",
      "READ",
      [
        "storage",
        "01125cb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d584",
      "WRITE",
      [
        "storage",
        "01125cb0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d55c",
      "READ",
      [
        "storage",
        "01125da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d568",
      "READ",
      [
        "storage",
        "01125db0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d584",
      "WRITE",
      [
        "storage",
        "01125db0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d4ac.md#insn-00b4d4e8) · [`00b4d534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d4ac.md#insn-00b4d534) · [`00b4d538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d4ac.md#insn-00b4d538)
- 新版 [`00b4d584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d548.md#insn-00b4d584) · [`00b4d5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d548.md#insn-00b4d5d0) · [`00b4d5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d548.md#insn-00b4d5d4)

~~~diff
- 00b4d4e8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4d4e8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4d4e8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:cb0:8"]]
- 00b4d4e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4d584 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4d584 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4d584 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:db0:8"]]
+ 00b4d584 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4d4e8 bytes bfc23239
+ 00b4d584 bytes bfc23639
- 00b4d534 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4d534 ["INT_ADD", "register:40f0:8", ["const:b4d534:8", "const:4:8"]]
- 00b4d534 ["CALLIND", null, ["register:0:8"]]
+ 00b4d5d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d5d0 ["INT_ADD", "register:40f0:8", ["const:b4d5d0:8", "const:4:8"]]
+ 00b4d5d0 ["CALLIND", null, ["register:0:8"]]
- 00b4d534 bytes 00013fd6
+ 00b4d5d0 bytes 00013fd6
- 00b4d538 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
- 00b4d538 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4d538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4d5d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:da8:8"]]
+ 00b4d5d4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4d5d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4d538 bytes 9f5606f9
+ 00b4d5d4 bytes 9fd606f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d78c6af9db70ec492b9c9cb37a84ed7c"></a>

### [`00b4d54c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d54c.md) → [`00b4d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d5e8.md) _ZN8firebase4util11short_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4d628",
      "incomplete_value": true,
      "site": "00b4d628",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d58c",
      "incomplete_value": true,
      "site": "00b4d58c",
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
            "const:ca8:8"
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
      "definition_site": "00b4d604",
      "incomplete_value": true,
      "site": "00b4d604",
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
      "definition_site": "00b4d568",
      "incomplete_value": true,
      "site": "00b4d568",
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
      "definition_site": "00b4d60c",
      "incomplete_value": false,
      "site": "00b4d620",
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
            "const:7c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d570",
      "incomplete_value": false,
      "site": "00b4d584",
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
            "const:81a:8"
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
      "00b4d5fc",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d60c",
      "PARAM",
      [
        "storage",
        "002bf81a",
        null,
        "string"
      ]
    ],
    [
      "00b4d628",
      "WRITE",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d5fc",
      "READ",
      [
        "storage",
        "01125da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d60c",
      "PARAM",
      [
        "storage",
        "002bf7c6",
        null,
        "string"
      ]
    ],
    [
      "00b4d628",
      "WRITE",
      [
        "storage",
        "01125da8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d54c.md#insn-00b4d584) · [`00b4d58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d54c.md#insn-00b4d58c) · [`00b4d560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d54c.md#insn-00b4d560)
- 新版 [`00b4d620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d5e8.md#insn-00b4d620) · [`00b4d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d5e8.md#insn-00b4d628) · [`00b4d5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d5e8.md#insn-00b4d5fc)

~~~diff
- 00b4d584 ["INT_ADD", "register:40f0:8", ["const:b4d584:8", "const:4:8"]]
- 00b4d584 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d620 ["INT_ADD", "register:40f0:8", ["const:b4d620:8", "const:4:8"]]
+ 00b4d620 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d584 bytes 63360494
+ 00b4d620 bytes 70360494
- 00b4d58c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
- 00b4d58c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d628 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:da8:8"]]
+ 00b4d628 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d58c bytes 805606f9
+ 00b4d628 bytes 80d606f9
- 00b4d560 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
- 00b4d560 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d5fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:da8:8"]]
+ 00b4d5fc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d560 bytes 815646f9
+ 00b4d5fc bytes 81d646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-609bf64e0d243df6b5f64f2b6d3309b6"></a>

### [`00b4d5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d5bc.md) → [`00b4d658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d658.md) _ZN8firebase4util11short_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4d674",
      "incomplete_value": false,
      "site": "00b4d678",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d5d8",
      "incomplete_value": false,
      "site": "00b4d5dc",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4d684",
      "incomplete_value": true,
      "site": "00b4d690",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4d5e8",
      "incomplete_value": true,
      "site": "00b4d5f4",
      "value": [
        "LOAD",
        "8",
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
      "00b4d674",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4d684",
      "DATA",
      [
        "storage",
        "01125cb8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d674",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4d684",
      "DATA",
      [
        "storage",
        "01125db8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d5bc.md#insn-00b4d5dc) · [`00b4d5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d5bc.md#insn-00b4d5d8) · [`00b4d5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d5bc.md#insn-00b4d5e4)
- 新版 [`00b4d678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d658.md#insn-00b4d678) · [`00b4d674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d658.md#insn-00b4d674) · [`00b4d680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d658.md#insn-00b4d680)

~~~diff
- 00b4d5dc ["INT_ADD", "register:40f0:8", ["const:b4d5dc:8", "const:4:8"]]
- 00b4d5dc ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4d678 ["INT_ADD", "register:40f0:8", ["const:b4d678:8", "const:4:8"]]
+ 00b4d678 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4d5dc bytes 89360494
+ 00b4d678 bytes 96360494
- 00b4d5d8 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4d5d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d5d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d5d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d674 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4d674 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d674 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d674 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4d5d8 bytes 009c0d91
+ 00b4d674 bytes 002c0c91
- 00b4d5e4 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 00b4d5e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d5e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d5e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4d680 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00b4d680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4d5e4 bytes 08e13291
+ 00b4d680 bytes 08e13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5331838393f57c84c020a03ac0cdd224"></a>

### [`00b4d5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d5f8.md) → [`00b4d694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d694.md) _ZN8firebase4util11short_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4d6d4",
      "incomplete_value": true,
      "site": "00b4d6d4",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d638",
      "incomplete_value": true,
      "site": "00b4d638",
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
            "const:ca8:8"
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
      "definition_site": "00b4d6b0",
      "incomplete_value": true,
      "site": "00b4d6b0",
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
      "definition_site": "00b4d614",
      "incomplete_value": true,
      "site": "00b4d614",
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
      "definition_site": "00b4d6b8",
      "incomplete_value": false,
      "site": "00b4d6cc",
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
            "const:7c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d61c",
      "incomplete_value": false,
      "site": "00b4d630",
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
            "const:81a:8"
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
      "00b4d6a8",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d6b8",
      "PARAM",
      [
        "storage",
        "002bf81a",
        null,
        "string"
      ]
    ],
    [
      "00b4d6d4",
      "WRITE",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d6a8",
      "READ",
      [
        "storage",
        "01125da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d6b8",
      "PARAM",
      [
        "storage",
        "002bf7c6",
        null,
        "string"
      ]
    ],
    [
      "00b4d6d4",
      "WRITE",
      [
        "storage",
        "01125da8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d5f8.md#insn-00b4d630) · [`00b4d638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d5f8.md#insn-00b4d638) · [`00b4d60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d5f8.md#insn-00b4d60c)
- 新版 [`00b4d6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d694.md#insn-00b4d6cc) · [`00b4d6d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d694.md#insn-00b4d6d4) · [`00b4d6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d694.md#insn-00b4d6a8)

~~~diff
- 00b4d630 ["INT_ADD", "register:40f0:8", ["const:b4d630:8", "const:4:8"]]
- 00b4d630 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d6cc ["INT_ADD", "register:40f0:8", ["const:b4d6cc:8", "const:4:8"]]
+ 00b4d6cc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d630 bytes 38360494
+ 00b4d6cc bytes 45360494
- 00b4d638 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
- 00b4d638 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d6d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:da8:8"]]
+ 00b4d6d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d638 bytes 805606f9
+ 00b4d6d4 bytes 80d606f9
- 00b4d60c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
- 00b4d60c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d6a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:da8:8"]]
+ 00b4d6a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d60c bytes 815646f9
+ 00b4d6a8 bytes 81d646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98fb35603d58ef8a27f64f14ca70ba61"></a>

### [`00b4d668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d668.md) → [`00b4d704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d704.md) _ZN8firebase4util11short_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4d720",
      "incomplete_value": false,
      "site": "00b4d724",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d684",
      "incomplete_value": false,
      "site": "00b4d688",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4d730",
      "incomplete_value": true,
      "site": "00b4d73c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4d694",
      "incomplete_value": true,
      "site": "00b4d6a0",
      "value": [
        "LOAD",
        "8",
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
      "00b4d720",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4d730",
      "DATA",
      [
        "storage",
        "01125cc8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d720",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4d730",
      "DATA",
      [
        "storage",
        "01125dc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d668.md#insn-00b4d688) · [`00b4d684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d668.md#insn-00b4d684) · [`00b4d690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d668.md#insn-00b4d690)
- 新版 [`00b4d724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d704.md#insn-00b4d724) · [`00b4d720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d704.md#insn-00b4d720) · [`00b4d72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d704.md#insn-00b4d72c)

~~~diff
- 00b4d688 ["INT_ADD", "register:40f0:8", ["const:b4d688:8", "const:4:8"]]
- 00b4d688 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4d724 ["INT_ADD", "register:40f0:8", ["const:b4d724:8", "const:4:8"]]
+ 00b4d724 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4d688 bytes 5e360494
+ 00b4d724 bytes 6b360494
- 00b4d684 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4d684 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d684 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d684 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d720 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4d720 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d720 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d720 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4d684 bytes 00781491
+ 00b4d720 bytes 00341591
- 00b4d690 ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00b4d690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4d72c ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00b4d72c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d72c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d72c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4d690 bytes 08213391
+ 00b4d72c bytes 08213791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b59d6f25c7f0976b9d084c5b48feb2a"></a>

### [`00b4d6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d6a4.md) → [`00b4d740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d740.md) _ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4d76c",
      "incomplete_value": true,
      "site": "00b4d76c",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d6d0",
      "incomplete_value": true,
      "site": "00b4d6d0",
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
            "const:cd0:8"
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
      "definition_site": "00b4d754",
      "incomplete_value": true,
      "site": "00b4d754",
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
      "definition_site": "00b4d6b8",
      "incomplete_value": true,
      "site": "00b4d6b8",
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
      "definition_site": "00b4d760",
      "incomplete_value": false,
      "site": "00b4d764",
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
            "const:a44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d6c4",
      "incomplete_value": false,
      "site": "00b4d6c8",
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
            "const:aa0:8"
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
      "00b4d750",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d760",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "00b4d76c",
      "WRITE",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d750",
      "READ",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d760",
      "PARAM",
      [
        "storage",
        "002aea44",
        null,
        "string"
      ]
    ],
    [
      "00b4d76c",
      "WRITE",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d6a4.md#insn-00b4d6c8) · [`00b4d6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d6a4.md#insn-00b4d6d0) · [`00b4d6b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d6a4.md#insn-00b4d6b4)
- 新版 [`00b4d764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d740.md#insn-00b4d764) · [`00b4d76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d740.md#insn-00b4d76c) · [`00b4d750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d740.md#insn-00b4d750)

~~~diff
- 00b4d6c8 ["INT_ADD", "register:40f0:8", ["const:b4d6c8:8", "const:4:8"]]
- 00b4d6c8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d764 ["INT_ADD", "register:40f0:8", ["const:b4d764:8", "const:4:8"]]
+ 00b4d764 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d6c8 bytes 12360494
+ 00b4d764 bytes 1f360494
- 00b4d6d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
- 00b4d6d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d76c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
+ 00b4d76c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d6d0 bytes 606a06f9
+ 00b4d76c bytes 60ea06f9
- 00b4d6b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
- 00b4d6b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d750 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
+ 00b4d750 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d6b4 bytes 686a46f9
+ 00b4d750 bytes 68ea46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61654ff655314cf6ef86e5371b00947c"></a>

### [`00b4d6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d6e4.md) → [`00b4d780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d780.md) _ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4d7ac",
      "incomplete_value": true,
      "site": "00b4d7ac",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d710",
      "incomplete_value": true,
      "site": "00b4d710",
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
            "const:cd0:8"
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
      "definition_site": "00b4d794",
      "incomplete_value": true,
      "site": "00b4d794",
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
      "definition_site": "00b4d6f8",
      "incomplete_value": true,
      "site": "00b4d6f8",
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
      "definition_site": "00b4d79c",
      "incomplete_value": false,
      "site": "00b4d7a4",
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
            "const:a44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d700",
      "incomplete_value": false,
      "site": "00b4d708",
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
            "const:aa0:8"
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
      "00b4d790",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d79c",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "00b4d7ac",
      "WRITE",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d790",
      "READ",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d79c",
      "PARAM",
      [
        "storage",
        "002aea44",
        null,
        "string"
      ]
    ],
    [
      "00b4d7ac",
      "WRITE",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d6e4.md#insn-00b4d708) · [`00b4d710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d6e4.md#insn-00b4d710) · [`00b4d6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d6e4.md#insn-00b4d6f4)
- 新版 [`00b4d7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d780.md#insn-00b4d7a4) · [`00b4d7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d780.md#insn-00b4d7ac) · [`00b4d790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d780.md#insn-00b4d790)

~~~diff
- 00b4d708 ["INT_ADD", "register:40f0:8", ["const:b4d708:8", "const:4:8"]]
- 00b4d708 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d7a4 ["INT_ADD", "register:40f0:8", ["const:b4d7a4:8", "const:4:8"]]
+ 00b4d7a4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d708 bytes 02360494
+ 00b4d7a4 bytes 0f360494
- 00b4d710 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
- 00b4d710 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d7ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
+ 00b4d7ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d710 bytes 606a06f9
+ 00b4d7ac bytes 60ea06f9
- 00b4d6f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
- 00b4d6f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d790 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
+ 00b4d790 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d6f4 bytes 686a46f9
+ 00b4d790 bytes 68ea46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fae973941f08898884c18a59010fb60e"></a>

### [`00b4d724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d724.md) → [`00b4d7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d7c0.md) _ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4d7f0",
      "incomplete_value": true,
      "site": "00b4d7f0",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d754",
      "incomplete_value": true,
      "site": "00b4d754",
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
            "const:cd0:8"
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
      "definition_site": "00b4d7d4",
      "incomplete_value": true,
      "site": "00b4d7d4",
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
      "definition_site": "00b4d738",
      "incomplete_value": true,
      "site": "00b4d738",
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
      "definition_site": "00b4d7e0",
      "incomplete_value": false,
      "site": "00b4d7e8",
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
            "const:a44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d744",
      "incomplete_value": false,
      "site": "00b4d74c",
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
            "const:aa0:8"
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
      "00b4d7d0",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d7e0",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "00b4d7f0",
      "WRITE",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d7d0",
      "READ",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d7e0",
      "PARAM",
      [
        "storage",
        "002aea44",
        null,
        "string"
      ]
    ],
    [
      "00b4d7f0",
      "WRITE",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d74c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d724.md#insn-00b4d74c) · [`00b4d754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d724.md#insn-00b4d754) · [`00b4d734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d724.md#insn-00b4d734)
- 新版 [`00b4d7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d7c0.md#insn-00b4d7e8) · [`00b4d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d7c0.md#insn-00b4d7f0) · [`00b4d7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d7c0.md#insn-00b4d7d0)

~~~diff
- 00b4d74c ["INT_ADD", "register:40f0:8", ["const:b4d74c:8", "const:4:8"]]
- 00b4d74c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d7e8 ["INT_ADD", "register:40f0:8", ["const:b4d7e8:8", "const:4:8"]]
+ 00b4d7e8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d74c bytes f1350494
+ 00b4d7e8 bytes fe350494
- 00b4d754 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
- 00b4d754 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d7f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
+ 00b4d7f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d754 bytes 606a06f9
+ 00b4d7f0 bytes 60ea06f9
- 00b4d734 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
- 00b4d734 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d7d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
+ 00b4d7d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d734 bytes 686a46f9
+ 00b4d7d0 bytes 68ea46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d1bd135a4c7a5ff66866636d04ec5c3"></a>

### [`00b4d768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d768.md) → [`00b4d804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d804.md) _ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4d834",
      "incomplete_value": true,
      "site": "00b4d834",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d798",
      "incomplete_value": true,
      "site": "00b4d798",
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
            "const:cd0:8"
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
      "definition_site": "00b4d818",
      "incomplete_value": true,
      "site": "00b4d818",
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
      "definition_site": "00b4d77c",
      "incomplete_value": true,
      "site": "00b4d77c",
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
      "definition_site": "00b4d820",
      "incomplete_value": false,
      "site": "00b4d82c",
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
            "const:a44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d784",
      "incomplete_value": false,
      "site": "00b4d790",
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
            "const:aa0:8"
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
      "00b4d814",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d820",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "00b4d834",
      "WRITE",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d814",
      "READ",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d820",
      "PARAM",
      [
        "storage",
        "002aea44",
        null,
        "string"
      ]
    ],
    [
      "00b4d834",
      "WRITE",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d768.md#insn-00b4d790) · [`00b4d798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d768.md#insn-00b4d798) · [`00b4d778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d768.md#insn-00b4d778)
- 新版 [`00b4d82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d804.md#insn-00b4d82c) · [`00b4d834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d804.md#insn-00b4d834) · [`00b4d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d804.md#insn-00b4d814)

~~~diff
- 00b4d790 ["INT_ADD", "register:40f0:8", ["const:b4d790:8", "const:4:8"]]
- 00b4d790 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d82c ["INT_ADD", "register:40f0:8", ["const:b4d82c:8", "const:4:8"]]
+ 00b4d82c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d790 bytes e0350494
+ 00b4d82c bytes ed350494
- 00b4d798 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
- 00b4d798 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d834 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
+ 00b4d834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d798 bytes 606a06f9
+ 00b4d834 bytes 60ea06f9
- 00b4d778 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
- 00b4d778 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d814 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
+ 00b4d814 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d778 bytes 686a46f9
+ 00b4d814 bytes 68ea46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c085ff990d554bddafd42664e9e719c"></a>

### [`00b4d7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d7b8.md) → [`00b4d854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d854.md) _ZN8firebase4util6string15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4d8dc",
      "incomplete_value": true,
      "site": "00b4d8dc",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d840",
      "incomplete_value": true,
      "site": "00b4d840",
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
            "const:cd8:8"
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
      "definition_site": "00b4d888",
      "incomplete_value": true,
      "site": "00b4d894",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d7ec",
      "incomplete_value": true,
      "site": "00b4d7f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
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
      "00b4d868",
      "READ",
      [
        "storage",
        "01125cd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d888",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d8dc",
      "WRITE",
      [
        "storage",
        "01125cd8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d868",
      "READ",
      [
        "storage",
        "01125dd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d888",
      "READ",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d8dc",
      "WRITE",
      [
        "storage",
        "01125dd8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d7b8.md#insn-00b4d7f8) · [`00b4d840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d7b8.md#insn-00b4d840) · [`00b4d7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d7b8.md#insn-00b4d7cc)
- 新版 [`00b4d894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d854.md#insn-00b4d894) · [`00b4d8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d854.md#insn-00b4d8dc) · [`00b4d868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d854.md#insn-00b4d868)

~~~diff
- 00b4d7f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4d7f8 ["INT_ADD", "register:40f0:8", ["const:b4d7f8:8", "const:4:8"]]
- 00b4d7f8 ["CALLIND", null, ["register:0:8"]]
+ 00b4d894 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d894 ["INT_ADD", "register:40f0:8", ["const:b4d894:8", "const:4:8"]]
+ 00b4d894 ["CALLIND", null, ["register:0:8"]]
- 00b4d7f8 bytes 00013fd6
+ 00b4d894 bytes 00013fd6
- 00b4d840 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4d840 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:cd8:8"]]
- 00b4d840 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4d8dc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4d8dc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:dd8:8"]]
+ 00b4d8dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4d840 bytes a0623339
+ 00b4d8dc bytes a0623739
- 00b4d7cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cd8:8"]]
- 00b4d7cc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4d7cc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4d868 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dd8:8"]]
+ 00b4d868 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d868 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4d7cc bytes a8627339
+ 00b4d868 bytes a8627739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61a0557905c5adb12849afe4f16593ed"></a>

### [`00b4d854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d854.md) → [`00b4d8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d8f0.md) _ZN8firebase4util6string12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00b4d92c",
      "incomplete_value": true,
      "site": "00b4d92c",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d890",
      "incomplete_value": true,
      "site": "00b4d890",
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
            "const:cd8:8"
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
      "definition_site": "00b4d97c",
      "incomplete_value": true,
      "site": "00b4d97c",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d8e0",
      "incomplete_value": true,
      "site": "00b4d8e0",
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
            "const:cd0:8"
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
      "definition_site": "00b4d908",
      "incomplete_value": true,
      "site": "00b4d908",
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
      "definition_site": "00b4d86c",
      "incomplete_value": true,
      "site": "00b4d86c",
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
      "00b4d904",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d910",
      "READ",
      [
        "storage",
        "01125cd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d92c",
      "WRITE",
      [
        "storage",
        "01125cd8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d904",
      "READ",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d910",
      "READ",
      [
        "storage",
        "01125dd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d92c",
      "WRITE",
      [
        "storage",
        "01125dd8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d854.md#insn-00b4d890) · [`00b4d8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d854.md#insn-00b4d8dc) · [`00b4d8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d854.md#insn-00b4d8e0)
- 新版 [`00b4d92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d8f0.md#insn-00b4d92c) · [`00b4d978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d8f0.md#insn-00b4d978) · [`00b4d97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d8f0.md#insn-00b4d97c)

~~~diff
- 00b4d890 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4d890 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4d890 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:cd8:8"]]
- 00b4d890 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4d92c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4d92c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4d92c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:dd8:8"]]
+ 00b4d92c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4d890 bytes bf623339
+ 00b4d92c bytes bf623739
- 00b4d8dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4d8dc ["INT_ADD", "register:40f0:8", ["const:b4d8dc:8", "const:4:8"]]
- 00b4d8dc ["CALLIND", null, ["register:0:8"]]
+ 00b4d978 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d978 ["INT_ADD", "register:40f0:8", ["const:b4d978:8", "const:4:8"]]
+ 00b4d978 ["CALLIND", null, ["register:0:8"]]
- 00b4d8dc bytes 00013fd6
+ 00b4d978 bytes 00013fd6
- 00b4d8e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
- 00b4d8e0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4d8e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4d97c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd0:8"]]
+ 00b4d97c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4d97c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4d8e0 bytes 9f6a06f9
+ 00b4d97c bytes 9fea06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2cf2d2b8c5d02c27db2d5c0c80416fe"></a>

### [`00b4d8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d8f4.md) → [`00b4d990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d990.md) _ZN8firebase4util6string14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4d9d0",
      "incomplete_value": true,
      "site": "00b4d9d0",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d934",
      "incomplete_value": true,
      "site": "00b4d934",
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
            "const:cd0:8"
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
      "definition_site": "00b4d9ac",
      "incomplete_value": true,
      "site": "00b4d9ac",
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
      "definition_site": "00b4d910",
      "incomplete_value": true,
      "site": "00b4d910",
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
      "definition_site": "00b4d9b4",
      "incomplete_value": false,
      "site": "00b4d9c8",
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
            "const:a44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d918",
      "incomplete_value": false,
      "site": "00b4d92c",
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
            "const:aa0:8"
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
      "00b4d9a4",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d9b4",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "00b4d9d0",
      "WRITE",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d9a4",
      "READ",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d9b4",
      "PARAM",
      [
        "storage",
        "002aea44",
        null,
        "string"
      ]
    ],
    [
      "00b4d9d0",
      "WRITE",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d8f4.md#insn-00b4d92c) · [`00b4d934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d8f4.md#insn-00b4d934) · [`00b4d908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d8f4.md#insn-00b4d908)
- 新版 [`00b4d9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d990.md#insn-00b4d9c8) · [`00b4d9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d990.md#insn-00b4d9d0) · [`00b4d9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d990.md#insn-00b4d9a4)

~~~diff
- 00b4d92c ["INT_ADD", "register:40f0:8", ["const:b4d92c:8", "const:4:8"]]
- 00b4d92c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d9c8 ["INT_ADD", "register:40f0:8", ["const:b4d9c8:8", "const:4:8"]]
+ 00b4d9c8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d92c bytes 79350494
+ 00b4d9c8 bytes 86350494
- 00b4d934 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
- 00b4d934 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d9d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd0:8"]]
+ 00b4d9d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d934 bytes 806a06f9
+ 00b4d9d0 bytes 80ea06f9
- 00b4d908 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
- 00b4d908 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d9a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd0:8"]]
+ 00b4d9a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d908 bytes 816a46f9
+ 00b4d9a4 bytes 81ea46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e2bafc39a3f362f42188f9900b3e9a9"></a>

### [`00b4d964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d964.md) → [`00b4da00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4da00.md) _ZN8firebase4util6string11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4da1c",
      "incomplete_value": false,
      "site": "00b4da20",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d980",
      "incomplete_value": false,
      "site": "00b4d984",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4da2c",
      "incomplete_value": true,
      "site": "00b4da38",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4d990",
      "incomplete_value": true,
      "site": "00b4d99c",
      "value": [
        "LOAD",
        "8",
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
      "00b4da1c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4da2c",
      "DATA",
      [
        "storage",
        "01125ce0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4da1c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4da2c",
      "DATA",
      [
        "storage",
        "01125de0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d964.md#insn-00b4d984) · [`00b4d980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d964.md#insn-00b4d980) · [`00b4d98c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d964.md#insn-00b4d98c)
- 新版 [`00b4da20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4da00.md#insn-00b4da20) · [`00b4da1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4da00.md#insn-00b4da1c) · [`00b4da28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4da00.md#insn-00b4da28)

~~~diff
- 00b4d984 ["INT_ADD", "register:40f0:8", ["const:b4d984:8", "const:4:8"]]
- 00b4d984 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4da20 ["INT_ADD", "register:40f0:8", ["const:b4da20:8", "const:4:8"]]
+ 00b4da20 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4d984 bytes 9f350494
+ 00b4da20 bytes ac350494
- 00b4d980 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4d980 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d980 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d980 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4da1c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4da1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4da1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4da1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4d980 bytes 009c0d91
+ 00b4da1c bytes 002c0c91
- 00b4d98c ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 00b4d98c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d98c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d98c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4da28 ["COPY", "tmp:0:8", ["const:de0:8"]]
+ 00b4da28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4da28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4da28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4d98c bytes 08813391
+ 00b4da28 bytes 08813791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33e9504c71d8033ffe6455fb64461c38"></a>

### [`00b4d9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d9a0.md) → [`00b4da3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4da3c.md) _ZN8firebase4util6string13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4da7c",
      "incomplete_value": true,
      "site": "00b4da7c",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d9e0",
      "incomplete_value": true,
      "site": "00b4d9e0",
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
            "const:cd0:8"
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
      "definition_site": "00b4da58",
      "incomplete_value": true,
      "site": "00b4da58",
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
      "definition_site": "00b4d9bc",
      "incomplete_value": true,
      "site": "00b4d9bc",
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
      "definition_site": "00b4da60",
      "incomplete_value": false,
      "site": "00b4da74",
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
            "const:a44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d9c4",
      "incomplete_value": false,
      "site": "00b4d9d8",
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
            "const:aa0:8"
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
      "00b4da50",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4da60",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "00b4da7c",
      "WRITE",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4da50",
      "READ",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4da60",
      "PARAM",
      [
        "storage",
        "002aea44",
        null,
        "string"
      ]
    ],
    [
      "00b4da7c",
      "WRITE",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d9a0.md#insn-00b4d9d8) · [`00b4d9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d9a0.md#insn-00b4d9e0) · [`00b4d9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d9a0.md#insn-00b4d9b4)
- 新版 [`00b4da74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4da3c.md#insn-00b4da74) · [`00b4da7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4da3c.md#insn-00b4da7c) · [`00b4da50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4da3c.md#insn-00b4da50)

~~~diff
- 00b4d9d8 ["INT_ADD", "register:40f0:8", ["const:b4d9d8:8", "const:4:8"]]
- 00b4d9d8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4da74 ["INT_ADD", "register:40f0:8", ["const:b4da74:8", "const:4:8"]]
+ 00b4da74 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d9d8 bytes 4e350494
+ 00b4da74 bytes 5b350494
- 00b4d9e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
- 00b4d9e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4da7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd0:8"]]
+ 00b4da7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d9e0 bytes 806a06f9
+ 00b4da7c bytes 80ea06f9
- 00b4d9b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
- 00b4d9b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4da50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd0:8"]]
+ 00b4da50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d9b4 bytes 816a46f9
+ 00b4da50 bytes 81ea46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92f7a325387887e1ee0758f6c2e097d8"></a>

### [`00b4da10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da10.md) → [`00b4daac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4daac.md) _ZN8firebase4util6string10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4dac8",
      "incomplete_value": false,
      "site": "00b4dacc",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4da2c",
      "incomplete_value": false,
      "site": "00b4da30",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4dad8",
      "incomplete_value": true,
      "site": "00b4dae4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4da3c",
      "incomplete_value": true,
      "site": "00b4da48",
      "value": [
        "LOAD",
        "8",
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
      "00b4dac8",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4dad8",
      "DATA",
      [
        "storage",
        "01125ce8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4dac8",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4dad8",
      "DATA",
      [
        "storage",
        "01125de8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4da30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da10.md#insn-00b4da30) · [`00b4da2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da10.md#insn-00b4da2c) · [`00b4da38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da10.md#insn-00b4da38)
- 新版 [`00b4dacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4daac.md#insn-00b4dacc) · [`00b4dac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4daac.md#insn-00b4dac8) · [`00b4dad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4daac.md#insn-00b4dad4)

~~~diff
- 00b4da30 ["INT_ADD", "register:40f0:8", ["const:b4da30:8", "const:4:8"]]
- 00b4da30 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4dacc ["INT_ADD", "register:40f0:8", ["const:b4dacc:8", "const:4:8"]]
+ 00b4dacc ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4da30 bytes 74350494
+ 00b4dacc bytes 81350494
- 00b4da2c ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4da2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4da2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4da2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4dac8 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4dac8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4dac8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4dac8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4da2c bytes 00781491
+ 00b4dac8 bytes 00341591
- 00b4da38 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 00b4da38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4da38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4da38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4dad4 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 00b4dad4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4dad4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4dad4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4da38 bytes 08a13391
+ 00b4dad4 bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea858c7c667fdd4d828f20454df063e7"></a>

### [`00b4da4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da4c.md) → [`00b4dae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dae8.md) _ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4db14",
      "incomplete_value": true,
      "site": "00b4db14",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4da78",
      "incomplete_value": true,
      "site": "00b4da78",
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
            "const:cf0:8"
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
      "definition_site": "00b4dafc",
      "incomplete_value": true,
      "site": "00b4dafc",
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
      "definition_site": "00b4da60",
      "incomplete_value": true,
      "site": "00b4da60",
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
      "definition_site": "00b4db08",
      "incomplete_value": false,
      "site": "00b4db0c",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4da6c",
      "incomplete_value": false,
      "site": "00b4da70",
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
            "const:9ad:8"
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
      "00b4daf8",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db08",
      "PARAM",
      [
        "storage",
        "002b99ad",
        null,
        "string"
      ]
    ],
    [
      "00b4db14",
      "WRITE",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4daf8",
      "READ",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db08",
      "PARAM",
      [
        "storage",
        "002b9959",
        null,
        "string"
      ]
    ],
    [
      "00b4db14",
      "WRITE",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4da70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da4c.md#insn-00b4da70) · [`00b4da78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da4c.md#insn-00b4da78) · [`00b4da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da4c.md#insn-00b4da5c)
- 新版 [`00b4db0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dae8.md#insn-00b4db0c) · [`00b4db14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dae8.md#insn-00b4db14) · [`00b4daf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dae8.md#insn-00b4daf8)

~~~diff
- 00b4da70 ["INT_ADD", "register:40f0:8", ["const:b4da70:8", "const:4:8"]]
- 00b4da70 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4db0c ["INT_ADD", "register:40f0:8", ["const:b4db0c:8", "const:4:8"]]
+ 00b4db0c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4da70 bytes 28350494
+ 00b4db0c bytes 35350494
- 00b4da78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00b4da78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4db14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b4db14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4da78 bytes 607a06f9
+ 00b4db14 bytes 60fa06f9
- 00b4da5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00b4da5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4daf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b4daf8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4da5c bytes 687a46f9
+ 00b4daf8 bytes 68fa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33eee4244ac48a87955208b6974fcacb"></a>

### [`00b4da8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da8c.md) → [`00b4db28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4db28.md) _ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4db54",
      "incomplete_value": true,
      "site": "00b4db54",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dab8",
      "incomplete_value": true,
      "site": "00b4dab8",
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
            "const:cf0:8"
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
      "definition_site": "00b4db3c",
      "incomplete_value": true,
      "site": "00b4db3c",
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
      "definition_site": "00b4daa0",
      "incomplete_value": true,
      "site": "00b4daa0",
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
      "definition_site": "00b4db44",
      "incomplete_value": false,
      "site": "00b4db4c",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4daa8",
      "incomplete_value": false,
      "site": "00b4dab0",
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
            "const:9ad:8"
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
      "00b4db38",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db44",
      "PARAM",
      [
        "storage",
        "002b99ad",
        null,
        "string"
      ]
    ],
    [
      "00b4db54",
      "WRITE",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4db38",
      "READ",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db44",
      "PARAM",
      [
        "storage",
        "002b9959",
        null,
        "string"
      ]
    ],
    [
      "00b4db54",
      "WRITE",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da8c.md#insn-00b4dab0) · [`00b4dab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da8c.md#insn-00b4dab8) · [`00b4da9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da8c.md#insn-00b4da9c)
- 新版 [`00b4db4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4db28.md#insn-00b4db4c) · [`00b4db54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4db28.md#insn-00b4db54) · [`00b4db38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4db28.md#insn-00b4db38)

~~~diff
- 00b4dab0 ["INT_ADD", "register:40f0:8", ["const:b4dab0:8", "const:4:8"]]
- 00b4dab0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4db4c ["INT_ADD", "register:40f0:8", ["const:b4db4c:8", "const:4:8"]]
+ 00b4db4c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4dab0 bytes 18350494
+ 00b4db4c bytes 25350494
- 00b4dab8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00b4dab8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4db54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b4db54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4dab8 bytes 607a06f9
+ 00b4db54 bytes 60fa06f9
- 00b4da9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00b4da9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4db38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b4db38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4da9c bytes 687a46f9
+ 00b4db38 bytes 68fa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe17ddc031858901c4230e96e28a4fe3"></a>

### [`00b4dacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dacc.md) → [`00b4db68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4db68.md) _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4db98",
      "incomplete_value": true,
      "site": "00b4db98",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dafc",
      "incomplete_value": true,
      "site": "00b4dafc",
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
            "const:cf0:8"
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
      "definition_site": "00b4db7c",
      "incomplete_value": true,
      "site": "00b4db7c",
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
      "definition_site": "00b4dae0",
      "incomplete_value": true,
      "site": "00b4dae0",
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
      "definition_site": "00b4db88",
      "incomplete_value": false,
      "site": "00b4db90",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4daec",
      "incomplete_value": false,
      "site": "00b4daf4",
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
            "const:9ad:8"
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
      "00b4db78",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db88",
      "PARAM",
      [
        "storage",
        "002b99ad",
        null,
        "string"
      ]
    ],
    [
      "00b4db98",
      "WRITE",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4db78",
      "READ",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db88",
      "PARAM",
      [
        "storage",
        "002b9959",
        null,
        "string"
      ]
    ],
    [
      "00b4db98",
      "WRITE",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dacc.md#insn-00b4daf4) · [`00b4dafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dacc.md#insn-00b4dafc) · [`00b4dadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dacc.md#insn-00b4dadc)
- 新版 [`00b4db90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4db68.md#insn-00b4db90) · [`00b4db98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4db68.md#insn-00b4db98) · [`00b4db78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4db68.md#insn-00b4db78)

~~~diff
- 00b4daf4 ["INT_ADD", "register:40f0:8", ["const:b4daf4:8", "const:4:8"]]
- 00b4daf4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4db90 ["INT_ADD", "register:40f0:8", ["const:b4db90:8", "const:4:8"]]
+ 00b4db90 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4daf4 bytes 07350494
+ 00b4db90 bytes 14350494
- 00b4dafc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00b4dafc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4db98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b4db98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4dafc bytes 607a06f9
+ 00b4db98 bytes 60fa06f9
- 00b4dadc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00b4dadc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4db78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b4db78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4dadc bytes 687a46f9
+ 00b4db78 bytes 68fa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9dcc1fe4505cb2be099ffc03a0eb0b5"></a>

### [`00b4db10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4db10.md) → [`00b4dbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dbac.md) _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4dbdc",
      "incomplete_value": true,
      "site": "00b4dbdc",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4db40",
      "incomplete_value": true,
      "site": "00b4db40",
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
            "const:cf0:8"
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
      "definition_site": "00b4dbc0",
      "incomplete_value": true,
      "site": "00b4dbc0",
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
      "definition_site": "00b4db24",
      "incomplete_value": true,
      "site": "00b4db24",
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
      "definition_site": "00b4dbc8",
      "incomplete_value": false,
      "site": "00b4dbd4",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4db2c",
      "incomplete_value": false,
      "site": "00b4db38",
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
            "const:9ad:8"
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
      "00b4dbbc",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dbc8",
      "PARAM",
      [
        "storage",
        "002b99ad",
        null,
        "string"
      ]
    ],
    [
      "00b4dbdc",
      "WRITE",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dbbc",
      "READ",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dbc8",
      "PARAM",
      [
        "storage",
        "002b9959",
        null,
        "string"
      ]
    ],
    [
      "00b4dbdc",
      "WRITE",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4db38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4db10.md#insn-00b4db38) · [`00b4db40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4db10.md#insn-00b4db40) · [`00b4db20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4db10.md#insn-00b4db20)
- 新版 [`00b4dbd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dbac.md#insn-00b4dbd4) · [`00b4dbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dbac.md#insn-00b4dbdc) · [`00b4dbbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dbac.md#insn-00b4dbbc)

~~~diff
- 00b4db38 ["INT_ADD", "register:40f0:8", ["const:b4db38:8", "const:4:8"]]
- 00b4db38 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4dbd4 ["INT_ADD", "register:40f0:8", ["const:b4dbd4:8", "const:4:8"]]
+ 00b4dbd4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4db38 bytes f6340494
+ 00b4dbd4 bytes 03350494
- 00b4db40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00b4db40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dbdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b4dbdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4db40 bytes 607a06f9
+ 00b4dbdc bytes 60fa06f9
- 00b4db20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00b4db20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dbbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b4dbbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4db20 bytes 687a46f9
+ 00b4dbbc bytes 68fa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9a3600d7401079c5acc1e340775694f"></a>

### [`00b4db60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4db60.md) → [`00b4dbfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dbfc.md) _ZN8firebase4util9throwable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4dc84",
      "incomplete_value": true,
      "site": "00b4dc84",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dbe8",
      "incomplete_value": true,
      "site": "00b4dbe8",
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
            "const:cf8:8"
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
      "definition_site": "00b4dc30",
      "incomplete_value": true,
      "site": "00b4dc3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4db94",
      "incomplete_value": true,
      "site": "00b4dba0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf0:8"
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
      "00b4dc10",
      "READ",
      [
        "storage",
        "01125cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dc30",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dc84",
      "WRITE",
      [
        "storage",
        "01125cf8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4dc10",
      "READ",
      [
        "storage",
        "01125df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dc30",
      "READ",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dc84",
      "WRITE",
      [
        "storage",
        "01125df8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4db60.md#insn-00b4dba0) · [`00b4dbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4db60.md#insn-00b4dbe8) · [`00b4db74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4db60.md#insn-00b4db74)
- 新版 [`00b4dc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dbfc.md#insn-00b4dc3c) · [`00b4dc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dbfc.md#insn-00b4dc84) · [`00b4dc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dbfc.md#insn-00b4dc10)

~~~diff
- 00b4dba0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4dba0 ["INT_ADD", "register:40f0:8", ["const:b4dba0:8", "const:4:8"]]
- 00b4dba0 ["CALLIND", null, ["register:0:8"]]
+ 00b4dc3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4dc3c ["INT_ADD", "register:40f0:8", ["const:b4dc3c:8", "const:4:8"]]
+ 00b4dc3c ["CALLIND", null, ["register:0:8"]]
- 00b4dba0 bytes 00013fd6
+ 00b4dc3c bytes 00013fd6
- 00b4dbe8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4dbe8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:cf8:8"]]
- 00b4dbe8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4dc84 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4dc84 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:df8:8"]]
+ 00b4dc84 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4dbe8 bytes a0e23339
+ 00b4dc84 bytes a0e23739
- 00b4db74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cf8:8"]]
- 00b4db74 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4db74 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4dc10 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:df8:8"]]
+ 00b4dc10 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dc10 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4db74 bytes a8e27339
+ 00b4dc10 bytes a8e27739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2ad815a20f1e23f7d7e4f19189fac43"></a>

### [`00b4dbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dbfc.md) → [`00b4dc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dc98.md) _ZN8firebase4util9throwable12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00b4dcd4",
      "incomplete_value": true,
      "site": "00b4dcd4",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dc38",
      "incomplete_value": true,
      "site": "00b4dc38",
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
            "const:cf8:8"
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
      "definition_site": "00b4dd24",
      "incomplete_value": true,
      "site": "00b4dd24",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dc88",
      "incomplete_value": true,
      "site": "00b4dc88",
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
            "const:cf0:8"
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
      "definition_site": "00b4dcb0",
      "incomplete_value": true,
      "site": "00b4dcb0",
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
      "definition_site": "00b4dc14",
      "incomplete_value": true,
      "site": "00b4dc14",
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
      "00b4dcac",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dcb8",
      "READ",
      [
        "storage",
        "01125cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dcd4",
      "WRITE",
      [
        "storage",
        "01125cf8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4dcac",
      "READ",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dcb8",
      "READ",
      [
        "storage",
        "01125df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dcd4",
      "WRITE",
      [
        "storage",
        "01125df8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dbfc.md#insn-00b4dc38) · [`00b4dc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dbfc.md#insn-00b4dc84) · [`00b4dc88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dbfc.md#insn-00b4dc88)
- 新版 [`00b4dcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dc98.md#insn-00b4dcd4) · [`00b4dd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dc98.md#insn-00b4dd20) · [`00b4dd24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dc98.md#insn-00b4dd24)

~~~diff
- 00b4dc38 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4dc38 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4dc38 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:cf8:8"]]
- 00b4dc38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4dcd4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4dcd4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4dcd4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:df8:8"]]
+ 00b4dcd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4dc38 bytes bfe23339
+ 00b4dcd4 bytes bfe23739
- 00b4dc84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4dc84 ["INT_ADD", "register:40f0:8", ["const:b4dc84:8", "const:4:8"]]
- 00b4dc84 ["CALLIND", null, ["register:0:8"]]
+ 00b4dd20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4dd20 ["INT_ADD", "register:40f0:8", ["const:b4dd20:8", "const:4:8"]]
+ 00b4dd20 ["CALLIND", null, ["register:0:8"]]
- 00b4dc84 bytes 00013fd6
+ 00b4dd20 bytes 00013fd6
- 00b4dc88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
- 00b4dc88 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4dc88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4dd24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
+ 00b4dd24 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4dd24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4dc88 bytes 9f7a06f9
+ 00b4dd24 bytes 9ffa06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb20efd2a2b7b62a34b044ced61b75dc"></a>

### [`00b4dc9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dc9c.md) → [`00b4dd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dd38.md) _ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4dd78",
      "incomplete_value": true,
      "site": "00b4dd78",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dcdc",
      "incomplete_value": true,
      "site": "00b4dcdc",
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
            "const:cf0:8"
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
      "definition_site": "00b4dd54",
      "incomplete_value": true,
      "site": "00b4dd54",
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
      "definition_site": "00b4dcb8",
      "incomplete_value": true,
      "site": "00b4dcb8",
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
      "definition_site": "00b4dd5c",
      "incomplete_value": false,
      "site": "00b4dd70",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dcc0",
      "incomplete_value": false,
      "site": "00b4dcd4",
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
            "const:9ad:8"
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
      "00b4dd4c",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dd5c",
      "PARAM",
      [
        "storage",
        "002b99ad",
        null,
        "string"
      ]
    ],
    [
      "00b4dd78",
      "WRITE",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dd4c",
      "READ",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dd5c",
      "PARAM",
      [
        "storage",
        "002b9959",
        null,
        "string"
      ]
    ],
    [
      "00b4dd78",
      "WRITE",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dc9c.md#insn-00b4dcd4) · [`00b4dcdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dc9c.md#insn-00b4dcdc) · [`00b4dcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dc9c.md#insn-00b4dcb0)
- 新版 [`00b4dd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dd38.md#insn-00b4dd70) · [`00b4dd78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dd38.md#insn-00b4dd78) · [`00b4dd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dd38.md#insn-00b4dd4c)

~~~diff
- 00b4dcd4 ["INT_ADD", "register:40f0:8", ["const:b4dcd4:8", "const:4:8"]]
- 00b4dcd4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4dd70 ["INT_ADD", "register:40f0:8", ["const:b4dd70:8", "const:4:8"]]
+ 00b4dd70 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4dcd4 bytes 8f340494
+ 00b4dd70 bytes 9c340494
- 00b4dcdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
- 00b4dcdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dd78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
+ 00b4dd78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4dcdc bytes 807a06f9
+ 00b4dd78 bytes 80fa06f9
- 00b4dcb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
- 00b4dcb0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dd4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
+ 00b4dd4c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4dcb0 bytes 817a46f9
+ 00b4dd4c bytes 81fa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f86a7b0173c9c14851242b3107e81d23"></a>

### [`00b4dd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dd0c.md) → [`00b4dda8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dda8.md) _ZN8firebase4util9throwable11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4ddc4",
      "incomplete_value": false,
      "site": "00b4ddc8",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dd28",
      "incomplete_value": false,
      "site": "00b4dd2c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4ddd4",
      "incomplete_value": true,
      "site": "00b4dde0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4dd38",
      "incomplete_value": true,
      "site": "00b4dd44",
      "value": [
        "LOAD",
        "8",
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
      "00b4ddc4",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4ddd4",
      "DATA",
      [
        "storage",
        "01125d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ddc4",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4ddd4",
      "DATA",
      [
        "storage",
        "01125e00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dd2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dd0c.md#insn-00b4dd2c) · [`00b4dd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dd0c.md#insn-00b4dd28) · [`00b4dd34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dd0c.md#insn-00b4dd34)
- 新版 [`00b4ddc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dda8.md#insn-00b4ddc8) · [`00b4ddc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dda8.md#insn-00b4ddc4) · [`00b4ddd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dda8.md#insn-00b4ddd0)

~~~diff
- 00b4dd2c ["INT_ADD", "register:40f0:8", ["const:b4dd2c:8", "const:4:8"]]
- 00b4dd2c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4ddc8 ["INT_ADD", "register:40f0:8", ["const:b4ddc8:8", "const:4:8"]]
+ 00b4ddc8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4dd2c bytes b5340494
+ 00b4ddc8 bytes c2340494
- 00b4dd28 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4dd28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4dd28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4dd28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ddc4 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4ddc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ddc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ddc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4dd28 bytes 009c0d91
+ 00b4ddc4 bytes 002c0c91
- 00b4dd34 ["COPY", "tmp:0:8", ["const:d00:8"]]
- 00b4dd34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4dd34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4dd34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4ddd0 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 00b4ddd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4ddd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4ddd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4dd34 bytes 08013491
+ 00b4ddd0 bytes 08013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfc36090cd667ccc710365703efc07f6"></a>

### [`00b4dd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dd48.md) → [`00b4dde4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dde4.md) _ZN8firebase4util9throwable13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4de24",
      "incomplete_value": true,
      "site": "00b4de24",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dd88",
      "incomplete_value": true,
      "site": "00b4dd88",
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
            "const:cf0:8"
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
      "definition_site": "00b4de00",
      "incomplete_value": true,
      "site": "00b4de00",
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
      "definition_site": "00b4dd64",
      "incomplete_value": true,
      "site": "00b4dd64",
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
      "definition_site": "00b4de08",
      "incomplete_value": false,
      "site": "00b4de1c",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dd6c",
      "incomplete_value": false,
      "site": "00b4dd80",
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
            "const:9ad:8"
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
      "00b4ddf8",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de08",
      "PARAM",
      [
        "storage",
        "002b99ad",
        null,
        "string"
      ]
    ],
    [
      "00b4de24",
      "WRITE",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ddf8",
      "READ",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de08",
      "PARAM",
      [
        "storage",
        "002b9959",
        null,
        "string"
      ]
    ],
    [
      "00b4de24",
      "WRITE",
      [
        "storage",
        "01125df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dd48.md#insn-00b4dd80) · [`00b4dd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dd48.md#insn-00b4dd88) · [`00b4dd5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dd48.md#insn-00b4dd5c)
- 新版 [`00b4de1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dde4.md#insn-00b4de1c) · [`00b4de24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dde4.md#insn-00b4de24) · [`00b4ddf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dde4.md#insn-00b4ddf8)

~~~diff
- 00b4dd80 ["INT_ADD", "register:40f0:8", ["const:b4dd80:8", "const:4:8"]]
- 00b4dd80 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4de1c ["INT_ADD", "register:40f0:8", ["const:b4de1c:8", "const:4:8"]]
+ 00b4de1c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4dd80 bytes 64340494
+ 00b4de1c bytes 71340494
- 00b4dd88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
- 00b4dd88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4de24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
+ 00b4de24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4dd88 bytes 807a06f9
+ 00b4de24 bytes 80fa06f9
- 00b4dd5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
- 00b4dd5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ddf8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
+ 00b4ddf8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4dd5c bytes 817a46f9
+ 00b4ddf8 bytes 81fa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c84b432cbe58d0e4de2ae54564ced5b"></a>

### [`00b4ddb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4ddb8.md) → [`00b4de54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4de54.md) _ZN8firebase4util9throwable10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4de70",
      "incomplete_value": false,
      "site": "00b4de74",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ddd4",
      "incomplete_value": false,
      "site": "00b4ddd8",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4de80",
      "incomplete_value": true,
      "site": "00b4de8c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4dde4",
      "incomplete_value": true,
      "site": "00b4ddf0",
      "value": [
        "LOAD",
        "8",
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
      "00b4de70",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4de80",
      "DATA",
      [
        "storage",
        "01125d18",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4de70",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4de80",
      "DATA",
      [
        "storage",
        "01125e18",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4ddb8.md#insn-00b4ddd8) · [`00b4ddd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4ddb8.md#insn-00b4ddd4) · [`00b4dde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4ddb8.md#insn-00b4dde0)
- 新版 [`00b4de74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4de54.md#insn-00b4de74) · [`00b4de70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4de54.md#insn-00b4de70) · [`00b4de7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4de54.md#insn-00b4de7c)

~~~diff
- 00b4ddd8 ["INT_ADD", "register:40f0:8", ["const:b4ddd8:8", "const:4:8"]]
- 00b4ddd8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4de74 ["INT_ADD", "register:40f0:8", ["const:b4de74:8", "const:4:8"]]
+ 00b4de74 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4ddd8 bytes 8a340494
+ 00b4de74 bytes 97340494
- 00b4ddd4 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4ddd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ddd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ddd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4de70 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4de70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4de70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4de70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4ddd4 bytes 00781491
+ 00b4de70 bytes 00341591
- 00b4dde0 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 00b4dde0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4dde0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4dde0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4de7c ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 00b4de7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4de7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4de7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4dde0 bytes 08613491
+ 00b4de7c bytes 08613891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a47bbf6d0122b5e2ad78a0431e056f95"></a>

### [`00b4ddf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4ddf4.md) → [`00b4de90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4de90.md) _ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4debc",
      "incomplete_value": true,
      "site": "00b4debc",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4de20",
      "incomplete_value": true,
      "site": "00b4de20",
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
            "const:d20:8"
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
      "definition_site": "00b4dea4",
      "incomplete_value": true,
      "site": "00b4dea4",
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
      "definition_site": "00b4de08",
      "incomplete_value": true,
      "site": "00b4de08",
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
      "definition_site": "00b4deb0",
      "incomplete_value": false,
      "site": "00b4deb4",
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
            "const:119:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4de14",
      "incomplete_value": false,
      "site": "00b4de18",
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
            "const:175:8"
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
      "00b4dea0",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4deb0",
      "PARAM",
      [
        "storage",
        "002a7175",
        null,
        "string"
      ]
    ],
    [
      "00b4debc",
      "WRITE",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dea0",
      "READ",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4deb0",
      "PARAM",
      [
        "storage",
        "002a7119",
        null,
        "string"
      ]
    ],
    [
      "00b4debc",
      "WRITE",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4de18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4ddf4.md#insn-00b4de18) · [`00b4de20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4ddf4.md#insn-00b4de20) · [`00b4de04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4ddf4.md#insn-00b4de04)
- 新版 [`00b4deb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4de90.md#insn-00b4deb4) · [`00b4debc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4de90.md#insn-00b4debc) · [`00b4dea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4de90.md#insn-00b4dea0)

~~~diff
- 00b4de18 ["INT_ADD", "register:40f0:8", ["const:b4de18:8", "const:4:8"]]
- 00b4de18 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4deb4 ["INT_ADD", "register:40f0:8", ["const:b4deb4:8", "const:4:8"]]
+ 00b4deb4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4de18 bytes 3e340494
+ 00b4deb4 bytes 4b340494
- 00b4de20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00b4de20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4debc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00b4debc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4de20 bytes 609206f9
+ 00b4debc bytes 601207f9
- 00b4de04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00b4de04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dea0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00b4dea0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4de04 bytes 689246f9
+ 00b4dea0 bytes 681247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32ec96074851a83574d7bcc931dba312"></a>

### [`00b4de34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4de34.md) → [`00b4ded0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4ded0.md) _ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4defc",
      "incomplete_value": true,
      "site": "00b4defc",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4de60",
      "incomplete_value": true,
      "site": "00b4de60",
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
            "const:d20:8"
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
      "definition_site": "00b4dee4",
      "incomplete_value": true,
      "site": "00b4dee4",
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
      "definition_site": "00b4de48",
      "incomplete_value": true,
      "site": "00b4de48",
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
      "definition_site": "00b4deec",
      "incomplete_value": false,
      "site": "00b4def4",
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
            "const:119:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4de50",
      "incomplete_value": false,
      "site": "00b4de58",
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
            "const:175:8"
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
      "00b4dee0",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4deec",
      "PARAM",
      [
        "storage",
        "002a7175",
        null,
        "string"
      ]
    ],
    [
      "00b4defc",
      "WRITE",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dee0",
      "READ",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4deec",
      "PARAM",
      [
        "storage",
        "002a7119",
        null,
        "string"
      ]
    ],
    [
      "00b4defc",
      "WRITE",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4de58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4de34.md#insn-00b4de58) · [`00b4de60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4de34.md#insn-00b4de60) · [`00b4de44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4de34.md#insn-00b4de44)
- 新版 [`00b4def4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4ded0.md#insn-00b4def4) · [`00b4defc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4ded0.md#insn-00b4defc) · [`00b4dee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4ded0.md#insn-00b4dee0)

~~~diff
- 00b4de58 ["INT_ADD", "register:40f0:8", ["const:b4de58:8", "const:4:8"]]
- 00b4de58 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4def4 ["INT_ADD", "register:40f0:8", ["const:b4def4:8", "const:4:8"]]
+ 00b4def4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4de58 bytes 2e340494
+ 00b4def4 bytes 3b340494
- 00b4de60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00b4de60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4defc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00b4defc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4de60 bytes 609206f9
+ 00b4defc bytes 601207f9
- 00b4de44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00b4de44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dee0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00b4dee0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4de44 bytes 689246f9
+ 00b4dee0 bytes 681247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a677de2458b6603761e7fa1a40f0ec17"></a>

### [`00b4de74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4de74.md) → [`00b4df10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4df10.md) _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4df40",
      "incomplete_value": true,
      "site": "00b4df40",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dea4",
      "incomplete_value": true,
      "site": "00b4dea4",
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
            "const:d20:8"
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
      "definition_site": "00b4df24",
      "incomplete_value": true,
      "site": "00b4df24",
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
      "definition_site": "00b4de88",
      "incomplete_value": true,
      "site": "00b4de88",
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
      "definition_site": "00b4df30",
      "incomplete_value": false,
      "site": "00b4df38",
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
            "const:119:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4de94",
      "incomplete_value": false,
      "site": "00b4de9c",
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
            "const:175:8"
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
      "00b4df20",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4df30",
      "PARAM",
      [
        "storage",
        "002a7175",
        null,
        "string"
      ]
    ],
    [
      "00b4df40",
      "WRITE",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4df20",
      "READ",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4df30",
      "PARAM",
      [
        "storage",
        "002a7119",
        null,
        "string"
      ]
    ],
    [
      "00b4df40",
      "WRITE",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4de9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4de74.md#insn-00b4de9c) · [`00b4dea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4de74.md#insn-00b4dea4) · [`00b4de84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4de74.md#insn-00b4de84)
- 新版 [`00b4df38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4df10.md#insn-00b4df38) · [`00b4df40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4df10.md#insn-00b4df40) · [`00b4df20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4df10.md#insn-00b4df20)

~~~diff
- 00b4de9c ["INT_ADD", "register:40f0:8", ["const:b4de9c:8", "const:4:8"]]
- 00b4de9c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4df38 ["INT_ADD", "register:40f0:8", ["const:b4df38:8", "const:4:8"]]
+ 00b4df38 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4de9c bytes 1d340494
+ 00b4df38 bytes 2a340494
- 00b4dea4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00b4dea4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4df40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00b4df40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4dea4 bytes 609206f9
+ 00b4df40 bytes 601207f9
- 00b4de84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00b4de84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4df20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00b4df20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4de84 bytes 689246f9
+ 00b4df20 bytes 681247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70c786499e58e25ededddd6f3188eeea"></a>

### [`00b4deb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4deb8.md) → [`00b4df54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4df54.md) _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4df84",
      "incomplete_value": true,
      "site": "00b4df84",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dee8",
      "incomplete_value": true,
      "site": "00b4dee8",
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
            "const:d20:8"
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
      "definition_site": "00b4df68",
      "incomplete_value": true,
      "site": "00b4df68",
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
      "definition_site": "00b4decc",
      "incomplete_value": true,
      "site": "00b4decc",
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
      "definition_site": "00b4df70",
      "incomplete_value": false,
      "site": "00b4df7c",
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
            "const:119:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ded4",
      "incomplete_value": false,
      "site": "00b4dee0",
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
            "const:175:8"
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
      "00b4df64",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4df70",
      "PARAM",
      [
        "storage",
        "002a7175",
        null,
        "string"
      ]
    ],
    [
      "00b4df84",
      "WRITE",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4df64",
      "READ",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4df70",
      "PARAM",
      [
        "storage",
        "002a7119",
        null,
        "string"
      ]
    ],
    [
      "00b4df84",
      "WRITE",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4deb8.md#insn-00b4dee0) · [`00b4dee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4deb8.md#insn-00b4dee8) · [`00b4dec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4deb8.md#insn-00b4dec8)
- 新版 [`00b4df7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4df54.md#insn-00b4df7c) · [`00b4df84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4df54.md#insn-00b4df84) · [`00b4df64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4df54.md#insn-00b4df64)

~~~diff
- 00b4dee0 ["INT_ADD", "register:40f0:8", ["const:b4dee0:8", "const:4:8"]]
- 00b4dee0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4df7c ["INT_ADD", "register:40f0:8", ["const:b4df7c:8", "const:4:8"]]
+ 00b4df7c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4dee0 bytes 0c340494
+ 00b4df7c bytes 19340494
- 00b4dee8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00b4dee8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4df84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00b4df84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4dee8 bytes 609206f9
+ 00b4df84 bytes 601207f9
- 00b4dec8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00b4dec8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4df64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00b4df64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4dec8 bytes 689246f9
+ 00b4df64 bytes 681247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cbbdf46a2f2dc46737ad46059f6035f"></a>

### [`00b4df08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4df08.md) → [`00b4dfa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dfa4.md) _ZN8firebase4util3uri15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4e02c",
      "incomplete_value": true,
      "site": "00b4e02c",
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
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4df90",
      "incomplete_value": true,
      "site": "00b4df90",
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
            "const:d28:8"
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
      "definition_site": "00b4dfd8",
      "incomplete_value": true,
      "site": "00b4dfe4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4df3c",
      "incomplete_value": true,
      "site": "00b4df48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d20:8"
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
      "00b4dfb8",
      "READ",
      [
        "storage",
        "01125d28",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dfd8",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e02c",
      "WRITE",
      [
        "storage",
        "01125d28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4dfb8",
      "READ",
      [
        "storage",
        "01125e28",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dfd8",
      "READ",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e02c",
      "WRITE",
      [
        "storage",
        "01125e28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4df48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4df08.md#insn-00b4df48) · [`00b4df90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4df08.md#insn-00b4df90) · [`00b4df1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4df08.md#insn-00b4df1c)
- 新版 [`00b4dfe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dfa4.md#insn-00b4dfe4) · [`00b4e02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dfa4.md#insn-00b4e02c) · [`00b4dfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4dfa4.md#insn-00b4dfb8)

~~~diff
- 00b4df48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4df48 ["INT_ADD", "register:40f0:8", ["const:b4df48:8", "const:4:8"]]
- 00b4df48 ["CALLIND", null, ["register:0:8"]]
+ 00b4dfe4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4dfe4 ["INT_ADD", "register:40f0:8", ["const:b4dfe4:8", "const:4:8"]]
+ 00b4dfe4 ["CALLIND", null, ["register:0:8"]]
- 00b4df48 bytes 00013fd6
+ 00b4dfe4 bytes 00013fd6
- 00b4df90 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4df90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d28:8"]]
- 00b4df90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4e02c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4e02c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e28:8"]]
+ 00b4e02c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4df90 bytes a0a23439
+ 00b4e02c bytes a0a23839
- 00b4df1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d28:8"]]
- 00b4df1c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4df1c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4dfb8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e28:8"]]
+ 00b4dfb8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dfb8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4df1c bytes a8a27439
+ 00b4dfb8 bytes a8a27839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-470ef0f3a30fe4aaaf6a2c6e784172fd"></a>

### [`00b4dfa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dfa4.md) → [`00b4e040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e040.md) _ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00b4e07c",
      "incomplete_value": true,
      "site": "00b4e07c",
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
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dfe0",
      "incomplete_value": true,
      "site": "00b4dfe0",
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
            "const:d28:8"
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
      "definition_site": "00b4e0cc",
      "incomplete_value": true,
      "site": "00b4e0cc",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e030",
      "incomplete_value": true,
      "site": "00b4e030",
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
            "const:d20:8"
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
      "definition_site": "00b4e058",
      "incomplete_value": true,
      "site": "00b4e058",
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
      "definition_site": "00b4dfbc",
      "incomplete_value": true,
      "site": "00b4dfbc",
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
      "00b4e054",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e060",
      "READ",
      [
        "storage",
        "01125d28",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4e07c",
      "WRITE",
      [
        "storage",
        "01125d28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4e054",
      "READ",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e060",
      "READ",
      [
        "storage",
        "01125e28",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4e07c",
      "WRITE",
      [
        "storage",
        "01125e28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dfa4.md#insn-00b4dfe0) · [`00b4e02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dfa4.md#insn-00b4e02c) · [`00b4e030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dfa4.md#insn-00b4e030)
- 新版 [`00b4e07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e040.md#insn-00b4e07c) · [`00b4e0c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e040.md#insn-00b4e0c8) · [`00b4e0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e040.md#insn-00b4e0cc)

~~~diff
- 00b4dfe0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4dfe0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4dfe0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d28:8"]]
- 00b4dfe0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4e07c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4e07c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4e07c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e28:8"]]
+ 00b4e07c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4dfe0 bytes bfa23439
+ 00b4e07c bytes bfa23839
- 00b4e02c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4e02c ["INT_ADD", "register:40f0:8", ["const:b4e02c:8", "const:4:8"]]
- 00b4e02c ["CALLIND", null, ["register:0:8"]]
+ 00b4e0c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4e0c8 ["INT_ADD", "register:40f0:8", ["const:b4e0c8:8", "const:4:8"]]
+ 00b4e0c8 ["CALLIND", null, ["register:0:8"]]
- 00b4e02c bytes 00013fd6
+ 00b4e0c8 bytes 00013fd6
- 00b4e030 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
- 00b4e030 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4e030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4e0cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e20:8"]]
+ 00b4e0cc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4e0cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4e030 bytes 9f9206f9
+ 00b4e0cc bytes 9f1207f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-349a7ce01d6d3b4e32a6116ae9e85867"></a>

### [`00b4e044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e044.md) → [`00b4e0e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e0e0.md) _ZN8firebase4util3uri14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4e120",
      "incomplete_value": true,
      "site": "00b4e120",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e084",
      "incomplete_value": true,
      "site": "00b4e084",
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
            "const:d20:8"
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
      "definition_site": "00b4e0fc",
      "incomplete_value": true,
      "site": "00b4e0fc",
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
      "definition_site": "00b4e060",
      "incomplete_value": true,
      "site": "00b4e060",
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
      "definition_site": "00b4e104",
      "incomplete_value": false,
      "site": "00b4e118",
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
            "const:119:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e068",
      "incomplete_value": false,
      "site": "00b4e07c",
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
            "const:175:8"
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
      "00b4e0f4",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e104",
      "PARAM",
      [
        "storage",
        "002a7175",
        null,
        "string"
      ]
    ],
    [
      "00b4e120",
      "WRITE",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e0f4",
      "READ",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e104",
      "PARAM",
      [
        "storage",
        "002a7119",
        null,
        "string"
      ]
    ],
    [
      "00b4e120",
      "WRITE",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e044.md#insn-00b4e07c) · [`00b4e084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e044.md#insn-00b4e084) · [`00b4e058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e044.md#insn-00b4e058)
- 新版 [`00b4e118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e0e0.md#insn-00b4e118) · [`00b4e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e0e0.md#insn-00b4e120) · [`00b4e0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e0e0.md#insn-00b4e0f4)

~~~diff
- 00b4e07c ["INT_ADD", "register:40f0:8", ["const:b4e07c:8", "const:4:8"]]
- 00b4e07c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4e118 ["INT_ADD", "register:40f0:8", ["const:b4e118:8", "const:4:8"]]
+ 00b4e118 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4e07c bytes a5330494
+ 00b4e118 bytes b2330494
- 00b4e084 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
- 00b4e084 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e120 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e20:8"]]
+ 00b4e120 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4e084 bytes 809206f9
+ 00b4e120 bytes 801207f9
- 00b4e058 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
- 00b4e058 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e0f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e20:8"]]
+ 00b4e0f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4e058 bytes 819246f9
+ 00b4e0f4 bytes 811247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a335735d17ca1777d28972a36977f0da"></a>

### [`00b4e0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e0b4.md) → [`00b4e150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e150.md) _ZN8firebase4util3uri11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4e16c",
      "incomplete_value": false,
      "site": "00b4e170",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e0d0",
      "incomplete_value": false,
      "site": "00b4e0d4",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4e17c",
      "incomplete_value": true,
      "site": "00b4e188",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4e0e0",
      "incomplete_value": true,
      "site": "00b4e0ec",
      "value": [
        "LOAD",
        "8",
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
      "00b4e16c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4e17c",
      "DATA",
      [
        "storage",
        "01125d30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e16c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4e17c",
      "DATA",
      [
        "storage",
        "01125e30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e0b4.md#insn-00b4e0d4) · [`00b4e0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e0b4.md#insn-00b4e0d0) · [`00b4e0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e0b4.md#insn-00b4e0dc)
- 新版 [`00b4e170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e150.md#insn-00b4e170) · [`00b4e16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e150.md#insn-00b4e16c) · [`00b4e178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e150.md#insn-00b4e178)

~~~diff
- 00b4e0d4 ["INT_ADD", "register:40f0:8", ["const:b4e0d4:8", "const:4:8"]]
- 00b4e0d4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4e170 ["INT_ADD", "register:40f0:8", ["const:b4e170:8", "const:4:8"]]
+ 00b4e170 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4e0d4 bytes cb330494
+ 00b4e170 bytes d8330494
- 00b4e0d0 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4e0d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4e0d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4e0d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4e16c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4e16c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4e16c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4e16c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4e0d0 bytes 009c0d91
+ 00b4e16c bytes 002c0c91
- 00b4e0dc ["COPY", "tmp:0:8", ["const:d30:8"]]
- 00b4e0dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4e0dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4e0dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4e178 ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 00b4e178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4e178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4e178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4e0dc bytes 08c13491
+ 00b4e178 bytes 08c13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfbf585d9c1d7d461045989b60349ffb"></a>

### [`00b4e0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e0f0.md) → [`00b4e18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e18c.md) _ZN8firebase4util3uri13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4e1cc",
      "incomplete_value": true,
      "site": "00b4e1cc",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e130",
      "incomplete_value": true,
      "site": "00b4e130",
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
            "const:d20:8"
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
      "definition_site": "00b4e1a8",
      "incomplete_value": true,
      "site": "00b4e1a8",
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
      "definition_site": "00b4e10c",
      "incomplete_value": true,
      "site": "00b4e10c",
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
      "definition_site": "00b4e1b0",
      "incomplete_value": false,
      "site": "00b4e1c4",
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
            "const:119:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e114",
      "incomplete_value": false,
      "site": "00b4e128",
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
            "const:175:8"
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
      "00b4e1a0",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e1b0",
      "PARAM",
      [
        "storage",
        "002a7175",
        null,
        "string"
      ]
    ],
    [
      "00b4e1cc",
      "WRITE",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e1a0",
      "READ",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e1b0",
      "PARAM",
      [
        "storage",
        "002a7119",
        null,
        "string"
      ]
    ],
    [
      "00b4e1cc",
      "WRITE",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e0f0.md#insn-00b4e128) · [`00b4e130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e0f0.md#insn-00b4e130) · [`00b4e104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e0f0.md#insn-00b4e104)
- 新版 [`00b4e1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e18c.md#insn-00b4e1c4) · [`00b4e1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e18c.md#insn-00b4e1cc) · [`00b4e1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e18c.md#insn-00b4e1a0)

~~~diff
- 00b4e128 ["INT_ADD", "register:40f0:8", ["const:b4e128:8", "const:4:8"]]
- 00b4e128 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4e1c4 ["INT_ADD", "register:40f0:8", ["const:b4e1c4:8", "const:4:8"]]
+ 00b4e1c4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4e128 bytes 7a330494
+ 00b4e1c4 bytes 87330494
- 00b4e130 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
- 00b4e130 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e1cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e20:8"]]
+ 00b4e1cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4e130 bytes 809206f9
+ 00b4e1cc bytes 801207f9
- 00b4e104 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
- 00b4e104 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e1a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e20:8"]]
+ 00b4e1a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4e104 bytes 819246f9
+ 00b4e1a0 bytes 811247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b86632f992e48ae6a494aa31fe9a453"></a>

### [`00b4e160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e160.md) → [`00b4e1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e1fc.md) _ZN8firebase4util3uri10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4e218",
      "incomplete_value": false,
      "site": "00b4e21c",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e17c",
      "incomplete_value": false,
      "site": "00b4e180",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4e228",
      "incomplete_value": true,
      "site": "00b4e234",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4e18c",
      "incomplete_value": true,
      "site": "00b4e198",
      "value": [
        "LOAD",
        "8",
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
      "00b4e218",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4e228",
      "DATA",
      [
        "storage",
        "01125d40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4e218",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4e228",
      "DATA",
      [
        "storage",
        "01125e40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e160.md#insn-00b4e180) · [`00b4e17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e160.md#insn-00b4e17c) · [`00b4e188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e160.md#insn-00b4e188)
- 新版 [`00b4e21c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e1fc.md#insn-00b4e21c) · [`00b4e218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e1fc.md#insn-00b4e218) · [`00b4e224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e1fc.md#insn-00b4e224)

~~~diff
- 00b4e180 ["INT_ADD", "register:40f0:8", ["const:b4e180:8", "const:4:8"]]
- 00b4e180 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4e21c ["INT_ADD", "register:40f0:8", ["const:b4e21c:8", "const:4:8"]]
+ 00b4e21c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4e180 bytes a0330494
+ 00b4e21c bytes ad330494
- 00b4e17c ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4e17c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4e17c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4e17c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4e218 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4e218 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4e218 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4e218 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4e17c bytes 00781491
+ 00b4e218 bytes 00341591
- 00b4e188 ["COPY", "tmp:0:8", ["const:d40:8"]]
- 00b4e188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4e188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4e188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4e224 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 00b4e224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4e224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4e224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4e188 bytes 08013591
+ 00b4e224 bytes 08013991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-618531e74a795f5f70885082448bfa07"></a>

### [`00b4e19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e19c.md) → [`00b4e238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e238.md) _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4e264",
      "incomplete_value": true,
      "site": "00b4e264",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e1c8",
      "incomplete_value": true,
      "site": "00b4e1c8",
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
            "const:d48:8"
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
      "definition_site": "00b4e24c",
      "incomplete_value": true,
      "site": "00b4e24c",
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
      "definition_site": "00b4e1b0",
      "incomplete_value": true,
      "site": "00b4e1b0",
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
      "definition_site": "00b4e258",
      "incomplete_value": false,
      "site": "00b4e25c",
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
            "const:f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e1bc",
      "incomplete_value": false,
      "site": "00b4e1c0",
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
            "const:151:8"
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
      "00b4e248",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e258",
      "PARAM",
      [
        "storage",
        "002ae151",
        null,
        "string"
      ]
    ],
    [
      "00b4e264",
      "WRITE",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e248",
      "READ",
      [
        "storage",
        "01125e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e258",
      "PARAM",
      [
        "storage",
        "002ae0f5",
        null,
        "string"
      ]
    ],
    [
      "00b4e264",
      "WRITE",
      [
        "storage",
        "01125e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e19c.md#insn-00b4e1c0) · [`00b4e1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e19c.md#insn-00b4e1c8) · [`00b4e1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e19c.md#insn-00b4e1ac)
- 新版 [`00b4e25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e238.md#insn-00b4e25c) · [`00b4e264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e238.md#insn-00b4e264) · [`00b4e248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e238.md#insn-00b4e248)

~~~diff
- 00b4e1c0 ["INT_ADD", "register:40f0:8", ["const:b4e1c0:8", "const:4:8"]]
- 00b4e1c0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4e25c ["INT_ADD", "register:40f0:8", ["const:b4e25c:8", "const:4:8"]]
+ 00b4e25c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4e1c0 bytes 54330494
+ 00b4e25c bytes 61330494
- 00b4e1c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00b4e1c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e264 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b4e264 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4e1c8 bytes 60a606f9
+ 00b4e264 bytes 602607f9
- 00b4e1ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00b4e1ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e248 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b4e248 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4e1ac bytes 68a646f9
+ 00b4e248 bytes 682647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83d4f3bbf663ee5f0f543abf676f5217"></a>

### [`00b4e1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e1dc.md) → [`00b4e278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e278.md) _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4e2a4",
      "incomplete_value": true,
      "site": "00b4e2a4",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e208",
      "incomplete_value": true,
      "site": "00b4e208",
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
            "const:d48:8"
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
      "definition_site": "00b4e28c",
      "incomplete_value": true,
      "site": "00b4e28c",
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
      "definition_site": "00b4e1f0",
      "incomplete_value": true,
      "site": "00b4e1f0",
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
      "definition_site": "00b4e294",
      "incomplete_value": false,
      "site": "00b4e29c",
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
            "const:f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e1f8",
      "incomplete_value": false,
      "site": "00b4e200",
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
            "const:151:8"
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
      "00b4e288",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e294",
      "PARAM",
      [
        "storage",
        "002ae151",
        null,
        "string"
      ]
    ],
    [
      "00b4e2a4",
      "WRITE",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e288",
      "READ",
      [
        "storage",
        "01125e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e294",
      "PARAM",
      [
        "storage",
        "002ae0f5",
        null,
        "string"
      ]
    ],
    [
      "00b4e2a4",
      "WRITE",
      [
        "storage",
        "01125e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e1dc.md#insn-00b4e200) · [`00b4e208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e1dc.md#insn-00b4e208) · [`00b4e1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e1dc.md#insn-00b4e1ec)
- 新版 [`00b4e29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e278.md#insn-00b4e29c) · [`00b4e2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e278.md#insn-00b4e2a4) · [`00b4e288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e278.md#insn-00b4e288)

~~~diff
- 00b4e200 ["INT_ADD", "register:40f0:8", ["const:b4e200:8", "const:4:8"]]
- 00b4e200 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4e29c ["INT_ADD", "register:40f0:8", ["const:b4e29c:8", "const:4:8"]]
+ 00b4e29c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4e200 bytes 44330494
+ 00b4e29c bytes 51330494
- 00b4e208 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00b4e208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e2a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b4e2a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4e208 bytes 60a606f9
+ 00b4e2a4 bytes 602607f9
- 00b4e1ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00b4e1ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e288 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b4e288 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4e1ec bytes 68a646f9
+ 00b4e288 bytes 682647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81e3de74135d60a91facbe83d8cba3c1"></a>

### [`00b4e21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e21c.md) → [`00b4e2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e2b8.md) _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4e2e8",
      "incomplete_value": true,
      "site": "00b4e2e8",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e24c",
      "incomplete_value": true,
      "site": "00b4e24c",
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
            "const:d48:8"
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
      "definition_site": "00b4e2cc",
      "incomplete_value": true,
      "site": "00b4e2cc",
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
      "definition_site": "00b4e230",
      "incomplete_value": true,
      "site": "00b4e230",
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
      "definition_site": "00b4e2d8",
      "incomplete_value": false,
      "site": "00b4e2e0",
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
            "const:f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e23c",
      "incomplete_value": false,
      "site": "00b4e244",
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
            "const:151:8"
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
      "00b4e2c8",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e2d8",
      "PARAM",
      [
        "storage",
        "002ae151",
        null,
        "string"
      ]
    ],
    [
      "00b4e2e8",
      "WRITE",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e2c8",
      "READ",
      [
        "storage",
        "01125e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e2d8",
      "PARAM",
      [
        "storage",
        "002ae0f5",
        null,
        "string"
      ]
    ],
    [
      "00b4e2e8",
      "WRITE",
      [
        "storage",
        "01125e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e21c.md#insn-00b4e244) · [`00b4e24c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e21c.md#insn-00b4e24c) · [`00b4e22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e21c.md#insn-00b4e22c)
- 新版 [`00b4e2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e2b8.md#insn-00b4e2e0) · [`00b4e2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e2b8.md#insn-00b4e2e8) · [`00b4e2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e2b8.md#insn-00b4e2c8)

~~~diff
- 00b4e244 ["INT_ADD", "register:40f0:8", ["const:b4e244:8", "const:4:8"]]
- 00b4e244 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4e2e0 ["INT_ADD", "register:40f0:8", ["const:b4e2e0:8", "const:4:8"]]
+ 00b4e2e0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4e244 bytes 33330494
+ 00b4e2e0 bytes 40330494
- 00b4e24c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00b4e24c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e2e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b4e2e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4e24c bytes 60a606f9
+ 00b4e2e8 bytes 602607f9
- 00b4e22c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00b4e22c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e2c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b4e2c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4e22c bytes 68a646f9
+ 00b4e2c8 bytes 682647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1381d6890a4bb27c2b6daf35ee295883"></a>

### [`00b4e260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e260.md) → [`00b4e2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e2fc.md) _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4e32c",
      "incomplete_value": true,
      "site": "00b4e32c",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e290",
      "incomplete_value": true,
      "site": "00b4e290",
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
            "const:d48:8"
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
      "definition_site": "00b4e310",
      "incomplete_value": true,
      "site": "00b4e310",
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
      "definition_site": "00b4e274",
      "incomplete_value": true,
      "site": "00b4e274",
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
      "definition_site": "00b4e318",
      "incomplete_value": false,
      "site": "00b4e324",
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
            "const:f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e27c",
      "incomplete_value": false,
      "site": "00b4e288",
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
            "const:151:8"
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
      "00b4e30c",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e318",
      "PARAM",
      [
        "storage",
        "002ae151",
        null,
        "string"
      ]
    ],
    [
      "00b4e32c",
      "WRITE",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e30c",
      "READ",
      [
        "storage",
        "01125e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e318",
      "PARAM",
      [
        "storage",
        "002ae0f5",
        null,
        "string"
      ]
    ],
    [
      "00b4e32c",
      "WRITE",
      [
        "storage",
        "01125e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e260.md#insn-00b4e288) · [`00b4e290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e260.md#insn-00b4e290) · [`00b4e270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e260.md#insn-00b4e270)
- 新版 [`00b4e324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e2fc.md#insn-00b4e324) · [`00b4e32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e2fc.md#insn-00b4e32c) · [`00b4e30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e2fc.md#insn-00b4e30c)

~~~diff
- 00b4e288 ["INT_ADD", "register:40f0:8", ["const:b4e288:8", "const:4:8"]]
- 00b4e288 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4e324 ["INT_ADD", "register:40f0:8", ["const:b4e324:8", "const:4:8"]]
+ 00b4e324 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4e288 bytes 22330494
+ 00b4e324 bytes 2f330494
- 00b4e290 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00b4e290 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e32c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b4e32c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4e290 bytes 60a606f9
+ 00b4e32c bytes 602607f9
- 00b4e270 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00b4e270 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e30c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b4e30c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4e270 bytes 68a646f9
+ 00b4e30c bytes 682647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e0771c9e468a828adf6063904e8f76a"></a>

### [`00b4e3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e3ec.md) → [`00b4e488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e488.md) _ZN8firebase4util6object14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "site": "00b4e3ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e3ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e3f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4e3ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e3f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e400",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e488",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4e48c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4e49c",
      "READ",
      [
        "storage",
        "01125e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e3ec.md#insn-00b4e3ec) · [`00b4e3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e3ec.md#insn-00b4e3f0) · [`00b4e408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e3ec.md#insn-00b4e408)

~~~diff
- 00b4e3ec ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4e3ec ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4e3ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4e3ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4e3ec bytes f44fbea9
- 00b4e3f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4e3f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4e3f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4e3f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4e3f0 bytes fd7b01a9
- 00b4e408 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4e408 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b4e408 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bea37cbc2370373ad06ceb4494c9417"></a>

### [`00b4e498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e498.md) → [`00b4e534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e534.md) _ZN8firebase4util6object13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00b4e4d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4e574"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4e558",
      "incomplete_value": false,
      "site": "00b4e56c",
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
            "const:f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e4bc",
      "incomplete_value": false,
      "site": "00b4e4d0",
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
            "const:151:8"
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
      "unmatched:00b4e4ac",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4e4bc",
      "PARAM",
      [
        "storage",
        "002ae151",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4e4d8",
      "WRITE",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e548",
      "READ",
      [
        "storage",
        "01125e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e558",
      "PARAM",
      [
        "storage",
        "002ae0f5",
        null,
        "string"
      ]
    ],
    [
      "00b4e574",
      "WRITE",
      [
        "storage",
        "01125e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e498.md#insn-00b4e4d0) · [`00b4e4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e498.md#insn-00b4e4d8)
- 新版 [`00b4e56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e534.md#insn-00b4e56c) · [`00b4e574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e534.md#insn-00b4e574)

~~~diff
- 00b4e4d0 ["INT_ADD", "register:40f0:8", ["const:b4e4d0:8", "const:4:8"]]
- 00b4e4d0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4e56c ["INT_ADD", "register:40f0:8", ["const:b4e56c:8", "const:4:8"]]
+ 00b4e56c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4e4d0 bytes 90320494
+ 00b4e56c bytes 9d320494
- 00b4e4d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d48:8"]]
- 00b4e4d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4e4d8 bytes 80a606f9
+ 00b4e574 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e48:8"]]
+ 00b4e574 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e574 bytes 802607f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-414d3238553d4af2293059bb7ebe46a9"></a>

### [`00b4e544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e544.md) → [`00b4e5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e5e0.md) _ZN8firebase4util25InitializeActivityClassesEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b4f0.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00b4eab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eab4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c5b5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b5c0.md) · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00b4eb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4eb50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 47.50% / 新版 47.50%

CFGの説明率　旧版 32.88% / 新版 34.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 1件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 17件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e5b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e60c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4e564",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00b4e570",
      "WRITE",
      [
        "storage",
        "01125d68",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00b4e588",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e600",
      "READ",
      [
        "storage",
        "01125e68",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e60c",
      "WRITE",
      [
        "storage",
        "01125e68",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e624",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e544.md#insn-00b4e570) · [`00b4e590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e544.md#insn-00b4e590) · [`00b4e5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e544.md#insn-00b4e5b4)

~~~diff
- 00b4e570 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d68:8"]]
- 00b4e570 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b4e570 bytes e86a0db9
- 00b4e590 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4e590 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b4e590 bytes 410100b5
- 00b4e5b4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:7c8:8"]]
- 00b4e5b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4e5b4 bytes c0e603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27fa0c6611d49333b262bd2e5d6b8787"></a>

### [`00b4e904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e904.md) → [`00b4e9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e9a0.md) _ZN8firebase4util24TerminateActivityClassesEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b4e0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b5b0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 36.11% / 新版 36.11%

CFGの説明率　旧版 28.21% / 新版 28.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e938"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e968"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e9b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4e9b4",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e9bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4e934"
      ]
    ],
    [
      "unmatched:00b4e928",
      "PARAM",
      [
        "storage",
        "002bd0fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4e9b4",
      "READ",
      [
        "storage",
        "01125e68",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e9bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4e9d0"
      ]
    ],
    [
      "00b4e9c4",
      "PARAM",
      [
        "storage",
        "002bd0aa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e904.md#insn-00b4e918) · [`00b4e92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e904.md#insn-00b4e92c) · [`00b4e938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e904.md#insn-00b4e938)
- 新版 [`00b4e9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e9a0.md#insn-00b4e9b4)

~~~diff
- 00b4e918 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
- 00b4e918 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00b4e918 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
+ 00b4e9b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e68:8"]]
+ 00b4e9b4 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e9b4 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 00b4e918 bytes 886a4db9
+ 00b4e9b4 bytes 886a4eb9
- 00b4e92c ["INT_ADD", "register:40f0:8", ["const:b4e92c:8", "const:4:8"]]
- 00b4e92c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4e92c bytes b5310494
- 00b4e938 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
- 00b4e938 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b4e938 bytes 886a0db9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64e4f1602260f2e0261343402521e54f"></a>

### [`00b4eab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eab4.md) → [`00b4eb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4eb50.md) FUN_00b4eb50

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4e544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e544.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00b4e5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4e5e0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment

命令の説明率　旧版 85.29% / 新版 85.29%

CFGの説明率　旧版 46.15% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4ebcc",
      "incomplete_value": true,
      "site": "00b4ebcc",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4eb30",
      "incomplete_value": true,
      "site": "00b4eb30",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4eb74",
      "incomplete_value": true,
      "site": "00b4eb78",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00b4ead8",
      "incomplete_value": true,
      "site": "00b4eadc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4eb04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4eb64",
      "READ",
      [
        "storage",
        "01125d70",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4eaf8",
      "READ",
      [
        "storage",
        "01125d70",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4eb04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4eb80"
      ]
    ]
  ],
  "added": [
    [
      "00b4eb64",
      "READ",
      [
        "storage",
        "01125e70",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4eb94",
      "READ",
      [
        "storage",
        "01125e70",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4eba0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4eb80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4eadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eab4.md#insn-00b4eadc) · [`00b4eb04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eab4.md#insn-00b4eb04) · [`00b4eb24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eab4.md#insn-00b4eb24)
- 新版 [`00b4eb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4eb50.md#insn-00b4eb78) · [`00b4ebc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4eb50.md#insn-00b4ebc0)

~~~diff
- 00b4eadc ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00b4eb78 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b4eadc bytes 80010054
+ 00b4eb78 bytes 80010054
- 00b4eb04 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b4eb04 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4eb04 bytes 01ffff54
- 00b4eb24 ["INT_ADD", "register:40f0:8", ["const:b4eb24:8", "const:4:8"]]
- 00b4eb24 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b4ebc0 ["INT_ADD", "register:40f0:8", ["const:b4ebc0:8", "const:4:8"]]
+ 00b4ebc0 ["CALL", null, ["callee:00c57f80:8"]]
- 00b4eb24 bytes e3240494
+ 00b4ebc0 bytes f0240494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55660248efd36b6626e27142171c598d"></a>

### [`00b4eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eb3c.md) → [`00b4ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4ebd8.md) _ZN8firebase4util10InitializeEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aea0.md) · 呼出先 13件 [`00b4fbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4f/00b4fbc0.md) [`00b50de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50de4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5af70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af70.md) · 呼出先 13件 [`00b4fc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4f/00b4fc5c.md) [`00b50e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b50/00b50e80.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 29.90% / 新版 29.90%

CFGの説明率　旧版 22.56% / 新版 22.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 48件, `store_condition` 4件, `store_destination` 12件, `unresolved_branch_alignment` 62件, `unresolved_call_alignment` 57件, `unresolved_store_alignment` 30件

アドレスに依存する影響 `branch_value` 4件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4ec10",
      "incomplete_value": true,
      "site": "00b4ec10",
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
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4eb74",
      "incomplete_value": true,
      "site": "00b4eb74",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ebbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ec14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ec04",
      "READ",
      [
        "storage",
        "01125d78",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4ec10",
      "WRITE",
      [
        "storage",
        "01125d78",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4ec30",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ec04",
      "READ",
      [
        "storage",
        "01125e78",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4ec10",
      "WRITE",
      [
        "storage",
        "01125e78",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4ec30",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4eb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eb3c.md#insn-00b4eb74) · [`00b4ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eb3c.md#insn-00b4ebbc) · [`00b4ec10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eb3c.md#insn-00b4ec10)
- 新版 [`00b4ec10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4ebd8.md#insn-00b4ec10)

~~~diff
- 00b4eb74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
- 00b4eb74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b4ec10 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e78:8"]]
+ 00b4ec10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b4eb74 bytes a87a0db9
+ 00b4ec10 bytes a87a0eb9
- 00b4ebbc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:830:8"]]
- 00b4ebbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ebbc bytes c01a04f9
- 00b4ec10 ["COPY", "register:4008:8", ["register:4000:8"]]
- 00b4ec10 bytes e10300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1da461f7d07a539bddd6163714f19472"></a>

### [`00b4fbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4f/00b4fbc0.md) → [`00b4fc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4f/00b4fc5c.md) FUN_00b4fc5c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b4eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eb3c.md) [`00b50de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50de4.md) · 呼出先 1件 [`00c5b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b380.md)
- 新版 呼出元 2件 [`00b4ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4ebd8.md) [`00b50e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b50/00b50e80.md) · 呼出先 1件 [`00c5b450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b450.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 22.31% / 新版 22.31%

CFGの説明率　旧版 17.06% / 新版 17.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `unresolved_branch_alignment` 84件, `unresolved_call_alignment` 148件, `unresolved_store_alignment` 60件

アドレスに依存する影響 `branch_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4fbfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4fc4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4fc78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4fc70",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4fc78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4fc50"
      ]
    ],
    [
      "00b4fc80",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4fc70",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4fc78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4fcec"
      ]
    ],
    [
      "00b4fc80",
      "READ",
      [
        "storage",
        "01125968",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4fbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4f/00b4fbc0.md#insn-00b4fbfc) · [`00b4fc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4f/00b4fbc0.md#insn-00b4fc4c) · [`00b4fc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4f/00b4fbc0.md#insn-00b4fc78)

~~~diff
- 00b4fbfc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4fbfc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4fbfc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:868:8"]]
- 00b4fbfc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4fbfc bytes bfa22139
- 00b4fc4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:860:8"]]
- 00b4fc4c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4fc4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4fc4c bytes 9f3204f9
- 00b4fc78 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4fc78 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4fc78 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:838:8"]]
- 00b4fc78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4fc78 bytes bfe22039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70f0f5f7414b36dc5e9c531c9d0a286e"></a>

### [`00b50de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50de4.md) → [`00b50e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b50/00b50e80.md) _ZN8firebase4util9TerminateEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b4eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eb3c.md) [`00c5afd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afd0.md) · 呼出先 10件 [`00b4fbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4f/00b4fbc0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5af00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af00.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b240.md)
- 新版 呼出元 2件 [`00b4ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4e/00b4ebd8.md) [`00c5b0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0a0.md) · 呼出先 10件 [`00b4fc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4f/00b4fc5c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afd0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b310.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.14% / 新版 87.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b50eb4",
      "incomplete_value": true,
      "site": "00b50eb4",
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
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b50e18",
      "incomplete_value": true,
      "site": "00b50e18",
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
            "const:d78:8"
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
      "definition_site": "00b50f18",
      "incomplete_value": true,
      "site": "00b50f18",
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
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b50e7c",
      "incomplete_value": true,
      "site": "00b50e7c",
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
            "const:d80:8"
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
      "definition_site": "00b50ed4",
      "incomplete_value": true,
      "site": "00b50ed4",
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
      "definition_site": "00b50e38",
      "incomplete_value": true,
      "site": "00b50e38",
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
      "00b50e94",
      "READ",
      [
        "storage",
        "01125d78",
        null,
        "undefined4"
      ]
    ],
    [
      "00b50ea4",
      "PARAM",
      [
        "storage",
        "002a0ab8",
        null,
        "string"
      ]
    ],
    [
      "00b50eac",
      "READ",
      [
        "storage",
        "01125d78",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b50e94",
      "READ",
      [
        "storage",
        "01125e78",
        null,
        "undefined4"
      ]
    ],
    [
      "00b50ea4",
      "PARAM",
      [
        "storage",
        "002a0a6b",
        null,
        "string"
      ]
    ],
    [
      "00b50eac",
      "READ",
      [
        "storage",
        "01125e78",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b50df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50de4.md#insn-00b50df8) · [`00b50e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50de4.md#insn-00b50e08) · [`00b50e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50de4.md#insn-00b50e0c)
- 新版 [`00b50e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b50/00b50e80.md#insn-00b50e94) · [`00b50ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b50/00b50e80.md#insn-00b50ea4) · [`00b50ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b50/00b50e80.md#insn-00b50ea8)

~~~diff
- 00b50df8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d78:8"]]
- 00b50df8 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00b50df8 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
+ 00b50e94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e78:8"]]
+ 00b50e94 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00b50e94 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 00b50df8 bytes 887a4db9
+ 00b50e94 bytes 887a4eb9
- 00b50e08 ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 00b50e08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b50e08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b50e08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b50ea4 ["COPY", "tmp:0:8", ["const:a6b:8"]]
+ 00b50ea4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b50ea4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b50ea4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b50e08 bytes 00e02a91
+ 00b50ea4 bytes 00ac2991
- 00b50e0c ["INT_ADD", "register:40f0:8", ["const:b50e0c:8", "const:4:8"]]
- 00b50e0c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b50ea8 ["INT_ADD", "register:40f0:8", ["const:b50ea8:8", "const:4:8"]]
+ 00b50ea8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b50e0c bytes 7d280494
+ 00b50ea8 bytes 8a280494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e687575e1ed528e466da95e4a8f49b0"></a>

### [`00b50efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50efc.md) → [`00b50f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b50/00b50f98.md) _ZN8firebase4util18CacheEmbeddedFilesEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3a0.md) · 呼出先 6件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md)
- 新版 呼出元 1件 [`00c5b470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b470.md) · 呼出先 6件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b50fbc",
      "incomplete_value": true,
      "site": "00b50fc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b50f20",
      "incomplete_value": true,
      "site": "00b50f28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e0:8"
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
    "new": {
      "definition_site": "00b5101c",
      "incomplete_value": false,
      "site": "00b51020",
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
            "const:4df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b50f80",
      "incomplete_value": false,
      "site": "00b50f84",
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
            "const:4ae:8"
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
      "definition_site": "00b5103c",
      "incomplete_value": true,
      "site": "00b51058",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b50fa0",
      "incomplete_value": true,
      "site": "00b50fbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a90:8"
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
      "00b50fbc",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5101c",
      "PARAM",
      [
        "storage",
        "002b34ae",
        null,
        "string"
      ]
    ],
    [
      "00b5103c",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b50fbc",
      "READ",
      [
        "storage",
        "011258e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5101c",
      "PARAM",
      [
        "storage",
        "002b34df",
        null,
        "string"
      ]
    ],
    [
      "00b5103c",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b50f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50efc.md#insn-00b50f20) · [`00b50f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50efc.md#insn-00b50f28) · [`00b50f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50efc.md#insn-00b50f84)
- 新版 [`00b50fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b50/00b50f98.md#insn-00b50fbc) · [`00b50fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b50/00b50f98.md#insn-00b50fc4) · [`00b51020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b50/00b50f98.md#insn-00b51020)

~~~diff
- 00b50f20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7e0:8"]]
- 00b50f20 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b50fbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8e0:8"]]
+ 00b50fbc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b50f20 bytes 02f143f9
+ 00b50fbc bytes 027144f9
- 00b50f28 ["INT_ADD", "register:40f0:8", ["const:b50f28:8", "const:4:8"]]
- 00b50f28 ["CALL", null, ["callee:00497874:8"]]
+ 00b50fc4 ["INT_ADD", "register:40f0:8", ["const:b50fc4:8", "const:4:8"]]
+ 00b50fc4 ["CALL", null, ["callee:00497874:8"]]
- 00b50f28 bytes 431ae597
+ 00b50fc4 bytes 2c1ae597
- 00b50f84 ["INT_ADD", "register:40f0:8", ["const:b50f84:8", "const:4:8"]]
- 00b50f84 ["CALL", null, ["callee:00c5b200:8"]]
+ 00b51020 ["INT_ADD", "register:40f0:8", ["const:b51020:8", "const:4:8"]]
+ 00b51020 ["CALL", null, ["callee:00c5b200:8"]]
- 00b50f84 bytes 6b280494
+ 00b51020 bytes 78280494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a854893355c984a9da58145a39d3b5a"></a>

### [`00b5139c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b5139c.md) → [`00b51438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b51438.md) _ZN8firebase4util17JavaThreadContext10InitializeEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b350.md) · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 1件 [`00c5b420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b420.md) · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 7件, `store_condition` 1件, `store_destination` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b51484",
      "incomplete_value": true,
      "site": "00b51484",
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
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b513e8",
      "incomplete_value": true,
      "site": "00b513e8",
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
            "const:678:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b51524",
      "incomplete_value": true,
      "site": "00b51524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51488",
      "incomplete_value": true,
      "site": "00b51488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b51570",
      "incomplete_value": true,
      "site": "00b51570",
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
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b514d4",
      "incomplete_value": true,
      "site": "00b514d4",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b51454",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51468",
      "PARAM",
      [
        "storage",
        "002be58b",
        null,
        "string"
      ]
    ],
    [
      "00b51484",
      "WRITE",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b51454",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51468",
      "PARAM",
      [
        "storage",
        "002be537",
        null,
        "string"
      ]
    ],
    [
      "00b51484",
      "WRITE",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b513e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b5139c.md#insn-00b513e0) · [`00b513e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b5139c.md#insn-00b513e8) · [`00b51410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b5139c.md#insn-00b51410)
- 新版 [`00b5147c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b51438.md#insn-00b5147c) · [`00b51484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b51438.md#insn-00b51484) · [`00b514ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b51438.md#insn-00b514ac)

~~~diff
- 00b513e0 ["INT_ADD", "register:40f0:8", ["const:b513e0:8", "const:4:8"]]
- 00b513e0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b5147c ["INT_ADD", "register:40f0:8", ["const:b5147c:8", "const:4:8"]]
+ 00b5147c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b513e0 bytes cc260494
+ 00b5147c bytes d9260494
- 00b513e8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
- 00b513e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b51484 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 00b51484 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b513e8 bytes c03e03f9
+ 00b51484 bytes c0be03f9
- 00b51410 ["INT_ADD", "register:40f0:8", ["const:b51410:8", "const:4:8"]]
- 00b51410 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b514ac ["INT_ADD", "register:40f0:8", ["const:b514ac:8", "const:4:8"]]
+ 00b514ac ["CALL", null, ["callee:00c5b000:8"]]
- 00b51410 bytes c8260494
+ 00b514ac bytes d5260494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-092585d3b8ad8c05a007bbd2b06b219a"></a>

### [`00b51510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51510.md) → [`00b515ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b515ac.md) _ZN8firebase4util15CancelCallbacksEP7_JNIEnvPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5af00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af00.md) · 呼出先 7件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md) [`00c5b600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b600.md)
- 新版 呼出元 1件 [`00c5afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afd0.md) · 呼出先 7件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b200.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md) [`00c5b6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.80% / 新版 92.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b515e4",
      "incomplete_value": true,
      "site": "00b515e8",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51548",
      "incomplete_value": true,
      "site": "00b5154c",
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
            "const:79c:8"
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
      "definition_site": "00b51730",
      "incomplete_value": true,
      "site": "00b5173c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c8:8"
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
      "definition_site": "00b51694",
      "incomplete_value": true,
      "site": "00b516a0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c8:8"
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
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b515e0",
      "PARAM",
      [
        "storage",
        "002bd11b",
        null,
        "string"
      ]
    ],
    [
      "00b515e4",
      "PARAM",
      [
        "storage",
        "002bf79c",
        null,
        "string"
      ]
    ],
    [
      "00b51614",
      "PARAM",
      [
        "storage",
        "01125d88",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b515e0",
      "PARAM",
      [
        "storage",
        "002bd0c7",
        null,
        "string"
      ]
    ],
    [
      "00b515e4",
      "PARAM",
      [
        "storage",
        "002bf748",
        null,
        "string"
      ]
    ],
    [
      "00b51614",
      "PARAM",
      [
        "storage",
        "01125e88",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5154c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51510.md#insn-00b5154c) · [`00b516a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51510.md#insn-00b516a0) · [`00b51534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51510.md#insn-00b51534)
- 新版 [`00b515e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b515ac.md#insn-00b515e8) · [`00b5173c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b515ac.md#insn-00b5173c) · [`00b515d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b515ac.md#insn-00b515d0)

~~~diff
- 00b5154c ["INT_ADD", "register:40f0:8", ["const:b5154c:8", "const:4:8"]]
- 00b5154c ["CALL", null, ["callee:00c5b200:8"]]
+ 00b515e8 ["INT_ADD", "register:40f0:8", ["const:b515e8:8", "const:4:8"]]
+ 00b515e8 ["CALL", null, ["callee:00c5b200:8"]]
- 00b5154c bytes f9260494
+ 00b515e8 bytes 06270494
- 00b516a0 ["INT_ADD", "register:40f0:8", ["const:b516a0:8", "const:4:8"]]
- 00b516a0 ["CALL", null, ["callee:00574d2c:8"]]
+ 00b5173c ["INT_ADD", "register:40f0:8", ["const:b5173c:8", "const:4:8"]]
+ 00b5173c ["CALL", null, ["callee:00574d2c:8"]]
- 00b516a0 bytes 938de897
+ 00b5173c bytes 7c8de897
- 00b51534 ["COPY", "tmp:0:8", ["const:11b:8"]]
- 00b51534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b51534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b51534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b515d0 ["COPY", "tmp:0:8", ["const:c7:8"]]
+ 00b515d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b515d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b515d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b51534 bytes 086d0491
+ 00b515d0 bytes 081d0391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-270fd2c5f0c7532414b1772cdcd19c1a"></a>

### [`00b51838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51838.md) → [`00b518d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b518d4.md) _ZN8firebase4util19StdVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA_EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b420.md) · 呼出先 2件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md)
- 新版 呼出元 1件 [`00c5b4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b4f0.md) · 呼出先 2件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b518f8",
      "incomplete_value": true,
      "site": "00b51904",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b5185c",
      "incomplete_value": true,
      "site": "00b51868",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
      "definition_site": "00b518fc",
      "incomplete_value": true,
      "site": "00b51904",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51860",
      "incomplete_value": true,
      "site": "00b51868",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:840:8"
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
      "00b518f8",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b518fc",
      "READ",
      [
        "storage",
        "01125840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51918",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b518f8",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b518fc",
      "READ",
      [
        "storage",
        "01125940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51918",
      "READ",
      [
        "storage",
        "01125950",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b51868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51838.md#insn-00b51868) · [`00b51854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51838.md#insn-00b51854) · [`00b5185c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51838.md#insn-00b5185c)
- 新版 [`00b51904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b518d4.md#insn-00b51904) · [`00b518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b518d4.md#insn-00b518f0) · [`00b518f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b518d4.md#insn-00b518f8)

~~~diff
- 00b51868 ["INT_ADD", "register:40f0:8", ["const:b51868:8", "const:4:8"]]
- 00b51868 ["CALL", null, ["callee:00589734:8"]]
+ 00b51904 ["INT_ADD", "register:40f0:8", ["const:b51904:8", "const:4:8"]]
+ 00b51904 ["CALL", null, ["callee:00589734:8"]]
- 00b51868 bytes a3dfe897
+ 00b51904 bytes 8cdfe897
- 00b51854 ["COPY", "tmp:0:8", ["const:840:8"]]
- 00b51854 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00b51854 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00b51854 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00b518f0 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00b518f0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00b518f0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00b518f0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00b51854 bytes d6022191
+ 00b518f0 bytes d6022591
- 00b5185c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:830:8"]]
- 00b5185c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b518f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:930:8"]]
+ 00b518f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5185c bytes 011944f9
+ 00b518f8 bytes 019944f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c21ae674ad23792710c12c0e27eb4a31"></a>

### [`00b51940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51940.md) → [`00b519dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b519dc.md) _ZN8firebase4util25StdUnorderedSetToJavaListEP7_JNIEnvRKNSt6__ndk113unordered_setINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b51a00",
      "incomplete_value": true,
      "site": "00b51a0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b51964",
      "incomplete_value": true,
      "site": "00b51970",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
      "definition_site": "00b51a04",
      "incomplete_value": true,
      "site": "00b51a0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51968",
      "incomplete_value": true,
      "site": "00b51970",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:840:8"
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
      "00b51a00",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51a04",
      "READ",
      [
        "storage",
        "01125840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51a1c",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b51a00",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51a04",
      "READ",
      [
        "storage",
        "01125940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51a1c",
      "READ",
      [
        "storage",
        "01125950",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b51970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51940.md#insn-00b51970) · [`00b5195c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51940.md#insn-00b5195c) · [`00b51964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51940.md#insn-00b51964)
- 新版 [`00b51a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b519dc.md#insn-00b51a0c) · [`00b519f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b519dc.md#insn-00b519f8) · [`00b51a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b519dc.md#insn-00b51a00)

~~~diff
- 00b51970 ["INT_ADD", "register:40f0:8", ["const:b51970:8", "const:4:8"]]
- 00b51970 ["CALL", null, ["callee:00589734:8"]]
+ 00b51a0c ["INT_ADD", "register:40f0:8", ["const:b51a0c:8", "const:4:8"]]
+ 00b51a0c ["CALL", null, ["callee:00589734:8"]]
- 00b51970 bytes 61dfe897
+ 00b51a0c bytes 4adfe897
- 00b5195c ["COPY", "tmp:0:8", ["const:840:8"]]
- 00b5195c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00b5195c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00b5195c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00b519f8 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00b519f8 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00b519f8 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00b519f8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00b5195c bytes b5022191
+ 00b519f8 bytes b5022591
- 00b51964 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:830:8"]]
- 00b51964 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b51a00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:930:8"]]
+ 00b51a00 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b51964 bytes 011944f9
+ 00b51a00 bytes 019944f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-489653c58b42663e7a522d10be86d812"></a>

### [`00b51a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51a38.md) → [`00b51ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b51ad4.md) _ZN8firebase4util19VariantMapToJavaMapEP7_JNIEnvRKNSt6__ndk13mapINS_7VariantES5_NS3_4lessIS5_EENS3_9allocatorINS3_4pairIKS5_S5_EEEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b430.md) · 呼出先 3件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5b440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b440.md)
- 新版 呼出元 1件 [`00c5b500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b500.md) · 呼出先 3件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5b510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b510.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.85% / 新版 97.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b51af8",
      "incomplete_value": true,
      "site": "00b51b04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51a5c",
      "incomplete_value": true,
      "site": "00b51a68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
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
      "definition_site": "00b51afc",
      "incomplete_value": true,
      "site": "00b51b04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51a60",
      "incomplete_value": true,
      "site": "00b51a68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b20:8"
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
      "00b51af8",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51afc",
      "READ",
      [
        "storage",
        "01125b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51b0c",
      "READ",
      [
        "storage",
        "01125c48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b51af8",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51afc",
      "READ",
      [
        "storage",
        "01125c20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51b0c",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b51a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51a38.md#insn-00b51a68) · [`00b51b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51a38.md#insn-00b51b04) · [`00b51a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51a38.md#insn-00b51a5c)
- 新版 [`00b51b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b51ad4.md#insn-00b51b04) · [`00b51ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b51ad4.md#insn-00b51ba0) · [`00b51af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b51ad4.md#insn-00b51af8)

~~~diff
- 00b51a68 ["INT_ADD", "register:40f0:8", ["const:b51a68:8", "const:4:8"]]
- 00b51a68 ["CALL", null, ["callee:00589734:8"]]
+ 00b51b04 ["INT_ADD", "register:40f0:8", ["const:b51b04:8", "const:4:8"]]
+ 00b51b04 ["CALL", null, ["callee:00589734:8"]]
- 00b51a68 bytes 23dfe897
+ 00b51b04 bytes 0cdfe897
- 00b51b04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b51b04 ["INT_ADD", "register:40f0:8", ["const:b51b04:8", "const:4:8"]]
- 00b51b04 ["CALLIND", null, ["register:0:8"]]
+ 00b51ba0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b51ba0 ["INT_ADD", "register:40f0:8", ["const:b51ba0:8", "const:4:8"]]
+ 00b51ba0 ["CALLIND", null, ["register:0:8"]]
- 00b51b04 bytes 00013fd6
+ 00b51ba0 bytes 00013fd6
- 00b51a5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b10:8"]]
- 00b51a5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b51af8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c10:8"]]
+ 00b51af8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b51a5c bytes 018945f9
+ 00b51af8 bytes 010946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b40330be0a3addaae296cc6a38e5a968"></a>

### [`00b51bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51bac.md) → [`00b51c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b51c48.md) _ZN8firebase4util19VariantToJavaObjectEP7_JNIEnvRKNS_7VariantE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5b440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b440.md) · 呼出先 7件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5ab00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab00.md) [`00c5ab20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab20.md) [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b430.md)
- 新版 呼出元 1件 [`00c5b510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b510.md) · 呼出先 7件 [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5abd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abd0.md) [`00c5abf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abf0.md) [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) [`00c5b500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b500.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b51e54",
      "incomplete_value": false,
      "site": "00b51e58",
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
            "const:34b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51db8",
      "incomplete_value": false,
      "site": "00b51dbc",
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
            "const:3a7:8"
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
      "00b51c78",
      "DATA",
      [
        "storage",
        "0030b5fa",
        "switchD_00b51be8::switchdataD_0030b5fa",
        "byte"
      ]
    ],
    [
      "00b51ccc",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51cd0",
      "READ",
      [
        "storage",
        "01125c20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b51c78",
      "DATA",
      [
        "storage",
        "0030b63a",
        "switchD_00b51c84::switchdataD_0030b63a",
        "byte"
      ]
    ],
    [
      "00b51ccc",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51cd0",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b51dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51bac.md#insn-00b51dbc) · [`00b51bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51bac.md#insn-00b51bd4) · [`00b51bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51bac.md#insn-00b51bd8)
- 新版 [`00b51e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b51c48.md#insn-00b51e58) · [`00b51c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b51c48.md#insn-00b51c70)

~~~diff
- 00b51dbc ["INT_ADD", "register:40f0:8", ["const:b51dbc:8", "const:4:8"]]
- 00b51dbc ["CALL", null, ["callee:00c5aeb0:8"]]
+ 00b51e58 ["INT_ADD", "register:40f0:8", ["const:b51e58:8", "const:4:8"]]
+ 00b51e58 ["CALL", null, ["callee:00c5aeb0:8"]]
- 00b51dbc bytes 09240494
+ 00b51e58 bytes 16240494
- 00b51bd4 ["COPY", "tmp:0:8", ["const:5fa:8"]]
- 00b51bd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b51bd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b51bd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b51c70 ["COPY", "tmp:0:8", ["const:63a:8"]]
+ 00b51c70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b51c70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b51c70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b51bd4 bytes 29e91791
+ 00b51c70 bytes 29e91891
- 00b51bd8 ["COPY", "register:4050:8", ["const:b51bec:8"]]
- 00b51bd8 bytes aa000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e24d07e3cdb6984f4687c8348516ca81"></a>

### [`00b520d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b520d8.md) → [`00b52174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b52174.md) _ZN8firebase4util15JavaMapToStdMapEP7_JNIEnvPNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEESA_NS3_4lessISA_EEN

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.34% / 新版 99.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b521b4",
      "incomplete_value": true,
      "site": "00b521bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52118",
      "incomplete_value": true,
      "site": "00b52120",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c58:8"
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
    "new": {
      "definition_site": "00b52200",
      "incomplete_value": true,
      "site": "00b5220c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52164",
      "incomplete_value": true,
      "site": "00b52170",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
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
      "definition_site": "00b52250",
      "incomplete_value": true,
      "site": "00b52260",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b521b4",
      "incomplete_value": true,
      "site": "00b521c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b521b4",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52200",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52250",
      "READ",
      [
        "storage",
        "01125bc8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b521b4",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52200",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52250",
      "READ",
      [
        "storage",
        "01125cc8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b520d8.md#insn-00b52120) · [`00b52170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b520d8.md#insn-00b52170) · [`00b521c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b520d8.md#insn-00b521c4)
- 新版 [`00b521bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b52174.md#insn-00b521bc) · [`00b5220c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b52174.md#insn-00b5220c) · [`00b52260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b52174.md#insn-00b52260)

~~~diff
- 00b52120 ["INT_ADD", "register:40f0:8", ["const:b52120:8", "const:4:8"]]
- 00b52120 ["CALL", null, ["callee:00497874:8"]]
+ 00b521bc ["INT_ADD", "register:40f0:8", ["const:b521bc:8", "const:4:8"]]
+ 00b521bc ["CALL", null, ["callee:00497874:8"]]
- 00b52120 bytes c515e597
+ 00b521bc bytes ae15e597
- 00b52170 ["INT_ADD", "register:40f0:8", ["const:b52170:8", "const:4:8"]]
- 00b52170 ["CALL", null, ["callee:00497874:8"]]
+ 00b5220c ["INT_ADD", "register:40f0:8", ["const:b5220c:8", "const:4:8"]]
+ 00b5220c ["CALL", null, ["callee:00497874:8"]]
- 00b52170 bytes b115e597
+ 00b5220c bytes 9a15e597
- 00b521c4 ["INT_ADD", "register:40f0:8", ["const:b521c4:8", "const:4:8"]]
- 00b521c4 ["CALL", null, ["callee:00497a88:8"]]
+ 00b52260 ["INT_ADD", "register:40f0:8", ["const:b52260:8", "const:4:8"]]
+ 00b52260 ["CALL", null, ["callee:00497a88:8"]]
- 00b521c4 bytes 2116e597
+ 00b52260 bytes 0a16e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e248403227ea24168bd1403debcacfb"></a>

### [`00b526b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b526b0.md) → [`00b5274c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b5274c.md) FUN_00b5274c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b526ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b526ac.md) [`00b529b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b529b4.md) · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md)
- 新版 呼出元 2件 [`00b52748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b52748.md) [`00b52a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b52a50.md) · 呼出先 7件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.45% / 新版 98.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5278c",
      "incomplete_value": true,
      "site": "00b52794",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b526f0",
      "incomplete_value": true,
      "site": "00b526f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c58:8"
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
    "new": {
      "definition_site": "00b527d8",
      "incomplete_value": true,
      "site": "00b527e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5273c",
      "incomplete_value": true,
      "site": "00b52748",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
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
      "definition_site": "00b52828",
      "incomplete_value": true,
      "site": "00b52838",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5278c",
      "incomplete_value": true,
      "site": "00b5279c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5278c",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b527d8",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52828",
      "READ",
      [
        "storage",
        "01125bc8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5278c",
      "READ",
      [
        "storage",
        "01125d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b527d8",
      "READ",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52828",
      "READ",
      [
        "storage",
        "01125cc8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b526f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b526b0.md#insn-00b526f8) · [`00b52748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b526b0.md#insn-00b52748) · [`00b5279c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b526b0.md#insn-00b5279c)
- 新版 [`00b52794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b5274c.md#insn-00b52794) · [`00b527e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b5274c.md#insn-00b527e4) · [`00b52838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b5274c.md#insn-00b52838)

~~~diff
- 00b526f8 ["INT_ADD", "register:40f0:8", ["const:b526f8:8", "const:4:8"]]
- 00b526f8 ["CALL", null, ["callee:00497874:8"]]
+ 00b52794 ["INT_ADD", "register:40f0:8", ["const:b52794:8", "const:4:8"]]
+ 00b52794 ["CALL", null, ["callee:00497874:8"]]
- 00b526f8 bytes 4f14e597
+ 00b52794 bytes 3814e597
- 00b52748 ["INT_ADD", "register:40f0:8", ["const:b52748:8", "const:4:8"]]
- 00b52748 ["CALL", null, ["callee:00497874:8"]]
+ 00b527e4 ["INT_ADD", "register:40f0:8", ["const:b527e4:8", "const:4:8"]]
+ 00b527e4 ["CALL", null, ["callee:00497874:8"]]
- 00b52748 bytes 3b14e597
+ 00b527e4 bytes 2414e597
- 00b5279c ["INT_ADD", "register:40f0:8", ["const:b5279c:8", "const:4:8"]]
- 00b5279c ["CALL", null, ["callee:00497a88:8"]]
+ 00b52838 ["INT_ADD", "register:40f0:8", ["const:b52838:8", "const:4:8"]]
+ 00b52838 ["CALL", null, ["callee:00497a88:8"]]
- 00b5279c bytes ab14e597
+ 00b52838 bytes 9414e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5718319c6f412101d12073810bdeadc5"></a>

### [`00b529b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b529b4.md) → [`00b52a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b52a50.md) _ZN8firebase4util19JavaObjectToVariantEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b410.md) · 呼出先 19件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md)
- 新版 呼出元 1件 [`00c5b4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b4e0.md) · 呼出先 19件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`0058f5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f5dc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.02% / 新版 85.02%

CFGの説明率　旧版 47.87% / 新版 45.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52e90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52efc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b52f2c"
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
      "00b52a88",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52ae4",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52b04",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52a88",
      "READ",
      [
        "storage",
        "01125dd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52ae4",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52b04",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b529fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b529b4.md#insn-00b529fc) · [`00b52a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b529b4.md#insn-00b52a48) · [`00b52a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b529b4.md#insn-00b52a58)
- 新版 [`00b52a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b52a50.md#insn-00b52a98) · [`00b52ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b52a50.md#insn-00b52ae4) · [`00b52af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b52/00b52a50.md#insn-00b52af4)

~~~diff
- 00b529fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b529fc ["INT_ADD", "register:40f0:8", ["const:b529fc:8", "const:4:8"]]
- 00b529fc ["CALLIND", null, ["register:0:8"]]
+ 00b52a98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b52a98 ["INT_ADD", "register:40f0:8", ["const:b52a98:8", "const:4:8"]]
+ 00b52a98 ["CALLIND", null, ["register:0:8"]]
- 00b529fc bytes 00013fd6
+ 00b52a98 bytes 00013fd6
- 00b52a48 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a10:8"]]
- 00b52a48 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52ae4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b10:8"]]
+ 00b52ae4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52a48 bytes 220945f9
+ 00b52ae4 bytes 228945f9
- 00b52a58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b52a58 ["INT_ADD", "register:40f0:8", ["const:b52a58:8", "const:4:8"]]
- 00b52a58 ["CALLIND", null, ["register:0:8"]]
+ 00b52af4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b52af4 ["INT_ADD", "register:40f0:8", ["const:b52af4:8", "const:4:8"]]
+ 00b52af4 ["CALLIND", null, ["register:0:8"]]
- 00b52a58 bytes 00013fd6
+ 00b52af4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a5909c1d7eec780a681b83aa6f6b92a"></a>

### [`00b530cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b530cc.md) → [`00b53168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53168.md) _ZN8firebase4util24JavaSetToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b4d0.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5b5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b5a0.md) · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.62% / 新版 65.62%

CFGの説明率　旧版 5.19% / 新版 5.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 3件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b530d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b530d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b530d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b530d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b530d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b530f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5316c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b53170",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5318c",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b530d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b530cc.md#insn-00b530d0) · [`00b530d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b530cc.md#insn-00b530d4) · [`00b530f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b530cc.md#insn-00b530f0)

~~~diff
- 00b530d0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b530d0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b530d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b530d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b530d0 bytes fc6f03a9
- 00b530d4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b530d4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b530d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b530d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b530d4 bytes fa6704a9
- 00b530f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b530f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b530f0 bytes e90700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e7f6bc4dcf31767cab5da58d35ccaf2"></a>

### [`00b53380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53380.md) → [`00b5341c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b5341c.md) _ZN8firebase4util23VariantVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b4c0.md) · 呼出先 3件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5b440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b440.md)
- 新版 呼出元 1件 [`00c5b590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b590.md) · 呼出先 3件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5b510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b510.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.45% / 新版 53.45%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53384"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53380",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53384",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53388",
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
      "00b5341c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b53420",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b53424",
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

- 旧版 [`00b53380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53380.md#insn-00b53380) · [`00b53384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53380.md#insn-00b53384) · [`00b53388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53380.md#insn-00b53388)

~~~diff
- 00b53380 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b53380 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b53380 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b53380 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b53380 bytes f85fbca9
- 00b53384 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b53384 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b53384 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b53384 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53384 bytes f65701a9
- 00b53388 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b53388 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b53388 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b53388 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53388 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3aaf4ee08d4c8d5abad2692e9482aba"></a>

### [`00b53468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53468.md) → [`00b53504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53504.md) _ZN8firebase4util25JavaListToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_IS

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5abb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abb0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ac80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.27% / 新版 76.27%

CFGの説明率　旧版 19.05% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53478"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53478"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5347c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53478",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5347c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53498",
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
      "00b53514",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b53518",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b53534",
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

- 旧版 [`00b53478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53468.md#insn-00b53478) · [`00b5347c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53468.md#insn-00b5347c) · [`00b53498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53468.md#insn-00b53498)

~~~diff
- 00b53478 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b53478 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b53478 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b53478 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53478 bytes f44f05a9
- 00b5347c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5347c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5347c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b5347c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5347c bytes fd7b06a9
- 00b53498 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b53498 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b53498 bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a357cc191c9338621d74a21e3c6a119f"></a>

### [`00b53750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53750.md) → [`00b537ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b537ec.md) _ZN8firebase4util31JavaObjectListToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5abb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abb0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ac80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.89% / 新版 83.89%

CFGの説明率　旧版 22.92% / 新版 24.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53844"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b538e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53870"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b53828",
      "READ",
      [
        "storage",
        "01125c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b538cc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53874"
      ]
    ],
    [
      "unmatched:00b53870",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53a0c"
      ]
    ]
  ],
  "added": [
    [
      "00b53828",
      "READ",
      [
        "storage",
        "01125d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b538cc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53910"
      ]
    ],
    [
      "00b5390c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53a0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53750.md#insn-00b53794) · [`00b537a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53750.md#insn-00b537a8) · [`00b53818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53750.md#insn-00b53818)
- 新版 [`00b53830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b537ec.md#insn-00b53830) · [`00b53844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b537ec.md#insn-00b53844) · [`00b538b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b537ec.md#insn-00b538b4)

~~~diff
- 00b53794 ["INT_ADD", "register:40f0:8", ["const:b53794:8", "const:4:8"]]
- 00b53794 ["CALL", null, ["callee:005762f8:8"]]
+ 00b53830 ["INT_ADD", "register:40f0:8", ["const:b53830:8", "const:4:8"]]
+ 00b53830 ["CALL", null, ["callee:005762f8:8"]]
- 00b53794 bytes c98ae897
+ 00b53830 bytes b28ae897
- 00b537a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b537a8 ["INT_ADD", "register:40f0:8", ["const:b537a8:8", "const:4:8"]]
- 00b537a8 ["CALLIND", null, ["register:0:8"]]
+ 00b53844 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53844 ["INT_ADD", "register:40f0:8", ["const:b53844:8", "const:4:8"]]
+ 00b53844 ["CALLIND", null, ["register:0:8"]]
- 00b537a8 bytes 00013fd6
+ 00b53844 bytes 00013fd6
- 00b53818 ["INT_ADD", "register:40f0:8", ["const:b53818:8", "const:4:8"]]
- 00b53818 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00b538b4 ["INT_ADD", "register:40f0:8", ["const:b538b4:8", "const:4:8"]]
+ 00b538b4 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b53818 bytes e61c0494
+ 00b538b4 bytes f31c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39e3dc208be61e25e7eed1b28c6f7099"></a>

### [`00b539a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b539a4.md) → [`00b53a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53a40.md) _ZN8firebase4util17JniObjectToStringEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md) [`00c5b5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5aff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aff0.md) [`00c5b690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b690.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.55% / 新版 79.55%

CFGの説明率　旧版 14.29% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b539a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b539a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b539a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b539a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b539a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b539ac",
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
      "00b53a40",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b53a44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b53a48",
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

- 旧版 [`00b539a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b539a4.md#insn-00b539a4) · [`00b539a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b539a4.md#insn-00b539a8) · [`00b539ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b539a4.md#insn-00b539ac)

~~~diff
- 00b539a4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b539a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b539a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b539a4 bytes f50f1df8
- 00b539a8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b539a8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b539a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b539a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b539a8 bytes f44f01a9
- 00b539ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b539ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b539ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b539ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b539ac bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-860b6d56106a684fc3daad4f3ca7e29c"></a>

### [`00b53a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53a54.md) → [`00b53af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53af0.md) _ZN8firebase4util21JavaListToVariantListEP7_JNIEnvPNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEEP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b4a0.md) · 呼出先 8件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md)
- 新版 呼出元 1件 [`00c5b570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b570.md) · 呼出先 8件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.88% / 新版 82.88%

CFGの説明率　旧版 40.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53a88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b53b24"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53ab4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53a88",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b53b2c",
      "READ",
      [
        "storage",
        "01125c00",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53ab4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53b74"
      ]
    ]
  ],
  "added": [
    [
      "00b53b24",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b53b2c",
      "READ",
      [
        "storage",
        "01125d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53b50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53b74"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53a54.md#insn-00b53a88) · [`00b53a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53a54.md#insn-00b53a98) · [`00b53aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53a54.md#insn-00b53aac)
- 新版 [`00b53b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53af0.md#insn-00b53b34)

~~~diff
- 00b53a88 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b53a88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b53a88 bytes e80f00f9
- 00b53a98 ["INT_ADD", "register:40f0:8", ["const:b53a98:8", "const:4:8"]]
- 00b53a98 ["CALL", null, ["callee:005762f8:8"]]
+ 00b53b34 ["INT_ADD", "register:40f0:8", ["const:b53b34:8", "const:4:8"]]
+ 00b53b34 ["CALL", null, ["callee:005762f8:8"]]
- 00b53a98 bytes 088ae897
+ 00b53b34 bytes f189e897
- 00b53aac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53aac ["INT_ADD", "register:40f0:8", ["const:b53aac:8", "const:4:8"]]
- 00b53aac ["CALLIND", null, ["register:0:8"]]
- 00b53aac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e541bec7fff0dbacac9f948a3ffa359"></a>

### [`00b53c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53c10.md) → [`00b53cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53cac.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE7reserveEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b630.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5b700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b700.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 77.46% / 新版 77.46%

CFGの説明率　旧版 30.00% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53c58"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53cdc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53c44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53db0"
      ]
    ],
    [
      "unmatched:00b53c58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53dc4"
      ]
    ],
    [
      "unmatched:00b53cdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53d94"
      ]
    ]
  ],
  "added": [
    [
      "00b53ce0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53db0"
      ]
    ],
    [
      "00b53cf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53dc4"
      ]
    ],
    [
      "00b53d78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53d94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53c10.md#insn-00b53c44) · [`00b53c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53c10.md#insn-00b53c58) · [`00b53c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53c10.md#insn-00b53c70)
- 新版 [`00b53d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53cac.md#insn-00b53d0c)

~~~diff
- 00b53c44 ["CBRANCH", null, ["local:b14:8", "register:102:1"]]
- 00b53c44 bytes 82060054
- 00b53c58 ["CBRANCH", null, ["local:b15:8", "register:102:1"]]
- 00b53c58 bytes 82060054
- 00b53c70 ["INT_ADD", "register:40f0:8", ["const:b53c70:8", "const:4:8"]]
- 00b53c70 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b53d0c ["INT_ADD", "register:40f0:8", ["const:b53d0c:8", "const:4:8"]]
+ 00b53d0c ["CALL", null, ["callee:00c57f60:8"]]
- 00b53c70 bytes 88100494
+ 00b53d0c bytes 95100494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-002de4af12e6c07935ff39fc5bd62da3"></a>

### [`00b53dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53dc0.md) → [`00b53e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53e5c.md) _ZN8firebase4util8IsJArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 85.37% / 新版 85.37%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b53dec",
      "incomplete_value": true,
      "site": "00b53df4",
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
    "new": {
      "definition_site": "00b53e8c",
      "incomplete_value": true,
      "site": "00b53e90",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": {
      "definition_site": "00b53df0",
      "incomplete_value": true,
      "site": "00b53df4",
      "value": [
        "live",
        "register:4000:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b53de4",
      "incomplete_value": true,
      "site": "00b53df4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:968:8"
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
      "00b53e80",
      "READ",
      [
        "storage",
        "01125968",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53e20",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b53e4c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b53e80",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53ebc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b53ee8",
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

- 旧版 [`00b53df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53dc0.md#insn-00b53df4) · [`00b53e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53dc0.md#insn-00b53e20) · [`00b53e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53dc0.md#insn-00b53e4c)
- 新版 [`00b53e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53e5c.md#insn-00b53e90)

~~~diff
- 00b53df4 ["INT_ADD", "register:40f0:8", ["const:b53df4:8", "const:4:8"]]
- 00b53df4 ["CALL", null, ["callee:00497a88:8"]]
+ 00b53e90 ["INT_ADD", "register:40f0:8", ["const:b53e90:8", "const:4:8"]]
+ 00b53e90 ["CALL", null, ["callee:00497a88:8"]]
- 00b53df4 bytes 150fe597
+ 00b53e90 bytes fe0ee597
- 00b53e20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53e20 ["INT_ADD", "register:40f0:8", ["const:b53e20:8", "const:4:8"]]
- 00b53e20 ["CALLIND", null, ["register:0:8"]]
- 00b53e20 bytes 00013fd6
- 00b53e4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53e4c ["INT_ADD", "register:40f0:8", ["const:b53e4c:8", "const:4:8"]]
- 00b53e4c ["CALLIND", null, ["register:0:8"]]
- 00b53e4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f74a5d298672c71e6ac8fdf79e63d514"></a>

### [`00b53e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53e64.md) → [`00b53f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53f00.md) _ZN8firebase4util16JObjectClassNameEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5aff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aff0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53f28",
      "incomplete_value": true,
      "site": "00b53f34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53e8c",
      "incomplete_value": true,
      "site": "00b53e98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:970:8"
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
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b53edc",
      "incomplete_value": true,
      "site": "00b53ee4",
      "value": [
        "live",
        "register:4098:8"
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
      "00b53f28",
      "READ",
      [
        "storage",
        "01125970",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53f28",
      "READ",
      [
        "storage",
        "01125a70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53e64.md#insn-00b53e98) · [`00b53ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53e64.md#insn-00b53ee4) · [`00b53e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53e64.md#insn-00b53e84)
- 新版 [`00b53f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53f00.md#insn-00b53f34) · [`00b53f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53f00.md#insn-00b53f80) · [`00b53f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53f00.md#insn-00b53f20)

~~~diff
- 00b53e98 ["INT_ADD", "register:40f0:8", ["const:b53e98:8", "const:4:8"]]
- 00b53e98 ["CALL", null, ["callee:00497874:8"]]
+ 00b53f34 ["INT_ADD", "register:40f0:8", ["const:b53f34:8", "const:4:8"]]
+ 00b53f34 ["CALL", null, ["callee:00497874:8"]]
- 00b53e98 bytes 670ee597
+ 00b53f34 bytes 500ee597
- 00b53ee4 ["INT_ADD", "register:40f0:8", ["const:b53ee4:8", "const:4:8"]]
- 00b53ee4 ["CALL", null, ["callee:00c5aff0:8"]]
+ 00b53f80 ["INT_ADD", "register:40f0:8", ["const:b53f80:8", "const:4:8"]]
+ 00b53f80 ["CALL", null, ["callee:00c5aff0:8"]]
- 00b53ee4 bytes 0f1c0494
+ 00b53f80 bytes 1c1c0494
- 00b53e84 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b53e84 ["INT_ADD", "register:40f0:8", ["const:b53e84:8", "const:4:8"]]
- 00b53e84 ["CALLIND", null, ["register:0:8"]]
+ 00b53f20 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b53f20 ["INT_ADD", "register:40f0:8", ["const:b53f20:8", "const:4:8"]]
+ 00b53f20 ["CALLIND", null, ["register:0:8"]]
- 00b53e84 bytes 20013fd6
+ 00b53f20 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6e14359839f699a858e475a28556ea0"></a>

### [`00b53f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53f08.md) → [`00b53fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53fa4.md) _ZN8firebase4util14JBooleanToBoolEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b2e0.md) · 呼出先 1件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md)
- 新版 呼出元 1件 [`00c5b3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b3b0.md) · 呼出先 1件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 48.15% / 新版 48.15%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53f08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53f08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53f0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53f08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53f0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b53fb4",
      "READ",
      [
        "storage",
        "01125898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53fa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b53fa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b53fb4",
      "READ",
      [
        "storage",
        "01125998",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53f08.md#insn-00b53f08) · [`00b53f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53f08.md#insn-00b53f0c) · [`00b53f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53f08.md#insn-00b53f20)
- 新版 [`00b53fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53fa4.md#insn-00b53fbc)

~~~diff
- 00b53f08 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b53f08 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b53f08 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b53f08 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b53f08 bytes f44fbea9
- 00b53f0c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b53f0c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b53f0c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b53f0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53f0c bytes fd7b01a9
- 00b53f20 ["INT_ADD", "register:40f0:8", ["const:b53f20:8", "const:4:8"]]
- 00b53f20 ["CALL", null, ["callee:00497a88:8"]]
+ 00b53fbc ["INT_ADD", "register:40f0:8", ["const:b53fbc:8", "const:4:8"]]
+ 00b53fbc ["CALL", null, ["callee:00497a88:8"]]
- 00b53f20 bytes ca0ee597
+ 00b53fbc bytes b30ee597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15a92375d8513963f979c5eca362d3ba"></a>

### [`00b53f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53f74.md) → [`00b54010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54010.md) _ZN8firebase4util12JByteToUInt8EP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b200.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53fa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b54044"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54020",
      "incomplete_value": true,
      "site": "00b54028",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53f84",
      "incomplete_value": true,
      "site": "00b53f8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
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
      "00b54020",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53fa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53fcc"
      ]
    ],
    [
      "unmatched:00b53fcc",
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
      "00b54020",
      "READ",
      [
        "storage",
        "01125a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54044",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54068"
      ]
    ],
    [
      "00b54068",
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

- 旧版 [`00b53f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53f74.md#insn-00b53f8c) · [`00b53fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53f74.md#insn-00b53fa0) · [`00b53fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53f74.md#insn-00b53fa8)
- 新版 [`00b54028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54010.md#insn-00b54028)

~~~diff
- 00b53f8c ["INT_ADD", "register:40f0:8", ["const:b53f8c:8", "const:4:8"]]
- 00b53f8c ["CALL", null, ["callee:00c5b2d0:8"]]
+ 00b54028 ["INT_ADD", "register:40f0:8", ["const:b54028:8", "const:4:8"]]
+ 00b54028 ["CALL", null, ["callee:00c5b2d0:8"]]
- 00b53f8c bytes 9d1c0494
+ 00b54028 bytes aa1c0494
- 00b53fa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53fa0 ["INT_ADD", "register:40f0:8", ["const:b53fa0:8", "const:4:8"]]
- 00b53fa0 ["CALLIND", null, ["register:0:8"]]
- 00b53fa0 bytes 00013fd6
- 00b53fa8 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b53fa8 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1454f4b4905559d6ba0b7fa340f865d"></a>

### [`00b53fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53fdc.md) → [`00b54078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54078.md) _ZN7_JNIEnv14CallByteMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b200.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5b2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2d0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 56.41% / 新版 56.41%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53fe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53fe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53fe4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53fe0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53fe4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5402c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5407c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b54080",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b540c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53fdc.md#insn-00b53fe0) · [`00b53fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53fdc.md#insn-00b53fe4) · [`00b5402c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53fdc.md#insn-00b5402c)

~~~diff
- 00b53fe0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b53fe0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b53fe0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00b53fe0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53fe0 bytes fc4f10a9
- 00b53fe4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b53fe4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b53fe4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00b53fe4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53fe4 bytes fd7b11a9
- 00b5402c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b5402c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00b5402c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b5402c bytes ab831ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d11735143d85641de6591b06f4cf1a46"></a>

### [`00b54078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54078.md) → [`00b54114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54114.md) _ZN8firebase4util11JCharToCharEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54124",
      "incomplete_value": true,
      "site": "00b5412c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54088",
      "incomplete_value": true,
      "site": "00b54090",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:948:8"
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
      "site": "00b540a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b540bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b54124",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b540a4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b540bc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54124",
      "READ",
      [
        "storage",
        "01125a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54140",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b54158",
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

- 旧版 [`00b54090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54078.md#insn-00b54090) · [`00b540a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54078.md#insn-00b540a4) · [`00b540bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54078.md#insn-00b540bc)
- 新版 [`00b5412c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54114.md#insn-00b5412c)

~~~diff
- 00b54090 ["INT_ADD", "register:40f0:8", ["const:b54090:8", "const:4:8"]]
- 00b54090 ["CALL", null, ["callee:00c5b2e0:8"]]
+ 00b5412c ["INT_ADD", "register:40f0:8", ["const:b5412c:8", "const:4:8"]]
+ 00b5412c ["CALL", null, ["callee:00c5b2e0:8"]]
- 00b54090 bytes 601c0494
+ 00b5412c bytes 6d1c0494
- 00b540a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b540a4 ["INT_ADD", "register:40f0:8", ["const:b540a4:8", "const:4:8"]]
- 00b540a4 ["CALLIND", null, ["register:0:8"]]
- 00b540a4 bytes 00013fd6
- 00b540bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b540bc ["INT_ADD", "register:40f0:8", ["const:b540bc:8", "const:4:8"]]
- 00b540bc ["CALLIND", null, ["register:0:8"]]
- 00b540bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-535cfea1758a77cc981797fba9a7dc87"></a>

### [`00b5417c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b5417c.md) → [`00b54218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54218.md) _ZN8firebase4util13JShortToInt16EP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b220.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b5418c",
      "incomplete_value": true,
      "site": "00b54194",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "site": "00b541a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b541c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b54228",
      "READ",
      [
        "storage",
        "01125cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b541a8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b541c0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54228",
      "READ",
      [
        "storage",
        "01125dc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54244",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b5425c",
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

- 旧版 [`00b54194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b5417c.md#insn-00b54194) · [`00b541a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b5417c.md#insn-00b541a8) · [`00b541c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b5417c.md#insn-00b541c0)
- 新版 [`00b54230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54218.md#insn-00b54230)

~~~diff
- 00b54194 ["INT_ADD", "register:40f0:8", ["const:b54194:8", "const:4:8"]]
- 00b54194 ["CALL", null, ["callee:00c5b2f0:8"]]
+ 00b54230 ["INT_ADD", "register:40f0:8", ["const:b54230:8", "const:4:8"]]
+ 00b54230 ["CALL", null, ["callee:00c5b2f0:8"]]
- 00b54194 bytes 231c0494
+ 00b54230 bytes 301c0494
- 00b541a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b541a8 ["INT_ADD", "register:40f0:8", ["const:b541a8:8", "const:4:8"]]
- 00b541a8 ["CALLIND", null, ["register:0:8"]]
- 00b541a8 bytes 00013fd6
- 00b541c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b541c0 ["INT_ADD", "register:40f0:8", ["const:b541c0:8", "const:4:8"]]
- 00b541c0 ["CALLIND", null, ["register:0:8"]]
- 00b541c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-435fe391068b079f26c91ca143810b92"></a>

### [`00b544cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b544cc.md) → [`00b54568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54568.md) _ZN8firebase4util15IsJBooleanArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_call_alignment

命令の説明率　旧版 76.67% / 新版 76.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b544f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b545ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b545cc",
      "incomplete_value": true,
      "site": "00b545dc",
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
      "unmatched:00b544e8",
      "PARAM",
      [
        "storage",
        "002abf8e",
        null,
        null
      ]
    ],
    [
      "unmatched:00b544f4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54584",
      "PARAM",
      [
        "storage",
        "002abf32",
        null,
        null
      ]
    ],
    [
      "00b545ac",
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

- 旧版 [`00b544f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b544cc.md#insn-00b544f4) · [`00b544e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b544cc.md#insn-00b544e8)
- 新版 [`00b545ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54568.md#insn-00b545ac)

~~~diff
- 00b544f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b544f4 ["INT_ADD", "register:40f0:8", ["const:b544f4:8", "const:4:8"]]
- 00b544f4 ["CALLIND", null, ["register:0:8"]]
- 00b544f4 bytes 00013fd6
+ 00b545ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b545ac ["INT_ADD", "register:40f0:8", ["const:b545ac:8", "const:4:8"]]
+ 00b545ac ["CALLIND", null, ["register:0:8"]]
+ 00b545ac bytes 00013fd6
- 00b544e8 ["COPY", "tmp:0:8", ["const:f8e:8"]]
- 00b544e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b544e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b544e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b544e8 bytes 21383e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec26f2065d3f171cb2f8cc913f4df816"></a>

### [`00b54544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54544.md) → [`00b545e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b545e0.md) _ZN8firebase4util12IsJByteArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 76.67% / 新版 76.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b545fc",
      "incomplete_value": false,
      "site": "00b54608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54560",
      "incomplete_value": false,
      "site": "00b5456c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:db4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54588"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b545a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54560",
      "PARAM",
      [
        "storage",
        "002bbdb4",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54588",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b545a4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b545fc",
      "PARAM",
      [
        "storage",
        "002bbd60",
        null,
        null
      ]
    ],
    [
      "00b54624",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b54640",
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

- 旧版 [`00b5456c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54544.md#insn-00b5456c) · [`00b54588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54544.md#insn-00b54588) · [`00b545a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54544.md#insn-00b545a4)
- 新版 [`00b54608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b545e0.md#insn-00b54608)

~~~diff
- 00b5456c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5456c ["INT_ADD", "register:40f0:8", ["const:b5456c:8", "const:4:8"]]
- 00b5456c ["CALLIND", null, ["register:0:8"]]
+ 00b54608 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b54608 ["INT_ADD", "register:40f0:8", ["const:b54608:8", "const:4:8"]]
+ 00b54608 ["CALLIND", null, ["register:0:8"]]
- 00b5456c bytes 00013fd6
+ 00b54608 bytes 00013fd6
- 00b54588 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54588 ["INT_ADD", "register:40f0:8", ["const:b54588:8", "const:4:8"]]
- 00b54588 ["CALLIND", null, ["register:0:8"]]
- 00b54588 bytes 00013fd6
- 00b545a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b545a4 ["INT_ADD", "register:40f0:8", ["const:b545a4:8", "const:4:8"]]
- 00b545a4 ["CALLIND", null, ["register:0:8"]]
- 00b545a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-845244b361fee5981125a6b05399050e"></a>

### [`00b54634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54634.md) → [`00b546d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b546d0.md) _ZN8firebase4util13IsJShortArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b546ec",
      "incomplete_value": false,
      "site": "00b546f8",
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
            "const:5fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54650",
      "incomplete_value": false,
      "site": "00b5465c",
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
            "const:5cb:8"
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
      "site": "00b546a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b54744"
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
      "unmatched:00b54650",
      "PARAM",
      [
        "storage",
        "002b45cb",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b546ec",
      "PARAM",
      [
        "storage",
        "002b45fc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54634.md#insn-00b5465c) · [`00b546a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54634.md#insn-00b546a8)
- 新版 [`00b546f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b546d0.md#insn-00b546f8) · [`00b54744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b546d0.md#insn-00b54744)

~~~diff
- 00b5465c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5465c ["INT_ADD", "register:40f0:8", ["const:b5465c:8", "const:4:8"]]
- 00b5465c ["CALLIND", null, ["register:0:8"]]
+ 00b546f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b546f8 ["INT_ADD", "register:40f0:8", ["const:b546f8:8", "const:4:8"]]
+ 00b546f8 ["CALLIND", null, ["register:0:8"]]
- 00b5465c bytes 00013fd6
+ 00b546f8 bytes 00013fd6
- 00b546a8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b546a8 ["RETURN", null, ["register:0:8"]]
- 00b546a8 bytes c0035fd6
+ 00b54744 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b54744 ["RETURN", null, ["register:0:8"]]
+ 00b54744 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ba8d9e1725bbecb74c8e04f453095eb"></a>

### [`00b54814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54814.md) → [`00b548b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b548b0.md) _ZN8firebase4util14IsJDoubleArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b548cc",
      "incomplete_value": false,
      "site": "00b548d8",
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
            "const:561:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54830",
      "incomplete_value": false,
      "site": "00b5483c",
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
            "const:532:8"
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
      "00b548cc",
      "PARAM",
      [
        "storage",
        "002a9532",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b548cc",
      "PARAM",
      [
        "storage",
        "002a9561",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5483c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54814.md#insn-00b5483c) · [`00b54830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54814.md#insn-00b54830) · [`00b54858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54814.md#insn-00b54858)
- 新版 [`00b548d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b548b0.md#insn-00b548d8) · [`00b548cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b548b0.md#insn-00b548cc) · [`00b548f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b548b0.md#insn-00b548f4)

~~~diff
- 00b5483c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5483c ["INT_ADD", "register:40f0:8", ["const:b5483c:8", "const:4:8"]]
- 00b5483c ["CALLIND", null, ["register:0:8"]]
+ 00b548d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b548d8 ["INT_ADD", "register:40f0:8", ["const:b548d8:8", "const:4:8"]]
+ 00b548d8 ["CALLIND", null, ["register:0:8"]]
- 00b5483c bytes 00013fd6
+ 00b548d8 bytes 00013fd6
- 00b54830 ["COPY", "tmp:0:8", ["const:532:8"]]
- 00b54830 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b54830 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b54830 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b548cc ["COPY", "tmp:0:8", ["const:561:8"]]
+ 00b548cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b548cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b548cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b54830 bytes 21c81491
+ 00b548cc bytes 21841591
- 00b54858 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54858 ["INT_ADD", "register:40f0:8", ["const:b54858:8", "const:4:8"]]
- 00b54858 ["CALLIND", null, ["register:0:8"]]
+ 00b548f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b548f4 ["INT_ADD", "register:40f0:8", ["const:b548f4:8", "const:4:8"]]
+ 00b548f4 ["CALLIND", null, ["register:0:8"]]
- 00b54858 bytes 00013fd6
+ 00b548f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-485657702eda38b186beaf2ae6edde44"></a>

### [`00b54b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54b8c.md) → [`00b54c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54c28.md) _ZN8firebase4util19JCharArrayToVariantEP7_JNIEnvP11_jcharArray

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3e0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5b4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b4b0.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 9.52% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54b90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54b90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54b94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54b90",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54b94",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54b98",
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
      "00b54c2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b54c30",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b54c34",
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

- 旧版 [`00b54b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54b8c.md#insn-00b54b90) · [`00b54b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54b8c.md#insn-00b54b94) · [`00b54b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54b8c.md#insn-00b54b98)

~~~diff
- 00b54b90 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b54b90 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b54b90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b54b90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54b90 bytes fc6f02a9
- 00b54b94 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b54b94 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b54b94 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b54b94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54b94 bytes fa6703a9
- 00b54b98 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b54b98 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b54b98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b54b98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54b98 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb12263500f28c1263cd6888632b6d0c"></a>

### [`00b54e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54e88.md) → [`00b54f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54f24.md) _ZN8firebase4util18JIntArrayToVariantEP7_JNIEnvP10_jintArray

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3b0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5b480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b480.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 90.53% / 新版 90.53%

CFGの説明率　旧版 23.53% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54fd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b55074"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b54fb0",
      "incomplete_value": true,
      "site": "00b54fb4",
      "value": [
        "INT_LEFT",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:40d0:8"
              ],
              "INT_LEFT"
            ]
          ],
          [
            "leaf",
            "const:3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54f14",
      "incomplete_value": true,
      "site": "00b54f18",
      "value": [
        "live",
        "register:40c0:8"
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
      "unmatched:00b54fd0",
      "READ",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54fd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55098"
      ]
    ],
    [
      "unmatched:00b54fc8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5506c",
      "READ",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b55074",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55098"
      ]
    ],
    [
      "00b55064",
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

- 旧版 [`00b54f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54e88.md#insn-00b54f18) · [`00b54f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54e88.md#insn-00b54f5c) · [`00b54fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54e88.md#insn-00b54fc8)
- 新版 [`00b54fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54f24.md#insn-00b54fb4) · [`00b54ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54f24.md#insn-00b54ff8)

~~~diff
- 00b54f18 ["INT_ADD", "register:40f0:8", ["const:b54f18:8", "const:4:8"]]
- 00b54f18 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b54fb4 ["INT_ADD", "register:40f0:8", ["const:b54fb4:8", "const:4:8"]]
+ 00b54fb4 ["CALL", null, ["callee:00c57f60:8"]]
- 00b54f18 bytes de0b0494
+ 00b54fb4 bytes eb0b0494
- 00b54f5c ["INT_ADD", "register:40f0:8", ["const:b54f5c:8", "const:4:8"]]
- 00b54f5c ["CALL", null, ["callee:00c5a900:8"]]
+ 00b54ff8 ["INT_ADD", "register:40f0:8", ["const:b54ff8:8", "const:4:8"]]
+ 00b54ff8 ["CALL", null, ["callee:00c5a900:8"]]
- 00b54f5c bytes 35160494
+ 00b54ff8 bytes 42160494
- 00b54fc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54fc8 ["INT_ADD", "register:40f0:8", ["const:b54fc8:8", "const:4:8"]]
- 00b54fc8 ["CALLIND", null, ["register:0:8"]]
- 00b54fc8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccd5bd61df1fe468648dc507f418ba99"></a>

### [`00b55004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55004.md) → [`00b550a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b550a0.md) _ZN8firebase4util19JLongArrayToVariantEP7_JNIEnvP11_jlongArray

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3f0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5b4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b4c0.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 96.84% / 新版 96.84%

CFGの説明率　旧版 31.25% / 新版 29.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b550b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b55150"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55174"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b550b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55140"
      ]
    ]
  ],
  "added": [
    [
      "00b55150",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55140"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b550b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55004.md#insn-00b550b4) · [`00b550d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55004.md#insn-00b550d8)
- 新版 [`00b55174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b550a0.md#insn-00b55174) · [`00b55150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b550a0.md#insn-00b55150)

~~~diff
- 00b550b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b550b4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b550b4 bytes 81ffff54
- 00b550d8 ["INT_ADD", "register:40f0:8", ["const:b550d8:8", "const:4:8"]]
- 00b550d8 ["CALL", null, ["callee:00c5a900:8"]]
+ 00b55174 ["INT_ADD", "register:40f0:8", ["const:b55174:8", "const:4:8"]]
+ 00b55174 ["CALL", null, ["callee:00c5a900:8"]]
- 00b550d8 bytes d6150494
+ 00b55174 bytes e3150494
+ 00b55150 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b55150 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b55150 bytes 81ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96094a6c80fa6314a2fb8c73cf18e140"></a>

### [`00b55308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55308.md) → [`00b553a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b553a4.md) _ZN8firebase4util21JDoubleArrayToVariantEP7_JNIEnvP13_jdoubleArray

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b480.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5b550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b550.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.63% / 新版 92.63%

CFGの説明率　旧版 33.33% / 新版 35.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55320"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55320"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5533c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55320",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5533c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55364",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b553bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b553d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b55400",
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

- 旧版 [`00b55320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55308.md#insn-00b55320) · [`00b5533c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55308.md#insn-00b5533c) · [`00b55364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55308.md#insn-00b55364)

~~~diff
- 00b55320 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b55320 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b55320 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b55320 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55320 bytes fd7b07a9
- 00b5533c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b5533c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b5533c bytes e90f00f9
- 00b55364 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55364 ["INT_ADD", "register:40f0:8", ["const:b55364:8", "const:4:8"]]
- 00b55364 ["CALLIND", null, ["register:0:8"]]
- 00b55364 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-499aeff55ede0edca57ec5e1e9b4ba15"></a>

### [`00b55484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55484.md) → [`00b55520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55520.md) _ZN8firebase4util21JObjectArrayToVariantEP7_JNIEnvP13_jobjectArray

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b490.md) · 呼出先 7件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b410.md)
- 新版 呼出元 1件 [`00c5b560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b560.md) · 呼出先 7件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b4e0.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 30.77% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5552c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b555c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b55504",
      "incomplete_value": true,
      "site": "00b5550c",
      "value": [
        "live",
        "register:8:8"
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
      "unmatched:00b5552c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5561c"
      ]
    ],
    [
      "unmatched:00b55544",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b555c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5561c"
      ]
    ],
    [
      "00b555e0",
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

- 旧版 [`00b5550c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55484.md#insn-00b5550c) · [`00b5552c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55484.md#insn-00b5552c) · [`00b55544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55484.md#insn-00b55544)
- 新版 [`00b555a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55520.md#insn-00b555a8)

~~~diff
- 00b5550c ["INT_ADD", "register:40f0:8", ["const:b5550c:8", "const:4:8"]]
- 00b5550c ["CALL", null, ["callee:00c5a900:8"]]
+ 00b555a8 ["INT_ADD", "register:40f0:8", ["const:b555a8:8", "const:4:8"]]
+ 00b555a8 ["CALL", null, ["callee:00c5a900:8"]]
- 00b5550c bytes c9140494
+ 00b555a8 bytes d6140494
- 00b5552c ["CBRANCH", null, ["local:b8:8", "register:102:1"]]
- 00b5552c bytes a2020054
- 00b55544 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55544 ["INT_ADD", "register:40f0:8", ["const:b55544:8", "const:4:8"]]
- 00b55544 ["CALLIND", null, ["register:0:8"]]
- 00b55544 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a51129271d073e2e0417c29ab6a52d21"></a>

### [`00b555d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b555d4.md) → [`00b55670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55670.md) _ZN8firebase4util15JArrayToVariantEP7_JNIEnvP7_jarray

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b300.md) · 呼出先 11件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3b0.md) [`00c5b3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3d0.md) [`00c5b3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3e0.md)
- 新版 呼出元 1件 [`00c5b3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b3d0.md) · 呼出先 11件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b480.md) [`00c5b4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b4a0.md) [`00c5b4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b4b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 73.43% / 新版 73.43%

CFGの説明率　旧版 35.48% / 新版 37.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 12件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b556c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55738"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b557a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b556a0",
      "READ",
      [
        "storage",
        "01125968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55708",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5567c"
      ]
    ],
    [
      "unmatched:00b55674",
      "PARAM",
      [
        "storage",
        "002a4d9b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b556a0",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55708",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55718"
      ]
    ],
    [
      "00b55710",
      "PARAM",
      [
        "storage",
        "002a4d3f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b555fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b555d4.md#insn-00b555fc) · [`00b55614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b555d4.md#insn-00b55614) · [`00b55628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b555d4.md#insn-00b55628)
- 新版 [`00b556b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55670.md#insn-00b556b0)

~~~diff
- 00b555fc ["COPY", "register:0:8", ["register:4048:8"]]
- 00b555fc ["INT_ADD", "register:40f0:8", ["const:b555fc:8", "const:4:8"]]
- 00b555fc ["CALLIND", null, ["register:0:8"]]
- 00b555fc bytes 20013fd6
- 00b55614 ["INT_ADD", "register:40f0:8", ["const:b55614:8", "const:4:8"]]
- 00b55614 ["CALL", null, ["callee:00497a88:8"]]
+ 00b556b0 ["INT_ADD", "register:40f0:8", ["const:b556b0:8", "const:4:8"]]
+ 00b556b0 ["CALL", null, ["callee:00497a88:8"]]
- 00b55614 bytes 0d09e597
+ 00b556b0 bytes f608e597
- 00b55628 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55628 ["INT_ADD", "register:40f0:8", ["const:b55628:8", "const:4:8"]]
- 00b55628 ["CALLIND", null, ["register:0:8"]]
- 00b55628 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32c076222d972541e7a93ff93c1aa46d"></a>

### [`00b55a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55a74.md) → [`00b55b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55b10.md) _ZN8firebase4util14JniUriToStringEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b2f0.md) · 呼出先 3件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md) [`00c5b5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5c0.md)
- 新版 呼出元 1件 [`00c5b3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b3c0.md) · 呼出先 3件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5aff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aff0.md) [`00c5b690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b690.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55ab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b55b54"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b55b2c",
      "incomplete_value": true,
      "site": "00b55b38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b55a90",
      "incomplete_value": true,
      "site": "00b55a9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
      "00b55b2c",
      "READ",
      [
        "storage",
        "01125d30",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b55ab8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55b78"
      ]
    ],
    [
      "unmatched:00b55b30",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b55b2c",
      "READ",
      [
        "storage",
        "01125e30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55b54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55b78"
      ]
    ],
    [
      "00b55bcc",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55a74.md#insn-00b55a9c) · [`00b55ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55a74.md#insn-00b55ab0) · [`00b55ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55a74.md#insn-00b55ab8)
- 新版 [`00b55b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55b10.md#insn-00b55b38)

~~~diff
- 00b55a9c ["INT_ADD", "register:40f0:8", ["const:b55a9c:8", "const:4:8"]]
- 00b55a9c ["CALL", null, ["callee:00497874:8"]]
+ 00b55b38 ["INT_ADD", "register:40f0:8", ["const:b55b38:8", "const:4:8"]]
+ 00b55b38 ["CALL", null, ["callee:00497874:8"]]
- 00b55a9c bytes 6607e597
+ 00b55b38 bytes 4f07e597
- 00b55ab0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55ab0 ["INT_ADD", "register:40f0:8", ["const:b55ab0:8", "const:4:8"]]
- 00b55ab0 ["CALLIND", null, ["register:0:8"]]
- 00b55ab0 bytes 00013fd6
- 00b55ab8 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00b55ab8 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d567cee159ebfcc22990d90dc1785917"></a>

### [`00b55b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55b3c.md) → [`00b55bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55bd8.md) _ZN8firebase4util13CharsToJniUriEP7_JNIEnvPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b2b0.md) · 呼出先 2件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md)
- 新版 呼出元 1件 [`00c5b380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b380.md) · 呼出先 2件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 88.41% / 新版 88.41%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b55b60",
      "incomplete_value": true,
      "site": "00b55b6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6f8:8"
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
    "new": null,
    "old": {
      "definition_site": "00b55b64",
      "incomplete_value": true,
      "site": "00b55b6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:708:8"
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
    "new": {
      "definition_site": "00b55c30",
      "incomplete_value": true,
      "site": "00b55c38",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
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
      "unmatched:00b55b60",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b55b64",
      "READ",
      [
        "storage",
        "01125708",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55c24",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b55bfc",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55c00",
      "READ",
      [
        "storage",
        "01125808",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55c24",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55b3c.md#insn-00b55b6c) · [`00b55b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55b3c.md#insn-00b55b84) · [`00b55b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55b3c.md#insn-00b55b9c)
- 新版 [`00b55c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55bd8.md#insn-00b55c08) · [`00b55c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55bd8.md#insn-00b55c20) · [`00b55c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55bd8.md#insn-00b55c38)

~~~diff
- 00b55b6c ["INT_ADD", "register:40f0:8", ["const:b55b6c:8", "const:4:8"]]
- 00b55b6c ["CALL", null, ["callee:00589734:8"]]
+ 00b55c08 ["INT_ADD", "register:40f0:8", ["const:b55c08:8", "const:4:8"]]
+ 00b55c08 ["CALL", null, ["callee:00589734:8"]]
- 00b55b6c bytes e2cee897
+ 00b55c08 bytes cbcee897
- 00b55b84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55b84 ["INT_ADD", "register:40f0:8", ["const:b55b84:8", "const:4:8"]]
- 00b55b84 ["CALLIND", null, ["register:0:8"]]
+ 00b55c20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55c20 ["INT_ADD", "register:40f0:8", ["const:b55c20:8", "const:4:8"]]
+ 00b55c20 ["CALLIND", null, ["register:0:8"]]
- 00b55b84 bytes 00013fd6
+ 00b55c20 bytes 00013fd6
- 00b55b9c ["INT_ADD", "register:40f0:8", ["const:b55b9c:8", "const:4:8"]]
- 00b55b9c ["CALL", null, ["callee:00497874:8"]]
+ 00b55c38 ["INT_ADD", "register:40f0:8", ["const:b55c38:8", "const:4:8"]]
+ 00b55c38 ["CALL", null, ["callee:00497874:8"]]
- 00b55b9c bytes 2607e597
+ 00b55c38 bytes 0f07e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcfc434e62fa3737eb492146ea588224"></a>

### [`00b55c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55c50.md) → [`00b55cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55cec.md) _ZN8firebase4util14ParseUriStringEP7_JNIEnvPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 75.61% / 新版 75.61%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b55c78",
      "incomplete_value": true,
      "site": "00b55c8c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d20:8"
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
    "new": null,
    "old": {
      "definition_site": "00b55c7c",
      "incomplete_value": true,
      "site": "00b55c8c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d38:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b55d24",
      "incomplete_value": true,
      "site": "00b55d28",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": {
      "definition_site": "00b55c88",
      "incomplete_value": true,
      "site": "00b55c8c",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55c78",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b55c7c",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b55ca0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b55d14",
      "READ",
      [
        "storage",
        "01125e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55d18",
      "READ",
      [
        "storage",
        "01125e38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55d3c",
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

- 旧版 [`00b55c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55c50.md#insn-00b55c8c) · [`00b55ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55c50.md#insn-00b55ca0) · [`00b55cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55c50.md#insn-00b55cb8)
- 新版 [`00b55d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55cec.md#insn-00b55d28)

~~~diff
- 00b55c8c ["INT_ADD", "register:40f0:8", ["const:b55c8c:8", "const:4:8"]]
- 00b55c8c ["CALL", null, ["callee:00c5ac70:8"]]
+ 00b55d28 ["INT_ADD", "register:40f0:8", ["const:b55d28:8", "const:4:8"]]
+ 00b55d28 ["CALL", null, ["callee:00c5ac70:8"]]
- 00b55c8c bytes c5130494
+ 00b55d28 bytes d2130494
- 00b55ca0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55ca0 ["INT_ADD", "register:40f0:8", ["const:b55ca0:8", "const:4:8"]]
- 00b55ca0 ["CALLIND", null, ["register:0:8"]]
- 00b55ca0 bytes 00013fd6
- 00b55cb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55cb8 ["INT_ADD", "register:40f0:8", ["const:b55cb8:8", "const:4:8"]]
- 00b55cb8 ["CALLIND", null, ["register:0:8"]]
- 00b55cb8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bc618f8f6e364ecd49878e071fdc114"></a>

### [`00b55cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55cf4.md) → [`00b55d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55d90.md) _ZN8firebase4util10CharsToURLEP7_JNIEnvPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.93% / 新版 82.93%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55cf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55cf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55cf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55cf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55cf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55cfc",
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
      "00b55d90",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b55d94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b55d98",
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

- 旧版 [`00b55cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55cf4.md#insn-00b55cf4) · [`00b55cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55cf4.md#insn-00b55cf8) · [`00b55cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55cf4.md#insn-00b55cfc)

~~~diff
- 00b55cf4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b55cf4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b55cf4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b55cf4 bytes f50f1df8
- 00b55cf8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b55cf8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b55cf8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b55cf8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55cf8 bytes f44f01a9
- 00b55cfc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b55cfc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b55cfc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b55cfc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55cfc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c96ac24b2e6fc55062ae690deadba3cd"></a>

### [`00b55d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55d98.md) → [`00b55e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55e34.md) _ZN8firebase4util20JniByteArrayToVectorEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b470.md) · 呼出先 1件 [`00c5b660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b660.md)
- 新版 呼出元 1件 [`00c5b540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b540.md) · 呼出先 1件 [`00c5b730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b730.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 75.76% / 新版 75.76%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b55e70",
      "incomplete_value": true,
      "site": "00b55e74",
      "value": [
        "live",
        "register:40a8:8"
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
      "definition_site": "00b55e6c",
      "incomplete_value": true,
      "site": "00b55e74",
      "value": [
        "INT_SEXT",
        "8",
        [
          [
            "live",
            "register:40b0:4"
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
      "site": "00b55df8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55e10",
      "READ",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55df8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b55eac",
      "READ",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b55e94",
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

- 旧版 [`00b55dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55d98.md#insn-00b55dd8) · [`00b55df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55d98.md#insn-00b55df8)
- 新版 [`00b55e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55e34.md#insn-00b55e74) · [`00b55e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55e34.md#insn-00b55e94)

~~~diff
- 00b55dd8 ["INT_ADD", "register:40f0:8", ["const:b55dd8:8", "const:4:8"]]
- 00b55dd8 ["CALL", null, ["callee:00c5b730:8"]]
+ 00b55e74 ["INT_ADD", "register:40f0:8", ["const:b55e74:8", "const:4:8"]]
+ 00b55e74 ["CALL", null, ["callee:00c5b730:8"]]
- 00b55dd8 bytes 22160494
+ 00b55e74 bytes 2f160494
- 00b55df8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55df8 ["INT_ADD", "register:40f0:8", ["const:b55df8:8", "const:4:8"]]
- 00b55df8 ["CALLIND", null, ["register:0:8"]]
- 00b55df8 bytes 00013fd6
+ 00b55e94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55e94 ["INT_ADD", "register:40f0:8", ["const:b55e94:8", "const:4:8"]]
+ 00b55e94 ["CALLIND", null, ["register:0:8"]]
+ 00b55e94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58fd723fa282eaa187607e8538d8a491"></a>

### [`00b55ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55ea4.md) → [`00b55f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55f40.md) _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5af40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af40.md) · 呼出先 6件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md)
- 新版 呼出元 1件 [`00c5b010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b010.md) · 呼出先 6件 [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.62% / 新版 74.62%

CFGの説明率　旧版 31.71% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55eb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55eb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55f9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55eb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55ec8",
      "PARAM",
      [
        "storage",
        "01125d88",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55ee4",
      "READ",
      [
        "storage",
        "01125d80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b55f54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b55f64",
      "PARAM",
      [
        "storage",
        "01125e88",
        null,
        null
      ]
    ],
    [
      "00b55f80",
      "READ",
      [
        "storage",
        "01125e80",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55ea4.md#insn-00b55eb8) · [`00b55edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55ea4.md#insn-00b55edc) · [`00b55ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55ea4.md#insn-00b55ef0)
- 新版 [`00b55f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55f40.md#insn-00b55f78)

~~~diff
- 00b55eb8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b55eb8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b55eb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b55eb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55eb8 bytes fd7b05a9
- 00b55edc ["INT_ADD", "register:40f0:8", ["const:b55edc:8", "const:4:8"]]
- 00b55edc ["CALL", null, ["callee:00c5b770:8"]]
+ 00b55f78 ["INT_ADD", "register:40f0:8", ["const:b55f78:8", "const:4:8"]]
+ 00b55f78 ["CALL", null, ["callee:00c5b770:8"]]
- 00b55edc bytes f1150494
+ 00b55f78 bytes fe150494
- 00b55ef0 ["INT_EQUAL", "tmp:0:1", ["register:40d8:8", "const:0:8"]]
- 00b55ef0 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b55ef0 bytes 1b0200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-855c0a3fc402c424a101ef30ba3cd238"></a>

### [`00b560ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b560ac.md) → [`00b56148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b56148.md) _ZN8firebase4util32JniResultCallback_nativeOnResultEP7_JNIEnvP8_jobjectS4_hhP8_jstringll

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aff0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.47% / 新版 64.47%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b560b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b560b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b560b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b560b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b560b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b560b8",
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
      "00b5614c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b56150",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b56154",
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

- 旧版 [`00b560b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b560ac.md#insn-00b560b0) · [`00b560b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b560ac.md#insn-00b560b4) · [`00b560b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b560ac.md#insn-00b560b8)

~~~diff
- 00b560b0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b560b0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b560b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b560b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b560b0 bytes fc6f02a9
- 00b560b4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b560b4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b560b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b560b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b560b4 bytes fa6703a9
- 00b560b8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b560b8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b560b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b560b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b560b8 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10e792a35f6348ee640972b92960548d"></a>

### [`00b561ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b561ec.md) → [`00b56288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b56288.md) _ZN8firebase4util17JavaThreadContext6CancelEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5b1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 63.33% / 新版 63.33%

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
      "site": "00b561ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b561f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b561f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b561ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b561f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b562a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b56258"
      ]
    ]
  ],
  "added": [
    [
      "00b56288",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5628c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b562a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b562f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b561ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b561ec.md#insn-00b561ec) · [`00b561f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b561ec.md#insn-00b561f0) · [`00b56214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b561ec.md#insn-00b56214)
- 新版 [`00b562b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b56288.md#insn-00b562b0)

~~~diff
- 00b561ec ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b561ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b561ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b561ec bytes f30f1ef8
- 00b561f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b561f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b561f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b561f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b561f0 bytes fd7b01a9
- 00b56214 ["INT_ADD", "register:40f0:8", ["const:b56214:8", "const:4:8"]]
- 00b56214 ["CALL", null, ["callee:00574d2c:8"]]
+ 00b562b0 ["INT_ADD", "register:40f0:8", ["const:b562b0:8", "const:4:8"]]
+ 00b562b0 ["CALL", null, ["callee:00574d2c:8"]]
- 00b56214 bytes b67ae897
+ 00b562b0 bytes 9f7ae897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-315676fb5d5fbd06c17fd0c1be6c8b95"></a>

### [`00b56264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56264.md) → [`00b56300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b56300.md) _ZN8firebase4util17JavaThreadContext24ReleaseExecuteCancelLockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5b1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56268"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56268"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56264",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56268",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b56320",
      "READ",
      [
        "storage",
        "01125698",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b56300",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b56304",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b56320",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b56264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56264.md#insn-00b56264) · [`00b56268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56264.md#insn-00b56268) · [`00b5628c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56264.md#insn-00b5628c)
- 新版 [`00b56328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b56300.md#insn-00b56328)

~~~diff
- 00b56264 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b56264 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b56264 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b56264 bytes f30f1ef8
- 00b56268 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b56268 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b56268 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b56268 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56268 bytes fd7b01a9
- 00b5628c ["INT_ADD", "register:40f0:8", ["const:b5628c:8", "const:4:8"]]
- 00b5628c ["CALL", null, ["callee:00574d2c:8"]]
+ 00b56328 ["INT_ADD", "register:40f0:8", ["const:b56328:8", "const:4:8"]]
+ 00b56328 ["CALL", null, ["callee:00574d2c:8"]]
- 00b5628c bytes 987ae897
+ 00b56328 bytes 817ae897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95c31a6a640f5c67433b090a16a6c927"></a>

### [`00b562dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b562dc.md) → [`00b56378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b56378.md) _ZN8firebase4util17JavaThreadContext24AcquireExecuteCancelLockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c5b1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00c5b2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2b0.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 12.50% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56398",
      "incomplete_value": true,
      "site": "00b563a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b562fc",
      "incomplete_value": true,
      "site": "00b56304",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6a0:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5631c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56344"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b56398",
      "READ",
      [
        "storage",
        "011256a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5631c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b56344",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b56398",
      "READ",
      [
        "storage",
        "011257a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b563b8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b563e0",
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

- 旧版 [`00b56304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b562dc.md#insn-00b56304) · [`00b5631c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b562dc.md#insn-00b5631c) · [`00b56344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b562dc.md#insn-00b56344)
- 新版 [`00b563a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b56378.md#insn-00b563a0)

~~~diff
- 00b56304 ["INT_ADD", "register:40f0:8", ["const:b56304:8", "const:4:8"]]
- 00b56304 ["CALL", null, ["callee:00497a88:8"]]
+ 00b563a0 ["INT_ADD", "register:40f0:8", ["const:b563a0:8", "const:4:8"]]
+ 00b563a0 ["CALL", null, ["callee:00497a88:8"]]
- 00b56304 bytes d105e597
+ 00b563a0 bytes ba05e597
- 00b5631c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5631c ["INT_ADD", "register:40f0:8", ["const:b5631c:8", "const:4:8"]]
- 00b5631c ["CALLIND", null, ["register:0:8"]]
- 00b5631c bytes 00013fd6
- 00b56344 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b56344 ["INT_ADD", "register:40f0:8", ["const:b56344:8", "const:4:8"]]
- 00b56344 ["CALLIND", null, ["register:0:8"]]
- 00b56344 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35b56690c5a18d09417709526d63fb07"></a>

### [`00b56360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56360.md) → [`00b563fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b563fc.md) _ZN8firebase4util17JavaThreadContext9TerminateEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b380.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5b450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b450.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 21.13% / 新版 21.13%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5639c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b563ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56418"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b56410",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56418",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b563f0"
      ]
    ],
    [
      "00b56420",
      "READ",
      [
        "storage",
        "01125680",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b56410",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56418",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5648c"
      ]
    ],
    [
      "00b56420",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5637c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56360.md#insn-00b5637c) · [`00b56388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56360.md#insn-00b56388) · [`00b56398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56360.md#insn-00b56398)
- 新版 [`00b56418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b563fc.md#insn-00b56418)

~~~diff
- 00b5637c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5637c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b56418 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b56418 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b5637c bytes a10300b4
+ 00b56418 bytes a10300b4
- 00b56388 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b56388 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b56388 bytes c8000034
- 00b56398 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b56398 ["INT_ADD", "register:40f0:8", ["const:b56398:8", "const:4:8"]]
- 00b56398 ["CALLIND", null, ["register:0:8"]]
- 00b56398 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c40890d0f5c66d35b5818ec1eec1bac"></a>

### [`00b5647c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b5647c.md) → [`00b56518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b56518.md) _ZN8firebase4util17JavaThreadContext13SetupInstanceEP7_JNIEnvPFvPvES4_S6_PS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5b180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b180.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5b250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b250.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 14.29% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56540",
      "incomplete_value": true,
      "site": "00b5654c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b564a4",
      "incomplete_value": true,
      "site": "00b564b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:678:8"
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
      "definition_site": "00b56544",
      "incomplete_value": true,
      "site": "00b5654c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:788:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b564a8",
      "incomplete_value": true,
      "site": "00b564b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:688:8"
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
      "definition_site": "00b564a0",
      "incomplete_value": true,
      "site": "00b564b0",
      "value": [
        "live",
        "register:4008:8"
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
      "unmatched:00b564a4",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b564a8",
      "READ",
      [
        "storage",
        "01125688",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b564c4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b56540",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56544",
      "READ",
      [
        "storage",
        "01125788",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56560",
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

- 旧版 [`00b564b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b5647c.md#insn-00b564b0) · [`00b564c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b5647c.md#insn-00b564c4) · [`00b564fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b5647c.md#insn-00b564fc)
- 新版 [`00b5654c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b56518.md#insn-00b5654c) · [`00b56598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b56518.md#insn-00b56598)

~~~diff
- 00b564b0 ["INT_ADD", "register:40f0:8", ["const:b564b0:8", "const:4:8"]]
- 00b564b0 ["CALL", null, ["callee:00589734:8"]]
+ 00b5654c ["INT_ADD", "register:40f0:8", ["const:b5654c:8", "const:4:8"]]
+ 00b5654c ["CALL", null, ["callee:00589734:8"]]
- 00b564b0 bytes 91cce897
+ 00b5654c bytes 7acce897
- 00b564c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b564c4 ["INT_ADD", "register:40f0:8", ["const:b564c4:8", "const:4:8"]]
- 00b564c4 ["CALLIND", null, ["register:0:8"]]
- 00b564c4 bytes 00013fd6
- 00b564fc ["INT_ADD", "register:40f0:8", ["const:b564fc:8", "const:4:8"]]
- 00b564fc ["CALL", null, ["callee:00c5b250:8"]]
+ 00b56598 ["INT_ADD", "register:40f0:8", ["const:b56598:8", "const:4:8"]]
+ 00b56598 ["CALL", null, ["callee:00c5b250:8"]]
- 00b564fc bytes 21130494
+ 00b56598 bytes 2e130494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1737064b79be2b5558d21f64398c0682"></a>

### [`00b56514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56514.md) → [`00b565b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b565b0.md) _ZN8firebase4util17JavaThreadContext15RunOnMainThreadEP7_JNIEnvP8_jobjectPFvPvES6_S8_PS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b360.md) · 呼出先 3件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5b180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b180.md) [`00c5b240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b240.md)
- 新版 呼出元 1件 [`00c5b430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b430.md) · 呼出先 3件 [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5b250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b250.md) [`00c5b310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b310.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 60.94% / 新版 60.94%

CFGの説明率　旧版 7.14% / 新版 7.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56568"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b565d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b56604"
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
      "unmatched:00b56540",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b56544",
      "READ",
      [
        "storage",
        "01125688",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b56568",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56628"
      ]
    ]
  ],
  "added": [
    [
      "00b565dc",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b565e0",
      "READ",
      [
        "storage",
        "01125788",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56604",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56628"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5654c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56514.md#insn-00b5654c) · [`00b56568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56514.md#insn-00b56568) · [`00b56578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56514.md#insn-00b56578)
- 新版 [`00b565e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b565b0.md#insn-00b565e8)

~~~diff
- 00b5654c ["INT_ADD", "register:40f0:8", ["const:b5654c:8", "const:4:8"]]
- 00b5654c ["CALL", null, ["callee:00589734:8"]]
+ 00b565e8 ["INT_ADD", "register:40f0:8", ["const:b565e8:8", "const:4:8"]]
+ 00b565e8 ["CALL", null, ["callee:00589734:8"]]
- 00b5654c bytes 6acce897
+ 00b565e8 bytes 53cce897
- 00b56568 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b56568 bytes 20010054
- 00b56578 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b56578 ["INT_ADD", "register:40f0:8", ["const:b56578:8", "const:4:8"]]
- 00b56578 ["CALLIND", null, ["register:0:8"]]
- 00b56578 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1a618ca244b3f707d188c759e956ff8"></a>

### [`00b56614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56614.md) → [`00b566b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b566b0.md) _ZN8firebase4util17JavaThreadContext21RunOnBackgroundThreadEP7_JNIEnvPFvPvES4_S6_PS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b370.md) · 呼出先 3件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5b180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b180.md) [`00c5b240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b240.md)
- 新版 呼出元 1件 [`00c5b440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b440.md) · 呼出先 3件 [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5b250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b250.md) [`00c5b310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b310.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.19% / 新版 74.19%

CFGの説明率　旧版 14.29% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56618"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56614",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56618",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5661c",
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
      "00b566b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b566b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b566b8",
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

- 旧版 [`00b56614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56614.md#insn-00b56614) · [`00b56618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56614.md#insn-00b56618) · [`00b5661c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56614.md#insn-00b5661c)

~~~diff
- 00b56614 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b56614 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b56614 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b56614 bytes f50f1df8
- 00b56618 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b56618 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b56618 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b56618 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56618 bytes f44f01a9
- 00b5661c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5661c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5661c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5661c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5661c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98ae18bfd56539106daa063865d0a260"></a>

### [`00b56714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56714.md) → [`00b567b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b567b0.md) _ZN8firebase4util9FindClassEP7_JNIEnvPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b570.md) · 呼出先 1件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md)
- 新版 呼出元 1件 [`00c5b640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b640.md) · 呼出先 1件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.58% / 新版 52.58%

CFGの説明率　旧版 6.90% / 新版 6.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56714"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56714"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56718"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56714",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56718",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5671c",
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
      "00b567b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b567b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b567b8",
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

- 旧版 [`00b56714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56714.md#insn-00b56714) · [`00b56718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56714.md#insn-00b56718) · [`00b5671c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56714.md#insn-00b5671c)

~~~diff
- 00b56714 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b56714 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b56714 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b56714 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b56714 bytes f85fbca9
- 00b56718 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b56718 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b56718 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b56718 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56718 bytes f65701a9
- 00b5671c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5671c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5671c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5671c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5671c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40130174949ba4b43ca8e12f05d864bf"></a>

### [`00b56898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56898.md) → [`00b56934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b56/00b56934.md) _ZN8firebase4util16FindClassInFilesEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b330.md) · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5b400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b400.md) · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.09% / 新版 70.09%

CFGの説明率　旧版 13.33% / 新版 13.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_condition` 5件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 18件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5689c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5689c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b568c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5689c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b568c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b568cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56974"
      ]
    ]
  ],
  "added": [
    [
      "00b56938",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b5695c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b56968",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56974"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5689c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56898.md#insn-00b5689c) · [`00b568c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56898.md#insn-00b568c0) · [`00b568cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56898.md#insn-00b568cc)

~~~diff
- 00b5689c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b5689c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b5689c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b5689c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5689c bytes fc6f0aa9
- 00b568c0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b568c0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa8:8"]]
- 00b568c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b568c0 bytes a8831af8
- 00b568cc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b568cc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b568cc bytes 61000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-113278289a66660a02fdd7701f6b1752"></a>

### [`00b56f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56f98.md) → [`00b57034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57034.md) _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_S6_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b670.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5b740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b740.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.89% / 新版 82.89%

CFGの説明率　旧版 14.29% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56f98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56f98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56f9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56f98",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56f9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56fa0",
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
      "00b57034",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b57038",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5703c",
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

- 旧版 [`00b56f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56f98.md#insn-00b56f98) · [`00b56f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56f98.md#insn-00b56f9c) · [`00b56fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b56f98.md#insn-00b56fa0)

~~~diff
- 00b56f98 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b56f98 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b56f98 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b56f98 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b56f98 bytes f85fbca9
- 00b56f9c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b56f9c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b56f9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b56f9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56f9c bytes f65701a9
- 00b56fa0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b56fa0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b56fa0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b56fa0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56fa0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20d2fa2a59eda1d51b6f95a631abb2a6"></a>

### [`00b570c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b570c8.md) → [`00b57164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57164.md) _ZN8firebase4util25GetResourceIdFromActivityEP7_JNIEnvP8_jobjectPKcNS0_12ResourceTypeE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 68.18% / 新版 68.18%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 6件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57110"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57160"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b571f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b570e4",
      "READ",
      [
        "storage",
        "01125800",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b57110",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b571d0"
      ]
    ],
    [
      "00b571d4",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b57180",
      "READ",
      [
        "storage",
        "01125900",
        null,
        "undefined8"
      ]
    ],
    [
      "00b571ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b571d0"
      ]
    ],
    [
      "00b571d4",
      "READ",
      [
        "storage",
        "011258f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b570f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b570c8.md#insn-00b570f4) · [`00b57108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b570c8.md#insn-00b57108) · [`00b57110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b570c8.md#insn-00b57110)
- 新版 [`00b57190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57164.md#insn-00b57190)

~~~diff
- 00b570f4 ["INT_ADD", "register:40f0:8", ["const:b570f4:8", "const:4:8"]]
- 00b570f4 ["CALL", null, ["callee:00497874:8"]]
+ 00b57190 ["INT_ADD", "register:40f0:8", ["const:b57190:8", "const:4:8"]]
+ 00b57190 ["CALL", null, ["callee:00497874:8"]]
- 00b570f4 bytes d001e597
+ 00b57190 bytes b901e597
- 00b57108 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b57108 ["INT_ADD", "register:40f0:8", ["const:b57108:8", "const:4:8"]]
- 00b57108 ["CALLIND", null, ["register:0:8"]]
- 00b57108 bytes 00013fd6
- 00b57110 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b57110 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

